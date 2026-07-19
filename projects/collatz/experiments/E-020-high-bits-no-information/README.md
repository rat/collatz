# E-020 — Control: high bits carry little (not zero) information

Related hypothesis: [`H-020-high-bits-no-information.md`](../../hypotheses/H-020-high-bits-no-information.md)

## What was tested

F-statistic comparison (ANOVA-style, between-group / within-group
variance) for total_stopping_time grouped by: (a) n's 8 lowest bits,
(b) 8 highest bits (just below the leading bit), (c) random label
(pure-noise control), all with n of fixed length (50 bits), 200,000
samples.

## Result

| grouping | F |
|---|---|
| low bits | **50.70** |
| high bits | 1.80 |
| random control (pure noise) | 0.94 |
| high bits, after removing the K·log₂n trend (H-010) | 1.40 |

## Honest interpretation

Low bits carry real, strong information (F=50.7, expected — Terras/
H-002). High bits have a much smaller F (1.80) but **not exactly equal
to pure noise** (0.94) — not a clean confirmation of "zero
information".

Part of the excess is explained by the already-known trend (H-010:
mean stopping time grows with log₂n, and within a fixed-length
interval, high bits correlate with n's exact position in the interval,
hence with log₂n). Removing this trend, F drops from 1.80 to 1.40 —
still above the control (0.94), but closer. The residual likely comes
from H-011 (**variance** also depends on log₂n, not just the mean) — a
high-bit grouping corresponds to narrow log₂n bands with slightly
different variances, which violates the F-test's homogeneous-variance
assumption and inflates its value even without genuine new information.

Reproduce: `python3 experiment.py 50 200000`.

## Conclusion

High bits carry **much less** information than low bits (a factor of
~25-36×), consistent with the general expectation. But we did not
confirm exactly "zero information" — the small observed excess is
plausibly explained by already-known effects (H-010/H-011), not a new
discovery. Recorded with this caveat rather than overclaiming a
cleaner result than the data supports.

## Status of H-020

**Partially confirmed** — strong asymmetry confirmed, but "zero
information" in the high bits was not established with full precision.
