# Thirty milestones for understanding the project

[Learning entry](README.md) · [Childs-to-project bridge](CHILDS_BRIDGE.md) · [Scientific model](../science/model.md) · [Repository overview](../README.md)

This map describes the scientific understanding needed to connect the problem, mechanism, proofs, implementation and limits of forward-only quantum discrimination. Its targets and dependencies belong to the project and are independent of any reader's prior knowledge or progress. It is a route through the contribution, not a list of every technical detail in its proofs.

The single educational anchor is **Andrew M. Childs, [Lecture Notes on Quantum Algorithms](https://www.cs.umd.edu/~amchilds/qa/qa.pdf), title-page date 17 April 2025**. The author-hosted URL is a rolling document; section and page pointers below refer to that dated version. PDF page links count the eight opening pages before printed page 1. The [bridge](CHILDS_BRIDGE.md) explains the notation and the additional project-specific arguments. Primary papers linked from the scientific pages supply research attribution, rather than additional educational anchors.

## Allocation and dependency structure

- **Background/preliminaries, M01–M12:** twelve targets join states, circuits, query access, spectral phases, norm errors, coherent amplification, Hamiltonian evolution and distinguishing bounds into the precise problem. M12 integrates this framework.
- **Narrative/innovation, M13–M30:** eighteen targets develop the useful two-state motion, the nuisance obstruction, the shared spectral mechanism, the two separate proofs, and their optimality, implementation and scope. M30 integrates the complete contribution.

This 12/18 allocation reflects a project that connects several established algorithmic ideas but develops one specific discrimination mechanism in depth. Within each phase, the route moves from individual objects and argument components to their combined scientific meaning. Dependencies name earlier milestones; the canonical scientific pages remain the authority for exact statements.

## Phase I: background and preliminaries

### M01. States and the known pair

**Central question:** What does it mean to specify two known orthogonal quantum states?

**Understanding target:** Interpret a normalized state vector, orthogonality, amplitudes and the computational basis; identify the roles of the distinguished states and their orthogonal complement.

**Dependencies and story role:** No earlier milestone. This establishes the objects on which every later operation acts.

**Conceptual connection:** The familiar state-vector language becomes a concrete decision problem about a known transition direction.

**Source pointers:** Childs [§1.1](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=9); [a weak, known transition](../science/model.md#a-weak-known-transition).

### M02. A column and its unknown completion

**Central question:** How much of a unitary is determined by its action on one state?

**Understanding target:** Distinguish the promised first column from the remaining unknown action, and explain why a known output column does not make the whole process known or preserve a two-state subspace.

**Dependencies and story role:** M01. This introduces the nuisance degrees of freedom that the proof must handle uniformly.

**Conceptual connection:** A unitary's action on an entire basis clarifies the gap between a specified transition and an arbitrary completion.

**Source pointers:** Childs [§§1.1–1.2](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=9); [discrete promise](../science/model.md#discrete-promise-and-theorem).

### M03. Readout and the independent-copy baseline

**Central question:** Why does detecting a small amplitude by preparing fresh copies cost inverse-square resources?

**Understanding target:** Relate amplitude to departure probability, distinguish a measurement outcome from a hypothesis, and understand how overlap limits even collective discrimination of independent copies.

**Dependencies and story role:** M01–M02. This supplies the baseline against which coherent reuse becomes meaningful.

**Conceptual connection:** Born probabilities and state overlap connect a weak transition to a statistical resource cost.

**Source pointers:** Childs [§1.1](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=9) and [§23.1, Fact 23.1](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=117); [independent-copy baseline](../science/lower_bounds.md#the-independent-copy-baseline).

### M04. Circuit order and available operations

**Central question:** Which operations can actually be placed between calls to the unknown process?

**Understanding target:** Read products in right-to-left circuit order and distinguish a known gate, its implementable adjoint, an unknown forward query, and an unknown inverse or controlled query.

**Dependencies and story role:** M01–M02. This turns linear-algebra notation into an operational access model.

**Conceptual connection:** Mathematical reversibility of a unitary does not grant physical access to its inverse.

**Source pointers:** Childs [§§1.2–1.3](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=9); [allowed operations and charged resources](../science/model.md#allowed-operations-and-charged-resources).

### M05. Reversible work and selective known controls

**Central question:** How can a circuit act on a specified basis subspace while returning its work register to zero?

**Understanding target:** Explain predicate computation, a conditional known operation and uncomputation; distinguish control of a known gate from access to a controlled unknown oracle.

**Dependencies and story role:** M01, M04. This supplies the circuit ingredients for the later implementation account.

**Conceptual connection:** Reversible computation makes the project's selective controls explicit rather than treating them as free abstract operations.

**Source pointers:** Childs [§1.4](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=10); [exact controls for a qubit register](../science/resources.md#exact-controls-for-a-qubit-register).

### M06. Query models and resource comparisons

**Central question:** What is being counted when a quantum algorithm uses an oracle?

**Understanding target:** Separate oracle calls, known gates, workspace and sequential depth; identify which access assumptions must match before comparing algorithms. Recognize that the standard self-inverse bit oracle does not supply an inverse of this project's arbitrary unknown unitary.

**Dependencies and story role:** M03–M05. This integrates the elementary circuit objects into a fair resource model.

**Conceptual connection:** The query viewpoint isolates the cost of coherent interaction while keeping the additional implementation costs visible.

**Source pointers:** Childs [§1.6](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=11) and [§§21.1–21.2](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=105); [access and resource assumptions](../science/model.md#allowed-operations-and-charged-resources).

### M07. Eigenphases and long coherent powers

**Central question:** What happens when an eigenstate of a unitary undergoes many repetitions?

**Understanding target:** Explain eigenvalues on the unit circle, phase accumulation under powers, and the observable role of relative phases between branches.

**Dependencies and story role:** M01, M04. This introduces the spectral language used by the shared mechanism.

**Conceptual connection:** The eigenphase idea from phase estimation supplies intuition; the project's circuit extracts interference without running a phase-estimation subroutine.

**Source pointers:** Childs [§4.3](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=27); [the two distinguished branches](../science/spectral_mechanism.md#the-two-distinguished-branches).

### M08. Norm errors and accumulated distinguishability

**Central question:** How does an error bound on operations constrain the final observable outcome?

**Understanding target:** Interpret operator norm, follow a telescoping circuit-error bound, and connect a final state-distance bound to a bound on measurement probabilities.

**Dependencies and story role:** M03–M04, M06. This supplies the baseline error logic used in both optimality and implementation analysis.

**Conceptual connection:** A small error per call can accumulate with sequence length; the later spectral argument must explain why its specific leakage estimate behaves differently.

**Source pointers:** Childs [§1.3](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=10) and [§2.1, Lemma 2.2](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=15); [the local hybrid argument](../science/lower_bounds.md#a-hybrid-bound).

### M09. Coherent amplification and its access requirements

**Central question:** How can coherent rotation improve on independent sampling, and which operations enable ordinary amplitude amplification?

**Understanding target:** Explain the two-dimensional rotation picture and identify the role of inverse preparation and selective reflections in the standard construction.

**Dependencies and story role:** M03–M04, M07. This motivates a useful forward-only discriminator while making its distinction from generic amplification explicit.

**Conceptual connection:** A familiar quadratic gain suggests the target scaling, but its usual oracle operations cannot be silently imported.

**Source pointers:** Childs [§19.3, printed pp. 88–89](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=96); [the access boundary](../science/interpretation.md#the-access-boundary).

### M10. Hamiltonian evolution and the physical clock

**Central question:** How do a Hamiltonian, a unitary evolution and an elapsed time describe different parts of one experiment?

**Understanding target:** Interpret $`e^{-itH}`$, the norm scale $`\Lambda`$, the coupling $`\varepsilon`$, and the distinction between the number of calls and total unknown-evolution time.

**Dependencies and story role:** M01, M06–M08. This provides the second input model without identifying its promised column with the exponential's column.

**Conceptual connection:** Spectral phases become dynamical phases, and the duration of each permitted interaction becomes an explicit resource.

**Source pointers:** Childs [§17.1, printed pp. 73–74](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=81); [Hamiltonian promise](../science/model.md#fixed-step-hamiltonian-promise-and-theorem).

### M11. What a query lower bound establishes

**Central question:** How can two nearby admissible inputs rule out every algorithm with too few queries?

**Understanding target:** Separate an upper-bound circuit from a worst-case lower bound; understand why bounded-error outputs must become distinguishable and how a hybrid argument limits their separation.

**Dependencies and story role:** M03, M06, M08. This prepares the optimality claim, including algorithms with workspace or adaptive operations.

**Conceptual connection:** Childs' adversary perspective motivates tracking distinguishability; this project's norm hybrid is proved locally for its unitary hypotheses.

**Source pointers:** Childs [§23.1](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=117); [a hybrid bound](../science/lower_bounds.md#a-hybrid-bound).

### M12. The complete problem before the new mechanism

**Central question:** What must a successful forward-only discriminator achieve under the two precise promises?

**Understanding target:** Assemble the known direction and signal, trusted norm bound, arbitrary completion, allowed controls, bounded-error output and charged resources into the discrete and Hamiltonian tasks.

**Dependencies and story role:** M02–M11. This closes the background phase by integrating its objects and resource distinctions.

**Conceptual connection:** The sampling baseline, coherent opportunity and missing inverse jointly define the scientific question the next phase resolves.

**Source pointers:** Childs [§§21.1–21.2](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=105) and [§17.1](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=81); [complete model and results](../science/model.md).

## Phase II: narrative and innovation

### M13. The complete two-state mechanism

**Central question:** What does the paired sequence do when only the known transition is present?

**Understanding target:** Follow preparation, the two ordered blocks, accumulated rotation and final departure measurement in the exactly solvable two-state example, with every call counted.

**Dependencies and story role:** M07, M09–M10, M12. This begins the new narrative with a complete local example before adding an unknown completion.

**Conceptual connection:** The coherent-rotation picture explains why an inverse-signal number of calls could produce a visible decision signal.

**Source pointers:** Childs [§19.3](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=96); [complete two-state example](../science/examples.md#a-complete-two-state-example).

### M14. The nuisance obstruction

**Central question:** Why can simple repetition fail even when the transition direction is known and the oracle is near the identity?

**Understanding target:** Explain detuning in the explicit discrete and Hamiltonian examples and why waiting longer does not overcome their small transfer ceiling.

**Dependencies and story role:** M02, M07, M10, M13. This identifies the obstruction that the controls must overcome beyond the solvable example.

**Conceptual connection:** Eigenphase mismatch links unknown completion to suppressed coherent transfer.

**Source pointers:** Childs [§4.3](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=27) and [§17.1](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=81); [why uncontrolled repetition can fail](../science/examples.md#why-uncontrolled-repetition-can-fail).

### M15. The symmetric kick and its distinguished branches

**Central question:** How does a known control create the spectral structure used by the algorithm?

**Understanding target:** Identify the two known superpositions, the complementary subspace and the kick eigenvalues $`+i,-i,-1`$; explain the gap and the different choices of $`G`$ in the two models.

**Dependencies and story role:** M05, M07, M12, M14. This introduces the common mechanism's central constructed object.

**Conceptual connection:** Selective control turns the known transition geometry into separated spectral branches.

**Source pointers:** Childs [§4.3](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=27); [distinguished branches](../science/spectral_mechanism.md#the-two-distinguished-branches), [discrete algorithm](../science/discrete.md#theorem-and-algorithm), and [Hamiltonian algorithm](../science/Hamiltonian.md#normalized-model-and-theorem).

### M16. Spectral isolation and controlled leakage

**Central question:** Why do the useful branches survive every completion admitted by the norm promise?

**Understanding target:** Distinguish the existence of one simple nearby eigenvalue from the bound on its eigenvector leakage; explain the roles of perturbation radius, spectral gap and $`q(r)`$.

**Dependencies and story role:** M08, M15. This establishes the stability needed before taking long powers.

**Conceptual connection:** Operator-norm control becomes a dimension-independent overlap guarantee. The spectral-count and leakage arguments are supplied in the project.

**Source pointers:** Childs [§1.3](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=10); [Lemma 1](../science/spectral_mechanism.md#lemma-1-isolated-eigenvalues-and-leakage).

### M17. Paired powers without growing leakage

**Central question:** How can a long sequence accumulate the useful phase while keeping its state approximation error bounded?

**Understanding target:** Explain the invariant eigenvector decomposition, the power-independent error, and the conversion of four branch phases into the measured contrast $`D`$.

**Dependencies and story role:** M07–M08, M15–M16. This joins the isolated branches into the actual two-block sequence.

**Conceptual connection:** Eigenvector mismatch and arbitrary per-gate approximation are different error mechanisms. The paired-power extraction is inherited from Shin–Tong and reproduced locally.

**Source pointers:** Childs [§4.3](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=27) and [§2.1](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=15); [Lemma 2](../science/spectral_mechanism.md#lemma-2-powers-do-not-accumulate-leakage) and [paired accumulation](../science/spectral_mechanism.md#corollary-paired-phase-accumulation).

### M18. Exact null cancellation

**Central question:** Why does the nuisance phase contrast vanish at the null hypothesis?

**Understanding target:** Connect the reflection $`S`$, its exchange of distinguished branches, the relation $`SCS=C^\dagger`$ and the null oracle's symmetry to exact $`D=0`$. Retain the small physical leakage and two-sided error.

**Dependencies and story role:** M04, M15–M17. This supplies the cancellation on which both signal-response proofs depend.

**Conceptual connection:** The selective-reflection idea has a new role here: it establishes an exact relation between two controlled spectra.

**Source pointers:** Childs [§19.3](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=96); [Lemma 3](../science/spectral_mechanism.md#lemma-3-exact-null-cancellation) and [why the symmetric kick matters](../science/examples.md#why-the-symmetric-kick-matters).

### M19. The discrete proof-only path

**Central question:** How can the actual signal oracle be connected to an exact null while preserving control of its spectrum?

**Understanding target:** Explain the factorization $`U=R_a\overline U`$, why $`\overline U`$ fixes the initial state, and how the interpolation remains in a bounded norm neighborhood. Identify this path as analysis rather than additional query access.

**Dependencies and story role:** M02, M12, M16, M18. This constructs the first model's route from exact cancellation to a nonzero signal.

**Conceptual connection:** The promised column determines a useful analytical factorization while leaving the unknown completion unrestricted within the norm bound.

**Source pointers:** Childs [§§21.1–21.2](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=105); [discrete signal interpolation](../science/discrete.md#proof-a-signal-interpolation).

### M20. A uniform discrete signal slope

**Central question:** What prevents the unknown completion from masking an arbitrarily weak signal?

**Understanding target:** Connect the eigenphase derivative to the generator expectation, the leakage bound to extremal expectations, and integration from $`D(0)=0`$ to a relative signal-error bound.

**Dependencies and story role:** M16–M19. This is the load-bearing response estimate for the discrete theorem.

**Conceptual connection:** Exact cancellation and a nonzero derivative turn a potentially additive nuisance offset into a bounded multiplicative change of the signal.

**Source pointers:** Childs [§4.3](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=27) supplies eigenphase language; the derivative and slope proofs are [Lemma 4](../science/spectral_mechanism.md#lemma-4-eigenphase-derivatives) and [the discrete interpolation](../science/discrete.md#proof-a-signal-interpolation).

### M21. The complete discrete guarantee

**Central question:** How do cancellation, slope, rounding and leakage produce a bounded-error decision with linear query cost?

**Understanding target:** Assemble the known repetition number, outside-state probability and uniform error into the two success bounds and $`N=O(1/\varepsilon)`$ under the exact stated domain.

**Dependencies and story role:** M12, M17–M20. This integrates the first model's local ingredients into its full upper-bound theorem.

**Conceptual connection:** Controlled phase interference becomes an operational discrimination guarantee for every admitted completion.

**Source pointers:** Childs [§1.6](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=11) and [§19.3](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=96); [discrete theorem](../science/discrete.md#theorem-and-algorithm) and [success probability](../science/discrete.md#proof-success-probability).

### M22. A separate Hamiltonian path

**Central question:** Why does the Hamiltonian theorem require its own interpolation?

**Understanding target:** Distinguish a column of $`H`$ from a column of its exponential; explain the compression $`A`$, the family $`H_\lambda`$, its uniform norm bound and its null symmetry.

**Dependencies and story role:** M10, M12, M18–M19. This adapts the shared mechanism to the second promise without transferring an invalid column identity.

**Conceptual connection:** Hermiticity, compression and convexity replace the unitary-column factorization.

**Source pointers:** Childs [§17.1](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=81); [bounded Hamiltonian interpolation](../science/Hamiltonian.md#a-uniformly-bounded-hamiltonian-interpolation).

### M23. Finite-step bias proportional to the coupling

**Central question:** How are all orders of the matrix exponential controlled without shrinking the step with the signal?

**Understanding target:** Explain the integrated generator in the exact eigenphase derivative, its norm estimate, and why integration from the exact null bounds the contrast error proportionally to the coupling.

**Dependencies and story role:** M08, M16, M18, M20, M22. This supplies the second model's response estimate.

**Conceptual connection:** Keeping exact eigenphases and controlling their response avoids relying on an additive short-time state approximation over the full run.

**Source pointers:** Childs [§17.1](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=81) and [§2.1](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=15); [exact Hamiltonian eigenphase derivatives](../science/Hamiltonian.md#exact-eigenphase-derivatives).

### M24. The fixed-clock Hamiltonian guarantee

**Central question:** Which resource remains fixed, and which resources grow as the coupling becomes weak?

**Understanding target:** Combine the response and leakage bounds, restore units using $`\Lambda`$, and explain $`\tau=0.01/\Lambda`$, $`N=O(\Lambda/\varepsilon)`$ and $`T=O(1/\varepsilon)`$ with the stated success probabilities.

**Dependencies and story role:** M06, M10, M17, M22–M23. This integrates the second upper-bound theorem and its clock interpretation.

**Conceptual connection:** A constant query duration is compatible with a growing number of coherent interventions and a growing total evolution time.

**Source pointers:** Childs [§1.6](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=11) and [§17.1](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=81); [Hamiltonian success and count](../science/Hamiltonian.md#success-probability-and-query-count) and [general norm bound](../science/Hamiltonian.md#general-known-norm-bound).

### M25. Matching optimality bounds

**Central question:** Why can no alternative algorithm improve the leading inverse-signal scaling in these promise classes?

**Understanding target:** Check that the two-state witnesses obey the full promises, apply the local norm hybrid, and distinguish query optimality, evolution-time optimality and optimality of numerical constants.

**Dependencies and story role:** M11, M21, M24. This joins achievable performance to a worst-case obstruction and completes the scaling claims.

**Conceptual connection:** The simple local witnesses constrain algorithms with arbitrary workspace and stronger controlled access, so they also constrain the stated forward-only model.

**Source pointers:** Childs [§23.1](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=117); [discrete witnesses](../science/lower_bounds.md#discrete-witnesses-inside-the-promised-domain) and [Hamiltonian witnesses](../science/lower_bounds.md#hamiltonian-witnesses-and-the-fixed-clock).

### M26. Paying for the known controls

**Central question:** What does the abstract kick cost in a specified qubit encoding?

**Understanding target:** Connect the all-zero predicate, conditional Clifford phases and uncomputation to the gate, workspace and depth counts; preserve relative phases and distinguish arbitrary dimension from an actual qubit-register implementation.

**Dependencies and story role:** M05–M06, M15, M21, M24. This closes the gap between the query theorems and their additional circuit resources.

**Conceptual connection:** The explicit construction turns an assumed selective control into a charged operation, with no QRAM or signal-dependent quantum rotation synthesis.

**Source pointers:** Childs [§§1.3–1.4](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=10); [exact controls](../science/resources.md#exact-controls-for-a-qubit-register), [gate counts](../science/resources.md#predicate-circuit-and-exact-gate-count), and [classical repetition count](../science/resources.md#classical-control-of-the-repetition-number).

### M27. Precision and the structure of errors

**Central question:** How does error structure affect the guarantee and the sufficient worst-case per-use error allowance?

**Understanding target:** Interpret the composable error budget, distinguish exact nuisance symmetry and paired angle calibration from arbitrary implementation errors, and understand the scale of approximate-column tolerance.

**Dependencies and story role:** M08, M18, M21, M24, M26. This qualifies the operational meaning of the ideal theorem.

**Conceptual connection:** The same long coherent sequence has bounded spectral leakage but a shrinking sufficient per-use allowance for worst-case implementation error; the assumptions determine which statement applies.

**Source pointers:** Childs [§2.1, Lemma 2.2](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=15); [implementation-error budget](../science/resources.md#a-direct-implementation-error-budget), [structured calibration](../science/resources.md#structured-calibration-errors-and-exact-cancellation), and [approximate columns](../science/resources.md#approximate-column-promises).

### M28. What the finite checks establish

**Central question:** How do reproducible examples support the analytical account without replacing its uniform proof?

**Understanding target:** Identify what the two-state, detuned, dense-completion, conditional-phase and symmetry checks can detect; separate floating-point agreement from exact cancellation, general-dimension guarantees and lower bounds.

**Dependencies and story role:** M21, M24–M27. This connects the claims to the particular forms of evidence that support them.

**Conceptual connection:** Error-controlled computation is useful for checking formulas and implementations, while the written argument supplies the universal statement.

**Source pointers:** Childs [§2.1](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=15) supplies circuit-error context; the evidence account is [verification](../verification/README.md#what-each-check-establishes) and its [boundaries](../verification/README.md#evidence-boundaries).

### M29. The precise contribution and its ancestry

**Central question:** Which ingredients are inherited, and what additional guarantee is established here?

**Understanding target:** Attribute paired eigenphase extraction to Shin–Tong, recognize earlier spectral and sensing mechanisms, and place the two promise-specific theorems beside the unrestricted forward-only task and existing fixed-duration learning results.

**Dependencies and story role:** M09, M17–M18, M21, M24–M25, M28. This situates the complete result within its scientific context.

**Conceptual connection:** The gain comes from exact null cancellation and a uniform response under stated promises; originality and significance require this task-and-resource comparison, beyond correctness alone.

**Source pointers:** Childs [§19.3](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=96) supplies amplification context; [related work and attribution](../references/RELATED_WORK.md) supplies the primary research comparison, especially [Shin–Tong](../references/RELATED_WORK.md#shin-tong) and [Wang–Carolan–Childs](../references/RELATED_WORK.md#wang-carolan-childs).

### M30. The complete scientific account

**Central question:** What does the project establish about forward-only access, and which assumptions carry that conclusion?

**Understanding target:** Connect the two exact promises, shared mechanism, separate response proofs, optimal resource scalings, native controls, precision requirements and evidence limits into one account. Explain both the useful access insight and the remaining model boundaries.

**Dependencies and story role:** M12, M21, M24–M29. This closes the narrative phase by integrating the contribution as a whole.

**Conceptual connection:** Known direction and spectral control enable optimal coherent discrimination under specific access conditions; the scope remains a decision theorem rather than a general inverse, a full learning procedure or a device-level speedup.

**Source pointers:** Childs [§§21.1–21.2](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=105) and [§17.1](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=81); [model and results](../science/model.md), [meaning and boundaries](../science/interpretation.md), and [physical resource boundary](../science/resources.md#physical-interpretation-and-boundary).
