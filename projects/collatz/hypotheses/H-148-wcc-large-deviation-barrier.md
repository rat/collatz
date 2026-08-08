# H-148: large-deviation barrier for the WCC-to-beta bridge

Status: closed-confirmed; sharp truncated-mass barrier proved

Created: 2026-08-07

Let `A_i` be independent with `P(A_i=m)=2^-m` and
`B_ell=sum_i A_i`. For every fixed `1<s<2`,

    P(B_ell<=s ell)=exp(-I(s)ell+o(ell)),

where

    I(s)=s log 2+(s-1)log(s-1)-s log s > 0.

The Syracuse mass contributed by all tuples below this cost has this
same total mass. Its minimum over the `2*3^(ell-1)` unit residues is at
most its average, hence at most

    3^(-ell) exp(-I(s)ell+o(ell)).

At the critical WCC slope `s*=1+log_4(3)`,

    I(s*)=0.012039386618...,
    1+I(s*)/log(3)=1.010958721964....

Thus even perfect weighted equidistribution of every representation in
the WCC cost slice cannot prove beta=1. H-131 had left open whether
multiplicity inside that slice could recover the entire deficit. It
cannot. A WCC-to-beta implication needs control reaching costs
`B=2ell-o(ell)`, where the geometric cost law has subexponential rather
than exponentially small mass. This is the central window studied by
H-143 and H-144.

E-118 evaluates the exact negative-binomial tail and converges to the
closed-form rate. The proof uses the generating function
`E exp(tA)=exp(t)/(2-exp(t))` and Cramér tilting; no numerical estimate
is needed.

