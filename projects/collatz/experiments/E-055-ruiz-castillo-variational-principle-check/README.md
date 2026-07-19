# E-055 — Verification of paper #020 (Ruiz Castillo, "Residual Variational Principle")

## Goal

Verify "Principio Variacional Residual de Ruiz Castillo y formalismo
termodinámico para la dinámica acelerada de la Conjetura de Collatz"
(Juan Carlos Ruiz Castillo, 58 pages). The sixth paper by this author
reviewed in the collection (after item 001/H-039, item 008/H-050, item
010/H-052, item 013/H-053, item 017/H-054). Proposes unifying residual
debt, residual drift, residual pressure, dissipative entropy, large
deviations, and dissipative dimension under a single variational
principle `P_RC(t) = sup_{μ∈M_RC}{H_RC(μ) − tD_RC(μ)}`. Does not claim
to prove Collatz.

## Character of the paper

Mostly **abstract convex analysis** (sup of affine functions is convex,
subgradients, Legendre–Fenchel duality) applied to `P_RC(t)` and
`I_RC(x)` — classic textbook facts, correctly derived, but with no
additional Collatz-specific content (M_RC and its measures are never
explicitly constructed, as in item 017/H-054).

## What we did

**Part 1 — concrete Collatz-specific identities** (all confirmed, 0
failures):
1. Proposition 1.2 (multiplicative interpretation of residual debt:
   2^{L_k(n)}=3^k/2^{A_k(n)}, and the sign criterion via exact
   `Fraction`).
2. Proposition 2.5 / Corollary 2.6 (symbolic semiconjugacy and
   forward invariance).
3. Proposition 3.3 (local classification of the potential via a₀:
   a₀=1⟹φ<0, a₀≥2⟹φ>0).
4. Proposition 3.4 / Theorem 3.5 / Corollary 3.6 (ergodic sum and
   the fundamental identity — the same one as always, verified once
   more for this specific paper).

**Part 2 — toy verification (not Collatz-specific)** of the convex
analysis apparatus: we generated 20 random affine lines, defined
`P(t)=sup_i F_i(t)`, and numerically confirmed (200 pairs `(t1,t2,λ)`)
that the convexity inequality holds — confirms that
Proposition 5.4/6.2 (sup of affines is convex) was correctly applied.

## Result

**No real error found.** Every concrete identity is a trivial, correct
rewrite. The abstract convex-analysis apparatus is standard mathematics
correctly applied. Where the derivation is only formal/structural
(Proposition 8.6, pressure–rate duality), the text itself explicitly
admits it: *"Este razonamiento no constituye por sí solo una
demostración completa del principio de grandes desviaciones para la
dinámica determinista real de Collatz."* Every genuinely open result
(Conjecture 7.6 existence of equilibrium measures, Conjecture 10.1
Residual Triangle) is honestly labeled "Conjecture", not
"Theorem"/"Proposition".

Unlike item 013 (H-053), no statement-vs-proof inconsistencies. Returns
to the "elementary but correct" pattern of most reviewed Ruiz Castillo
papers.

See `hypotheses/H-055-ruiz-castillo-variational-principle-review.md`.

## How to run

```
/home/rat/.venv/bin/python3 experiment.py
```
