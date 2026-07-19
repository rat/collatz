# E-045 — Verification of paper #011 (Abdullah Mohammed) — full-proof claim

## Goal

Verify "Structural Analysis, Dynamic Density Sieve, and Logarithmic
Contraction of Collatz Sequences" (Abdullah Mohammed, Kafr El-Sheikh
University, Egypt) — claims a complete proof of the Collatz Conjecture
via a geometric density sieve + Baker's theorem (linear forms in
logarithms).

## Result

**Sections 2-5 are correct** (but not new): geometric sieve
P(M=m)=1/2^m, E[M]=2 (our own H-001/H-011), elementary exclusion of
1-cycles (n=1/(2^m-3), the only positive solution is m=2,n=1), the
"special numbers" sequence 1,5,21,85,341,... (OEIS A002450, numbers
that reach 1 in one step).

**Decisive hole in Section 7.1 (Eq.48)**: to use Baker's theorem to
exclude non-trivial cycles, one must compare Baker's lower bound
against the value of M/P that a REAL cycle would force. Section 6 of
the paper itself derives the cycle equation 2^M=∏(3+1/n_i), which
forces M/P → log₂(3)≈1.585 for large elements (proven here
elementarily: for any P≥2, 3^P < ∏(3+1/n_i) < 4^P, so M∈(P·log₂3, 2P)
strictly — never equal to 2P). But Eq.48 substitutes M≈2P — the
ERGODIC/AVERAGE expectation E[M]=2 from Section 3, which describes the
TYPICAL/RANDOM odd number, not the constraint a specific
self-consistent cycle would need to satisfy. This wrong substitution
produces Λ≈0.288·P (grows linearly, confirmed to match the paper's
number exactly), which trivially satisfies Baker's weak bound — the
"check" restricts nothing. The comparison that would actually matter
(Λ→0 as M/P→log₂3) is exactly where the genuine difficulty would lie.

This is the same method genuinely used by Simons & de Weger (2005) with
explicit Baker constants to exclude cycles up to certain lengths — but
not "all cycles" in general, because it doesn't close for arbitrarily
large P with the known effective constants. Mohammed's paper doesn't
even reach that level (doesn't compute C, κ explicitly) and still uses
the wrong substitution.

See `hypotheses/H-045-mohammed-density-sieve-baker-flaw.md`.

## How to run

```
/home/rat/.venv/bin/python3 experiment.py
```
