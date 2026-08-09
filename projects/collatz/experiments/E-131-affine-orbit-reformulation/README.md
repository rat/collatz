# E-131: affine-orbit reformulation of the worst-cylinder recursion (H-158 step 4 / H-161)

H-158's step 4 asks for a recursive subexponential inequality for
`c_ell = min` over units of the Syracuse law `mu_ell`. This experiment
verifies an exact structural identity found while attempting that step
(via an external consultation, Rule 11b, independently re-verified
before being trusted, Rule 8c), and tests the empirical question it
raises.

## `fact_a_check.py`: the exact orbit identity

The verified memoryless recursion is `mu_ell(y) = 1/2 nu(2y) + 1/2
mu_ell(2y)` (forward, increasing powers of 2 — an earlier attempt at
this identity used the wrong, decreasing-power direction and failed
numerically; this is the corrected, verified form). Unrolling gives a
sum over `t` with `2^t y == 1 (mod 3)` (where `nu` is supported), which
share a fixed parity `t0(y) in {1,2}`. The step `t -> t+2` sends
`z=2^t y` to `4z`; writing `z=1+3k` turns this into the affine map

```text
A(k) = 4k+1 (mod 3^(ell-1))
```

which is a single cycle of length `3^(ell-1)` covering all of
`Z/3^(ell-1)Z` (4 has order exactly `3^(ell-1)` mod `3^ell`). This
gives the exact identity

```text
mu_ell(y) = 2^-t0(y) * sum_j 4^-j * mu_(ell-1)(A^j(k0(y)))
c_ell = (1/4) * min_k G(k),   G(k) = sum_j 4^-j mu_(ell-1)(A^j(k))
```

Run:

```sh
python3 fact_a_check.py --max-level 8
```

Expected result: exact match (relative difference at machine precision)
between the direct recursion (E-111's `weighted_bridge.py`) and the
orbit-formula reconstruction, at every level and every sampled residue.

## `deficient_arc_scan.py`: does the deficiency cluster along the orbit?

From the identity above, `beta_eff(ell) -> 1` is equivalent (elementary
consequence of the identity, not independently re-derived line by line
here) to: for every `eps>0`, the longest run of consecutive positions
along the `A`-orbit with normalized mass `N_ell(u) = 3^ell mu_ell(u) <=
exp(-eps*ell)` has length `o(ell)`.

Testing this needs a threshold that shrinks with `ell`. A first attempt
used FIXED thresholds (0.2, 0.3, 0.5) and found the longest run growing
with `ell` — but this does not test the claim: at a fixed threshold,
the fraction of positions below it grows with `ell` on its own, so an
i.i.d. random arrangement of the same per-level frequencies would show
a growing longest run purely from more trials, with no clustering
signal at all. This script uses the threshold the claim actually needs
(`exp(-eps*ell)`) and reports the observed longest run against the
random-arrangement baseline `log(N)/log(1/p)` (`N` = number of unit
positions, `p` = the level's own observed fraction below threshold).

Run:

```sh
python3 deficient_arc_scan.py --min-level 8 --max-level 18 --eps-list 0.1 0.2
```

Expected result: at `eps=0.1`, the observed longest run (5,5,5,5,5,5,
4,4,4,4,3 for `ell=8..18`) stays below the random-arrangement baseline
throughout, and decreases over the tested range while the baseline
rises then plateaus (6.89 to 8.13 to 7.87). At `eps=0.2`, the observed
run is 2 wherever the threshold is met at all, again at or below
baseline (baseline falls toward 0 as the fraction below threshold
collapses to zero by `ell=16`). This is evidence of anti-clustering
(not merely absence of clustering) of the deficient positions along
the `A`-orbit, but the tested range (`ell=8` to `18`, 11 points) is far
too short to extrapolate an asymptotic conclusion. See H-161.

## Cross-check

`min_N` in `deficient_arc_scan.py`'s output equals `3^ell * c_ell`
computed by the (already independently verified) direct method in
E-127/E-130: e.g. `ell=12`: `0.0529150`; `ell=18` (with `--max-level
18`): `0.0404242`. This confirms the fast binary-doubling evaluation
used here (`circ_geom_half`, needed to reach higher levels than the
direct `O(period)` method comfortably affords) computes the same
`mu_ell` as the reference recursion.
