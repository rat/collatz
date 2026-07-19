# E-066 — Verification of paper #057/089 (Reyes Jiménez, "A Fibonacci theorem for Collatz trajectories via modular graph structure")

Related hypothesis: [`H-066-reyes-jimenez-fibonacci-review.md`](../../hypotheses/H-066-reyes-jimenez-fibonacci-review.md)

## Paper

Reyes Jiménez, M-A. (2026). *A Fibonacci theorem for Collatz
trajectories via modular graph structure*. arXiv:2606.02621 [math.NT].
Local PDF: `literature/papers/056_Fibonacci-theorem-Collatz-modular-graph.pdf`.

Genuine, technically sophisticated mathematical research (not an
amateur attempt at solving the conjecture). Item 089 is a confirmed
duplicate.

## What was tested

11 parts, covering the paper's whole structure:

1. Lemma 2.1 (corrective residue) + Example 2.2.
2. Proposition 2.3 (bijectivity/periodicity).
3. Lemmas 2.4-2.5 (antisymmetry/translation).
4. Proposition 2.8 (mod 6 transition — already verified in H-027).
5. Propositions 3.1/3.3 (graph SCCs and simple cycles).
6. Five spectral radii (Propositions 3.4, 4.10, 4.11, 4.13, Theorem
   4.15).
7. Corollary 4.5 (confinement to {1,2,4,5}).
8. **Theorem 4.7 (main result)**: exact Fibonacci count.
9. Example 4.8.
10. Theorem 4.1 + Corollary 4.4 (modular path theorem).
11. Proposition 4.18/Corollary 4.19 (distribution over positive
    cycles).

## Result

**0 failures across all 11 parts.** The Fibonacci count (Theorem 4.7)
was reproduced by brute force exactly for m=1 to 22 (F(2)=1 through
F(23)=28,657). No mathematical error found — the most technically
rigorous paper reviewed in this session.

Two bugs were found and fixed in OUR OWN verification script (not in
the paper): a cycle comparison without consistent rotation
normalization (Part 5), and an off-by-one indexing error when
extracting (h₂,h₃,h₄) (Part 9) — see H-066 for details.

## How to reproduce

```
python3 experiment.py
```

Requires `numpy` (for eigenvalues in Part 6; without numpy, that part
is skipped and doesn't count as a failure). Runs in a few seconds.
