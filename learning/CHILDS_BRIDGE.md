# From Childs's notes to forward-only discrimination

[Learning overview](README.md) · [30-milestone map](MILESTONES.md) · [Scientific model](../science/model.md) · [Repository overview](../README.md)

This bridge develops the project's mechanism from a small rotation, an unknown phase that spoils that rotation, and a known control that restores a useful signal. The full statements and proofs remain in `science/`; the explanations here show how their parts fit together.

## A narrow route through the anchor

The single educational anchor is Andrew M. Childs, **[Lecture Notes on Quantum Algorithms](https://www.cs.umd.edu/~amchilds/qa/qa.pdf)**, dated **17 April 2025**. The [author's page](https://www.cs.umd.edu/~amchilds/qa/) hosts the notes. That PDF address may change its contents over time; the date identifies the version used here.

| Read when needed | Printed pages | Foundation used here |
|---|---:|---|
| [§§1.1–1.4](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=9) | 1–3 | States, circuits, operator norm, reversible work |
| [§1.6](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=11) | 3 | Query count versus circuit size and depth |
| [§2.1, Lemma 2.2](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=15) | 7 | Telescoping implementation errors |
| [§19.3](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=96) | 88–89 | Coherent amplification as an algorithmic resource |
| [§§21.1–21.2](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=105) | 97–98 | Specifying the oracle and counting calls |
| [§17.1](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=81) | 73–74 | Hamiltonian evolution |
| [§23.1, Fact 23.1](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=117) | 109 | State overlap and distinguishing advantage |

[§4.3](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=27), printed page 19, is optional background on eigenphases. This algorithm does not run phase estimation. The standard bit-flip oracle in §21.2 is self-inverse; our unknown unitary has a different access restriction.

The notes supply foundations. This repository supplies the spectral-isolation estimates, exact null parity, two signal interpolations, and the resulting promise-specific algorithm. The paired-power extraction has a separate research ancestry in [Shin–Tong](../references/RELATED_WORK.md#shin-tong), retained in the scientific citations.

## The decision task

An unknown operation acts on a system with two known basis states, called $`|0\rangle`$ and $`|1\rangle`$. We know a small positive amplitude $`\varepsilon`$ and want to decide between

```math
\begin{aligned}
\mathrm{YES}:&\quad U|0\rangle=|0\rangle,\\
\mathrm{NO}:&\quad U|0\rangle=\sqrt{1-\varepsilon^2}|0\rangle+\varepsilon|1\rangle.
\end{aligned}
```

The names YES and NO are fixed conventions: NO means that the transition is present. The entire displayed column, including its phase and direction, is promised. Other columns remain unknown.

If we prepare $`|0\rangle`$, apply $`U`$ once, and measure, the signal produces $`|1\rangle`$ with probability $`\varepsilon^2`$. Independent trials therefore need order $`\varepsilon^{-2}`$ calls for a constant detection probability. Even a joint measurement on independently prepared copies has this scaling, as shown in the [copy baseline](../science/lower_bounds.md#the-independent-copy-baseline).

The algorithm instead reuses one register coherently. The supplied unknown operation is only $`U`$. Although every unitary has a mathematical inverse, its inverse is not an available instruction. Known gates and their inverses can still be implemented. This difference between a mathematical identity and an allowed operation is central to the [access model](../science/model.md#allowed-operations-and-charged-resources).

There is one further input promise:

```math
\|U-I\|\le c_0=0.01,
\qquad 0<\varepsilon\le c_0/2.
```

The norm bound controls the action of $`U-I`$ on every unit vector, not only on $`|0\rangle`$. It allows an arbitrary dense completion within this neighborhood. The algorithm trusts the bound; it does not measure or certify it for free.

## Notation for this project

| Symbol | Meaning |
|---|---|
| $`d`$ | Dimension of the system Hilbert space |
| $`P_j=\lvert j\rangle\langle j\rvert`$ | Projector onto distinguished state $`j`$ |
| $`P=P_0+P_1`$, $`Q=I-P`$ | Distinguished two-state span and its complement |
| $`G`$ | Known two-state generator: $`Y_{01}`$ for the discrete task, $`X_{01}`$ for the Hamiltonian task |
| $`C=iG-Q`$ | Known kick inserted after each unknown query |
| $`m`$, $`N=2m`$ | Calls in each block, and total calls in one run |
| $`x_\sigma`$ | Known eigenvector of $`G`$ with eigenvalue $`\sigma=\pm1`$ |
| $`D`$ | Contrast of the two per-pair branch-phase sums; the total relative phase is $`mD`$ |
| $`\tau`$, $`T=N\tau`$ | Hamiltonian query duration and total unknown-evolution time |

In particular, $`Q`$ is a projector, not the query count. The abstract query theorem permits any finite $`d\ge2`$. The explicit qubit implementation separately assumes a data register of dimension $`2^n`$.

## A complete coherent-rotation example

Start with a case whose unknown completion causes no trouble:

```math
Y_{01}=
\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad
R_a=e^{-iaY_{01}}=
\begin{pmatrix}\cos a&-\sin a\\\sin a&\cos a\end{pmatrix},
\qquad \sin a=\varepsilon.
```

These matrices act on the distinguished span; $`R_a`$ is the identity elsewhere. One call rotates amplitude through angle $`a`$. Successive coherent calls add this angle, so after $`N`$ calls the departure probability is $`\sin^2(Na)`$.

The general algorithm prepares $`|0\rangle`$, applies

```math
(C^\dagger U)^m(CU)^m,
\qquad
C=iY_{01}-Q,
\qquad
m=\mathrm{round}\!\left(\frac{\pi}{4a}\right),
```

then measures whether the system is outside $`|0\rangle`$. The rightmost block is executed first: apply $`U`$ and then $`C`$, repeat $`m`$ times, then apply $`U`$ and $`C^\dagger`$ another $`m`$ times.

For $`U=R_a`$, the kick commutes with the oracle and the known factors cancel:

```math
(C^\dagger R_a)^m(CR_a)^m=R_a^{2m},
\qquad
R_a^{2m}|0\rangle
=\cos(2ma)|0\rangle+\sin(2ma)|1\rangle.
```

Since $`2ma`$ is close to $`\pi/2`$, the final measurement almost certainly detects departure. For example, $`\varepsilon=10^{-3}`$ gives $`m=785`$ and $`N=1570`$. There is one initial preparation and one final measurement. The unknown oracle and the known controls are called many times on the same coherent state.

For the null example $`U=I`$, the two blocks cancel exactly. This example explains the useful inverse-amplitude scaling. The general theorem must establish that an unknown completion cannot destroy it.

## Why repetition alone can fail

Consider a legal completion that adds an unknown phase to the second state:

```math
U=R_a
\begin{pmatrix}1&0\\0&e^{-ib}\end{pmatrix}.
```

Its first column is unchanged. If $`a+|b|\le0.01`$, it also obeys the global norm promise. Yet the phase changes the relation between consecutive small rotations. Define $`\omega`$ through $`\cos\omega=\cos a\cos(b/2)`$. Direct diagonalization gives, for every number of repetitions,

```math
|\langle1|U^N|0\rangle|^2
\le
\frac{\sin^2a}
{\sin^2a+\cos^2a\sin^2(b/2)}.
```

At fixed nonzero $`b`$, this ceiling tends to zero with $`\varepsilon`$. For $`\varepsilon=10^{-4}`$ and $`b=0.005`$, it is below $`0.0016`$: waiting longer cannot turn this particular uncontrolled repetition into a reliable detector.

The phase $`b`$ acts as a detuning. The paired control sequence must remove its harmful contribution without knowing it. [Examples](../science/examples.md#why-uncontrolled-repetition-can-fail) derives this formula and its Hamiltonian counterpart. Neither example is a lower bound against all possible uncontrolled protocols.

## How the kick protects useful eigenvectors

For the discrete task define

```math
|x_\sigma\rangle
=\frac{|0\rangle+i\sigma|1\rangle}{\sqrt2},
\qquad \sigma\in\{+1,-1\}.
```

These are the two eigenvectors of $`Y_{01}`$. The kick has eigenvalues $`+i`$ and $`-i`$ on them and $`-1`$ on the complement. Each useful eigenvalue lies at least $`g=\sqrt2`$ away from every other eigenvalue in the complex plane. This separation is fixed even as the number of unknown dimensions grows.

Because $`U`$ is close to the identity, $`CU`$ is close to $`C`$. Each isolated eigenvector therefore moves only slightly. More precisely, if a unitary $`A`$ satisfies $`\|A-C^s\|\le r<g/2`$, its corresponding normalized eigenvector $`v`$ obeys

```math
\sqrt{1-|\langle x_\sigma|v\rangle|^2}
\le q(r),\qquad q(r)=\frac{r}{g-r}.
```

The [spectral proof](../science/spectral_mechanism.md#lemma-1-isolated-eigenvalues-and-leakage) first establishes that this eigenvalue exists and remains simple, then derives the overlap bound. It does not assume a nondegenerate bath spectrum.

Why is a small eigenvector error useful for a very long sequence? Write $`x_\sigma=\alpha v+w`$, with $`w\perp v`$. If the eigenvalue is $`\lambda`$, then

```math
A^m x_\sigma-\lambda^m x_\sigma
=A^m w-\lambda^m w,
\qquad
\|A^m w-\lambda^m w\|\le2\|w\|\le2q(r).
```

The unwanted component keeps its small norm under exact unitary evolution. It does not get added again on each repetition. This is an approximation of the initial eigenvector alignment, rather than an approximation of every gate.

Apply this argument to both $`F_+=CU`$ and $`F_-=C^\dagger U`$. If their useful eigenphases are $`\phi_{\sigma,+}`$ and $`\phi_{\sigma,-}`$, the output stays within $`E(r)=4\sqrt2q(r)`$ of

```math
|\widetilde\psi_m\rangle
=\frac1{\sqrt2}\sum_{\sigma=\pm1}
e^{im(\phi_{\sigma,+}+\phi_{\sigma,-})}|x_\sigma\rangle.
```

This bound holds without assuming the two blocks commute. The relative phase is measured by

```math
D=(\phi_{+,+}+\phi_{+,-})-(\phi_{-,+}+\phi_{-,-}),
\qquad
p_{\rm ideal}=\sin^2(mD/2).
```

At $`r=0.01`$, the state-vector error is below $`0.041`$, independently of $`m`$. This inherited [paired-power mechanism](../science/spectral_mechanism.md#corollary-paired-phase-accumulation) creates a stable readout of the exact perturbed phases. A further argument is needed to show those phases distinguish the two promises.

## Exact cancellation at the null

Let $`S=I-2|0\rangle\langle0|`$. It changes only the sign of $`|0\rangle`$. Consequently,

```math
S|x_\sigma\rangle=-|x_{-\sigma}\rangle,
\qquad SCS=C^\dagger.
```

If $`U|0\rangle=|0\rangle`$, unitarity prevents amplitude from the orthogonal complement entering $`|0\rangle`$. Thus $`U`$ commutes with $`S`$, and

```math
S(CU)S=C^\dagger U.
```

The reflection exchanges the two blocks and their useful branches. Their local phase values therefore satisfy $`\phi_{+,+}=\phi_{-,-}`$ and $`\phi_{+,-}=\phi_{-,+}`$, giving $`D=0`$ exactly. The unknown completion may contribute large accumulated common phases; their difference cancels.

This exact zero matters because $`m`$ diverges as the signal shrinks. A small signal-independent offset in $`D`$ would also be amplified by $`m`$. Exact null cancellation removes that offset at every order.

The physical state still has its small eigenvector-mismatch component. Therefore exact phase cancellation gives a false-positive probability below $`E(0.01)^2<0.002`$, not an exactly zero false-positive probability. See [the parity lemma](../science/spectral_mechanism.md#lemma-3-exact-null-cancellation).

## Turning on the discrete signal

The proof now connects each signal oracle to a null oracle. Set

```math
\overline U=R_a^\dagger U,
\qquad U_t=R_t\overline U,
\qquad 0\le t\le a.
```

The specified column ensures $`\overline U|0\rangle=|0\rangle`$, and $`U_a=U`$. These operators are a mathematical interpolation: the algorithm never constructs or queries $`\overline U`$ or the intermediate $`U_t`$.

Throughout this path, $`\|U_t-I\|\le3c_0`$, so the useful eigenvectors remain close to $`x_\sigma`$. Because the kick commutes with $`Y_{01}`$, differentiation gives

```math
\phi'_{\sigma,s}(t)
=-\langle v_{\sigma,s}(t)|Y_{01}|v_{\sigma,s}(t)\rangle.
```

The expectation is close to $`\sigma`$. Combining the four branches bounds $`D'(t)`$ close to $`-4`$. Integrating from the exact value $`D(0)=0`$ yields

```math
D(a)=-4a(1-\eta),
\qquad 0\le\eta<0.001.
```

The nuisance completion changes the response by a small fraction of the signal. It cannot add a fixed offset at zero signal. Choosing $`m\simeq\pi/(4a)`$ therefore makes $`mD`$ close to $`-\pi`$, and the final departure probability exceeds $`0.9`$. The [discrete proof](../science/discrete.md) supplies the path, derivative, rounding, and probability estimates in full.

## The Hamiltonian problem has a separate path

Here the promised object is a generator:

```math
\|H\|\le\Lambda,
\qquad H|0\rangle=0
\quad\hbox{or}\quad
H|0\rangle=\varepsilon|1\rangle,
\qquad 0<\varepsilon\le\Lambda.
```

The coupling $`\varepsilon`$ now has units of inverse time. The supplied primitive is only $`U=e^{-i\tau H}`$ with $`\tau=0.01/\Lambda`$. Higher powers of $`H`$ generally introduce extra components into the first column of this exponential, so the discrete column theorem cannot simply be applied to it.

The Hamiltonian algorithm uses $`G=X_{01}`$, $`C=iX_{01}-Q`$, and real superpositions $`x_\sigma=(|0\rangle+\sigma|1\rangle)/\sqrt2`$. In the normalized case $`\Lambda=1`$, write

```math
A=H-\varepsilon X_{01},
\qquad H_\lambda=A+\lambda X_{01}.
```

The operator $`A`$ is the compression of $`H`$ to $`|0\rangle^\perp`$, extended by zero on $`|0\rangle`$. Thus it has norm at most one. For $`0\le\lambda\le\varepsilon`$, the path is a convex combination of $`A`$ and $`H`$, retaining that norm bound. The zero-coupling endpoint has exact null cancellation.

Differentiating the exact exponential introduces an averaged conjugate of $`X_{01}`$, rather than exactly $`\tau X_{01}`$. Its difference from $`\tau X_{01}`$ has norm at most $`\tau^2`$. Combining this estimate with spectral confinement gives

```math
|D(\varepsilon)+4\varepsilon\tau|
\le4\varepsilon\tau\,[\tau+2q(\tau)^2].
```

The finite-step error is again proportional to the signal. With $`m=\mathrm{round}(\pi/(4\varepsilon\tau))`$, the algorithm obtains the same decision guarantees. The [Hamiltonian proof](../science/Hamiltonian.md) explains the derivative identity and rescaling to general $`\Lambda`$.

## Paying for the algorithm

The query count is dimension independent, but the selective kick has a gate cost. For the explicit $`n`$-qubit encoding, the pair is $`|0^{n-1}0\rangle,|0^{n-1}1\rangle`$. A reversible circuit checks whether the first $`n-1`$ bits are zero, applies a fixed conditional operation to the last bit, and uncomputes its work.

For $`n\ge2`$, the construction uses $`4n-4`$ Clifford/Toffoli gates and $`n-2`$ clean work qubits per kick. Every work qubit returns to zero before the next unknown query. Its angles are fixed exactly; the algorithm needs no increasingly precise synthesized quantum rotation as $`\varepsilon`$ shrinks.

| Resource per run | Discrete task | Hamiltonian task |
|---|---|---|
| Unknown forward calls and known kicks | $`\Theta(1/\varepsilon)`$ each | $`\Theta(\Lambda/\varepsilon)`$ each |
| Additional known gates | $`O(n/\varepsilon)`$ | $`O(n\Lambda/\varepsilon)`$ |
| Unknown-evolution time | Not defined by this oracle model | $`\Theta(1/\varepsilon)`$ |
| Query duration | Not specified | Every call has duration $`0.01/\Lambda`$ |
| Preparation and readout | One basis preparation; one final measurement | Same |

The calls are sequential. State loading, QRAM, controlled unknown calls, and inverse unknown calls are absent. The [resource account](../science/resources.md) gives exact controls, connectivity qualifications, classical handling of the repetition count, and the cost of increasing confidence.

## Error accumulation and the limits of the claim

The bounded eigenvector mismatch is not a physical noise budget. If the implementation differs from the intended operation on each call, those new errors can accumulate. In the half-diamond convention, let $`\delta_j`$ bound each operation's channel error, with preparation and measurement errors $`\eta_{\rm prep}`$ and $`\eta_{\rm meas}`$. A sufficient run budget is

```math
\eta_{\rm tot}
=\eta_{\rm prep}+\eta_{\rm meas}+\sum_j\delta_j.
```

This changes either output probability by at most $`\eta_{\rm tot}`$. For example, a total budget of $`0.1`$ retains false-positive probability below $`0.102`$ and signal detection above $`0.8`$. With a uniform bound per operation, the sufficient worst-case per-operation allowance therefore shrinks as the run grows; the total run budget can remain fixed.

A fixed calibration change that preserves the exact pairing and parity can behave differently; [structured calibration](../science/resources.md#structured-calibration-errors-and-exact-cancellation) treats that case. Neither statement gives tolerance to a constant rate of arbitrary physical noise.

The Hamiltonian oracle also permits trusted controls between separate evolution intervals. If the unknown generator acts during finite-duration control gates, their combined dynamics need additional analysis. The total $`T`$ counts unknown evolution, while wall-clock control time must be added separately.

## From mechanism to optimality

The algorithm amplifies a small difference at a rate that matches a general obstruction. Compare the valid discrete inputs $`U_0=I`$ and $`U_1=R_a`$. One query can change the two possible states by at most

```math
\|U_1-U_0\|=2\sin(a/2)=\Theta(\varepsilon).
```

Replacing oracle calls one at a time bounds the final distinguishability by $`N\|U_1-U_0\|`$. Constant decision advantage therefore requires $`N=\Omega(1/\varepsilon)`$. The same reasoning for $`H_0=0`$ and $`H_1=\varepsilon X_{01}`$ gives $`N=\Omega(1/(\varepsilon\tau))`$ and $`T=\Omega(1/\varepsilon)`$. [Lower bounds](../science/lower_bounds.md) handles workspace, measurements, and adaptive choices.

The complete contribution combines four facts: known controls isolate two useful eigenbranches; long powers preserve their small alignment error; parity cancels the null phase exactly; and turning on the known signal changes the contrast at a uniformly nonzero rate. Matching lower bounds then identify the scaling as optimal within the stated promise classes.

The [related-work account](../references/RELATED_WORK.md) separates the inherited machinery from these promise-specific conclusions. The [finite checks](../verification/README.md) test signs, ordering, exact controls, and selected completions. Their role is to catch implementation mistakes; the written proofs establish the uniform statements. The [milestone map](MILESTONES.md) organizes this same account from local objects to the full result.
