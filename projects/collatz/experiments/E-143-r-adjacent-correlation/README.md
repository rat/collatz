# E-143: is R_ell(k) correlated with R_ell(A(k))? (H-176)

H-176 tested whether H-166's convex-combination identity (`R_ell` is a
window average of `R_{ell-1}` along the `A`-orbit) explains the
decorrelation E-132 measured for a different quantity (the joint tail
of `N`/`W` at consecutive units). The hypothesis's own pre-registered
counter-argument: overlapping-window averages classically correlate
nearby points, not decorrelate them.

## How to run

```
python3 r_adjacent_correlation.py
```

## Result

```
ell   corr(R(k),R(A(k)))   corr(R,shuffled)
 4          0.4014             -0.0645
 6          0.5041              0.0660
 8          0.5103             -0.0021
10          0.5297             -0.0084
12          0.5393             -0.0030
14          0.5457              0.0010
```

`R_ell(k)` and `R_ell(A(k))` are positively correlated (0.40 to 0.55,
increasing and flattening with `ell`), against approximately zero for a
random permutation of the same values. Exactly the counter-argument the
hypothesis predicted.

## Verdict, and its correct scope (added after a critique round)

`fechada-refutada` for H-176 as literally stated. This is a bulk
Pearson correlation over the whole distribution of `R`, and it refutes
that specific pre-registered question. It does **not** rule out joint
deep-tail anti-concentration at a scaled threshold `exp(-eps*ell)`,
which is what Q2 (H-161) actually needs; a positive bulk correlation is
compatible with the deep tails still decorrelating. The claim "os dois
fenômenos não têm o mesmo mecanismo, pelo motivo mais simples possível"
in an earlier version of H-176 overstated this: the correct scope is
that the pre-registered bulk-correlation test failed for the stated
reason, not that H-166's identity is proven irrelevant to E-132's
deep-tail effect in general.

Not mirrored in `collatz-endogeny` (not yet cited by any paper text).
