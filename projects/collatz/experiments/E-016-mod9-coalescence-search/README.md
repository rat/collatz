# E-016 — Mod-9 coalescence search for H-008 (negative result)

Related hypothesis: [`H-016-mod9-coalescence-search.md`](../../hypotheses/H-016-mod9-coalescence-search.md)

## What was tested

We generalized E-015's symbolic simulator to joint modulus 9·2^d (full
information mod 9 + d binary bits), searching for some coalescence N
vs. N−k that would exclude class 4 mod 9 (H-008's open question).

## Result — candidates found, but none genuine

The search (d=1 to 6, k=1 to 100) found several apparent coalescences
for N≡4 mod9 (e.g. d=3, N≡13 mod72, M=N−1, verified against real
orbits: 10/10 K's confirmed). **But when testing whether these
relations are exclusive to class 4 mod 9** — repeating the same search
(same d, same residue mod 2^d, same k) for the other 8 possible
residues mod 9 — **all of them worked equally for all 9 residues**. In
other words: none of these coalescences actually depends on the
residue mod 9 — they are purely mod-2^d phenomena (already covered by
H-015's broader search), which only "appear" in class 4 mod 9 by
arithmetic coincidence (the chosen r1 also happens to satisfy ≡4 mod9,
without this being relevant to the mechanism).

We repeated the search with k up to 100 and no finding exclusive to
mod9=4 appeared.

## Why this doesn't work (technical explanation)

We derived: T(n) mod 9 = (3r+1)·5^a mod 9, where r = n mod 3 (not n mod
9!) and a is the step's valuation. That is, the evolution of the
residue mod 9 **only depends on n mod 3**, not on the full value of n
mod 9 — n's residue mod 9 carries "extra" information that has no
effect whatsoever on the future trajectory mod 9. This explains why
fixing the joint modulus 9·2^d creates no new restriction beyond what
already comes from pure mod-2^d: the "mod 9 beyond mod 3" part is
irrelevant to any coalescence based on subtracting a small k.

## Conclusion

**This technique does not solve H-008.** It's a negative result, but
an instructive one: it shows that the "H-014/H-015-style coalescence,
just with modulus mod 9 added" route is structurally bound to find
nothing specific to mod 9, because the coalescence mechanics driven by
subtracting a small k is entirely governed by the binary structure (mod
2^d), and the relevant mod-3 information that actually affects the
dynamics (H-005) is coarser than the full mod 9.

If H-008 has a solution, it probably needs a different idea — not a
small-offset coalescence search, but perhaps a multiplicative (not
additive) relation between N and M, or a cycle/period analysis using
the T(n) mod 9 = (3r+1)·5^a mod9 formula directly in a more elaborate
way (e.g. looking at the whole orbit, not just one step).

## Status of H-016

**Refuted as an approach to H-008** (technically works as a
coalescence, but isn't specific to mod 9 — doesn't advance the open
question). Theoretical explanation documented so as not to repeat this
exact attempt in the future.
