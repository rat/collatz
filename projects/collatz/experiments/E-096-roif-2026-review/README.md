# E-096 — Refutation of Roif's (2026) proof claim, item 050

Related hypothesis: [`H-096-roif-2026-review.md`](../../hypotheses/H-096-roif-2026-review.md)

## What was done

The paper closes the "ergodic gap" (the density-zero exceptional set
from Tao's 2022 Theorem) by asserting that "density zero implies empty
set" (Lemma 4.3). This experiment numerically demonstrates this is
false via two classic, elementary counterexamples: perfect squares and
powers of 2 — both infinite, both with density tending to zero.

## Result

The density of perfect squares drops from 10⁻¹ (N=10²) to 10⁻⁶
(N=10¹²); the density of powers of 2 drops to 4×10⁻¹¹ (N=10¹²) — in
both cases the set is obviously infinite. Directly refutes the paper's
Lemma 4.3, which is the only mechanism used to close Tao's exceptional
set and complete the "proof".

## Reproduce

```
python3 experiment.py
```
