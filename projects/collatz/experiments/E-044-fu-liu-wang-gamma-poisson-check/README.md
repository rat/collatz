# E-044 — Verification of paper #018/019 (Fu, Liu & Wang — Gamma/Poisson)

## Goal

Independently verify the paper "Emergence of Gamma-Type Upward-Phase
Statistics in the Collatz Map: An Effective Poisson Process Mechanism"
(Fu, Liu & Wang, arXiv:2606.26811) — item 019 of `INDEX.md` (local file
numbered `018_...pdf`, one of the 15 downloaded). Unlike CTUHSK
(H-043), **this paper does not claim to prove the conjecture** — it
proposes a heuristic mechanism (Poisson process + geometric 2-adic
valuation) to explain why N↑ (number of Syracuse steps until reaching
1) approximately follows a Gamma distribution.

## What we did

1. Confirmed E[h]=2, Var(h)=2 for the 2-adic valuation (already
   established in H-001/H-011 — a calibration point).
2. Tested the paper's Eq.6 (an approximate closed formula linking N↓ to
   X0 and N↑, inherited from ref.[19] of the same group) against the
   exact simulated N↓, for every odd X0 from 3 to 200,001 — including
   the classically long orbit of X0=27 (41 accelerated steps).
3. Reproduced (at a much smaller scale than the paper: L=10⁴ and 10⁵ vs
   their 10⁵–10¹⁵) the central verification — empirical mean and
   variance of N↑ compared to the theoretical predictions θ_T=2/(2−log₂3)²
   and K_T=(2−log₂3)/2·(1+log₂L).
4. Manually checked, term by term, the algebra of the cycle-closure
   condition (Eqs.30-34).

## Result

- **Eq.6 matches exactly in 99999/99999 (100%) of tested cases**,
  including X0=27 — our initial hypothesis that the approximation would
  break down for long orbits was wrong; the formula is more robust than
  we expected.
- **Mean of N↑** matches the corrected prediction (Eq.37) to ~2% at
  L=10⁴ and 10⁵ — the same precision order the paper itself reports.
- **Empirical θ (~10.6) is ~8.5% below θ_T=11.61** at these scales.
  This is **not an error in the paper** — the paper itself shows θ only
  approaches the theoretical value slowly as L grows, and even at
  L=10¹⁵ the fitted value (11.245) is still ~3% below theoretical.
  Since we don't have the computational budget to replicate L=10¹⁵, a
  larger gap at our smaller scales is expected, in the right direction
  — a confirmation with honestly limited scope, not a discrepancy.
- **The cycle-closure condition's algebra (Eqs.30-34) is correct** — we
  verified every step of the derivation by hand. Unlike CTUHSK
  (H-043), this paper is **explicit and correct** in stating that this
  asymptotic obstruction does NOT prove the nonexistence of
  non-trivial cycles — it textually acknowledges that the finite
  correction 1/Xn cannot be rigorously ruled out.

**No error found.** See
`hypotheses/H-044-fu-liu-wang-gamma-poisson-review.md`.

## How to run

```
/home/rat/.venv/bin/python3 experiment.py
```

No external dependencies (only `math` and `collections` from the
standard library — we did not use scipy, which isn't installed in the
project's venv; the Gamma fit was done by the method of moments,
sufficient for comparison with the paper's own theoretical
predictions).
