# E-001 — Independence between consecutive 2-adic valuations

Related hypothesis: [`H-001-parity-independence.md`](../../hypotheses/H-001-parity-independence.md)

## What was tested

Whether a_i (2-adic valuation of 3n+1 in the accelerated orbit) and
a_{i+1} (the valuation of the next step) are statistically independent,
as standard stochastic models in the literature assume.

## Attempt 1 — `experiment.py` (with an identified methodological flaw)

Aggregated pairs (a_i, a_{i+1}) from **all positions of all orbits**
for the first N odd numbers. Initial result: huge chi-square,
appearing to show strong dependence.

**Problem discovered**: Collatz orbits collide — once two different
trajectories reach the same intermediate value, their entire
subsequent tail is identical. Aggregating by position-in-orbit counts
the same path segment multiple times, violating the independent-sample
assumption (pseudo-replication). A simple "minimum n" filter (to
exclude the universal final tail ...→8→4→2→1) reduced but did not
eliminate the effect — collisions happen well before the final tail,
whenever distinct orbits converge to the same value.

**This problem is itself a useful finding**: any future experiment
aggregating statistics across multiple orbits needs to consider orbit
collision as a source of pseudo-replication. See the note added to
`protocols/new-experiment.md`.

## Attempt 2 — `experiment_v2_clean.py` (corrected design)

Samples K **distinct, random** odd numbers over a large interval
(10^9–10^12), looking only at the first 2 steps (a_1, a_2) of each.
With large, spread-out starting numbers, the chance of two
trajectories colliding within 1-2 steps is negligible — each pair is a
genuinely independent observation (confirmed: 0 collisions detected in
either round).

### Results

| K (samples) | seed | Pearson r | p (Pearson) | chi-square | dof | p (chi-square) |
|---|---|---|---|---|---|---|
| 300,000 | 42 | -0.00376 | 0.039 | 42.0 | 49 | 0.75 |
| 1,000,000 | 7 | -0.00035 | 0.72 | 39.5 | 49 | 0.83 |

Reproduce: `python3 experiment_v2_clean.py 1000000 1000000000000 7`

## Conclusion

With the correct experimental design (no pseudo-replication from orbit
collisions), **independence between a_1 and a_2 is not rejected** — the
data are consistent with the i.i.d. model used by the standard
stochastic literature. The "dependence" signal from Attempt 1 was a
methodological artifact, not a real phenomenon.

This is consistent with the classical equidistribution theorem of
Terras (1976) / Everett (1977), which already formally establishes
that finite blocks of the parity sequence are equidistributed as n
varies — i.e., this experiment **empirically reproduces an already
known result**, rather than discovering something new. Value of the
exercise: validating our own methodology (and the orbit-collision
pitfall) before attempting something more original.

## Status of H-001

**Refuted** (in the form tested here — simple 2-step independence,
large n). Not supported by the data. A natural extension (long-range
dependence, or effects conditioned on residual structure) is recorded
as a possible next step, but is not an immediate priority given that
the simple case is already known/confirmed.
