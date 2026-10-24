# Related work and attribution

[Scientific model](../science/model.md) · [Bibliography](references.bib)

The comparisons below use the listed primary-source versions, inspected on 24 October 2026. They distinguish inherited methods from the promise-specific results proved here. This is a focused comparison, not an exhaustive certification that no other literature contains the result.

## Shin-Tong

Myeongjin Shin and Yu Tong, [*Hamiltonian Learning and Certification via Eigenphase Engineering*](https://arxiv.org/html/2609.26596v1), arXiv:2609.26596v1 (22 September 2026), §3.1, Lemmas 4–5, Corollary 1 and Theorem 7.

This is the closest methodological predecessor. **Lemma 5 already analyzes the paired ordering $`F_-^mF_+^m`$ and bounds its state error independently of $`m`$.** The isolated-branch phase-accumulation method is inherited and is attributed at the [shared lemma](../science/spectral_mechanism.md). Theorem 7 estimates known-state energy-expectation differences with forward evolution, a logarithmically shrinking grid and high-order extrapolation.

Applying that estimator to $`(|0\rangle\pm|1\rangle)/\sqrt2`$ already handles the Hamiltonian decision task, with those resources. Our addition is a symmetric kick satisfying $`SCS=C^\dagger`$, exact null-contrast cancellation, and a uniform derivative bound in the signal parameter. These give the fixed step for this decision promise and the separate discrete norm-neighborhood theorem. The [null-kick example](../science/examples.md#why-the-symmetric-kick-matters) illustrates why the published asymmetric kick does not automatically have this exact cancellation.

## Wang-Carolan-Childs

Emma Wang, Joseph Carolan and Andrew M. Childs, [*On State Distinguishing Without Inverse Queries*](https://arxiv.org/html/2610.05389v1), arXiv:2610.05389v1 (4 October 2026), Theorems 1.1–1.2 and §1.3.

This work defines the same two column-discrimination tasks. Without the global norm restriction, its discrete forward-query complexity is $`\Theta(\varepsilon^{-2})`$ in sufficiently large dimension; the stated lower-bound regime is $`d=\Omega(\varepsilon^{-8})`$. Its Hamiltonian result achieves $`\Theta(\varepsilon^{-1})`$ total time using arbitrarily short evolution intervals and Zeno projections. It asks how long those intervals may remain.

The new discrete norm promise restricts the permitted completions and excludes the lower-bound construction. The theorem here establishes a sufficient fixed positive interval for the Hamiltonian task, without a sparsity or locality condition. It does not identify the maximal interval. The unitary-column and Hamiltonian-column promises remain distinct, as emphasized in the source.

## Other forward-only lower bounds

Ewin Tang and John Wright, [*Amplitude amplification and estimation require inverses*](https://arxiv.org/abs/2507.23787v2), arXiv:2507.23787v2 (23 April 2026 revision), establishes inverse-free obstructions for generic amplification and estimation. The present known-direction promise is a more restricted decision task; it is not a generic replacement for amplitude amplification.

Richard R. Allen, Matthias C. Caro, Yanlin Chen, Tom Gur and Angus Lowe, [*The power of time reversal in Hamiltonian property testing*](https://arxiv.org/html/2610.04996v1), arXiv:2610.04996v1 (4 October 2026), extends relevant lower bounds to fractional queries and proves time-reversal separations for Hamiltonian testing. Its generic tasks have different promises from the specified known column here. A spectral norm bound alone should not be advertised as defeating those obstructions.

## Fixed minimum evolution times

Myeongjin Shin, Junseo Lee and Changhun Oh, [*Heisenberg-limited Hamiltonian learning without short-time control*](https://arxiv.org/html/2604.27838v1), arXiv:2604.27838v1 (30 April 2026), already establishes constant-minimum-duration learning results, including logarithmically sparse Hamiltonians, with sparsity-dependent tradeoffs more generally.

The present theorem concerns a single known-column decision with an arbitrary dense completion and one fixed primitive duration. It is not the first appearance of Heisenberg scaling with a minimum query duration, and it does not replace a full Hamiltonian-learning guarantee.

## Floquet sensing and branch symmetries

J. E. Lang, R. B. Liu and T. S. Monteiro, [*Dynamical-Decoupling-Based Quantum Sensing: Floquet Spectroscopy*](https://journals.aps.org/prx/pdf/10.1103/PhysRevX.5.041016), *Physical Review X* **5**, 041016 (2015), §II and Appendices A–C.

This work develops repeated Floquet-phase accumulation, overlap-dependent sensing oscillations, higher-dimensional bath formulas and finite-width-pulse analysis. Appendix B relates the CPMG branches through reordered half-period propagators. These are mechanism-level precedents for phase accumulation and branch symmetry.

The result here is a uniform known-column decision guarantee with charged forward queries and a lower bound on useful response for every admitted completion. Our trusted-interleaving oracle model does not inherit the source's physical finite-width-pulse analysis. The focused comparison did not locate the present query theorem in that article.

## Spectral search and dimension-dependent estimation

Avatar Tulsi, [*General framework for quantum search algorithms*](https://arxiv.org/abs/0806.1257v3), arXiv:0806.1257v3 (2009; associated journal article *Physical Review A* **86**, 042331 (2012)), supplies earlier spectral and phase-matching analyses of generalized search. Selective controls and resonant eigenphase transfer are established ideas. The promise and forward-only uniform guarantee here require their own proof.

Kean Chen, [*Inverse-free quantum state estimation with Heisenberg scaling*](https://arxiv.org/html/2510.25750v1), arXiv:2510.25750v1 (2025), gives dimension-dependent forward-only state and amplitude estimation. It establishes that inverse-free inverse-precision scaling is possible in other regimes. The present result removes a dimension factor for a restricted decision promise; it does not provide unrestricted estimation.

## Attribution boundary

The [spectral pages](../science/spectral_mechanism.md) reproduce the elementary proof needed for self-contained use and credit the inherited paired-power method. The exact cancellation, discrete interpolation, fixed-step Hamiltonian response and explicit resource statements have their authoritative homes under [science/](../science/model.md). Numerical comparisons of the kicks illustrate a specific structural difference; they cannot prove originality or replace the analytical result.
