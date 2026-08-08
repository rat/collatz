# E-125: logarithmic collision renormalization

This experiment checks the exact one-level identity

```text
K_ell = sum_m 15/(17-8*cos(2*pi*m/3^(ell-1))) * |A_m|^2,
```

where `A_m` is the unnormalized Fourier transform of

```text
a_j = mu_(ell-1)((4^j-1)/3 mod 3^(ell-1)).
```

The direct side is computed with the original Syracuse recursion from
E-100.  The spectral side independently permutes the preceding law,
takes its FFT, and applies the closed multiplier.  The same comparison
is also performed for independent random preceding laws through level
8, so the check is not restricted to the Syracuse trajectory.

Run:

```sh
python3 verify_logarithmic_renormalization.py --max-level 12
```

The computation checks the indexing and normalization.  The identity
itself follows algebraically from the two-step recursion along the orbit
of `2` modulo `3^ell`.
