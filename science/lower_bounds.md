# Query and evolution-time lower bounds

[Model](model.md) · [Discrete upper bound](discrete.md) · [Hamiltonian upper bound](Hamiltonian.md)

## A hybrid bound

Let two possible unitary queries be $`V_0,V_1`$, and let an algorithm use them $`N`$ times, with any intervening known operations, workspace and measurements. Purify the operations and defer measurements. Replacing the oracle calls one at a time gives a Euclidean distance between final purifications at most

```math
N\|V_1-V_0\|.
```

For pure states, trace distance is at most Euclidean distance for any chosen phases. Trace distance cannot increase under discarding registers or measurement. Therefore the total variation distance between the algorithm's two output distributions is at most $`N\|V_1-V_0\|`$.

If each hypothesis is answered with error at most $`\delta<1/2`$, the probability of the NO output differs by at least $`1-2\delta`$. Consequently

```math
N\ge\frac{1-2\delta}{\|V_1-V_0\|}.
```

Adaptive algorithms with at most $`N`$ calls fit the same argument by adding coherent query controls and padding shorter branches. The norm difference of controlled versions of the two queries is unchanged. Thus allowing these extra operations only strengthens the lower-bound model; the upper-bound circuit does not require controlled unknown queries.

## Discrete witnesses inside the promised domain

Choose

```math
U_0=I,\qquad U_1=e^{-iaY_{01}},\qquad a=\arcsin\varepsilon.
```

Both act as the identity on $`Q`$. Their columns are exactly the two promised alternatives, and

```math
\|U_1-I\|=2\sin(a/2),\qquad
\varepsilon\le2\sin(a/2)\le a\le2\varepsilon\le c_0.
```

The last inequalities hold throughout $`0<\varepsilon\le c_0/2`$. Thus these are valid witnesses for every allowed signal size, not merely formal limiting examples. The hybrid bound yields

```math
N\ge\frac{1-2\delta}{2\sin(a/2)}
\ge\frac{1-2\delta}{2\varepsilon}
=\Omega(\varepsilon^{-1}).
```

Together with the paired-kick construction this proves optimal worst-case query scaling. It does not prove that the displayed upper-bound constant is optimal.

## Hamiltonian witnesses and the fixed clock

Choose $`H_0=0`$ and $`H_1=\varepsilon X_{01}`$. Their norms obey the promise for $`\varepsilon\le\Lambda`$. At the supplied step $`\tau=1/(100\Lambda)`$,

```math
\|e^{-i\tau H_1}-I\|=2\sin(\varepsilon\tau/2)
\le\varepsilon\tau.
```

Any bounded-error algorithm therefore needs

```math
N\ge\frac{1-2\delta}{\varepsilon\tau}
=\Omega\!\left(\frac{\Lambda}{\varepsilon}\right),\qquad
T=N\tau\ge\frac{1-2\delta}{\varepsilon}.
```

The evolution-time obstruction also survives replacing the fixed clock by arbitrary forward durations. For a fixed schedule, a call of duration $`t`$ changes the two possible evolutions by at most $`\varepsilon t`$, and telescoping gives total distance at most $`\varepsilon T`$.

For adaptive durations with worst-case total evolution budget $`T`$, defer measurements and place each branch's known operations at its cumulative oracle time. Pad branches to a common clock interval $`[0,T]`$ using controlled off intervals. Between known controls, the two possible generators differ by a block-diagonal controlled version of $`H_1-H_0`$, of norm at most $`\varepsilon`$. Integrating this generator difference bounds the final-state distance by $`\varepsilon T`$. The additional coherent controls strengthen the lower-bound model. This argument uses the maximum total duration along a branch, rather than a potentially larger sum of per-stage duration maxima.

## The independent-copy baseline

In the discrete problem one query can prepare either $`|0\rangle`$ or $`|\psi_\varepsilon\rangle=\sqrt{1-\varepsilon^2}|0\rangle+\varepsilon|1\rangle`$. For $`k`$ independent copies, their squared overlap is $`(1-\varepsilon^2)^k`$. The optimal equal-prior error is

```math
p_{\mathrm{err}}^{(k)}
=\frac12\left(1-\sqrt{1-(1-\varepsilon^2)^k}\right).
```

This follows by diagonalizing the difference of the two pure-state density matrices on their two-dimensional span. Constant error requires $`k=\Theta(\varepsilon^{-2})`$. Measuring each copy for departure also attains that scaling: under NO, each trial departs with probability $`\varepsilon^2`$.

This comparison isolates coherent reuse versus independent-copy access. It is not a classical computational lower bound for explicitly described circuits, and it does not replace the stronger unrestricted-forward-oracle result of [Wang, Carolan and Childs](../references/RELATED_WORK.md#wang-carolan-childs).
