# E-100 — Collision mass K_ℓ of the Syracuse measure: testing the L² hypothesis

Related hypothesis: [`H-126-regime2-decorrelacao-agregados-irmaos-estrutura-exata.md`](../../hypotheses/H-126-regime2-decorrelacao-agregados-irmaos-estrutura-exata.md)

## What was done

A decisive computational test, requested by the advisor before
formalizing the "regime-2 lemma" (H-115/H-126): the Fable proposed a
conditional Lemma 2' whose hypothesis is K_∞ := lim_ℓ K_ℓ < ∞, where

    K_ℓ := 3^ℓ · Σ_y P(Syrac(Z/3^ℓZ) = y)² = 3^ℓ · P(Syrac_ℓ = Syrac'_ℓ)

is the normalized collision mass of Tao's (2022) Syracuse measure —
equivalently, the density f = dμ/d(Haar) belongs to L²(Z_3).

We computed K_ℓ EXACTLY (up to double floating-point rounding, with no
significant truncation of the geometric tail) via a recursion derived
in this session from Tao's identity F_n(a) = 2^{-a_1}·(1+3·F_{n-1}(a_2,...,a_n))
(eq. 1.22/1.29) and the memoryless property of Geom(2): the law μ_n of
F_n satisfies the fixed point

    μ_n(y) = (1/2)·ν(2y mod 3^n) + (1/2)·μ_n(2y mod 3^n)

where ν = the law of 1+3·F_{n-1}. Since F_n is never a multiple of 3
(Tao's Remark 1.15) and 2 is a primitive root mod 3^n for every n, the
integer support of μ_n lives on a single cyclic orbit of size 2·3^{n-1}
under multiplication by 2; along it, the equation above is a circular
linear recursion, solved via a truncated geometric series (the kernel
(1/2)^s decays so fast that truncating at s=100 is irrelevant in
floating point).

## Result

K_ℓ does NOT saturate — it grows cleanly and consistently linearly up
to ℓ=17 (the practical limit tested), with increments ΔK_ℓ converging
monotonically to ≈0.47 (from 0.476 at ℓ=2 to 0.472 at ℓ=17, with no
sign of reversal). **The L² hypothesis (K_∞<∞) FAILS** — a direct
empirical refutation, not merely "open". This kills the Fable's
conditional Lemma 2' via the same wall as regime 3: the "regime-2
lemma" isn't an easier step than regime 3, it's its sibling, and now
with computational evidence that the extra condition that would save
it is false. See H-126 for the full analysis and the structure theorem
that survives (the exact coarse component, Prop. 2 — that part is
positive and proven).

Sanity check: K_1 = 5/3 exact (computed by hand from
P(Syrac_1=1)=1/3, P(Syrac_1=2)=2/3 — matches the script, error <1e-10).

**Machinery validation (requested by the advisor)**: the only point
checked above (ℓ=1) is the hard-coded base case, which doesn't exercise
the recursion itself. `validate_against_direct_mc.py` compares the
recursion's distribution p_ℓ, BIN BY BIN (not just K_ℓ), against DIRECT
Monte Carlo sampling of Syrac's primary definition
(F_ℓ(a) = Σ_j 3^{j-1}·2^{-a_[1,j]} mod 3^ℓ, a_i~Geom(2) iid, 3×10⁶
samples) at ℓ=3 and ℓ=4 — the first levels where the recursion actually
runs. Result: max|p_dp-p_mc| = 0.000311 (ℓ=3) and 0.000213 (ℓ=4), both
WITHIN the expected Monte Carlo noise (~1/√N≈0.000577). The recursion
is correct at the tested levels; since the machinery is the same at
every ℓ (no per-level special case), this validates the method, not
just two points.

## Files

- `experiment_k_ell.py` — the single script: recursion of F_n's law via
  DP on the cyclic orbit, computation of K_ℓ for ℓ=1..17, a coarse
  log-log fit of the growth exponent.
- `validate_against_direct_mc.py` — bin-by-bin validation of the
  recursion against direct Monte Carlo sampling at ℓ=3,4.

## Reproduce

```
python3 experiment_k_ell.py
python3 validate_against_direct_mc.py
```

Cost: ℓ≤14 is instantaneous; ℓ=17 takes ~55s (dominated by `np.roll`
over an array of size 2·3^16≈86 million, ~100 times). Don't go much
beyond ℓ=18-19 without need — the cost per level scales ~3× (the orbit
size triples).
