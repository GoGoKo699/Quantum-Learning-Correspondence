# Information saturation and identification

The [exact kernel](correlation-kernel.md) bounds the purity of the entire anonymous batch. This page converts that bound into two operational statements. The first controls the information that any measurement can reveal. The second directly bounds the success of identifying the hidden transformation and gives the quantitative benchmark used in the main theorem.

## A reference-state entropy bound

Let $`\tau=I/D`$ on the full batch Hilbert space. For any density operator $`\omega`$,

```math
D(\omega\Vert \tau)
=\log D-S(\omega)
\le\log\!\left(D\mathrm{Tr}\omega^2\right).
```

Here $`D(\cdot\Vert \cdot)`$ is quantum relative entropy. To see the inequality directly, diagonalize $`\omega`$ with eigenvalues $`\lambda_j`$ and apply concavity of the logarithm with weights $`\lambda_j`$:

```math
\sum_j\lambda_j\log\lambda_j
\le\log\!\left(\sum_j\lambda_j^2\right).
```

Zero eigenvalues are handled by continuity. Full rank of the source is unnecessary because the reference $`\tau`$ is full rank.

For an ensemble $`\{p_\theta,\omega_\theta\}`$ with average $`\overline\omega`$, the relative-entropy decomposition gives

```math
\sum_\theta p_\theta D(\omega_\theta\Vert \tau)
=\chi(\{p_\theta,\omega_\theta\})
+D(\overline\omega\Vert \tau).
```

The last term is nonnegative. The same identity holds with an integral for a continuous prior. Hence a uniform purity bound $`D\mathrm{Tr}\omega_\theta^2\le C`$ implies

```math
\chi(\{p_\theta,\omega_\theta\})\le\log C.
```

By the Holevo bound, the mutual information between the parameter and the outcome of any measurement is no greater than this quantity. The measurement may act jointly on the entire batch and arbitrary initialized ancillas.

## Less than one nat for transformed swap pairs

For $`\omega_U=\Omega_{N,v}(U)`$, the kernel theorem supplies $`C=C_{d,v}`$ for every $`U`$ and every $`N`$. Moreover,

```math
\begin{aligned}
\log C_{d,v}
&=-(d^2-1)\log(1-t^2)\\
&\le\frac{(d^2-1)t^2}{1-t^2}\\
&=\frac{(d^2-1)v^2}{d(d+2v)}
\lt v^2\le1.
\end{aligned}
```

We used $`-\log(1-x)\le x/(1-x)`$ for $`0\le x\lt1`$. Thus one anonymous batch carries less than one nat of Holevo information about the unknown unitary, regardless of its size. At fixed $`v`$, the upper-bound constant satisfies $`\log C_{d,v}\to v^2`$ as $`d\to\infty`$; it does not grow with the number of unitary parameters.

This is an upper bound on information, not a claim that it is all accessible or that the bound is tight. A finite amount of information can still identify a sufficiently small discrete class; the next argument gives the explicit failure probability for the class used here.

## A direct discrimination inequality

**Lemma 5.** Suppose $`M`$ equally likely density operators on a $`D`$-dimensional space obey $`D\mathrm{Tr}\omega_i^2\le C`$. For every POVM $`\{E_i\}_{i=1}^M`$,

```math
P_{\mathrm{guess}}
=\frac1M\sum_i\mathrm{Tr}(E_i\omega_i)
\le\left(\frac{C}{M}\right)^{1/2}.
```

**Proof.** Apply Hilbert–Schmidt Cauchy–Schwarz to the direct sum of the operators:

```math
\begin{aligned}
\sum_i\mathrm{Tr}(E_i\omega_i)
&\le
\left(\sum_i\mathrm{Tr}E_i^2\right)^{1/2}
\left(\sum_i\mathrm{Tr}\omega_i^2\right)^{1/2}\\
&\le\left(D\cdot\frac{MC}{D}\right)^{1/2}
=\sqrt{MC}.
\end{aligned}
```

The second line uses $`0\le E_i\le I`$, hence $`E_i^2\le E_i`$, and $`\sum_iE_i=I`$. Divide by $`M`$. Internal adaptive measurements, intermediate classical records and ancillas are already represented by a POVM on the received state, so they do not evade the bound.

## Applying the inequality to Pauli learning

For $`d=2^n`$, take the $`M=d^2`$ Pauli transformations $`W_w`$, with the uniform prior. Each anonymous source has the same purity upper bound. Lemma 5 therefore gives, for every $`N`$,

```math
P_{\mathrm{guess}}^{\mathrm{anonymous}}
\le\frac{\sqrt{C_{d,v}}}{d}
\lt\frac{e^{v^2/2}}d.
```

This decreases exponentially in $`n`$. The result concerns success averaged over the hidden-Pauli prior. Consequently no learner can guarantee a larger success probability for every hidden Pauli. It is not asserted that every individual Pauli is difficult for a learner designed to favor a particular label.

Because $`C_{d,v}\lt e\lt4\le d^2`$, the upper bound is strictly below one at every fixed $`d\ge2`$. Uniform consistent identification is therefore impossible as $`N\to\infty`$ even in a fixed dimension. The stronger high-dimensional conclusion is that success remains small for every batch size, including sizes that grow arbitrarily quickly with $`d`$.

The [prediction theorem](prediction.md) turns this identification obstruction into a gate-fidelity obstruction for both classical estimates and coherent learned programs. Its conclusion does not rely on requiring the learner to reveal the label $`w`$.

## Scope of the general determinant bound

For a family of uniform-marginal sources with correlation matrices $`T_\theta`$, strict contraction and a common bound

```math
C(T_\theta)
=\det(I-T_\theta T_\theta^{\mathsf T})^{-1}
\le C
```

give the same information and discrimination inequalities. These constants can depend on the physical source family and its dimension. The special transformed-swap family has the additional dimension-uniform bound $`\log C_{d,v}\lt1`$.

If a source has parameter-dependent marginals, an unpaired list can itself contain learnable information and this theorem does not apply. If a correlation singular value reaches one, the finite determinant ceiling is unavailable. These are changes in the mathematical premises, not loopholes in the collective-measurement argument.
