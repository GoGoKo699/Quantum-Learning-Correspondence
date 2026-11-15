# Thirty milestones for understanding quantum correspondence learning

This map follows one scientific question: **what can a learner lose when it keeps every quantum specimen but forgets which input belongs to which output?** Its milestones describe the project's conceptual dependencies for any reader. They do not attempt to replace every specialist proof or cover all of quantum learning.

The allocation is **12 background/preliminary milestones** and **18 narrative/innovation milestones**. The background begins with individual specimens, channels and measurements, then assembles the complete acquisition experiment. The narrative begins with the source and its local correlations, builds the global anonymous-data bound, constructs the paired learner and finishes with prediction and resource interpretation.

The single educational anchor is John Watrous, *The Theory of Quantum Information* (2018). The [Watrous bridge](WATROUS_BRIDGE.md) gives verified textbook reading routes, notation translations and the steps supplied by this project. References below to an anchor topic mean the corresponding route in that bridge; the canonical proofs remain in [science](../science/README.md).

## Phase I: background and preliminaries — M01–M12

<a id="m01"></a>

### M01 — A specimen is not a state description

**Central question.** What information does receiving an unknown quantum register actually supply?

**Understanding target.** Distinguish the density operator describing a specimen, a classical specification of that operator and the measurement outcome obtained from one copy. Explain why a source can privately know a preparation circuit without giving that knowledge to the learner.

**Dependencies and story role.** No earlier milestone is required. This establishes the local object that both acquisition interfaces receive.

**Conceptual connection.** The source supplies native quantum examples rather than a table of amplitudes or a chosen-input oracle. That distinction is needed before comparing paired and anonymous data.

**Source pointers.** Watrous §§2.1.2 and 2.3.1, via the [bridge](WATROUS_BRIDGE.md); [model, quantum demonstrations](../science/model.md#quantum-demonstrations); [resources, preparing the same specimens](../science/resources.md#preparing-the-same-specimens).

<a id="m02"></a>

### M02 — Private randomness becomes a mixed state

**Central question.** How does a random pure preparation appear when its classical seed is unavailable?

**Understanding target.** Explain ensemble averaging and distinguish a hidden classical label from a label delivered with the state. Recognize that many ensembles can realize the same density operator and that a learner's probabilities are computed from the state it actually receives.

**Dependencies and story role.** Uses M01. It connects one specimen to a source that repeatedly draws private random states.

**Conceptual connection.** Averaging the source seed is a physical information boundary. Retaining or revealing that record would create a different learning experiment.

**Source pointers.** Watrous §§2.1.2–2.1.3 and 5.3.3, via the [bridge](WATROUS_BRIDGE.md); [model, quantum demonstrations](../science/model.md#quantum-demonstrations); [resources, chronology](../science/resources.md#why-chronology-matters).

<a id="m03"></a>

### M03 — Invisible marginals can hide a visible relation

**Central question.** Can two registers contain useful joint information when each register alone contains none?

**Understanding target.** Compute or reason about reduced states and distinguish a product state from a correlated state with the same marginals. Explain why a parameter-independent marginal does not imply a parameter-independent joint state.

**Dependencies and story role.** Uses M01–M02. It moves from one specimen to the input–output pair that carries the hidden transformation.

**Conceptual connection.** Both local marginals of the demonstration source are $`I/d`$. The learnable content lies in their relation, making correspondence potentially consequential.

**Source pointers.** Watrous §2.1.3, via the [bridge](WATROUS_BRIDGE.md); [model, quantum demonstrations](../science/model.md#quantum-demonstrations); [kernel, uniform-marginal sources](../science/correlation-kernel.md#uniform-marginal-sources).

<a id="m04"></a>

### M04 — A learned transformation is a physical channel

**Central question.** What must it mean for a learned device to transform a new input?

**Understanding target.** Distinguish a unitary target, an arbitrary trace-preserving quantum channel and a classical estimate of a unitary. Explain how initialization, quantum memory and measurement feedback can be combined into a channel acting on a later input.

**Dependencies and story role.** Uses M01–M03. It introduces the eventual operational output without assuming the learner must produce classical parameters.

**Conceptual connection.** The strongest converse will allow a consumable quantum program. Its limitation cannot be attributed merely to a demand for a classical description.

**Source pointers.** Watrous §§2.2.1–2.2.2, via the [bridge](WATROUS_BRIDGE.md); [prediction, processor and score](../science/prediction.md#the-processor-and-its-score).

<a id="m05"></a>

### M05 — A POVM includes every collective decoding strategy

**Central question.** How can one bound a learner without listing its measurement algorithm?

**Understanding target.** Read a POVM as positive effects summing to the identity and express a discrimination success probability using those effects. Explain why initialized ancillas, adaptive measurements and intermediate classical records induce a POVM on the original received state.

**Dependencies and story role.** Uses M01 and M04. It makes a measurement-independent converse possible.

**Conceptual connection.** The anonymous learner is allowed to try quantum matching and global inference. A bound on every POVM includes these attempts, rather than assuming that each specimen is measured separately.

**Source pointers.** Watrous §§2.3.1 and 3.1.2, via the [bridge](WATROUS_BRIDGE.md); [information ceiling, direct discrimination inequality](../science/information-ceiling.md#a-direct-discrimination-inequality); [model, acquisition interfaces](../science/model.md#two-acquisition-interfaces).

<a id="m06"></a>

### M06 — Forgetting a permutation is a channel

**Central question.** What is the quantum state of an ordered list after its hidden reordering is forgotten?

**Understanding target.** Distinguish a known permutation, a permutation accompanied by an accessible record and a uniformly randomized permutation whose record is unavailable to the learner. Explain why the learner's reduced state in the last case averages the corresponding conjugations, whether the record is destroyed or retained elsewhere.

**Dependencies and story role.** Uses M02–M05. It connects classical metadata loss to a precise quantum input state.

**Conceptual connection.** The anonymous source preserves every physical register while discarding a relation between registers. Its definition must specify which randomness or environment records are unavailable.

**Source pointers.** Watrous §§2.2.1 and 7.1.1, via the [bridge](WATROUS_BRIDGE.md); [model, acquisition interfaces](../science/model.md#two-acquisition-interfaces).

<a id="m07"></a>

### M07 — Swap and Bell readout describe joint structure

**Central question.** Why are the swap operator and Bell basis useful for an input–output pair?

**Understanding target.** Explain the action of swap, its symmetric and antisymmetric sectors and the role of a maximally entangled Bell basis in joint measurement. Distinguish entanglement in a measurement basis from entanglement in the supplied source state.

**Dependencies and story role.** Uses M03 and M05. It supplies local algebra that later connects the separable source to an exact decoding equation.

**Conceptual connection.** The demonstration state is separable, while its useful readout can be a Bell measurement. These are compatible properties of different parts of the experiment.

**Source pointers.** Watrous §§2.1.3, 6.3.1 and 7.1.1, via the [bridge](WATROUS_BRIDGE.md); [paired learning, Pauli labels and Bell states](../science/paired-learning.md#pauli-labels-and-bell-states); [model, source preparation](../science/model.md#quantum-demonstrations).

<a id="m08"></a>

### M08 — Operator geometry turns correlations into matrices

**Central question.** How can a bipartite quantum source be described by an ordinary real correlation matrix?

**Understanding target.** Use a traceless Hermitian operator basis and its Hilbert–Schmidt orthogonality. Explain what the coefficients in $`T`$ encode, why physical positivity remains an extra condition and how Cauchy–Schwarz controls an operator overlap.

**Dependencies and story role.** Uses M03 and M07. It connects local quantum operators to the matrix expression used by the global proof.

**Conceptual connection.** The cycle calculation needs only two operator factors at each register. Orthogonality, rather than a commuting-source assumption, performs the contractions.

**Source pointers.** Watrous Chapter 1, operator-space foundations, via the [bridge](WATROUS_BRIDGE.md); [kernel, uniform-marginal sources](../science/correlation-kernel.md#uniform-marginal-sources); [information ceiling, discrimination proof](../science/information-ceiling.md#a-direct-discrimination-inequality).

<a id="m09"></a>

### M09 — Purity, entropy and accessible information are different

**Central question.** How can a bound on a state's purity limit information about its hidden preparation parameter?

**Understanding target.** Distinguish purity, von Neumann entropy, relative entropy and Holevo information. Explain why comparison with a parameter-independent maximally mixed reference can upper-bound the information available from every measurement, without claiming the bound is achievable.

**Dependencies and story role.** Uses M02, M05 and M08. It introduces the information bridge needed after the kernel is bounded.

**Conceptual connection.** A finite purity ratio for the entire anonymous batch will give a finite information ceiling, even as the number of physical specimens grows.

**Source pointers.** Watrous §§5.2.1–5.2.2 and 5.3.3, via the [bridge](WATROUS_BRIDGE.md); [information ceiling, reference-state bound](../science/information-ceiling.md#a-reference-state-entropy-bound).

<a id="m10"></a>

### M10 — Pauli transformations have finite-field labels

**Central question.** How does an unknown quantum transformation become a set of binary unknowns?

**Understanding target.** Interpret a Pauli label $`w=(x,z)`$, ignore its global phase appropriately and distinguish the quadratic transpose sign $`q(w)`$ from the bilinear symplectic form $`[b,w]`$. Explain how these algebraic objects describe commutation and Bell-basis signs.

**Dependencies and story role.** Uses M07–M08. It prepares the explicit paired algorithm while retaining a physical meaning for its binary equations.

**Conceptual connection.** The target class has $`d^2`$ Pauli operators orthogonal in the Hilbert–Schmidt inner product but only $`2n`$ label bits. The paired source will reveal those bits through joint specimen measurements.

**Source pointers.** Watrous §2.1.3 and the operator foundations in Chapter 1, via the [bridge](WATROUS_BRIDGE.md); [paired learning, Pauli labels](../science/paired-learning.md#pauli-labels-and-bell-states). The project's finite-field derivation is supplied locally.

<a id="m11"></a>

### M11 — Entanglement fidelity diagnoses a learned channel

**Central question.** Why can a test on half an entangled pair reveal a limitation on ordinary input-averaged prediction?

**Understanding target.** Distinguish a channel's normalized Choi state, its target-relative entanglement fidelity and its fidelity averaged over Haar-random pure inputs. Explain why the fixed reference is a diagnostic device rather than an extra call to the unknown transformation.

**Dependencies and story role.** Uses M04, M05, M07 and M10. It joins channel learning to state discrimination.

**Conceptual connection.** An accurate learned Pauli channel would produce the corresponding Bell state. A Bell measurement would then identify the Pauli, creating the reduction used by the prediction converse.

**Source pointers.** Watrous §§2.2.2 and 2.1.3, via the [bridge](WATROUS_BRIDGE.md); [prediction, discrimination reduction](../science/prediction.md#proof-turn-a-useful-program-into-a-discriminator).

<a id="m12"></a>

### M12 — Assemble the complete causal experiment

**Central question.** Which information and operations distinguish the two learners before any theorem is applied?

**Understanding target.** Describe the whole sequence: a fixed hidden transformation, independent private random preparations, either retained or erased pairing, unrestricted processing and a classical label or later quantum output. Identify source descriptions, chosen-input calls and hidden records as additional resources if supplied.

**Dependencies and story role.** Integrates M01–M11. This completes the background phase by turning its local objects into one precise access model.

**Conceptual connection.** The scientific comparison becomes meaningful only when both learners receive the same specimens and differ in the declared acquisition information.

**Source pointers.** [Model](../science/model.md); [resources](../science/resources.md); [Watrous bridge](WATROUS_BRIDGE.md).

## Phase II: narrative and innovation — M13–M30

<a id="m13"></a>

### M13 — Build the separable demonstration source

**Central question.** How does a private random input produce the transformed-swap pair state?

**Understanding target.** Connect the state 2-design second moment to $`\rho_{U,1}=(I+F_U)/[d(d+1)]`$. Explain why stabilizer-state preparation makes the Pauli example explicit and why the preparation seed remains private. Interpret lower visibility as uncorrelated mixing.

**Dependencies and story role.** Uses M02, M03, M07 and M12. It starts the narrative with the actual source rather than an assumed data oracle.

**Conceptual connection.** Separability and efficient native preparation coexist with useful joint readout. Ideal visibility does not mean the local registers contain perfectly correlated values of a fixed observable.

**Source pointers.** [Model, quantum demonstrations](../science/model.md#quantum-demonstrations); [resources, preparation](../science/resources.md#preparing-the-same-specimens); [related work](../references/RELATED_WORK.md).

<a id="m14"></a>

### M14 — Express correspondence erasure exactly

**Central question.** What changes mathematically when one output list is globally shuffled?

**Understanding target.** Read the permutation average defining $`\Omega_{N,v}(U)`$ and distinguish independent source draws from the common hidden transformation. Explain why the learner still has both lists and all quantum registers, and why the state averages unavailable metadata.

**Dependencies and story role.** Uses M06, M12 and M13. It identifies the precise object whose learnability must be bounded.

**Conceptual connection.** The anonymous interface is more permissive than an individual-measurement model. Any matching inference must operate on this complete averaged state.

**Source pointers.** [Model, two interfaces](../science/model.md#two-acquisition-interfaces); [kernel, uniform-marginal formulation](../science/correlation-kernel.md#uniform-marginal-sources).

<a id="m15"></a>

### M15 — Two possible matchings form cycles

**Central question.** Why does the overlap of two anonymous states reduce to one relative permutation?

**Understanding target.** Explain how a common relabeling removes one permutation from the double average. Describe the alternating cycles formed by the two matchings and why disjoint cycles factorize under the trace.

**Dependencies and story role.** Uses M08 and M14. It is the first structural step that makes the factorial mixture tractable.

**Conceptual connection.** The relative-permutation graph replaces a large quantum-state expression with independent correlation loops, without choosing a measurement.

**Source pointers.** [Kernel, reducing two matchings to one](../science/correlation-kernel.md#proof-reducing-two-matchings-to-one).

<a id="m16"></a>

### M16 — Tracelessness selects whole correlation loops

**Central question.** Which terms survive when identity and correlation factors are expanded around one cycle?

**Understanding target.** Explain why one traceless factor at a register gives zero, so a surviving cycle uses either no correlation edges or all of them. Derive conceptually the cycle weight $`1+\mathrm{Tr}[(TS^{\mathsf T})^\ell]`$ and recognize why noncommuting local bases do not invalidate it.

**Dependencies and story role.** Uses M08 and M15. It supplies the load-bearing quantum contraction step before any counting formula is applied.

**Conceptual connection.** The degree-two overlap graph needs only second-order orthogonality. A statement about a commuting Pauli subfamily is not being substituted for the general operator proof.

**Source pointers.** [Kernel, cycle-contraction proof](../science/correlation-kernel.md#proof-reducing-two-matchings-to-one); [verification](../verification/README.md).

<a id="m17"></a>

### M17 — Sum all cycle types with one determinant

**Central question.** How does a sum over every permutation become a determinant generating function?

**Understanding target.** Interpret cycle counts and the factor $`\ell^{m_\ell}m_\ell!`$ in their enumeration. Connect the exponential cycle index to $`(1-z)^{-1}\det(I-zTS^{\mathsf T})^{-1}`$ and distinguish a formal identity from an asymptotic approximation.

**Dependencies and story role.** Uses M15–M16. It joins the local loop calculation into the exact finite-batch kernel.

**Conceptual connection.** The generating function encodes every batch size at once. Classical cycle-index methods are inherited; their application to the full received density operator supplies the collective-learner scope.

**Source pointers.** [Kernel, summing cycle types](../science/correlation-kernel.md#proof-summing-cycle-types); [related work](../references/RELATED_WORK.md).

<a id="m18"></a>

### M18 — Strict contraction makes the global purity finite

**Central question.** Which property of the source stops correlation loops from accumulating without bound?

**Understanding target.** Interpret the singular values of $`T`$, explain the nonnegative coefficients in the self-kernel and show why $`\|T\|_{\mathrm{op}}\lt1`$ gives $`K_N(T,T)\le\det(I-TT^{\mathsf T})^{-1}`$ for every $`N`$. Distinguish this sufficient ceiling from a claim at singular value one.

**Dependencies and story role.** Uses M08 and M17. It turns an exact formula into a uniform bound on the entire batch.

**Conceptual connection.** Uniform local marginals remove direct local parameter information; strictly contractive correlations make the remaining anonymous loops summable.

**Source pointers.** [Kernel, theorem](../science/correlation-kernel.md#theorem-4-cycle-and-determinant-formulas); [strict-contraction meaning](../science/correlation-kernel.md#what-strict-contraction-means).

<a id="m19"></a>

### M19 — Specialize the ceiling to less than one nat

**Central question.** Why does the transformed-swap source have a dimension-uniform information ceiling?

**Understanding target.** Explain why its correlation matrix has $`d^2-1`$ singular values equal to $`t=v/(d+v)`$. Connect its exact purity partial sum to $`C_{d,v}`$ and the entropy inequality to $`\chi\le\log C_{d,v}\lt1`$. Distinguish the exact all-$`N`$ statement from its fixed-$`v`$, large-$`d`$ interpretation.

**Dependencies and story role.** Uses M09, M13 and M18. It produces the first complete information-theoretic conclusion of the narrative.

**Conceptual connection.** More specimens increase the Hilbert-space dimension, yet the normalized purity ratio remains bounded. The source's shrinking per-direction correlations balance its growing operator dimension.

**Source pointers.** [Kernel, transformed-swap specialization](../science/correlation-kernel.md#specialization-to-transformed-swap-demonstrations); [information ceiling, one nat](../science/information-ceiling.md#less-than-one-nat-for-transformed-swap-pairs).

<a id="m20"></a>

### M20 — Turn purity into a decoding success bound

**Central question.** How can the state-level ceiling bound an arbitrary learner's chance of guessing one of many labels?

**Understanding target.** Explain the Hilbert–Schmidt Cauchy–Schwarz argument across all POVM effects and why $`E_i^2\le E_i`$ gives $`P_{\mathrm{guess}}\le\sqrt{C/M}`$ for a uniform $`M`$-state ensemble. Recognize the uniform-prior assumption and the bound's independence from decoding time.

**Dependencies and story role.** Uses M05, M08 and M18. It converts the global state bound into an explicit operational restriction.

**Conceptual connection.** A general measurement need not resemble the paired Bell decoder. The inequality constrains it solely through the density operators it receives.

**Source pointers.** [Information ceiling, discrimination inequality](../science/information-ceiling.md#a-direct-discrimination-inequality).

<a id="m21"></a>

### M21 — The anonymous Pauli remains unidentified at every batch size

**Central question.** What does the success inequality imply for the project's concrete hidden transformation?

**Understanding target.** Substitute the $`d^2`$ Pauli labels to obtain $`P_{\mathrm{guess}}\le\sqrt{C_{d,v}}/d`$. Explain both the fixed-dimension error floor and the exponentially small high-dimensional success, preserving that the statement averages over the uniform hidden label and implies a worst-case obstruction.

**Dependencies and story role.** Uses M10, M19 and M20. It completes the anonymous identification side of the comparison.

**Conceptual connection.** The quantifier is every $`N`$, including arbitrarily large dimension-dependent batches. It is not an extrapolation from a finite computation or a claim that a learner cannot favor one known label.

**Source pointers.** [Information ceiling, Pauli application](../science/information-ceiling.md#applying-the-inequality-to-pauli-learning); [model, Theorem 2](../science/model.md#theorem-2-identifying-the-hidden-pauli).

<a id="m22"></a>

### M22 — A known pair supplies an exact Pauli equation

**Central question.** What information does the paired learner obtain that the global converse says cannot accumulate anonymously?

**Understanding target.** Connect the twisted-swap Bell eigenvalue to the support condition $`q(b+w)=0`$. Rewrite it as $`[b,w]+c=q(b)`$ with the augmented bit $`c=q(w)`$, and explain which physical pairing the Bell circuit needs.

**Dependencies and story role.** Uses M07, M10 and M13. It begins the constructive side with one demonstration and one valid equation.

**Conceptual connection.** The underlying ideal pair states commute in the known Bell basis, so this specific learner has a classical outcome description after joint readout. That does not weaken the unrestricted anonymous converse.

**Source pointers.** [Paired learning, one demonstration](../science/paired-learning.md#one-demonstration-gives-one-equation); [resources, paired learner](../science/resources.md#paired-learner).

<a id="m23"></a>

### M23 — Random equations span the target bits

**Central question.** Why does a small collection of Bell outcomes identify all the unknown bits with high probability?

**Understanding target.** Relate the quadratic Gauss sum to the Fourier bias $`1/(d+1)`$ of the allowed outcome set. Explain how this bounds every affine hyperplane's probability by $`2/3`$, and how a union bound controls failure of full affine span.

**Dependencies and story role.** Uses M10 and M22. It turns locally valid equations into a global high-confidence reconstruction.

**Conceptual connection.** The sample guarantee depends on the geometry of the entire outcome support, not an assumption that the equation coefficients are exactly uniform independent bits.

**Source pointers.** [Paired learning, span bound](../science/paired-learning.md#why-a-linear-number-of-equations-suffices); [verification](../verification/README.md).

<a id="m24"></a>

### M24 — Complete the matched efficient learning comparison

**Central question.** What does the entire paired protocol cost, and what has correspondence alone changed?

**Understanding target.** Connect Bell acquisition, augmented Gaussian elimination and Pauli output into a polynomial-time learner using $`O(n+\log(1/\delta))`$ demonstrations. Compare this uniform high-confidence guarantee with the arbitrary-$`N`$ anonymous upper bound while holding source preparation and private seeds fixed.

**Dependencies and story role.** Integrates M12–M23. It joins the two identification arguments into the central acquisition comparison.

**Conceptual connection.** The separation concerns access information rather than a quantum-versus-classical processing race. The efficient paired construction has no chosen-unitary calls or uncharged state descriptions.

**Source pointers.** [Paired learning, complete learner](../science/paired-learning.md#the-complete-learner); [resources](../science/resources.md); [scientific comparison](../science/README.md#principal-quantitative-comparison).

<a id="m25"></a>

### M25 — A consumable quantum program would also identify the Pauli

**Central question.** Could the learner keep the training data coherent and avoid the need to estimate the transformation?

**Understanding target.** Describe the most general fixed trace-preserving processor on the data and one later input. Explain why feeding half a fixed maximally entangled state and Bell-measuring the result induces a valid POVM on the training data, with success equal to target-relative entanglement fidelity.

**Dependencies and story role.** Uses M04, M05, M11 and M21. It extends the converse from a classical output label to the action of a quantum learned device.

**Conceptual connection.** All retained quantum data may be consumed on one prediction. The reduction therefore isolates an information obstruction rather than a classical-storage or reusability requirement.

**Source pointers.** [Prediction, processor](../science/prediction.md#the-processor-and-its-score); [prediction, reduction proof](../science/prediction.md#proof-turn-a-useful-program-into-a-discriminator).

<a id="m26"></a>

### M26 — Translate the obstruction into ordinary prediction quality

**Central question.** How does limited entanglement fidelity constrain the score on a fresh ordinary input?

**Understanding target.** Use the channel identity linking entanglement fidelity to Haar-average input fidelity. Compare the anonymous upper bound $`(\sqrt{C_{d,v}}+1)/(d+1)`$, the blind benchmark $`1/d`$ and the paired learner's fidelity at least $`1-d\delta/(d+1)`$, with all branches included.

**Dependencies and story role.** Uses M11, M24 and M25. It completes the operational prediction comparison on the same source and target class.

**Conceptual connection.** A fixed-dimensional positive error floor and a dimension-growing fidelity of order $`1/d`$ are distinct consequences of the same finite-batch theorem.

**Source pointers.** [Prediction theorem](../science/prediction.md#theorem-6-finite-batch-prediction-bound); [matched prediction](../science/prediction.md#matched-paired-data-prediction); [blind benchmark](../science/prediction.md#comparison-with-a-blind-device).

<a id="m27"></a>

### M27 — Identify which metadata and chronology are resources

**Central question.** Which apparently small changes in data delivery alter the stated conclusion?

**Understanding target.** Distinguish one globally anonymous batch from several independently shuffled batches with marked boundaries. Explain the upper bounds $`\chi\le B\log C_{d,v}`$ and $`P_{\mathrm{guess}}\le\min\{1,C_{d,v}^{B/2}/d\}`$ for $`B`$ such batches without claiming optimality or attainability. Locate pair lists, source seeds, storage and processing time in the resource account.

**Dependencies and story role.** Uses M12, M19, M21 and M26. It reconnects the mathematical guarantees to a complete physical acquisition process.

**Conceptual connection.** A larger anonymous batch is not equivalent to more separately identified batches. Extra grouping information changes the received quantum state.

**Source pointers.** [Resources, chronology](../science/resources.md#why-chronology-matters); [resources, batch count](../science/resources.md#one-batch-and-several-batches).

<a id="m28"></a>

### M28 — Preserve the boundaries of the theorem

**Central question.** Which restrictions are essential, and which stronger claims have not been established?

**Understanding target.** Explain why parameter-dependent marginals and singular value one fall outside the determinant ceiling. Distinguish a converse valid for $`0\lt v\le1`$ from an efficient exact-equation learner proved only at $`v=1`$. Identify postselected conditional fidelity, active unitary access and a hardware-noise threshold as different questions.

**Dependencies and story role.** Uses M18, M24, M26 and M27. It defines the exact scientific reach before the final synthesis.

**Conceptual connection.** Removing a theorem premise is not a contradiction. A restricted source-level impossibility should not become a universal claim that all anonymous quantum demonstrations are unlearnable.

**Source pointers.** [Kernel, contraction boundary](../science/correlation-kernel.md#what-strict-contraction-means); [paired learning, visibility endpoint](../science/paired-learning.md#why-the-visibility-endpoint-matters); [interpretation, resource boundaries](../science/interpretation.md#boundaries-that-matter-operationally).

<a id="m29"></a>

### M29 — Separate inherited tools, proved conclusions and finite checks

**Central question.** What establishes this contribution, and what does each form of evidence actually support?

**Understanding target.** Identify the inherited source, state-design preparation, cycle methods and information inequalities. Distinguish the local operator derivation and decision reductions from numerical corroboration. Explain why finite noncommuting matrix tests, Pauli support checks and decoder runs support their stated assertions but do not establish all-$`N`$ proofs or exhaustive priority.

**Dependencies and story role.** Uses M16–M28. It makes the complete account inspectable without substituting citation lists or test counts for the argument.

**Conceptual connection.** The quantum obstruction is established before measurement and then connected to an explicit task. The Pauli learner's classical outcome structure and the classical anonymous-data antecedents remain visible in that assessment.

**Source pointers.** [Related work](../references/RELATED_WORK.md); [verification](../verification/README.md); [interpretation, scientific relationship](../science/interpretation.md#scientific-relationship-to-earlier-learning-models).

<a id="m30"></a>

### M30 — Explain the complete correspondence-learning law

**Central question.** What changes in quantum learning when correspondence is removed, and why?

**Understanding target.** Give a coherent account from source preparation to output quality: private random inputs hide local information; known pairings expose exact equations; anonymous matching produces summable correlation loops; the resulting state-level ceiling limits every decoder and even a consumed quantum predictor. State the achieved paired guarantee, anonymous limitation, averaging convention and material boundaries together.

**Dependencies and story role.** Integrates M13–M29 and the access framework of M12. This concludes the narrative with the whole contribution, rather than one additional isolated lemma.

**Conceptual connection.** The result identifies correspondence as a substantive acquisition resource for this native quantum learning task. Its meaning comes from the matched specimens and explicit output comparison, not from the size of the Hilbert space alone.

**Source pointers.** [Scientific overview](../science/README.md); [model and theorems](../science/model.md); [interpretation](../science/interpretation.md); [Watrous bridge](WATROUS_BRIDGE.md).
