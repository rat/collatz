# E-115: Wirsching's microcanonical multiplicity

Related hypothesis: H-143.

This experiment computes Wirsching's generator counts `g_ell(k,a)`
exactly from equation (2.1) of his 2003 paper. At fixed `k`, their sum
over the `2*3^(ell-1)` unit residues is the number of bounded
compositions of `k` with coordinate capacities
`2, 6, 18, ..., 2*3^(ell-1)`. The script verifies this total at every
level.

The reported `min_over_mean` is precisely the finite-level quotient in
condition `(?3)`, minimized over the residue variable. The normalized
collision statistic equals one for a uniform distribution and its
excess over one is the squared L2 distance from uniform. The costs
tested are `k=ell+u*floor(sqrt(ell))` for `u=-1,0,1`.

Run:

```sh
python3 microcanonical_multiplicity.py --max-ell 12
python3 validate_canonical_decomposition.py
python3 support_threshold.py --max-ell 16 --k-max 30
```

The second command compares the canonical mixture bin by bin with the
independent E-100 Syracuse recursion through `ell=4`. The expected
maximum discrepancy is below `1e-14`.

The third command discards multiplicities and retains only Boolean
support. It extends the cumulative and fixed-cost covering thresholds
farther than the full count computation. Through `ell=16`, the first
fixed cost covering every residue is `ell+5` for `10<=ell<=16`. This
finite pattern is not an asymptotic claim.

The computation is a diagnostic. A finite minimum of zero does not
refute an asymptotic lower bound, and a positive finite minimum would
not prove one.
