# E-141: does the path-index average localize the same way the free-parameter average does? (H-162)

**Correction notice (2026-08-10):** the "residual mass" this
experiment measures a conductor profile of is the same quantity E-140
found to be an artifact of mass concentration within a full support
(participation-ratio effect, not sparse support: an earlier version of
this note called it a "sparse-support artifact", which E-140's own
correction history shows is wrong by five orders of magnitude), not
sibling-specific cancellation (see E-140's README and H-163's closure).
The REFUTATION
below (H-162's own question: does E-133's conductor localization
transfer to the path-index average?) survives that finding intact,
because it does not depend on the underlying sum being real
cancellation; but the earlier framing ("difference between the two
averages is itself part of the barrier's description") overclaimed a
mechanism that a control (below) shows is not sibling-specific either.
Both the original claim and the correction are kept on record.

H-159/E-133 prove that the diagonal coefficient `D(xi) = E[e(xi(X-Y))]`
of a sibling leaf pair, averaged over the **free arithmetic parameter**
`t`, cancels above conductor `3^(1+v3(k))` (`k = Delta/2`, the gap
between the two admissible first steps). H-162 asks whether the
**path-index average** at a single **fixed** `v` (no `t` to average
over) localizes at the same conductor.

Reuses E-140's `S_1(xi)`, `S_2(xi)` (real branch weights, fixed `v`,
full weighted enumeration of the sibling subtrees, vectorised with
per-level residue deduplication; the correctness check against slow
brute-force enumeration is copied from E-140 verbatim, not
re-derived) and adds a conductor breakdown: group `xi != 0` by
conductor `3^r` (`r = ell - v3(xi)`, the graduation of H-154/H-155/
E-133).

**The exact statistic** (described imprecisely in an earlier version of
this README): `per_r[r] = |sum_{xi: cond(xi)=3^r} S_1(xi) conj(S_2(xi))|`
-- the COMPLEX sum within each conductor class, magnitude taken after
summing (so cancellation within a class is already folded in), not
`sum_{xi: cond=3^r} |S_1(xi) S_2(xi)^*|` (sum of magnitudes). Re-running
with the sum-of-magnitudes version gives the same qualitative pattern
(checked, not persisted separately).

## How to run

```
python3 path_index_diagonal.py --roots 1 5 7 11 13 17 --depths 8 10 \
    --rank-pairs 1,2 2,3 1,3
python3 path_index_diagonal.py --roots 1 5 7 11 13 17 19 23 25 29 31 35 \
    --depths 8 --rank-pairs 1,2 2,3 1,3 --control    # persisted: run_ell8.txt
python3 path_index_diagonal.py --roots 1 5 7 11 13 17 \
    --depths 10 --rank-pairs 1,2 2,3 1,3 --control    # persisted: run_ell10.txt
```

`--rank-pairs i,j` selects the `i`-th and `j`-th smallest admissible
first-step exponents at `v` as the sibling pair, so gaps other than the
minimal `Delta=2` (`k=1`, predicted `r=1`) can be probed. The realized
`k` depends on the root, not just the rank pair: `(1,3)` gives `k=2` or
`k=3` depending on `v`, and `(2,3)` gives `k=1` or `k=2` depending on
`v` (an earlier version of this README claimed `(2,3)` always gives
`k=1`; false, checked against the persisted output).

`--control` adds, per row, the same conductor-fraction statistic with
sibling 2 replaced by a random-unit dilation of its own subtree (same
control that overturned E-140/H-163).

Cross-check: for `rank-pairs 1,2`, `|total|` reproduces E-140's
`measured_abs` exactly at the same `(v, depth)` (both scripts build the
identical `S_1`, `S_2`; verified by direct comparison before trusting
either).

## Result

`run_ell8.txt` (12 roots x 3 rank-pairs, `ell=8`, 36 rows) and
`run_ell10.txt` (6 roots x 3 rank-pairs, `ell=10`, 18 rows) are
persisted in this folder.

Real siblings: fraction at the conductor E-133 predicts averages
`0.1175` (stdev `0.0722`, n=36, `ell=8`); fraction **above** the
predicted conductor averages `0.8367` (stdev `0.0977`). Dilation
control (same 36 rows, sibling 2 replaced): fraction at predicted
conductor `0.1235` (stdev `0.0788`); fraction above `0.8235` (stdev
`0.1201`). **Statistically indistinguishable from the real siblings.**

**What survives**: E-133's conductor localization does not transfer to
the path-index average -- confirmed, and this conclusion does not
depend on whether the underlying sum is a real cancellation effect or
an artifact, since the control's profile is equally non-localized.

**What does not survive**: any claim that this non-localization is a
sibling-specific "broadband cancellation mechanism". The control shows
the same profile for an unrelated pair, so there is no mechanism here
to describe, sibling-specific or otherwise, at least not one this
statistic can see.

Not mirrored in `collatz-endogeny` (not yet cited by any paper text).
