# E-012 — Predecessors of powers of 2

Related hypothesis: [`H-012-powers-of-2-predecessor-structure.md`](../../hypotheses/H-012-powers-of-2-predecessor-structure.md)

## Origin

Observation from the scientific director while exploring the Collatz
reverse tree: powers of 2 like 32 and 64 seem to behave differently —
some are only reached via the trivial doubling chain, others have an
extra branch.

## What was verified

2^k has a genuine odd predecessor (via 3m+1=2^k) if and only if k is
even, in which case the predecessor is exactly Σ_{i=0}^{k/2−1} 4^i
(always odd). Full proof in
`hypotheses/H-012-powers-of-2-predecessor-structure.md`.

## Result

Verified without exception for k=1 through 60. Reproduce:
`python3 experiment.py 60`.

## Status

**Confirmed.** Exactly explains the original observation: 2^5=32 (odd
k) has no odd predecessor — it's only reached by doubling 16 — while
2^6=64 (even k) has the odd predecessor 21 (3·21+1=64), an extra
branch in the tree.
