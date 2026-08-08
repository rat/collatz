# E-121: targeted central support for Wirsching generators

This experiment evaluates the exact Boolean predicate
`g_ell(k,a)>0` without constructing the full table modulo `3^ell`.
The recursion is equation (2.1) of Wirsching (2003), truncated only by
the requested total cost, so its output is exact.

The motivating candidate obstruction was

```text
g_ell(ell, 2^(-1) mod 3^ell) = 0 for every ell.
```

It agrees with the exhaustive E-115 tables through `ell=16` and remains
true through `ell=21`. It fails at `ell=22`. The same residue family is
centrally reachable at every tested level from 22 through 60. Thus the
finite support holes do not provide this proposed counterexample to
condition `(?3)`.

Run:

```sh
python3 central_support.py
```

The assertions certify the transition at levels 21 and 22. This is a
diagnostic and neither proves eventual full central support nor proves
Wirsching's Conjecture 2.

The targeted predicate was independently compared with the complete
Boolean tables from E-115 for every unit residue, every cost through 12,
and every level through 8. All entries agreed.
