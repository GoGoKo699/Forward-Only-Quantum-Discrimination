"""Deterministic finite checks of the paired-kick claims.

The analytical proofs establish the uniform theorems. These checks target
sign/order mistakes, valid-input construction, control compilation and the
specific null-bias distinction from the predecessor's asymmetric kick.
Run from any directory; --record updates the committed numerical reference.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parent
C0 = 0.01
TAU = 0.01
SEED = 10242026


def primitives(d, model, theta=np.pi / 2):
    e0 = np.eye(d, dtype=complex)[:, 0]
    e1 = np.eye(d, dtype=complex)[:, 1]
    g = np.zeros((d, d), complex)
    g[0, 1] = -1j if model == "discrete" else 1
    g[1, 0] = 1j if model == "discrete" else 1
    q = np.eye(d, dtype=complex)
    q[:2, :2] = 0
    p = np.eye(d) - q
    c = np.cos(theta) * p + 1j * np.sin(theta) * g - q
    factor = 1j if model == "discrete" else 1
    bright = [(e0 + sign * factor * e1) / np.sqrt(2) for sign in (1, -1)]
    return e0, e1, g, c, bright


def matched_phases(c, u, bright):
    phases = np.empty((2, 2))
    leakages = []
    for si, cs in enumerate((c, c.conj().T)):
        values, vectors = np.linalg.eig(cs @ u)
        used = set()
        for bi, x in enumerate(bright):
            z = np.vdot(x, cs @ x)
            j = int(np.argmin(abs(values - z)))
            assert j not in used, "Branches collided in finite check"
            used.add(j)
            phase = np.angle(z) + np.angle(values[j] / z)
            phases[bi, si] = phase
            v = vectors[:, j] / np.linalg.norm(vectors[:, j])
            leakage = np.linalg.norm(v - x * np.vdot(x, v))
            leakages.append(float(leakage))
    contrast = float(phases[0].sum() - phases[1].sum())
    return phases, contrast, max(leakages)


def paired_state(c, u, m, e0):
    # Binary matrix powering is independent of the eigenphase approximation.
    return np.linalg.matrix_power(c.conj().T @ u, m) @ (
        np.linalg.matrix_power(c @ u, m) @ e0
    )


def check_instance(model, d, eps, background, theta=np.pi / 2):
    e0, e1, g, c, bright = primitives(d, model, theta)
    signal_phase = np.arcsin(eps) if model == "discrete" else eps * TAU
    m = int(round(np.pi / (4 * signal_phase)))
    gap = min(2 * abs(np.sin(theta)), 2 * abs(np.cos(theta / 2)))
    error_bound = 4 * np.sqrt(2) * C0 / (gap - C0)
    rows = []
    for is_signal in (False, True):
        coupling = eps if is_signal else 0.0
        if model == "discrete":
            v = np.eye(d, dtype=complex)
            v[1:, 1:] = expm(-1j * background)
            u = expm(-1j * np.arcsin(coupling) * g) @ v
            expected = np.sqrt(1 - coupling**2) * e0 + coupling * e1
            assert np.linalg.norm(u @ e0 - expected) < 1e-12
            norm_value = float(np.linalg.norm(u - np.eye(d), 2))
            assert norm_value <= C0 + 1e-13
        else:
            h = np.zeros((d, d), complex)
            h[1:, 1:] = background
            h += coupling * g
            assert np.linalg.norm(h @ e0 - coupling * e1) < 1e-12
            norm_value = float(np.linalg.norm(h, 2))
            assert norm_value <= 1 + 1e-13
            u = expm(-1j * TAU * h)
        assert np.linalg.norm(u.conj().T @ u - np.eye(d)) < 1e-12
        psi = paired_state(c, u, m, e0)
        norm_residual = float(abs(np.linalg.norm(psi) - 1))
        assert norm_residual < 2e-6
        probability = float(np.vdot(psi[1:], psi[1:]).real)
        phases, contrast, leakage = matched_phases(c, u, bright)
        ideal = sum(np.exp(1j * m * phases[bi].sum()) * bright[bi]
                    for bi in (0, 1)) / np.sqrt(2)
        state_error = float(np.linalg.norm(psi - ideal))
        assert leakage <= C0 / (gap - C0) + 1e-10
        assert state_error <= error_bound + 2e-6
        if not is_signal:
            assert abs(contrast) < 1e-12
        standard = abs(theta - np.pi / 2) < 1e-14
        if is_signal:
            assert probability > (0.9 if standard else 0.88)
        else:
            assert probability < (0.002 if standard else 0.004)
        rows.append({"signal": is_signal, "input_norm": norm_value,
                     "departure_probability": probability,
                     "phase_contrast": contrast, "branch_leakage": leakage,
                     "paired_state_error": state_error,
                     "numerical_norm_residual": norm_residual})
    return {"model": model, "dimension": d, "epsilon": eps,
            "theta": float(theta), "forward_queries": 2 * m,
            "hypotheses": rows}


def dense_checks():
    rng = np.random.default_rng(SEED)
    records = []
    for model in ("discrete", "hamiltonian"):
        for d in (3, 12):
            for eps in ((0.005, 0.001, 0.0001) if model == "discrete"
                        else (1.0, 0.001, 0.0001)):
                z = rng.normal(size=(d - 1, d - 1)) + 1j * rng.normal(size=(d - 1, d - 1))
                b = z + z.conj().T
                target_norm = 0.004 if model == "discrete" else 0.8 * (1 - eps)
                b *= target_norm / np.linalg.norm(b, 2)
                records.append(check_instance(model, d, eps, b))
    # Endpoint calibration examples test the separately proved structured family.
    b = np.array([[0.3, 0.4], [0.4, -0.2]], dtype=complex)
    calibration = [check_instance("hamiltonian", 3, 0.001, b, theta)
                   for theta in (np.pi / 3, 2 * np.pi / 3)]
    return records, calibration


def two_state_checks():
    rows = []
    for model in ("discrete", "hamiltonian"):
        eps = 0.001
        e0, _, g, c, _ = primitives(2, model)
        phase = np.arcsin(eps) if model == "discrete" else eps * TAU
        m = int(round(np.pi / (4 * phase)))
        u = expm(-1j * phase * g)
        psi = paired_state(c, u, m, e0)
        expected = float(np.sin(2 * m * phase)**2)
        observed = float(abs(psi[1])**2)
        assert abs(observed - expected) < 1e-8
        b = 0.004 if model == "discrete" else 0.5
        background = np.array([[b]], complex)
        detuned = check_instance(model, 2, eps, background)
        ceiling = (eps**2 / (eps**2 + (1 - eps**2) * np.sin(b / 2)**2)
                   if model == "discrete" else 4 * eps**2 / (b**2 + 4 * eps**2))
        rows.append({"model": model, "rotation_closed_form": expected,
                     "rotation_computed": observed,
                     "uncontrolled_detuned_ceiling": float(ceiling),
                     "paired_detuned_signal_probability": detuned["hypotheses"][1]["departure_probability"]})
    return rows


def compiled_basis_column(n, model, sign, value):
    """Compute an exact monomial control circuit on a basis input.

    The last system bit is the target, the first n-1 bits are controls.
    All work bits start at zero and must return to zero. Global phases in
    the n=1 implementation are chosen to match -C^sign for comparison.
    """
    system = [(value >> (n - 1 - j)) & 1 for j in range(n)]
    bits = system + [0] * max(0, n - 2)
    amp = 1 + 0j
    count = 0

    def flip(j):
        nonlocal count
        bits[j] ^= 1
        count += 1

    def toffoli(a, b, target):
        nonlocal count
        bits[target] ^= bits[a] & bits[b]
        count += 1

    if n == 1:
        if model == "discrete":
            if sign == 1:
                amp *= (-1)**bits[0]
                bits[0] ^= 1
            else:
                bits[0] ^= 1
                amp *= (-1)**bits[0]
            count = 2
        else:
            bits[0] ^= 1
            amp *= -1j if sign == 1 else 1j
            count = 1
    else:
        controls = list(range(n - 1))
        for j in controls:
            flip(j)
        chain = []
        if n == 2:
            flag = 0
        else:
            chain.append((0, 1, n))
            for j in range(2, n - 1):
                chain.append((n + j - 2, j, n + j - 1))
            for gate in chain:
                toffoli(*gate)
            flag = n + n - 3
        target = n - 1
        if model == "discrete":
            if sign == 1:
                amp *= (-1)**(bits[flag] * bits[target])  # CZ, then CNOT: XZ
                bits[target] ^= bits[flag]
            else:
                bits[target] ^= bits[flag]             # CNOT, then CZ: ZX
                amp *= (-1)**(bits[flag] * bits[target])
        else:
            bits[target] ^= bits[flag]
            amp *= (-1j if sign == 1 else 1j)**bits[flag]
        count += 2
        for gate in reversed(chain):
            toffoli(*gate)
        for j in controls:
            flip(j)
    assert not any(bits[n:]), "Work qubits failed to uncompute"
    out = sum(bit << (n - 1 - j) for j, bit in enumerate(bits[:n]))
    return out, amp, count


def gate_checks():
    count = 0
    max_error = 0.0
    for n in range(1, 6):
        d = 2**n
        for model in ("discrete", "hamiltonian"):
            _, _, _, c, _ = primitives(d, model)
            for sign in (1, -1):
                expected = -(c if sign == 1 else c.conj().T)
                actual = np.zeros((d, d), complex)
                for value in range(d):
                    out, phase, gates = compiled_basis_column(n, model, sign, value)
                    actual[out, value] = phase
                    assert gates <= (4 * n - 4 if n >= 2 else 2)
                    count += 1
                error = float(np.linalg.norm(actual - expected, 2))
                assert error < 1e-14
                max_error = max(max_error, error)
    return {"basis_columns_checked": count, "n_range": [1, 5],
            "maximum_operator_error": max_error, "workspace_returned": True}


def null_bias_check():
    h = np.array([[0, 0, 0], [0, 0.3, 0.4], [0, 0.4, -0.2]], complex)
    _, _, _, symmetric, bright = primitives(3, "hamiltonian")
    q = np.diag([0, 0, 1])
    asymmetric = np.outer(bright[0], bright[0].conj()) - 1j * np.outer(bright[1], bright[1].conj()) - q
    u = expm(-1j * TAU * h)
    asym_d = matched_phases(asymmetric, u, bright)[1]
    sym_d = matched_phases(symmetric, u, bright)[1]
    assert np.linalg.norm(h, 2) < 1
    assert abs(sym_d) < 1e-12
    assert 1e-8 < abs(asym_d) < 1e-7
    return {"tau": TAU, "hamiltonian_norm": float(np.linalg.norm(h, 2)),
            "asymmetric_contrast": asym_d, "symmetric_contrast": sym_d}


def compare(expected, actual, path="root"):
    if isinstance(expected, dict):
        assert set(expected) == set(actual), path
        for key in expected:
            compare(expected[key], actual[key], path + "." + key)
    elif isinstance(expected, list):
        assert len(expected) == len(actual), path
        for i, (e, a) in enumerate(zip(expected, actual)):
            compare(e, a, path + f"[{i}]")
    elif isinstance(expected, float):
        assert np.isclose(expected, actual, atol=2e-7, rtol=2e-7), (path, expected, actual)
    else:
        assert expected == actual, (path, expected, actual)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", action="store_true", help="Replace the committed expected numerical record")
    args = parser.parse_args()
    dense, calibration = dense_checks()
    nulls = [row["hypotheses"][0]["departure_probability"] for row in dense]
    signals = [row["hypotheses"][1]["departure_probability"] for row in dense]
    data = {"seed": SEED, "dense_instances": dense, "structured_calibration": calibration,
            "two_state_examples": two_state_checks(), "native_controls": gate_checks(),
            "null_kick_comparison": null_bias_check(),
            "summary": {"dense_pairs": len(dense), "maximum_null_departure": max(nulls),
                        "minimum_signal_departure": min(signals)}}
    target = ROOT / "expected_results.json"
    if args.record:
        target.write_text(json.dumps(data, indent=2) + "\n")
    else:
        compare(json.loads(target.read_text()), data)
    print(json.dumps({"status": "PASS", **data["summary"],
                      "native_basis_columns": data["native_controls"]["basis_columns_checked"],
                      "calibration_endpoint_pairs": len(calibration)}, indent=2))


if __name__ == "__main__":
    main()
