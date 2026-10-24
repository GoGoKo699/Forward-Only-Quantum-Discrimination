# Spectral mechanism of the paired sequence

Two isolated eigenbranches let a long sequence accumulate phase while its state error stays bounded independently of the number of repetitions. Pairing two known kicks then cancels the nuisance phase exactly at the null hypothesis. The discrete and Hamiltonian proofs use different interpolations to show that the remaining contrast grows linearly with the promised signal.

The uniform-in-power paired extraction is inherited from **Shin and Tong, Lemma 5**; see the [closest-work comparison](../references/RELATED_WORK.md#shin-tong). The promise-specific cancellation and its consequences are developed in [the discrete theorem](discrete.md) and [the fixed-duration Hamiltonian theorem](Hamiltonian.md).

## The two distinguished branches

Let $`|x_+\rangle,|x_-\rangle`$ be known orthonormal states satisfying

```math
|0\rangle=\frac{|x_+\rangle+|x_-\rangle}{\sqrt2}.
```

Write $`P_\sigma=|x_\sigma\rangle\langle x_\sigma|`$, $`Q=I-P_+-P_-`$, and

```math
G=P_+-P_-,\qquad C=iG-Q.
```

The eigenvalues of $`C`$ on the two distinguished states are $`+i`$ and $`-i`$. Its remaining eigenvalue, when $`Q\ne0`$, is $`-1`$. Each distinguished eigenvalue is simple and has separation at least

```math
g=\sqrt2
```

from every other eigenvalue. This lower bound also applies when the Hilbert space has dimension two and $`Q=0`$.

For $`s,\sigma\in\{+1,-1\}`$, the eigenvalue of $`C^s`$ on $`x_\sigma`$ is

```math
z_{\sigma,s}=e^{is\sigma\pi/2}.
```

All norms below are operator norms for operators and Euclidean norms for vectors.

## Lemma 1: isolated eigenvalues and leakage

Let $`A`$ be unitary and satisfy $`\|A-C^s\|\le r<g/2`$. For each $`\sigma`$, there is a unique, algebraically simple eigenvalue $`\lambda_{\sigma,s}`$ of $`A`$ within distance $`r`$ of $`z_{\sigma,s}`$. If $`v_{\sigma,s}`$ is a normalized eigenvector, then

```math
\sqrt{1-|\langle x_\sigma|v_{\sigma,s}\rangle|^2}
\le q(r),\qquad q(r)=\frac{r}{g-r}.
```

### Proof of the spectral count

Put $`B=C^s`$ and $`E=A-B`$. Around a distinguished eigenvalue $`z`$ of $`B`$, take the circle $`\Gamma=\{w:|w-z|=g/2\}`$. Every point on this contour is at distance at least $`g/2`$ from the spectrum of $`B`$. Since $`B`$ is normal,

```math
\|(B-w)^{-1}\|\le \frac{2}{g}.
```

For the straight-line matrix path $`B_t=B+tE`$, $`0\le t\le1`$, the factorization

```math
B_t-w=(B-w)\bigl[I+t(B-w)^{-1}E\bigr]
```

is invertible on $`\Gamma`$, because $`\|t(B-w)^{-1}E\|\le2r/g<1`$. The Riesz projector enclosed by $`\Gamma`$ consequently has constant algebraic rank one. The path need not consist of unitary matrices.

The same resolvent argument shows that every eigenvalue of $`B_t`$ is within distance $`tr`$ of the spectrum of $`B`$. Therefore the unique eigenvalue inside $`\Gamma`$ at $`t=1`$ is within $`r`$ of $`z`$. This establishes the count, simplicity and displacement.

### Proof of the leakage bound

For its normalized eigenvector $`v`$, project

```math
(B-\lambda)v=-Ev
```

onto the orthogonal complement of $`x_\sigma`$. On that complement, every eigenvalue of $`B`$ is at distance at least $`g-r`$ from $`\lambda`$. Thus

```math
\|(I-P_\sigma)v\|\le\frac{r}{g-r}.
```

This is the claimed bound. No assumption is required on the multiplicities of the remaining eigenvalues.

## Lemma 2: powers do not accumulate leakage

Under Lemma 1, every nonnegative integer $`m`$ obeys

```math
\|A^m|x_\sigma\rangle-\lambda_{\sigma,s}^{m}|x_\sigma\rangle\|
\le2q(r).
```

To see this, decompose $`x_\sigma`$ into its component along $`v_{\sigma,s}`$ and an orthogonal remainder $`w`$. The remainder has norm at most $`q(r)`$. Since $`A`$ is unitary, the orthogonal complement of $`v_{\sigma,s}`$ is invariant, and

```math
\|A^m w-\lambda_{\sigma,s}^{m}w\|\le2\|w\|.
```

The error is an eigenvector mismatch. It does not grow with $`m`$.

## Corollary: paired phase accumulation

Let $`V`$ be unitary with $`\|V-I\|\le r<g/2`$, and define

```math
F_+=CV,\qquad F_-=C^\dagger V.
```

For the distinguished eigenvalues write $`\lambda_{\sigma,s}=e^{i\phi_{\sigma,s}}`$. Choose each phase in the interval centered at $`s\sigma\pi/2`$ with radius $`2\arcsin(r/2)`$. These intervals give unambiguous phases near the corresponding unperturbed eigenvalues.

Applying Lemma 2 to each factor, without assuming that $`F_+`$ and $`F_-`$ commute, gives

```math
\left\|F_-^mF_+^m|0\rangle-|\widetilde\psi_m\rangle\right\|
\le E(r),\qquad E(r)=4\sqrt2\,q(r),
```

where

```math
|\widetilde\psi_m\rangle
=\frac{1}{\sqrt2}\sum_{\sigma=\pm1}
 e^{im(\phi_{\sigma,+}+\phi_{\sigma,-})}|x_\sigma\rangle.
```

Define the phase contrast

```math
D=(\phi_{+,+}+\phi_{+,-})-(\phi_{-,+}+\phi_{-,-}).
```

The ideal probability outside $`|0\rangle`$ is exactly

```math
\|(I-|0\rangle\langle0|)|\widetilde\psi_m\rangle\|^2
=\sin^2(mD/2).
```

Projection cannot increase the state-vector error. The actual outside amplitude differs from $`|\sin(mD/2)|`$ by at most $`E(r)`$. In particular:

- If $`D=0`$, the actual outside probability is at most $`E(r)^2`$.
- If $`|\sin(mD/2)|>E(r)`$, the actual outside probability is at least $`\bigl(|\sin(mD/2)|-E(r)\bigr)^2`$.

At $`r=1/100`$, the useful uniform bound is $`E(r)<0.041`$.

## Lemma 3: exact null cancellation

Let $`S=I-2|0\rangle\langle0|`$. The definitions imply

```math
S|x_\sigma\rangle=-|x_{-\sigma}\rangle,\qquad SCS=C^\dagger.
```

If $`V|0\rangle=|0\rangle`$, unitarity implies that $`V`$ is block diagonal on $`|0\rangle\oplus|0\rangle^\perp`$. Hence $`SVS=V`$ and

```math
S(CV)S=C^\dagger V.
```

The distinguished eigenbranches are exchanged:

```math
\lambda_{+,+}=\lambda_{-,-},\qquad
\lambda_{+,-}=\lambda_{-,+}.
```

Their local phase branches are exchanged as well, so $`D=0`$ exactly. The physical outside probability is bounded by $`E(r)^2`$; exact phase cancellation alone does not assert exact return of the physical state.

## Lemma 4: eigenphase derivatives

For a differentiable unitary family $`F(t)`$ with an isolated simple eigenpair $`Fv=e^{i\phi}v`$, write

```math
F'(t)=-iK(t)F(t),\qquad K(t)=K(t)^\dagger.
```

Differentiating the eigenvalue equation and taking its expectation in $`v`$ gives

```math
\phi'(t)=-\langle v(t)|K(t)|v(t)\rangle.
```

The isolated simple eigenvalue has a differentiable phase on any parameter interval where the spectral separation persists. The local phase intervals above fix its branch throughout the interpolations used in the two theorems.

For $`G=P_+-P_-`$, Lemma 1 also gives

```math
|\langle v_{\sigma,s}|G|v_{\sigma,s}\rangle-\sigma|
\le2q(r)^2.
```

More precisely, the expectation for the plus branch lies in $`[1-2q(r)^2,1]`$, and that for the minus branch lies in $`[-1,-1+2q(r)^2]`$. These estimates convert spectral confinement into a dimension-independent bound on the contrast's derivative.
