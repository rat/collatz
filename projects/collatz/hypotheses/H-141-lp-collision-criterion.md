# H-141: exact Lp collision criterion

Status: closed-confirmed

Created: 2026-08-07

## Statement

For every pressure root alpha, level k, and p greater than 1,

    ||M_k^(alpha)||_p^p
      = q^(k(p-1)) sum_u mu_(alpha,k)(u)^p.

The tilted projective measure has an Lp density if and only if these
quantities are bounded uniformly in k. For integer p, the sum is the
probability that p independent tilted Syracuse sums collide modulo q^k.

## Proof

Haar measure on the finite quotient gives mass q^(-k) to each residue.
Substitution of M_k(u)=q^k mu_k(u) proves the identity. A uniform Lp
bound gives Lp martingale convergence and preserves total mass, hence
the limiting density is in Lp. Conversely, if the projective measure
has density f in Lp, then M_k is the conditional expectation of f on
the level-k cylinder sigma algebra, and conditional expectation is an
Lp contraction.

## Computation

E-114 computes the spectrum for the ordinary Syracuse law through
k=14. Moments below p=2 slow down on the tested range, p=2 shows the
almost-linear behavior already seen in E-100, and moments above p=2
grow faster. This is finite evidence only. It does not prove a critical
index or settle absolute continuity.

## Consequence for paper 01

The L2 statistic is now part of an exact family rather than an isolated
sufficient condition. This supplies a rigorous collision vocabulary
for O7. It does not imply the worst-residue lower bound in O2, because
averaged concentration does not control the smallest cylinder mass.
