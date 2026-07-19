# E-067 — Verification of paper #074 (Carelli, "Loop Termination and Generalized Collatz Sequences")

Related hypothesis: [`H-067-carelli-loop-termination-review.md`](../../hypotheses/H-067-carelli-loop-termination-review.md)

## Paper

Carelli, M. (2026). *Loop Termination and Generalized Collatz
Sequences*. arXiv:2605.15094 [cs.LO]. CISPA Helmholtz Center. Local
PDF: `literature/papers/073_Loop-Termination-Generalized-Collatz.pdf`.

A theoretical computer science paper (decidability of linear loop
termination). Doesn't attempt to solve the classical conjecture —
"generalized Collatz" is a broader family of which classical Collatz
is a particular case (d=2, m=3).

## What was tested (scope limited to Collatz-relevant content)

1. Algebraic mechanism of Proposition 17 (fixed point per residue
   class).
2. Empirical test of Proposition 17's practical content (~20,000
   trajectories).
3. Example 19 — a question explicitly left OPEN in the paper, tested up
   to n=2,000,000.
4. Theorem 14 (cycle bound ≤2 for 1D SLCs) — spot check.
5. Proposition 11 (combinatorial construction) — spot check.

## Result

**0 failures.** No error found in the content related to generalized
Collatz sequences. The broader computational-geometry machinery
(Minkowski-Weyl, Lemmas 21/23/24/25) is outside this review's scope —
it's about SLCs in general, not about Collatz.

## How to reproduce

```
python3 experiment.py
```

No dependencies beyond the stdlib (scipy isn't available in this
environment; Part 5 uses a combinatorial fallback with no LP). Runs in
a few seconds.
