# E-034 — Following up from the video: cycle equation and H-009 extension

Related hypothesis: [`H-034-video-cycle-equation-followup.md`](../../hypotheses/H-034-video-cycle-equation-followup.md)

## What was tested

Part 1: reproduces the specific finding from an informal video (n=13
for 3 multiplications + 5 divisions) with the correct, verified formula
(same as H-009/E-009).

Part 2: extends H-009 (which went up to a=14) beyond that, precisely
quantifying where the combinatorial explosion of compositions makes
brute force infeasible.

## Result

Part 1: **refuted** — no integer candidate exists for (a=3,S=5) in any
of the 6 orders. The video's finding doesn't hold up.

Part 2: complete, clean verification up to **a=16** (restricting to
S=S_min exactly). Beyond that, the combinatorics grow too fast
(billions of compositions per pair to test) for pure brute force.

Reproduce: `python3 experiment.py [A_MAX] [S_WINDOW] [MAX_COMPOSITIONS]`
(e.g. `python3 experiment.py 16 0 5000000` for the complete clean
search).

## Status of H-034

**Confirmed** — the video's finding is technically refuted; H-009
extended from a=14 to a=16 (narrower window); the combinatorial wall
precisely quantified, explaining why the professional literature
(Simons & de Weger) needs continued fractions + additional techniques,
not just more computational power.
