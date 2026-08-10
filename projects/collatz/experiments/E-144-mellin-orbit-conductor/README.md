# E-144: Mellin/orbit-time transform of N_ell, by orbit conductor (H-175)

H-175's "tentativa 2" established that the Mellin/orbit-time transform
of `N_ell` (the object H-161's Weyl section actually uses) is
structurally different from the additive Fourier transform E-137
measures. This experiment takes the next step: decompose the Mellin
spectrum by orbit conductor `3^r` (`r := (ell-1) - v3(m)`, the exact
analogue in orbit-time space of the conductor graduation
H-154/H-155/E-137 use in additive space).

## How to run

```
python3 mellin_orbit_conductor.py
```

## Result

Persisted output in `run_output.txt`, `ell=6` to `12`. Self-consistency
check (sum of per-conductor energies against the total) passes at
`0.00e+00` relative error at every level.

**Energy per conductor class is nearly constant across `r`**, despite
the number of frequencies per class growing by a factor of almost
`60000` between `r=1` (2 frequencies) and the finest class at `ell=12`
(`r=11`, 118098 frequencies). At `ell=12` the eleven per-class energies
all fall between `34.76` and `35.86` billion (under 3% spread). This is
the opposite of the additive-spectrum pattern E-137 found (primitive
`l^2` mass concentrated at the maximizer, not equidistributed by
conductor).

Consequence: since energy per class is roughly fixed but frequency
count grows exponentially with `r`, the typical (RMS-within-class)
coefficient falls like `~3^{-r/2}` (square-root cancellation within
each class), but `sup` in the `r=1` class (only 2 frequencies, no room
for cancellation) grows by an exact factor `3` per level, while `sup`
in the finest class of each level grows far more slowly
(`sup/sqrt(3^r)` moves from `2.55` at `ell=6` to `6.65` at `ell=12`,
nearly stable).

## What this does and does not establish

An empirical structural finding (Regra 10b) about the Mellin transform,
verified and reproducible, not connected here to Q2 (H-177) or to any
proof. The `r=1` class (2 frequencies, no cancellation possible by
sample size) looks structurally different from the rest; whether that
is a genuine obstruction or an artifact of having only two samples at
that conductor is an open theoretical question, not pursued further
here (would be new theory, not measurement).

Not mirrored in `collatz-endogeny` (not yet cited by any paper text).
