# E-077 — Review of Clay, "The Long Search for Collatz Counterexamples" (2023)

Related hypothesis: [`H-077-clay-2023-review.md`](../../hypotheses/H-077-clay-2023-review.md)

## What was done

An expository paper (makes no proof claim) about excluding residue
classes mod 2^k. We verified three explicit algebraic formulas from the
footnotes (sequence length for classes 2k, 4k+1, 16k+3) and the claim
that 7.4% of "untamed" altitudes remain after excluding the cited
classes mod 32/128/256.

## Result

Everything confirmed exactly. A first attempt to verify the 7.4% gave
4.30% — our own error (we confused mod16 classes from one refinement
stage with mod32 classes from another stage, listed in different parts
of the text). Fixed, the calculation matches exactly: 19/256 ≈ 7.42%.
See H-077 for the full verdict.

## Reproduce

```
python3 experiment.py
```
