# E-083 — Review of Wang, "Non-Existence of Collatz m-Cycles for m≤95" (2026)

Related hypothesis: [`H-083-wang-2026-review.md`](../../hypotheses/H-083-wang-2026-review.md)

## What was done

Does not claim a full proof — excludes specific non-trivial cycles
(m≤95), in the Simons–de Weger/Hercher style (the same territory as
this project's H-057). We verified the central, checkable algebraic
identities without reproducing the author's heavy computational
apparatus: Lemma 1 (local-minimum transition), Lemma 3 (elementary
estimate T(n)<3/n), Lemma 9 (suffix-exponent monotonicity), and Lemma
13's arithmetic (U(49)<7×10¹¹).

## Result

Everything confirmed without exception. The specific numerical values
in Lemma 12's Table and the finite searches for m=92-95 were not
reproduced (would require replicating the full "affine a-ladder"). See
H-083 for the full verdict.

## Reproduce

```
python3 experiment.py
```
