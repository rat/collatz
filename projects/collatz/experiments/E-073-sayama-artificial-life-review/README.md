# E-073 — Review of Sayama, "An Artificial Life View of the Collatz Problem" (2011)

Related hypothesis: [`H-073-sayama-artificial-life-review.md`](../../hypotheses/H-073-sayama-artificial-life-review.md)

## What was done

We verified the paper's two central formulas (item 103): growth rate
L_app=log₂3≈1.585 bits/step (Eq.5) and extinction rate R_app=2
bits/step (Eq.6), for the accelerated, division-free dynamics
x_{t+1}=3x_t+LSNB(x_t).

## Interesting finding during verification

Measuring L over a long trajectory gave ~2.0 instead of ~1.585 — it
looked like a real discrepancy. Investigation showed powers of 2 are an
exact absorbing state of this dynamics (3·2^k+2^k=2^(k+2)), and 200/200
random samples reach a power of 2 within ≤500 steps. Measuring only the
active phase (before reaching the power of 2), the rate matches log₂3
within <0.5%. **Not an error in the paper** — the text already
explicitly acknowledges this extreme case right after Eq.5.

## Result

Both central formulas confirmed. See H-073 for the full verdict and the
discussion of what this absorbing state implies for the reach of the
"ecological explanation" the paper proposes.

## Reproduce

```
python3 experiment.py
```
