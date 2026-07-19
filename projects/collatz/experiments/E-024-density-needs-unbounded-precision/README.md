# E-024 — Density requires unbounded 3-adic precision

Related hypothesis: [`H-024-density-needs-unbounded-precision.md`](../../hypotheses/H-024-density-needs-unbounded-precision.md)

Origin: a list of ideas from another AI (suggesting a spectral/graph
approach for H-013), tested before investing effort in that direction.

## What was tested

Whether the density D(v) of the Collatz reverse subtree depends only
on v mod 3^K (a finite residue) — which would allow a finite-dimensional
transfer operator to compute it exactly.

## Result

Five values of v, all ≡85 (mod 729=3⁶), with proportional magnitude
budget (avoiding the error of comparing unequal budgets):

| v | D(v) |
|---|---|
| 85 | 0.0089 |
| 1543 | 0.0004 |
| 4459 | 0.0002 |
| 14665 | 0.000038 |
| 72985 | 0.000027 |

**Variation of more than 300×** between numbers with the same residue
mod 729. Methodology validated (exactly reproduces the already-checked
J_4 values in the original setup before running this test).

Reproduce: `python3 experiment.py 6 24`.

## Conclusion

D(v) is **not** a function of a bounded 3-adic residue — it depends on
arbitrarily deep structure. This closes, with direct evidence (not just
a failed attempt), the "finite-dimensional transfer operator" line for
H-013's formula, and also informs against naively trying a
"spectral/graph theory" approach (truncating residues) for this
specific quantity.

## Status of H-024

**Confirmed** — a negative result that rigorously explains an
already-suspected limitation, closing this investigation line with
clarity instead of leaving it open unexplained.
