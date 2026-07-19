# E-059 — Verification of paper #021 (Amirian & Amirian, "3x+4y+1")

Related hypothesis: [`H-059-amirian-3x4y1-review.md`](../../hypotheses/H-059-amirian-3x4y1-review.md)

## Paper

Amirian, R. & Amirian, A. (2026). *A Generalization of 3x+1 Problem to
3x+4y+1*. SSRN 6993335, 3 pages, not peer-reviewed. Local PDF:
`literature/papers/021_Generalization-3x1-to-3x4y1.pdf`.

## What was tested

Proposes `x_{i+1}=3x_i+4y+1` (odd) / `x_i/2-y` (even), claiming every
orbit reaches `1-2y`. No proofs, only examples + a numerical sweep
("~640 billion points"). We tested:

1. Exact reproduction of the paper's 4 numerical examples.
2. Computational verification of the identity `z=x+2y` ⟺ standard
   Collatz.
3. Quantification of the redundancy in the "~640 billion" sweep.
4. Sample test (500 random cases) of the general claim.

## Result

Examples and the general claim are correct — but **not because it's a
real generalization**: the change of variable `z=x+2y` transforms the
proposed map exactly into standard Collatz (the same formula, symbol
for symbol), with the domain `x_0≥1-2y` being exactly `z_0≥1`. Not a
family of problems, but the same problem reparametrized. Quantified
consequence: the "~640 billion data points" tested cover, at best, ~2.4
million distinct instances of standard Collatz (not 640 billion
independent ones) — already covered by direct verifications published
in the literature (`2^68`–`2^71`).

## How to reproduce

```
python3 experiment.py
```

No dependencies beyond the stdlib. Runs in <0.1s.
