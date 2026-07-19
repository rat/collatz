# E-093 — Refutation of Tynski's (2026) proof claim, item 087

Related hypothesis: [`H-093-tynski-2026-review.md`](../../hypotheses/H-093-tynski-2026-review.md)

## What was done

The paper claims to prove Collatz via a deterministic Lyapunov bound
(axiom W6): log₂(n_m) ≤ log₂(n₀) − m·δ + C·√m with universal C≤5,
numerically verified only up to n₀≤3×10⁴. This experiment computes the
smallest C that makes the bound hold across the whole trajectory, for
samples far beyond the range the paper tested, including known
delay-record holders and adversarial seeds.

## Result

C_min already exceeds 5 just past n₀=10⁴, reaching 8.34 for known
delay-record holders, with no sign of stabilizing. Directly refutes
the central numerical claim underpinning axiom (W6) — the same pattern
of confusing average rate with deterministic guarantee already
catalogued in other proof claims in this project (H-045, H-065).

## Reproduce

```
python3 experiment.py
```
