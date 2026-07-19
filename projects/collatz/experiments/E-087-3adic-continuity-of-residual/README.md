# E-087 — 3-adic continuity of G(v)=D(v)·v

Related hypothesis: [`H-087-3adic-continuity-of-residual.md`](../../hypotheses/H-087-3adic-continuity-of-residual.md)

## What was done

A continuation of H-086 (which showed that most of the D(v) variation
found in H-024 was the trivial D(v)~C/v term). We tested whether the
residual G(v)=D(v)·v has 3-adic continuity: by progressively fixing
more base-3 digits of v (growing residue mod 3^K, K=1 to 8, in nested
chains) and letting magnitude vary freely, we measured whether the
variance of log10(G(v)) drops with K. Repeated with 5 independent
residue chains so as not to rely on a single coincidence.

## Result

Variance drops monotonically and consistently across the 5 chains —
more than a 4× reduction in standard deviation between K=1 and K=8.
Unlike raw D(v) (H-024, where no K reduced the variance), G(v) shows
real 3-adic continuity. A qualified green light for investing in the
Mahler-expansion or Syracuse-measure-in-ℤ₃ ideas proposed by the Fable.
See H-087 for the full analysis and the caveats about the strength of
the evidence.

## Reproduce

```
python3 experiment.py
```
