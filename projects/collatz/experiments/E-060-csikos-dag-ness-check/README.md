# E-060 — Verification of the Collatz-specific content of paper #028 (Csikos, "DAG-ness")

Related hypothesis: [`H-060-csikos-dag-ness-review.md`](../../hypotheses/H-060-csikos-dag-ness-review.md)

## Paper

Csikos, E. (2026). *A Continuous Multi-Component Measure of Directed
Acyclicity (DAG-ness)*. arXiv:2606.22205, 22 pages. **A graph-theory
paper, not a Collatz paper** — Collatz appears only in Section 5.2
(half a page) as an illustrative example. Local PDF:
`literature/papers/027_Continuous-Multi-Component-Measure-DAG-ness.pdf`.

## What was tested (scope limited to the Collatz-specific content)

1. Restricting the standard Collatz map to the first 2228 positive
   integers: there is exactly one cyclic SCC (`{1,2,4}`), every
   `n=1..2228` reaches it.
2. Cycle direction, checked against the real edges of the map `T(n)`
   defined in the paper itself.
3. Arithmetic of the Composite Score `D(G)=0.875` (Table 1).

## Result

Collatz-specific content correct, except: the paper describes the
cycle as "1→2→4→1", but by `T(n)`'s real edges (`T(1)=4, T(4)=2,
T(2)=1`) the correct cycle is **1→4→2→1**. Doesn't affect any numeric
result (`A`,`F`,`M`,`S`,`D` don't depend on the textual order). A
description error, not a calculation error. The rest of the paper
(Sections 2-4, the general graph-theory framework) is outside this
review's scope — it isn't Collatz-specific.

## How to reproduce

```
python3 experiment.py
```

No dependencies beyond the stdlib. Runs in <1s.
