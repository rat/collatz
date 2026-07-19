# E-054 — Verification of paper #017 (Ruiz Castillo, "Residual Gibbs Measures")

## Goal

Verify "Medidas de Gibbs Residuales de Ruiz Castillo y estados de
equilibrio en la dinámica acelerada de la Conjetura de Collatz" (Juan
Carlos Ruiz Castillo, 62 pages). The fifth paper by this author
reviewed in the collection (after item 001/H-039, item 008/H-050, item
010/H-052, item 013/H-053). Introduces "Residual Gibbs Measures"
assigning thermodynamic weights to realizable cylinders via
`μ_t([ω]_C) ≍ exp(tL(ω) − kP_RC(t))`, using the same fundamental
identity `S_k(φ)(ω) = −L(ω)` as always.

## What we did

We computationally verified every concrete, checkable
proposition/theorem/corollary:

1. **Proposition 1.1** (U(n) well-defined, odd→odd): confirmed.
2. **Proposition 1.3** (logarithmic interpretation L_k=log₂(3^k/2^Ak))
   and **Corollary 1.4** (L_k<0 ⟺ 2^Ak>3^k, via exact `Fraction` to
   avoid floating-point false positives near the threshold — a lesson
   already applied in H-050/E-050): confirmed.
3. **Theorem 3.6 / Proposition 1.5** (fundamental identity
   S_k(φ)(ω)=−L(ω)): confirmed — 39×5 cases, 0 failures.
4. **Proposition 2.6** (symbolic semiconjugacy π(U(n))=σ(π(n))):
   confirmed.
5. **Proposition 2.11/2.13** (partition by realizable cylinders):
   confirmed (a finite check, no ambiguity).
6. **Proposition 9.1** (Gibbs-residual equivalence, pointwise event
   identity): confirmed.

## Result

**No real error found** — unlike item 013 (H-053, which had a
**false** Proposition 5.3, contradicted by its own proof), this paper
returns to the "elementary but correct" pattern of H-039/H-050/H-052.
Every concrete derivation is correct (a trivial algebraic rewriting of
the same fundamental identity as always), and every genuinely open
result is honestly labeled **"Conjecture"**, not "Theorem" or
"Proposition":

- Conjecture 7.3 (residual quasi-Bernoulli property)
- Conjecture 8.4 (Gibbs implies residual equilibrium)
- Conjecture 9.3 (Gibbs–large-deviations duality)
- Conjecture 10.4 (residual Gibbs dimension formula)

**No directly testable empirical consequence** (unlike item 010/H-052):
this paper's conjectures deal with the **existence** of a family of
measures μ_t that is never explicitly constructed — unlike item 013's
transfer operator, which had a closed formula over the unrestricted
space and allowed direct numerical testing. There is no computable
statistic on real trajectories to directly test these existence
conjectures, so we did not write an empirical "Part 2" for this paper.

**Stylistic note (not an error)**: Proposition 4.4 ("normalizing
interpretation") is argued rhetorically/informally, without an
effectively checkable quantitative bound — but, unlike item 013's
Proposition 5.3, it makes no concrete numerical claim that is false.

See `hypotheses/H-054-ruiz-castillo-gibbs-measures-review.md`.

## How to run

```
/home/rat/.venv/bin/python3 experiment.py
```
