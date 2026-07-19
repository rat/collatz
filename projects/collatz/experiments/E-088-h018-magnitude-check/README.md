# E-088 — Tests whether H-018's obstruction has the same magnitude confound as H-024

Related hypothesis: [`H-088-h018-branch-decay-not-magnitude-confounded.md`](../../hypotheses/H-088-h018-branch-decay-not-magnitude-confounded.md)

## What was done

The Fable, consulted about H-026, raised a third suspicion: H-018's
"decay rate between fertile branches" (73×–680×) might have the same
magnitude confound that H-024/H-086 already corrected for raw D(v). We
tested this directly using 18 already-decomposed branch pairs
(t=10,13,16,17): we computed the expected trivial term w_{i+3}/w_i and
checked whether it varies (which would allow confounding) or is
constant (which would not).

## Result

w_{i+3}/w_i = 64 exactly across all 18 pairs (an algebraic consequence
of "3 positions" always multiplying by 4³). Dividing by a fixed
constant doesn't change the spread — confirmed numerically (identical
log10 standard deviation before and after, 0.5674 dex). The Fable's
suspicion doesn't apply here: it reinforces H-018's original conclusion
rather than requiring a correction. See H-088 for the full analysis.

## Reproduce

```
python3 experiment.py
```
