# E-105 — Spectral gap of the dual transfer operator (H-129)

Related hypothesis: [`H-129-q-adic-pole-analog-seymour.md`](../../hypotheses/H-129-q-adic-pole-analog-seymour.md)
See also: [`H-109-...md`](../../hypotheses/H-109-generalized-qx1-pressure-equation-exact-closed-form.md),
[`E-103-tail-index-q5-rigorous-test`](../E-103-tail-index-q5-rigorous-test/README.md)
(corrected by this experiment).

## What motivated this

The project's notes (H-109, E-103, H-129) attributed the slow
convergence transient k^-0.222 observed in the q=5 tail-index test to
"a subdominant complex root of the transfer operator". While resuming
H-129 ("Perron-Frobenius spectral analysis" was the next step listed
in H-129/E-104), I noticed a real tension before writing any code:
**oscillatory geometric** decay (the signature of an isolated
subdominant eigenvalue) and **power-law** decay k^-0.222 (the classic
signature of the ABSENCE of a spectral gap) are mathematically
incompatible categories at the same layer.

## Consulting the Fable

I consulted the Fable (full context: the fiber-bijection lemma, the
already-proven impossibility of a finite state — Example
ex:naive-fails —, the annealed pressure identity, the quenched/annealed
dichotomy). Summarized response (see H-129 for the full text):

1. The right operator is the **dual** M_α (parent→child, via
   φ_a(w)=(qw+1)·2^-a), not the Koopman L_α (child→parent, which is
   what Fact 2/Example ex:naive-fails forbids as a finite state). M_α
   PRESERVES locally constant functions mod q^K exactly.
2. M_α has a **perfect, structural spectral gap**: uniform q-adic
   expansion by an exact factor q, zero distortion — the spectrum of
   M_α restricted to any level K is EXACTLY {Λ,0} (Λ=q^α/(2^α−1)), with
   no isolated subdominant eigenvalue. Manneville-Pomeau/Sarig-Iommi
   (which would require the absence of a gap) doesn't apply.
3. The k^-0.222 belongs to a different, NONLINEAR layer: the moment
   test at α near the tail index sits at the boundary case of branching
   random walk (α_+ is always frozen, already proven) — polynomial
   corrections in k (Bramson, Aïdékon) are expected there, without
   contradicting the linear layer's gap. Suspicion: a log-periodic
   lattice effect (weights are powers of 2).
4. A pitfall identified preemptively: a naive Ulam-type test (looking
   at the truncated L_α spectrum, or expecting a "subdominant
   eigenvalue converging" as K grows) would produce a guaranteed
   numerical artifact, due to non-normality of the nilpotent block —
   not a real signal of "the gap closing".

## Numerical verification (`experiment_gap_check.py`)

Exact construction (exact modular arithmetic for the indices; floating
point only for the weights/eigenvalues) of the q^K×q^K matrix of M_α,
for q=5, α_+=1 (frozen) and α_-=0.650919 (non-frozen), K=2,3,4.

**Result — confirms the Fable's prediction at every point**:

- The row sums of M_α = the theoretical Λ exactly (matches to 8+
  digits), in every row and every K — confirms M_α·1=Λ·1.
- The dominant eigenvalue = Λ, in every case.
- All other eigenvalues ≈0: 2.3e-8 (K=2) → 9.3e-6 (K=3) → 2.0e-4 (K=4).
  The growth with K is exactly the non-normality noise predicted by the
  Fable (growing nilpotent block) — **not** a real eigenvalue
  approaching Λ. I did not interpret this as "the gap closing" because
  I was warned about the artifact before running it.

## Conclusion

Spectrum {Λ,0} confirmed both structurally and numerically — a perfect
spectral gap at the linear layer. The "Perron-Frobenius spectral
analysis" route listed in H-129/E-104 as a next step is **closed**: the
answer is definitive, and doesn't resolve the Tail-Index Conjecture
(which lives in the nonlinear critical layer, not the linear one). We
corrected the "subdominant complex root" terminology in H-109 and
E-103/README.md — it doesn't hold up under the correct formalization of
the operator.

## Next steps (if the line is resumed)

~~Directly test the log-periodic hypothesis for the tail~~ — **done and
not supported, E-103 Stage 2 (2026-07-19)**: a Fable consultation
derived that the system is non-arithmetic (log₂5 irrational destroys
the periodicity, Goldie's dichotomy) — no asymptotic log-periodicity
expected. A pre-registered test at the two derived periods confirmed:
periodogram power at the noise level across all 4 tested headrooms.
See `experiments/E-103-tail-index-q5-rigorous-test/README.md`, the
"Stage 2" section.

This does NOT close the origin of the k^-0.222 — it only refutes one
more candidate explanation (the first was the spectral gap, here). The
real item that remains is testing the transient on the axis where it
was observed (M_k(p) vs. k, not W_v's tail in x) — see E-103's next
steps, item 5.

## Files

- `experiment_gap_check.py` — construction and numerical verification
  of M_α.

## Reproduce

```
python3 experiment_gap_check.py    # seconds, no dependencies beyond numpy
```
