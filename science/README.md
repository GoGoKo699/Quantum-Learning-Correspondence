# Scientific account

A quantum demonstration can contain two useful things: the specimens themselves and the information saying which specimens belong together. This project separates those resources. It compares the same input and output specimens with their pairing retained or with one global output permutation hidden.

The principal example is learning an unknown Pauli transformation from separable quantum demonstrations. With the pairs identified, a Bell measurement turns each demonstration into one exact linear equation, and a linear number of demonstrations suffices. With their correspondence hidden, even an arbitrarily large batch contains less than one nat of Holevo information about the transformation. The obstruction includes joint measurements of every specimen and a coherent model that consumes all its training data to process one later input.

The growing-batch account determines what remains: at fixed dimensions and strict correlation contraction, separate collective measurements of the two lists asymptotically retain the full quantum statistical experiment. It is equivalent to one classical Gaussian observation with target-dependent cross-covariance. This operational sufficiency theorem complements the ceiling without restoring consistent learning from one batch.

## Reading route

| Question | Account |
| --- | --- |
| What exactly does the source supply, and what is erased? | [Model and theorem statements](model.md) |
| How can a random permutation be analyzed without summing factorially many states? | [Exact correlation kernel](correlation-kernel.md) |
| Why does increasing the batch size fail to remove the uncertainty? | [Information ceiling and identification converse](information-ceiling.md) |
| What survives in a growing batch, and does reading the lists separately lose it? | [Separate-list sufficiency and Gaussian experiment](separate-list-readout.md) |
| How are the same paired specimens learned efficiently? | [Paired learning algorithm](paired-learning.md) |
| Could a quantum model avoid producing a classical estimate? | [Prediction with a consumable quantum model](prediction.md) |
| What does the comparison establish physically? | [Interpretation](interpretation.md) |
| What must preparation, storage, pairing and processing cost? | [Resources](resources.md) |
| Which ingredients and earlier models are inherited? | [Related work](../references/RELATED_WORK.md) |

For the finite-batch separation, read the model, the cycle-contraction proof, the discrimination bound and the paired algorithm in that order. The prediction page then converts identification into a statement about what a learned device can do. For the growing-batch result, continue from the exact kernel to the separate-list proof: its full-likelihood norm identity supplies the step beyond a central-limit calculation.

## Principal quantitative comparison

Let $`d=2^n`$, let the hidden transformation be a uniformly selected $`n`$-qubit Pauli, and use the ideal source visibility $`v=1`$. Define

```math
C_d=\left(1-\frac{1}{(d+1)^2}\right)^{-(d^2-1)}\lt e.
```

| Supplied correspondence | Supported performance |
| --- | --- |
| Every input is paired with its transformed partner | $`O(n+\log(1/\delta))`$ demonstrations and polynomial processing recover the Pauli with failure at most $`\delta`$. |
| One globally shuffled output list; permutation withheld | For every batch size $`N`$, every learner has average identification success at most $`\sqrt{C_d}/d\lt\sqrt e\,2^{-n}`$. |
| The shuffled data are retained as a coherent program | Its average fidelity for applying the hidden transformation to one later Haar-random input is at most $`(\sqrt{C_d}+1)/(d+1)`$. |

The averages in the last two rows are over the uniform hidden-Pauli prior and all source and learner randomness. They imply corresponding minimax obstructions. The paired construction is an explicit high-confidence algorithm. These are finite-batch statements with the source and access assumptions held fixed; no large-$`N`$ approximation is used in the converse.

The [verification account](../verification/README.md) documents finite matrix and finite-field checks. Those checks support the calculations, while the arguments on these pages establish the all-$`N`$ claims and the separate fixed-dimension asymptotic theorem. A finite example or matching covariance does not certify statistical sufficiency.
