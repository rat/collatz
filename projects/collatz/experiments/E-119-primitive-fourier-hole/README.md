# E-119: primitive Fourier spectrum of a one-hole unit law

For each `ell>=2`, the script takes the uniform distribution on the
units modulo `3^ell` after deleting one unit. It verifies:

- the coarse coefficient at frequency `3^(ell-1)` has modulus at least
  `1/2`;
- every primitive coefficient has modulus exactly
  `1/(2*3^(ell-1)-1)`.
- a non-full distribution lifted uniformly from the preceding modulus
  has every primitive coefficient equal to zero.

Run:

```sh
python3 primitive_hole.py --max-level 8
```

This is a finite check of the Ramanujan-sum calculation in H-149. The
proof in H-149 is exact and does not depend on the computation.
