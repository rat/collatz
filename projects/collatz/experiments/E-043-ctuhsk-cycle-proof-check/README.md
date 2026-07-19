# E-043 — Verification of the "CTUHSK proof" (collection paper #016)

## Goal

Independently verify the central claim of the paper "Collatz-
Thwaites-Ulam-Hasse-Syracuse-Kakutani (CTUHSK) Theorem: Convergence of
Collatz (3n+1) Sequence to the Trivial Cycle Proved" (KP Bikarnakatte /
Dr. Keshava Prasad Halemane, engrxiv.org preprint, 35 pages) — which
claims a complete proof of the Collatz Conjecture.

## Structure of the paper's "proof"

1. **Necessary condition** (Section 10.1): shows that H^s (the
   component of framework H connected to the sink node BEL(1), i.e. to
   the trivial cycle {4,2,1}) satisfies the Dedekind-Peano axioms and is
   therefore order-isomorphic to N.
2. **Sufficient condition** (Section 10.2): argues, by contradiction,
   that no extra cycles (H^∞) nor divergent chains (H^&) exist — i.e.,
   that H^s = H (domain exhaustion).

## What we did

- Reimplemented the paper's basic structures (Syracuse map, mod-6
  classification of odd numbers, predecessor formula) and confirmed
  the preliminary structural facts (Eqn.7, 8, 9) are correct: multiples
  of 3 indeed have no predecessor at all; numbers of type (6m-1) indeed
  have a valid predecessor `(n·2^v - 1)/3` for every odd exponent v.
- Reproduced exactly the paper's own numerical example (k=2, n=11,
  predecessor 7 via v=1) and confirmed the arithmetic.
- **Central finding**: for n=11, infinitely many valid predecessors
  exist (one per odd v: 7, 29, 117, 469, 1877, ...), but the paper uses
  only the v=1 one to "prove" that a hypothetical cycle containing 11
  as the minimal element of type (6m-1) leads to a minimality
  contradiction (since 7<11). This doesn't generalize: for v≥3, the
  predecessor is LARGER than 11 (29, 117, ...), and so would violate no
  minimality at all. The paper never argues why the actual predecessor,
  within the hypothetical cycle/chain, would have to be specifically
  the v=1 one.
- Confirmed algebraically (not just for n=11) that this is a general
  pattern: `pred(v=1) = (2n-1)/3 < n` and `pred(v=3) = (8n-1)/3 > n` for
  every n>0 of type (6m-1) — not a coincidence of the example the paper
  chose, it's an algebraic property of any n of that form.
- Confirmed that Section 10.2.2 (divergent chains H^&) uses "the same
  argument" (the paper's own words) and suffers from exactly the same
  flaw (tested with n=5, k=1).

## Result

**The "proof" has a decisive logical hole in the sufficient
condition**, the only part that would carry real mathematical content
(the necessary condition is tautological — H^s is defined as whatever
reaches the trivial cycle). See
`hypotheses/H-043-ctuhsk-halemane-proof-flaw.md` for the full analysis.

## How to run

```
/home/rat/.venv/bin/python3 experiment.py
```

No external dependencies (uses only the standard library's
`fractions`).
