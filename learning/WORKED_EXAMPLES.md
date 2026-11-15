# Two finite calculations

These examples use the [canonical source and acquisition interfaces](../science/model.md), with one qubit per register and visibility one: $`n=1`$, $`d=2`$, $`v=1`$. Preparation seeds remain private. They illustrate the theorem rather than estimate the performance of an optimal anonymous measurement.

## The hidden Pauli is a missing Bell outcome

Write a Pauli label as $`w=(x,z)`$, in the order used by the [paired decoder](../science/paired-learning.md):

| Label | Pauli, up to phase | Bell state $`(I\otimes W_b)\lvert\Phi\rangle`$ when used as outcome label $`b`$ |
|---|---|---|
| $`00`$ | $`I`$ | $`\Phi^+`$ |
| $`10`$ | $`X`$ | $`\Psi^+`$ |
| $`01`$ | $`Z`$ | $`\Phi^-`$ |
| $`11`$ | $`Y`$ | $`\Psi^-`$, up to phase |

Here $`q(x,z)=xz`$. An identified pair has Bell-outcome probabilities

```math
\Pr[b\mid w]=\frac{1+(-1)^{q(b+w)}}6.
```

For one qubit, $`q`$ is one only at $`11`$. Exactly one Bell label is forbidden for each hidden transformation:

| Hidden label $`w`$ | Forbidden outcome $`b=w+11`$ | Other outcomes |
|---|---|---|
| $`00`$ | $`11`$ | Each has probability $`1/3`$. |
| $`10`$ | $`01`$ | Each has probability $`1/3`$. |
| $`01`$ | $`10`$ | Each has probability $`1/3`$. |
| $`11`$ | $`00`$ | Each has probability $`1/3`$. |

Seeing all three allowed labels therefore identifies the fourth, absent label and hence the hidden Pauli. Observing just one or two distinct labels does not establish which remaining label is forbidden. With $`N\ge1`$ independent paired measurements, the probability of seeing all three allowed labels is exactly

```math
1-3(2/3)^N+3(1/3)^N.
```

For example, at $`N=3`$ it is $`2/9`$, and it tends to one as the number of identified pairs grows. This is the success of the particular rule that declares failure until it has seen all three; it is not a claim of optimal finite-sample success.

### The same observations as a linear decoder

Let the hidden transformation be $`Y`$, so $`w=(1,1)`$. Consider the valid observed labels $`10,01,11`$. Each row of

```math
[b,w]+c=q(b),\qquad c=q(w)
```

is linear in the augmented unknown $`(x,z,c)`$. The three observations give

| Observed $`b`$ | Row $`(z_b,x_b,1\mid q(b))`$ | Equation over $`\mathbb F_2`$ |
|---|---|---|
| $`10`$ | $`(0,1,1\mid0)`$ | $`z+c=0`$ |
| $`01`$ | $`(1,0,1\mid0)`$ | $`x+c=0`$ |
| $`11`$ | $`(1,1,1\mid1)`$ | $`x+z+c=1`$ |

The first two equations give $`x=z=c`$. Substitution in the third gives $`c=1`$, so the unique solution is $`(x,z,c)=(1,1,1)`$. It satisfies the required quadratic check $`c=xz`$. This is ordinary binary Gaussian elimination on valid source outcomes. For general $`n`$, the [paired-learning page](../science/paired-learning.md) proves that a linear number of observations gives full affine rank with high probability.

## Two anonymous pairs and a nonzero error floor

For the same physical source, erase the correspondence between two output registers before any measurement. Set

```math
C_N=D\mathrm{Tr}\Omega_N(W)^2,\qquad D=2^{2N}.
```

This is normalized collision purity, independent of the hidden Pauli. It is not the probability of a collision between two classical Bell records. The [cycle formula](../science/correlation-kernel.md) has $`p=3`$ and $`t=1/3`$, giving cycle weight $`a_\ell=1+3t^{2\ell}`$.

There are two relative permutations at $`N=2`$. The identity has two cycles of length one; the transposition has one cycle of length two. Therefore

```math
a_1=\frac43,\qquad a_2=\frac{28}{27},\qquad
C_2=\frac{a_1^2+a_2}{2}=\frac{38}{27}.
```

The unnormalized collision purity is $`\mathrm{Tr}\Omega_2^2=C_2/16=19/216`$. With four equally likely hidden Paulis, the [direct discrimination bound](../science/information-ceiling.md) gives

```math
P_{\mathrm{guess}}\le\frac12\left(\frac{38}{27}\right)^{1/2}
\approx0.593171,
\qquad
P_{\mathrm{error}}\ge0.406829.
```

The bound permits every measurement on all four registers. It does not assume bitwise Bell readout or a guessed matching.

Increasing the size of this single anonymous batch still leaves the uniform bound

```math
C_N\le(1-1/9)^{-3}=\frac{729}{512},\qquad
P_{\mathrm{error}}\ge1-\frac{27}{32\sqrt2}
\approx0.403379.
```

This last inequality is the illustrated error floor: it remains positive for every batch size. It is an upper bound on possible success, not an exact evaluation of the optimal anonymous measurement. The paired rule above approaches success one using the same source. Independently repeated anonymous batches with their batch boundaries retained would be a different acquisition interface.
