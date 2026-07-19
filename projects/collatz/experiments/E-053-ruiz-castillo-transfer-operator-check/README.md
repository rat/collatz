# E-053 — Verification of paper #013 (Ruiz Castillo, "Residual Transfer Operator")

## Goal

Verify "Operador de Transferencia Residual de Ruiz Castillo y teoría
espectral para la dinámica acelerada de la Conjetura de Collatz" (Juan
Carlos Ruiz Castillo, 47 pages). The fourth paper by this author
reviewed in the collection (after item 001/H-039, item 008/H-050, item
010/H-052). Introduces a formal transfer operator L_t over the full
symbolic space, then conjecturally motivates a restricted version
L_{RC,t} over the realizable space Σ_C, using classical spectral theory
(Gelfand's formula, Perron-Frobenius, spectral gap) to formulate three
explicit conjectures (Conjecture 6.6, 7.1, 8.4).

## Central finding — the first real error in this series of 4 papers

**Proposition 5.3 states `lim_{t→∞} L_t(1) = 0`**, but its own "proof"
derives the closed formula from Proposition 5.1,
`L_t(1) = e^{(log₂3−1)t}/(1−e^{-t})`, and since log₂3−1 ≈ 0.585 > 0,
this expression **diverges exponentially** as t→∞ — the exact opposite
of what the proposition states. The text itself acknowledges this in
the very next sentence ("crece exponencialmente cuando t → ∞"), but the
end-of-proof symbol (□) appears right after, without the "= 0"
statement being corrected or withdrawn.

We consulted `advisor()` before finalizing this finding. Assessment:
the calculation is correct and Proposition 5.3, as printed, is indeed
false — but the paper's own proof **correctly derives** the asymptotic
behavior (exponential growth) and even uses this observation to justify
the future need for normalization via "residual pressure". The author
understood the asymptotics; the defect is that the boxed formal
statement was never updated to reflect its own proof. This is a
**statement-vs-proof inconsistency** — the same category as the
labeling error already found in Pratiher (H-037), **not** a calculation
error by the author. For this reason it does not go into
`literature/unverified-proof-claims.md` (the paper doesn't claim to
prove Collatz).

## What we did

1. **Proposition 5.1** (closed formula for L_t(1)): confirmed — direct
   sum of the series (5000 terms) matches the closed formula for t ∈
   {0.1; 0.5; 1; 2; 5; 10}.
2. **Proposition 5.2** (positivity, L_t(1)>0 for t>0): confirmed.
3. **Proposition 4.2** (absolute convergence): confirmed — the
   difference between sums truncated at 1000 and 2000 terms is ~0 for
   every tested t.
4. **Proposition 5.3** (asymptotic behavior): **FALSE as printed** — we
   computed L_t(1) for t=1 through t=200: the sequence is strictly
   **increasing** (2.84 → 6.4×10⁵⁰), not decreasing to 0.

## Containment of the error

We confirmed that Proposition 5.3 is a preliminary calculation in
Section 5, about the **unrestricted** symbolic space (with no Collatz
arithmetic constraints). No later result in the paper (Sections 6-8,
about the **restricted** operator L_{RC,t} on Σ_C, all explicitly
conjectural) cites or depends on the numerical value of L_t(1). The
error doesn't compromise the rest of the paper, which remains honest
about its scope: "los resultados obtenidos no constituyen una
demostración de la Conjetura de Collatz."

## Result

The first real error found across the four Ruiz Castillo papers
reviewed so far (H-039, H-050, H-052 were all "elementary but
correct"). The rest of the apparatus (Gelfand's formula, spectral
radius positivity, logarithmic equivalence) is standard functional
mathematics, correctly applied; the three central conjectures
(Conjecture 6.6, 7.1, 8.4) are honestly labeled as conjectures, not
theorems.

See `hypotheses/H-053-ruiz-castillo-transfer-operator-review.md`.

## How to run

```
/home/rat/.venv/bin/python3 experiment.py
```
