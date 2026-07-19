# E-015 — Systematic search for coalescences mod 2^d

Related hypothesis: [`H-015-systematic-coalescence-search.md`](../../hypotheses/H-015-systematic-coalescence-search.md)

## What was tested

Direct generalization of the H-014 technique: for each residue class
N≡r₁ (mod 2^d), search for M=N−k (same free "K", small k) whose
symbolic orbit collides exactly with N's, excluding N as a record
holder. Search for d=2 through 16, k=1 through 40, with
deduplication (a class only counts as "new" if it isn't a refinement
of an already-found smaller-modulus exclusion).

## Result — quantitative

**2,374 genuinely new residue classes found** (beyond H-014).
Cumulative fraction of excluded residues by modulus:

| d (mod 2^d) | excluded | fraction |
|---|---|---|
| 3 | 1/8 | 12.5% |
| 6 | 26/64 | 40.6% |
| 9 | 276/512 | 53.9% |
| 12 | 2532/4096 | 61.8% |
| 16 | 45430/65536 | **69.3%** |

The fraction grows rapidly and keeps rising with larger d (not an
exhaustive search — stopped at d=16 for time scope, not a theoretical
limit).

## Critical verification (pitfall found and resolved)

The first attempt to verify the findings against real orbits at K=0
**failed** for every tested case — investigating, I found it's a
boundary effect: for K too small, the actual value N=2^d·K+r is too
small and the trajectory "collapses" (reaches 1 or a small value)
before the assumed symbolic prefix completes. Testing with K≥10,
**every verified case matched exactly** (stopping-time difference =
predicted, no exceptions).

This directly parallels N=2 in H-007 (where the dominating M collapses
to 1 — the same kind of small-number exception).

## Verification against the 148 official record holders

6 record holders "violate" some excluded class: **3, 6, 7, 9, 18,
25** — all among the first 8 record holders in the official list (very
small numbers). No larger record holder (from 27 onward) violates any
found exclusion. This is exactly the expected boundary effect — the
technique is valid for N sufficiently large within each class; the
small record holders are known exceptions, analogous to H-007's N=2.

## Important limitation (by construction, not for lack of effort)

This search is restricted to modulus 2^d. Since 2^d and 9 are coprime,
**no restriction mod 2^d can say anything about the residue mod 9**
(via the Chinese Remainder Theorem) — so this technique **cannot, by
construction, solve H-008** (the absence of class 4 mod 9). This isn't
a failure of the search, it's a clear structural limitation, documented
so as not to waste time trying this same technique on H-008 in the
future — it would need a separate mod-3^b technique (e.g. a
generalization of H-005 to mod 9).

Reproduce: `python3 experiment.py 16 40` (~6s).

## Status of H-015

**Confirmed as a general, valid technique** (with the caveat of N being
large enough). Does not solve H-008. The quantitative result (69% of
residues mod 2^16 excluded) is, on its own, an interesting finding
about how structurally "rare" it is to survive as a record-holder
candidate.
