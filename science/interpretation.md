# What correspondence changes

The examples contain a hidden relation, not a visible description of the transformation. Each input specimen alone is maximally mixed on average; the same is true of each output specimen. With the pairing retained, their joint state exposes how the transformation acts. Erasing the association does not erase every correlation, but it prevents those correlations from accumulating into an accurate learned transformation in the model studied here.

## The same specimens, different acquisition information

For the ideal Pauli source, the source prepares a random stabilizer state, produces its transformed partner and withholds the seed. No state description is supplied. The paired learner performs a Bell measurement on the two specimens that belong together. Its outcome satisfies an exact equation in the hidden Pauli bits. A linear number of independent equations identifies the transformation.

The anonymous learner receives the same quantum registers after the output list is shuffled. It may retain them all and try any joint quantum matching or inference procedure. The impossibility result already includes such strategies. The state overlap calculation shows that the total information remains bounded independently of how many pairs were generated.

Thus the change is an acquisition resource: the association of specimens. It is not a comparison between a small quantum memory and a large classical one, or between a chosen simple decoder and a better decoder left unexamined.

## A one-qubit illustration

With $`n=1`$, an ideal Bell outcome can be labeled by $`I,X,Y,Z`$. For a hidden identity transformation, the support is $`\{I,X,Z\}`$; the $`Y`$ outcome never occurs. Applying a hidden Pauli translates this three-element support and changes which outcome is excluded. Identified pairs let the learner accumulate these exclusions until the hidden label is fixed.

For a general dimension, the same mechanism becomes an affine linear system over $`\mathbb F_2`$. The [paired proof](paired-learning.md) bounds the chance that the collected equations remain deficient.

When all output correspondence is hidden, adding more one-qubit specimens still cannot make the average fidelity approach one. At $`d=2,v=1`$,

```math
C_{2,1}=(9/8)^3,
\qquad
F_{\mathrm{avg}}^{\mathrm{anonymous}}
\le\frac{1+\sqrt{(9/8)^3}}3\approx0.7311.
```

This is an upper bound, not the claimed optimal fidelity. Its purpose is to exhibit a positive error floor at fixed dimension. In larger dimensions, the bound becomes stronger: even a single-use coherent model has fidelity $`O(1/d)`$ for every batch size.

## Why the obstruction is not a classical-output bottleneck

The initial identification task asks for classical Pauli bits, but the [prediction theorem](prediction.md) removes that requirement. A model may retain the data coherently and consume them when one later input arrives. If it could apply the unknown Pauli accurately, applying it to half of a fixed entangled pair and measuring the resulting Bell label would identify that Pauli. This would contradict the data-discrimination bound.

The program may use arbitrary collective processing and need not survive the prediction. The statement therefore concerns the information available in the anonymous source itself, rather than a chosen way of storing or reading a learned model.

## Why a huge batch does not restore the pairing

Two copies of the anonymous density operator lead to two possible matchings. Their overlap graph consists of cycles. The contribution of a cycle of length $`\ell`$ is suppressed by $`t^{2\ell}`$ in the transformed-swap source. Summing all cycle types gives a convergent determinant expression. The resulting purity bound is uniform in the number of specimens.

This does not say that every randomly permuted quantum source has only a finite amount of information. The [general kernel theorem](correlation-kernel.md) requires uniform local marginals and strictly contractive correlations. A source with parameter-dependent marginals or an exact local correlation can behave differently. The ideal visibility $`v=1`$ used in the Pauli learner still has strictly contractive local correlations: averaging over private random input states gives $`t=1/(d+1)`$.

## Boundaries that matter operationally

| Available resource | Relation to the result |
| --- | --- |
| All quantum specimens in one anonymous batch | Included in the converse, with unrestricted collective processing. |
| A private permutation or state-preparation record revealed to the learner | Changes the supplied information and is outside the anonymous model. |
| A list of pair associations | Restores the paired acquisition interface. |
| $`B`$ independently shuffled batches whose boundaries are identified | Supplies extra grouping information. The combined Holevo upper bound is $`B\log C_{d,v}`$, rather than the one-batch constant; see [resources](resources.md). |
| Chosen-input calls to the unknown transformation | A different access model, not supplied by these native demonstrations. |
| Imperfect visibility in the source | The converse covers $`0\lt v\le1`$; the efficient exact-equation learner is proved at $`v=1`$. |
| Conditional success after postselection | Must include its probability or all failure branches; it is not the unconditional prediction score used here. |

All storage, source preparation and measurement work remain physical costs. The result establishes no hardware crossover or processing-time speedup on ordinary classical data. The [resource account](resources.md) specifies those costs separately.

## Scientific relationship to earlier learning models

The transformed-swap source, its separability and coherent readout benefits are established foundations. The present account changes the acquisition interface by withholding correspondence while retaining all specimens and allowing every collective learner. The determinant calculation and its decision-theoretic consequences isolate the resulting all-sample information ceiling. The explicit Pauli learner supplies a matched efficient comparison using exactly the same ideal specimens.

Classical anonymous-data problems provide related cycle and likelihood methods; [related work](../references/RELATED_WORK.md) records those dependencies. For the Pauli subfamily, the identified pair states commute in the known Bell basis, so its paired learning problem has an explicit classical outcome description. The converse is nevertheless proved on the density operators before measurement and includes every collective quantum learner. The contribution is the quantum source-level obstruction and its consequence for coherent prediction, rather than a claim that permutation cycle identities or hidden-matching statistics originate in this setting.
