# E-027 — H-007 corollary that closes H-008's even half

Related hypothesis: [`H-027-mod6-corollary-closes-h008-even-half.md`](../../hypotheses/H-027-mod6-corollary-closes-h008-even-half.md)

Origin: an attempt to close H-008's even half (N≡4 mod18), left pending
since H-022 with the (imprecise, see below) note that it was blocked by
depending on accelerated steps.

## What was tested

Whether even N with N/2 ≡ 2 (mod 3) — which, after a single halving
step, falls directly into the class already excluded by H-007 —
provides a valid exclusion for N.

## Correction during development

The first version of the script parametrized by j (N=18j+4, targeting
mod9/mod18 specifically) and tested only 300k cases of THAT subclass.
While reviewing the proof before reporting (consulting the advisor), it
became clear the derivation never uses mod9 — the real condition is
just N≡4 mod6, a class 3× broader. Rewritten to test the general class
N=6k+4 (k=1..500,000).

## Result

Zero exceptions in 500,000 cases. Confirms: for every N≡4 mod6,
P=2k+1<N has total_stopping_time(P) = total_stopping_time(N)+1. N can
never be a record holder.

Reproduce: `python3 experiment.py 500000`

## Honest assessment

This closes H-008 completely (the even half is the k=3j subcase of
this more general fact), but it is **not an independent new result** —
it's a corollary of a line of algebra about H-007. H-008's even half
was never structurally hard; it only seemed blocked because H-022
framed it in terms of accelerated steps (which indeed don't directly
reach even N), when a single simple halving already resolves it.

## Status of H-027 / H-008

**H-027 confirmed.** **H-008 is now FULLY RESOLVED**: H-022 (odd half,
new technique) + H-027 (even half, corollary) together exclude the
entire class 4 mod9 from record holders, with proof.
