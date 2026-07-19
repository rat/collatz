# E-047 — Verification of paper #003 (Jonathan S. Gilbert, "A Collatz-Equivalent Map on the Nonzero Integers")

## Goal

Verify "A Collatz-Equivalent Map on the Nonzero Integers" (Jonathan S.
Gilbert, preprints.org, 14 pages). The paper does **not** claim to
prove the conjecture ("No proof of the conjecture is claimed; the aim
is a coordinate system in which its dynamics are easier to see").

## What we did

We reimplemented the accelerated map T, the bijection J between the
relevant residue classes [1]₃∪[2]₃ and the nonzero integers Z*, the
conjugate map K, and the accelerated map K̂ (which contracts runs
through negative even integers). We independently tested:

1. **Conjugation K=J∘T∘J⁻¹** (Theorem 5): confirmed in 1000 cases.
2. **Pruning of multiples of 3** (Lemma 2/Theorem 4): confirmed up to
   n=20000 — no n outside [0]₃ maps into it, and every orbit starting in
   [0]₃ exits within ≤v₂(n)+1 steps and never returns.
3. **"Equivalent conjecture"** (Theorem 6): confirmed in 4999 cases (the
   J/K translation correctly preserves which orbit converges — not a
   test of the conjecture itself, only of the translation's
   correctness).
4. **Accelerated map K̂** (Lemma 4) and the paper's own example
   (n=-160 → K̂(n)=608, Remark 5): confirmed exactly.
5. **Parent formula** (Proposition 3): confirmed via brute-force graph
   search, for several k.
6. **Proposition 4** (algebraic identity between two expressions via
   lifting-the-exponent, and connection to OEIS A254046): confirmed —
   the two formulas agree with each other, with the direct parent
   count, **and with the real sequence A254046** (see note below).

## Note on OEIS access

The first attempt to confirm OEIS sequence A254046 used `WebFetch` on
`oeis.org` — the site blocked the automated access (403), the same
pattern seen with other hosts in the project. On the scientific
director's suggestion, we redid it via `curl` with a browser User-Agent
(`curl -s -A "Mozilla/5.0 ..." https://oeis.org/A254046/b254046.txt`),
which works without being blocked on this site (see memory
`feedback_oeis_access_method.md`). **The real sequence confirms exactly**
the paper's formula — Proposition 4 correct in every tested aspect.

## Result

**No error found** in any tested claim. A high-quality paper — the same
standard of honesty and rigor as H-042 (Williams) and H-044 (Fu/Liu/
Wang): carefully distinguishes what is a proven theorem from what is an
equivalent (weaker) conjecture and from what is analogy/heuristic
(Section 7, explicitly labeled as such, "by itself it proves nothing").

See `hypotheses/H-047-gilbert-collatz-equivalent-map-review.md`.

## How to run

```
/home/rat/.venv/bin/python3 experiment.py
```
