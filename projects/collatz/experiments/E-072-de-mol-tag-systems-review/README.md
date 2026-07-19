# E-072 — Review of De Mol, "Tag systems and Collatz-like functions" (2008)

Related hypothesis: [`H-072-de-mol-tag-systems-review.md`](../../hypotheses/H-072-de-mol-tag-systems-review.md)

## What was done

We literally implemented the tag system T_C from the paper's Theorem
2.1 (item 102, `literature/papers/102_Tag-Systems-and-Collatz-Like-Functions.pdf`)
— μ=3 symbols {α,c,y}, shift v=2, rules α→cy, c→α, y→ααα — and verified
that it correctly simulates the accelerated Collatz function
C'(2m)=m, C'(2m+1)=3m+2.

## Result

Confirmed without exception: 200 direct cases (n=1 to 200), 4 full
iterated trajectories (seeds 7, 27, 97, 871, until converging to
{1,2,4}), and the paper's own introductory example (period 6). See
H-072 for the full verdict. The paper makes no claim whatsoever about
the Collatz Conjecture itself — it's a computability-theory result
about tag systems, using Collatz as a case study.

## Performance note

The initial implementation used string concatenation (O(n) per step);
for large n this gave O(n²) total and timed out. Reimplemented with
`collections.deque` (O(1) per step) — see `experiment.py`.

## Reproduce

```
python3 experiment.py
```
