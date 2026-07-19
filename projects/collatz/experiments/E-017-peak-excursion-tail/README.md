# E-017 — Orbit peak tail: exact factor of 2 per bit

Related hypothesis: [`H-017-peak-excursion-tail.md`](../../hypotheses/H-017-peak-excursion-tail.md)

## What was tested

The Collatz sequence is an exact multiplicative martingale (E[3/2^a]=1,
verified analytically — exact geometric series sum, not an
approximation). Via the Cramér large-deviations equation, this implies
the orbit peak's tail decay exponent is **exactly θ*=1** — we verified
this by solving 3^θ = 2^(1+θ)−1 and confirming θ=1 is an exact root
(3¹=3, 2²−1=3).

Prediction: P(peak(n) ≥ n·2^Δ) ~ C·2^(−Δ) — the tail decays by exactly
a factor of 2 per extra bit of excursion.

## Result

Sample of 2,000,000 random n in [10⁹, 10¹²]. Log-linear fit of
P(Δ≥x) vs. x:

- Using all points with reasonable statistical count (x=2 to 15):
  empirical slope = **−0.9657** (predicted −1.0).
- Using only the farthest tail (x≥6, where the asymptotic approximation
  is more accurate): empirical slope = **−1.0045** — a difference of
  only **0.45%** from the exact theoretical value.

Reproduce: `python3 experiment.py 2000000 1000000000 1000000000000 99`
(~30s). Also confirmed with a smaller sample (500k) and a different
seed (42): slope −0.9682 (all points).

## Conclusion

The Cramér exponent θ*=1 (with no free parameter, derived solely from
the martingale property already implicit in H-001) predicts the orbit
peak's tail with better than 0.5% precision in the asymptotic region.
This is the project's third precise theoretical confirmation in the
H-010/H-011 style (derive → confirm), this time for the orbit's
**maximum** rather than the mean/variance of time.

## Status of H-017

**Confirmed** (far-tail slope within 0.5% of predicted).
