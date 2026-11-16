# Worked examples: from Bell records to sufficient readout

The first three examples use the [canonical source and acquisition interfaces](../science/model.md), with one qubit per register and visibility one: $`n=1`$, $`d=2`$, $`v=1`$. Preparation seeds remain private. The spectral-reconstruction example then isolates the physical channel used by the [general separate-list theorem](../science/separate-list-readout.md). These calculations explain normalizations and mechanisms; they do not evaluate an optimal finite-batch anonymous measurement or synthesize the limiting receiver.

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


## The Gaussian likelihood uses the whole collision budget

Continue with the same ideal qubit source. In the Pauli basis $`(X,Y,Z)`$, the correlation strength is $`t=1/3`$. For hidden identity, the limiting covariance is

```math
\Sigma_I=
\begin{pmatrix}I_3&tI_3\\tI_3&I_3\end{pmatrix}.
```

For hidden Pauli $`X`$, conjugation leaves the first coordinate unchanged and reverses the other two, so its cross-correlation matrix is $`t\,\mathrm{diag}(1,-1,-1)`$. Each local three-vector still has the standard Gaussian law for either target. The target is visible only in their relation; for example the expectation of the product of their third coordinates is $`t`$ for identity and $`-t`$ for Pauli $`X`$.

These Gaussian coordinates describe collective fluctuations, not a promise of measuring the three noncommuting Pauli observables exactly on each supplied qubit. The theorem constructs compatible approximants for finite Fourier families on the entire list. It holds for the full unitary orbit, including noncommuting target choices; this diagonal Pauli example is only a simple calculation.

Let $`\gamma=\mathcal N(0,I_6)`$ and write the Gaussian likelihood as

```math
\ell_I(z)=\frac{d\mathcal N(0,\Sigma_I)}{d\gamma}(z).
```

The six covariance eigenvalues are $`1+t`$ and $`1-t`$, each three times. Their paired products give

```math
\det\Sigma_I=(1-t^2)^3,\qquad
\|\ell_I\|_{L^2(\gamma)}^2
=(1-t^2)^{-3}=\frac{729}{512}.
```

This is exactly the limiting normalized quantum collision purity calculated above. The equality concerns the **full** quantum likelihood norm; it is what makes the Fourier limit complete rather than an unverified covariance analogy.

To see the normalization in a minimal Fourier approximation, take just the constant function $`q=1`$, whose quantum counterpart is the identity operator. Both likelihoods integrate to one, so

```math
\|L_N-I\|_{2,\tau_N}^2=C_N-1,
\qquad
\|\ell_I-1\|_{L^2(\gamma)}^2
=\frac{729}{512}-1=\frac{217}{512}.
```

At $`N=2`$ the finite quantum residual is $`38/27-1=11/27`$. As $`N`$ grows it tends to $`217/512`$. Thus keeping only a constant record does discard persistent information: the limiting experiment is not the independent reference. More Fourier terms can approximate the Gaussian likelihood arbitrarily well. The proof matches each finite Fourier residual on the quantum and Gaussian sides, then invokes a compatible local receiver for that whole finite dictionary. The finite diagnostic in the [verification guide](../verification/README.md) checks these identities on noncommuting target examples; the universal implication remains analytical.

## A spectral label must become a classical record

A common eigenspace may have dimension larger than one. Consider one list with a four-dimensional Hilbert space, split into rank-two projectors

```math
P_1=\lvert1\rangle\langle1\rvert+\lvert2\rangle\langle2\rvert,
\qquad
P_2=\lvert3\rangle\langle3\rvert+\lvert4\rangle\langle4\rvert.
```

The pure state $`\lvert+\rangle=(\lvert1\rangle+\lvert2\rangle)/\sqrt2`$ lies wholly in the first block. Ordinary block pinching leaves it unchanged:

```math
\sum_{i=1}^2P_i\lvert+\rangle\langle+\rvert P_i
=\lvert+\rangle\langle+\rvert.
```

A classical outcome saying only “block one” cannot reconstruct the unknown quantum state within that block. The receiver therefore uses the scalar conditional expectation

```math
E_A(X)=\sum_{i=1}^2
\frac{\mathrm{Tr}(P_iX)}{2}P_i,
\qquad
E_A(\lvert+\rangle\langle+\rvert)=\frac{P_1}{2}.
```

Its implementation is explicit: measure $`\{P_1,P_2\}`$, retain the classical label and prepare $`P_i/2`$. Applying the same construction on the other list gives a product reconstruction. If the second list has projectors $`Q_j`$ of ranks $`s_j`$, outcome $`(i,j)`$ prepares $`(P_i/2)\otimes(Q_j/s_j)`$.

This example by itself does not say that the chosen blocks suffice for the anonymous source. The theorem supplies appropriate target-independent blocks and proves

```math
\sup_T\|L_N(T)-E_NL_N(T)\|_{2,\tau_N}\longrightarrow0.
```

The conversion to physical state error has no extra dimension penalty:

```math
\|\Omega_N(T)-E_N\Omega_N(T)\|_1
=\|L_N(T)-E_NL_N(T)\|_{1,\tau_N}
\le\|L_N(T)-E_NL_N(T)\|_{2,\tau_N}.
```

Consequently the classical records can simulate every joint bounded decision rule with vanishing error. The reverse map is physical and independent of the target; it never reconstructs a private preparation seed or the missing matching.

## One large batch and many tagged batches

The Gaussian limit above gives one covariance observation for one increasingly large anonymous batch. It does not turn that batch into arbitrarily many independent observations, and the old positive error floor remains compatible with the new sufficient readout.

If $`m`$ independently shuffled batches of size $`b`$ have visible tags, product reconstruction has trace error at most $`m\varepsilon_b`$, where $`\varepsilon_b\to0`$ is the one-batch reconstruction error. Fixed $`m`$ is covered. A growing $`m(b)`$ is covered by this direct bound only when

```math
m(b)\varepsilon_b\longrightarrow0.
```

The proof does not give a usable rate for $`\varepsilon_b`$. It therefore supplies neither an arbitrary simultaneous growth law nor an exact high-precision coefficient. The receiver retains every list coherently until its collective measurement; an asymptotically classical statistical experiment does not imply a small or efficiently compiled physical measurement.
