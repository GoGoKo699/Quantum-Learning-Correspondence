# Finite verification

Run the scientific checks with Python 3.12 and NumPy:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_science.py
python verification/check_fourier_saturation.py
python verification/check_navigation.py
```

The original science script writes [results.json](results.json). It records the actual runtime versions, seed, script hash, measured residuals, exact rational results, and the scope of the run. A different output path or simulation seed can be selected with `--output` and `--seed`.

The growing-batch diagnostic writes [fourier_saturation_results.json](fourier_saturation_results.json), and the navigation check writes [structure_results.json](structure_results.json). Both support an alternative JSON path with `--output`. Every command exits unsuccessfully when one of its stated checks fails.

## What is checked

| Check | Method | Scope |
|---|---|---|
| Permutation cycle identity | Construct the shuffled density matrices directly by summing all output permutations; compare their Hilbert–Schmidt overlap with the cycle coefficient | One to four pairs of qubits; distinct physical sources with noncommuting correlation matrices, plus the Werner endpoint |
| Bell outcome law | Construct the Pauli Bell basis and the process-probe density matrix; inspect the full transformed matrix | One to four qubits per specimen, selected hidden Paulis including a transpose-sensitive Y component |
| Support and affine mass | Enumerate the quadratic support, every Fourier character and every translated support | Exact binary arithmetic for one to four qubits |
| Paired decoder | Solve the augmented linear equations for seeded samples; compare with the actual hidden Pauli | One to four qubits, 512 trials per size; an illustrative finite run |
| Rank probability | Enumerate row-space distributions with integer counts; compare with the union bound and an independent one-qubit coupon formula | Exact rational probabilities in the stated one- and two-qubit cases |
| Converse constants | Evaluate the finite-dimension constant and the elementary logarithmic upper bound | One to sixteen qubits |
| Anonymous Fourier expectation and Gram normalization | Compare exact tensor-product formulas with direct shuffled density matrices and direct operators | Qubit specimens, visibility one half, batch sizes one through three, three target unitaries including noncommuting rotations |
| Complete finite Fourier residual identity | Compare the direct normalized Hilbert–Schmidt residual with the collision-kernel, characteristic-function and Gram-matrix formula | Nine direct dense source/batch cases; a fixed fifteen-frequency dictionary |
| Gaussian limit and local commutators | Evaluate exact finite tensor formulas through batch size 16384 and compare the likelihood residual with its Gaussian value | The same fixed dictionary and targets; no large dense state is formed |
| Source navigation and learning-map inventory | Check relative destinations, Markdown heading fragments, fenced-block balance, and M01–M30 exactly once in order | All current Markdown files; external links and actual rendering are excluded |

The generic correlation-matrix cases matter: they check the cycle contraction without assuming that the two source matrices share an eigenbasis. The Bell check inspects off-diagonal entries as well as outcome probabilities. The decoder reports every full-rank error and does not treat random simulation frequencies as a proof of its success probability.

## What the run establishes

The recorded run passes its stated finite checks. The universal statements follow from the analytical proofs in `science/`: small matrices and sampled demonstrations do not establish an all-sample-count bound. The coherent-program consequence uses an exact channel-to-POVM reduction and the standard entanglement-fidelity identity; it is an analytical statement, not a hardware experiment.

For the [separate-list theorem](../science/separate-list-readout.md), the new diagnostic checks normalizations and the finite Fourier residual identity independently using dense anonymous states. In the recorded run the largest dense Gram error is below $`6\times10^{-16}`$, and the largest discrepancy between the finite and Gaussian squared residuals at batch size 16384 is below $`2.3\times10^{-6}`$. The fixed dictionary deliberately has a nonzero limiting approximation residual: the test checks convergence to that value, rather than claiming that this finite dictionary exhausts the likelihood. The proof obtains arbitrarily accurate approximation by selecting suitable finite dictionaries and then taking a diagonal sequence.

The diagnostic does not synthesize commuting approximants, a Glebsky measurement, or either Gaussian randomization kernel. It does not numerically certify uniform operational sufficiency, entropy continuity, a convergence rate, Fisher-information convergence, a growing-dimension limit, or an efficient receiver. Those boundaries also apply to the observed decay of its finite local commutators. Historical source pins in the JSON identify the inherited model and kernel; they are not final integration or hosted-rendering receipts.

No device benchmark, arbitrary-dimension exhaustive enumeration, source preparation experiment, or exhaustive priority certificate is claimed. Dense matrix construction deliberately stops at small sizes; the paired learner itself uses polynomial gate and classical decoding resources.

## Hosted presentation

The [hosted review tools](hosted_math/README.md) separately compare actual commit-pinned GitHub MathML with its source, including tables and both wide and narrow layouts. The repository's same-repository pull-request job uses read-only permissions and retains reports and screenshots for inspection. Those presentation checks and the scientific suite answer different questions; neither substitutes for the other.
