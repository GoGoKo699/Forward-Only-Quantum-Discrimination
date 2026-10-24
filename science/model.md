# Problem, access model and results

[Repository overview](../README.md) · [Spectral mechanism](spectral_mechanism.md) · [Resources](resources.md)

## A weak, known transition

An unknown quantum process acts on a system with two distinguished, known basis states. The task is to decide whether the process leaves the first state unchanged or moves a small amplitude toward the second. Repeating state preparation and measurement pays an inverse-square cost in that amplitude. Coherent access can do better, but the unknown operation is available only in the forward direction.

This project identifies a sufficient spectral promise for optimal forward-query discrimination. It also solves a related Hamiltonian promise using one fixed positive evolution interval. The two input promises are different, so the Hamiltonian result has its own proof.

Let the system Hilbert space have finite dimension $`d\ge2`$, with known orthonormal computational states $`|0\rangle,|1\rangle`$. All norms on operators are operator norms unless stated otherwise. Define

```math
P_j=|j\rangle\langle j|,\qquad P=P_0+P_1,\qquad Q=I-P,
\qquad S=I-2P_0.
```

Here $`Q`$ denotes a projector, never the query count. We use $`N`$ for the number of forward oracle calls. A YES instance is the null case; the algorithm outputs NO when its final measurement finds a state outside $`|0\rangle`$.

## Allowed operations and charged resources

The algorithm may prepare computational basis states, apply known gates, use clean work qubits and measure in the computational basis. One query applies the supplied unknown unitary to the system register. No inverse or controlled version of that unknown unitary is supplied. The known gates may be interleaved with calls, and the same unknown oracle is reused coherently throughout one run.

The main bounds count forward queries. The circuit account also charges known gates, workspace, preparation, measurement and sequential depth. For the Hamiltonian problem, total time under the unknown Hamiltonian is a separate resource. Known-control duration is not included in that evolution-time total; the model assumes trusted interleaving controls. A continuously acting unknown drift during finite-duration controls requires an additional model.

The global norm bounds and exact columns below are input promises, not quantities that the algorithm certifies at no cost. The signal size is known. The encoding and gate construction are explicit in [Resources](resources.md).

## Discrete promise and theorem

Fix $`c_0=1/100`$. The input is a forward-only unitary $`U`$ and a known number $`0<\varepsilon\le c_0/2`$, with

```math
\|U-I\|\le c_0,\qquad
\begin{cases}
\mathrm{YES}:& U|0\rangle=|0\rangle,\\
\mathrm{NO}:& U|0\rangle=\sqrt{1-\varepsilon^2}|0\rangle+\varepsilon|1\rangle.
\end{cases}
```

The phase convention and the complete known column are part of the promise. The rest of the unitary may be dense and unknown.

Define

```math
Y_{01}=-i|0\rangle\langle1|+i|1\rangle\langle0|,\qquad
C_Y=iY_{01}-Q,\qquad a=\arcsin\varepsilon,
\qquad m=\mathrm{round}\!\left(\frac{\pi}{4a}\right).
```

**Discrete theorem.** Preparing $`|0\rangle`$, applying $`(C_Y^\dagger U)^m(C_YU)^m`$ and testing for departure from $`|0\rangle`$ gives

```math
\Pr(\mathrm{NO}\mid\mathrm{YES})<0.002,\qquad
\Pr(\mathrm{NO}\mid\mathrm{NO})>0.9,
\qquad N=2m\le\frac{\pi}{2\varepsilon}+1.
```

The worst-case bounded-error query complexity is $`\Theta(\varepsilon^{-1})`$, uniformly in $`d`$. The [complete proof](discrete.md) uses spectral confinement and exact cancellation of the null phase. The [lower bound](lower_bounds.md) already holds in dimension two.

## Fixed-step Hamiltonian promise and theorem

The input is a Hermitian operator $`H`$ with a known bound $`\|H\|\le\Lambda`$, $`\Lambda>0`$, and known coupling $`0<\varepsilon\le\Lambda`$. The promise is

```math
\begin{cases}
\mathrm{YES}:& H|0\rangle=0,\\
\mathrm{NO}:& H|0\rangle=\varepsilon|1\rangle.
\end{cases}
```

The only unknown primitive is

```math
U=e^{-i\tau H},\qquad \tau=\frac{1}{100\Lambda}.
```

The algorithm uses this one duration; it needs neither shorter unknown evolutions nor variable query times. Set

```math
X_{01}=|0\rangle\langle1|+|1\rangle\langle0|,\qquad
C_X=iX_{01}-Q,\qquad
m=\mathrm{round}\!\left(\frac{\pi}{4\varepsilon\tau}\right).
```

**Hamiltonian theorem.** The same paired sequence with $`C_X`$ has the same two probability bounds, with

```math
N=2m=\Theta\!\left(\frac{\Lambda}{\varepsilon}\right),\qquad
T=N\tau\le\frac{\pi}{2\varepsilon}+\tau
=\Theta(\varepsilon^{-1}).
```

The step is constant with respect to the shrinking signal at fixed norm bound. It still depends on $`\Lambda`$. Both query and evolution-time scalings are optimal in this model. The [Hamiltonian proof](Hamiltonian.md) controls the exponential's higher-order terms directly. A promise about $`H|0\rangle`$ is not a promise about the exact first column of $`e^{-i\tau H}`$.

## What supports the claims

The analytical chain is [spectral isolation and paired powers](spectral_mechanism.md), then [the unitary interpolation](discrete.md) or [the Hamiltonian interpolation](Hamiltonian.md), followed by [matching lower bounds](lower_bounds.md). [Examples](examples.md) explain the mechanism; [verification](../verification/README.md) checks selected finite instances and exact circuit identities.

The paired-power extraction is inherited from Shin and Tong's eigenphase-engineering analysis. The promise-specific ingredients here are the symmetric kick, exact null cancellation and a uniform signal-response bound. [Related work](../references/RELATED_WORK.md) distinguishes these claims from existing forward-only lower bounds, Hamiltonian learning and Floquet sensing.
