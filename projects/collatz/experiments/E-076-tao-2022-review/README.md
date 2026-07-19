# E-076 — Review of Tao, "Almost all orbits of the Collatz map attain almost bounded values" (2022)

Related hypothesis: [`H-076-tao-2022-review.md`](../../hypotheses/H-076-tao-2022-review.md)

## What was done

Not a "bug hunt" (a Terence Tao paper, peer-reviewed in a top-tier
journal) — a disciplined verification of the numerical examples and
concrete explicit identities the text presents: examples of the
Syracuse map, the identity Col_min(N)=Syr_min(N/2^v2(N)), and the exact
distribution of Syrac(ℤ/3ℤ) and Syrac(ℤ/9ℤ) via an independent
reimplementation of Lemma 1.12's recursive formula.

## Result

Everything confirmed without exception, including exact reproduction
(fraction arithmetic, not floating point) of 12 non-trivial rational
probability values (e.g. 8/63, 22/63) that the text presents as the
recursive formula's result. See H-076 for the full verdict.

## Reproduce

```
python3 experiment.py
```
