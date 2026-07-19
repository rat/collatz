# E-062 — Verification of paper #031 (Melas & Poulios, "Predicting Extreme Stopping Time Behavior")

Related hypothesis: [`H-062-melas-poulios-stopping-time-review.md`](../../hypotheses/H-062-melas-poulios-stopping-time-review.md)

## Paper

Melas, E. & Poulios, N.C. (2026). *Predicting Extreme Stopping Time
Behavior in the Collatz System: A Probabilistic and Statistical
Approach*. Journal of Dynamics and Games (AIMS), peer-reviewed. Local
PDF: `literature/papers/031_Predicting-Extreme-Stopping-Time.pdf`.

## What was tested

A statistical paper (logit regression + decision tree) for predicting
extreme stopping time, not for proving Collatz. Uses `Col(n)=n/2`
(even) `/(3n+1)/2` (odd) — a different map from the accelerated `T(n)`
used in other reviews in this collection.

1. Exact logarithmic identity (Eq. 3), via `Fraction`, 300 cases.
2. The paper's specific numerical example (`n=10`).
3. Sanity check of the modified Collatz map `Col_mod` (`n=2..200,000`).
4. Exact, deterministic reproduction (full census, no random sampling)
   of the 6 density windows cited (Figures 7 and 8).

## Result

**Everything confirmed exactly**, including the 6 density counts
(powers of 10 and of 3, up to `10¹⁵`). The logit/decision-tree models
(Sections 5-7) were not reproduced byte-for-byte — they depend on
random sampling whose exact generator/seed isn't fully specified in
the paper (out of scope, not a failure).

## How to reproduce

```
python3 experiment.py
```

No dependencies beyond the stdlib (`fractions`). Runs in ~1.6s.
