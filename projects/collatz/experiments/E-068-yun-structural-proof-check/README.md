# E-068 — Verification of paper #076 (Yun, "A Structural Proof of the Collatz Conjecture") — PROOF CLAIM

Related hypothesis: [`H-068-yun-structural-proof-review.md`](../../hypotheses/H-068-yun-structural-proof-review.md)

## Paper

Yun, Y.H. (2026). *A Structural Proof of the Collatz Conjecture via
non-repeating trajectory and Recursive Decay*. osf.io (not
peer-reviewed). Local PDF:
`literature/papers/075_Structural-Proof-Collatz-nonrepeating.pdf`.

## Verdict

**NOT a valid proof** — weaker than item 049 (Boyle, H-065). Contains
three independent circular arguments:

1. **Most severe gap** (Section 8): the "rank function"
   `r(x):=min{n : f^(n)(x)=1}` is only defined for `x` whose orbit
   already reaches 1 — it presumes its own conclusion. Demonstrated by
   analogy with a map that provably diverges (`g(x)=2x`), whose
   analogous "rank function" is likewise undefined.
2. Theorem 6.1: "the only known fixed point is 1" — presents the
   conclusion (absence of other cycles) as a premise.
3. Section 5/9.2.3: a fallacy about infinite cardinalities
   (non-injectivity doesn't imply dynamical convergence).

A concrete arithmetic error was also found (Equation 9.8): `f(5)` and
`f(21)` computed with wrong powers of 2, arriving at a result (2) that
isn't even odd.

## What was tested

1. Lemma 6.1 (neighbor distinction) — correct.
2. Arithmetic error in Equation 9.8 — confirmed.
3. Method counterexample for the rank function (Part 3).
4. Computational search for non-trivial cycles up to 2 million — none
   found (doesn't prove their absence, just doesn't contradict it).

## How to reproduce

```
python3 experiment.py
```

No dependencies beyond the stdlib. Runs in a few seconds.
