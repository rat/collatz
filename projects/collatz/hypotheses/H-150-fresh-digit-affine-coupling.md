# H-150: maximal affine coupling of fresh sibling digits

Status: closed-confirmed; O1 target corrected

Created: 2026-08-07

For a fixed sibling pair, or any fixed pair of descendant paths, the
two leaf values are affine functions of the same free 3-adic parameter
with unit multipliers. After conditioning modulo `3^r`, let X and Y be
their next s digits. The affine relation maps the `3^s` possible X
blocks bijectively onto the Y blocks. Thus both marginals are uniform,
but the joint law is uniform on the graph of a permutation.

Exactly,

    TV(L(X,Y),L(X) tensor L(Y)) = 1-3^(-s),
    I(X;Y) = s log(3).

The fresh blocks therefore become maximally dependent as s grows.
Literal near-independence of fresh digits across a fixed pair is
impossible at every precision. The former wording of O1 and of the
endogeny remark was incorrect.

The viable target is aggregate: expand two subtree populations using
independent path indices, remove the exact coarse affine modes, and
prove cancellation of the remaining centered diagonal-frequency sum.
This is not pairwise independence. H-150 does not prove aggregate
cancellation; it identifies the only logically possible formulation.

E-120 verifies the two exact information identities for several gaps,
coarse precisions, and fresh block lengths.

