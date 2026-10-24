# Forward-Only Quantum Discrimination

**When can a weak, known transition be detected optimally without reversing the unknown process?** A global near-identity promise lets a fixed pair of known controls distinguish two promised unitary columns with $`\Theta(1/\varepsilon)`$ forward queries, independently of Hilbert-space dimension. A related Hamiltonian theorem uses one fixed evolution interval and optimal total evolution time.

| Problem | Essential promise | Forward calls | Unknown evolution time |
|---|---|---:|---:|
| Discrete unitary | Known column and $`\lVert U-I\rVert\le0.01`$ | $`\Theta(1/\varepsilon)`$ | Not an assigned resource |
| Hamiltonian | $`H\lvert0\rangle=0`$ or $`\varepsilon\lvert1\rangle`$, $`\lVert H\rVert\le\Lambda`$ | $`\Theta(\Lambda/\varepsilon)`$ | $`\Theta(1/\varepsilon)`$ |

For the Hamiltonian problem every call has duration $`\tau=0.01/\Lambda`$, independent of the signal size. Both results have matching lower bounds. Their unitary-column and Hamiltonian-column promises are distinct.

The algorithm prepares $`|0\rangle`$, applies

```math
(C^\dagger U)^m(CU)^m,
```

then tests for departure from $`|0\rangle`$. The known kick has eigenvalues $`+i,-i,-1`$ on two distinguished superpositions and their complement. A spectral gap controls leakage; a parity symmetry cancels the null eigenphase contrast exactly. The resulting one-run probabilities satisfy $`\Pr(\mathrm{NO}\mid\mathrm{YES})<0.002`$ and $`\Pr(\mathrm{NO}\mid\mathrm{NO})>0.9`$.

The paired-power extraction follows **Shin and Tong's eigenphase engineering**. The contribution here is the promise-specific symmetric cancellation, uniform signal-response proof and resulting discrimination theorems. See [related work](references/RELATED_WORK.md) for the closest results and the limits of this comparison.

## Read the science

Start with the [access model and exact claims](science/model.md), then follow the shared spectral argument into either theorem.

| Question | Authoritative account |
|---|---|
| Why does leakage remain bounded through a long coherent run? | [Spectral mechanism](science/spectral_mechanism.md) |
| How does a norm neighborhood restore optimal forward queries? | [Discrete theorem](science/discrete.md) |
| Why can the Hamiltonian step remain fixed? | [Hamiltonian theorem](science/Hamiltonian.md) |
| Why are these query and time scalings optimal? | [Lower bounds and copy baseline](science/lower_bounds.md) |
| What gates, workspace and precision are required? | [Resources and robustness](science/resources.md) |
| What happens in simple and detuned systems? | [Worked examples](science/examples.md) |
| Which assumptions determine the scope? | [Interpretation](science/interpretation.md) |
| Which ingredients are inherited? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

[llms.txt](llms.txt) maps reader questions to these pages.

## Reproduce the finite checks

From the repository root (tested with Python 3.12):

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/check_results.py
```

The checks cover exact two-state dynamics, valid dense completions, the distinction between symmetric and asymmetric kicks, and native control identities. They support implementation consistency. The uniform guarantees and optimality claims rest on the analytical proofs, not on a finite numerical sweep. See [verification instructions and expected results](verification/README.md).

## Resources and scope

For an $`n`$-qubit computational encoding, each kick has an exact $`O(n)`$ known-gate implementation with $`O(n)`$ reusable clean workspace. There is no QRAM, unknown inverse, controlled unknown query or precision-dependent quantum rotation synthesis. The norm bound, exact column and known direction remain load-bearing promises. Arbitrary per-use errors must shrink with the length of the coherent run, as quantified in the resource account.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
