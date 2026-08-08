# E-123: primitive Fourier energy and fresh fibres

The script checks the exact identity

```text
sum_(3 does not divide xi) |mu_hat(xi)|^2
 = 3^(ell-1) sum_b [(x_0-x_1)^2+(x_1-x_2)^2+(x_2-x_0)^2],
```

where `x_t=mu(b+t*3^(ell-1))`. It compares the two sides for random
integer count vectors and also checks that a uniform lift from the
preceding modulus has zero primitive energy.

Run:

```sh
python3 primitive_fibre_energy.py --max-level 8
```

For integer counts it also checks the sharp consequence that any
nonuniform fibre produces a primitive coefficient of magnitude at least
the reciprocal of the total count. The proof is Parseval and does not
depend on floating-point computation.
