# E-026 — Divergence rate of finite 3-adic memory approximations

Related hypothesis: [`H-026-divergence-rate-independent-of-K.md`](../../hypotheses/H-026-divergence-rate-independent-of-K.md)

Origin: extension of H-024/E-024, item #15 from a fourth list of
external ideas.

## What was tested

Whether using more 3-adic digits (larger K) when approximating D(v) by
residue "holds up" longer (larger magnitude) before diverging from the
real value, compared to using fewer digits (smaller K).

## Bug found and fixed along the way

The first attempt used consecutive multipliers (m=0,1,2,5,...) with a
parity correction ("if v is even, add mod"). Since mod=3^K is odd and
the base residue is odd, an odd m followed by the correction could
collide with the raw v of the next even m (e.g. m=1 corrected gave
exactly the same v as m=2 uncorrected). Fixed by using only even
multipliers — guarantees odd v without needing a correction,
eliminating the collision.

## Result

Comparing K=4,6,8 over the same range of v's magnitude (not the same
multiplier m, which gives quite different scales per K): the
divergence |log(D(v)/D(v₀))| stays in the same order of magnitude for
all three K's. No evidence that a deeper residue delays the divergence.

**Caveat**: each point is a single measurement of a quantity already
known (H-024) to be extremely erratic — not a statistical average. A
suggestive result, not a robust one. See the hypothesis file for
details and the non-monotonicity observed within the same K.

Reproduce: `python3 experiment.py 18 4,6,8 0,2,4,10,20,50,100,200,400`
(requires E-018's `experiment.py` module on the relative path).

## Status of H-026

**Confirmed with a caveat** — real signal but not statistically
robust; averaging over multiple residues per (K, magnitude) is the
natural next step if this line is resumed.
