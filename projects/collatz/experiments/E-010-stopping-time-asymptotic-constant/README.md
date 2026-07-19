# E-010 — Asymptotic constant of the stopping time

Related hypothesis: [`H-010-stopping-time-asymptotic-constant.md`](../../hypotheses/H-010-stopping-time-asymptotic-constant.md)

## What was tested

We derived K≈7.2283 from facts we had already established ourselves
(E[a]=2 for the geometric distribution of valuations, H-001),
predicting total_stopping_time(n) ≈ K·log₂(n). We fit a simple linear
regression on real data (~1 million odd n, 3 up to 2,000,000).

## Result

- **Empirical K = 7.1833** vs. **theoretical K = 7.2283** — relative
  difference of only **0.62%**. Excellent agreement between the
  theoretical derivation (from facts already established in H-001) and
  the real data.
- **R² = 0.0307** — log₂(n) alone explains only ~3% of the variance in
  total_stopping_time(n). The vast majority of the variation does
  **not** come from the size of n, it comes from fine structure (the
  specific valuation sequence). This is consistent with — and helps
  explain why — we were able to find record holders and structural
  exceptions (H-004, H-007): the mean behaves as predicted, but the
  individual deviation is huge.
- The standard deviation of residuals grows slowly with log₂(n) (54.5
  → 60.2 across the sample) — consistent with the classical theory of
  passage times for random walks with drift, where variance grows
  approximately linearly in the number of steps (here, in log(n)).

Reproduce: `python3 experiment.py 2000000` (~7s).

## Conclusion

The random-walk heuristic is exactly right **on average** — our own
derivation matches the data within <1%. But the low R² is the more
interesting point: it quantitatively confirms that the magnitude of n
says very little about the individual stopping time, which is exactly
the kind of residual variance that can hide structure (like what we
found in H-004/H-007). Not a new discovery — it reproduces a classical
result — but we did the derivation and verification ourselves, with
our own data and already-established facts, rather than just citing
the literature.

## Status of H-010

**Confirmed** (theoretical derivation matches empirical data within
<1%).
