# E-127: worst Syracuse cylinder

This experiment extends the direct computation of

```text
c_ell = min_(3 does not divide a) mu_ell(a)
```

without running the much larger fixed-cost dynamic program from E-111.
It reports the minimizing residue, its discrete logarithm to base `2`,
whether it lifts the preceding minimizer, and a descriptive power fit
for `3^ell*c_ell`.

Run:

```sh
python3 scan_worst_cylinder.py --max-level 15
```

The distribution recursion is imported from E-111.  Its base cases and
small levels were previously checked against exact values and direct
enumeration.  The power fit is a diagnostic only and is not used as an
asymptotic conclusion.
