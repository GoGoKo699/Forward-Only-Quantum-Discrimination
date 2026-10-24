# Forward-only discrimination near the identity

A fixed operator-norm neighborhood of the identity is sufficient for optimal linear query scaling in the known-column discrimination problem. The proof allows an arbitrary completion of the promised column and places no restriction on Hilbert-space dimension beyond finiteness.

The algorithm uses the [paired spectral mechanism](spectral_mechanism.md). Its uniform phase-accumulation step is inherited from [Shin–Tong](../references/RELATED_WORK.md#shin-tong); the exact null cancellation makes the nuisance contribution proportional to the signal.

## Access model and promise

Let $`d\ge2`$, with two known orthogonal computational basis states $`|0\rangle,|1\rangle`$. The unknown input is a unitary $`U`$ available only through forward queries. Known gates, ancillary systems, computational-basis preparation and computational-basis measurement are allowed.

Set $`c_0=1/100`$. A known number $`\varepsilon`$ satisfies $`0<\varepsilon\le c_0/2`$. The trusted input promise is $`\|U-I\|\le c_0`$ and exactly one of

```math
\begin{aligned}
\mathrm{YES}:&\quad U|0\rangle=|0\rangle,\\
\mathrm{NO}:&\quad U|0\rangle=\sqrt{1-\varepsilon^2}|0\rangle+
\varepsilon|1\rangle.
\end{aligned}
```

The full column, including its phase convention and target direction, is promised. The global norm bound is an assumption supplied with the input.

## Theorem and algorithm

Define

```math
\begin{aligned}
G&=Y_{01}=-i|0\rangle\langle1|+i|1\rangle\langle0|,\\
Q&=I-|0\rangle\langle0|-|1\rangle\langle1|,\\
C&=iG-Q,\\
|x_\sigma\rangle&=(|0\rangle+i\sigma|1\rangle)/\sqrt2,
\qquad \sigma\in\{+1,-1\}.
\end{aligned}
```

Let

```math
a=\arcsin\varepsilon,\qquad
m=\mathrm{round}\!\left(\frac{\pi}{4a}\right),
```

where either nearest integer is allowed at a tie. Prepare $`|0\rangle`$ and apply

```math
(C^\dagger U)^m(CU)^m,
```

in the usual right-to-left circuit order. Measure in the computational basis and output NO exactly when the result is outside $`|0\rangle`$.

**Theorem.** The YES probability of outputting NO is below $`0.002`$, and the NO probability of outputting NO exceeds $`0.9`$. The algorithm uses exactly $`2m`$ forward queries, with

```math
2m\le\frac{\pi}{2\varepsilon}+1.
```

Its query complexity is $`\Theta(1/\varepsilon)`$, uniformly in dimension. It uses $`2m`$ known kicks; neither an inverse query nor a controlled unknown query is required.

## Proof: null hypothesis

The two distinguished eigenvalues of $`C`$ are $`+i`$ and $`-i`$, separated by at least $`\sqrt2`$ from the rest of its spectrum. Write $`F_+=CU`$ and $`F_-=C^\dagger U`$. Both are within $`c_0`$ of their respective known kicks.

The [paired accumulation corollary](spectral_mechanism.md#corollary-paired-phase-accumulation) approximates the final state by its two-branch phase superposition with error

```math
E(c_0)=4\sqrt2\frac{c_0}{\sqrt2-c_0}<0.041,
```

independently of $`m`$. In the YES case, $`U`$ fixes $`|0\rangle`$, so [exact null cancellation](spectral_mechanism.md#lemma-3-exact-null-cancellation) gives $`D=0`$. The probability outside $`|0\rangle`$ is consequently at most

```math
E(c_0)^2<0.041^2<0.002.
```

## Proof: a signal interpolation

For a NO instance, introduce the proof-only family

```math
R_t=e^{-itG},\qquad
\overline U=R_a^\dagger U,\qquad
U_t=R_t\overline U,\qquad 0\le t\le a.
```

The promised column gives $`\overline U|0\rangle=|0\rangle`$, while $`U_a=U`$. No member of this interpolation is queried by the algorithm.

The column also yields

```math
2\sin(a/2)=\|(U-I)|0\rangle\|\le c_0,
```

so $`a\le2c_0`$. Since $`U_t=R_{t-a}U`$,

```math
\|U_t-I\|\le\|R_{t-a}-I\|+\|U-I\|
\le|t-a|+c_0\le3c_0.
```

The distinguished eigenbranches of $`F_s(t)=C^sU_t`$, $`s=\pm1`$, are therefore simple throughout the interpolation. Choose their phases $`\phi_{\sigma,s}(t)`$ in the fixed local neighborhoods of $`s\sigma\pi/2`$, and let

```math
D(t)=(\phi_{+,+}(t)+\phi_{+,-}(t))
-(\phi_{-,+}(t)+\phi_{-,-}(t)).
```

At $`t=0`$, the oracle $`\overline U`$ fixes $`|0\rangle`$, so $`D(0)=0`$ exactly.

Because $`C`$ commutes with $`G`$,

```math
F_s'(t)=-iG F_s(t).
```

The [eigenphase derivative lemma](spectral_mechanism.md#lemma-4-eigenphase-derivatives) gives

```math
\phi'_{\sigma,s}(t)
=-\langle v_{\sigma,s}(t)|G|v_{\sigma,s}(t)\rangle.
```

At every interpolation point, the plus-branch expectation is in $`[1-2q(3c_0)^2,1]`$, and the minus-branch expectation is in $`[-1,-1+2q(3c_0)^2]`$, with $`q(r)=r/(\sqrt2-r)`$. Thus

```math
-4\le D'(t)\le-4+8q(3c_0)^2.
```

Integrating from the exact null,

```math
D(a)=-4a(1-\eta),\qquad
0\le\eta\le2q(3c_0)^2<0.001.
```

An arbitrary completion of the promised column changes the signal by a uniformly bounded relative amount. It cannot introduce a signal-independent contrast at the null.

## Proof: success probability

Rounding $`m`$ gives $`|4ma-\pi|\le2a`$. Therefore

```math
|mD(a)+\pi|
\le2a+(\pi+2a)\,2q(3c_0)^2
<0.044.
```

The ideal outside amplitude is at least $`\cos(0.022)`$. At the actual oracle, the state approximation uses the original radius $`c_0`$, so the actual NO detection probability is at least

```math
\bigl(\cos(0.022)-E(c_0)\bigr)^2
>\bigl(\cos(0.022)-0.041\bigr)^2>0.9.
```

All numerical constants follow from elementary inequalities. For example, $`1.414<\sqrt2<1.415`$ gives $`E(c_0)<0.041`$ and $`2q(3c_0)^2<0.001`$; using $`\pi<22/7`$ proves the displayed phase bound. Finally, $`\cos x\ge1-x^2/2`$ certifies the success threshold.

The query count follows from

```math
2m\le\frac{\pi}{2a}+1\le\frac{\pi}{2\varepsilon}+1.
```

## Optimality and scope

For every allowed $`\varepsilon`$, the pair $`U_0=I`$ and $`U_1=e^{-iaY_{01}}`$, acting as identity outside the distinguished span, satisfies the respective promises. In particular,

```math
\|U_1-U_0\|=2\sin(a/2)
=\frac{\varepsilon}{\cos(a/2)}
\le\sqrt2\,\varepsilon<c_0.
```

The hybrid argument in [the lower-bound analysis](lower_bounds.md) therefore requires $`\Omega(1/\varepsilon)`$ queries for constant distinguishing advantage, even with controlled oracle access. This establishes optimality in the stated promise class.

The signal magnitude is known, the direction is known, and the entire first column is fixed by the promise. The theorem addresses this decision task. Oracle-query independence from dimension does not remove the cost of implementing the known selective controls. Repeating independent runs and taking a majority gives failure probability $`\delta`$ with $`O(\log(1/\delta))`$ runs.
