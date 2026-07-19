# E-061 — Verification of paper #029 (Alic, "Collatz Progressions Reframed")

Related hypothesis: [`H-061-alic-p2er-review.md`](../../hypotheses/H-061-alic-p2er-review.md)

## Paper

Alic, N. (2026). *Collatz Progressions Reframed: Exponent
Representation, Algorithmic Hierarchies, and Record Computations*. IEEE
Access, vol. 14, peer-reviewed. Local PDF:
`literature/papers/029_Collatz-Progressions-Reframed.pdf`. An
algorithms/engineering paper — makes no mathematical claim about
Collatz.

## What was tested

The central P2ER algebra (representing `n` as a vector of exponents of
powers of 2; odd step = concatenation+consolidation via binary carry;
even step = block shift):

1. Odd step vs. direct `3n+1` — 500 random trajectories (`n` up to 4000
   bits), 20,000 steps tested.
2. Even step vs. direct repeated division — 500 cases.
3. The paper's own numerical example (Figure 1, `n=15`, full 17-step
   sequence).
4. "Waiting line" and "end-gap" examples (p. 5).

## Result

**Algebra confirmed correct in every test**, including exact
reproduction of every numerical example in the paper. Gives confidence
that the comparative benchmarks (PASA/REN/UPX/ACCEL/POW2BASIC) measure
correct implementations of the Collatz map. The "record computation"
(`2^{1,024,001}-1`, 13.8 million steps) was not reproduced —
computationally infeasible in this session (the paper itself took hours
on a 56-core/512GB RAM machine).

## How to reproduce

```
python3 experiment.py
```

No dependencies beyond the stdlib. Runs in a few seconds.
**Implementation note**: the first version of this script used a naive
`consolidate()` function (O(n²), rescanning the entire histogram on
every carry) that hung with the original parameters (n up to 4000
bits, 500 trials) — rewritten to a single linear scan (O(exponent
range)) before actually running it.
