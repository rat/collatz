# E-130: cost-band decomposition of the worst Syracuse cylinder (H-158 step 3)

H-158 asks whether the worst-cylinder mass `c_ell` decays fast enough
for `beta_eff(ell) -> 1`. Its third listed next step is to separate
the contribution to `c_ell` by microcanonical cost band, without
running the exponential min-cost DP (E-111's `reachable_w`), which is
exactly what becomes infeasible at the levels where this matters.

The Tao memoryless recursion, unrolled to a geometric tail, already
supplies a usable cost coordinate for free:

```text
mu_ell(y) = sum_{s=0}^{tail-1} 2^-(s+1) * nu(2^-(s+1) y mod 3^ell)
```

Term `s` is the contribution from paths taking exactly `s+1` extra
doubling steps before landing in the previous level's law `nu`. This
script re-derives, at each level, the per-term breakdown for three
residues: the minimum-mass residue (E-127's `c_ell`), the maximum-mass
residue, and a residue of median mass, and reports the smallest number
of leading terms whose cumulative sum reaches 50%/90%/99% of each
residue's total mass.

Run:

```sh
python3 decompose_worst_cylinder.py --max-level 15
```

## Why a raw cumulative-fraction count would be meaningless alone

The `2^-(s+1)` prefactor decays geometrically for every residue, not
just the worst one. Any residue's cumulative sum saturates within a
handful of terms just from that prefactor. Reporting the min residue's
saturation point by itself would show nothing about the min residue
specifically. The comparison against the max- and median-mass residues
at the same level is what carries the information.

## Result

The three residues behave differently, and the difference is stable
across all 15 levels tested:

- The **maximum**-mass residue is essentially a single term: for
  `ell>=5` the `s=0` term alone already exceeds 99% of its total mass.
  It is reached almost entirely by the cheapest possible path.
- The **median**-mass residue needs a handful of terms, `s` up to about
  1-6 for 90%, up to about 4-7 for 99%.
- The **minimum**-mass residue (`c_ell`) consistently needs more:
  `s` up to 5 for 90%, up to 9-11 for 99%, at every level from 2
  through 15.

None of the three thresholds shows a trend with `ell` over the range
tested (the min row's `s99` moves between 9 and 11, which reads as
noise at this range rather than growth). The worst residue's deficit
is not explained by any single cheap path contributing an outsized
share, the way the best residue's surplus is; it draws comparable
amounts from several cost bands. This is descriptive finite-level
evidence, not an asymptotic claim, and it does not by itself resolve
H-158's target.

## What this does not show

This does not identify a recursive inequality for `c_ell` (H-158's
step 4, still open), and it does not connect to the min-cost DP's own
cost variable (`a_1+...+a_n` in E-111's `reachable_w`), which is a
different, more expensive coordinate that this script deliberately
avoids computing. The `s` coordinate here is specific to the geometric
unrolling of the memoryless recursion, not the WCC's representation
cost.
