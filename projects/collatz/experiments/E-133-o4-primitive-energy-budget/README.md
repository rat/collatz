# E-133: the l2 budget available to O4 (Regime 3)

Related hypotheses:
[`H-115`](../../hypotheses/H-115-tao-bivariate-extension-three-precision-regimes.md)
(three precision regimes, O4),
[`H-155`](../../hypotheses/H-155-multiscale-parseval-o5-o7.md)
(multiscale Parseval),
[`H-154`](../../hypotheses/H-154-primitive-fibre-energy.md)
(fresh-fibre energy identity),
[`H-162`](../../hypotheses/H-162-emparelhamento-bilinear-irmaos-sem-decaimento.md)
(the route this measurement leaves standing).

## What it measures

O4 asks for exponential control of the fine-frequency tail at linear
precision, after sublinear-conductor modes have been separated. The only
implementation the second-moment route supplies is a Cauchy-Schwarz bound
on the pairing of the two siblings' character sums, and the budget that
bound spends is the primitive Fourier energy of the Syracuse law above
the separated conductors. This script measures that budget directly.

For the Syracuse law `mu_ell` on `Z/3^ell Z`:

    K_ell = 3^ell * sum_x mu_ell(x)^2
    E_ell = sum over xi with 3 not dividing xi of |muhat_ell(xi)|^2
    sup_ell = max over the same xi of |muhat_ell(xi)|

`mu_ell` comes from the exact recursion of E-100, validated there bin by
bin against direct Monte Carlo at `ell = 3, 4`.

## Results (levels 1 to 15, exact up to double-precision rounding)

**(a) Three expressions for the primitive energy agree.** `K_ell -
K_(ell-1)` (the multiscale Parseval identity of H-155), the direct FFT
sum over primitive frequencies, and the fresh-fibre form of H-154 match
to `2.1e-15` at every level. H-155 and H-154 are therefore verified here
independently of E-124 and E-123, on the Syracuse law itself.

**(b) Sublinear-conductor separation removes a shrinking share of the
budget.** The fraction `(K_r - 1) / (K_ell - 1)` of total primitive l2
mass sitting in conductors at most `3^r`:

| ell | r = 3 | r = ell/2 |
|-----|-------|-----------|
| 8   | 0.408 | 0.526     |
| 10  | 0.330 | 0.521     |
| 12  | 0.276 | 0.517     |
| 14  | 0.238 | 0.514     |

Along any sublinear sequence the share falls; along `r = ell/2` it sits
at about one half. The residual `K_ell - K_r` grows linearly in `ell` in
both columns.

**(c) The primitive spectrum sits at, and above, the square-root scale.**
`E_ell` stays near `0.47` across the whole range: 0.4762 at `ell = 2`,
down to 0.4616 at `ell = 3`, then rising to 0.4708 at `ell = 15` with one
small reversal at `ell = 7`. So the RMS primitive coefficient stays
between `0.832` and `0.845` times `3^(-ell/2)`, with no trend that would
carry it off that scale. The maximum is far larger and grows against the
same scale:

| ell | sup * 3^(ell/2) | sup / rms | argmax xi |
|-----|-----------------|-----------|-----------|
| 5   | 2.02            | 2.4       | 32        |
| 10  | 9.30            | 11.1      | 54953     |
| 15  | 61.69           | 73.4      | 262144    |

The per-level ratio `sup_ell / sup_(ell-1)` drifts upward across the
range, from 0.6546 at `ell = 2` to 0.8513 at `ell = 15` (not monotone;
it dips at `ell = 9` and `ell = 12`), against the `3^(-1/2) = 0.5774`
that a uniform square-root bound would need. The maximizer
sits on the multiplicative orbit of `1` under doubling at almost every
level, which is where the support of `mu_ell` lives.

## Status of these numbers

Finite-level measurement, not proof. `K_ell` is nondecreasing (H-138), so
no finite range separates convergence from divergence; H-140 records that
correction and it stands here. What the range does show is the size and
the shape of the budget at the levels reachable, and both are far from
what the Cauchy-Schwarz implementation of O4 would need.

## Reproduce

```
python3 primitive_energy_budget.py
```

Runs to `ell = 15` in 12 s, peak resident memory 1.0 GB. Cost per level
grows by a factor of three, so do not raise `lmax` much without need.
