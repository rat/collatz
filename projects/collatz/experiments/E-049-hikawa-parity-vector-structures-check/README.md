# E-049 — Verification of paper #007 (Kazunobu Hikawa, "Parity Vector Structures")

## Goal

Verify "Finite-Dimensional Combinatorial and Arithmetic Structures of
Parity Vectors for the Accelerated Collatz Map" (Kazunobu Hikawa, 34
pages). A purely combinatorial paper about "parity vectors" (binary
strings encoding the odd/even step sequence of the accelerated map),
classified by length k and Hamming weight d. Repeatedly honest: "these
finite-dimensional results do not by themselves determine the
existence or nonexistence of an infinite non-convergent trajectory...
remain an open problem."

## What we did

1. **Theorem 3.2** (explicit bijection Φ:U(d)→J(d+1), identity
   X(d+1)=W(d)): confirmed by brute force for d=1..7 — we generated
   U(d) and J(d+1) directly by weight (via combinations, avoiding
   enumerating all 2^(k-1) vectors) and confirmed that Φ's image
   applied to ALL of U(d) coincides exactly (as a set) with J(d+1).
2. **Theorem 5.2** (2-adic rigidity): confirmed on 2000 random pairs of
   vectors of the same length and same weight, with exact arithmetic
   (`fractions.Fraction`).
3. **Remark 5.3** (the paper's own counterexample for unequal weights):
   confirmed that the formula indeed does NOT hold in this case, as the
   paper honestly anticipates.
4. **Independent reimplementation of Algorithm 1** (dynamic
   programming): exactly reproduces the W(k) and W(d) values from the
   paper's Tables 1-2 (k=1,10,100; d=1,2,5,10,20 — all match exactly,
   within what's computable in this session, k up to 200).

## Efficiency note

The first version of the script tried enumerating ALL binary vectors up
to length 40 (2^39 ≈ 5.5×10¹¹) and then filtering by weight —
computationally infeasible, the background process failed without
producing output. Fixed by generating vectors directly by exact weight
via `itertools.combinations` (choosing the positions of the 1s),
reducing the cost from exponential to polynomial in the length.

## Result

**No error found** in any tested claim. A combinatorially high-quality
paper, honest about the limited scope of its results (nothing about the
conjecture itself). Discloses use of generative AI only for
prose/structure, with final responsibility resting with the author.

See `hypotheses/H-049-hikawa-parity-vector-structures-review.md`.

## How to run

```
/home/rat/.venv/bin/python3 experiment.py
```
