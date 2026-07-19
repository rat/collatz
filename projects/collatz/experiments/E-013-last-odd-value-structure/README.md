# E-013 — Structure of an orbit's last odd value

Related hypothesis: [`H-013-last-odd-value-structure.md`](../../hypotheses/H-013-last-odd-value-structure.md)

## What was tested

Whether the last odd value (>1) of any orbit is always J_t=(4^t−1)/3
(a consequence of H-012), and how the value of t is distributed.

## Result (300,000 random samples, n up to 10^9)

Formula confirmed without exception. Distribution of t:

| t | J_t | fraction |
|---|---|---|
| 2 | 5 | 93.77% |
| 4 | 85 | 2.37% |
| 5 | 341 | 3.78% |
| 7 | 5461 | 0.01% |
| 8 | 21845 | 0.06% |
| 10 | 349525 | ~0% |
| 11 | 1398101 | ~0% |

Classes t=3,6,9 (J_t divisible by 3: 21, 1365, 87381) have **zero**
occurrences — explained by H-005 (a value divisible by 3 never
reappears after a generic orbit's first odd step).

**Unexplained anomaly**: t=5 has a higher fraction than t=4, contrary
to the naive expectation of monotonic decay ~1/4 per step. Recorded as
an open question in H-013.

Reproduce: `python3 experiment.py 300000 2`

## Update — exhaustive sweep and correction (see `CORRECTION.md`)

A second attempt to explain the anomaly via J_t's residue mod 3 was
**refuted** by an exhaustive (not sampled) sweep up to 80 million: the
ratio between adjacent classes grows for the pairs (t=4,5) and (t=7,8)
but **inverts** for (t=10,11) and (t=13,14). The anomaly is real, but
does not follow the simple mod-3 pattern I had speculated. Full details
and data in `experiment_exhaustive.py` and `CORRECTION.md`.

## Status

**Confirmed** (structure + explanation of the sterile classes). The
p₅>p₄ anomaly (and the broader, non-monotonic pattern between adjacent
classes) remains genuinely open — more complex than the initial mod-3
hypothesis.
