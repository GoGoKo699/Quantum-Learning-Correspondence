# Related work and attribution

The question is whether a learner can infer a fixed quantum transformation after the correspondence between its input and output specimens has been erased. The source supplies native quantum demonstrations. It withholds their preparation records, and it shuffles the output registers **before any learner measurement**. The receiver may keep and jointly measure the complete database.

The principal separation uses an unknown Pauli conjugation on `n` qubits and fresh random stabilizer demonstrations. Known correspondence permits an efficient Bell-measurement learner using order `n` pairs. After one uniform shuffle of the whole output block, the identification bound applies to every collective measurement, for every size of that single database. A learner may use and consume an arbitrary quantum model: this is already a quantum channel followed by a measurement on the supplied registers.

## The closest statistical antecedent

**Vered Paslev and Wasim Huleihel, _Testing Dependency of Unlabeled Databases_, IEEE Transactions on Information Theory 70(10), 7410–7431 (2024).** [DOI](https://doi.org/10.1109/TIT.2024.3442977) · [arXiv:2311.05874v1](https://arxiv.org/abs/2311.05874v1) · [version used for equation locators](https://arxiv.org/html/2311.05874v1).

Their data are classical databases with an unknown row correspondence. Under one hypothesis the databases are independent; under the other, matched rows follow a specified correlated law with the same marginals. Lemma 1 and Eqs. (64), (71) express the likelihood-ratio second moment through relative-permutation cycles and the spectrum of the single-row likelihood kernel.

This cycle/spectral second-moment method is an inherited foundation. Here it is reconstructed for overlaps of **quantum density operators before measurement**, using the operator correlation matrix. Its use bounds arbitrary collective quantum readout, rather than one classical measurement record. The Pauli example then connects that operator bound to an efficient paired learning task. The contribution is not the first obstruction to learning from unlabeled data, nor a new discovery of permutation-cycle combinatorics.

## Quantum demonstrations with correspondence retained

**Ruge Lin, _Quantum Learning Readout_, public scientific account at commit `ce61966034a9b72ba1c846a354f8034f5e1a9285`.** [Model](https://github.com/GoGoKo699/Quantum-Learning-Readout/blob/ce61966034a9b72ba1c846a354f8034f5e1a9285/science/model.md) · [attribution](https://github.com/GoGoKo699/Quantum-Learning-Readout/blob/ce61966034a9b72ba1c846a354f8034f5e1a9285/references/related_work.md).

That account uses the same separable Werner-orbit demonstration model, with hidden preparation records and maximally mixed individual marginals. It compares per-pair separable readout, per-pair joint readout, and collective readout of paired examples. Its regular high-precision estimation theorem fixes dimension and a visibility strictly between zero and one.

The present operation erases the **source correspondence**, not merely a readout permission. Every input and output specimen remains available, and unrestricted collective processing is allowed. The noiseless Pauli learner at visibility one has its own Bell-support argument; it does not follow by substituting that rank-deficient endpoint into the earlier regular estimation theorem. The paired source model and its established usefulness are credited to the earlier account.

The Werner-state terminology and invariant-state framework originate with **Reinhard F. Werner, _Quantum states with Einstein-Podolsky-Rosen correlations admitting a hidden-variable model_, Physical Review A 40, 4277–4281 (1989)**, [DOI](https://doi.org/10.1103/PhysRevA.40.4277).

## Growing anonymous batches and statistical sufficiency

The [separate-list theorem](../science/separate-list-readout.md) adds an operational conclusion to the exact anonymous-source kernel. At fixed dimensions, uniformly over compact physical uniform-marginal correlation families with a strict contraction bound, the complete anonymous experiment is asymptotically recoverable from separate collective measurements of the two lists. Its limiting experiment is a centered Gaussian law with target-dependent cross-covariance. This is the authoritative home of that shared result; the paired-source and precision context remain in Quantum Learning Readout.

**Lev Glebsky, _Almost commuting matrices with respect to normalized Hilbert–Schmidt norm_, arXiv:1002.3082v1 (2010), Theorem 2.** [Primary text](https://arxiv.org/html/1002.3082v1).

For any fixed finite number of unitary matrices, pairwise small commutators in normalized Hilbert–Schmidt norm imply nearby exactly commuting unitary matrices, with a modulus independent of matrix dimension. This simultaneous approximation theorem is inherited. The norm is normalized Hilbert–Schmidt, not Schatten one. It applies here only after the entire likelihood has been approximated by a finite family of bounded local Fourier observables. A diagonal schedule, rather than an arbitrary growing-family application, gives the receiver sequence.

**Greg Kuperberg, _A tracial quantum central limit theorem_, Transactions of the American Mathematical Society 357 (2005), 459–471.** [arXiv:math-ph/0202035](https://arxiv.org/abs/math-ph/0202035).

Theorem 1 identifies classical Gaussian polynomial limits for centered independent sums in a tracial noncommutative probability space. The classical fluctuation mechanism at the maximally mixed reference is therefore established. The source-specific proof here uses bounded Fourier expansions directly. Weak moment or spectral-distribution convergence alone does not supply one separate-side receiver or exclude a remaining quantum decision advantage.

**Mădălin Guţă and Anna Jenčová, _Local asymptotic normality in quantum statistics_, arXiv:quant-ph/0606213v2 (2007), Section 3.4.** [Primary text](https://arxiv.org/abs/quant-ph/0606213v2).

Two-sided comparison by physical channels is the established statistical notion of quantum experiment equivalence. It is stronger than matching covariance or a Fisher-information matrix. The general comparison language is inherited; the theorem here constructs the needed separate-list measurements, recovery channel and classical coupling kernels for this anonymous model.

**Koichi Yamagata, Akio Fujiwara and Richard D. Gill, _Quantum local asymptotic normality based on a new quantum likelihood ratio_, Annals of Statistics 41 (2013), 2197–2217.** [arXiv:1210.3749v3](https://arxiv.org/html/1210.3749v3).

The iid local-asymptotic-normality framework gives Gaussian shift experiments in shrinking neighborhoods and can include a maximally mixed reference. The present family is globally indexed by a surviving covariance orientation after anonymization. The paired-copy precision argument in Readout and a routine invocation of iid local asymptotic normality therefore do not by themselves yield the separate-list theorem.

The added inference is full-likelihood saturation: the Gaussian covariance likelihood has exactly the limiting squared $`L^2`$ norm supplied by the operator collision kernel. Its Fourier functions consequently approximate the complete likelihood. Glebsky's theorem then produces local commuting measurements, and the scalar conditional expectation onto their abelian algebra gives genuine classical readout and state recovery. A reference coupling proves two-way Gaussian equivalence. No new general central limit theorem, almost-commuting theorem, or efficient receiver is claimed.

**Dénes Petz, _Quantum Information Theory and Quantum Statistics_ (2008).** [Published edition](https://doi.org/10.1007/978-3-540-74636-2). Sections 9.1–9.2 and 9.5 provide the common educational foundation for coarse-graining, conditional expectations and sufficiency; Sections 10.1–10.3 connect estimation and Fisher information. The project-specific Fourier-saturation theorem remains separately proved, and the book is not cited as already establishing it.

## Lost pairing is an established physical question

**J. Eisert, T. Felbinger, P. Papadopoulos, M. B. Plenio and M. Wilkens, _Classical Information and Distillable Entanglement_, Physical Review Letters 84, 1611–1614 (2000).** [DOI](https://doi.org/10.1103/PhysRevLett.84.1611) · [arXiv:quant-ph/9907021](https://arxiv.org/abs/quant-ph/9907021).

This work explicitly destroys the record of which particles form entangled pairs and determines the resulting distillable entanglement in its model. It also interprets the operation as randomization of signal order. The idea that classical correspondence can carry operational quantum value is therefore prior work.

**Jean-Daniel Bancal, Cyril Branciard, Nicolas Brunner, Nicolas Gisin, Sandu Popescu and Christoph Simon, _Testing a Bell inequality in multipair scenarios_, Physical Review A 78, 062110 (2008).** [DOI](https://doi.org/10.1103/PhysRevA.78.062110) · [arXiv:0810.0942](https://arxiv.org/abs/0810.0942) · [accepted author manuscript](https://access.archive-ouverte.unige.ch/access/metadata/d56fd832-f67d-4981-b542-153e7f4a902c/download).

Their independent-pair setting loses classical pairing information during collective counting. They compare its surviving entanglement and Bell nonlocality with coherent indistinguishability. These results concern entangled resources and specified Bell measurements. They do not give the present all-measurement transformation-learning converse. Conversely, a learning obstruction does not say that a shuffled state has no correlations, entanglement, or usefulness for every other task.

## Exact source preparation and Bell measurements

| Established ingredient | Primary source | Use here |
|---|---|---|
| The uniform Clifford group is an exact unitary 2-design | Dankert, Cleve, Emerson and Livine (2009), Theorem 1 | Applying it to a fixed basis state gives the required exact second moment of random stabilizer states. The source averages to the stated separable pair density matrix. |
| Exact efficient uniform Clifford selection | Koenig and Smolin (2014) | A polynomial-time finite random source replaces an unimplemented Haar draw. The preparation seed remains private. |
| Bell sampling and binary linear algebra for learning | Montanaro (2017), Theorem 1 and Lemma 2 | Bell measurements and their stabilizer-learning use are inherited. Here each pair contains a freshly drawn stabilizer and its Pauli-transformed partner, rather than two copies of one fixed unknown stabilizer. The affine equations identify the common transformation. |

**Christoph Dankert, Richard Cleve, Joseph Emerson and Etera Livine, _Exact and approximate unitary 2-designs and their application to fidelity estimation_, Physical Review A 80, 012304 (2009).** [DOI](https://doi.org/10.1103/PhysRevA.80.012304) · [author-hosted article](https://www.math.uwaterloo.ca/~jemerson/papers/DankertPRA09.pdf).

**Robert Koenig and John A. Smolin, _How to efficiently select an arbitrary Clifford group element_, Journal of Mathematical Physics 55, 122202 (2014).** [DOI](https://doi.org/10.1063/1.4903507) · [arXiv:1406.2170](https://arxiv.org/abs/1406.2170).

**Ashley Montanaro, _Learning stabilizer states by Bell sampling_, arXiv:1707.04012v2 (2017).** [arXiv](https://arxiv.org/abs/1707.04012v2) · [author manuscript](https://people.maths.bris.ac.uk/~csxam/papers/bsampling.pdf).

## Standard information and loss tools

**Michael A. Nielsen, _A simple formula for the average gate fidelity of a quantum dynamical operation_, Physics Letters A 303(4), 249–252 (2002).** [DOI](https://doi.org/10.1016/S0375-9601(02)01272-0) · [arXiv:quant-ph/0205035v2](https://arxiv.org/abs/quant-ph/0205035v2).

The conversion between entanglement fidelity and Haar-average gate fidelity is inherited. It identifies the operational meaning of a Pauli-channel estimate; it is not a new loss formula.

**Alexander S. Holevo, _Bounds for the Quantity of Information Transmitted by a Quantum Communication Channel_, Problems of Information Transmission 9(3), 177–183 (1973).** [journal archive and bibliographic record](https://www.mathnet.ru/eng/ppi903).

The Holevo accessible-information bound and elementary entropy inequalities are standard tools. **John Watrous, _The Theory of Quantum Information_ (2018)**, [author manuscript](https://cs.uwaterloo.ca/~watrous/TQI/), Chapters 3, 5 and 7, gives modern foundations for discrimination, entropy and permutation methods. The source-specific content here is the uniform spectral bound on the shuffled quantum database, not those general inequalities.

## Scope of the comparison

The separation concerns one database whose entire output block receives one unrecorded uniform permutation. Independent repeated shuffled batches, protected pairing tags, latent preparation descriptions, chosen-input queries, or an accessible permutation register are additional resources.

The efficient paired algorithm uses exact noiseless demonstrations. Adding fixed noise changes its clean affine equations into a statistical decoding problem; the same efficient running-time guarantee is not asserted. The anonymous converse allows unrestricted computation and quantum storage. It is a statement about quantum-data correspondence, not an end-to-end speedup for an ordinary classical dataset.

The comparisons above identify the material models and proof dependencies inspected for the stated contribution. They do not certify exhaustive priority or replace independent mathematical review. Structured bibliographic data are in [references.bib](references.bib).

