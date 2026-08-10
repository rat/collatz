# E-097 — Empirical statistical gate for the qx+1 generalization (H-113)

Related hypothesis: [`H-113-statistical-gate-kontorovich-lagarias-vs-volkov.md`](../../hypotheses/H-113-statistical-gate-kontorovich-lagarias-vs-volkov.md)

## What was done

Measures the empirical counting exponent of the real 5x+1 reverse tree
to decide between two competing theoretical predictions from the
literature: Kontorovich-Lagarias (2009), 0.650919 (identical to our
second root of the qx+1 pressure equation, H-109), vs. Volkov, 0.678.

## Files

- `pressure_qx1.py`, `empirical_qx1_tree.py`, the Fable's original
  scripts (multitype pressure-equation verification; the first ad hoc
  empirical confirmation, cited in H-109 but never persisted in the
  repository before).
- `pilot_gate_5x1.py`, `pilot2_gate_5x1.py` — noise/bias/cost
  calibration pilots (q=5 admissibility rule, sensitivity to
  truncation bias).
- `experiment_gate_production.py` — production run, n=300, fixed
  window 1e5-1e8, buffer=5 decades (first version; documented in H-113
  as the step that revealed the "CI excludes both candidates" failure
  mode predicted by the Fable).
- `experiment_gate_richardson.py` — final version: DFS with path-max
  tracking (a single pass gives the counts at every buffer
  simultaneously, validated byte-for-byte against the old method) +
  Aitken Δ² extrapolation on the mean curve across roots + bootstrap.

## Result (original, 2026-07-17; superseded reading, kept for the record)

Aitken Δ² (buffer→∞): **0.639, 95% CI=[0.633, 0.645]**, read at the
time as excluding Volkov (0.678) with wide margin (~10+ standard
errors), with the residual gap to Kontorovich-Lagarias (0.650919)
attributed to a fixed-window pre-asymptotic (the per-decade slope panel
was still rising in the last tested decade), not to uncorrected
truncation bias.

**This exclusion claim does not hold.** H-137 (2026-08-07) and E-139
(2026-08-09) show the estimator above is itself biased by 0.038 on a
process of known exponent, more than the gap Δ=0.027 between the two
disputed values, so a raw 0.639 reading was never evidence against
either prediction: it is close to what a process of exponent 0.650919
returns on this same estimator. E-139 calibrates the bias out with
matched synthetic controls sharing the arithmetic tree's branching and
sibling-spacing law: at a checkpoint decade where the bias has fallen
below 0.003, the arithmetic tree's reading lands inside the band of
three independent constructions of exponent 0.650919 and more than
seven band-widths from a construction of exponent 0.678. See H-113 for
the full history, `../E-139-kl-volkov-window-calibration/` for the
calibrated experiment, and H-113 also for a necessary correction to an
earlier H-109 claim (the "1.547 vs 1.5363" Hill estimator cited there
is not confirmatory, the real standard error is ~0.45).

## Reproduce

```
python3 experiment_gate_richardson.py
```
