# From Petz to anonymous quantum learning and sufficient readout

The educational reference is Dénes Petz, [*Quantum Information Theory and Quantum Statistics*](https://doi.org/10.1007/978-3-540-74636-2), first edition, Springer, copyright 2008. The locators below refer to that edition. They identify the concepts used from the source, without claiming that the book contains this project's source-specific theorems. No copy of the book is redistributed here.

## Verified source routes

| Petz sections | Foundation | Application here |
|---|---|---|
| §§9.1–9.2 | Coarse-graining and conditional expectations | Model the forgotten matching as a channel, then distinguish a permutation average from the scalar conditional expectation used for classical measurement and reconstruction. |
| §9.5 | Sufficiency | Ask whether a restricted measurement retains an entire statistical experiment, and require target-independent recovery rather than a match of selected moments. |
| §§10.1–10.3 | Estimation and Fisher information | Distinguish finite-batch decision risk, a growing anonymous covariance experiment, and precision limits based on many independent batches. |
| §§3.3–3.5 and §5.5 | Entropy and Holevo information | Convert an operator collision bound to an all-measurement information ceiling, without inferring an attaining receiver from the ceiling alone. |

The [supplementary Watrous route](WATROUS_BRIDGE.md) supplies detailed finite-dimensional state, channel, measurement and permutation references. Petz is the common anchor of the present route; a supplemental reference does not replace it.

## Fix the project's conventions

A supplied specimen is a quantum register; its hidden preparation label and classical state description are not supplied. A source state with uniform local marginals is expanded as

```math
\rho_T=\frac1{d_A d_B}\left(I+\sum_{a,b}T_{ab}A_a\otimes B_b\right),\qquad
\frac{\mathrm{Tr}(A_aA_c)}{d_A}=\delta_{ac},\quad
\frac{\mathrm{Tr}(B_bB_e)}{d_B}=\delta_{be}.
```

The complete batch dimension is $`D_N=(d_A d_B)^N`$. Its normalized trace is $`\tau_N(X)=\mathrm{Tr}(X)/D_N`$, and its likelihood relative to the maximally mixed reference is $`L_N(T)=D_N\Omega_N(T)`$. The norm $`\|X\|_{2,\tau_N}=\sqrt{\tau_N(X^\dagger X)}`$ is normalized Hilbert–Schmidt. It differs both from ordinary Hilbert–Schmidt norm and from trace norm. This distinction matters when applying Glebsky's theorem and converting likelihood error to density-operator trace error.

Project entropies use natural logarithms and information is in nats. A value in bits is obtained by dividing by $`\ln2`$. The project scores $`F_e`$ and $`F_{\mathrm{avg}}`$ are overlap fidelities; check any reference's squared or unsquared fidelity convention before substitution. A subscript $`N`$ counts pairs inside one anonymous batch, while a later $`m`$ counts independently tagged batches.

## One experiment, two different coarse-grainings

First the source removes correspondence before the learner acts:

```math
\Omega_N(T)=\frac1{N!}\sum_{\pi\in S_N}
(I\otimes P_\pi)\rho_T^{\otimes N}(I\otimes P_\pi^\dagger).
```

This channel preserves all physical specimens. Its missing classical record is the matching. It is not projection onto the symmetric subspace, and it supplies no coherent superposition or accessible purification of matchings. The [model](../science/model.md) fixes that access boundary.

The second coarse-graining is chosen by the learner. The separate-list receiver measures local joint spectral projectors $`P_i`$ on the input list and $`Q_j`$ on the output list. Reconstructing their normalized projectors gives

```math
E_N(X)=\sum_{i,j}
\frac{\mathrm{Tr}[(P_i\otimes Q_j)X]}{r_i s_j}
(P_i\otimes Q_j),\qquad
r_i=\mathrm{Tr}P_i,\quad s_j=\mathrm{Tr}Q_j.
```

This scalar conditional expectation is completely positive, trace preserving, unital and the orthogonal projection onto a product abelian algebra in $`L^2(\tau_N)`$. Ordinary block pinching can retain quantum information within degenerate blocks; the displayed map replaces each block by its scalar identity and corresponds to a fully classical record. The [worked examples](WORKED_EXAMPLES.md) make the distinction explicit.

The scientific question is whether the second coarse-graining loses any of the information surviving the first. Petz's sufficiency language makes the correct standard clear: one target-independent measurement and recovery sequence for the whole family, not a receiver chosen using the unknown parameter.

## The source-specific proof bridge

The following steps are established in this project's scientific account, with inherited tools attributed there.

1. **Compute the full operator kernel.** The [cycle proof](../science/correlation-kernel.md) reduces two hidden matchings to relative-permutation cycles. It yields an exact finite-batch overlap and, under a strict correlation contraction, the limit

   ```math
   \|L_N(T)\|_{2,\tau_N}^2\longrightarrow
   \det(I-TT^{\mathsf T})^{-1}.
   ```

2. **Retain the old information conclusion.** The [information proof](../science/information-ceiling.md) converts that bound to an all-measurement Holevo ceiling and a Pauli identification bound. The [paired learner](../science/paired-learning.md) and [prediction reduction](../science/prediction.md) provide the matched operational comparison. None of these upper bounds alone identifies an optimal restricted readout.

3. **Identify a possible complete limit.** Let $`P_T=\mathcal N(0,\Sigma_T)`$, with $`\Sigma_T=\begin{pmatrix}I&T\\T^{\mathsf T}&I\end{pmatrix}`$, and compare it with the independent standard Gaussian law $`\gamma`$. The Gaussian likelihood has the same squared $`L^2`$ norm as the limiting quantum likelihood. A direct local Fourier expansion gives both its characteristic function and the independent-reference Fourier Gram matrix.

4. **Exclude a hidden remainder.** Equality of the full likelihood norms, together with those pairings and density of finite Fourier sums, proves approximation of the entire quantum likelihood. Matching a covariance matrix or a few moments would not supply this step.

5. **Produce a physically restricted receiver.** Local Fourier unitaries asymptotically commute in normalized Hilbert–Schmidt norm. Glebsky's inherited Theorem 2 supplies exactly commuting approximants for each fixed finite frequency set, independently on each side. The scalar conditional expectation above fixes their algebra. Its best-approximation property converts the likelihood approximation into uniform trace-norm state recovery.

6. **Complete the Gaussian comparison.** A coupling of the reference spectral outcome law with the Gaussian Fourier coordinates gives target-independent Markov kernels in both directions. Uniform likelihood approximation controls their total-variation errors. A diagonal sequence of finite dictionaries makes all errors vanish. The full proof is [separate-list readout](../science/separate-list-readout.md).

This bridge uses an elementary bounded Fourier proof rather than promoting a generic local iid mean-shift theorem into an anonymous covariance theorem. The exact kernel, full-likelihood saturation and receiver are not claimed as results in Petz, and the Glebsky approximation theorem is credited as an external ingredient.

## Sufficiency has a scale and a resource price

The theorem fixes local dimensions and a compact physical family satisfying $`\sup_T\|T\|_{\mathrm{op}}\le r\lt1`$. It constructs one receiver sequence, independent of the target, with maximum reconstruction trace error $`\varepsilon_N\to0`$. Every bounded decision score and the bounded score of a consumable predictor are preserved asymptotically by channel contractivity.

The separate-list measurements retain all specimens in each list coherently until collective readout. They differ from the original pair-by-pair separable measurement class in Readout. The proof gives no efficient circuit, useful convergence rate or dimension-growing guarantee. For $`m`$ tagged batches of size $`b`$, direct product recovery has error at most $`m\varepsilon_b`$. A growing $`m(b)`$ therefore needs $`m(b)\varepsilon_b\to0`$. Neither this bounded-risk statement nor Gaussian covariance convergence proves convergence of Fisher information or of a risk multiplied by a diverging sample budget.

Use the [thirty milestones](MILESTONES.md) to reconstruct this sequence and the [examples](WORKED_EXAMPLES.md) to check its normalizations. The scientific pages remain canonical for claims and assumptions.
