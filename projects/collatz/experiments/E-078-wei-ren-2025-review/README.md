# E-078 — Review of Wei Ren, "Reduced Collatz dynamics is periodical..." (2025)

Related hypothesis: [`H-078-wei-ren-2025-review.md`](../../hypotheses/H-078-wei-ren-2025-review.md)

## What was done

We verified the paper's central "Period Theorem" (item 108): if the
"reduced dynamics" d_r(x) (the I/O operation sequence up to the first
iterate below x) exists, then d_r(x+2^L)=d_r(x), where L is the
sequence length. We also verified the extension (Corollary 3.24) and
the appendix's form characterization (Form Corollary).

## Result

Everything confirmed without exception: the paper's own examples, the
Period Theorem (499 cases), Corollary 3.24 (245 cases), the Form
Corollary (999 cases, in both parts). We also confirmed the theorem is
conditional (only holds for x whose reduced dynamics already exists)
and doesn't close the conjecture — something the author himself
explicitly acknowledges in the conclusion. See H-078 for the full
verdict.

## Reproduce

```
python3 experiment.py
```
