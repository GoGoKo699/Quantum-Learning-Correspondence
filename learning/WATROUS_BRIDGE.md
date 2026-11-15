# From Watrous to quantum learning with lost correspondence

The reference is John Watrous, [*The Theory of Quantum Information*](https://cs.uwaterloo.ca/~watrous/TQI/), Cambridge University Press, 2018, [DOI: 10.1017/9781316848142](https://doi.org/10.1017/9781316848142). The author's landing page provides chapter links and describes publication in April 2018.

The locators below refer specifically to the **standard-layout author manuscript**, marked ©2018 with a January 2018 preface, checked on 15 November 2026. Page numbers are the manuscript's printed numbers, not PDF-viewer indices. The compact layout has different pagination. The manuscript is available for personal use under the author's terms and is not redistributed here.

## A map of the required foundations

| Foundation | Verified manuscript locator | Role in this repository |
|---|---|---|
| Density operators, mixtures and reduced states | §§2.1.2–2.1.3, pp. 61–71 | Define the demonstrations, average over private source seeds, and verify that both individual marginals equal the maximally mixed state. See [model](../science/model.md). |
| Channels and their representations | §2.2.1, p. 72; Definition 2.13, p. 73; §2.2.2, p. 77 | Model all allowed data processing and a learned program's later action as completely positive, trace-preserving maps. See [prediction](../science/prediction.md). |
| Measurements | §2.3.1, p. 100; Definition 2.34, p. 101 | A measurement is a family of positive effects summing to the identity. This includes joint measurements on the whole received batch. |
| Discrimination of an ensemble | §3.1.2, p. 132 | Write hidden-Pauli recovery as average success of a measurement on a known ensemble of possible batch states. See [information ceiling](../science/information-ceiling.md). |
| Binary discrimination | §3.1.1, p. 125; Theorem 3.4, p. 128 | The Holevo–Helstrom theorem explains the operational meaning of trace distance. The repository's many-label purity bound is proved separately. |
| State fidelity | §3.2, p. 139; Definition 3.11, p. 139 | Translate the book's unsquared fidelity before comparing it with the project's overlap scores. |
| Entropy and relative entropy | §5.2.1, p. 265; Definitions 5.17–5.18, pp. 265–266; §5.2.2, p. 267 | Convert normalized purity into an entropy deficit relative to the maximally mixed batch state. |
| Accessible information and the Holevo quantity | §5.3.3, p. 294; the quantity is defined on p. 297; Theorem 5.49, p. 299 | Bound the mutual information revealed by any measurement of the batch. |
| Bell states and joint readout | §6.3.1, Example 6.50, pp. 365–366 | Supply the maximally entangled basis used for paired measurements and the fixed diagnostic test in the prediction reduction. The project's affine Pauli decoder is proved locally. |
| Permuting tensor factors | §7.1.1, p. 391, Eqs. (7.3)–(7.4); Proposition 7.1, p. 392 | Represent the forgotten output correspondence by permutation unitaries. The proposition concerns the symmetric-subspace projector, which must be distinguished from a permutation channel on density operators. |
| Invariant measures and moments | §7.2.1, p. 408; Lemma 7.24, p. 416; Example 7.25, p. 417 | Obtain the spherical second moment and understand the swap symmetry of the source. Exact stabilizer preparation additionally uses the design references in [related work](../references/RELATED_WORK.md). |

## Translate the conventions first

Watrous writes the adjoint as an asterisk, uses column vectors in place of ket notation, and often writes an ensemble as positive operators $`\eta(w)=p_w\omega_w`$ that already include their probabilities. Here the same ensemble is written $`\{p_w,\omega_w\}`$. His measurement effect $`\mu(w)`$ corresponds to $`E_w`$, and the identity operator is often written $`1`$ rather than $`I`$.

The book's entropy notation is $`H`$ and its $`\log`$ has base two. Here $`S`$ denotes von Neumann entropy and $`\log`$ is natural. Thus a project information value in nats is converted to the book's bits by division by $`\ln 2`$. In particular, the ceiling below one nat is below $`1/\ln2`$ bits; it is not a claim of a ceiling below one bit.

Watrous defines state fidelity as $`F(\rho,\sigma)=\Vert \sqrt\rho\sqrt\sigma\Vert _1`$. With a pure target, its square is the target overlap. The project's $`F_e`$ and $`F_{\mathrm{avg}}`$ use overlap scores, not this unsquared state-fidelity convention. Their relation is stated explicitly in [prediction](../science/prediction.md).

The project's $`D=d^{2N}`$ denotes a Hilbert-space dimension, while $`D(\omega\Vert \tau)`$ denotes relative entropy. Context distinguishes them. Pauli labels in the [paired decoder](../science/paired-learning.md) are binary vectors; they are not channel matrices.

## Where the textbook tools enter the proof

Start with the physical source in [model](../science/model.md). The second moment from Lemma 7.24, specialized to two copies, gives

```math
\mathbb E_\psi[\psi^{\otimes2}]
=\frac{\Pi_{\mathrm{sym}}}{d(d+1)/2}
=\frac{I+F}{d(d+1)}.
```

Conjugating the second register by the hidden unitary produces the ideal demonstration state. A finite exact state 2-design has the same moment. This explains the density operator after discarding the preparation seed; it does not provide the learner with a description of the sampled state.

Next apply the channel that averages conjugation by output permutations. For a batch state $`X`$, that channel is

```math
\mathcal T_B(X)=\frac1{N!}\sum_{\pi\in S_N}
(I\otimes P_\pi)X(I\otimes P_\pi^\dagger).
```

It preserves trace and produces a permutation-invariant operator. It is **not** multiplication by the symmetric-subspace projector, nor a promise that the state is supported on that subspace. Losing a classical permutation record gives the average above, not a coherent superposition of matchings.

The [kernel proof](../science/correlation-kernel.md) is the source-specific step. Two matchings form alternating cycles. Tracelessness eliminates partially selected cycles, and two-factor operator orthogonality evaluates every surviving cycle. This gives

```math
\sum_{N\ge0}K_N(T,S)z^N
=\frac1{(1-z)\det(I-zTS^{\mathsf T})}.
```

This exact overlap identity, its determinant ceiling, and its specialization to the demonstration source are proved in this repository. They are not asserted as results of Watrous. The relative-permutation cycle method has a classical antecedent, credited in [related work](../references/RELATED_WORK.md); the calculation here acts on quantum states before a measurement is selected.

Only after obtaining $`D\mathrm{Tr}\omega_w^2\le C`$ do the entropy tools enter. The [information proof](../science/information-ceiling.md) establishes

```math
D(\omega_w\Vert I/D)\le\log C,\qquad
\chi\le\sum_wp_wD(\omega_w\Vert I/D)\le\log C.
```

Theorem 5.49 then bounds every measurement's accessible information. The separate Hilbert–Schmidt argument on that page gives $`P_{\mathrm{guess}}\le\sqrt{C/M}`$ for $`M`$ equally likely labels. It is this direct inequality, rather than a substitution into a binary discrimination formula, that yields the Pauli success bound.

Finally, [prediction](../science/prediction.md) composes a fixed learned processor with a fixed maximally entangled diagnostic input and a Bell measurement. This composition induces an ordinary measurement on the training batch. The reduction therefore covers a quantum model consumed on one later input. The average-gate-fidelity identity used to convert its score is credited to Nielsen (2002) in [related work](../references/RELATED_WORK.md).

## What requires an additional project proof

The textbook supplies the language of states, channels, measurements, entropy and invariant integration. It does not supply the present correspondence-loss theorem. The exact anonymous kernel, its batch-size-uniform bound, the clean Pauli affine decoder, and the prediction reduction are the steps to reconstruct from the canonical scientific pages. The [worked examples](WORKED_EXAMPLES.md) make two of these steps finite and explicit; the [milestones](MILESTONES.md) organize the full derivation.
