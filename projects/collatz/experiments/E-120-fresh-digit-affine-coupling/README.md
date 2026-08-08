# E-120: affine coupling of fresh sibling digits

For several sibling gaps and coarse precisions, the script enumerates
all `3^s` lifts of one affine residue class and computes the joint law
of the next `s` base-3 digits of the two coordinates. It verifies

```text
TV(joint, product of marginals) = 1-3^-s
mutual information              = s*log(3).
```

Run:

```sh
python3 fresh_digit_coupling.py --max-fresh 6
```

The identities are proved algebraically in H-150. The enumeration
checks the residue orientation and carry handling.

