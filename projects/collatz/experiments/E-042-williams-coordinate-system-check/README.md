# E-042 — Verification of paper #014 (Williams, "A Coordinate System for Collatz Dynamics")

Related hypothesis: [`H-042-williams-coordinate-system-review.md`](../../hypotheses/H-042-williams-coordinate-system-review.md)

## What was tested

A paper of good academic quality (real institutional affiliation,
extensive literature, honest AI-use disclosure, public code on GitHub).
Eight checks in total (2 original from 2026-07-14 + 6 added on
2026-07-15, upon realizing — late — that this item had already been
reviewed here):

- **Theorem 3.6** (diagonal dynamics) — 20,000 random cases.
- **Theorem 4.1** (Zero-Prime Rows) — exhaustive k=6,10,...,300 (74
  rows). Exception k=2 confirmed. Off-pattern controls have primes.
- **Theorem 2.13** (bijective partition Z≥0→crown triangles) —
  n=0..200,000.
- **Proposition 3.10** (boundary transition a=1) — 81 cases.
- **Theorem 4.2** (count of "prime-admissible" positions) — k=2..300.
- **Proposition 6.2** (asymptotic chain-count formula).
- **Observation 6.3** ("accidentally" prime-free rows) — exact lists.
- **OEIS references** (Section 5.2) — checked via `curl` on oeis.org.

## Result

**Every theorem confirmed without exception.** Two OEIS citation errors
in Section 5.2 (don't affect any proof): `A017557` cited for "crowns≡8
mod12" is actually `12n+3` (≡3 mod12) — the correct sequence is
`A017617` (`12n+8`); and "primes in `L_1`=A005105" should be "A005105
minus the element 2" (a single-element difference).

## Integrity note — our own error caught and fixed before finishing

A first attempt to verify Proposition 6.2 (incorrectly) flagged a
"factor-2 error", using `T_c(k,0)` as row `k`'s minimum element. This
was **wrong — a bug in the verification, not the paper**: the real
minimum is at `T_c(k,1)` (odd position), confirmed against the paper's
own Example 2.9. `advisor()` flagged the inconsistency before any
wrong conclusion was written. See `H-042.md` for the recorded lesson on
suspicion order when investigating discrepancies.

## Reproduce

`python3 experiment.py` (~1.4s)

## Status

Review complete — no mathematical error found (only two isolated OEIS
citation errors, not affecting any proof). An important calibration
point for the cumulative critique (not every paper in the collection
has problems).
