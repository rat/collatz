# E-009 — Search for non-trivial cycles (brute force, small scale)

Related hypothesis: [`H-009-nontrivial-cycles.md`](../../hypotheses/H-009-nontrivial-cycles.md)

## What was tested

Question from the scientific director: just as negative integers have
3 known cycles in the extended Collatz map, does an analogous
non-trivial cycle exist for positive integers? We searched directly via
the cycle equation (see `hypotheses/H-009-nontrivial-cycles.md`), for
number of "up" steps "a" from 1 to 14, brute-force enumerating
compositions of S (sum of valuations).

## Result

No genuinely new cycle found for a from 1 to 14 (within the covered
search window — some (a,S) combinations with a composition count above
3 million were skipped for computational cost, see the script's
output). The only "cycles" found were the trivial cycle (n0=1)
traversed "a" times in a row (b=(2,2,...,2)) — not new cycles, just the
same 1→4→2→1 cycle repeated.

Reproduce: `python3 experiment.py 14 3000000` (~57s).

## Honest limitations of this search

- It's simple brute force, not using the continued-fraction techniques
  Simons & de Weger (2005) used to rigorously prove there is no
  non-trivial cycle with up to **68** up-steps — a much stronger result
  than ours.
- Some (a,S) combinations with many possible compositions were skipped
  (see `skipped` in the output) — the search isn't 100% exhaustive for
  larger a within the tested window, though it covers the most likely
  combinations (S closest to the optimum a·log₂3, which have the
  fewest compositions and are most likely to yield a small n0).
- This is an **independent, own verification** of an already
  well-established result — not a new discovery. The value is having
  done the check ourselves, reproducibly, and understanding the
  mechanism (cycle equation via continued fractions of log₂3) rather
  than just citing the literature.

## Status of H-009

Consistent with the literature (Steiner 1977, Simons 2005, Simons & de
Weger 2005): no non-trivial cycle found in the tested range. Neither
refutes nor proves the conjecture — merely replicates, at smaller
scale, a result already rigorously established by others.
