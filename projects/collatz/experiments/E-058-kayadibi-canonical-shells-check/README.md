# E-058 — Verification of paper #015 (Kayadibi, "Canonical Shells and Residue-Cover Trees")

Related hypothesis: [`H-058-kayadibi-canonical-shells-review.md`](../../hypotheses/H-058-kayadibi-canonical-shells-review.md)

## Paper

Kayadibi, S.Y. (2026). *Canonical Shells and Residue-Cover Trees in a
Conditional First-Descent Approach to the Collatz Problem*. Victoria
University, Melbourne. Local PDF:
`literature/papers/015_Canonical-Shells-Residue-Cover-Trees.pdf`.
Builds on two earlier papers by the same author (one of them is item
038 of this collection).

## What was tested

A conditional framework (reduces "universal first descent" to two
structural conditions not proven in general: dyadic gap + residue-cover
tree closure). We verified everything the paper actually PROVES (not
the conditional part itself):

1. Persistence Identity (Lemma 3.1) + Corollary 3.2 (no early descent)
   — 3120+2730 cases, against real Collatz simulation.
2. First-Exit Formula (Lemma 4.1) + Certified Exact Descent (Theorem
   4.5) — 1414 cases, 191 certified, `τ(n)=m` exactly confirmed.
3. Dyadic Gap Condition (Definition 5.1) — `2≤m≤20,000` with exact
   native integers; Table 1 values from the paper reproduced exactly.
4. Cumulative Affine Formula (Theorem 7.3) + Residue Cylinder (Theorem
   8.2) — 2000+500 random cases.
5. Smaller-scale reproduction of Table 2/3 (`N=10⁶`, `L=2000`) — 0
   early descents, 0 unresolved cases.

## Result

**No error found.** The entire proven machinery held up under
verification without exception, including exact reproduction of the
paper's specific values (Table 1: convergents 5,41,306,15601 and their
K_m: 8,65,485,24727). The paper is explicit (Section 15) that it does
NOT unconditionally prove Collatz — the conditional part (global dyadic
gap + tree closure) remains genuinely open, and this review did not
attempt to resolve it (out of scope).

## How to reproduce

```
python3 experiment.py
```

No dependencies beyond the stdlib. Runs in ~6s (Part 3, dyadic gap up
to m=20,000, and Part 5, N=10⁶, are the most costly).
