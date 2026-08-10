# E-135: central-cost zeros and the quantitative half of Wirsching's (?3)

Related hypotheses: H-134 (dated section of 2026-08-09), H-167, H-168.

Wirsching (2003) reduces uniform positive predecessor density to a chain
of five conditions. Conjecture 2 is the step `(?4) => (?3)`, where

```text
(?3)  g_ell(k_ell, a) >= mu * gbar_ell(k_ell)
      for every unit a, every ell >= ell_0, and every sequence
      (k_ell) with |ell - k_ell| <= delta*sqrt(ell),
```

and `(?4)` is a statement about the one-dimensional averaging operator
`W_3` that never mentions the generators. Since `k_ell = ell` is an
admissible sequence for every `delta > 0`, a single unit residue with
`g_ell(ell,a) = 0` at one level `ell >= ell_0` falsifies `(?3)`.

This experiment separates the two independent halves of `(?3)`.

## `central_zeros.py`: the support half

Exact Boolean support of `g_ell(.,a)` for every residue modulo `3^ell`
and every cost up to a ceiling, packed one bit per cost into one word
per residue. Reports the zero set at cost exactly `ell`, the least cost
whose support covers every unit, and the coherent subtree of residues
whose truncations are central-cost zeros at every earlier level.

```sh
python3 central_zeros.py --max-ell 18
```

Through `ell = 18` the zero set is never empty and the least fully
covering cost is `ell + 5` for every `ell` from 10 on, extending the
pattern E-115 saw through 16. At `ell = 18` there are 11,540,739 zeros
among 258,280,326 units and 734,754 coherent ones. A coherent subtree
that stayed nonempty at every level would produce, by the inverse limit
of nonempty finite sets, a 3-adic `alpha` that is a central-cost zero at
every level, refuting `(?3)` and `(?2)` at that `alpha`. Its growth
ratio falls from 2.17 to 1.79 over the last four levels, so it plausibly
goes extinct near `ell = 24` and no compactness argument will be
available. Both directions are extrapolation.

The packed table is audited against the independent backward predicate
of E-121 at every level through 7, and the smallest coherent witnesses
of each level are rechecked against the same predicate at every earlier
level.

## `central_ratio.py`: the quantitative half

Exact integer counts from the same recursion, reporting

```text
min_{a in S} g_ell(ell+d, a) / gbar_ell(ell+d)
```

for a range of offsets `d`, and separately for a fixed set of integers
`a` that does not grow with `ell`. Every row total is checked against
the independent count of bounded compositions of `k` with capacities
`2, 6, 18, ..., 2*3^(ell-1)`, which is Wirsching's identity
`2*3^(ell-1)*gbar_ell(k)`.

```sh
python3 central_ratio.py --max-ell 15
python3 central_ratio.py --max-ell 16 --offsets 0 5 12 --sqrt-multiples 1
python3 central_ratio.py --max-ell 16 --offsets 5 --sqrt-multiples 1 \
    --fixed-offset 5 --random-fixed 1458 --random-bound 2187
```

Minimum over all units, at offsets where the support is already
complete, decays geometrically in `ell`: at `d = +12` it falls from
0.4805 at `ell = 6` to 0.2555 at `ell = 16`, a factor near 0.94 per
level that is the same on both halves of the range. The offset would
have to grow linearly in `ell` to compensate, and Wirsching's window
allows only `d <= delta*sqrt(ell)`. So the infimum over `Z_3^x` that
`(?3)` demands stabilises nowhere in the window, not only at `k = ell`
for lack of support.

Minimum over a fixed set of integers behaves differently. At `d = +5`,
over all 486 units below `3^6`, the ratio reads 0.102, 0.147, 0.134,
0.138, 0.131, 0.140 for `ell = 10..15`: flat. Over all 1458 units below
`3^7` it reads 0.102, 0.074, 0.107, 0.079, 0.116, 0.108, 0.096 for
`ell = 10..16`, and over all 4374 units below `3^8` it reads 0.051,
0.074, 0.081, 0.079, 0.102, 0.097, 0.088: also flat. Over all 54 units
below `3^4` it sits near 0.22.

The minimum over all units modulo `3^ell` is the minimum over integers
`a < 3^ell`, and that is not evidence about `liminf_ell` at any fixed
`a`, because the residue attaining it has an integer representative of
size `3^ell`. What the tables establish is that at fixed `a` the ratio
does not deteriorate with `ell`; the decay of the all-unit minimum is
the growth of the index set. Separating that from a genuine decay of the
left tail needs quantiles rather than the minimum, which is the next
step recorded in H-168.

## `central_quantiles.py`: is the minimum's decay extreme-value statistics?

Fixed quantiles of the same distribution `g_ell(k,a)/gbar_ell(k)` over
unit residues, `k = ell + d`, run through `ell = 16`:

```sh
python3 central_quantiles.py --max-ell 16 --offsets 5 12 \
    --quantiles 1e-4 1e-3 1e-2 1e-1 0.5
```

A quantile does not carry the extreme-value confound of a minimum: the
value below which a fixed *fraction* of the population falls does not
mechanically shrink just because the population grows. H-168 states the
test directly: if a low quantile stays flat in `ell` while the minimum
falls, the minimum's decay is extreme-value statistics of a growing
index set; if the quantile also falls, the left tail is deteriorating
for real.

The two offsets return opposite verdicts by that test. At `d = +5`
(support complete from `ell = 10`), `q = 10^-3` reads 0.102, 0.110,
0.107, 0.118, 0.116, 0.107, 0.104 for `ell = 10..16`: flat, while the
minimum over the same rows is noisy and small (0.02-0.07) with no clear
trend. The criterion reads extreme-value statistics. At `d = +12`
(support complete from `ell = 4`), `q = 10^-4` falls from 0.402 at
`ell = 10` to 0.276 at `ell = 16`, a factor near 0.94 per level, close
to the minimum's own decay rate at that offset. The criterion reads
real tail deterioration. Neither offset is more authoritative than the
other; both are legitimate members of Wirsching's window
`|ell - k_ell| <= delta*sqrt(ell)`, and the disagreement between them is
itself the finding, not noise to average away (H-171, opened from this
run).

Part of the `d = +12` decay is bulk drift rather than tail pinching:
the median (`q = 0.5`) also falls, from 1.011 at `ell = 10` to 0.953 at
`ell = 16`, so `gbar_ell` is pulled up by the right tail relative to
the bulk. Normalizing `q = 10^-4` by the median instead of by 1 still
decays at close to the same 0.94/level rate, so bulk drift is not the
whole story at `d = +12`. At `d = +5` the same normalization makes the
already-flat `q = 10^-4` column rise slightly (0.053 to 0.093 over
`ell = 10..16`), the opposite direction. The `q = 10^-4` column is the
4th order statistic at `ell = 10` (`n_units = 39366`, so `10^-4` picks
index 3) and is min-contaminated there; read its trend only from
`ell >~ 13`.

Full data (`ell`, `d`, `n_units`, quantiles `1e-4/1e-3/1e-2/1e-1/0.5`,
min) in `quantiles_ell16.log` in this folder.

## Resolving the `d`-sensitivity: an offset grid (H-171)

`central_quantiles.py --max-ell 16 --offsets 6 7 8 9 10 11` (plus
`--thresholds` and `--bucket-quantile`, added to the script alongside
this run) settles which offset is the outlier. Every `d` from 6 to 11
decays at a rate close to `d = +12`'s (0.93-0.96 per level on
`q = 10^-3`); `d = +5` is the one that stays flat. `d = +5` is not a
generic point in the window: it is exactly the first cost with
complete support at each level (`central_zeros.py`'s own boundary,
`ell + 5` for every `10 <= ell <= 18`), so its distribution is
dominated by residues whose count has only just left zero, a boundary
regime distinct from `d >= 6` where support has been complete for
several levels already. Full data in `quantiles_grid_ell16.log`.

## What the population tail decay is made of: bottom-bucket composition

`central_quantiles.py` also reports, for the bottom `10^-3` bucket of
the unit population at each level, what fraction of those residues has
an integer representative below `3^8 = 6561` (a "small", fixed-in-`ell`
integer by the standard of the fixed-set columns above). That fraction
falls from about 0.5 at `ell = 9` to 0.0002-0.0007 at `ell = 16`, at
every offset tested (`d = 5` through `12`). The population's low tail
is, at the levels that matter, almost entirely new residues whose
integer representative only exists from that level on, not any small
fixed integer getting worse. This is the mechanism reconciling the
population decay above with the fixed-set flatness below: the group
grows and keeps injecting bad new residues: no evidence surfaces of any
already-existing small `a` deteriorating. Full data in
`quantiles_thresholds_ell16.log`.

## Extending the fixed-integer test to `ell = 17`

`central_ratio.py --max-ell 17 --offsets 5 12 --sqrt-multiples 1
--fixed-offset 5 --random-fixed 1458 --random-bound 2187` (peak memory
~39 GiB, checked live against free RAM before launch, since a dense
`(k_max+1) x 3^17` array is close to the edge on this machine). The
minimum over the same exhaustive 1458 integers below `3^7` at `d = +5`
reads 0.102, 0.074, 0.107, 0.079, 0.116, 0.108, 0.096, 0.089 for
`ell = 10..17`: seven levels, no bend at the new one either. Full
table in `ratio_ell17.log`.

## Escalation: does H-166's cascade transfer here? (Regra 11b)

A structurally different result in this project (H-166, unrelated to
Wirsching's `g_ell`) proves `min_u N_ell(u)/N_(ell-1)(...)` is a convex
combination of the previous level's ratios, giving monotonicity and a
bound certified at every higher level from one finite computation. An
external model (Codex, high reasoning effort) was asked whether the
same mechanism applies to `R_ell(k,a) = g_ell(k,a)/gbar_ell(k)`. It
does not, with a derivation and an explicit counterexample rather than
a bare assertion:

- Dividing the `extend` recursion by `gbar_ell(k)` gives weights whose
  sum over the admissible `j`'s for a fixed `a`, `S_ell(k,a)`, is **not**
  identically 1; only its average over `a` is (a Haar identity, not a
  pointwise one). Exact counterexample at `ell = 3, k = 3`:
  `S_3(3,a) = 9/7, 12/7, 6/7, 6/7, 3/7, 6/7` for `a = 1,2,4,5,7,8 mod 9`.
  H-166's mechanism worked because its denominator transforms under the
  *same* operator as its numerator, pointwise; here it does not.
- The diagonal `k = ell + d` is not preserved by the one-step recursion
  (`k - j = (ell-1) + (d+1-j)` mixes many offsets), so any bound this
  route gives for `min_a R_ell(ell+d,a)` degenerates to zero.
- `min_a R_ell` is not even monotone at small levels: exact fractions
  `m_ell = 9/28, 648/1459, 2430/5057, 13851/30695` for `ell = 4..7`
  (matching this project's own floating-point values independently),
  rising then falling.
- What does survive is a genuine convex combination of full probability
  *vectors* across residues, which yields convex-functional bounds
  (entropy, norms), not a positive coordinate minimum.

No route from the composition-counting recursion alone, without new
input, currently closes H-168 either way. See `HYPOTHESES` H-168's
2026-08-10 section for the full writeup and closure as
`closed-inconclusive`.

## Memory and runtime

The support run holds two `3^ell` arrays of 32-bit words during a level
transition plus a few `3^ell` Boolean arrays, so `ell = 18` needs about
5 GB. The last level took 117 s. The exact-count run holds two
`(k_max+1) x 3^ell` int64 arrays, so the `ell = 16` command above, whose
ceiling is `k_max = 28`, needs about 20 GB. Its last level took 96 s.
`central_quantiles.py` holds the same shape of array, so its memory
scales the same way with `--max-ell` and the largest `--offsets` value.
The `ell = 17` extension of `central_ratio.py` peaked at about 39 GiB
RSS (checked live against free system RAM before launching, since this
machine runs other unrelated jobs concurrently); `ell = 18` at the same
`k_max` would need roughly 90 GiB and was not attempted. Both scripts
are single-threaded numpy. Lower `--offsets` to lower `k_max` and the
memory falls proportionally.
