# E-031 — Systematic scan of untested primes

Related hypothesis: [`H-031-prime-modulus-scan.md`](../../hypotheses/H-031-prime-modulus-scan.md)

## What was tested

Whether any prime p≠2,3 (5,7,11,13,17,19,23), or higher power of 3 (27,
81), shows any empty residue class among the 148 real record holders
that isn't already explained by H-007/H-014/H-022/H-027/H-008.

## Result

No new exclusion. Primes 5-23: no class with a low count. Mod 27: the
only low-count class is the base case n=2. Mod 81: 3 classes with count
0 unexplained, but this is **less** than expected by pure chance (~13
classes, computed via Poisson) — noise, not signal.

Reproduce: `python3 experiment.py`.

## Status of H-031

**Confirmed (clean negative)** — a genuine check (result not
predictable a priori), no new finding. Reinforces that the known
exclusion family (primes 2 and 3 only) is complete at the small moduli
tested.
