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
python3 pair_decoupling.py --levels 8 10 12 14 16 --eps 0.1
```

## Why a fixed threshold is the wrong test (again)

Comparing `pair(x)/d(x)^2` at a FIXED `x` across levels mixes the
correlation effect with the fact that `d(x)` itself changes with
`ell` at fixed `x` (the same trap already caught once in E-131 for
arc lengths). This script uses `x = exp(-eps*ell)`, which shrinks
with `ell`, so the comparison is between events of comparable rarity
at each level.

## Result

At `eps=0.1`, `ell=8..16`:

```text
ell   ratio=pair(x)/d(x)^2   implied theta (if pair ~ d^theta)
 8         0.336                    2.90
10         0.205                    3.13
12         0.084                    3.54
14         0.019                    4.16
16         0.001                    5.26
```

(hit counts for the pair statistic range from 129 to 1480, dropping
to 414 at `ell=16`; not single-observation noise.) The ratio falls
far below 1 and keeps falling, and the implied exponent `theta`
(assuming a fixed power-law form `pair(x) ~ d(x)^theta`) is not
converging to a constant — it grows from 2.90 to 5.26 over the tested
range. A constant `theta` would already give the conditional result
above with room to spare (any `theta > 1` is unconditionally useful,
and even `theta` near 2, i.e. full independence, was the original
hoped-for target). A GROWING `theta` means the joint tail decays
faster than any single fixed power of the marginal tail: a stronger
anti-clustering signal than what the m=2 hypothesis in H-161 asked
for.

## What this does not show

Five points at `ell<=16` cannot distinguish "a genuinely growing
exponent" from "approaching some larger fixed exponent slowly" from
"a finite-range effect that will not persist." This is evidence, not
a proof of any rate, and the theorem in H-161 needs the bound to hold
uniformly down to `x ~ exp(-c0*ell)` for a FIXED `c0` — a growing
`theta` estimated only at one threshold and one growing `ell` does
not by itself establish that. It is still the strongest quantitative
signal so far in this line of investigation, and worth extending
(more levels, more `eps` values, checking the two pair types
separately) before attempting to turn it into a proof.
