# E-124: multiscale Parseval decomposition

For compatible probability laws `mu_ell` modulo `3^ell`, the script
checks

```text
K_ell-K_(ell-1)
 = sum_(3 does not divide xi) |mu_ell_hat(xi)|^2,

K_ell
 = 1 + sum_(r=1)^ell sum_(3 does not divide xi)
                       |mu_r_hat(xi)|^2.
```

It uses two independent compatible sequences:

- the Syracuse laws from the E-100 recursion;
- random Dirichlet refinements whose three children sum exactly to each
  parent mass.

Run:

```sh
python3 multiscale_parseval.py --max-level 12
```

The theorem is an exact partition of the character group by conductor.
The computation checks indexing, normalization, and compatibility.
