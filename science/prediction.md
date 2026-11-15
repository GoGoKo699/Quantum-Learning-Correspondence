# A coherent learned model has the same obstruction

A learner might avoid identifying the hidden Pauli explicitly. It could retain the quantum training data as a program and use that program only when a new input arrives. The anonymous-data converse still applies to this more permissive task.

## The processor and its score

Take $`d=2^n`$ and a uniformly hidden Pauli $`W_w`$. After receiving the anonymous batch $`\Omega_{N,v}(W_w)`$, the learner may keep every register, compress it, measure part of it, retain classical outcomes and initialize additional work. All these operations can be absorbed into one fixed trace-preserving processor $`\Lambda`$ acting on the batch and a later input. Its induced channel is

```math
\mathcal E_w(X)
=\Lambda\!\left(\Omega_{N,v}(W_w)\otimes X\right).
```

The processor is independent of the unknown $`w`$. It may consume the entire training batch on this single use. There is no reusability requirement and no restriction to a classical model.

The input is a fresh pure state, scored by fidelity with its ideal transformed state and averaged over Haar measure:

```math
F_{\mathrm{avg}}(\mathcal E_w,W_w)
=\int d\psi\,
\langle\psi|W_w^\dagger
\mathcal E_w(|\psi\rangle\langle\psi|)
W_w|\psi\rangle.
```

Every output branch contributes to the score. A processor that declares failure must still supply its prescribed output on that branch. Conditional fidelity after accepting a rare event is a different task.

## Theorem 6: finite-batch prediction bound

For every such processor and every $`N`$,

```math
\frac1{d^2}\sum_wF_{\mathrm{avg}}(\mathcal E_w,W_w)
\le\frac{\sqrt{C_{d,v}}+1}{d+1}
\lt\frac{e^{v^2/2}+1}{d+1}.
```

Equivalently, its average gate infidelity is at least

```math
\frac d{d+1}
\left(1-\frac{\sqrt{C_{d,v}}}{d}\right).
```

The statement is average case over a uniform hidden Pauli. Therefore some hidden Pauli has fidelity no larger than the upper bound, yielding the corresponding minimax obstruction. The fidelity already averages over the source permutation, hidden preparation seeds and the processor's outcomes.

### Proof: turn a useful program into a discriminator

Let $`|\Phi\rangle=d^{-1/2}\sum_j|j\rangle_R|j\rangle_B`$ and $`|\Phi_w\rangle=(I\otimes W_w)|\Phi\rangle`$. Feed register $`B`$ of this fixed maximally entangled state into the learned processor, retain $`R`$, and Bell-measure the output together with $`R`$.

When the hidden label is $`w`$, the probability of the Bell outcome $`w`$ is

```math
F_e(\mathcal E_w,W_w)
=\langle\Phi_w|
(\operatorname{id}\otimes\mathcal E_w)
(|\Phi\rangle\langle\Phi|)
|\Phi_w\rangle.
```

This experiment is a fixed measurement on the received batch. Its extra entangled input, ancillas, processor and final Bell basis are all independent of $`w`$. More formally, composing the fixed input preparation, the trace-preserving processor and the complete Bell POVM induces positive effects $`E_w`$ on the data Hilbert space with $`\sum_wE_w=I`$. The success of this data discriminator is exactly the average entanglement fidelity above. The [identification bound](information-ceiling.md) therefore implies

```math
\frac1{d^2}\sum_wF_e(\mathcal E_w,W_w)
\le\frac{\sqrt{C_{d,v}}}{d}.
```

For a trace-preserving channel relative to a unitary target, the standard identity is

```math
F_{\mathrm{avg}}(\mathcal E_w,W_w)
=\frac{dF_e(\mathcal E_w,W_w)+1}{d+1}.
```

It follows by using the Haar second moment of $`|\psi\rangle\langle\psi|`$ in the average-fidelity integral. Substitution proves the theorem. The conversion is valid for arbitrary induced channels, including those arising from coherent quantum programs and internal measurement feedback.

The entangled state used in this proof is a diagnostic input to an arbitrary channel. It does not give the actual learner an additional unknown-unitary call or a source seed. The Haar-input fidelity identity allows that diagnostic to bound the stated input-averaged score.

## Classical estimates are included

A learner that first outputs a classical estimate $`\widehat U`$ and then applies it to the later input is a special case of the processor. Hence the same bound rules out uniform consistent unitary estimation from one anonymous batch. One may also see this directly from orthogonality of the Weyl Bell states: the squared normalized trace overlaps of a unitary estimate with all $`d^2`$ Pauli targets sum to one.

The theorem is stronger than a restriction on measuring training data before a test. It remains valid when the test and all training registers are processed jointly, and when the learned model is used only once.

## Matched paired-data prediction

At $`v=1`$, apply the [paired learner](paired-learning.md) with failure at most $`\delta`$. Retain the recovered $`2n`$-bit Pauli label and apply the corresponding known circuit to each later input.

On a correct recovery the channel is exact. On a wrong Pauli label, the target-relative normalized trace overlap is zero, so the average input fidelity is $`1/(d+1)`$. Thus, for every hidden $`w`$,

```math
F_{\mathrm{avg}}^{\mathrm{paired}}(w)
\ge1-\frac{d\delta}{d+1}.
```

The learner uses $`O(n+\log(1/\delta))`$ demonstrations and polynomial processing. After learning, its explicit classical model can be reused; the anonymous upper bound allowed the more permissive alternative of consuming all its data for a single prediction.

## Comparison with a blind device

A device with no $`w`$-dependent data has average input fidelity exactly $`1/d`$ against the uniform Pauli target. Pauli twirling, or completeness of the Bell basis, gives its average entanglement fidelity $`1/d^2`$.

Since $`C_{d,v}\lt e^{v^2}`$, the anonymous model's fidelity is at most a constant factor above this blind benchmark as $`d`$ grows. At $`v=1`$ it is bounded by approximately $`(1+\sqrt e)/d`$, whereas the paired model can approach fidelity one. These statements compare the same source and output task; they do not assume an efficient optimal anonymous decoder.
