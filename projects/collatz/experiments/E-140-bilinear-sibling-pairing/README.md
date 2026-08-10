# E-140: bilinear pairing between sibling subtrees (H-163)

**Correction notice (2026-08-10, same session as the original run):**
this experiment's original conclusion was wrong. An independent
critique found, and a second independent check (mine, not just reading
the critic's numbers) confirmed, that the measured "cancellation"
carries no sibling-specific information: two controls with no real
relationship to the sibling pair (a random frequency dilation; an
unrelated, far-away root) reproduce the same ratios. See "Corrected
result" below and H-163's closure for the full analysis. Nothing here
is deleted; the original method, the error, and the correction are all
kept on record.

## What this was meant to test

H-163 prescribes a cheap first check: does the bilinear pairing

```
Cov(xi) ~ sum_{xi != 0} S_1(xi) * conj(S_2(xi))
```

between the two subtrees hanging off a common fixed node `v` in the
reverse Syracuse tree (q=3) show phase cancellation, where `S_i(xi)` is
the character sum over admissible depth-`D` continuations below
sibling `i`, weighted by the real branch weight `prod_j 2^{-a_j}` (not
renormalized), evaluated at the leaf's residue mod `3^ell`?

Siblings are the two smallest admissible first-step exponents at `v`.
The gap `alpha_2-alpha_1` is usually 2, but not for every root: `v=17`
gives `alpha_1=1, alpha_2=5` (gap 4), because the further exclusion
`w%3==0` can skip a candidate. Do not assume gap 2 without checking.

## How to run

```
python3 bilinear_pairing.py --roots 1 5 7 11 17 25 --depths 2 3 4 5 6 7 8
python3 bilinear_pairing.py --roots 1 5 --depths 6 8 --controls
```

`--max-exp` caps the admissible-exponent search range per step
(default 14); results are stable to within about 1% between
`max-exp=14` and `max-exp=20` (not bit-identical -- an earlier version
of this README overstated this as "identical").

## Method notes

- `enumerate_subtree_fast` tracks residues at modulus `3^(ell+
  remaining)` through the reverse recursion so every division by 3
  stays exact, vectorised with numpy over each full tree level, with
  per-level deduplication of repeated residues (`np.unique` +
  `np.bincount`). Without the per-level dedup, intermediate arrays grow
  with the raw branching factor instead of being capped by unique
  residues, which used over 20GB resident before being caught and
  fixed (see H-163 for the incident).
- `character_sum_from_hist` builds `S(xi)` as an FFT of the weighted
  residue histogram, not a direct double loop over `(path, xi)`; this
  is what makes depth 8-14 tractable.
- `enumerate_subtree_slow` (individual Python path objects, no
  vectorisation, no big-modulus trick) is kept only as the reference
  implementation the fast path is checked against
  (`_check_fast_matches_slow`, run at import time, must pass before
  anything else runs).
- `control_dilation` / `control_unrelated_root` are the two controls
  that overturned the original conclusion; kept as permanent parts of
  this experiment, not a one-off patch.

## Corrected result (2026-08-10, second pass after a critique round found the first correction was itself wrong about the mechanism)

By Parseval, `measured = m*<h1,h2> - m1*m2` (`m=3^ell`, `h_i` the
weighted residue histogram, `m_i` its total mass). `h1`, `h2` have FULL
support (every residue coprime to 3, verified with `(h>0).sum()`:
4374/6561 at ell=8, 354294/531441 at ell=12, identical support size for
both siblings; an earlier version of this README wrongly called the
supports "sparse", off by five orders of magnitude). What is small is
the PARTICIPATION RATIO (`m_i^2/sum(h_i^2)`, an effective-atom count,
roughly 11-85 in the cases measured), a different statistic. The
unrenormalized branch weight concentrates most mass onto a handful of
heavy residues within the full support, and the two siblings' heavy
residues rarely coincide: `m*<h1,h2>/(m1*m2)` measures 0.03-0.5 in the
cases checked (not ~0; `v=17,ell=4` is an exception at 5.8), enough
that `measured` is usually dominated by `-m1*m2` without a
sparse-support argument. `ratio_CS`, `ratio_RP` reduce to a function of
the two subtrees' participation-ratio structure, carrying no phase
information.

Confirmed with two controls (`--controls`), each replacing sibling 2 by
something with no real relationship to sibling 1. A single random
dilation draw is noisy (the same cell read anywhere from 0.04 to 0.11
across draws in an earlier interactive check); `control_dilation_median`
reports the median of 5 draws with recorded seeds. Persisted output,
not regenerated ad hoc, in `controls_ell8_10_12.txt`:

```
v    ell   ratio_RP(real)   ratio_RP(dilation-control, median of 5)   ratio_RP(unrelated-root)
1     8         0.1304                    0.0680                              0.0822
1    10         0.0559                    0.0487                              0.0406
1    12         0.0359                    0.0480                              0.0343
5     8         0.0961                    0.1011                              0.1467
5    10         0.0523                    0.0511                              0.0897
5    12         0.0337                    0.0296                              0.0429
11    8         0.1147                    0.1185                              0.0624
11   10         0.0513                    0.0541                              0.4688
11   12         0.0363                    0.0205                              0.0139
17    8         0.1377                    0.1224                              0.1218
17   10         0.0432                    0.0881                              0.0837
17   12         0.0165                    0.0443                              0.3207
```

Real siblings and both controls cover the same range at every depth
tested; in two cells (`v=11,ell=10` and `v=17,ell=12`) the unrelated-root
control is far larger than the real value, strengthening rather than
weakening the conclusion. The original pre-registered decision rule was
also, on reflection, unfalsifiable:
its "no cancellation" branch (measured near `sqrt(E1*E2)`) requires
`h1` proportional to `h2`, which two genuinely different subtrees
essentially never satisfy for `ell>2` -- so the "cancellation" branch
was the only reachable outcome regardless of any real phase relation.

**What this experiment does NOT establish**: neither presence nor
absence of real phase cancellation in the object H-115/H-126 actually
define (Tao's idealised decomposition `mu_ell = sum_j 2^{-j}
mu_ell^{(j)}`, spread over all unit residues mod `3^ell`, with the
coarse affine modes of H-126 Prop. 2 removed before summing). The
depth-truncated real-integer subtree used here is a different, nearly
atomic object, and the Parseval argument above applies to it for
essentially structural reasons unrelated to arithmetic. See H-163's
closure for the corrected recommendation if this line is retomed.

Not mirrored in `collatz-endogeny` (not yet cited by any paper text).
