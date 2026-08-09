# E-132: pair-decoupling exponent for consecutive units along the A-orbit

H-161 reduces the entire open band in direction (B) of the
beta_eff-vs-arc equivalence to one question: does the joint lower
tail of two consecutive units decouple relative to the marginal tail?
Precisely, with `N(u) := 3^ell * mu_ell(u)` and "next unit" meaning
the next unit in the A-orbit's contracted (units-only) sequence:

```text
P(N(k) <= x  AND  N(next unit) <= x) <= C * P(N <= x)^theta
```

If this holds with `theta > 1` down to `x ~ exp(-c0*ell)` for `c0`
large enough, a union bound over the `~3^ell` pairs gives the
unconditional result `beta_eff <= 1 + 1/(2*kappa) + o(1)` for
`kappa < theta/2 - 1/2` (derivation in H-161, independently
re-verified: the union bound forces no pair below
`x* ~ 3^(-ell/(2*kappa))`, and the exact recursive identity
`W(k) = N(k) + (1/4)*W(A(k))` then forces `min_k W >= x*/16`).

Run:

```sh
python3 pair_decoupling.py --levels 8 10 12 14 16 18 --eps 0.1
```

## Why a fixed threshold is the wrong test (again)

Comparing `pair(x)/d(x)^2` at a FIXED `x` across levels mixes the
correlation effect with the fact that `d(x)` itself changes with
`ell` at fixed `x` (the same trap already caught once in E-131 for
arc lengths). This script uses `x = exp(-eps*ell)`, which shrinks
with `ell`, so the comparison is between events of comparable rarity
at each level.

## Correction (Rule 11b escalation, 2026-08-09): the first version pooled two different marginals

The first version of this script computed `ratio = pair(x)/d(x)^2`
against a single pooled marginal `d(x)`. This is wrong: F1 (H-161)
shows the two positions of every consecutive-unit pair sit at
different phases mod 3 with genuinely different distributions
(`N = (3/2)*W` at phase 2, `N = (3/4)*W` at phase 1), and the
contracted unit sequence strictly alternates phase 1, 2, 1, 2, ...
Comparing the joint tail against a pooled marginal squared is not the
correct independence baseline: by AM-GM, `d1*d2 <= ((d1+d2)/2)^2` for
any `d1 != d2`, so pooling mechanically pushes the "independence"
denominator up and the apparent ratio down, inflating the appearance
of anti-clustering. This is the same failure shape as two earlier bugs
in this session (fixed-threshold comparison in an earlier draft of
this script's own trap, and the non-unit inflation bug in E-131's
`deficient_arc_scan.py`): a statistic pooled over a population with
real internal structure.

Caught via a second Rule 11b escalation before the numbers below were
trusted. The fix: compute `d1(x)` and `d2(x)` for each phase
separately, verify the free identity `d1(x) = d2(2*x)` (forced by F1)
as a bookkeeping check, and compare `pair(x)` against the correct
product baseline `E[d(phase_a)*d(phase_b)]`.

## Result (corrected)

At `eps=0.1`, `ell=8..18`, pooled over both pair types:

```text
ell   ratio=pair(x)/(d1*d2)   implied theta (if pair ~ d1^theta)
 8         0.379                    3.05
10         0.237                    3.32
12         0.100                    3.81
14         0.024                    4.56
16         0.0015                   5.91
18       ~0.00000                   8.80    <- 2 hits total, see below: not a measurement
```

The `d1(x) = d2(2x)` bookkeeping check passes exactly (to the printed
precision) at every level, confirming the phase algebra. The corrected
ratio is close to the pooled version's numbers and falls slightly
*faster*, not slower: fixing the marginal-mismatch artifact did not
explain away the signal, contrary to the natural expectation that a
pooling bug this shape usually inflates an effect. The anti-clustering
finding survives the correction.

Split by pair type (`(1,2)`: `k==1 mod 3` stepping via `A`; `(2,1)`:
`k==2 mod 3` stepping via `A^2`, skipping the non-unit), both compared
against the same product baseline `d1*d2`:

```text
ell   ratio (1,2)   hits (1,2)   ratio (2,1)   hits (2,1)
 8       0.423          72           0.335          57
10       0.268         275           0.205         210
12       0.100         588           0.101         596
14       0.020         619           0.028         861
16       0.0008        104           0.0023        310
18        0             0           ~0              2
```

Both types show the same qualitative pattern (falling ratio, no sign
of leveling off) at comparable magnitude and with comparable hit
counts through `ell=16`, so the pooled result up to there is not an
artifact of one type dominating the other. **`ell=18` does not extend
this**: total hits collapse to 2 (both in type `(2,1)`, none in type
`(1,2)`), out of roughly 86 million candidate pairs. A ratio computed
from 2 hits is not a measurement of anything, it is what a single
observed pair looks like once expressed as a fraction. The pooled
`ell=18` row (`pair(x)=7.74e-9`, implied `theta=8.8`) reported by the
main table above must be read the same way: consistent with the
trend continuing, but supplying no actual evidence for it. Pushing
`eps=0.1` further in `ell` runs out of usable signal before it
confirms or refutes anything.

## What this does not show

Five points at `ell<=16` cannot distinguish "a genuinely growing
exponent" from "approaching some larger fixed exponent slowly" from
"a finite-range effect that will not persist." This is evidence, not
a proof of any rate, and the theorem in H-161 needs the bound to hold
uniformly down to `x ~ exp(-c0*ell)` for a FIXED `c0` with
`c0 >= log(3)/(2*kappa)`. At `eps=0.1`, `d1(x)` ranges from about 0.40
(`ell=8`) to 0.19 (`ell=16`): this probes the bulk of the tail, not a
deep tail, so a growing `theta` measured only here does not by itself
establish the uniform bound the theorem needs. Pushing `eps` much
higher runs into the same wall as E-131's arc scan: by `ell~14` the
threshold falls below the smallest observed `N` value and the
statistic loses all hits (see E-131's README, `eps=0.2` column). This
is still the strongest quantitative signal so far in this line of
investigation, and worth extending (more levels, an explicit rate fit,
the Weyl-sum induction program sketched in H-161) before attempting to
turn it into a proof.
