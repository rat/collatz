# E-113: finite checks for Wirsching Conjecture 1

The script independently constructs the coefficients

```text
P_ell(z) = product_j (1-z^c_j)^(-1),
Q_ell(z) = product_j (1-z^c_j)/(1-z),
```

and verifies coefficient by coefficient that
`P_ell(z)Q_ell(z)=(1-z)^(-ell-1)`. It also reports finite convolution
tail fractions and checks the elementary `exp(C log^2 m)` upper bound
for the infinite coin system through `m=1000`.

Run `python3 check_generating_identity.py`.

The computation is a diagnostic. The proof is the generating-function
cancellation and tail estimate recorded in H-133.
