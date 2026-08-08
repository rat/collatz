# H-145: equivalence of ensembles at fixed 3-adic precision

Status: closed-confirmed; fixed-precision theorem proved

Created: 2026-08-07

Let

    p_(ell,k)(a)=g_ell(k,a)/sum_b g_ell(k,b).

For every fixed precision r, uniformly for
`|k-ell| <= delta sqrt(ell)`, the projection of `p_(ell,k)` modulo
`3^r` converges in total variation to Tao's canonical Syracuse law
`mu_r`.

Under the canonical weights, the folded costs are independent and the
microcanonical law is their joint law conditioned on their sum. A
uniform lattice local central limit theorem shows that conditioning the
sum to a central value does not change the limiting law of any fixed
terminal block. The terminal r costs determine the residue modulo
`3^r`. Reducing their large folded-geometric caps to the smaller orders
`2*3^i` gives exactly the r canonical folded-geometric coordinates.
Total variation contracts under this deterministic residue map.

Consequently, fixed-conductor Fourier coefficients converge to the
corresponding coefficients of `mu_r` and need not vanish. The old O4
formulation asking for decay uniformly over every nonzero frequency was
impossible. H-146 subsequently extends this theorem to every
`r=o(ell)`. The remaining target starts at linear precision.

E-117 checks the finite convergence independently through ell=12 and
r=3. At ell=12 the total-variation distances for k=ell are 0.02050,
0.04024, and 0.06228 at r=1,2,3. For
k=ell+floor(sqrt(ell)) they are 0.04310, 0.07902, and 0.12677.
