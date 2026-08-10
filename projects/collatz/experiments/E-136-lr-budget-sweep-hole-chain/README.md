# E-136: the l^r budget family for O5, and the doubling structure of WCC holes

Related hypotheses:
[`H-164`](../../hypotheses/H-164-familia-lr-orcamento-anelado-o5.md),
[`H-165`](../../hypotheses/H-165-cadeia-duplicacao-buracos-wcc.md),
[`H-127`](../../hypotheses/H-127-reducao-z-number-dicotomia-espectral-wcc.md).

Two independent parts, both aimed at O5 (excluding a primitively
spectrally diffuse failure of the Weak Covering Conjecture). Part 1
asks whether a different norm closes the Jensen deficit of
Proposition C. Part 2 tests a support-side mechanism with no Fourier
budget in it.

## Part 1: `norm_sweep.py`

Same annealed model as
[E-101](../E-101-jensen-constant-annealed-fourier-budget/README.md):
`Z = sum_{g>=1} w_g e(U_g)`, `U_g` i.i.d. uniform, `w_g = p(1-p)^{g-1}`,
`p = 1/gamma`. A frequency of conductor `3^r` collects exactly `r` such
factors, so `|muhat(xi)| ~ |Z|^r` in the benchmark. E-101 supplies the
`r -> 0` endpoint (`exp(E log|Z|) = p`, the Jensen identity); this
script does not recompute it, it checks it.

A support hole forces `sum_{xi != 0} |muhat(xi)| >= 1`. Holder with
exponent `r >= 1` gives `||muhat||_{l^r} >= (3^ell-1)^{1/r-1}`, and the
annealed value of the left side is `3^{ell/r} ||Z||_r^ell`. The
criterion therefore closes if and only if

    ||Z||_r < 1/3.

Run:

```sh
python3 norm_sweep.py --samples 2000000 --threshold-samples 200000
```

Takes about two minutes.

### What it checks and what came out

Self-checks at `p_c = 1/gamma_c = 0.557886`, all passing:

- `||Z||_2` against the closed form `sqrt(p/(2-p))`, relative error
  `1.2e-4`;
- the `r -> 0` limit against `p` (Jensen), relative error `1.0e-4`;
- the pre-registered bracket `p <= E|Z| <= ||Z||_2`;
- monotonicity of `||Z||_r` in `r`.

| r | `\|\|Z\|\|_r` | deficit `D_r` | gamma threshold |
|---|---|---|---|
| 0 (Jensen) | 0.557830 | 1.8822 | 3.3079 |
| 0.5 | 0.575797 | 1.9902 | 3.7438 |
| 1 (l^1) | 0.592460 | 2.0987 | 4.1774 |
| 1.5 | 0.607812 | 2.2065 | 4.5860 |
| 2 (l^2) | 0.621902 | 2.3130 | 5.0000 |
| 3 | 0.646651 | 2.5200 | 5.8065 |
| 4 | 0.667506 | 2.7179 | 6.5986 |

`D_r = log 3 / log(1/||Z||_r)` is the factor by which the annealed
decay exponent falls short. The gamma threshold is the slope at which
that member of the family would start to work. The actual slope is
`gamma_c = 1.7925`.

Closed forms confirmed by the run: `||Z||_2^2 = p/(2-p)`, so the `l^2`
threshold is `p < 1/5`, that is `gamma > 5` exactly. The `r -> 0`
endpoint is `p` exactly, so its nominal threshold is `p < 1/3`, that is
`gamma > 3`.

Second table in the output: `Lambda(p) = E log(1/|Z|)` against
`log(1/p)`. They agree for `p >= 1/2` and separate below it, because
the Jensen identity needs `|Z'| <= p/(1-p)`. At `p = 1/3`,
`Lambda = 1.032 < log 3 = 1.0986`. The true `r -> 0` inversion slope is
therefore `3.31`, not `3`.

## Part 2: `hole_chain.py`

`S_j` is the image modulo `3^ell` of `sum_i 2^{alpha_i} 3^i` over
strictly decreasing exponent tuples bounded by `j+ell-1`, that is
`R_{ell-1,j}`. `H_j = U \ S_j`, and `j*(ell)` is the least `j` with
`H_j` empty. Raising every exponent by one costs one extra top slot,
so `2 S_j subset S_{j+1}`, hence

    H_{j+m} subset intersection_{k=0}^{m} 2^k H_j,

and a hole at stage `j+m` forces the whole halving chain
`b, b/2, ..., b/2^m` to be holes at stage `j`, giving
`|H_j| >= j*(ell) - j`.

The script computes `S_j` for all `j` at once by a dynamic program on
the least achievable largest exponent, then verifies every claim.

Run:

```sh
python3 hole_chain.py --max-level 10
```

Runs in well under a second.

### What came out

All checks pass for `ell = 2, ..., 10`: `S_j` sits inside the units,
`2 S_j subset S_{j+1}`, the halving chains are present, and
`|H_j| >= j*-j` holds.

| ell | j* | j*/ell | `\|H_{j*-1}\|` | `\|H_{j*-2}\|` | `\|H_{j*-3}\|` |
|---|---|---|---|---|---|
| 4 | 7 | 1.75 | 3 | 10 | 20 |
| 5 | 9 | 1.80 | 1 | 9 | 28 |
| 6 | 10 | 1.67 | 3 | 24 | 77 |
| 7 | 11 | 1.57 | 9 | 66 | 208 |
| 8 | 12 | 1.50 | 22 | 169 | 552 |
| 9 | 13 | 1.44 | 48 | 415 | 1430 |
| 10 | 15 | 1.50 | 2 | 90 | 968 |

The ratio `j*/ell` drifts down across this range, consistent with the
value near `1.2` reported in H-114 at larger scales.

The lower bound is close at `j = j*-1`, where it predicts one hole and
the counts are single digit at every level checked, `2` at `ell = 10`.
It is exponentially loose two or three steps below threshold, where
the counts already run into the hundreds against a bound of `2` or `3`.
So the doubling structure is a real constraint on the last few stages
before covering, and says essentially nothing before that.
