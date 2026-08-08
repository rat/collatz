# E-122: linear-block nonequivalence

This experiment computes the total-variation distance between the
canonical law of the terminal folded-cost block and its law conditional
on the total cost `K_ell=k`. The finite probabilities use the exact
folded geometric caps. Negative-binomial coefficients replace repeated
convolution only where every cap exceeds the largest requested sum, in
which range the coefficients are identical.

For `r/ell -> rho` and `(k-ell)/sqrt(ell) -> u`, H-153 predicts the
Gaussian limit

```text
TV(N(rho*u, 2*rho*(1-rho)), N(0, 2*rho)).
```

Run:

```sh
python3 linear_block_tv.py
```

The default run uses `u=0`, levels 100, 200, 500, and 1000, and
`rho=1/4,1/2,3/4`. It checks normalization of both finite laws. The
experiment validates the limiting calculation; the theorem uses the
lattice local central limit theorem.

The folded-sum coefficient routine was cross-checked against direct
variable-by-variable convolution for start indices 0 through 3, block
lengths 1 through 8, and every sum through 40. The maximum discrepancy
was below `2e-14`.
