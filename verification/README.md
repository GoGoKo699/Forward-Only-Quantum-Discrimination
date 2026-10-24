# Reproducing the finite checks

[Scientific model](../science/model.md) · [Proof mechanism](../science/spectral_mechanism.md) · [Source comparison](../references/RELATED_WORK.md)

The two uniform discrimination guarantees are analytical. This suite checks concrete failure modes in the formulas and implementation: circuit ordering, signal signs, integer rounding, input-promise construction, exact conditional phases, workspace restoration and the distinction between the two kick choices.

## Environment and command

The recorded run used Python **3.12.14**, NumPy **2.3.5** and SciPy **1.17.0**. From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/check_results.py
```

The script can also be called by absolute path; it resolves its expected output relative to its own location. It performs assertions and compares its numerical results with [expected_results.json](expected_results.json). Normal verification does not rewrite that file. An intentional reference regeneration uses `--record` after reviewing a scientific change.

Expected summary, with small platform-dependent differences in the last digits:

```json
{
  "status": "PASS",
  "dense_pairs": 12,
  "maximum_null_departure": 0.000022512248749134162,
  "minimum_signal_departure": 0.9999152947912973,
  "native_basis_columns": 248,
  "calibration_endpoint_pairs": 2
}
```

The seeded matrices and all relevant parameters are generated in [check_results.py](check_results.py); the seed is `10242026`. No downloaded data, network access, simulator service, QRAM or external oracle is needed to run the finite checks.

## What each check establishes

| Check | Inputs and method | Concrete purpose |
|---|---|---|
| Exact two-state dynamics | One instance of each model, compared with its closed-form rotation probability | Detect sign, block-order and repetition-count mistakes |
| Dense completions | Dimensions 3 and 12; three signal values per model; both hypotheses | Verify norms and exact columns, output gap, isolated-branch leakage and uniform state-error formula in 12 valid instance pairs |
| Endpoint signal domain | Discrete signal 0.005; normalized Hamiltonian signal 1 | Include the declared domain endpoints rather than only asymptotically small signals |
| Detuned examples | Two-state phase detuning and Hamiltonian energy detuning | Compare successful paired discrimination with the analytical ceiling on simple uninterrupted transfer |
| Structured kick calibration | Hamiltonian examples at both ends of the proved angle interval | Check the stated structured corollary in finite instances |
| Native controls | Every data basis column for 1 through 5 qubits, both models and both signs | Check relative phases, identity action on the complement, gate counts and clean-work uncomputation |
| Null kick comparison | The displayed three-dimensional null Hamiltonian at step 0.01 | Reproduce the nonzero asymmetric-kick contrast and the symmetric-kick numerical zero |

Because the compiled controls are monomial matrices, checking all basis columns establishes the full matrix identity for each tested register size by linearity. The reversible ladder argument in [Resources](../science/resources.md) establishes the construction for general register size. The numerical matrix comparison still uses floating-point arithmetic; the conditional Clifford phases in the basis calculation are exact values in $`\{1,-1,i,-i\}`$.

Long powers are evaluated by binary matrix powering. The eigenphase approximation is evaluated separately, so it is not used to manufacture the circuit output against which it is checked. Input norms, columns, unitarity and accumulated numerical norm residuals are checked before interpreting probabilities. The suite uses tolerance $`2\times10^{-7}`$ for cross-platform numerical-record comparisons and separate tighter or claim-specific assertions for branch cancellation and native controls.

## Evidence boundaries

The finite examples do not establish worst-case behavior in arbitrary dimension, prove a lower bound, certify originality, or simulate a noisy physical device. The maximum null departure and minimum signal departure above summarize only the selected examples. The conservative universal bounds remain below 0.002 at the null and above 0.9 at the signal, proved in [Discrete](../science/discrete.md) and [Hamiltonian](../science/Hamiltonian.md).

The symmetric contrast is exactly zero because of the [parity identity](../science/spectral_mechanism.md#lemma-3-exact-null-cancellation); a floating-point zero is only corroboration. The implementation-error budget and approximate-promise statements are derived in [Resources](../science/resources.md), independently of this numerical suite. Source and link checks do not establish how mathematics renders in the hosting interface.
