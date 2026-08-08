# H-146: equivalence of ensembles at sublinear 3-adic precision

Status: closed-confirmed; sublinear-precision theorem proved

Created: 2026-08-07

H-145 extends from fixed precision to every integer sequence
`r_ell=o(ell)`. Uniformly for

    |k-ell| <= delta sqrt(ell),

the projection modulo `3^r_ell` of

    p_(ell,k)(a)=g_ell(k,a)/sum_b g_ell(k,b)

converges in total variation to the canonical Syracuse law
`mu_(r_ell)`.

Write the canonical cost as `K=R+B`, where B is the terminal block of
length r. The Radon derivative of the conditioned block law relative
to its unconditioned law is

    P(R=k-B)/P(K=k).

If r tends to infinity and r=o(ell), choose h tending to infinity with
`h*sqrt(r/ell)->0`. Exponential concentration puts
`|B-E B|<=h sqrt(r)` with probability tending to one. On this event a
uniform lattice local CLT for R and K makes the displayed ratio tend
to one. This proves total-variation convergence of the blocks. Bounded
r is H-145. Reduction of the terminal block to the required orders is
exact and gives `mu_r`, as in H-145.

The conclusion is uniform over every character at conductor at most
`r_ell`, since Fourier transforms differ by at most twice the total
variation distance. Thus O4 has no unidentified coarse regime below
linear precision. The unresolved Fourier problem starts when the
conductor is comparable with ell.

E-117 was also run through precision 6. At ell=12 and k=ell, the TV
distances at r=3 and r=6 were 0.06228 and 0.11369. This finite range is
only an implementation check and does not test the asymptotic
sublinear theorem.

