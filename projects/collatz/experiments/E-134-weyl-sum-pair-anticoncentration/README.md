# E-134: the 3-adic Weyl-sum program for the pair inequality, and an unconditional cascade bound

Two results, one negative and one positive, both aimed at H-161's
Question 2 (the pair anti-concentration inequality that would give
`beta_eff <= 1 + 1/(2*kappa)`).

The negative one answers the question that was asked: the sketched
program of 3-adic Weyl sums cannot prove the pair inequality, and the
reason is not a failure of equidistribution. The positive one came out
of setting that program up, and improves the best unconditional bound on
`beta_eff` recorded in this project from `2.306270` to `1.882712`.

## Result 1 (positive, unconditional): the cascade factor is nondecreasing

Write `N_ell(u) = 3^ell mu_ell(u)` and, for `u` a unit mod `3^ell`,

```text
R_ell(u) := N_ell(u) / N_(ell-1)(u mod 3^(ell-1)).
```

F4 (pushforward) says the three children of every `u` average to the
parent, so `R` has mean 1 over each sibling triple and `min_u R <= 1`.

**Claim.** `min_u R_ell(u) >= min_v R_(ell-1)(v)`.

*Proof.* F1 gives `N_ell(y) = 3*2^-t0(y)*W_ell(k0(y))` with
`W_ell(k) = sum_{j>=0} 4^-j N_(ell-1)(A^j k)` and `A(k) = 4k+1 mod
3^(ell-1)`. Since `t0` depends only on `y mod 3` and
`k0(y mod 3^(ell-1)) = k0(y) mod 3^(ell-2)`, the `3*2^-t0` factors cancel
in the ratio:

```text
R_ell(y) = W_ell(k) / W_(ell-1)(k mod 3^(ell-2)),    k = k0(y).
```

`A` is given by an integer formula, so `A^j k mod 3^(ell-2) =
A^j(k mod 3^(ell-2))` for every `j`. Numerator and denominator therefore
run over the same index `j` with the same weights `4^-j`. Substituting
`N_(ell-1)(A^j k) = N_(ell-2)(A^j k') * R_(ell-1)(A^j k)` exhibits
`R_ell(k)` as a weighted average of `R_(ell-1)(A^j k)` with weights
`4^-j N_(ell-2)(A^j k') / W_(ell-1)(k') >= 0` summing to 1. A convex
combination lies between the min and the max of what it averages. The
weights vanish exactly at non-unit positions, where `N` is identically
zero and `R_(ell-1)` is undefined, so no `0/0` term enters. QED

**Consequence.** `N_ell(u) = N_(ell-1)(u mod 3^(ell-1)) * R_ell(u)`
pointwise, so `min N_ell >= (min R_ell)(min N_(ell-1))`, and by the claim
`min R_ell >= min R_L` for every `ell >= L`. Hence for any single level
`L`,

```text
3^ell c_ell = min_u N_ell(u) >= (min R_L)^(ell-L) * min_u N_L(u)
limsup beta_eff <= 1 + log(1 / min R_L) / log 3.
```

A finite computation at one level bounds every level above it.

### Certified values (exact rational arithmetic, no floating point)

```text
 ell   min R_ell (exact)        decimal        beta bound
   2   2/7                     0.285714285714   2.140314
   3   5240/15257              0.343448908698   1.972788
   4   49-bit ratio            0.358528086675   1.933676
   5   153-bit ratio           0.367554035026   1.911045
   6   479-bit ratio           0.372104367916   1.899845
   7   1450-bit ratio          0.375368623784   1.891895
   8   4365-bit ratio          0.376951049877   1.888066
   9   13112-bit ratio         0.377986076854   1.885570
  10   39355-bit ratio         0.379174805339   1.882712
```

`min R_2 = 2/7` already gives `beta_eff <= 2.140314` from a nine-element
computation, beating the `2.306270` previously recorded in H-158. Level
10 gives `1.882712`.

### Where the method saturates

float64, levels 2 to 16 (min N cross-checked against the values E-127
recorded independently, `match` in the last column):

```text
 ell    min R        max R      min N      minN/prev   beta bound  E-127
  10  0.37917481  1.51367184  0.060876   0.91318    1.882712
  12  0.37982580  1.51306047  0.052915   0.97170    1.881150  match
  14  0.38016988  1.51271393  0.046917   0.93648    1.880326  match
  16  0.38030266  1.51244385  0.042929   0.97315    1.880008  match
```

`min R_ell` increases and is bounded by 1, so it converges; the measured
values sit near `0.3803` and are still climbing at level 16. This route
therefore floors out near `beta_eff <= 1.880` and **cannot reach 1**. The
reason is visible in the table: the proved per-level factor is `0.38`
while the ratio the truth achieves (`minN/prev`) runs at `0.93` to
`0.97`. That gap is exactly what the pair inequality would close, and it
is why H-161's Question 2 stays open.

Only `min R_L` at a computed `L` is certified. The limit near `0.3803` is
a measurement, not a proved constant.

### Relation to H-158's "no scalar recursion" claim

H-158 records, as a sketch not rederived line by line, that no inequality
using only the scalar `c_(ell-1)` (or any finite list of order statistics
of `mu_(ell-1)`, with no positional information) can do better than about
`beta <= 2.31`. Result 1 is a scalar recursion with factor `0.3798 >
5/21`, so the two statements have to be reconciled.

They are consistent. `min R_L` is not a function of `c_(ell-1)`, nor of
any order statistic of a single level: it is an inter-level quantity,
comparing `mu_ell` against `mu_(ell-1)` at matched residues. The
adversarial construction behind the H-158 sketch (a hypothetical
level-`ell-1` measure holding a block of values at the minimum along an
A-arc) is ruled out here not by how small the values are but by the
convex-combination identity, which constrains how a real Syracuse law at
one level can sit above its own projection. The H-158 sketch is about
what the value `c_(ell-1)` alone can support, and it survives; it just
does not cover inter-level input.

## Result 2 (negative): the Weyl-sum program cannot prove the pair inequality

### The reformulation is clean and exact

In the coordinate `z = 1+3k`, the affine map `A(k) = 4k+1` is
multiplication by 4 on the cyclic group `G = {z = 1 mod 3}` inside
`(Z/3^(n+1))^*`, of order `3^n`. The orbit time is the 3-adic discrete
logarithm base 4, `tau(z) = log(z)/log(4)`, both logarithms convergent on
`G`. So `A` is the shift `tau -> tau+1` and the characters of `G` are
exactly the Weyl phases `chi_m(z) = e(m tau(z) / 3^n)`. In this basis the
recursion `W(k) = N(k) + (1/4) W(A(k))` diagonalizes exactly:

```text
What(m) = Nhat(m) / (1 - (1/4) e(-m/3^n)),
```

whose denominator has modulus between 3/4 and 5/4, so `W` and `N` have
comparable coefficients frequency by frequency.

F2's two pair types become affine maps of `G` (both verified below):

```text
Type (1,2):  b = 2a+1       <=>  sigma1(z) = 2z+2
Type (2,1):  a''' = 32b+17  <=>  sigma2(z) = 32z+20
```

### The mixed Weyl sums are maximally non-degenerate

`T(m,n) = sum_{z in G} chi_m(z) chi_n(sigma z)`. Writing `z = 1+3a` and
`lambda = log/3`, the phase is `F(a) = m~ lambda(1+3a) + n~ lambda(sigma
z)` with `m~ = m/lambda(4)`, and

```text
sigma1:  F'(a) = m~/(1+3a) + n~/(2+3a)
sigma2:  F'(a) = m~/(1+3a) + 8 n~/(13+24a)
```

A critical point mod 3 requires `2m+n = 0 (mod 3)` for `sigma1` and
`m+2n = 0 (mod 3)` for `sigma2` (`lambda(4)` is a 3-adic unit, so the
criteria read the same in `m,n` as in `m~,n~`). With no critical point
the sum vanishes identically.

Verified exhaustively for `n = 2..7` and both maps:

- off the criterion, `max|T| < 3.3e-14`: the vanishing is exact;
- on the criterion, `|T(m,n)| = 3^((n+1+v)/2)` with
  `v = v_3(gcd(m,n))`, attained. Ratio `max|T| / 3^((n+1+v)/2) =
  1.000000` at every level tested.

So every primitive frequency has square-root cancellation, `|T| =
3^((n+1)/2) = sqrt(3|G|)`, and the only larger sums are the
arithmetically forced ones at frequencies divisible by a power of 3
(a frequency divisible by `3^v` collapses the sum to `3^v` copies of a
sum mod `3^(n-v)`). The phase is as non-degenerate as a phase can be.

### And it still gives nothing

Let `S, S' ⊂ G` with densities `delta, delta'`, and
`Sigma = #{z : z in S, sigma z in S'}`. Expanding both indicators,

```text
Sigma = |S||S'|/|G| + |G|^-2 * sum_{(m,n)!=(0,0)} conj(Shat(m)) conj(S'hat(n)) T(m,n).
```

Bounding the error by absolute values, with
`sum_m |Shat(m)| <= |G|^(1/2) (sum_m |Shat(m)|^2)^(1/2) = |G|^(3/2)
delta^(1/2)`:

```text
error <= max|T| * |G| * (delta*delta')^(1/2) = 3^(1/2) |G|^(3/2) (delta delta')^(1/2),
```

against a main term `|G| delta delta'`. This substitutes the most
favorable value `max|T| = sqrt(3|G|)`, the primitive one; the true
maximum over all nonzero frequencies is `|G|`, which only makes it
worse. The error beats the main term
only if `(delta delta')^(1/2) > 3^(1/2) |G|^(1/2)`, which is impossible
for densities at most 1. **At no density does this route say anything**,
including the dense regime, let alone the deep tail `x ~ 3^(-ell/2kappa)`
the theorem needs.

This is not an artifact of taking absolute values. `T(m,n)/|G|` is the
matrix, in the character basis, of composition with a bijection of `G`;
composition with a bijection is an isometry of `L^2(G)`, so that matrix is
unitary and the operator-norm route returns exactly the trivial
Cauchy-Schwarz bound `(|S||S'|)^(1/2)`. Decisively: taking `S' =
sigma(S)` gives `Sigma = |S|`, so **no bound depending only on `|S|`,
`|S'|` and spectral data of `sigma` can be nontrivial**, no matter how
good the Weyl estimates are.

### What is actually missing

Not equidistribution of `sigma`. What is missing is harmonic control of
the level set `{V <= x}` itself, jointly with `sigma`: some reason why
`Shat` cannot align with the frequencies where `T` is large. Since `S` is
defined by `V` and `sigma` relates `V` to itself, any proof has to use
the self-similar description of `V` rather than treat `S` as a black box.

Scope of the negative claim: it rules out the specific program (estimate
`T`, insert into the expansion, bound the error), not Weyl-type methods
in general. Estimating the Mellin coefficients of `V` itself is untouched
and remains the natural next thing to try.

## Files

- `cascade_factor_bound.py`: Result 1. `--exact L` runs certified
  rational arithmetic through level `L`; `--float L` runs the float64
  measurement, checks F4 and monotonicity at every level, and
  cross-checks min N against E-127.
- `pair_character_sum.py`: Result 2. Re-verifies F1 and both F2 pair
  types from a scratch rebuild of the laws, derives the `z`-coordinate
  maps, and evaluates `T(m,n)` exhaustively against the stationary-phase
  prediction and the size law.

## Running

```sh
python3 cascade_factor_bound.py --exact 8 --float 12     # seconds
python3 cascade_factor_bound.py --exact 10 --float 16    # about 100 s
python3 pair_character_sum.py --weyl-levels 2 3 4 5 6 7  # about 3 s
```

Exact level 10 takes about 74 s and is the slow part (the minimum search
compares 39355-bit rationals). Level 16 in float64 peaks at 2.4 GB
resident (measured).
Every assertion in both scripts is a check that would fail loudly:
total mass 1 at each level, F4 to 1e-10, monotonicity of `min R`,
`min R <= 1`, `sigma` bijective on `G`, and 4 generating `G`.
