# Finite verification

Run the scientific checks with Python 3.12 and NumPy:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_science.py
```

The script writes `verification/results.json`. It records the actual runtime versions, seed, script hash, measured residuals, exact rational results, and the scope of the run. A different output path or simulation seed can be selected with `--output` and `--seed`.

## What is checked

| Check | Method | Scope |
|---|---|---|
| Permutation cycle identity | Construct the shuffled density matrices directly by summing all output permutations; compare their Hilbert–Schmidt overlap with the cycle coefficient | One to four pairs of qubits; distinct physical sources with noncommuting correlation matrices, plus the Werner endpoint |
| Bell outcome law | Construct the Pauli Bell basis and the process-probe density matrix; inspect the full transformed matrix | One to four qubits per specimen, selected hidden Paulis including a transpose-sensitive Y component |
| Support and affine mass | Enumerate the quadratic support, every Fourier character and every translated support | Exact binary arithmetic for one to four qubits |
| Paired decoder | Solve the augmented linear equations for seeded samples; compare with the actual hidden Pauli | One to four qubits, 512 trials per size; an illustrative finite run |
| Rank probability | Enumerate row-space distributions with integer counts; compare with the union bound and an independent one-qubit coupon formula | Exact rational probabilities in the stated one- and two-qubit cases |
| Converse constants | Evaluate the finite-dimension constant and the elementary logarithmic upper bound | One to sixteen qubits |

The generic correlation-matrix cases matter: they check the cycle contraction without assuming that the two source matrices share an eigenbasis. The Bell check inspects off-diagonal entries as well as outcome probabilities. The decoder reports every full-rank error and does not treat random simulation frequencies as a proof of its success probability.

## What the run establishes

The recorded run passes its stated finite checks. The universal statements follow from the analytical proofs in `science/`: small matrices and sampled demonstrations do not establish an all-sample-count bound. The coherent-program consequence uses an exact channel-to-POVM reduction and the standard entanglement-fidelity identity; it is an analytical statement, not a hardware experiment.

No device benchmark, arbitrary-dimension exhaustive enumeration, source preparation experiment, or exhaustive priority certificate is claimed. Dense matrix construction deliberately stops at small sizes; the paired learner itself uses polynomial gate and classical decoding resources.
