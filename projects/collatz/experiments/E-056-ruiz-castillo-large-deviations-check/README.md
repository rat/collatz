# E-056 — Verification of paper #026 (Ruiz Castillo, "Residual Large Deviations")

Related hypothesis: `H-056`.

## Paper

Ruiz Castillo, J.C. (2026). *Grandes Desviaciones Residuales de Ruiz
Castillo en la dinámica acelerada de la Conjetura de Collatz*. Zenodo,
DOI [10.5281/zenodo.20767811](https://zenodo.org/records/20767811), 44
pages. The seventh paper by this author reviewed in this collection
(after item 001/H-039, 008/H-050, 010/H-052, 013/H-053, 017/H-054,
020/H-055).

Local PDF: `literature/papers/026_Grandes-Desviaciones-Residuales-Ruiz-Castillo.pdf`
(md5:f12d30c3d0e052854f6da782f0af7bab, matches the md5 listed on the
Zenodo page). The original collection link (item 026 of
`literature/papers/INDEX.md`) points to ResearchGate, which blocks
automated download — the same paper is mirrored on Zenodo (open, no
blocking) under the DOI above; we used that route.

## What was tested

**Part 1 — algebraic identities (Sections 1-2), against REAL Collatz
orbits** (not the abstract i.i.d. model): Proposition 1.2
(multiplicative interpretation of residual debt), Proposition 2.3
(residual-dissipative equivalence), Corollary 2.4 (critical event
x=0), Proposition 2.5 (event monotonicity, the "finite k" analogue of
Proposition 3.4 that enters the central finding). 24 values of n (9
fixed + 15 random odd numbers up to 10⁶) × 6 values of k × (up to 8
values of x or 5 pairs) = 2160 total cases.

**Part 2 — ideal probabilistic model** (a_j iid Geometric(1/2), the
same model as H-001/H-011): Proposition 4.4 (E[a]=2), Theorem 4.7
(negative residual drift, log₂3−2), Theorem 5.2 (Chernoff bound
P(L_k≥0)≤e^{-ck}) — all verified by computing the MGF/Ψ(t) in closed
form and comparing against the paper's own proof.

**Central finding — a real internal inconsistency** (not an isolated
calculation error): Definition 3.1 defines I_RC(x) via the
**one-sided** tail event {L_k/k≥x}. Proposition 3.4 (p. 19, **already
proven**) correctly shows this I_RC is non-decreasing — but this
conclusion is *conditional* on the existence of the limit defining
I_RC at each point. Figure 1 (p. 33, Section 6, "conceptual") and
Conjecture 7.3 (p. 36, property 2: "existe un único punto x* tal que
I_RC(x*)=0") describe I_RC as a **two-sided** function over V/U,
positive on both sides of x*=log₂3−2. Conjecture 7.5 (p. 38, checked
directly against the PDF) formalizes this same two-sided reading:
I_RC(x)=sup_{t∈ℝ}{tx−Λ(t)}, an **unrestricted** sup — i.e., Figure 1,
Conjecture 7.3, and Conjecture 7.5 are mutually consistent with each
other, and it's this trio that contradicts Proposition 3.4: a
non-decreasing function with a zero at x* must necessarily be zero at
EVERY x≤x*, not just at a single point.

We confirmed in three independent ways that I_RC(x)=0 (not positive)
for x<x*, and hence that **the limit defining I_RC does in fact exist
in this regime** (the condition Proposition 3.4 depends on — without
this check, the finding would be "a false conjecture" rather than "a
conjecture provably incompatible with a proposition already proven in
the same paper"):

1. **Analytically**: `I_RC_restricted(x)` = sup_{t≥0}{tx−Λ(t)} — the
   standard sign restriction from large-deviations theory for one-sided
   events (Dembo-Zeitouni, ch. 2), the same restriction used implicitly
   (only for x=0) in the already-proven proof of Theorem 5.2. Gives
   exactly 0 for x<x*, coinciding with `J_unrestricted(x)` (the
   two-sided Legendre-Fenchel, unrestricted — Conjecture 7.5 as
   literally written) only for x≥x*.
2. **Monte Carlo**: for x=−0.6 (<x*≈−0.415), simulating sums of k iid
   Geometric(1/2)'s, P(L_k/k≥x) **rises** from 0.667 (k=10) to 0.99996
   (k=1000) — the event becomes LESS rare, not more.
3. **Exact for small k**: closed-form Negative Binomial distribution via
   `Fraction` (no floating point near the threshold), same increasing
   pattern (k=5→40: 0.623→0.804).

## How to reproduce

```
python3 experiment.py
```

No dependencies beyond `numpy` (used only for the vectorized Monte
Carlo simulation). Runs in a few seconds.

## Integrity note (see H-056 for details)

1. **Verified directly against the original PDF**: an earlier draft of
   this same analysis characterized Conjecture 7.5 as already having
   the correct sign restriction (t≥0) — treating it as "the correction
   the paper itself offers" for Conjecture 7.3. This was **wrong**: we
   checked p. 38 directly and Conjecture 7.5, as written, is
   unrestricted (sup_{t∈ℝ}). Fixed in `experiment.py` before
   finalizing. The central finding doesn't change — only the
   attribution of which conjecture has which formula.
2. **Reported, not re-verified in detail**: also in this session, an
   earlier stage of the same work reported a tuple-unpacking order bug
   in the verification code, identified and fixed before any number was
   reported. We don't have the file's git history (not yet committed)
   nor the exact form of the bug to reconstruct it with certainty — we
   report the fact that it was caught and fixed in-session, without
   inventing the specific diff.

## Result

Supports H-056: Sections 1-5 of the paper (concrete identities,
negative drift, Chernoff bound) are entirely correct. The real error is
contained in Section 7 (entirely conjectural, never labeled
"Theorem"/"Proposition"), which contradicts Proposition 3.4 (Section 3,
already proven). Not a claim of proving Collatz — the paper explicitly
denies this ("El marco desarrollado no demuestra la Conjetura de
Collatz", p. 41) — nor an isolated calculation error. It's a
global-structure conjecture (a two-sided rate function over V)
inconsistent with a local proposition already proven in the same text,
by conflating the classical (two-sided) Cramér rate function with the
real rate function of the one-sided tail event that Definition 3.1
actually defines.
