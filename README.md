# Quantum Learning Correspondence

**Can quantum examples remain learnable after the information saying which inputs belong to which outputs is erased?**

For an explicitly preparable family, the answer changes sharply. A linear number of paired demonstrations permits efficient learning of a hidden Pauli transformation. If the same output specimens are shuffled once across the whole dataset and their pairing is withheld, every batch size has an information ceiling. Even unrestricted collective quantum processing and a coherent model that consumes the data cannot restore reliable learning.

## What survives in a growing anonymous batch?

At fixed local dimensions, the surviving information becomes classical. For any compact physical source family with uniform local marginals and strictly contractive correlation matrices $`T`$, separate collective measurements of the input list and output list permit target-independent reconstruction of the complete anonymous quantum state with trace-norm error tending to zero. The limiting experiment is one Gaussian observation with covariance

```math
\Sigma_T=\begin{pmatrix}I&T\\T^{\mathsf T}&I\end{pmatrix}.
```

Thus separate-list readout retains asymptotically every bounded decision score, including a coherent predictor's single-use fidelity. The [full theorem and proof](science/separate-list-readout.md) establish state recovery and two-way statistical equivalence; convergence of covariance alone would not suffice. There is no finite-batch equality, efficient receiver, convergence rate, dimension-growing guarantee or Fisher-information conclusion.

**Scientific relationship.** [Quantum Learning Readout](https://github.com/GoGoKo699/Quantum-Learning-Readout) supplies the paired-source model and sharp precision hierarchy when correspondence is available. This repository owns the anonymous-batch kernel, information ceiling, and shared separate-list sufficiency theorem. The new receiver may act collectively within each list; it is different from the earlier pair-by-pair separable measurement class. Both accounts retain their own tasks and assumptions.

## Finite-batch learning separation

Each demonstration contains a privately sampled $`n`$-qubit stabilizer state and its image under the same hidden Pauli. The source discards its preparation seed. Each input–output pair is separable. Write $`d=2^n`$ and

```math
C_d=\left(1-\frac1{(d+1)^2}\right)^{-(d^2-1)}\lt e.
```

| Acquisition interface | Supported performance |
| --- | --- |
| Input–output correspondence retained | $`O(n+\log(1/\delta))`$ demonstrations identify the Pauli with failure at most $`\delta`$, using Bell measurements and polynomial classical linear algebra. |
| One global output shuffle, correspondence withheld | For every batch size $`N`$, average identification success over a uniform hidden Pauli is at most $`\sqrt{C_d}/d\lt\sqrt e\,2^{-n}`$. |
| Anonymous data used as a coherent, consumable program | Its average fidelity for applying the hidden Pauli to one later Haar-random input is at most $`(\sqrt{C_d}+1)/(d+1)`$. |

The full anonymous batch carries less than one nat of Holevo information about the target, uniformly in its size and in $`d`$. The exact finite-batch collision formula explains this ceiling. It is an operator-level statement before measurement and therefore covers every joint readout of the supplied specimens.

## Read the science

Start with the [connected scientific account](science/README.md), or choose a direct route:

| Question | Route |
| --- | --- |
| What is supplied, and what information disappears? | [Model and theorem statements](science/model.md) |
| How does the permutation produce the information ceiling? | [Exact correlation kernel](science/correlation-kernel.md), then [information and identification](science/information-ceiling.md) |
| What information survives as one anonymous batch grows, and how can it be read? | [Separate-list sufficiency and Gaussian covariance equivalence](science/separate-list-readout.md) |
| How does the efficient paired learner work? | [Bell outcomes and the binary decoder](science/paired-learning.md) |
| Could a quantum model avoid identifying the transformation? | [Consumable quantum prediction](science/prediction.md) |
| What costs and assumptions control the comparison? | [Resources](science/resources.md) and [interpretation](science/interpretation.md) |
| What is inherited from earlier work? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

## Learn the project

The common educational anchor is **Dénes Petz, *Quantum Information Theory and Quantum Statistics* (2008)**, [published edition](https://doi.org/10.1007/978-3-540-74636-2). The [source bridge](learning/PETZ_BRIDGE.md) connects conditional expectations and sufficiency to the information ceiling, separate-list recovery and Gaussian covariance experiment. The new Fourier-saturation argument is developed in the project rather than attributed to the book.

Start with the [learning route](learning/README.md) and [complete worked examples](learning/WORKED_EXAMPLES.md). The [30-milestone map](learning/MILESTONES.md) progresses from individual specimens through the learning obstruction to the operational description of surviving information. It is a common map of the project, independent of any reader's progress.

## Reproduce the finite checks

Install the pinned dependency and run from the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/check_science.py
```

The [verification guide](verification/README.md) records the tested cases, actual outputs and limitations. The checks include direct shuffled density matrices, noncommuting correlation examples, Bell distributions and the finite-field decoder. Universal size-independent statements are proved analytically in the science pages.

The separate [hosted mathematical review](verification/hosted_math/README.md) compares actual GitHub mathematics against its pinned source at wide and narrow widths. Source parsing and scientific checks do not by themselves establish correct hosted rendering.

## Scope

There is one globally shuffled batch, with the permutation, private preparation seeds and their purifications unavailable before any learner interaction. Further target queries and chosen input probes are different access models. Independently tagged batches also supply additional information. Their direct reconstruction bound is $`m\varepsilon_b`$ for $`m`$ batches of $`b`$ pairs, so unrestricted simultaneous growth is not implied by the one-batch limit. The efficient paired algorithm uses ideal source visibility; the information bound extends to lower visibility. The separate-list theorem fixes dimension and a strict contraction bound. All branches count in prediction fidelity.

The source family is inherited from [Quantum Learning Readout](https://github.com/GoGoKo699/Quantum-Learning-Readout/blob/ce61966034a9b72ba1c846a354f8034f5e1a9285/science/model.md). Here the changed resource is correspondence, rather than a restriction on the allowed readout. Classical shuffled-database cycle methods and earlier lost-pairing studies are credited in the related-work account. The comparison establishes an acquisition limitation for native quantum examples; it makes no computational speedup claim for classical data.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
