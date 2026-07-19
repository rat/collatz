# E-057 — Continued fractions of log₂(3) and cycle exclusion

Related hypothesis: [`H-057-continued-fraction-cycle-exclusion.md`](../../hypotheses/H-057-continued-fraction-cycle-exclusion.md)

## Origin

Candidate #1 from the `BACKLOG.md` "not-yet-implemented candidates"
list (section 6): connecting the classical cycle-exclusion technique
(Steiner/Simons/de Weger/Hercher, via continued fractions of log₂(3))
with our own combinatorial wall (H-009/H-034).

## What was tested

1. **Continued fraction of log₂(3)** (45 terms) + full convergents +
   **semiconvergents** (necessary because this is a one-sided
   approximation problem — we need `S > a·log₂(3)` strictly, not just
   small `|S/a − log₂(3)|`; full convergents alone give a list that's
   too sparse, with huge jumps between `a=1,5,41,306,...`).
2. **Real self-consistency check** (reusing `compositions`/
   `candidate_n0`/`check_self_consistency` from E-034, without
   reimplementing) on the `(a,S)` candidates within our computational
   reach (`a=3,5,17`), at the exact `S` of the convergent/
   semiconvergent.
3. **Closed-form `n0_min`**: `(3^a−2^a)/(2^S−3^a)`, for the composition
   `(1,1,...,1,S-a+1)` — confirmed by exhaustive enumeration (a=3,5,17)
   as the one minimizing `n₀` among all compositions of `S` into `a`
   parts.
4. **Combinatorial cost** `C(S-1,a-1)` for candidates beyond our reach,
   up to and beyond the literature's current bound (`a=91`, Hercher
   2023, arXiv:2201.00406 — an update to "a≤68", which was outdated in
   our notes, verified via WebSearch/WebFetch before writing the code).

## Result

No new cycle. For `a=3,5,17`: stronger than "none self-consistent" —
**not a single composition produces even a positive integer `n₀`**
(fails the divisibility condition itself, for the 6 / 35 / 5,311,735
tested compositions). A subset of what H-034 already covered (same
`S`, within the `S_min..S_min+20` window), not an additional check.

For `a=29,41`: beyond our reach (`C(S-1,a-1)` ~10¹²/~10¹⁷), but already
excluded by Simons & de Weger (2005, `a≤68`). For `a=94` onward: open
territory (beyond Hercher 2023, `a≤91`) — not resolved by us nor, as far
as we've checked, by the literature.

## Interpretation correction (via `advisor()`, before finalizing)

The first version of this experiment claimed that **smaller excess
`L(a,S)=S−a·log₂(3)` implies a smaller possible `n₀`**, and so labeled
`a=29,41` as the "most dangerous" candidates. **Inverted**: for the
minimizing composition, `n0_min ≈ 1/(L·ln2)` — smaller excess implies
**larger** `n0_min`. Verified numerically (Part 2b of the script):
`n0_min` grows from 3.8 (`a=3`) to ~1069 (`a=1636`) as `L` shrinks. But
this is only the minimum over compositions — the `n₀` of a "bad"
composition (large valuations at the start) for the same pair
(a=306,S=485) reaches ~4.5×10²⁵, against `n0_min≈978`. Small `L(a,S)`
measures **analytic** exclusion difficulty (Baker bounds), not the size
of a potential cycle. See `H-057` for the full analysis of this
correction.

## How to reproduce

```
python3 experiment.py
```

No dependencies beyond `mpmath`. Runs in well under a minute (biggest
cost: the exhaustive check for `a=17`, ~13s for 5,311,735 compositions).
