# Discrimination with one fixed Hamiltonian evolution step

A known global norm bound permits one fixed positive query duration, independent of the promised weak coupling, while retaining optimal inverse-coupling total evolution time. The proof treats the exact matrix exponential, including all higher-order contributions to the evolved column.

The algorithm uses the [paired spectral mechanism](spectral_mechanism.md), whose uniform-in-power extraction is inherited from [Shin–Tong](../references/RELATED_WORK.md#shin-tong). An exact parity at zero coupling makes the finite-step contrast error proportional to the coupling.

## Normalized model and theorem

Let $`H`$ be an unknown Hermitian operator on a finite-dimensional Hilbert space, with $`\|H\|\le1`$. Two orthogonal computational basis states $`|0\rangle,|1\rangle`$ are known. For a known $`0<\varepsilon\le1`$, exactly one of the following holds:

```math
\begin{aligned}
\mathrm{YES}:&\quad H|0\rangle=0,\\
\mathrm{NO}:&\quad H|0\rangle=\varepsilon|1\rangle.
\end{aligned}
```

The available unknown primitive is the single forward unitary

```math
U=e^{-i\tau H},\qquad \tau=\frac1{100}.
```

Known gates can be interleaved with these queries. No variable-duration evolution primitive is assumed.

Set

```math
\begin{aligned}
X_{01}&=|0\rangle\langle1|+|1\rangle\langle0|,\\
Q&=I-|0\rangle\langle0|-|1\rangle\langle1|,\\
C&=iX_{01}-Q,\\
|x_\sigma\rangle&=(|0\rangle+\sigma|1\rangle)/\sqrt2,
\qquad \sigma\in\{+1,-1\},\\
m&=\mathrm{round}\!\left(\frac{\pi}{4\varepsilon\tau}\right).
\end{aligned}
```

Either nearest integer is allowed at a tie. Prepare $`|0\rangle`$, apply

```math
(C^\dagger U)^m(CU)^m,
```

in right-to-left order, and output NO precisely when a computational-basis measurement returns a state outside $`|0\rangle`$.

**Theorem.** The YES probability of outputting NO is below $`0.002`$, and the NO probability of outputting NO exceeds $`0.9`$. The algorithm uses exactly $`N=2m`$ queries and $`2m`$ known kicks. Its total unknown evolution time is

```math
T=N\tau\le\frac{\pi}{2\varepsilon}+\tau.
```

The fixed-step query complexity is $`\Theta(1/(\varepsilon\tau))`$, and the total evolution time is $`\Theta(1/\varepsilon)`$, uniformly in dimension. The primitive duration $`\tau`$ remains fixed as $`\varepsilon`$ decreases.

## Null hypothesis

For every input, $`\|e^{-i\tau H}-I\|\le\tau`$. The [paired accumulation corollary](spectral_mechanism.md#corollary-paired-phase-accumulation) therefore bounds the final state error by

```math
E(\tau)=4\sqrt2\frac{\tau}{\sqrt2-\tau}<0.041,
```

uniformly in $`m`$. In the YES case, $`U|0\rangle=|0\rangle`$. The parity lemma gives exact null contrast $`D=0`$, so the outside probability is at most $`E(\tau)^2<0.002`$.

## A uniformly bounded Hamiltonian interpolation

For a NO instance, write

```math
A=H-\varepsilon X_{01},\qquad
H_\lambda=A+\lambda X_{01},\qquad -\varepsilon\le\lambda\le\varepsilon.
```

Hermiticity and the promised first column imply

```math
A=(I-|0\rangle\langle0|)H(I-|0\rangle\langle0|),
```

so $`A|0\rangle=0`$ and $`\|A\|\le1`$. For $`0\le\lambda\le\varepsilon`$, the interpolated operator is a convex combination:

```math
H_\lambda=
\left(1-\frac{\lambda}{\varepsilon}\right)A
+\frac{\lambda}{\varepsilon}H.
```

Hence $`\|H_\lambda\|\le1`$ there. With $`S=I-2|0\rangle\langle0|`$, one also has

```math
SH_\lambda S=H_{-\lambda},
```

which proves the same norm bound for negative $`\lambda`$.

This family is used only for analysis. The circuit queries only the actual primitive at $`\lambda=\varepsilon`$.

Define

```math
F_s(\lambda)=C^s e^{-i\tau H_\lambda},\qquad s\in\{+1,-1\}.
```

Since $`\|F_s(\lambda)-C^s\|\le\tau`$ throughout the interpolation, each distinguished eigenbranch remains simple and its eigenvector leakage is at most

```math
q(\tau)=\frac{\tau}{\sqrt2-\tau}.
```

Choose the eigenphases $`\phi_{\sigma,s}(\lambda)`$ in their fixed local neighborhoods of $`s\sigma\pi/2`$, and define

```math
D(\lambda)=(\phi_{+,+}(\lambda)+\phi_{+,-}(\lambda))
-(\phi_{-,+}(\lambda)+\phi_{-,-}(\lambda)).
```

At $`\lambda=0`$, the primitive $`e^{-i\tau A}`$ fixes $`|0\rangle`$. Therefore $`D(0)=0`$ exactly.

## Exact eigenphase derivatives

Differentiating the matrix exponential gives the left-generator identity

```math
F_s'(\lambda)=-iK_s(\lambda)F_s(\lambda),
```

where

```math
K_s(\lambda)=C^s\left[
\int_0^\tau e^{-iuH_\lambda}X_{01}e^{iuH_\lambda}\,du
\right]C^{-s}.
```

Because $`C`$ commutes with $`X_{01}`$ and $`\|H_\lambda\|\le1`$,

```math
\begin{aligned}
\|K_s(\lambda)-\tau X_{01}\|
&\le\int_0^\tau
\|e^{-iuH_\lambda}X_{01}e^{iuH_\lambda}-X_{01}\|\,du\\
&\le\int_0^\tau 2u\,du=\tau^2.
\end{aligned}
```

The second line follows by integrating the commutator bound $`\|[H_\lambda,X_{01}]\|\le2`$.

The [eigenphase derivative lemma](spectral_mechanism.md#lemma-4-eigenphase-derivatives) and the leakage estimate now give

```math
\left|\phi'_{\sigma,s}(\lambda)+\sigma\tau\right|
\le\tau^2+2\tau q(\tau)^2.
```

Combining the four phase derivatives and integrating from the exact null yields

```math
\left|D(\varepsilon)+4\varepsilon\tau\right|
\le4\varepsilon\tau\left[\tau+2q(\tau)^2\right].
```

The finite-step bias in the contrast is thus bounded relative to the coupling. The global norm bound controls this relative error without a sparsity, locality or dimension assumption on the remaining Hamiltonian entries.

## Success probability and query count

Let $`\rho=\tau+2q(\tau)^2`$. At $`\tau=0.01`$, $`\rho<0.0102`$. Rounding $`m`$ gives $`|4m\varepsilon\tau-\pi|\le2\varepsilon\tau`$, so

```math
|mD(\varepsilon)+\pi|
\le2\varepsilon\tau+(\pi+2\varepsilon\tau)\rho
<0.053.
```

The ideal outside amplitude is at least $`\cos(0.0265)`$. The actual NO detection probability therefore obeys

```math
p_{\mathrm{NO}}
\ge\bigl(\cos(0.0265)-E(\tau)\bigr)^2
>\bigl(\cos(0.0265)-0.041\bigr)^2>0.9.
```

The inequalities can be certified using $`1.414<\sqrt2<1.415`$, $`\pi<22/7`$ and $`\cos x\ge1-x^2/2`$. No numerical simulation enters the guarantee.

Finally,

```math
N=2m\le\frac{\pi}{2\varepsilon\tau}+1,\qquad
T=N\tau\le\frac{\pi}{2\varepsilon}+\tau.
```

## General known norm bound

For a known $`\Lambda>0`$ and $`0<\varepsilon\le\Lambda`$, suppose $`\|H\|\le\Lambda`$ and the same column alternatives hold. Apply the normalized theorem to $`H/\Lambda`$ with coupling $`\varepsilon/\Lambda`$. The required physical query duration is

```math
\tau=\frac{0.01}{\Lambda},
```

and the algorithm uses $`m=\mathrm{round}(\pi/(4\varepsilon\tau))`$. Its resource scaling is

```math
N=\Theta\!\left(\frac{\Lambda}{\varepsilon}\right),\qquad
T=\Theta\!\left(\frac1{\varepsilon}\right).
```

The duration depends on the known global norm bound and remains independent of the signal magnitude.

## Optimality and model boundaries

The pair $`H_0=0`$, $`H_1=\varepsilon X_{01}`$ satisfies the two promises and obeys

```math
\|e^{-i\tau H_1}-e^{-i\tau H_0}\|
=2\sin(\varepsilon\tau/2)\le\varepsilon\tau.
```

The [hybrid lower bound](lower_bounds.md) gives $`\Omega(1/(\varepsilon\tau))`$ fixed-step queries for constant distinguishing advantage. Applying the same argument to the sum of the durations gives the $`\Omega(1/\varepsilon)`$ total-time lower bound.

The access model supplies trusted known controls between exact unknown-evolution queries. A physical model in which the unknown Hamiltonian also acts during finite-duration control gates requires a separate drift-and-control analysis. The theorem establishes a sufficient step $`0.01/\Lambda`$; it does not identify the largest possible step. Its promised direction and coupling are known, and its output is a bounded-error decision. Independent repetition gives failure probability $`\delta`$ with $`O(\log(1/\delta))`$ runs.
