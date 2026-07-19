# E-104 — Ergodic optimization test for the freezing (H-129)

Related hypothesis: [`H-129-q-adic-pole-analog-seymour.md`](../../hypotheses/H-129-q-adic-pole-analog-seymour.md)

## What was tested

After reframing the quenched-vs-annealed freezing (already proven in
general in the paper, Proposition prop:always-frozen) as an ergodic
optimization/zero-temperature thermodynamic-formalism phenomenon (a
reframing suggested by the Fable in an earlier consultation about an
external Seymour paper), we directly tested whether the quenched Gibbs
measure concentrates on the "greedy" trajectory (always the smallest
admissible `a` at each step) as depth grows, in the frozen vs.
non-frozen phase.

## Result 1 — no genuine concentration (revised)

`experiment_greedy_concentration.py` computes p_greedy(k) = the
quenched probability of always following the greedy branch for the
first k steps, via the same exact DP `Z_k` already validated in E-103.
Initial observation: in frozen q=5, p_greedy seemed to slow toward a
near-plateau — but an EXACT argument (Z_k ≥ greedy_weight, valid for
every k, since all weights are positive) shows the greedy path's own
rate is much more negative than Z_k's real growth rate, in both phases.
The observed plateau is a pre-asymptotic artifact (the same k≈407
crossover already known from H-109) — there is no genuine
concentration.

## Result 2 — a real collateral finding, but the numerical prediction wasn't confirmed

Along the way, it emerged that A(α)/α = P(α_c)/α_c is constant (an
already-established exact fact), and that the exponent B(α_c)=3/2 is
literally the Bramson constant for branching-random-walk maxima — a
real, citable connection to the BRW extremes literature, independent of
the rest.

This led to testing whether a*=(log q − P(α_c)/α_c)/log 2 predicts the
real average ⟨a⟩ of the map's known cycles. The initial confirmation
seemed strong for q=5 (secondary cycles matching a* to 1.3%), but a
direct test (computing A(α)/α via DP, without the annealed shortcut,
for 3 real roots of q=5) **did not reproduce** a* in any case, and
showed unstable oscillation in k. A third data point (q=7) refuted the
alternative hypothesis tested (the ratio α₊/α_c predicting fit
quality).

**Verdict**: a*'s numerical agreement with catalogued cycles should be
treated as weak anecdotal evidence, not confirmation. The formula used
is, at best, an unverified upper bound (a_min≤a*), not a tested
equality — equality would require a REM-type freezing formula that was
never proven nor tested for this specific deterministic subshift.

## What survives as solid

- The Bramson constant B(α_c)=3/2 (an exact fact, citable on its own).
- The ergodic-optimization/thermodynamic-formalism framing as a more
  correct theoretical lens than REM/spin glass for this freezing (but
  without a*'s quantitative prediction, which didn't hold up).

## Files

- `experiment_greedy_concentration.py` — Result 1 (concentration of the
  greedy measure).
- `output.txt`, `greedy_concentration_results.json` — raw data.

Result 2's scripts (the A(α)/α test via direct DP, without the
annealed shortcut) were run in session scratchpad, not persisted in
this repository (they were exploratory, and refuted the very
hypothesis they tested).

## Next steps (if the line is resumed)

~~A genuine spectral analysis of the transfer operator (Perron-Frobenius
on Z/q^kZ) or the Manneville-Pomeau/Sarig-Iommi formalism for
infinite-alphabet Markov chains~~ — **executed and closed in
[E-105](../E-105-transfer-operator-spectral-gap/README.md)
(2026-07-19)**: the dual operator M_α has a perfect, proven spectral
gap (exact spectrum {Λ,0}), Manneville-Pomeau/Sarig-Iommi doesn't
apply. The k^-0.222 transient belongs to a separate, nonlinear layer.
What remains as a real path: a log-periodic tail test (see
E-105/E-103). None of this was integrated into the paper.
