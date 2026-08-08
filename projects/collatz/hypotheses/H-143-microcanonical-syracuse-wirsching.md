# H-143: microcanonical decomposition of the Syracuse measure

Status: closed-confirmed

Created: 2026-08-07

Let c_i=2*3^i and let g_ell(k,a) be Wirsching's generator. Folding each
geometric exponent minus one modulo c_i leaves the corresponding
Syracuse residue unchanged and gives

    mu_ell(a)
      = product_i [1/(2(1-2^(-c_i)))]
        * sum_k 2^(-k) g_ell(k,a).

This was derived from the exponent orders and checked bin by bin
against the independent E-100 recursion through ell=4.

The folded costs J_i are independent, with mean sum ell+O(1) and
variance 2*ell+O(1). Their central window
|sum J_i-ell| <= delta*sqrt(ell) has probability bounded below.
Consequently, a uniform lower bound

    g_ell(k,a) >= eta * average_a g_ell(k,a)

through that window implies mu_ell(a) >= C*3^(-ell) uniformly. Thus
Wirsching's target condition (?3) directly implies the cylinder lower
bound required by Tao's beta=1.

E-115 computes the fixed-cost multiplicities exactly through ell=12.
At ell=12 the support fractions at costs ell-floor(sqrt(ell)), ell,
and ell+floor(sqrt(ell)) are 0.2735, 0.8074, and 0.9973. The minimum is
still zero at all three costs. This finite fact does not decide the
asymptotic lower bound.

A Boolean support recursion reaches ell=16. The first fixed cost that
covers every unit residue is ell+5 for every ell from 10 through 16.
At ell=16, central coverage is 0.9194 and upper-window coverage is
0.99999972. No extrapolation from this finite pattern is used.

An attempted obstruction based on the 3-adic fixed point 1/13 was
rejected: following the locally cheapest branch is not globally
optimal. At ell=3 the alternative increments (5,0,1) already beat the
repeated fixed-point branch.
