# E-075 — Review of Barina, "Convergence verification of the Collatz problem" (2020/2021)

Related hypothesis: [`H-075-barina-2020-verification-review.md`](../../hypotheses/H-075-barina-2020-verification-review.md)

## What was done

We verified the paper's central algorithm (item 105) — a technique for
avoiding the additive "+1" step by switching between the n and n+1
domains, using only multiplicative operations. We literally
reimplemented the identities (Eqs. 4-6) and the two convergence
algorithms (Algorithm 1: glide; Algorithm 2: delay).

## Result

Confirmed without exception: identities Eq.4/Eq.5 (200,000 cases),
Algorithm 1 converging correctly (999 cases), Algorithm 2 exactly
matching the standard delay count (5 seeds), the general formula Eq.6
(1000 random cases), and the textual claim about the average of 4
iterations per algorithm step (empirically confirmed, 4.009 vs 4.0
predicted). See H-075 for the full verdict.

## Reproduce

```
python3 experiment.py
```
