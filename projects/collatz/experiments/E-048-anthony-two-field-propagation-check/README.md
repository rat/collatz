# E-048 — Verification of paper #006 (Michael Mark Anthony, "A Two-Field Propagation Model for the Collatz Map")

## Goal

Verify "A Two-Field Propagation Model for the Collatz Map" (Michael
Mark Anthony, Enertron Inc., 17 pages). An elaborate paper, with heavy
mathematical apparatus (Riemann P-equation, monodromy, PGL(2,C),
digamma function, hypergeometrics, 24 Kummer solutions) — but honest
and explicit, in several sections, about not extending known results
nor proving the conjecture.

## What we did

We computationally verified the central checkable claims:

1. **Möbius reformulation Φ(n)=1/(n+1)** (Proposition 5.1): confirmed
   in 4999 cases — M_E and M_O exactly reproduce Φ(T(n)).
2. **Theorem 8.1** (the m=1 regime doesn't persist indefinitely):
   longest run found up to n=200,000 was 16 steps; the explicit
   construction n₀=2^(t+1)-1 sustains exactly t steps as predicted by
   the theorem's own 2-adic induction proof.
3. **Worked example from Section 9** (n=7): trajectory confirmed
   exactly.
4. **Theorems 10.3/10.4** (exact harmonic identity H_q=ψ(q+1)+γ and the
   Euler-Mascheroni limit): confirmed via `mpmath` (50 digits of
   precision) — standard digamma-function facts, not specific to
   Collatz, but correctly used.
5. **Hypergeometric identity from Eq.28** (ψ(z)=(z-1)·₃F₂(1,1,2-z;2,2;1)-γ):
   confirmed numerically for several z.

## Result

**No error found** in any testable claim. The paper is remarkably
careful throughout the ENTIRE text (Remarks 5.2, 6.1, 10.1, 11.1, 12.1,
14.1, and the whole of Section 16) in distinguishing: what is a proven
theorem about the reformulation; what is a structural analogy, not a
literal identification ("this is an analogy of form, not of kind");
what is heuristic/conditional (the "Collapse Theorem" 14.1 is
explicitly labeled "conditional...consistent with, but not a proof of,
the conjecture"); and where there is no extension of known results
(Section 12, about Tao's result). The author himself identifies and
corrects, within the text, an earlier mistaken claim (δ_m=1/m, Section
10) — a sign of careful research practice.

Much of the apparatus (P-equation, monodromy, PGL(2,C), digamma,
hypergeometrics, Kummer) functions more as decorative context/analogy
than as mathematical content with real weight on the conjecture — the
paper itself agrees with this reading (Section 16).

See `hypotheses/H-048-anthony-two-field-propagation-review.md`.

## How to run

```
/home/rat/.venv/bin/python3 experiment.py
```

Requires `mpmath` (already installed in the project's venv).
