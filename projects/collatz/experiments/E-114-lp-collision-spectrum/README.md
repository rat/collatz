# E-114: finite-level Lp collision spectrum

Related hypothesis: H-141.

This experiment computes the exact finite-quotient identity

```text
L_p(ell) = 3^(ell(p-1)) sum_u mu_ell(u)^p
         = ||d mu_ell / d Haar_ell||_p^p.
```

For integer `p`, this is `3^(ell(p-1))` times the probability that `p`
independent Syracuse sums agree modulo `3^ell`. The distribution is
computed with the recursion audited in E-100. Floating-point rounding
and the truncation after 100 terms are below the displayed precision.

The calculation tests how the normalized moments behave on a finite
range around `p=2`. It cannot prove that any moment is bounded or
divergent as `ell` tends to infinity.

Run from this directory:

```sh
python3 lp_collision_spectrum.py --max-ell 14
```

The script prints each level, reports the last consecutive ratio and a
local log-slope, and writes `lp_collision_spectrum.csv`. These last two
quantities are diagnostics, not extrapolated asymptotic exponents.
