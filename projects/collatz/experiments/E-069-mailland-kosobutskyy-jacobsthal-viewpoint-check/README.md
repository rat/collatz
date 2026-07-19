# E-069 — Verification of paper #084 (Mailland & Kosobutskyy, "Modelling the Collatz Problem from a Jacobsthal Viewpoint")

Related hypothesis: [`H-069-mailland-kosobutskyy-jacobsthal-viewpoint-review.md`](../../hypotheses/H-069-mailland-kosobutskyy-jacobsthal-viewpoint-review.md)

## Paper

Mailland, D. & Kosobutskyy, P. (2026). *Modelling the Collatz Problem
from a Jacobsthal Viewpoint*. Communications in Advanced Mathematical
Sciences, 8(1), 49-55, peer-reviewed. Local PDF:
`literature/papers/084_Modelling-Collatz-Jacobsthal-Viewpoint.pdf`.

A pedagogical version, restricted to κ=3, of the same framework as
paper #032 (same authors, reverse order) — see
[`E-063`](../E-063-jacobsthal-trees-check/) / [`H-063`](../../hypotheses/H-063-jacobsthal-trees-review.md).

## What was tested

This script does **not** duplicate E-063 (which already exhaustively
verified the general framework and this paper's two numerical examples
in its Part 8). It covers only what E-063 hadn't verified:

1. Eq. 5-8 (integrality/periodicity mod 3) — quick, independent
   reconfirmation.
2. Examples 1 and 2 of the paper — quick reconfirmation.
3. Fig. 1 — full reconstruction of the generating tree (columns θ=5
   and θ=1 expanded across several k, including the dead branches
   θ=3,21).
4. Fig. 2 — confirms the 10 columns shown in the Petri net are
   reachable from the root θ=1.

## Result

**0 failures across all 4 parts.** No mathematical error found.

## Methodology note

An initial visual reading of Fig. 1 incorrectly suggested nodes 57 and
229 were linked to 85; computational verification showed both actually
come from θ=43, not θ=85. Likely a figure transcription error (not the
paper's) — see H-069 for details. For this reason the script only
verifies the numbers themselves (all valid), not the exact adjacency of
each edge.

## How to reproduce

```
python3 experiment.py
```

No dependencies beyond the stdlib. Runs in under a second.
