# Meaning, assumptions and boundaries

[Model and results](model.md) · [Resources and robustness](resources.md) · [Related work](../references/RELATED_WORK.md)

## The access boundary

Knowing the two possible output states does not generally remove the cost of losing inverse queries. The discrete result here adds a global near-identity promise on the entire unknown unitary. Under that promise, a known selective control creates isolated eigenphase branches and an optimal forward-query discriminator.

The norm condition is sufficient, not a classification of all easy oracles. The value $`c_0=0.01`$ is an explicit conservative constant. No sharp threshold or largest admissible neighborhood is established. Query independence from dimension does not imply that controls, system storage or classical descriptions have zero cost.

## Why a fixed Hamiltonian interval is possible

A direct short-time approximation usually has an additive error independent of the weak coupling. Accumulating a signal for time proportional to $`1/\varepsilon`$ can then require a shrinking step. Here the analysis keeps the exact eigenphases of the controlled finite-step evolution. Symmetry makes their relevant contrast vanish exactly at the null hypothesis; a derivative bound controls its change proportionally to the signal.

This is why the same interval $`\tau=0.01/\Lambda`$ works for every $`0<\varepsilon\le\Lambda`$. The number of intervals still diverges as $`\Lambda/\varepsilon`$. The coherent run lasts longer as the signal shrinks, and the supplied sufficient worst-case implementation guarantee uses smaller per-call error allowances.

The Hamiltonian theorem is not obtained by identifying $`H|0\rangle`$ with the first column of its exponential. Those columns contain different information. The separate interpolation proof is essential.

## What is known and what is trusted

The distinguished direction, signal size, operator-norm bound, exact column promise and ability to perform the specified known controls are supplied. The algorithm does not learn an unknown successful direction or validate those promises for free. It returns one decision bit; it does not estimate an arbitrary state, learn all Hamiltonian coefficients or implement an unknown inverse.

In a computational-basis encoding, the selective controls have an exact circuit with linearly many known gates. For other encodings, the cost of preparing, mapping or reflecting about the distinguished states must be charged separately. A description of a state is not automatically an efficient state-preparation circuit.

The interleaving model treats oracle evolution and known controls as separate operations. Applying finite-duration controls while an unknown Hamiltonian remains active is a different physical access model. The explicit worst-case error budget in [Resources](resources.md) describes tolerable deviations from the ideal circuit; it does not establish a device-specific fault-tolerance threshold.

## Relation to prior mechanisms

Eigenphase engineering, paired-power phase accumulation and Floquet sensing precede this result. The scientific addition is the specific symmetry cancellation and uniform decision guarantee under the stated promises, with the discrete query theorem and fixed-clock consequence. The [source comparison](../references/RELATED_WORK.md) gives the relevant tasks, versions and attribution.

The quantum advantage is an oracle-resource statement. No application-level speed comparison against a classical simulation of a supplied circuit or a particular laboratory device is asserted. The examples explain how nuisance detuning can obstruct unassisted coherent transfer, while the theorem handles every completion admitted by its promises.
