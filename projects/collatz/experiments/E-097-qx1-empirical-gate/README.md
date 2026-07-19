# E-097 — Empirical statistical gate for the qx+1 generalization (H-113)

Related hypothesis: [`H-113-statistical-gate-kontorovich-lagarias-vs-volkov.md`](../../hypotheses/H-113-statistical-gate-kontorovich-lagarias-vs-volkov.md)

## What was done

Measures the empirical counting exponent of the real 5x+1 reverse tree
to decide between two competing theoretical predictions from the
literature: Kontorovich-Lagarias (2009), 0.650919 (identical to our
second root of the qx+1 pressure equation, H-109), vs. Volkov, 0.678.

## Files

- `pressure_qx1.py`, `empirical_qx1_tree.py` — the Fable's original
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

## Result

Aitken Δ² (buffer→∞): **0.639, 95% CI=[0.633, 0.645]** — excludes
Volkov (0.678) with wide margin (~10+ standard errors); the residual
gap to Kontorovich-Lagarias (0.650919) has the signature of a
fixed-window pre-asymptotic (the per-decade slope panel is still
rising in the last tested decade), not of uncorrected truncation bias.
See H-113 for the full analysis, including a necessary correction to
an earlier H-109 claim (the "1.547 vs 1.5363" Hill estimator cited
there is not confirmatory — the real standard error is ~0.45).

## Reproduce

```
python3 experiment_gate_richardson.py
```
