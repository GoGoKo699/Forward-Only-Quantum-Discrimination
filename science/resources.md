# Resources, implementation, and robustness

[Model](model.md) · [Spectral mechanism](spectral_mechanism.md) · [Finite checks](../verification/README.md)

The paired-kick algorithms use a single coherent data register and a fixed known control after every unknown query. Their query bounds do not include the cost of implementing the oracle itself. This page accounts for the additional controls and separates the exact oracle model from implementation error.

## One run and its paid resources

Write $`N=2m`$ for the number of unknown queries in one run. In the discrete problem, $`a=\arcsin\varepsilon`$ and $`m=\operatorname{round}(\pi/(4a))`$. In the Hamiltonian problem, $`\|H\|\le\Lambda`$, the fixed query duration is $`\tau=0.01/\Lambda`$, and $`m=\operatorname{round}(\pi/(4\varepsilon\tau))`$. Here the Hamiltonian coupling $`\varepsilon`$ has units of inverse time and satisfies $`0<\varepsilon\le\Lambda`$.

| Resource | Discrete oracle | Fixed-step Hamiltonian oracle |
|---|---|---|
| Unknown forward queries | $`N\le\pi/(2\varepsilon)+1`$ | $`N\le\pi/(2\varepsilon\tau)+1`$ |
| Known kicks | $`N`$ | $`N`$ |
| Unknown evolution time | Not a resource defined by this oracle model | $`T=N\tau\le\pi/(2\varepsilon)+\tau`$ |
| Duration of every unknown evolution call | Not specified | Exactly $`\tau`$ |
| Initial state | One computational basis state | One computational basis state |
| Final readout | Computational zero/nonzero test | Computational zero/nonzero test |
| Inverse or controlled unknown calls | None | None |
| Phase estimation, oracle calibration, or power oracle | None | None |
| QRAM or an unknown-state loading primitive | None | None |

All powers are implemented by their displayed number of forward calls. No variable-duration query or hidden negative evolution appears in either proof interpolation. The algorithm is the single sequence $`(C^\dagger U)^m(CU)^m`$, with the rightmost block executed first.

A run requires $`N`$ sequential unknown calls. It is not a short-depth algorithm. Independent repetition with fresh preparation reduces the error to $`\delta`$ using $`O(\log(1/\delta))`$ runs. Repetition multiplies total queries, controls, and evolution time by that factor; it does not increase the coherent register size.

## Exact controls for a qubit register

For this implementation take the physical data space to have dimension $`d=2^n`$, and encode

```math
|0\rangle=|0^{n-1}0\rangle,
\qquad
|1\rangle=|0^{n-1}1\rangle.
```

The first $`n-1`$ qubits are controls and the final qubit is the target. The algebraic query theorem applies to arbitrary finite dimension separately. It does not supply an uncharged extension of an arbitrary $`d`$-dimensional oracle to unused states of a qubit register.

Let $`b`$ be the reversible predicate that the first $`n-1`$ bits are all zero. The distinguished two-dimensional subspace is exactly the $`b=1`$ subspace. The kick equals $`iG`$ there and $`-I`$ on its complement. Multiplying the entire kick by $`-1`$ gives a gate that is the identity when $`b=0`$ and equals $`-iG`$ when $`b=1`$.

This overall phase is harmless. In fact, replacing every kick by its negative introduces the total factor $`(-1)^{2m}=1`$ in the complete circuit. Relative phases inside a conditional gate must still be preserved.

### Discrete control

On the target, $`-iY=XZ`$ and $`+iY=ZX`$. Therefore:

- To implement $`-C`$, apply $`\operatorname{CZ}_{b,t}`$ followed by $`\operatorname{CNOT}_{b,t}`$.
- To implement $`-C^\dagger`$, apply the same two gates in the opposite order.

Both operations have the identity action when $`b=0`$. Their ordered product gives the required conditional sign when $`b=1`$.

### Hamiltonian control

The Hamiltonian proof uses $`G=X`$ on the target pair. Implement $`-C`$ using $`S_b^\dagger`$ and $`\operatorname{CNOT}_{b,t}`$, and implement $`-C^\dagger`$ using $`S_b`$ and $`\operatorname{CNOT}_{b,t}`$. Here $`S_b=\operatorname{diag}(1,i)`$ is the single-qubit phase gate on the predicate. These two gates commute.

The phase gate on the predicate is necessary: conditional $`X`$ alone would omit the relative factor $`\mp i`$ between the distinguished subspace and its complement and would implement the wrong kick.

### Predicate circuit and exact gate count

For $`n\ge2`$, flip each of the first $`n-1`$ data bits, compute their AND, perform the two gates above, uncompute the AND, and undo the flips. For $`n=2`$, the flipped control itself is the predicate, so no work qubit is needed. For $`n\ge3`$, a ladder of $`n-2`$ Toffoli gates computes the AND into $`n-2`$ clean work qubits; the reverse ladder uncomputes it.

The resulting cost per kick is:

| Item | Count for $`n\ge2`$ |
|---|---:|
| Toffoli gates, including uncomputation | $`2(n-2)`$ |
| Single-qubit $`X`$ gates on the controls | $`2(n-1)`$ |
| Additional Clifford gates | $`2`$ |
| Total Clifford/Toffoli gates | $`4n-4`$ |
| Clean work qubits | $`n-2`$ |

Every work qubit returns to zero before the next unknown query. With all-to-all connectivity, parallel initial/final bit flips, and a Toffoli counted as one gate layer, the straightforward construction has depth at most $`2n`$ per kick. Routing and decomposition into a device's actual gate set must be charged separately. For $`n=1`$, the kick is an ordinary fixed one-qubit operation and needs no work register.

Thus the additional known-gate count is at most $`(4n-4)N`$ for $`n\ge2`$: $`O(n/\varepsilon)`$ in the discrete problem and $`O(n\Lambda/\varepsilon)`$ in the Hamiltonian problem. For $`n\ge2`$, the number of data plus work qubits is at most $`2n-2`$. These are exact mathematical Clifford/Toffoli circuits with fixed angles. There is no rotation-synthesis precision that grows as $`\varepsilon`$ decreases. This exact decomposition is not a statement about physical gate accuracy.

Other fixed computational basis pairs can be mapped to this pair by a known affine reversible circuit using $`O(n)`$ additional Clifford gates. More general specified quantum states require their own charged preparation and selective-control construction.

## Classical control of the repetition number

The signal parameter and the norm bound are inputs to the promise problem. Computing the repetition number is a classical task. The integer $`m`$ has $`O(\log(1/\kappa))`$ bits, where $`\kappa=a`$ in the discrete problem and $`\kappa=\varepsilon\tau`$ in the Hamiltonian problem. Bit complexity of the supplied numerical input and classical arithmetic is separate from oracle complexity.

The proof does not require resolving the exact side of a rounding tie. The same conservative one-run bounds hold whenever the chosen integer satisfies

```math
|4m\kappa-\pi|\le0.1.
```

Indeed, the discrete relative contrast error is less than $`0.001`$, and the Hamiltonian relative contrast error is less than $`0.0102`$. The displayed pulse-area condition bounds the total phase mismatch by less than $`0.104`$ and $`0.134`$, respectively. Combined with the state-error bound below $`0.041`$, each still gives signal detection above $`0.9`$. Certified constant fractional accuracy in the signal-time product therefore suffices; epsilon-dependent quantum rotation synthesis is unnecessary. This relaxed count retains the asymptotic query bounds; the exact numerical bounds in the table use the nearest-integer formula.

The Hamiltonian argument also holds for any fixed actual duration satisfying $`0<\tau\Lambda\le0.01`$. A fixed clock-calibration uncertainty can be handled through this norm condition and the pulse-area condition above. This is distinct from arbitrary, independently varying errors on successive evolution calls.

## A direct implementation-error budget

Use the half-diamond distance for a channel error:

```math
\delta_j=\frac12\|\widetilde{\mathcal E}_j-\mathcal E_j\|_\diamond.
```

Suppose preparation differs from its ideal state by trace distance at most $`\eta_{\rm prep}`$, and the implemented final binary measurement effect differs from the ideal effect in operator norm by at most $`\eta_{\rm meas}`$. A telescoping expansion of the composed channels, together with trace-distance contractivity, gives

```math
|\widetilde p-p|
\le
\eta_{\rm prep}+\eta_{\rm meas}+\sum_j\delta_j
=: \eta_{\rm tot}.
```

The estimate permits time-varying, coherent, and nonunitary errors in the individual channels. It assumes a composable channel description on the data and declared work registers; a bound on marginal channels alone does not justify neglecting an uncontrolled environment that retains memory between calls.

If every unknown query has error at most $`\delta_U`$ and every complete known kick has error at most $`\delta_C`$, then

```math
\eta_{\rm tot}
\le\eta_{\rm prep}+\eta_{\rm meas}+N(\delta_U+\delta_C).
```

Alternatively, for the exact circuit above and a common error bound $`\delta_g`$ on each counted Clifford/Toffoli gate,

```math
\eta_{\rm tot}
\le\eta_{\rm prep}+\eta_{\rm meas}
 +N\delta_U+(4n-4)N\delta_g,
\qquad n\ge2.
```

The ideal bounds $`p_{\rm null}<0.002`$ and $`p_{\rm signal}>0.9`$ consequently imply

```math
\widetilde p_{\rm null}<0.002+\eta_{\rm tot},
\qquad
\widetilde p_{\rm signal}>0.9-\eta_{\rm tot}.
```

For example, $`\eta_{\rm tot}\le0.1`$ leaves the null probability below $`0.102`$ and the signal probability above $`0.8`$. Majority voting on independent runs reaches error at most $`\delta`$ with $`R\ge\lceil\log(1/\delta)/0.18\rceil`$ runs by Hoeffding's inequality.

This sufficient worst-case budget requires arbitrary per-query or per-kick errors to be $`O(\varepsilon)`$ in the discrete setting and $`O(\varepsilon/\Lambda)`$ in the fixed-step Hamiltonian setting. A uniform error bound on each counted known gate scales as $`O(\varepsilon/n)`$ or $`O(\varepsilon/(n\Lambda))`$, respectively. These are sufficient adversarial budgets, not necessity claims for every structured noise model.

For unitary implementation errors, $`\frac12\|\mathcal W-\mathcal V\|_\diamond\le\|W-V\|`$, so an operator-norm gate-error estimate can be inserted directly. A static Hamiltonian error $`\Delta H`$ obeys the Duhamel bound

```math
\|e^{-i\tau(H+\Delta H)}-e^{-i\tau H}\|
\le\tau\|\Delta H\|,
```

and hence contributes at most $`T\|\Delta H\|`$ to the run budget. An arbitrary sequence of interval errors $`\Delta\tau_j`$ contributes at most $`\Lambda\sum_j|\Delta\tau_j|`$ when the generator itself is unchanged.

## Structured calibration errors and exact cancellation

The uniform-in-power spectral estimate tolerates the entire unknown nuisance completion already allowed by the exact promise. That tolerance does not follow from a per-call approximation. It follows from isolated bright eigenvectors and an exact cancellation of the null phase contrast.

A closely related, explicitly structured calibration statement is useful. Let

```math
C_\theta
=\cos\theta\,P+i\sin\theta\,G-Q,
\qquad
P=|0\rangle\langle0|+|1\rangle\langle1|,
\qquad
Q=I-P,
```

and pair $`C_\theta`$ with its exact adjoint. If $`\theta\in[\pi/3,2\pi/3]`$ is fixed, both the generator commutation and the parity identity survive:

```math
[C_\theta,G]=0,
\qquad
SC_\theta S=C_\theta^\dagger.
```

The bright eigenvalues are $`e^{\pm i\theta}`$ and the bath eigenvalue is $`-1`$. Their minimum gap is

```math
g_\theta
=\min\{2\sin\theta,\,2\cos(\theta/2)\}\ge1.
```

Repeat the proof with $`q(r)=r/(1-r)`$ in place of $`r/(\sqrt2-r)`$. The output-state error is then below $`0.0572`$. In the discrete problem the accumulated phase mismatch is below $`0.047`$; in the Hamiltonian problem it is below $`0.053`$. The unchanged repetition number gives null probability below $`0.004`$ and signal probability above $`0.88`$ in both problems.

Thus a fixed common offset of the two paired kick angles can be harmless at constant size when these exact structural relations are retained. This statement does not apply to an arbitrary pair of imperfect controls, generic native-gate errors, or drift that breaks the pairing. The exact Clifford/Toffoli implementation above uses $`\theta=\pi/2`$; no free implementation of general angles is being assumed.

## Approximate column promises

The implementation budget also gives a clean way to state approximate-promise guarantees. Suppose an actual discrete oracle is within operator distance $`\zeta`$ of an oracle satisfying the exact theorem. Its output probability differs by at most $`N\zeta`$. If an actual Hamiltonian is within operator distance $`\zeta_H`$ of a Hamiltonian satisfying the exact theorem at the same fixed step, its output probability differs by at most $`T\zeta_H`$.

Column errors can be reduced to these statements without an additional unknown operation in the algorithm. For a unitary $`U`$, write $`u=U|0\rangle`$ and let $`v`$ be the desired unit-norm first column. There exists a unitary $`W`$ satisfying

```math
Wu=v,
\qquad
\|W-I\|=\|u-v\|.
```

To see this, write $`v=\alpha u+\beta w`$, with $`w\perp u`$ and $`\beta\ge0`$. On $`\operatorname{span}\{u,w\}`$ use the unitary matrix

```math
\begin{pmatrix}
\alpha&-\beta\\
\beta&\overline\alpha
\end{pmatrix},
```

and use the identity on the complement. Its sum with its adjoint is $`2\operatorname{Re}\alpha`$ times the identity on that span, which proves the norm equality. If $`\beta=0`$, a phase on $`u`$ suffices. Consequently $`U_*=WU`$ has the exact target column and $`\|U-U_*\|\le\zeta`$ whenever the column error is at most $`\zeta`$. A sufficient norm margin is $`\|U-I\|\le c_0-\zeta`$, which ensures $`\|U_*-I\|\le c_0`$.

For a Hermitian $`H`$, let $`e=H|0\rangle-v`$, where $`v=0`$ or $`v=\varepsilon|1\rangle`$. Its coefficient $`e_0=\langle0|e\rangle`$ is real. Write $`e=e_0|0\rangle+b|w\rangle`$ with $`w\perp0`$ and $`b\ge0`$. The Hermitian correction

```math
\Delta
=e_0(|0\rangle\langle0|-|w\rangle\langle w|)
+b(|0\rangle\langle w|+|w\rangle\langle0|)
```

has $`\Delta|0\rangle=e`$ and $`\|\Delta\|=\|e\|`$. If $`b=0`$, use $`\Delta=e_0|0\rangle\langle0|`$. Hence $`H_*=H-\Delta`$ has the exact target column and lies within operator distance $`\|e\|`$ of $`H`$. The explicit sufficient margin $`\|H\|\le\Lambda-\zeta_H`$ ensures $`\|H_*\|\le\Lambda`$ when $`\|e\|\le\zeta_H`$. An enlarged known norm bound may instead be used when selecting the fixed step.

These are proof-only repairs. The algorithm neither constructs $`W`$ or $`\Delta`$ nor queries the repaired oracle. They show that column errors of order a sufficiently small constant times $`\varepsilon`$ preserve a constant distinguishing gap. An absolute column tolerance independent of $`\varepsilon`$ cannot be guaranteed uniformly as $`\varepsilon\to0`$: the neighborhoods of the two target columns eventually overlap.

## Physical interpretation and boundary

The Hamiltonian oracle model allows trusted known controls between distinct intervals of unknown evolution. Its total unknown-evolution time $`T`$ excludes the time required to perform those controls. If a complete kick takes wall-clock time $`t_C`$, the control contribution is $`Nt_C`$ in addition to $`T`$, preparation, and measurement. The native circuit above also presumes a gate and connectivity model under which its stated controls are available.

A device on which the unknown Hamiltonian continues to act during finite-duration controls requires a joint drift-and-control analysis. The fixed query duration proved here does not supply that analysis. Likewise, the theorem does not certify the global norm promise for free, learn every Hamiltonian coefficient, provide generic amplitude amplification with an unknown target direction, or establish tolerance to a constant rate of arbitrary physical noise.
