# E-022 — Partial proof of H-008 via a multiplicative (2-step) relation

Related hypothesis: [`H-022-mod9-multiplicative-exclusion.md`](../../hypotheses/H-022-mod9-multiplicative-exclusion.md)

## What was tested

After H-015/H-016 failed (they searched for M=N−k, an additive shift,
which could never isolate mod 9), we tried a **multiplicative**
construction: M such that 2 accelerated steps from M lead exactly to N.
Solving the congruence for N≡4 (mod 9), we found the simplest
solution: valuations (a,b)=(1,2), giving M=(8N−5)/9.

## Result

For N=18j+13 (the **odd** half of N≡4 mod9), M=16j+11 always satisfies
M<N, and the chain M→M₁→N (2 accelerated steps, exact valuations 1 and
2) holds for every j — **verified without exception for j=0 to
100,000** (N up to ~1.8 million).

Confirmed that 0 of the 148 official record holders are ≡13 mod18
(consistent with the proof) and also 0 are ≡4 mod18 (the even half,
not yet proven).

**Confirmed novelty**: of 1000 tested cases, 750 (75%) were not already
covered by H-007 (mod3=2) or H-014 (mod8=5) — not a disguised
rediscovery.

Reproduce: `python3 experiment.py 100000`.

## What's missing

The **even** half of N≡4 mod9 (N≡4 mod18) cannot be excluded by the
same technique — accelerated steps only reach odd numbers, so an even N
is never the direct "target" of a chain from another M. Would need a
different argument. Remains an open question (but also empirically
never observed among the 148 real record holders).

## Status of H-022

**Confirmed** (odd half of H-008 rigorously proven). H-008 (the
original, complete question) is now **partially resolved**: half
proven, half (even) still open.
