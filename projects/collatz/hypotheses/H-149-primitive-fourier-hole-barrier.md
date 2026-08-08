# H-149: primitive Fourier correction and sharp one-hole barrier

Status: closed-confirmed; O5 definition corrected

Created: 2026-08-07

The spectral concentration definition used by O5 allowed every nonzero
additive frequency. This made it automatic. Every relevant law is
supported on the units modulo `N=3^ell`. At frequency `N/3`, its
coefficient is a convex combination of the two nontrivial cube roots of
unity and therefore has modulus at least `1/2`.

The diagonal configuration in O5 requires a primitive frequency
`3 not divide xi`. Thus the concentration hypothesis and its claimed
conclusion used different frequency classes. The corrected definition
is

    SC_prim(epsilon): some xi with 3 not divide xi satisfies
    |mu_hat(xi)| >= 3^(-epsilon ell).

This correction exposes a sharp abstract barrier. Let `u_a` be uniform
on all `M=2*3^(ell-1)` units except one unit a. It has a support hole.
For every primitive frequency and ell>=2, the Ramanujan sum over all
units is zero, so

    |u_a_hat(xi)|=1/(M-1).

Hence a support failure alone cannot imply `SC_prim(epsilon)` for any
fixed `epsilon<1`. Arithmetic structure beyond the existence of a hole
is indispensable. The conditional reduction can remain as a conjecture
only after imposing primitive concentration explicitly.

There is no unconditional positive primitive bound at all. Lift a
non-full law on the units modulo `3^(ell-1)` uniformly over each
three-point fibre modulo `3^ell`. It still has support holes, while the
sum of every primitive character over each fibre is zero. Thus the old
`tau>=3^-ell` step selected some nonzero frequency but did not ensure
the primitive frequency required by the diagonal configuration.

The paper's former diagonal conclusion was also too weak because it did
not chain exponent choices across adjacent scales. It has been replaced
by an explicit open target requiring a consecutive chain of length
`L/log(ell)->infinity` with bounded exponent increments. The current
Riesz-product/Halász argument yields neither that chain nor a primitive
coefficient from a hole.

E-119 verifies the coarse lower bound, the one-hole primitive identity,
and the zero spectrum of the lifted example through ell=8.
