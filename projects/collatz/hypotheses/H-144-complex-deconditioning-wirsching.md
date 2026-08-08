# H-144: conditional local-limit bridge for Wirsching multiplicities

Status: closed-confirmed; conditional reduction proved

Created: 2026-08-07

Define

    Q_(ell,a)(k)=2^(-k)g_ell(k,a)/G_(ell,a)(1/2)

and define bar Q analogously. Direct cancellation gives

    g_ell(k,a)/bar g_ell(k)
      = [G_(ell,a)(1/2)/bar G_ell(1/2)]
        [Q_(ell,a)(k)/bar Q_ell(k)].

The unconditional folded-cost law satisfies a lattice local CLT, so
bar Q_ell(k) is comparable to ell^(-1/2) in the central window.
Therefore a constant canonical lower bound together with

    Q_(ell,a)(k) >= c_delta ell^(-1/2)

uniformly in the residue implies Wirsching's condition (?3).

Beta=1 supplies only a subexponential version of the first factor. The
second factor is a residue-conditioned local limit theorem and requires
control of G_(ell,a)(exp(it)/2)/G_(ell,a)(1/2) over the phase t. This
is the exact deconditioning input separating O2 from O3.

Critic correction: an earlier sufficient condition compared every
G_(ell,a) directly with bar G on the full complex circle. It was
logically valid but structurally sterile because the coarse mod-3 bias
prevents such convergence. The conditional identity above replaces it.

E-116 evaluates the simpler additive Fourier l1 sufficient condition.
Its budget grows strongly through ell=12 and is dominated by primitive
frequencies, so triangle-inequality summation does not close the gap.
At ell=12 the largest coefficient is coarse (0.339 at central cost),
whereas the largest primitive coefficient is 0.0246. This is the
finite signature that exposed the sterile flat-to-uniform hypothesis.

## Literature boundary

Dragičević, Froyland, González-Tokman, and Vaienti (2018) prove a
quenched LCLT for random expanding dynamics using quasi-compact twisted
operator cocycles and an aperiodicity estimate. Hafouta (2020) proves
limit theorems for time-dependent expanding systems using sequential
complex Ruelle-Perron-Frobenius stability. Both frameworks require
uniform operator control on a fixed regularity space. Wirsching's
Theorem 3 only controls fixed equicontinuous families, while
g_(ell-1) has resolution growing with ell. Neither theorem applies
directly without proving the missing uniform twisted gap.
