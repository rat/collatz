# E-133: does a moment/Fourier functional of the fresh-digit joint law cancel after aggregation?

E-120 and H-150 (paper: `thm:fresh-digit-coupling`) prove that a fixed
sibling pair has maximally coupled fresh digits: `TV = 1-3^-s` and
`I(X;Y) = s*log(3)`. E-129 aggregated that joint law over the natural
branching measure on the sibling gap (`P(Delta=2k)=3*4^-k`, from E-108)
and found TV and mutual information essentially unmoved. H-159 recorded
the correct reading of that negative result: TV and mutual information
are not the functionals the second-moment programme consumes, and the
open target is cancellation of a specific moment or Fourier coefficient.

This experiment measures that coefficient.

## Which functional, and why it is the relevant one

Section 9 of `main.tex`, under "The correct, non-circular
reformulation", writes the quantity the programme actually needs as

```text
Cov  proportional to  sum_{xi != 0} S_1(xi) * conj(S_2(xi)),
```

with the **same** frequency `xi` in both factors. That is one diagonal
slice of the bivariate spectrum of the pair. Equivalently it is a
character functional of the difference of the two leaves,

```text
D(xi) := E[ e_{3^s}( xi * (X - Y) ) ],
```

which is exactly what `thm:multiscale-parseval` and
`prop:primitive-fibre-energy` also consume: a coefficient of one law at
one frequency, never a distance between two laws. Under the product law
`D(xi) = 0` for every `xi != 0`, since both marginals are uniform. So
`D` has a clean independence baseline and TV does not.

The bivariate spectrum `Phi(xi,eta) = E[e(xi X + eta Y)]` is what TV
sees. For a fixed pair it is unimodular on the whole line
`xi + eta*m = 0 mod 3^s` with `m = 2^Delta`, which is the "line of
resonant frequencies" of `prop:fixed-pair`. The question this
experiment answers is what that line leaves on the diagonal
`eta = -xi`.

## Run

```sh
python3 fresh_digit_moment_cancellation.py
python3 fresh_digit_moment_cancellation.py --coarse 1 --max-fresh 6 --k-max-list 16 300
```

The second invocation is the one directly comparable to E-129, which
used `coarse=1` and `k_max=16`; it reproduces E-129's aggregate TV of
`0.992193` at `fresh=6` exactly, as an independent check of that
experiment before contrasting against it.

Runtime is under two minutes. Every reported `D(xi)` is computed twice,
once from the divisibility predicate and once by direct summation over
the free parameter, and the run aborts if the two disagree beyond
`1e-10`.

## Result

Aggregated over the same branching measure E-129 used, same ensemble,
`coarse=1`:

```text
fresh   aggregate TV      max primitive |D_agg|   bound 4^(1-3^(s-1))
        (k_max=16)           (k_max=300)
  1       0.651045              9.77e-01               1.00e+00
  2       0.783566              4.74e-02               6.25e-02
  3       0.885610              1.14e-05               1.53e-05
  4       0.948799              1.67e-16               2.22e-16
  5       0.979831              5.13e-49               6.84e-49
  6       0.992193             1.50e-146              2.00e-146
```

The functional cancels. TV does not. The two columns are not two
metrics on one object; they are two different objects, and the
programme reads the second one.

At E-129's own truncation `k_max=16` the diagonal column is more
extreme still, exactly `0` from `fresh=4` on, because no resonant gap
is inside the truncation at all. The `k_max=300` column is the honest
one, and it is the one the bound is compared against.

The mechanism is exact, not numerical. For a fixed gap `Delta = 2k`,
the fresh blocks satisfy `Y = m X + g mod 3^s` with `m = 2^Delta`, so
`X - Y = (1-m)X - g` and

```text
D(xi) = e(-xi g / 3^s) * muhat( xi*(1-m) ),
```

where `mu` is the law of the free parameter. For uniform `mu` this is a
root of unity when `3^s` divides `xi*(1-m)` and exactly zero otherwise.
Since `v3(1 - 2^(2k)) = 1 + v3(k)`, the whole diagonal resonance of a
pair with gap `2k` sits at conductor `3^(1+v3(k))`, and nothing at all
survives above that conductor. For the typical gap that is conductor
`3`: one single coarse mode, which is the mode O1's own statement
already removes.

Two consequences, both exact:

- A gap `2k` contributes to a primitive frequency at scale `s` only if
  `v3(k) >= s-1`, hence only if `k >= 3^(s-1)`. Those gaps carry total
  branching weight at most `4^(1-3^(s-1))`, which is the bound in the
  table above and is met to within a factor below `1.4` at every scale.
- At `fresh=1` there is no cancellation at all, and none is claimed:
  `X - Y = -g mod 3` identically, so the conductor-3 mode is fully
  resonant. The honest statement is not "the diagonal vanishes" but
  "the entire diagonal resonance sits at conductor `3^(1+v3(k))`".

Section C measures the identity for non-uniform `mu` and confirms the
energy relation it forces,

```text
sum over primitive xi mod 3^s of |D(xi)|^2  =  3^j * E_(s-j)(mu),
       j = v3(1-2^Delta) = 1 + v3(k),
```

with `E_r` exactly the primitive energy of `thm:multiscale-parseval`.
Verified to relative error below `5e-14` at every `(s,k,mu)` tried.
The pair functional at scale `s` is therefore controlled by the free
parameter's own spectrum at the coarser scale `s-j`, with no
independence hypothesis anywhere. The `L2` criterion of
`thm:multiscale-parseval` transfers to the pair term by term.

Section D measures a functional that does **not** cancel: the
covariance of the `d`-th base-3 digits of the two leaves. Aggregated
over the gap ensemble at `coarse=1` it sits at `-0.333` (digit 0),
`0.203` (digit 1) and `0.111` (digit 2). The values move with the
coarse offset (at `coarse=2` they are `0.464`, `0.096`, `0.188`) but
stay away from zero either way. Choosing the character sum of the
difference is doing real work; "some low-order moment" would not have
sufficed.

## What section E found, and it changed the model

Section E checks on actual integers that `prop:fixed-pair`'s affine
form is real. It holds exactly: for every admissible depth-5 exponent
sequence tried, `w(v0 + 3^D t) = w(v0) + 2^A t` for all `t` tested.

But the first version of the check failed, and the reason is
substantive. A leaf of the Syracuse tree must be coprime to `3`, and
`w(v0) + 2^A t` runs through all three classes mod `3` as `t` varies,
so one class of `t` is inadmissible per leaf. Intermediate vertices are
unaffected, since they shift by `2^(A_i) * 3^(D-i) t`, which vanishes
mod 3. The free parameter of a real leaf pair is therefore uniform on a
union of classes mod `3`, not on all of `Z/3^s`, which is a weaker
hypothesis than the one `thm:fresh-digit-coupling` states.

That restriction does not break the cancellation, and the identity of
section C says why: for such a law `muhat` vanishes off the multiples
of `3^(s-1)`, so `E_r(mu) = 0` for every `r >= 2`, and the primitive
diagonal vanishes at every scale `s >= j+2` with the entire residual at
`s = j+1`. Measured on real leaf pairs from `v0 in {1,5,7,11,17,25}`,
all with `j=1`: max primitive `|D|` is `1.000` at `fresh=2` and drops
to `1e-14` at `fresh=3` and `fresh=4`. The prediction is exact.

## What this does not show

**The averaging is over the free arithmetic parameter, not over path
indices at fixed `v`.** This is the limitation that bounds the whole
result. `thm:fresh-digit-coupling` posits a uniform free lift, and
E-129 aggregated inside that same model, so the comparison above is
apples to apples. But O1 needs cancellation for a **fixed integer**
`v`, where `S_1(xi) conj(S_2(xi))` for one pair of paths is a single
unimodular phase and there is no expectation over `t` to take at all.
The cancellation O1 needs must come from averaging over the two path
indices, which is a different average and a different theorem. Nothing
here supplies it. Registered as its own hypothesis (H-162).

Within the model, though, the reading is clean and it is a barrier
result about a barrier: the maximal coupling of
`thm:fresh-digit-coupling` constrains a functional the second-moment
route never evaluates, and on the functional the route does evaluate,
the surviving resonance is exactly the coarse affine mode that O1's own
wording already removes. The `TV = 1-3^-s` figure should not be read as
an obstruction to the Fourier programme.

Two further limits worth stating. The model is one sibling pair from a
common ancestor; the real tree functional aggregates many pairs at
once, and this says nothing about interference between pairs. And the
branching weight `3*4^-k` is E-108's size-biased pair measure, natural
because it is the weight appearing in the second-moment sum, but not
the only conceivable measure on gaps; E-108's own README already flags
that.

## Status of each claim

- Vanishing of `D(xi)` at primitive `xi` for a fixed gap with
  `v3(k) < s-1`, and the identity `D(xi) = phase * muhat(xi(1-m))`:
  **proved**, by the one-line computation above, and verified
  numerically as a cross-check.
- The aggregate bound `4^(1-3^(s-1))`: **proved** (sum of the
  branching weights of the resonant gaps).
- The energy relation `3^j * E_(s-j)(mu)`: **proved** (the map
  `xi -> xi(1-m)` is `3^j`-to-one from the units mod `3^s` onto the
  elements of valuation `j`), verified numerically.
- Everything in section E about real integers: **empirical**, a finite
  check over six roots and depth 5.
