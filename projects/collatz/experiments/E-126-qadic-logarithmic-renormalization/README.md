# E-126: q-adic logarithmic collision renormalization

For each tested odd prime `q`, put `d=ord_q(2)` and assume the order
lifts maximally, equivalently `2^d != 1 mod q^2`.  The script compares
the direct geometric Syracuse recursion with

```text
K_ell = sum_m W_(q,d)(2*pi*m/q^(ell-1)) |A_m|^2,

W_(q,d)(theta)
 = q*(4^d-1)
   / (3*(4^d+1-2^(d+1)*cos(theta))).
```

Here `A_m` is the Fourier transform of the preceding law after the
permutation `j -> (2^(d*j)-1)/q mod q^(ell-1)`.

Run:

```sh
python3 verify_qadic_renormalization.py --max-level 5
```

The default primes exhibit several distinct values of `ord_q(2)` and
include cases where `2` is not a primitive root modulo `q`.
