# E-011 — The variance in H-010 is predicted noise, not hidden structure

Related hypothesis: [`H-011-variance-scaling.md`](../../hypotheses/H-011-variance-scaling.md)

## What was tested

H-010 found R²=0.03 (log₂n explains little of the individual variance
of total_stopping_time). We derived the theoretical prediction that
Var(total_stopping_time(n)) ≈ 186.93·log₂(n) — **linear** growth in
log₂(n), not quadratic — using the first-passage-time approximation of
a random walk with drift (Inverse Gaussian distribution), combining
Var(a)=2 (H-001) with the exact relation between standard steps and
log₂ drift per accelerated step.

## Result

We sampled ~5,000 numbers per magnitude "level" (log₂n ≈ 10.5, 15.5,
..., 45.5 — from 2^10 to 2^46, using Python's native big integers) and
measured the empirical variance of total_stopping_time within each
level:

| log₂(n) | mean | variance | var/log₂n |
|---|---|---|---|
| 10.5 | 82.4 | 1969 | 187.5 |
| 15.5 | 115.6 | 2685 | 173.2 |
| 20.5 | 152.5 | 3557 | 173.5 |
| 25.5 | 188.9 | 4765 | 186.9 |
| 30.5 | 223.1 | 5345 | 175.2 |
| 35.5 | 261.5 | 6705 | 188.9 |
| 40.5 | 297.6 | 7208 | 178.0 |
| 45.5 | 333.6 | 8341 | 183.3 |

Regression (variance ~ coef·log₂n, no intercept): **empirical
coefficient = 181.53** vs. **theoretical = 186.93** — a difference of
only **2.9%**.

Reproduce: `python3 experiment.py 5000 7`

## Conclusion

Variance grows **linearly** in log₂(n) (not quadratically), with the
theoretically predicted coefficient matching the data within 3%. This
resolves H-010's open question: **the low R² is not evidence of hidden
structure** — it's exactly the behavior the random-walk heuristic
predicts. Since the mean grows linearly in log₂n but the standard
deviation grows only as √(log₂n), the signal-to-noise ratio
(deviation/mean) slowly decreases as n grows — but for the tested
magnitudes (log₂n ~ 10-45), it's still large enough (~35-45% of the
mean) to produce a small R² in a simple regression, without implying
anything new hidden.

## Status of H-011

**Confirmed** (empirical coefficient within 2.9% of theoretical, across
8 different orders of magnitude of n).
