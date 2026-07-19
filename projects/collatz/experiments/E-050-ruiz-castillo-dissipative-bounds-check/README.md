# E-050 — Verification of paper #008 (Ruiz Castillo, "Dissipative Bounds and Residual Decomposition")

## Goal

Verify "Dissipative Bounds and Ruiz Castillo Residual Decomposition in
the Accelerated Dynamics of the Collatz Conjecture" (Juan Carlos Ruiz
Castillo, University of San Carlos of Guatemala, 44 pages). The second
paper by this author reviewed in the collection (the first was item
001, H-039). Does not claim a proof: "The present work does not claim
to assert a final proof of the Collatz Conjecture."

## What we did

We computationally verified all central propositions/theorems:

1. **Exact affine identity** U^k(n)=(3^k n+B_k(n))/2^{A_k(n)} and the
   closed formula for B_k(n) (Propositions 3.1/3.3): confirmed exactly
   for 44 values of n × 6 values of k.
2. **Residual decomposition** U^k(n)=2^{L_k(n)}n+R_k(n) (Theorem 4.3):
   confirmed.
3. **Non-existence of exact equilibrium** (Proposition 2.14): confirmed
   (a sanity check, already guaranteed by unique factorization).
4. **Order sensitivity** (Proposition 5.5): confirmed that the words
   (1,3) and (3,1) — same sum A₂=4 — give R₂=5/16 and R₂=11/16
   respectively, exactly as the paper states.
5. **Universal bound** R_k(n)≤(3/2)^k−1 (Proposition 7.1): confirmed.
6. **Descent criterion** (Theorem 8.7): confirmed — with an important
   note below.

## Integrity note: false positive on the first attempt

The first verification of Theorem 8.7 using `2**(k*log2(3)-A_k)` via
Python floating point found 3 "failures", all at n=1 (the fixed point,
where U^k(1)=1 for every k). We investigated before reporting it as an
error: using exact arithmetic (`2^{L_k(n)} = 3^k/2^{A_k(n)}`, an exact
fraction, avoiding floating-point `log2(3)`), the 3 "failures"
disappear — they were a rounding artifact right at the inequality's
threshold (where both sides exactly equal n), not an error in the
paper. The theorem is correct; the bug was in our verification code,
fixed before reporting.

## Result

**No real error found.** The paper is mathematically correct in
everything we verified, but the content is entirely **elementary**: the
"exact affine identity" is the same standard "unrolling" of the
accelerated map that appears (under different notation) in several
other already-reviewed papers (Fu-Liu-Wang E-044, Mohammed E-045), and
the "dissipative bounds" are elementary geometric series.

**Zero real numerical content**: both of the paper's figures are
explicitly labeled "conceptual... does not represent real computational
data" — the same pattern as this author's first paper (H-039: "zero
numerical content, the single figure explicitly conceptual").

**Citation pattern**: 4 real external references (Lagarias ×2,
Wirsching, Tao) and 12 self-citations by Ruiz Castillo himself (75%
self-citation) — the list reveals ~12 other papers with nearly
identical titles already written by the same author about the same
"residual decomposition", a strong indication that the other Ruiz
Castillo papers still in the queue (items 010, 013, 017, 020) will
follow the same pattern.

See `hypotheses/H-050-ruiz-castillo-dissipative-bounds-review.md`.

## How to run

```
/home/rat/.venv/bin/python3 experiment.py
```
