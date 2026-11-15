# Efficient learning when the pairs are identified

The anonymous-data converse permits an unlimited number of demonstrations. To understand what the missing correspondence costs, we need an explicit learner using exactly the same underlying source with its pairs identified. For ideal demonstrations and a hidden Pauli transformation, Bell measurements give such a learner.

Throughout this page $`d=2^n`$ and $`v=1`$. The source preparation, private seeds and absence of chosen-unitary queries are the same as in the [model](model.md).

## Pauli labels and Bell states

Represent a Pauli, up to its irrelevant global phase, by

```math
w=(x,z)\in\mathbb F_2^{2n},\qquad
W_w=i^{\sum_jx_jz_j}X^xZ^z.
```

Define the quadratic form and symplectic form

```math
q(w)=x\cdot z\pmod2,\qquad
[b,w]=x_b\cdot z+z_b\cdot x\pmod2.
```

They obey

```math
W_w^{\mathsf T}=(-1)^{q(w)}W_w,\qquad
q(b+w)=q(b)+q(w)+[b,w].
```

Let $`|\Phi\rangle=d^{-1/2}\sum_j|j\rangle|j\rangle`$ and use the Bell basis $`|\Phi_b\rangle=(I\otimes W_b)|\Phi\rangle`$. Since $`F|\Phi_b\rangle=(-1)^{q(b)}|\Phi_b\rangle`$, the conjugated swap satisfies

```math
F_{W_w}|\Phi_b\rangle
=(-1)^{q(b+w)}|\Phi_b\rangle.
```

Global phases from multiplying Pauli matrices disappear from this eigenvalue relation.

## One demonstration gives one equation

Measure one identified pair $`\rho_{W_w,1}`$ in the Bell basis. Its outcome distribution is

```math
\Pr[b\mid w]
=\frac{1+(-1)^{q(b+w)}}{d(d+1)}
=\begin{cases}
2/[d(d+1)],&q(b+w)=0,\\
0,&q(b+w)=1.
\end{cases}
```

Thus every observed $`b`$ satisfies

```math
[b,w]+c=q(b),\qquad c=q(w).
```

This is a linear equation in the $`2n+1`$ augmented unknown bits $`(w,c)`$. The true value always solves every observed equation. If the observed labels span the full affine space $`\mathbb F_2^{2n}`$, their augmented coefficient matrix has full rank, so the solution is unique and recovers $`w`$.

The physical measurement is ordinary bitwise Bell readout: apply a CNOT from each input qubit to its partnered output qubit, apply a Hadamard to the input, then measure both in the computational basis. It uses $`O(n)`$ known gates per pair. The association identifies which qubits these gates should connect.

## Why a linear number of equations suffices

Let

```math
Q=\{b\in\mathbb F_2^{2n}:q(b)=0\}.
```

For $`a\ne0`$, the quadratic Gauss sum gives

```math
\sum_b(-1)^{q(b)+[a,b]}=d(-1)^{q(a)}.
```

To verify it, write $`a=(u,v)`$ and $`b=(x,z)`$. Summing over $`z`$ first gives zero unless $`x=u`$; the surviving term is $`d(-1)^{u\cdot v}`$. Taking $`a=0`$ gives $`\sum_b(-1)^{q(b)}=d`$, so

```math
|Q|=\frac{d^2+d}{2}.
```

Using the indicator $`1_Q(b)=[1+(-1)^{q(b)}]/2`$ and the vanishing sum of a nontrivial character, we obtain

```math
\mathbb E_{b\sim\operatorname{Unif}(Q)}(-1)^{[a,b]}
=\frac{(-1)^{q(a)}}{d+1},\qquad a\ne0.
```

The actual distribution is uniform on the translate $`Q+w`$. Translation changes only the sign of this Fourier coefficient. Therefore every affine hyperplane $`[a,b]=e`$ with $`a\ne0`$ contains probability at most

```math
\frac12\left(1+\frac1{d+1}\right)
=\frac{d+2}{2(d+1)}\le\frac23.
```

A proper affine subspace is contained in an affine hyperplane. There are $`2(d^2-1)`$ choices of a nonzero normal $`a`$ and offset $`e`$. Independence of the paired demonstrations and a union bound now give

```math
\Pr[\text{observed labels lack full affine span}]
\le2(d^2-1)(2/3)^N.
```

This argument holds for every hidden $`w`$, including $`n=1`$. Taking

```math
N\ge
\left\lceil
\frac{\log\!\left(2(d^2-1)/\delta\right)}{\log(3/2)}
\right\rceil
```

ensures recovery failure at most $`\delta`$. Since $`\log d=n\log2`$, the required number is $`O(n+\log(1/\delta))`$.

## The complete learner

1. Receive $`N`$ demonstrations from the native source, with their input–output pairs identified.
2. Bell-measure each pair and retain its $`2n`$-bit label $`b`$.
3. Form the affine linear equations $`[b,w]+c=q(b)`$ and solve them by Gaussian elimination over $`\mathbb F_2`$.
4. If the augmented matrix has full rank, output its unique Pauli label $`w`$. Otherwise declare failure or use any fixed fallback label.

The algorithm uses polynomial classical time and storage. It does not require coherent storage between different demonstrations: each pair can be measured on arrival. Its essential coherent operation is the Bell measurement within an identified pair. Source preparation and the pairing information are charged separately in the [resource account](resources.md).

## Why the visibility endpoint matters

For $`v\lt1`$, the Bell distribution becomes

```math
\Pr[b\mid w]
=\frac{1+v(-1)^{q(b+w)}}{d(d+v)}.
```

Both quadratic signs then have positive probability. The exact linear equations used above are no longer guaranteed. The anonymous-data converse remains valid throughout $`0\lt v\le1`$, but this polynomial-time paired learner is asserted at $`v=1`$ only. No efficient algorithm for the corresponding noisy equations is assumed.

The endpoint is physically meaningful: it is an ideal separable 2-design source, not a noiseless entangled training pair or an uncharged unitary-query oracle. The matched comparison at that endpoint already establishes the effect of correspondence alone.
