# E-021 — Erosion of terminal runs of 1s

Related hypothesis: [`H-021-terminal-run-erosion.md`](../../hypotheses/H-021-terminal-run-erosion.md)

## What was tested

(a) Erosion rule: n ending in a run of t≥2 ones gives valuation a=1 and
a result with run t−1. (b) Comparison of the average length of a=1 runs
between official record holders and typical orbits.

## Result

(a) **Confirmed without exception** in 50,000 tests, t from 2 to 20.

(b) Record holders: 13,741 runs, mean=**2.512**. Typical orbits: 4,744
runs, mean=**2.035** (matches almost exactly the theoretical prediction
under H-001: E[run]=1/(1−0.5)=2, since the run of consecutive a=1's,
under i.i.d. geometric(1/2), is itself geometric with stopping rate
0.5).

## Interpretation (with a tautology caveat)

Record holders have systematically longer runs of ascent (a=1) than
typical. This is plausible but **partly tautological**: having an
exceptionally high stopping time almost by definition requires longer
periods of slow descent (a=1 = ascent, contributes less to the drop).
We do not treat this as a new discovery — it is consistent with (and
perhaps reducible to) the very mechanism already characterized in
H-002/H-004.

Reproduce: `python3 experiment.py 50000`.

## Status of H-021

**Confirmed** (erosion mechanism, part a) and **supported with a
tautology caveat** (record-holder vs. typical run difference, part b)
— not presented as a new discovery.
