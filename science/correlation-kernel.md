# An exact kernel for anonymous quantum pairs

The anonymous state is an average over $`N!`$ matchings. Its Hilbert–Schmidt overlap has a simpler structure: two matchings together form disjoint cycles, and each register appears in exactly two factors. This reduces the calculation to the source's two-register correlation matrix.

The cycle-index machinery and its determinant form are established tools. The calculation here applies them directly to quantum density operators, before any measurement is chosen. This is what allows the resulting converse to cover every collective learner. See [related work](../references/RELATED_WORK.md) for attribution and nearby classical anonymous-data models.

## Uniform-marginal sources

Let $`A`$ and $`B`$ have dimensions $`d_A`$ and $`d_B`$. Choose traceless Hermitian bases satisfying

```math
\operatorname{Tr}(A_aA_c)=d_A\delta_{ac},\qquad
\operatorname{Tr}(B_bB_e)=d_B\delta_{be}.
```

A bipartite density operator with both marginals maximally mixed can be written uniquely as

```math
\rho_T
=\frac1{d_Ad_B}
\left(I+\sum_{a,b}T_{ab}A_a\otimes B_b\right).
```

Its correlation matrix $`T`$ is real. Not every real matrix defines a positive density operator; positivity is part of the source assumption. Let $`\Omega_N(T)`$ be the state obtained by independently sampling $`N`$ pairs and uniformly permuting the $`B`$ registers, as in the [model](model.md). Set $`D=(d_Ad_B)^N`$ and

```math
K_N(T,S)=D\operatorname{Tr}[\Omega_N(T)\Omega_N(S)].
```

We use the formal convention $`K_0(T,S)=1`$.

## Theorem 4: cycle and determinant formulas

For any two physical source matrices $`T,S`$,

```math
K_N(T,S)
=\frac1{N!}\sum_{\tau\in S_N}
\prod_{c\in\operatorname{cyc}(\tau)}
\left(1+\operatorname{Tr}[(TS^{\mathsf T})^{|c|}]\right).
```

Equivalently, as an identity of formal power series,

```math
\sum_{N=0}^{\infty}K_N(T,S)z^N
=\frac1{1-z}\,
\frac1{\det(I-zTS^{\mathsf T})}.
```

If $`T`$ has singular values $`s_j`$ with $`\|T\|_{\mathrm{op}}\lt1`$, its self-overlap satisfies

```math
K_N(T,T)
\le C(T):=\prod_j(1-s_j^2)^{-1}
```

for every $`N`$. The upper bound is approached monotonically as $`N\to\infty`$.

### Proof: reducing two matchings to one

Expand the two permutation averages in the definition of $`K_N`$. Invariance of the trace under a common permutation removes one permutation. Every remaining relative permutation $`\tau`$ occurs $`N!`$ times, so

```math
K_N(T,S)
=\frac D{N!}\sum_{\tau\in S_N}
\operatorname{Tr}\!\left[
\rho_T^{\otimes N}
(I\otimes P_\tau)\rho_S^{\otimes N}
(I\otimes P_\tau^\dagger)\right].
```

Represent the first product as edges joining $`A_i`$ to $`B_i`$, and the second as edges joining the same input list to its permuted output list. The union is a disjoint collection of alternating cycles. A cycle of the relative permutation with length $`\ell`$ contains $`\ell`$ registers of each type and $`2\ell`$ edges, alternating between $`T`$ and $`S`$.

For each edge choose either its identity term or its correlation term. If exactly one incident edge at a register is a correlation term, the partial trace contains one traceless basis matrix and vanishes. Therefore a nonzero contribution on a connected cycle either selects no correlation edges or selects all of them. No other subset survives.

If none are selected, normalized traces give one. If all are selected, orthogonality at each $`A`$ register contracts the two $`A`$ indices, and orthogonality at each $`B`$ register contracts the two $`B`$ indices. The resulting scalar is

```math
\sum_{a_1,\ldots,a_\ell}
\sum_{b_1,\ldots,b_\ell}
T_{a_1b_1}S_{a_2b_1}
T_{a_2b_2}S_{a_3b_2}\cdots
T_{a_\ell b_\ell}S_{a_1b_\ell}
=\operatorname{Tr}[(TS^{\mathsf T})^\ell].
```

The factors $`d_A,d_B`$ from these contractions cancel the state normalizations and the prefactor $`D`$. Distinct cycles use disjoint registers, so their factors multiply. Averaging over $`\tau`$ proves the first formula.

This argument does not require basis matrices to commute. Each register contains at most two basis factors in this overlap calculation; their second-order orthogonality is sufficient.

### Proof: summing cycle types

For cycle weights $`a_\ell`$, the permutation cycle index obeys

```math
\sum_{N=0}^{\infty}\frac{z^N}{N!}
\sum_{\tau\in S_N}\prod_c a_{|c|}
=\exp\!\left(\sum_{\ell=1}^{\infty}
\frac{a_\ell z^\ell}{\ell}\right).
```

It follows by specifying the number $`m_\ell`$ of cycles of each length. The number of permutations of that type is $`N!/\prod_\ell(\ell^{m_\ell}m_\ell!)`$, and the sum over every $`m_\ell\ge0`$ factorizes into exponentials. Substitute $`a_\ell=1+\operatorname{Tr}[(TS^{\mathsf T})^\ell]`$ and use the formal identities

```math
\sum_{\ell\ge1}\frac{z^\ell}{\ell}=-\log(1-z),\qquad
\sum_{\ell\ge1}\frac{z^\ell\operatorname{Tr}(M^\ell)}\ell
=-\log\det(I-zM).
```

This proves the determinant formula without an asymptotic approximation or an assumption about diagonalizability of $`TS^{\mathsf T}`$.

For the self-overlap, $`TT^{\mathsf T}`$ has nonnegative eigenvalues $`s_j^2`$. Write

```math
\prod_j(1-zs_j^2)^{-1}=\sum_{k\ge0}h_kz^k,
\qquad h_k\ge0.
```

Then $`K_N(T,T)=\sum_{k=0}^Nh_k`$. Under strict contraction this increasing partial sum is bounded by its value at $`z=1`$, namely $`C(T)`$. This also proves the claimed limit.

## What strict contraction means

Every physical source with uniform marginals satisfies $`\|T\|_{\mathrm{op}}\le1`$. Indeed, for real vectors $`x,y`$, form $`A(x)=\sum_ax_aA_a`$ and $`B(y)=\sum_by_bB_b`$. Cauchy–Schwarz in the state $`\rho_T`$ gives

```math
|x^{\mathsf T}Ty|^2
=|\operatorname{Tr}[\rho_T A(x)\otimes B(y)]|^2
\le\operatorname{Tr}[\rho_T A(x)^2\otimes I]
\operatorname{Tr}[\rho_T I\otimes B(y)^2]
=\|x\|^2\|y\|^2.
```

Strict contraction excludes an exactly correlated pair of normalized local observables. It supplies the finite determinant bound. When a singular value equals one, this proof no longer yields a constant ceiling; no universal consistency claim is made for that boundary. Likewise, parameter-dependent local marginals fall outside this theorem, because either unpaired list can then retain direct parameter information.

## Specialization to transformed swap demonstrations

For equal dimensions choose a traceless Hermitian basis $`A_a`$ with $`\operatorname{Tr}(A_aA_b)=d\delta_{ab}`$. The swap identity is

```math
F=\frac1d\left(I+\sum_{a=1}^{p}A_a\otimes A_a\right).
```

Consequently

```math
\rho_{U,v}
=\frac1{d^2}\left(I+t\sum_{a=1}^{p}
A_a\otimes UA_aU^\dagger\right).
```

The induced correlation matrix is $`t`$ times a real orthogonal adjoint matrix. Thus every singular value is $`t`$, independent of $`U`$, and

```math
K_N(U,U)
=\sum_{k=0}^N\binom{k+p-1}{p-1}t^{2k}
\le(1-t^2)^{-p}=C_{d,v}.
```

More generally, if $`R_G`$ denotes conjugation by $`G`$ on the traceless matrices, the cross-kernel can be written

```math
\sum_{N\ge0}K_N(U,V)z^N
=\frac1{1-z}\frac1{\det(I-zt^2R_{U^\dagger V})}.
```

Changing the adjoint-matrix convention may replace the relative rotation by its inverse. The determinant is unchanged, since a real orthogonal representation has conjugate-paired eigenvalues. The self-kernel, which controls the converse, is convention independent.

The [information ceiling](information-ceiling.md) now follows from a purity bound rather than from a restriction on measurement architecture.
