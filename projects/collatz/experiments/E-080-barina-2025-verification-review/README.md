# E-080 — Review of Barina, "Improved verification limit..." (2025)

Related hypothesis: [`H-080-barina-2025-verification-review.md`](../../hypotheses/H-080-barina-2025-verification-review.md)

## What was done

A direct continuation of the same author's 2020 paper (item 105,
already verified in E-075 — identical central equations). This review
focuses on what's new: the 3^k sieve mechanism. We directly simulated
(exhaustive search, not just reproducing numbers) to confirm that 100%
of numbers ≡2 (mod 3) are eliminable by the 3¹ sieve, and 0% of the
other residues — matches exactly the cited percentage (33.33%).

## Result

No error found. The verification timeline and the order of the 5 new
path records were also confirmed. See H-080 for the full verdict.

## Reproduce

```
python3 experiment.py
```
