# E-003 — Long-range dependence between valuations

Related hypothesis: [`H-003-long-range-dependency.md`](../../hypotheses/H-003-long-range-dependency.md)

## What was tested

Extension of H-001/E-001: instead of only lag 1 (a_1 vs a_2), we tested
lags 1 through 6 (a_1 vs a_{1+k}), each with a fresh sample of 500,000
distinct, random odd numbers in [10^9, 10^12] — the same clean design
validated in E-001 (no aggregation by position-in-orbit, avoiding
trajectory collision).

## Result

| lag | n_pairs | collisions | Pearson r | p (corr) | chi-square | dof | p (chi2) | verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | 500,000 | 3  | -0.00043 | 0.763 | 35.6 | 49 | 0.924 | independence ok |
| 2 | 500,000 | 2  |  0.00004 | 0.975 | 48.7 | 49 | 0.484 | independence ok |
| 3 | 500,000 | 6  |  0.00181 | 0.201 | 50.7 | 49 | 0.407 | independence ok |
| 4 | 500,000 | 21 |  0.00006 | 0.967 | 49.9 | 49 | 0.436 | independence ok |
| 5 | 500,000 | 36 | -0.00030 | 0.834 | 26.2 | 49 | 0.997 | independence ok |
| 6 | 500,000 | 91 |  0.00024 | 0.864 | 33.5 | 49 | 0.956 | independence ok |

Reproduce: `python3 experiment.py 500000 6`

Collisions (same value visited by two different trajectories) grow
with lag, as expected (longer orbits have more chance of crossing),
but remain a negligible fraction of the sample (max 91/500,000 =
0.018% at lag 6) — not enough to distort the result.

## Conclusion

No statistically significant dependence detected at any of the 6
tested lags. This extends — with fairly high confidence — the result
of E-001: it's not just lag 1 that's consistent with the i.i.d. model,
independence holds across the whole short/medium-range window tested.
Strengthens confidence in the assumption used by standard stochastic
models (Kontorovich–Lagarias).

## Status of H-003

The hypothesis (long-range dependence exists) is **not supported** —
result consistent with independence at every tested lag.
