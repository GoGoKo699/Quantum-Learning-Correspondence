# Thirty milestones for correspondence loss and surviving information

This map follows one question: **what is lost when every quantum specimen is retained but its input–output matching is erased, and how can all surviving information be read out?** Its thirty targets describe the project's conceptual dependencies for any reader, rather than personal learner progress or an exhaustive survey of quantum learning.

There are **ten background/preliminary milestones** and **twenty narrative/innovation milestones**. The background assembles specimens, channels, decisions, likelihood geometry and sufficiency. The narrative develops the paired-versus-anonymous learning separation, then uses the exact kernel to identify and attain the complete growing-batch Gaussian experiment. Within each phase the route moves from local objects to the global scientific account.

The common educational anchor is Dénes Petz, *Quantum Information Theory and Quantum Statistics*, first edition (2008). The [Petz bridge](PETZ_BRIDGE.md) gives the verified section routes and separates textbook foundations from project-specific proofs. The [worked examples](WORKED_EXAMPLES.md) check concrete parts of the story; the scientific pages remain canonical for claims.

## Phase I: background and preliminaries — M01–M10

<a id="m01"></a>

### M01 — A specimen and its hidden preparation

**Central question.** What does receiving a native quantum example supply?

**Understanding target.** Distinguish one quantum register, its density-operator description, a privately known preparation seed and a classical measurement record. Explain why revealing the seed changes the supplied experiment.

**Dependencies and story role.** No earlier target is required. This identifies the basic object shared by the paired and anonymous interfaces before either learner acts.

**Source pointers.** [Model](../science/model.md); [Petz bridge](PETZ_BRIDGE.md).

<a id="m02"></a>

### M02 — Information can live only in a relation

**Central question.** Can two parameter-independent lists retain parameter-dependent joint information?

**Understanding target.** Distinguish maximally mixed marginals from a product state and use a traceless Hermitian basis to encode a physical source by its real correlation matrix T. Keep positivity as a separate condition on that matrix.

**Dependencies and story role.** Uses M01. Moving from an individual specimen to a correlated input–output pair explains why pairing can carry a resource.

**Source pointers.** [Uniform-marginal sources](../science/correlation-kernel.md#uniform-marginal-sources); [Petz bridge](PETZ_BRIDGE.md).

<a id="m03"></a>

### M03 — A forgotten record is a channel

**Central question.** How does an unavailable classical permutation change a quantum dataset?

**Understanding target.** Write the average of permutation conjugations and distinguish it from a known routing, an accessible permutation register and projection onto a symmetric subspace. Explain when the averaging occurs in the causal experiment.

**Dependencies and story role.** Uses M01–M02. This gives correspondence erasure a physical state description rather than treating it as an estimator's inconvenience.

**Source pointers.** [Acquisition interfaces](../science/model.md#two-acquisition-interfaces); Petz §§9.1–9.2 via the [bridge](PETZ_BRIDGE.md).

<a id="m04"></a>

### M04 — A measurement includes the whole learner

**Central question.** How can a converse cover adaptive matching and arbitrary collective processing?

**Understanding target.** Interpret a POVM as positive effects summing to identity. Compose initialized ancillas, feedback and all output branches into a measurement on the supplied state, and express identification or bounded decision risk using it.

**Dependencies and story role.** Uses M01–M03. It establishes the measurement-independent scope of the anonymous converse and the operational meaning of later reconstruction.

**Source pointers.** [Information and identification](../science/information-ceiling.md); [supplementary measurement foundations](WATROUS_BRIDGE.md).

<a id="m05"></a>

### M05 — A likelihood has a reference and a norm

**Central question.** Why normalize the anonymous density operator by the full Hilbert-space dimension?

**Understanding target.** Define the maximally mixed reference, normalized trace and likelihood L_N=D_N Omega_N. Distinguish normalized Hilbert–Schmidt norm, ordinary Hilbert–Schmidt norm and trace norm; translate a likelihood L2 error into density-operator trace error without an exponentially growing factor.

**Dependencies and story role.** Uses M02 and M04. This puts the exact kernel and the later receiver proof in the same geometry.

**Source pointers.** [Kernel](../science/correlation-kernel.md); [separate-list theorem](../science/separate-list-readout.md); [norm conventions](PETZ_BRIDGE.md#fix-the-projects-conventions).

<a id="m06"></a>

### M06 — An information ceiling is not an attaining measurement

**Central question.** What does a purity bound say, and what does it leave open?

**Understanding target.** Distinguish purity, entropy, relative entropy, Holevo information and measurement outcomes. Explain how comparison with a fixed maximally mixed reference upper-bounds information for every prior, without identifying a readout that preserves the available information.

**Dependencies and story role.** Uses M04–M05. This separates the original impossibility conclusion from the later sufficiency question.

**Source pointers.** [Reference-state entropy bound](../science/information-ceiling.md#a-reference-state-entropy-bound); Petz §§3.3–3.5 and §5.5 via the [bridge](PETZ_BRIDGE.md).

<a id="m07"></a>

### M07 — Bell measurements and Pauli labels

**Central question.** How do a joint measurement and a binary label describe a transformation?

**Understanding target.** Explain swap sectors, the Pauli transpose sign, the quadratic form q and the symplectic form. Distinguish entanglement in the Bell measurement from entanglement in supplied pairs, and identify a fixed entangled reference as a diagnostic rather than an extra unknown-unitary query.

**Dependencies and story role.** Uses M02 and M04. It prepares both the explicit paired learner and the prediction-to-discrimination reduction.

**Source pointers.** [Pauli and Bell algebra](../science/paired-learning.md#pauli-labels-and-bell-states); [prediction](../science/prediction.md); [worked examples](WORKED_EXAMPLES.md).

<a id="m08"></a>

### M08 — Sufficiency requires a physical reverse map

**Central question.** When does a classical readout retain an entire quantum statistical experiment?

**Understanding target.** State a target-independent measurement and reconstruction criterion. Distinguish a scalar conditional expectation onto an abelian algebra from block pinching that leaves quantum states inside degenerate blocks. Recognize why an upper information bound or a target-chosen receiver is insufficient.

**Dependencies and story role.** Uses M03–M06. It sets the operational standard that the growing-batch construction must meet.

**Source pointers.** Petz §§9.1–9.2 and §9.5 via the [bridge](PETZ_BRIDGE.md); [classical reconstruction example](WORKED_EXAMPLES.md#a-spectral-label-must-become-a-classical-record).

<a id="m09"></a>

### M09 — Gaussian likelihoods and bounded Fourier observables

**Central question.** What is needed to describe a complete covariance experiment?

**Understanding target.** Read a centered block covariance with identity local marginals and a target-dependent cross-correlation. Distinguish characteristic-function convergence from L2 approximation of a full likelihood, and explain why finite Fourier sums can approximate a compact Gaussian likelihood family.

**Dependencies and story role.** Uses M02, M05 and M08. It supplies the probability language for a candidate limit without assuming that covariance agreement already proves sufficiency.

**Source pointers.** [Separate-list theorem](../science/separate-list-readout.md); [Petz bridge, project proof](PETZ_BRIDGE.md#the-source-specific-proof-bridge).

<a id="m10"></a>

### M10 — Keep the interface and the limits visible

**Central question.** Which resources and limiting orders make each comparison meaningful?

**Understanding target.** Describe one globally anonymous batch, several independently shuffled tagged batches, and paired observations as different inputs. Fix dimensions and the strict correlation gap before taking a large-batch limit; distinguish bounded decision risk from Fisher information and a risk scaled by a growing sample budget.

**Dependencies and story role.** Integrates M01–M09. The local concepts now form a complete acquisition and decision experiment before the project-specific proofs begin.

**Source pointers.** [Resources](../science/resources.md); Petz §§10.1–10.3 via the [bridge](PETZ_BRIDGE.md).

## Phase II: narrative and innovation — M11–M30

<a id="m11"></a>

### M11 — Build the native separable source

**Central question.** How does private random preparation create the transformed-swap state?

**Understanding target.** Use the state-2-design second moment to obtain the ideal pair density operator. Explain exact stabilizer preparation for the Pauli example, why the seed is withheld, and how uncorrelated mixing produces lower visibility without adding source entanglement.

**Dependencies and story role.** Uses M01–M03 and M07. The narrative starts with the actual supplied specimens and their physically realizable preparation.

**Source pointers.** [Quantum demonstrations](../science/model.md#quantum-demonstrations); [preparing the same specimens](../science/resources.md#preparing-the-same-specimens).

<a id="m12"></a>

### M12 — Write the complete anonymous state

**Central question.** What remains after the common transformation acts and one list is shuffled?

**Understanding target.** Form Omega_N from independent copies conditional on one hidden target and a uniform output permutation. Identify the unavailable records and explain why a receiver may still store all specimens, attempt matching and process them jointly.

**Dependencies and story role.** Uses M03–M04 and M11. This is the common input for both the all-measurement converse and the new restricted attaining receiver.

**Source pointers.** [Two interfaces](../science/model.md#two-acquisition-interfaces); [uniform-marginal formulation](../science/correlation-kernel.md#uniform-marginal-sources).

<a id="m13"></a>

### M13 — Two matchings become one relative permutation

**Central question.** Why does the overlap of two factorial mixtures reduce to cycles?

**Understanding target.** Remove one permutation by trace invariance. Draw the alternating matching graph, identify relative-permutation cycles, and explain why disjoint cycles factorize before any measurement has been selected.

**Dependencies and story role.** Uses M05 and M12. This turns a large density-operator expression into local correlation loops.

**Source pointers.** [Reducing two matchings to one](../science/correlation-kernel.md#proof-reducing-two-matchings-to-one).

<a id="m14"></a>

### M14 — Whole loops produce an exact determinant kernel

**Central question.** Which expanded edges survive, and how are all cycle types counted?

**Understanding target.** Use tracelessness to exclude a partially selected cycle and two-factor orthogonality to derive its correlation trace. Sum cycle types by the exponential cycle index to obtain the exact determinant generating function, without a commuting-source or asymptotic assumption.

**Dependencies and story role.** Uses M02 and M13. This joins the local operator contraction to an exact statement for every batch size.

**Source pointers.** [Cycle contraction and determinant](../science/correlation-kernel.md#theorem-4-cycle-and-determinant-formulas); [classical antecedents](../references/RELATED_WORK.md).

<a id="m15"></a>

### M15 — Strict contraction controls every batch size

**Central question.** Why do the anonymous correlations stop accumulating without bound?

**Understanding target.** Interpret the singular values of T and the nonnegative self-kernel coefficients. Establish a finite determinant ceiling and its limiting value under correlation norm strictly below one; identify why the boundary at singular value one is outside this conclusion.

**Dependencies and story role.** Uses M05 and M14. It gives the full-batch norm bound that will support both the information ceiling and the later norm-saturation argument.

**Source pointers.** [Strict contraction](../science/correlation-kernel.md#what-strict-contraction-means); [two-pair calculation](WORKED_EXAMPLES.md#two-anonymous-pairs-and-a-nonzero-error-floor).

<a id="m16"></a>

### M16 — Translate the operator bound into learning limits

**Central question.** How does the kernel limit what every decoder can learn?

**Understanding target.** Derive the reference-state entropy bound and the direct many-label discrimination inequality. Specialize to transformed-swap sources and uniform Pauli labels, distinguish nats from bits, and explain the difference between an upper success bound and the exact optimum.

**Dependencies and story role.** Uses M04–M06 and M15. The first global consequence is a size-independent learning obstruction, even with unrestricted readout.

**Source pointers.** [Information ceiling](../science/information-ceiling.md); [main constants](../science/model.md#the-constants).

<a id="m17"></a>

### M17 — One known pair supplies one exact equation

**Central question.** How does a Bell outcome reveal a hidden Pauli constraint?

**Understanding target.** Derive the ideal Bell law and its forbidden quadratic-sign sector. Convert every valid outcome into the affine equation in the hidden Pauli bits and one augmented quadratic bit, retaining the same private source seeds and no extra target queries.

**Dependencies and story role.** Uses M07 and M11. It explains constructively what paired data can reveal that the anonymous learner cannot accumulate in one batch.

**Source pointers.** [One demonstration, one equation](../science/paired-learning.md#one-demonstration-gives-one-equation); [Bell example](WORKED_EXAMPLES.md#the-hidden-pauli-is-a-missing-bell-outcome).

<a id="m18"></a>

### M18 — Complete the efficient paired learner

**Central question.** Why do a linear number of those equations recover the transformation?

**Understanding target.** Use the quadratic Fourier coefficient to bound the mass of every affine hyperplane, then apply independence and a union bound to full-rank failure. Describe Bell acquisition and binary elimination, including the failure branch, and retain the ideal-visibility restriction of the clean decoder.

**Dependencies and story role.** Uses M17. This completes a matched efficient learning comparison rather than comparing the converse with an unspecified favorable protocol.

**Source pointers.** [Rank and complete learner](../science/paired-learning.md#why-a-linear-number-of-equations-suffices); [resources](../science/resources.md#paired-learner).

<a id="m19"></a>

### M19 — A consumable program has the same obstruction

**Central question.** Could retaining the whole dataset quantumly bypass identification?

**Understanding target.** Compose an arbitrary trace-preserving learned processor with a fixed maximally entangled diagnostic input and Bell readout. Explain why it induces a POVM on the data, convert entanglement fidelity to Haar-average transformation fidelity, and include every output branch.

**Dependencies and story role.** Uses M04, M07, M16 and M18. It shows that the anonymous limitation is in the supplied information rather than a demand for a classical model.

**Source pointers.** [Prediction proof](../science/prediction.md); [matched paired prediction](../science/prediction.md#matched-paired-data-prediction).

<a id="m20"></a>

### M20 — Identify the question left by the ceiling

**Central question.** What information survives the shuffle, and must it still be read jointly?

**Understanding target.** Explain why bounded anonymous information need not be zero and why the all-measurement ceiling says nothing about an attaining separate-list receiver. Define separate collective readout on each coherent list and distinguish it from Readout's old per-pair separable class.

**Dependencies and story role.** Integrates M11–M19 using M08–M10. The original result becomes the starting point for a stronger operational description of the surviving experiment.

**Source pointers.** [Separate-list theorem](../science/separate-list-readout.md); [Petz bridge](PETZ_BRIDGE.md); [Readout relationship](https://github.com/GoGoKo699/Quantum-Learning-Readout).

<a id="m21"></a>

### M21 — Match the candidate Gaussian likelihood norm

**Central question.** Why is one correlated Gaussian vector the right candidate limit?

**Understanding target.** Write the Gaussian density ratio relative to independent standard coordinates and integrate its square. Use the paired covariance eigenvalues to identify the determinant norm and show that it equals the entire quantum collision-norm limit.

**Dependencies and story role.** Uses M09 and M15. This exact match, rather than an approximate covariance analogy, supplies the budget that can rule out a hidden likelihood remainder.

**Source pointers.** [Full likelihood norm](../science/separate-list-readout.md#1-the-full-likelihood-norm); [Gaussian worked example](WORKED_EXAMPLES.md#the-gaussian-likelihood-uses-the-whole-collision-budget).

<a id="m22"></a>

### M22 — Read bounded fluctuations without knowing the matching

**Central question.** Why does shuffling disappear from local Fourier expectations?

**Understanding target.** Define a tensor power of a small local unitary on each list. Use separate permutation invariance to express its anonymous expectation as a single-pair expectation raised to N, then derive the correlated Gaussian characteristic function by a uniform second-order expansion.

**Dependencies and story role.** Uses M03, M09, M12 and M21. It identifies observable information that is actually available without a matching record or a target-dependent measurement.

**Source pointers.** [Bounded Fourier fluctuations](../science/separate-list-readout.md#2-bounded-fourier-fluctuations-approximate-the-entire-likelihood).

<a id="m23"></a>

### M23 — Turn weak Fourier limits into full-likelihood approximation

**Central question.** What excludes correlations invisible to the proposed fluctuation coordinates?

**Understanding target.** Compute the reference Fourier Gram limit and expand the squared distance from a finite Fourier sum. Combine its pairings with the matching full norm to identify the exact Gaussian approximation error. Explain why weak convergence alone would leave the decisive inference open.

**Dependencies and story role.** Uses M05, M21 and M22. This is the norm-saturation step that rules out a persistent quantum remainder beyond the Gaussian experiment.

**Source pointers.** [Full-likelihood approximation](../science/separate-list-readout.md#2-bounded-fourier-fluctuations-approximate-the-entire-likelihood); [finite diagnostics](../verification/README.md).

<a id="m24"></a>

### M24 — Choose one finite dictionary for the whole family

**Central question.** How can the receiver avoid depending on the unknown target?

**Understanding target.** Use compactness of the Gaussian likelihood family and density of finite Fourier sums to cover every target with finitely many approximants. Take the union of their local frequencies and distinguish the proof-only nearest-approximant assignment from the physical measurement settings.

**Dependencies and story role.** Uses M09 and M23. This supplies uniformity and removes a potential hidden genie from the attaining construction.

**Source pointers.** [Uniform Fourier approximation](../science/separate-list-readout.md#2-bounded-fourier-fluctuations-approximate-the-entire-likelihood).

<a id="m25"></a>

### M25 — Replace almost commuting local unitaries by commuting ones

**Central question.** Why can a genuinely joint local measurement read the whole dictionary?

**Understanding target.** Bound the normalized Hilbert–Schmidt commutator of collective generators using their traceless one-site commutator. Apply the Duhamel bound and Glebsky's fixed-finite-family theorem independently on each list; retain the dimension-independent norm and avoid an operator-norm claim.

**Dependencies and story role.** Uses M05, M22 and M24. This inherited approximation theorem converts the accessible but noncommuting Fourier observables into compatible local measurement settings.

**Source pointers.** [Commuting measurement construction](../science/separate-list-readout.md#3-one-commuting-measurement-on-each-list); [attribution](../references/RELATED_WORK.md).

<a id="m26"></a>

### M26 — Make the retained record fully classical

**Central question.** How do local spectral outcomes produce a physical product reconstruction?

**Understanding target.** Measure the common spectral projectors on each list and prepare their normalized projectors. Derive the scalar conditional expectation onto the product abelian algebra, its L2 projection property and why ordinary block pinching is insufficient when eigenspaces are degenerate.

**Dependencies and story role.** Uses M08 and M25. This identifies the exact channel that turns separate-list quantum specimens into classical data with a prescribed reverse map.

**Source pointers.** [Local measurement and preparation](../science/separate-list-readout.md#3-one-commuting-measurement-on-each-list); [spectral example](WORKED_EXAMPLES.md#a-spectral-label-must-become-a-classical-record).

<a id="m27"></a>

### M27 — Recover the full anonymous experiment uniformly

**Central question.** How do finite approximation levels yield one asymptotically sufficient receiver?

**Understanding target.** Use the conditional expectation's best-approximation property and the uniform finite dictionary to control normalized likelihood error. Choose a target-independent diagonal schedule and convert it to trace-norm state recovery; deduce all bounded decision and coherent-prediction score consequences by channel contraction.

**Dependencies and story role.** Uses M04–M05 and M23–M26. This establishes an operational comparison with every joint readout, rather than an isolated estimator or observable.

**Source pointers.** [Separate-list theorem](../science/separate-list-readout.md#theorem-7-asymptotic-separate-list-sufficiency); [decision and prediction consequences](../science/separate-list-readout.md#consequences-for-learning-and-coherent-prediction).

<a id="m28"></a>

### M28 — Complete both directions of the Gaussian experiment

**Central question.** Why does the measured record contain exactly one covariance observation?

**Understanding target.** Transfer bounded word moments to the commuting spectral law, obtain weak reference convergence on its compact coordinate space, and couple that law to Gaussian Fourier coordinates. Use conditional reference kernels and likelihood L1 control in both directions, with neither kernel depending on the target.

**Dependencies and story role.** Uses M09 and M24–M27. This upgrades a sufficient discrete receiver into the complete classical limiting statistical experiment.

**Source pointers.** [Two-way Gaussian comparison](../science/separate-list-readout.md#4-two-way-equivalence-with-the-gaussian-covariance-experiment).

<a id="m29"></a>

### M29 — Price storage and keep two growth limits separate

**Central question.** What remains unproved when both batch size and batch count grow?

**Understanding target.** Count all supplied pairs and coherent specimens on each side. Tensorize the one-batch recovery error for independently tagged batches, state the needed product-error condition, and explain why no useful rate, efficient synthesis, Fisher-information convergence or exact rescaled precision coefficient follows.

**Dependencies and story role.** Uses M10, M18–M19 and M27–M28. It connects the attaining receiver back to a physical resource account while preserving the old information ceiling.

**Source pointers.** [Tagged batches and limits](../science/separate-list-readout.md#independently-tagged-batches-and-limit-order); [resources](../science/resources.md).

<a id="m30"></a>

### M30 — Explain the complete scientific relationship

**Central question.** What is the whole project's causal and mathematical story?

**Understanding target.** Reconstruct the source, paired decoder, anonymous kernel and learning/prediction ceiling, then explain full-likelihood saturation, separate collective recovery and Gaussian equivalence. State the assumptions and charged resources, credit the kernel and inherited tools once, and distinguish Correspondence's authoritative proof from Readout's paired benchmarks and application.

**Dependencies and story role.** Integrates all earlier milestones. A complete explanation must connect the global surviving experiment to its source and its actual physically permitted receiver without claiming an efficient implementation or restored consistency.

**Source pointers.** [Scientific route](../science/README.md); [Petz bridge](PETZ_BRIDGE.md); [worked examples](WORKED_EXAMPLES.md); [related work](../references/RELATED_WORK.md).
