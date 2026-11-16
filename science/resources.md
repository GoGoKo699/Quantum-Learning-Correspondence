# Resources and acquisition boundaries

The comparison holds the quantum specimens fixed and changes whether their input–output correspondence is supplied before the learner acts. It therefore concerns the information delivered by a data-acquisition interface. The anonymous converse grants arbitrary quantum processing; processing time is not the resource used to establish its impossibility.

## Preparing the same specimens

For the explicit Pauli task, set $`d=2^n`$ and $`v=1`$. For each demonstration, the source samples a uniformly random stabilizer state, prepares two specimens of that known sampled state, and applies the same hidden Pauli to the second specimen. The source may prepare both specimens because it knows the classical sampling seed. The learner receives neither that seed nor a preparation circuit.

Uniform stabilizer states are an exact projective 2-design. Standard Clifford sampling and synthesis give polynomial classical sampling work and polynomial gate count per demonstration; this construction does not require a table of $`2^n`$ amplitudes or QRAM. The [model](model.md) derives the resulting density operator. The source's randomness, Clifford preparation, two $`n`$-qubit registers and one application of the hidden transformation per demonstration are charged resources. Intra-register stabilizer entanglement is allowed; the two members of a demonstration are separable across $`A:B`$.

The source can generate the same ensemble for $`0\lt v\lt1`$ by mixing correlated demonstrations with uncorrelated maximally mixed pairs, with the mixing weight in the model. The information converse covers that range. The efficient paired decoder proved here uses the ideal endpoint $`v=1`$.

## Paired learner

One Bell measurement on each corresponding pair uses $`n`$ CNOTs, $`n`$ Hadamards and $`2n`$ single-qubit measurement outcomes. The resulting row has $`2n+1`$ binary coefficients and one binary right-hand side. Gaussian elimination can stream these rows, retaining polynomial classical memory and using polynomial classical work. A direct elimination on $`N`$ rows costs at most $`O(Nn^2+n^3)`$ elementary binary operations. No quantum state must persist between demonstrated pairs once its Bell outcome is recorded.

For failure probability $`\delta`$, the [paired theorem](paired-learning.md) gives $`N=O(n+\log(1/\delta))`$. The learner can then apply the identified Pauli to fresh inputs with at most $`n`$ single-qubit Pauli operations per use. This is an explicit efficient recovery algorithm for the source model; it is not an optimal total-resource theorem over all possible learning experiments.

## Anonymous learner

The anonymous learner receives every input and output register, with its physical list position, after one uniformly random permutation of the entire output list. All $`2nN`$ specimen qubits may be stored and processed coherently. The learner can attempt quantum matching, adaptive readout or any other joint strategy. Work registers and computation are unrestricted in the converse. A later quantum program may consume the whole training batch to process one fresh input.

No access is supplied to the permutation record, a purification of the erasure, the preparation seeds, further target calls, chosen input probes, inverse preparation or repeated specimens tied to a revealed seed. In particular, the learner has no opportunity to measure the true pairs before they are shuffled.

Producing a uniformly random permutation itself needs randomness and physical routing. An implementation may charge those operations separately. The theorem studies the resulting source channel and does not claim a runtime improvement from shuffling. Describing a complete arbitrary correspondence after the shuffle would take $`\lceil\log_2(N!)\rceil`$ bits in a fixed-length index. This observation is not a proof that that many metadata bits are necessary for learning: the optimal partial-correspondence budget is a different question. In the paired interface, preserved physical routing may already provide the association without a separate transmitted index.

## Separate collective readout of a growing list

The [separate-list receiver](separate-list-readout.md) acts on the same anonymous source. It stores each whole list coherently until a collective projective measurement of that list. No quantum gate between the input and output lists is needed. Entangling control within each list remains available, and the source still supplies all $`2nN`$ specimen qubits when $`d=2^n`$.

For a fixed finite set of Fourier frequencies, a normalized-Hilbert–Schmidt almost-commuting theorem provides exactly commuting approximants and their common spectral projectors. A diagonal schedule refines that frequency set as the batch grows. This proves that a target-independent receiver exists; it does not bound useful gate complexity, measurement synthesis, runtime, or noise sensitivity. The classical spectral labels and the subsequent classical processing may also be costly. No small classical-record theorem is asserted.

The reconstruction map prepares the known normalized projector $`P_i/\mathrm{Tr}P_i`$ on each side. This is a parameter-independent physical preparation, used to certify statistical sufficiency. It supplies no permutation, preparation seed, purification, unknown-target call, or extra specimen of a privately chosen source state. The maximally mixed reference and Gaussian variables in the proof are mathematical comparison devices, not additional source records delivered to a protocol.

The theorem fixes local dimensions and a compact physical correlation family whose operator norms stay strictly below one. It proves uniform trace-norm recovery and equivalence to one Gaussian covariance observation. It gives no finite-size rate, dimension-growing guarantee or derivative bound. In particular, preservation of bounded risk up to $`o(1)`$ does not imply convergence of Fisher information or equality of a precision coefficient after multiplying errors by a growing sample budget.

## Why chronology matters

For the Pauli family, the paired density operators commute in one Bell basis. Bell measurement of the actual pairs therefore produces a sufficient classical record for their identification task. Erasing association after that measurement cannot remove information already encoded in those records. The impossibility theorem applies when the association disappears before any learner interaction with the specimens.

Classical descriptions of the privately sampled stabilizer states would supply a richer dataset. Their potential usefulness is not bounded by a theorem for the two native state specimens. Conversely, the all-measurement converse cannot be inferred just by analyzing one local measurement of the anonymous specimens; its proof is at the density-operator level.

## One batch and several batches

The information ceiling applies for every size of one globally anonymous batch. If the source marks several independently shuffled batches, their tensor product is a different input. For $`B`$ marked batches, subadditivity and the same relative-entropy comparison give the valid upper bound $`B\log C_{d,v}`$ on the Holevo information, and the collision argument gives

```math
P_{\mathrm{guess}}\le
\min\left\{1,\frac{C_{d,v}^{B/2}}d\right\}
```

for the uniform Pauli task. These are upper bounds; they do not establish optimal dependence on batch count or its attainability. Taking every batch to contain one known input–output pair recovers the paired acquisition interface, so no contradiction is present.

For $`m`$ independent tagged batches of $`b`$ pairs, applying the separate-list receiver to each batch uses all $`mb`$ supplied pairs. Tensorization gives reconstruction error at most $`m\varepsilon_b`$, where $`\varepsilon_b\to0`$ is the one-batch normalized-Hilbert–Schmidt error bound and also bounds its trace error. Hence fixed $`m`$ is covered as $`b\to\infty`$. Simultaneous growth needs $`m(b)\varepsilon_b\to0`$, or an explicit diagonal choice of batch size large enough for a stated number of batches and error. The existence proof provides no unrestricted two-parameter rate or exact many-batch precision law.

## Implementation limits

The protocol assumes ideal state preparation, gates, readout and stored specimens. The anonymous information bound also holds at lower source visibility, but no efficient decoder under fixed noisy parity constraints, fault threshold, laboratory timing estimate or hardware crossover is established. All successful and unsuccessful branches of a processor are included in its prediction score; conditional fidelity after postselection needs its success probability charged separately. The [interpretation](interpretation.md) states the supported scientific conclusion within these boundaries.
