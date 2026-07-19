# E-039 — Explicit computation of Ruiz Castillo's residual pressure (item 001)

Related hypothesis: [`H-039-ruiz-castillo-geometria-residual-review.md`](../../hypotheses/H-039-ruiz-castillo-geometria-residual-review.md)

## What was tested

Paper #001 from the collection (`literature/papers/INDEX.md`) defines a
"residual pressure" P_RC(t) for the dissipation observable
φ(a)=a-log₂(3), but never computes it explicitly — the whole analysis
stays at the level of "IF P_RC is convex, THEN g_RC(t)≥0" etc. This
experiment computes P_RC(t), g_RC(t), and K_RC(t) explicitly for the
standard i.i.d. model (a ~ Geometric(1/2), already established in
H-001/H-011 of this project).

## Result

- Λ(t) [≡P_RC(t) up to sign convention] has a closed form:
  `t(1-log₂3) - log(2-eᵗ)`, domain t<log(2).
- Cross-check: Λ'(0)=2-log₂3≈0.415 and Λ''(0)=2 match exactly E[a]-log₂3
  and Var[a]=2, already established.
- g_RC(t)=2eᵗ/(2-eᵗ)² — strictly positive/convex over the whole domain
  (confirms, for the i.i.d. model, the hypothesis the paper only
  assumes formally).
- **Real singularity**: g_RC(t)→∞ as t→log(2)⁻ — the metric diverges
  exactly at the point where the geometric distribution's MGF stops
  converging (a direct consequence of the "2" in Geometric(1/2)).
- K_RC(t) = -2·g_RC(t) exactly (a closed relation specific to this
  model) — always strictly negative, never zero, unlike the paper's own
  conceptual U-shaped sketch (which is explicitly illustrative, not
  computed).

## Reproduce

`python3 experiment.py`

## Status

Supporting computation for H-039 — not a hypothesis tested in isolation
about the conjecture, it's an honest computational extension of a
reviewed external paper, done to fill the gap the paper itself leaves
(it never computes anything explicitly for the real problem).
