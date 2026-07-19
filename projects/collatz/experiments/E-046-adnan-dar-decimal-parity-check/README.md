# E-046 — Verification of paper #002 (Adnan & Dar, "Decimal-Parity-Based 3n+1 Mapping")

## Goal

Verify "Behavior of a Decimal-Parity-Based 3n+1 Mapping" (J. Adnan,
S.A. Dar — Global Journal of Pure and Applied Mathematics, 2026). The
paper does **not** claim to prove/refute the original Collatz
Conjecture — it proposes an ad hoc extension to decimals in (0,1) and
concludes it diverges.

## What we did

1. Reproduced all the paper's numerical examples (Tables 1-2, Examples
   1-3, the 5-step chain from Section 6) with exact arithmetic
   (`fractions.Fraction`) — all match.
2. Tested whether the "parity via last significant digit" rule is
   defined for numbers without a finite decimal expansion (1/3, 1/7,
   √2/10).
3. Tested 200 random decimals in (0,1) under the paper's rule.

## Result

**The paper's arithmetic is correct** — no calculation errors in the
examples.

**Conceptual problem at two levels**:
1. The "parity" rule is only defined for decimals with a finite
   expansion — a **countable** (measure zero) subset of (0,1). The
   "Mathematical Law" in the paper's conclusion ("for every n∈(0,1),
   the limit diverges") is a statement about the continuum, but isn't
   even well-defined for almost every real number in the domain it
   claims to cover (trivial counterexamples: 1/3, 1/7, any
   irrational).
2. Even restricted to finite decimals, the divergence is a trivial
   artifact (confirmed: 200/200 random decimals diverge within 30
   steps) — it follows from applying a "parity" with no algebraic
   relation to the numeric value to an additive constant (+1) never
   normalized relative to the (0,1) domain's scale. Unlike the real
   Collatz map, where 3n+1 is always even for odd n by algebraic
   construction (guaranteeing structural, not arbitrary, division),
   there is no analogous mechanism here — the divergence is expected by
   construction, not a discovery.

See `hypotheses/H-046-adnan-dar-decimal-parity-review.md`.

## How to run

```
/home/rat/.venv/bin/python3 experiment.py
```
