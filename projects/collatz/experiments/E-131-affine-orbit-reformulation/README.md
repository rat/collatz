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

## `max_mass_growth.py`: how large can a single point mass get?

The direction of the reformulation that would let a long deficient arc
*refute* `beta_eff -> 1` needs a bound on the maximum point mass
`M_ell = max_u mu_ell(u)` (equivalently `N_max = 3^ell M_ell`), to
control the part of the window sum beyond an observed short arc. A
one-line induction on the recursion gives `M_ell <= (2/3) M_(ell-1)`
(only half the terms contribute, by parity, each at most
`M_(ell-1)`), hence `M_ell <= (2/3)^ell`, i.e. `N_max <= 2^ell`
always — proved and checked by assertion in this script. The *actual*
growth is tighter: the ratio `N_max(ell)/N_max(ell-1)` converges to
exactly `1.5` by `ell~10`, i.e. `N_max ~ C*(3/2)^ell`, better than the
proved bound but still exponential, not bounded. This is why the
"long arc implies beta doesn't -> 1" direction does not close for the
arc lengths actually observed (see H-161 and `deficient_arc_scan.py`
below): even the sharper empirical rate requires arcs of length
`~0.29*ell` to make the tail negligible, and the observed arcs (3-5)
fall below that threshold from `ell~14` onward.

Run:

```sh
python3 max_mass_growth.py --max-level 16
```

## `deficient_arc_scan.py`: does the deficiency cluster along the orbit?

From the identity above, ONE direction of the natural reformulation is
elementary and proved with no extra hypothesis: if no arc of length
`Theta(ell)` exists in `{N_ell <= exp(-eps*ell)}` for any `eps>0`, then
`beta_eff(ell) -> 1` (take the contrapositive: if `beta_eff` does not
tend to 1, the argmin's window sum has a term-by-term bound that
directly produces such an arc). The converse ("`beta_eff->1` implies no
long arc") is NOT established by this argument alone; it needs the
`N_max` bound above to control the window sum beyond a short arc, and
neither the proved `2^ell` bound nor the sharper empirical `(3/2)^ell`
rate closes it at the arc lengths actually observed. So this
reformulation is currently a proved sufficient condition, not a proved
equivalence — see H-161 for the full derivation and where exactly it
does and does not close.

The proved direction is still the one that matters for interpreting
this measurement: for every `eps>0`, does the longest run of
consecutive positions along the `A`-orbit with normalized mass
`N_ell(u) = 3^ell mu_ell(u) <= exp(-eps*ell)` grow, stay bounded, or
shrink?

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
python3 deficient_arc_scan.py --min-level 8 --max-level 19 --eps-list 0.1 0.2
```

Expected result: at `eps=0.1`, the observed longest run (5,5,5,5,5,5,
4,4,4,4,3,2 for `ell=8..19`) stays below the random-arrangement
baseline throughout, and decreases over the tested range while the
baseline rises then plateaus (6.89 to 8.13 to 7.71). At `eps=0.2`, the
observed run is 2 wherever the threshold is met at all, again at or
below baseline (baseline falls toward 0 as the fraction below
threshold collapses to zero by `ell=16`). This is evidence of
anti-clustering (not merely absence of clustering) of the deficient
positions along the `A`-orbit, but the tested range (`ell=8` to `19`,
12 points) is far too short to extrapolate an asymptotic conclusion,
and even a confirmed asymptotic trend would only feed the proved
direction above (shrinking arcs support `beta_eff->1`), not prove it
outright. `ell=20` was not reached: the full-array method here needs
close to 90GB at that level, near this machine's safe ceiling; going
further needs an implementation that does not materialize the whole
`3^ell`-length law. See H-161.

## Cross-check

`min_N` in `deficient_arc_scan.py`'s output equals `3^ell * c_ell`
computed by the (already independently verified) direct method in
E-127/E-130: e.g. `ell=12`: `0.0529150`; `ell=18` (with `--max-level
18`): `0.0404242`. This confirms the fast binary-doubling evaluation
used here (`circ_geom_half`, needed to reach higher levels than the
direct `O(period)` method comfortably affords) computes the same
`mu_ell` as the reference recursion.
