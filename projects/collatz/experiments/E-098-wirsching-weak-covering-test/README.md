# E-098 — Direct computational test of the Weak Covering Conjecture (Wirsching 1998)

Related hypothesis: [`H-114-wirsching-weak-covering-computational-test.md`](../../hypotheses/H-114-wirsching-weak-covering-computational-test.md)

## What was done

The first direct computational test (as far as we know) of Wirsching's
(1998, Ch. V) "Weak Covering Conjecture for Mixed Power Sums", the
conjecture open for ~30 years identified in H-112 as structurally
equivalent to the endogeny barrier's "missing ingredient" (H-110/
H-111). Implements a bitset DP with cyclic rotation to compute, for
each ℓ, the smallest j*(ℓ) such that R_{j-1,j} (mixed sums of powers of
2 and 3, the book's exact definition) covers every invertible residue
mod 3^ℓ.

## Result

j*(ℓ) exists and is finite for ℓ=1 to 17 (validated exactly against an
independent reference table). The asymptotic regime of the excess
e(ℓ)=j*(ℓ)-ℓ·log₄3 remains undetermined with 17 points (only the most
pessimistic fast-linear-growth scenario is rejected). See H-114 for the
full analysis.

## Reproduce

```
python3 experiment_wcc.py
```
