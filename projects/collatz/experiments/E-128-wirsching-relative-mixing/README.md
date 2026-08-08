# E-128: Wirsching relative mixing

Related hypothesis: H-160.

The script uses the exact integer multiplicities from E-115 and compares
each fixed-cost row with Haar measure on the unit residues.  It reports:

- support fraction;
- minimum and maximum pointwise density ratios;
- the supremum relative defect;
- total variation and normalized collision;
- the two masses modulo `3` and their coarse total variation from Haar;
- density-ratio quantiles.

Run:

```sh
python3 relative_mixing.py --max-level 12 --offsets -1 0 1
```

The bounded-composition total is independently checked at every level.
Finite zeros do not refute asymptotic relative mixing, but they show
that the required uniform estimate has not entered its positive regime
on the tested range.

The mod-`3` diagnostic tests the analytic obstruction recorded in H-160:
at cost `k/ell -> lambda`, the newest increment has asymptotic geometric
tilt `z=lambda/(1+lambda)`, forcing limiting class masses
`1/(1+z)` and `z/(1+z)` instead of `1/2,1/2`.
