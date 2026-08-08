# E-129: does aggregation over the sibling gap cancel the fresh-digit coupling?

H-150/E-120 prove that for any FIXED sibling gap `delta`, the joint law
of the next `fresh` base-3 digits of two sibling coordinates is
maximally coupled: `TV(joint, product of marginals) = 1-3^-fresh`,
independent of `delta`. That refutes pairwise independence for a
single fixed pair. H-159 needs a different, weaker question: does the
dependence shrink once you average over the actual branching measure
on `delta` (E-108's `P(Delta=2k)=3*4^-k`), the way it would have to for
an aggregation-based route to an i.i.d.-tail transfer?

This script computes that aggregate joint exactly (finite sums, no
sampling) and reports its TV distance and mutual information against
the product of its own marginals, for a range of fresh depths and
truncation levels of the delta sum. It also documents a check that the
single-delta joint does not depend on which unit residue `x0` is used
as the reference point, so the aggregate is the correct conditional
law and not an artifact of one arbitrary choice.

Run:

```sh
python3 aggregate_fresh_digit_coupling.py --max-fresh 6 --k-max-list 3 6 10 16
```

## Result

The aggregate TV and mutual information stay close to the single-delta
values at every fresh depth tested (e.g. at `fresh=6`: single-delta
TV=0.998628, aggregate TV=0.992193 at `k_max=16`). Averaging over the
gap ensemble with its natural weight does not drive the dependence
toward zero.

## What this does and does not show

**Shows**: aggregation over the sibling-gap ensemble alone, measured in
total variation or mutual information, does not restore approximate
independence for a single fixed sibling pair. The naive route to
H-159 (average over `delta`, get a near-product joint, invoke
implicit renewal) does not work.

**Does not show**: that no aggregation-based transfer exists. Implicit
renewal does not need the joint close to a product in TV; it needs
control of a specific moment or Fourier/Mellin coefficient of the
aggregated sum. TV here is dominated by the fact that, for any fixed
`delta`, `y_block` is a deterministic function of `x_block`; TV is
forced close to 1 by that support structure regardless of whether the
coefficient implicit renewal actually needs happens to cancel. This
experiment also fixes two siblings from a common parent; the real tree
functional aggregates over many more pairs at once.

So E-129 rules out one specific naive strategy and narrows the target
for H-159 to a moment/Fourier functional of the aggregate, not a
distributional distance. It is not a structural counterexample against
transferability in general, and H-159 stays open.

## Verifying x0-invariance

```sh
python3 -c "
from aggregate_fresh_digit_coupling import single_delta_joint, tv_and_mi
print(tv_and_mi(single_delta_joint(4, 2, 3)))
"
```

then repeat with the residue-relabeled variant swapping which unit
`x0 mod 3^coarse` is used (checked by hand for coarse in {1,2,3} and
several deltas during this experiment): TV and mutual information are
identical across every unit residue tried.
