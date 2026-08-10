# E-135: central-cost zeros and the quantitative half of Wirsching's (?3)

Related hypotheses: H-134 (dated section of 2026-08-09), H-162, H-163.

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
step recorded in H-163.

## Memory and runtime

The support run holds two `3^ell` arrays of 32-bit words during a level
transition plus a few `3^ell` Boolean arrays, so `ell = 18` needs about
5 GB. The last level took 117 s. The exact-count run holds two
`(k_max+1) x 3^ell` int64 arrays, so the `ell = 16` command above, whose
ceiling is `k_max = 28`, needs about 20 GB. Its last level took 96 s.
Both are single-threaded numpy. Lower `--offsets` to lower `k_max` and
the memory falls proportionally.
