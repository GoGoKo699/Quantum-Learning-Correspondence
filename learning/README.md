# Learning correspondence loss and surviving information

This route follows one experiment from its source to its final statistical description. With identified pairs, Bell measurements efficiently learn an ideal hidden Pauli. One anonymous shuffle instead leaves a finite information ceiling, even for a coherent predictor. As that anonymous batch grows, the surviving experiment becomes a classical Gaussian covariance observation that can be obtained by separate collective measurements of the two lists.

The common educational anchor is Dénes Petz, [*Quantum Information Theory and Quantum Statistics*, first edition (2008)](https://doi.org/10.1007/978-3-540-74636-2). The [Petz bridge](PETZ_BRIDGE.md) connects coarse-graining, conditional expectation, sufficiency, information and estimation to this project. Its project-specific supplements supply the exact kernel, decoder, Fourier norm-saturation argument and separate-list receiver; those results are not attributed to the textbook.

| Page | Purpose |
|---|---|
| [Petz bridge](PETZ_BRIDGE.md) | Translate the selected source's statistical concepts into the acquisition model and its proofs. |
| [Worked examples](WORKED_EXAMPLES.md) | Follow Bell decoding, finite anonymous purity, the Gaussian norm identity and a genuinely classical reconstruction channel. |
| [Thirty milestones](MILESTONES.md) | Reconstruct the full story through ten background and twenty narrative targets. |
| [Scientific account](../science/README.md) | Read the canonical assumptions, statements, proofs and resource boundaries. |
| [Supplementary Watrous bridge](WATROUS_BRIDGE.md) | Consult additional finite-dimensional foundations for states, channels, discrimination and permutation operators. |

The [separate-list theorem](../science/separate-list-readout.md) is the authoritative proof of the shared result with [Quantum Learning Readout](https://github.com/GoGoKo699/Quantum-Learning-Readout). Readout supplies the paired precision benchmarks and explains the changed readout class. Both projects use Petz, with different learning routes.

Keep three limits distinct throughout. The efficient paired Pauli decoder uses ideal visibility one. The anonymous information bound holds for every size of one globally shuffled batch. Separate-list sufficiency fixes local dimensions and a strict correlation contraction before growing that batch; it supplies no efficiency or convergence-rate guarantee. Independently tagged batches add information, and simultaneous growth in their number needs the stated reconstruction-error control.
