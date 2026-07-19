# E-079 — Review of Getachew, "Unfolding the Collatz Tree: An Indirect Structural Proof" (2025)

Related hypothesis: [`H-079-getachew-2025-review.md`](../../hypotheses/H-079-getachew-2025-review.md)

**FULL-PROOF CLAIM — REFUTED.**

## What was done

The paper (item 109) constructs the Collatz reverse tree — the same
construction as this project's H-018/E-018 — and claims to prove the
conjecture by showing the tree (1) covers every n∈ℕ, (2) is acyclic
except for the trivial cycle, and (3) every path back to the root is
finite.

## The central logical hole

The "parent" relation defined in the paper (Remark 1) is **identical
to the direct Collatz map**: parent(m)=m/2 (even) or 3m+1 (odd). So,
"path back to the root" IS the direct Collatz orbit. Lemma 4.3 (every
path back is finite) does not follow from "acyclic + unique parent" —
acyclicity and parent uniqueness guarantee the path doesn't repeat or
branch, but they **do not guarantee it's finite**. The lemma is
logically equivalent to the conjecture itself, presented as if it
followed from weaker structural properties.

Theorem 5.1 (coverage) suffers from the same problem via another route:
the indexing formula it sums is just the unique odd×power-of-2
decomposition of any integer — a universal arithmetic fact, independent
of any Collatz branching rule.

## Computational verification

We confirmed: (1) Theorem 5.1 is correct but tautological (independent
of g(n)); (2) parent(x)=f(x) exactly; (3) the number 27 is, in
principle, reachable from the root (its orbit's reverse path satisfies
the branching rule at all 111 steps), but a direct search from the root
(with no shortcut) doesn't find it within millions of processed nodes —
concrete evidence that "coverage" cannot be established by a
combinatorial argument like Theorem 5.1's, without directly verifying
Collatz.

## Result

Not a valid proof. See H-079 for the full analysis of the error's
anatomy (a disguised petitio principii, dressed up in graph-theory
language).

## Reproduce

```
python3 experiment.py
```
