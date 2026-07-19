# E-071 — Review of Andrei & Masalagiu, "About the Collatz conjecture" (1998)

Related hypothesis: [`H-071-andrei-masalagiu-review.md`](../../hypotheses/H-071-andrei-masalagiu-review.md)

## What was done

Computational verification of the paper's central results (item 101 of
the collection, `literature/papers/101_About-the-Collatz-Conjecture.pdf`):

1. Theorem 3.1 (shortcut formula for 2p consecutive steps) — 458 cases,
   0 failures.
2. Lemma 4.1 (simple explicit family) — 21 cases, 0 failures.
3. Theorem 4.2 (general explicit family) — 110 cases, 0 failures, after
   fixing a parenthesis-precedence error in our own first attempt to
   reimplement the formula.
4. Theorem 3.2 part (1) (lower bound Racc≥1.5) — 99,998 cases, 0
   failures.
5. Theorem 3.2 part (2) (upper bound Racc≤i) — **refuted**, 5
   counterexamples up to n=10,000.
6. Conjecture 2 (asymptotic limit=3, not proven by the paper) — tested
   up to n=2^16-2^17, consistent with slow convergence to 3.

## Result

See H-071 for the full verdict. Summary: a correct and honest paper for
the most part, with one real contained error — Theorem 3.2 part (2) has
a missing proof (an unproven sentence) and is refutable with small
counterexamples (smallest: n=5).

## Reproduce

```
python3 experiment.py
```

No command-line arguments — the search limits (max_p, max_t, n_max,
max_power) are fixed in the code, chosen to run in under a minute.
