# Learning forward-only quantum discrimination

[Repository overview](../README.md) · [Scientific model](../science/model.md) · [Childs-to-project bridge](CHILDS_BRIDGE.md) · [30 milestones](MILESTONES.md)

The project asks when a weak, known transition can be detected with an optimal number of coherent interactions even though the unknown operation cannot be reversed. This route connects the required quantum-algorithm foundations to the controls, proofs and resource limits that answer that question.

## One educational anchor

The selected source is **Andrew M. Childs, [Lecture Notes on Quantum Algorithms](https://www.cs.umd.edu/~amchilds/qa/qa.pdf), dated 17 April 2025**, available from the [author's page](https://www.cs.umd.edu/~amchilds/qa/). The source address is a rolling document; the date identifies the version used for the section and page references here.

Use the relevant sections as needed: states and circuits, reversible work, query models, eigenphases, coherent amplification, Hamiltonian evolution and distinguishability. The [bridge's source map](CHILDS_BRIDGE.md#a-narrow-route-through-the-anchor) gives exact locations. Reading the entire notes is unnecessary for this route.

The notes establish the foundations. The bridge supplies the missing connections to the project and points to the authoritative proofs. Primary research citations retain their separate role in attributing the paired-power mechanism and comparing the resulting guarantees.

## Two connected routes

Start with the [Childs-to-project bridge](CHILDS_BRIDGE.md) for a continuous explanation: a complete two-state example, a detuned completion that defeats repetition, spectral isolation, exact null cancellation, the two signal-response arguments, and their implementation cost.

Use the [30-milestone map](MILESTONES.md) to organize the dependencies of the full scientific account:

| Phase | Understanding developed | Integration point |
|---|---|---|
| Background/preliminaries, M01–M12 | States, available operations, query costs, spectral phases, errors, amplification, evolution and lower bounds | [M12: the complete problem](MILESTONES.md#m12-the-complete-problem-before-the-new-mechanism) |
| Narrative/innovation, M13–M30 | The controlled mechanism, separate theorems, optimality, native controls, precision, evidence and attribution | [M30: the complete scientific account](MILESTONES.md#m30-the-complete-scientific-account) |

Each milestone has a central question, an understanding target, earlier dependencies, a conceptual connection and source pointers. The map describes the project independently of a reader's background or progress.

For exact assumptions and theorem statements, enter through the [scientific model](../science/model.md). The [resource account](../science/resources.md), [related work](../references/RELATED_WORK.md) and [reproduction guide](../verification/README.md) connect those results to implementation, attribution and finite checks.
