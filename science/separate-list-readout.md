# Separate collective readout of growing anonymous batches

An anonymous batch loses most of the information in its original input–output pairs. The information that remains has a sharper description: at fixed local dimensions and strict correlation contraction, it becomes a classical Gaussian covariance experiment. Separate collective measurements of the two lists retain the entire surviving statistical experiment asymptotically. Quantum interaction between the lists supplies no persistent advantage for a bounded decision task in this limit.

The word **collective** matters. Each measurement may couple all specimens within its own list. This is a different access class from measuring the two registers of each original pair separately and retaining only classical records between pairs. The result concerns a growing anonymous batch; it asserts neither exact sufficiency at a finite batch size nor efficient implementation.

## The source and the limiting experiment

Let the input and output dimensions be $`d_A,d_B\ge2`$. Choose complete traceless Hermitian bases with

```math
\operatorname{tr}_A(A_aA_c)=\delta_{ac},\qquad
\operatorname{tr}_B(B_bB_e)=\delta_{be},
\qquad \operatorname{tr}_A=\frac{\operatorname{Tr}}{d_A},
\quad \operatorname{tr}_B=\frac{\operatorname{Tr}}{d_B}.
```

Write $`p_A=d_A^2-1`$ and $`p_B=d_B^2-1`$. A physical source with uniform local marginals has the form

```math
\rho_T=\frac1{d_Ad_B}
\left(I+\sum_{a=1}^{p_A}\sum_{b=1}^{p_B}
T_{ab}A_a\otimes B_b\right),
```

where $`T`$ is real. Positivity of $`\rho_T`$ is an assumption; an arbitrary real matrix need not define a state. Let $`\Omega_N(T)`$ denote the state of $`N`$ independent source pairs after a uniform permutation of the output list, with the permutation and preparation records withheld as in the [anonymous model](model.md).

Fix a compact family $`\mathcal K`$ of physical matrices and a constant $`r\lt1`$ such that

```math
\sup_{T\in\mathcal K}\|T\|_{\mathrm{op}}\le r.
```

Local dimensions and this family remain fixed while $`N\to\infty`$. Define the classical experiment

```math
P_T=\mathcal N(0,\Sigma_T),\qquad
\Sigma_T=\begin{pmatrix}I_{p_A}&T\\T^{\mathsf T}&I_{p_B}\end{pmatrix}.
```

Strict contraction makes every $`\Sigma_T`$ positive definite. This is one Gaussian observation whose covariance depends on the target, rather than a growing number of independent Gaussian observations.

## Theorem 7: asymptotic separate-list sufficiency

There are target-independent local projective measurements $`M_N^A`$ on the full input list and $`M_N^B`$ on the full output list, together with target-independent local state-preparation channels $`R_N^A,R_N^B`$, such that

```math
\varepsilon_N:=(d_Ad_B)^{N/2}
\sup_{T\in\mathcal K}
\left\|\Omega_N(T)-
(R_N^A\otimes R_N^B)(M_N^A\otimes M_N^B)
\bigl(\Omega_N(T)\bigr)\right\|_2
\longrightarrow0.
```

Here $`\|\cdot\|_2`$ is the ordinary, unnormalized Hilbert–Schmidt norm. In particular,

```math
\sup_{T\in\mathcal K}
\left\|\Omega_N(T)-
(R_N^A\otimes R_N^B)(M_N^A\otimes M_N^B)
\bigl(\Omega_N(T)\bigr)\right\|_1
\le\varepsilon_N\longrightarrow0.
```

Both measurements act on their own list only; their outcomes may be combined classically. Reconstruction prepares the normalized local spectral projectors associated with those outcomes. The same receiver sequence works for the whole family $`\mathcal K`$ and does not require knowing $`T`$.

Moreover, the measured experiment and $`\{P_T:T\in\mathcal K\}`$ are asymptotically equivalent: there are target-independent classical Markov kernels in both directions whose maximal total-variation errors tend to zero. Combining the reverse kernel with $`R_N^A\otimes R_N^B`$ reconstructs the original quantum experiment in trace norm. Thus the Gaussian covariance experiment describes all surviving statistical information, rather than only a collection of moments.

### 1. The full likelihood norm

Set $`D_N=(d_Ad_B)^N`$, let $`\tau_N(X)=\operatorname{Tr}(X)/D_N`$, and define

```math
L_N(T)=D_N\Omega_N(T),\qquad
\|X\|_{2,\tau_N}^2=\tau_N(X^\dagger X).
```

The [exact correlation kernel](correlation-kernel.md) gives

```math
\|L_N(T)\|_{2,\tau_N}^2
=\sum_{k=0}^N h_k(TT^{\mathsf T})
\longrightarrow C(T):=\det(I-TT^{\mathsf T})^{-1},
```

where

```math
\det(I-zM)^{-1}=\sum_{k\ge0}h_k(M)z^k.
```

The convergence is uniform on $`\mathcal K`$. Indeed, with $`q=\min(p_A,p_B)`$,

```math
0\le h_k(TT^{\mathsf T})
\le\binom{k+q-1}{q-1}r^{2k},
```

and the series of upper bounds is summable.

Let $`\gamma=\mathcal N(0,I_{p_A+p_B})`$ and write $`\ell_T=dP_T/d\gamma`$. Its density ratio is

```math
\ell_T(z)=\det(\Sigma_T)^{-1/2}
\exp\!\left[-\frac12z^{\mathsf T}
(\Sigma_T^{-1}-I)z\right].
```

Because $`\|T\|_{\mathrm{op}}\lt1`$, the eigenvalues of $`\Sigma_T`$ lie below two. Gaussian integration therefore gives

```math
\|\ell_T\|_{L^2(\gamma)}^2
=\frac1{\sqrt{\det(\Sigma_T)\det(2I-\Sigma_T)}}
=\det(I-TT^{\mathsf T})^{-1}=C(T).
```

The last equality follows from the singular values of $`T`$: the nontrivial eigenvalues of $`\Sigma_T`$ are $`1\pm s_j(T)`$. The Gaussian likelihood exhausts exactly the limiting full quantum likelihood norm. This equality is the step that will exclude residual information invisible to the fluctuation observables.

The map $`T\mapsto\ell_T`$ is continuous in $`L^2(\gamma)`$ on $`\mathcal K`$. For example, the bounds $`(1-r)I\le\Sigma_T\le(1+r)I`$ dominate $`\ell_T^2\,d\gamma`$ uniformly by a constant times

```math
\exp\!\left[-\frac{1-r}{2(1+r)}|z|^2\right]dz.
```

Consequently the set of these likelihoods is compact in $`L^2(\gamma)`$.

### 2. Bounded Fourier fluctuations approximate the entire likelihood

For $`x\in\mathbb R^{p_A}`$ and $`y\in\mathbb R^{p_B}`$, define

```math
H_x=\sum_ax_aA_a,\qquad K_y=\sum_by_bB_b,
```

and the local unitaries

```math
W_N^A(x)=\left(e^{iH_x/\sqrt N}\right)^{\otimes N},\qquad
W_N^B(y)=\left(e^{iK_y/\sqrt N}\right)^{\otimes N}.
```

Each is invariant under permutations within its list. Hence output shuffling disappears from their joint expectation exactly:

```math
\tau_N\!\left[L_N(T)
\bigl(W_N^A(x)\otimes W_N^B(y)\bigr)\right]
=\left[\operatorname{Tr}\rho_T
\bigl(e^{iH_x/\sqrt N}\otimes e^{iK_y/\sqrt N}\bigr)\right]^N.
```

The source has zero local first moments, unit local covariance in the chosen bases, and cross-covariance $`T`$. A finite-dimensional Taylor expansion gives

```math
\operatorname{Tr}\rho_T
\bigl(e^{iH_x/\sqrt N}\otimes e^{iK_y/\sqrt N}\bigr)
=1-\frac{|x|^2+|y|^2+2x^{\mathsf T}Ty}{2N}
+O_{x,y}(N^{-3/2}),
```

uniformly in $`T\in\mathcal K`$. Therefore the expectation converges to

```math
\exp\!\left[-\frac12
\bigl(|x|^2+|y|^2+2x^{\mathsf T}Ty\bigr)\right]
=\mathbb E_{P_T}e^{i(x^{\mathsf T}X+y^{\mathsf T}Y)}.
```

Likewise, the normalized-trace Gram matrices converge to the independent Gaussian Fourier Gram matrices. On side $`A`$,

```math
\tau_{A,N}\!\left[W_N^A(x)^\dagger W_N^A(x')\right]
=\left[\operatorname{tr}_A
e^{-iH_x/\sqrt N}e^{iH_{x'}/\sqrt N}\right]^N
\longrightarrow e^{-|x-x'|^2/2},
```

and the two sides factor under $`\tau_N`$.

Take any finite Fourier sum

```math
q(z)=\sum_{\ell=1}^L c_\ell
e^{i(x_\ell^{\mathsf T}z_A+y_\ell^{\mathsf T}z_B)},
\qquad
q_N=\sum_{\ell=1}^L c_\ell
W_N^A(x_\ell)\otimes W_N^B(y_\ell).
```

Expanding the squared norm and using the preceding three limits proves

```math
\|L_N(T)-q_N\|_{2,\tau_N}^2
\longrightarrow\|\ell_T-q\|_{L^2(\gamma)}^2,
```

uniformly in $`T\in\mathcal K`$. Thus the argument uses the entire likelihood norm, not only convergence of characteristic functions.

Finite Fourier sums are dense in $`L^2(\gamma)`$. To verify density, a function orthogonal to all characters defines a finite complex measure $`f\,d\gamma`$ with zero Fourier transform; uniqueness of the Fourier transform implies $`f=0`$. Compactness of the Gaussian likelihood family now implies that, for every $`\eta\gt0`$, finitely many Fourier sums $`q_1,\ldots,q_J`$ satisfy

```math
\sup_{T\in\mathcal K}\min_{1\le j\le J}
\|\ell_T-q_j\|_{L^2(\gamma)}\lt\eta.
```

Use the union of their finitely many local frequencies. The assignment of a nearby $`q_j`$ to each $`T`$ is only a proof device; the receiver will use that whole frequency set and will not need the assignment or the target.

### 3. One commuting measurement on each list

The finite local Fourier family asymptotically commutes in normalized Hilbert–Schmidt norm. This follows from an exact estimate. Put

```math
F_N^A(x)=\frac1{\sqrt N}\sum_{i=1}^N H_x^{(i)}.
```

Then

```math
[F_N^A(x),F_N^A(x')]
=\frac1N\sum_{i=1}^N[H_x,H_{x'}]^{(i)}.
```

The one-register commutator is traceless, so cross terms vanish under the product normalized trace and

```math
\bigl\|[F_N^A(x),F_N^A(x')]\bigr\|_{2,\tau_{A,N}}
=\frac{\|[H_x,H_{x'}]\|_{2,\operatorname{tr}_A}}{\sqrt N}.
```

Duhamel's formula and unitary invariance of this norm give

```math
\|[e^{iH},e^{iK}]\|_{2,\tau}
\le\|[H,K]\|_{2,\tau}
```

for Hermitian $`H,K`$. Applying the bound to $`F_N^A(x),F_N^A(x')`$ proves that every required commutator of $`W_N^A`$ tends to zero. The same holds on side $`B`$.

Glebsky's [Theorem 2](https://arxiv.org/html/1002.3082v1), for any fixed finite number of unitary matrices, supplies pairwise commuting unitary approximants whenever all pairwise commutators tend to zero in normalized Hilbert–Schmidt norm. Its approximation modulus is independent of matrix dimension. Apply this inherited theorem separately on $`A^N`$ and $`B^N`$. Obtain exactly commuting local families $`V_N^A(x)`$ and $`V_N^B(y)`$ satisfying

```math
\max_x\|W_N^A(x)-V_N^A(x)\|_{2,\tau_{A,N}}\to0,
\qquad
\max_y\|W_N^B(y)-V_N^B(y)\|_{2,\tau_{B,N}}\to0.
```

There is no operator-norm almost-commutation claim. Nor is Glebsky's theorem applied to an arbitrarily growing frequency family: each approximation level uses a fixed finite set.

Let $`\{P_i\}`$ and $`\{Q_j\}`$ be the common spectral projectors of the two commuting families, with ranks $`r_i`$ and $`s_j`$. Measure these projectors locally. Given outcomes $`(i,j)`$, reconstruct

```math
\frac{P_i}{r_i}\otimes\frac{Q_j}{s_j}.
```

The resulting measurement-and-preparation map is

```math
E_N(X)=\sum_{i,j}
\frac{\operatorname{Tr}[(P_i\otimes Q_j)X]}{r_i s_j}
(P_i\otimes Q_j).
```

It is a product, unital, trace-preserving completely positive map and the $`L^2(\tau_N)`$ orthogonal projection onto the product abelian spectral algebra. It replaces every spectral block by a scalar multiple of its identity; it is not merely block pinching. This distinction makes the retained record fully classical.

Replacing the finitely many $`W`$'s in each $`q_{j,N}`$ by $`V`$'s gives $`\widetilde q_{j,N}`$ in that abelian algebra with

```math
\max_j\|q_{j,N}-\widetilde q_{j,N}\|_{2,\tau_N}\to0.
```

Orthogonal projection minimizes $`L^2`$ distance. The uniform Fourier approximation therefore implies

```math
\limsup_{N\to\infty}\sup_{T\in\mathcal K}
\|L_N(T)-E_NL_N(T)\|_{2,\tau_N}\le\eta.
```

For a sequence $`\eta_k\downarrow0`$, choose successively larger thresholds $`N_k`$ such that the level-$`k`$ construction has all its required errors small for every $`N\ge N_k`$. For $`N_k\le N\lt N_{k+1}`$, use that construction. This diagonal sequence is a single target-independent receiver, and its uniform normalized $`L^2`$ error tends to zero.

Finally,

```math
\|\Omega_N(T)-E_N\Omega_N(T)\|_1
=\|L_N(T)-E_NL_N(T)\|_{1,\tau_N}
\le\|L_N(T)-E_NL_N(T)\|_{2,\tau_N}.
```

The same last quantity equals $`\sqrt{D_N}`$ times the ordinary Hilbert–Schmidt error for density operators. This proves the first part of the theorem.

### 4. Two-way equivalence with the Gaussian covariance experiment

Fix one approximation level. The local commuting unitaries have joint eigenvalue vectors $`c_N(i,j)`$ in a fixed finite-dimensional torus $`\mathcal C`$. Under the maximally mixed reference, their outcome law is

```math
\mu_N(i,j)=\frac{r_i}{d_A^N}\frac{s_j}{d_B^N}.
```

Let $`G=(X,Y)\sim\gamma`$, and let $`\phi(G)\in\mathcal C`$ collect the corresponding local Fourier coordinates $`e^{ix^{\mathsf T}X}`$ and $`e^{iy^{\mathsf T}Y}`$.

The laws of $`c_N`$ under $`\mu_N`$ converge weakly to the law of $`\phi(G)`$. Indeed, telescoping any fixed word transfers its tracial expectation from the commuting approximants to the original bounded Fourier unitaries. The latter word expectation is an $`N`$th power of a one-site expectation. Its second-order trace expansion gives the corresponding Gaussian Fourier moment; traciality removes the order-dependent commutator terms. Laurent polynomials in the torus coordinates are dense in its continuous functions, so convergence of these moments proves weak convergence.

The measured target likelihood relative to $`\mu_N`$ is

```math
h_{N,T}(i,j)=
\frac{\operatorname{Tr}[(P_i\otimes Q_j)L_N(T)]}{r_i s_j}.
```

It is nonnegative, integrates to one, and represents $`E_NL_N(T)`$. Each finite Fourier sum is a continuous function of the torus coordinates. With the same finite index assignment $`j(T)`$ as above,

```math
\limsup_N\sup_{T\in\mathcal K}
\|h_{N,T}-q_{j(T)}\circ c_N\|_{L^1(\mu_N)}\le\eta,
\qquad
\sup_{T\in\mathcal K}
\|\ell_T-q_{j(T)}\circ\phi\|_{L^1(\gamma)}\le\eta.
```

Here each $`q_j`$ is understood as its continuous function of the Fourier-coordinate vector. The first bound follows by applying the $`L^2`$-contractive conditional expectation to the likelihood approximation, then using $`L^1\le L^2`$.

Compactness of $`\mathcal C`$ allows a reference coupling of $`c_N`$ and $`\phi(G)`$ whose expected distance tends to zero. Lift that coupling to a coupling $`\pi_N`$ of the full measured outcome and $`G`$, using conditional distributions over the coordinate maps. All spaces are standard Borel, and the measured outcome space is finite. Let

```math
K_N(dg\mid i,j)=\pi_N(dg\mid i,j),\qquad
H_N(i,j\mid g)=\pi_N(i,j\mid g).
```

These are target-independent kernels. Compare, on this common coupling space, the two densities $`h_{N,T}(i,j)`$ and $`\ell_T(g)`$. Their $`L^1`$ difference is at most the sum of the two approximation errors above and

```math
\mathbb E_{\pi_N}
\left|q_{j(T)}(c_N(i,j))-q_{j(T)}(\phi(G))\right|.
```

The latter tends to zero uniformly over the finite family of $`q_j`$ by uniform continuity. Marginalization and the factor one half between $`L^1`$ distance and total variation prove that both kernel errors have limiting supremum at most $`\eta`$. Include these errors in the preceding diagonal choice as $`\eta\downarrow0`$. This proves two-way classical equivalence. Forward quantum-to-Gaussian conversion first performs the separate-list measurement and then $`K_N`$; reverse conversion applies $`H_N`$ and prepares the normalized product spectral projectors. The trace-norm reconstruction error already proved tends to zero. This completes the theorem.

## Consequences for learning and coherent prediction

For every joint POVM on the original batch, its outcome distribution can be simulated from the separate-list records: given $`(i,j)`$, apply that POVM to the known reconstructed state, or sample the resulting known classical probabilities. The maximal total-variation discrepancy is at most $`\varepsilon_N/2`$. Consequently arbitrary priors and losses valued in $`[0,1]`$ have optimal risks differing by at most $`\varepsilon_N/2`$ between unrestricted joint readout and this separate-list receiver. This includes finite hypothesis tests, identification, and bounded unitary-estimation losses.

The conclusion also covers a [consumable quantum predictor](prediction.md). Let a target-independent trace-preserving processor consume the training batch together with a later input. Replacing the batch by its reconstruction changes the induced channel by at most $`\varepsilon_N`$ in diamond norm: append any input/reference state and use trace-norm contractivity of the processor. In particular, its Haar-average transformation fidelity changes by at most $`\varepsilon_N/2`$, with every output branch counted. Thus a coherent program cannot retain a persistent bounded-score benefit unavailable after separate collective readout in this limit. This conclusion concerns statistical information and permits unrestricted processing of the classical records; it gives no efficient simulation algorithm.

For the transformed-swap demonstrations shared with [Quantum Learning Readout](https://github.com/GoGoKo699/Quantum-Learning-Readout/blob/ce61966034a9b72ba1c846a354f8034f5e1a9285/science/model.md),

```math
\rho_{U,v}=\frac{I+vF_U}{d(d+v)},\qquad
T=tR_U,\quad t=\frac{v}{d+v},
```

where $`R_U`$ is an orthogonal adjoint representation. At fixed $`d`$ and known $`0\lt v\lt1`$, the unitary orbit is a compact strictly contractive family, so the theorem applies uniformly over $`U`$. The proof also covers $`v=1`$, despite the pair state's rank deficiency, because $`t\lt1`$ still holds and no inverse of the pair state was used.

The paired-readout hierarchy and the anonymous-batch result concern different resources. The former quantifies precision gains while correspondence is present. The latter shows that, after one increasingly large anonymous shuffle, the remaining information admits separate collective readout. The finite information ceiling is not removed: its surviving experiment is one finite-dimensional Gaussian covariance observation.

## Independently tagged batches and limit order

Suppose there are $`m`$ independently shuffled batches, each containing $`b`$ pairs, and their batch tags are supplied. Applying the receiver independently to each batch gives a product reconstruction error at most

```math
m\varepsilon_b.
```

Thus every fixed number of tagged batches is covered as $`b\to\infty`$. Simultaneous growth $`m=m(b)`$ is covered by this argument when $`m(b)\varepsilon_b\to0`$, or by choosing a diagonal schedule large enough for a stated batch count and error. The total number of supplied pairs is $`mb`$.

No convergence rate is proved here. In particular, an $`o(1)`$ comparison for bounded decisions does not establish convergence of Fisher information, an exact high-precision coefficient, or a risk comparison after rescaling losses by a diverging sample budget. Those require additional derivative or quantitative control.

## Resources, boundaries, and attribution

The receiver retains $`N`$ specimens coherently on each side until that side's collective measurement. It may use entangling control within each list, complicated spectral measurements, large classical records, and substantial computation. The existence proof supplies no efficient synthesis, storage reduction, noise tolerance, or runtime advantage. Dimensions are fixed; a growing dimension, a contraction bound approaching one, nonuniform local marginals, or access to withheld preparation/permutation records changes the hypotheses.

The exact operator collision kernel is inherited from this project's [kernel account](https://github.com/GoGoKo699/Quantum-Learning-Correspondence/blob/00d19bd0f60c6cd34ce4b77bb3268e52120efead/science/correlation-kernel.md). Tracial fluctuation limits and simultaneous normalized-Hilbert–Schmidt approximation are established tools. The added implication is the full-likelihood norm saturation and its conversion into target-independent separate-list measurement and recovery, followed by two-way equivalence to the Gaussian covariance experiment. Covariance agreement alone would not establish this implication.

Primary foundations:

- Lev Glebsky, *Almost commuting matrices with respect to normalized Hilbert–Schmidt norm*, arXiv:1002.3082v1 (2010), [Theorem 2](https://arxiv.org/html/1002.3082v1): dimension-independent commuting approximation for a fixed finite family of unitaries. The norm is normalized Hilbert–Schmidt, not Schatten one.
- Greg Kuperberg, *A tracial quantum central limit theorem*, *Transactions of the American Mathematical Society* **357** (2005), 459–471, [arXiv:math-ph/0202035](https://arxiv.org/abs/math-ph/0202035): the general tracial Gaussian mechanism. The bounded Fourier expansions needed above were proved directly.
- The existing [related-work account](../references/RELATED_WORK.md) credits the cycle-index and classical unlabeled-data methods underlying the inherited kernel. Neither a new general central limit theorem nor a new almost-commuting theorem is claimed here.
