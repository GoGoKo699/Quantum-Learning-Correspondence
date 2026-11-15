# Model: specimens and their correspondence

## Quantum demonstrations

Fix a dimension $`d\ge2`$, a known visibility $`0\lt v\le1`$ and an unknown unitary $`U\in U(d)`$. A demonstration contains an input register $`A`$ and an output register $`B`$. Its density operator is

```math
\rho_{U,v}
=\frac{I+vF_U}{d(d+v)},\qquad
F_U=(I\otimes U)F(I\otimes U^\dagger),
```

where $`F|a\rangle|b\rangle=|b\rangle|a\rangle`$. Both local marginals are exactly $`I/d`$, independent of $`U`$. Across demonstrations the source prepares independent copies of this pair state, conditional on the same hidden $`U`$.

At $`v=1`$ there is a direct separable preparation:

```math
\rho_{U,1}
=\mathbb E_{\psi}
\left[|\psi\rangle\langle\psi|
\otimes U|\psi\rangle\langle\psi|U^\dagger\right],
```

with $`|\psi\rangle`$ sampled from a projective state 2-design. The identity follows from the second-moment formula $`\mathbb E_\psi[\psi^{\otimes2}]=(I+F)/[d(d+1)]`$. For $`d=2^n`$, uniform stabilizer states give an exact, efficiently preparable choice. The preparation seed is private. The learner receives the specimens, not their state descriptions.

The other visibilities have the same physical interpretation with additional uncorrelated mixing:

```math
\rho_{U,v}
=a\rho_{U,1}+(1-a)\frac{I}{d^2},\qquad
a=\frac{v(d+1)}{d+v}.
```

Thus the entire source family is separable across each input–output pair. The bound below does not rely on entanglement in the supplied demonstrations.

## Two acquisition interfaces

For $`N`$ demonstrations, use the register order $`A_1\cdots A_NB_1\cdots B_N`$.

In the **paired interface**, the learner knows that $`A_i`$ belongs to $`B_i`$ and receives $`\rho_{U,v}^{\otimes N}`$ with this factorization identified.

In the **anonymous interface**, the source applies a uniformly random permutation $`\pi\in S_N`$ to the output registers and withholds it. The received state is

```math
\Omega_{N,v}(U)
=\frac1{N!}\sum_{\pi\in S_N}
(I_A\otimes P_\pi)
\rho_{U,v}^{\otimes N}
(I_A\otimes P_\pi^\dagger).
```

The input list and output list remain distinguishable. What is missing is the correspondence between their elements. There is one global batch, with no additional grouping information identifying smaller batches. The random permutation, its purification and the private state-preparation seeds are unavailable to the learner.

The learner may process all $`2N`$ registers jointly, store them coherently, add initialized work, measure adaptively and use unlimited classical computation. In particular, the model permits an attempt to infer the matching from the specimens. The source supplies no chosen-input calls to $`U`$, inverse preparation, extra copies of individual hidden states or QRAM. These conditions apply equally to both interfaces.

Randomization is a convenient precise model of withheld correspondence. The resulting average-case converse also rules out a guarantee required to hold for every unknown permutation: such a guarantee would hold after averaging over a uniform permutation.

## The constants

Write

```math
p=d^2-1,\qquad
t=\frac{v}{d+v},\qquad
C_{d,v}=(1-t^2)^{-p}.
```

Although the ideal pair state at $`v=1`$ is not full rank, $`t\lt1`$ throughout the stated model. The proofs use no inverse of the pair state. They also give

```math
\log C_{d,v}
\le\frac{(d^2-1)v^2}{d(d+2v)}
\lt v^2\le1.
```

Logs are natural, so information is measured in nats.

## Theorem 1: information saturation

For every $`N\ge1`$ and every $`U`$, with $`D=d^{2N}`$,

```math
D\mathrm{Tr}\!\left[\Omega_{N,v}(U)^2\right]
=\sum_{k=0}^N\binom{k+p-1}{p-1}t^{2k}
\le C_{d,v}.
```

Consequently, for any prior over $`U`$, the Holevo information of the anonymous batch is at most $`\log C_{d,v}\lt1`$. The bound is uniform in both the batch size and the dimension. The [kernel page](correlation-kernel.md) proves the exact identity, and the [information page](information-ceiling.md) gives the entropy deduction.

## Theorem 2: identifying the hidden Pauli

Let $`d=2^n`$ and let $`U=W_w`$ range over the $`d^2`$ Pauli transformations, with global phase ignored. For every anonymous-data learner and every $`N`$,

```math
\frac1{d^2}\sum_w
\Pr\!\left[\widehat w=w\mid\Omega_{N,v}(W_w)\right]
\le\frac{\sqrt{C_{d,v}}}{d}
\lt\frac{e^{v^2/2}}d.
```

Thus some hidden Pauli has success no larger than the displayed upper bound. This is an arbitrary-collective-measurement converse, not a restriction to measuring individual specimens.

For the paired interface at $`v=1`$, there is an explicit Bell-measurement and Gaussian-elimination algorithm with

```math
\Pr[\widehat w\ne w]
\le 2(d^2-1)(2/3)^N
```

for every $`w`$. Hence $`N=O(n+\log(1/\delta))`$ suffices for failure at most $`\delta`$. The [paired-learning proof](paired-learning.md) includes the source, measurement, finite-field equations and rank guarantee. This efficient algorithm is not asserted for $`v\lt1`$.

## Theorem 3: a coherent model cannot bypass the obstruction

Allow a learner to retain a quantum program from the anonymous batch and consume it in a fixed trace-preserving processor on one later input. Let $`\mathcal E_w`$ be its induced channel and let $`F_{\mathrm{avg}}(\mathcal E_w,W_w)`$ be its fidelity, averaged over a Haar-random pure input, to the ideal Pauli channel. Every outcome is included in this score. Then

```math
\frac1{d^2}\sum_wF_{\mathrm{avg}}(\mathcal E_w,W_w)
\le\frac{\sqrt{C_{d,v}}+1}{d+1}.
```

By contrast, the paired learner at $`v=1`$ can identify $`w`$ with failure at most $`\delta`$ and then apply its Pauli circuit, attaining average input fidelity at least $`1-d\delta/(d+1)`$ for every $`w`$. The [prediction page](prediction.md) proves both assertions.

These theorems concern native quantum data and a specified loss of correspondence. They do not establish a classical-data computational speedup, a noisy-device implementation threshold or an obstruction for arbitrary demonstration sources. The [resource account](resources.md) and [interpretation](interpretation.md) delimit those conclusions.
