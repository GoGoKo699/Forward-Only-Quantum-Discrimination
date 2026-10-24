# Examples and interpretation of the sequence

[Model](model.md) · [Spectral proof](spectral_mechanism.md) · [Finite checks](../verification/README.md)

## A complete two-state example

Take the discrete signal oracle $`U=e^{-iaY_{01}}`$ with $`\sin a=\varepsilon`$, and take it to be the identity on the remaining space. The known kick commutes with this oracle. Hence

```math
(C_Y^\dagger U)^m(C_YU)^m=U^{2m},\qquad
U^{2m}|0\rangle=\cos(2ma)|0\rangle+\sin(2ma)|1\rangle.
```

For $`m=\operatorname{round}(\pi/(4a))`$, the departure probability is $`\sin^2(2ma)`$, close to one. In the null example $`U=I`$, the two blocks cancel exactly. The circuit starts with one computational basis state, uses $`2m`$ forward calls and $`2m`$ known kicks, then measures the system once.

For $`H=\varepsilon X_{01}`$, the same calculation gives departure probability $`\sin^2(2m\varepsilon\tau)`$. This is the simplest view of the signal accumulating coherently. The general proof is needed because an unknown completion need not commute with the kick, preserve the two-state subspace or have a known spectrum.

## Why uncontrolled repetition can fail

A norm neighborhood alone does not make $`U^N|0\rangle`$ a useful amplifier. For a discrete two-state example, take

```math
U=\begin{pmatrix}\cos a&-\sin a\\\sin a&\cos a\end{pmatrix}
\begin{pmatrix}1&0\\0&e^{-ib}\end{pmatrix}.
```

The first column is the required signal column. For $`a+|b|\le c_0`$, the triangle inequality gives $`\|U-I\|\le c_0`$. After removing the global phase $`e^{-ib/2}`$, its determinant is one and its eigenvalues are $`e^{\pm i\omega}`$, where

```math
\cos\omega=\cos a\cos(b/2).
```

The Cayley–Hamilton identity gives the transition amplitude under $`N`$ repetitions as a phase times $`\sin a\,\sin(N\omega)/\sin\omega`$. Therefore, for every integer $`N`$,

```math
|\langle1|U^N|0\rangle|^2
\le\frac{\sin^2a}{\sin^2a+\cos^2a\sin^2(b/2)}.
```

With fixed nonzero $`b`$ inside the norm neighborhood and $`\varepsilon=\sin a\to0`$, this upper bound vanishes as $`O(\varepsilon^2/b^2)`$, regardless of how long one repeats $`U`$. The unknown phase detunes the two levels. The paired controls overcome this nuisance in the stated decision problem.

A Hamiltonian version is

```math
H=\begin{pmatrix}0&\varepsilon\\\varepsilon&b\end{pmatrix},
\qquad 0<b,\quad b+\varepsilon\le\Lambda.
```

Direct diagonalization gives

```math
|\langle1|e^{-itH}|0\rangle|^2
=\frac{4\varepsilon^2}{b^2+4\varepsilon^2}
\sin^2\!\left(\frac{t\sqrt{b^2+4\varepsilon^2}}2\right).
```

At fixed detuning, uninterrupted evolution never reaches a substantial departure probability as the coupling vanishes. This is an explanation of why known interleaving controls matter, not a lower bound against every uncontrolled measurement protocol.

## What the paired controls accomplish

The kick separates two known superpositions spectrally from the rest of the Hilbert space. A small perturbation changes their eigenvectors only slightly. Repeated powers accumulate their exact perturbed eigenphases; the eigenvector mismatch stays bounded independently of the repetition count.

The second block reverses the known kick. At zero signal, reflection of $`|0\rangle`$ exchanges the two blocks and their two distinguished branches. The branch-phase contrast is exactly zero, including every order of the unknown completion. Turning on the signal produces a contrast with a dimension-independent nonzero slope. Thus a long coherent run amplifies the signal without also amplifying an uncontrolled additive offset.

This does not make the full output state exactly return in every null instance: imperfect alignment with the distinguished eigenvectors leaves a bounded leakage contribution. Accordingly, the theorem is two-sided bounded error.

## Why the symmetric kick matters

A small null example separates the exact cancellation from generic paired phase accumulation. Take

```math
H=\begin{pmatrix}0&0&0\\0&0.3&0.4\\0&0.4&-0.2\end{pmatrix},
\qquad \|H\|\simeq0.521699,
\qquad \tau=0.01.
```

Let $`P_\pm`$ project onto $`(|0\rangle\pm|1\rangle)/\sqrt2`$. Compare the asymmetric kick $`V=P_+-iP_--Q`$ from the [eigenphase-engineering construction](../references/RELATED_WORK.md#shin-tong) with $`C=iP_+-iP_--Q`$. Matching the bright branches of each kick and its adjoint gives the following finite calculation:

| Kick | Null phase contrast at the stated step |
|---|---:|
| Asymmetric $`V`$ | Approximately $`-2.60\times10^{-8}`$ |
| Symmetric $`C`$ | Numerically zero within floating-point precision |

The [parity proof](spectral_mechanism.md#lemma-3-exact-null-cancellation) establishes exact zero for $`C`$, for every promised null completion. The computed zero alone would not do so. The asymmetric example shows an additive offset at this fixed step; sufficiently small signals can be smaller than that offset. This illustrates why a promise-specific cancellation is needed to avoid extrapolation. It is not a proof that no alternative processing of the asymmetric construction could solve the decision task.

## Reading the numerical examples

The verification script includes the exact two-state examples, detuned examples and seeded dense completions. It verifies each sampled input's norm and column promises before checking the output. A large number of oracle repetitions is evaluated by matrix powering, not simulated as a long noisy physical experiment.

These checks detect sign, ordering, rounding and implementation errors in finite examples. The uniform statement over arbitrary dimension and every promised completion comes from the written spectral and interpolation proofs.
