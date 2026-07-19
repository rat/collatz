# E-063 — Verification of paper #032 (Kosobutskyy & Mailland, "Jacobsthal Trees and Generalized κx±1 Transformations")

Related hypothesis: [`H-063-jacobsthal-trees-review.md`](../../hypotheses/H-063-jacobsthal-trees-review.md)

## Paper

Kosobutskyy, P. & Mailland, D. (2026). *Jacobsthal Trees and
Generalized κx±1 Transformations*. Communications in Advanced
Mathematical Sciences, 9(2), 77-91, peer-reviewed. Local PDF:
`literature/papers/032_Jacobsthal-Trees-Generalized-Transformations.pdf`.

Also covers the numerical examples of paper #084 (same authors, a
pedagogical version restricted to κ=3) — see
[`H-069`](../../hypotheses/H-069-mailland-kosobutskyy-jacobsthal-viewpoint-review.md).

## What was tested

A structural/notational paper generalizing the Collatz reverse tree to
`κx±1` (any odd κ) via "generalized Jacobsthal numbers". Doesn't claim
to prove the classical conjecture.

1. Definition 1.1 vs. Table 2.1 (reduces to classical Jacobsthal, OEIS
   A001045, in the κ=3 case).
2. Theorem 2.1 (periodicity) — `T_κ` = multiplicative order of 2 mod κ,
   tested for κ=1..199 and against Table 2.2 (including a 52-digit
   number for κ=181).
3. Table 2.4 (periodic node formation) — 24 cells.
4. Table 2.6 / Remark 1.7 (attractor points) — direct simulation of the
   forward map for κ=3,5,181.
5. Property 2.6 (uniqueness of the partition).
6. Property 2.7 (branching nodes = odd values in the cycle).
7. Property 2.5 (asymptotic ratio between consecutive nodes).
8. Specific examples from paper #084 (special case κ=3).

## Result

**0 failures across all 8 parts.** A minor finding: Remark 1.7 says
"PA={1,27,35}" for κ=181, but Table 2.6 itself shows that `q0=1`
diverges under κ=181 (`⋯→1→∞`) — confirmed by simulation (diverges,
32+ digits after 47 iterations). A textual inconsistency between
sections of the same paper, not an underlying mathematical error.

## Methodology note

Two iterations of our own verification script contained indexing bugs
(mixing up the `m`/`p` families, which have different index parities)
— fixed before finalizing; see the "Own methodology notes" section in
H-063 for details.

## How to reproduce

```
python3 experiment.py
```

No dependencies beyond the stdlib. Runs in a few seconds.
