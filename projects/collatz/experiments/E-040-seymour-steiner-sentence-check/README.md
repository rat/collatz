# E-040 — Verification of Theorem 5.1 from paper #004 (Seymour, Steiner Sentence Length)

Related hypothesis: [`H-040-seymour-steiner-sentence-length-error.md`](../../hypotheses/H-040-seymour-steiner-sentence-length-error.md)

## What was tested

Paper #004 (`literature/papers/004_First-Principles-Derivation...pdf`)
proves, with a claimed formal verification in Lean 4/Mathlib, that
P(Steiner sentence length = k) = 3^(k-1)/4^k, and explicitly argues
against the "naive" model P(k)=(1/2)^k. We reimplemented the paper's
exact definitions (Def 1.2, 1.3, Theorem 2.1) from scratch to verify
independently.

## Result

- **Theorem 2.1 (mod-8 transition matrix) — CONFIRMED** exactly, by
  directly sampling 200,000 random odd integers.
- **Theorem 5.1 (3^(k-1)/4^k distribution) — REFUTED**. Direct
  simulation (300,000 samples, following the paper's own Appendix B
  protocol exactly) matches **(1/2)^k** — exactly the "naive" model the
  paper argues is incorrect — and **not** 3^(k-1)/4^k.
- **Concrete counterexample, exact arithmetic** (no randomness): n=68567
  (≡7 mod8) → S(n)=102851 (≡3) → S(S(n))=154277 (≡5). The residue
  sequence [7,3,5] matches the regex `(7*3)?(1|5)` as **a single
  Steiner word**, ending in 5 — i.e., a sentence of length 1 with
  b₀≡7, **not** b₀≡5. This directly contradicts the paper's proof of
  Theorem 5.1, which counts **only** b₀≡5 as the source of length-1
  sentences.

## Diagnosis of the error (see H-040 for full details)

The recursion in Sections 3–5 of the paper applies Syracuse's
ONE-STEP transition matrix (Theorem 2.1) as if it were the
entry-to-entry transition between consecutive WORDS. This is valid for
entries 1 and 5 (which are always exactly 1-step words), but **not**
for entries 3 and 7 (which span 2+ steps): `P[3][5]=1/2` and `P[7][3]`
(followed by the 3→5 step) describe the **very terminal of the current
word**, not the entry of a "next word". By treating it as always a
transition to the next word, the paper never "spends" the probability
mass that should close the sentence right there, underestimating the
real closing rate (1/2 per word, not the 1/4 rate implicit in the
formula 3^(k-1)/4^k).

## Reproduce

`python3 experiment.py` (~1s, no external dependencies)

## Status

Important finding: the paper's central theorem appears to be incorrect,
despite the claimed formal verification in Lean 4/Mathlib. We don't
have access to the Lean code to pinpoint the exact line, but the
evidence (confirmed transition matrix + exact-arithmetic counterexample
+ large-scale simulation) is strong and reproducible.
