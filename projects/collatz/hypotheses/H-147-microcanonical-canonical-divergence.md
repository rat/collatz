# H-147: full-precision microcanonical-to-canonical domination

Status: closed-confirmed; divergence bound proved

Created: 2026-08-07

Let `p_(ell,k)^(r)` be the projection modulo `3^r` of the fixed-cost
law and let `mu_r` be the canonical Syracuse law. For every
`1<=r<=ell` and every event E,

    p_(ell,k)^(r)(E) <= P(K_ell=k)^(-1) mu_r(E).

This follows before projection because the microcanonical digit law is
the canonical law conditioned on `K_ell=k`. Data processing gives

    D_infinity(p_(ell,k)^(r) || mu_r)
      <= -log P(K_ell=k),

and the same bound holds for Kullback-Leibler divergence. A lattice
local CLT gives, uniformly for
`|k-ell|<=delta sqrt(ell)`,

    -log P(K_ell=k) = (1/2) log ell + O_delta(1).

Thus the microcanonical law differs from the canonical law by at most a
polynomial likelihood factor even at full precision. The relative
entropy per 3-adic digit tends to zero. This does not give the lower
pointwise bound required by Wirsching's condition (?3), since the
inequality has the opposite direction. It shows that the O2-to-O3 gap
is a lower-tail problem rather than an exponential entropy gap.

E-117 was extended to full precision. At ell=13, the TV distances at
r=ell are 0.25195 for k=ell and 0.26078 for
k=ell+floor(sqrt(ell)). At r=1 they are 0.01885 and 0.04003. These
finite values illustrate the separation of scales but do not determine
the full-precision limit.

