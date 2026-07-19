# E-102 — Computational test of the "one-bit orbit mixing" conjecture (Chang, 2026)

Related hypothesis: [`H-128-busca-literaria-dirigida-pos-h127.md`](../../hypotheses/H-128-busca-literaria-dirigida-pos-h127.md)

## What was done

Requested by the scientific director: test whether H-128's finding 2
(Chang 2026, arXiv:2603.25753, "A Structural Reduction of the Collatz
Conjecture to One-Bit Orbit Mixing") can help explain/close something
in the line. We extracted the paper's exact definitions (the
odd-to-odd compressed map T(n)=(3n+1)/2^v2(3n+1), the burst indicator
X_t=1[n_t≡1 mod4], burst-ending times, Props. 5.1-5.5 relating
bit4/mod32 to gap length) and implemented a direct test on real orbits
— no Fourier, no measure, just orbit arithmetic.

The paper's remaining conjecture (Section 5.9): within the
burst-ending subclass with n≡1 mod 8, the fraction landing at n≡9 mod
32 (long gap) vs. n≡25 mod 32 (unit gap) stays **bounded** near 1/2
(doesn't need to converge to 1/2 exactly, just stay below some δ).

Two complementary experiments:

1. **`experiment_ensemble.py`** — many moderate orbits (2×10⁴ to
   5×10⁴, 20-50 bits) run in parallel (vectorized numpy), aggregating
   every burst-ending from every orbit, start to finish for each.
2. **`experiment_deep_orbit.py`** — few but very long SINGLE orbits (500
   to 16000 bits, arbitrary-precision Python integers), tracking the
   cumulative evolution of the deviation WITHIN the same trajectory —
   truer to the "T→∞ along one orbit" the paper actually states.

## Result

**Implementation validation**: in neither experiment did a
burst-ending with n≡1 or 17 (mod 32) appear in the n≡1 mod 8 subclass —
matches exactly Props. 5.1-5.5 of the paper (only 9 and 25 should
occur).

**Ensemble (many short orbits aggregated)**: the deviation
|B9/(B9+B25) − 1/2| GROWS consistently over the first ~100 steps and
then stabilizes at a plateau of ~0.012-0.019 (1.2%-1.9%) — doesn't seem
to grow without bound, but also doesn't drop to zero. **This alone is
still consistent with Chang's conjecture** (it only asks for
boundedness, not convergence to 0).

**Single long orbit (the test truest to the paper's statement)**: here
the picture is cleaner. Running a single 16000-bit orbit (38395
compressed steps, 4761 burst-endings in the relevant subclass) and
tracking the deviation every 100 events, it **closely tracks the
~1/√i statistical-noise curve** (direct comparison in the output
table), with no sign of persistent systematic bias, ending at
|deviation|=0.00053 at event 4761. The 5 orbits of 500 to 8000 bits
tested in `experiment_deep_orbit.py` (main) show the same pattern:
small deviations consistent with sample noise (0.0004 to 0.028), with
no growth trend as orbit size increases.

**Interpretation**: the ~1-2% plateau seen in the ensemble is
apparently an artifact of aggregating many short, finite orbits
(dominated by the initial/transient phase, correlated across
similar-magnitude orbits), not a real asymptotic bias. The more
rigorous test (single orbit, genuinely large T within the same
trajectory) is consistent with Chang's mixing conjecture — the
deviation behaves like decreasing noise, not a persistent bias.
**Empirical (qualified) support for the paper's remaining conjecture**,
at the tested scale (up to ~4761 events in a single 16000-bit orbit) —
not a proof, the same epistemic pattern as this line's other empirical
tests (H-111, H-114).

## Files

- `experiment_ensemble.py` — vectorized (numpy) test on many moderate
  orbits.
- `experiment_deep_orbit.py` — test on a few very long single orbits
  (arbitrary-precision integers).

## Reproduce

```
python3 experiment_ensemble.py
python3 experiment_deep_orbit.py
```

Cost: both run in seconds to a few minutes (the 16000-bit orbit used
in the fine-grained analysis above was run separately, ~1-2min).
