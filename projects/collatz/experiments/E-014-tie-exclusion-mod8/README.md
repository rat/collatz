# E-014 — Tie exclusion: record holders are never ≡5 mod 8

Related hypothesis: [`H-014-tie-exclusion-mod8.md`](../../hypotheses/H-014-tie-exclusion-mod8.md)

## What was tested

For N=4u+1 with u odd (N≡5 mod 8), whether total_stopping_time(N) =
total_stopping_time(N−1) exactly (a tie from trajectory coalescence —
full proof in `hypotheses/H-014-tie-exclusion-mod8.md`), and whether no
official record holder falls into this class.

## Result

- Identity σ(N)=σ(N−1) confirmed without exception in 200,000 random
  cases.
- **None of the 148 official record holders (OEIS A006877) is ≡5 mod
  8.**

Reproduce: `python3 experiment.py 200000 1`

## Status

**Confirmed.** The project's second residue-class exclusion technique
(the first was H-007, via strict domination; this one is via an exact
tie).
