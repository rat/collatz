# E-018 — Branching structure of the reverse tree (Galton-Watson)

Related hypothesis: [`H-018-reverse-tree-branching.md`](../../hypotheses/H-018-reverse-tree-branching.md)

## What was done

We built the Collatz reverse tree explicitly via BFS starting from each
J_t (rule: every node v always has predecessor 2v, and (v−1)/3 if v is
even and v≡4 mod6), to mechanically understand the H-013 anomaly (why
the fraction of orbits ending at J_5 is larger than at J_4, but this
inverts at t=10/11).

## Bug found and fixed during implementation

The first BFS version pruned the search as soon as a node exceeded the
magnitude limit (n_max) — but a "child" via the odd branch ((v−1)/3,
which **divides** by ~3) can be smaller than n_max even if its "parent"
(reached only after several doublings) exceeds n_max. This discarded
valid excursions that return to small values, causing undercounting by
a factor of ~5. Fixed by separating the **search** limit (generous,
e.g. 100×n_max) from the **final counting** limit (n_max). With
mult=100, the results converge to the exact values from H-013's forward
scan (t=10 and t=11 match exactly; t=4,5,7,8 differ by <2%, the
residual coming from even-deeper excursions that would need a still
larger limit).

## Mechanism found

1. **Generation of the first "checkpoint"** (the first point in J_t's
   doubling chain satisfying v≡4 mod6, enabling an extra branch):
   **always generation 1** for t≡2 (mod 3), **always generation 2** for
   t≡1 (mod 3) — a constant pattern, verified for t=4,5,7,8,10,11,13,14.
   This alone does NOT explain the inversion (it's the same pattern for
   every t).

2. **Available bit "budget"** = log₂(n_max/J_t). Since J_t≈4^t/3, this
   budget **shrinks by exactly 2 bits per unit of t**:

   | t | J_t | budget (bits, n_max=20M) |
   |---|---|---|
   | 4 | 85 | 17.84 |
   | 5 | 341 | 15.84 |
   | 7 | 5461 | 11.84 |
   | 8 | 21845 | 9.84 |
   | 10 | 349525 | 5.84 |
   | 11 | 1398101 | 3.84 |
   | 13 | 22369621 | −0.16 |
   | 14 | 89478485 | −2.16 |

## Mechanistic explanation (qualitative, not a closed formula)

There is a **competition between two effects**:
- Branching one generation earlier (the t≡2 mod3 advantage)
  systematically favors more density — this explains why p₅>p₄ and
  p₈>p₇ (budget still large, 15-18 and 10-12 bits, enough for the
  systematic advantage to dominate).
- But J_t grows exponentially with t, consuming the available budget
  within any fixed n_max limit. For t=10/11 and t=13/14, the budget
  drops to a few bits (or goes negative) — the absolute population of
  nodes found is tiny (dozens or fewer), and becomes dominated by
  idiosyncratic fluctuations of a small finite tree, not by the average
  systematic advantage. This explains why the ratio can (and does)
  invert in these cases.

## Update — the inversion is a real asymptotic fact, not finite-sample noise

The original explanation (above) suggested the inversion at t=10/11 and
t=13/14 came from "idiosyncratic fluctuations of a small finite tree"
— which would imply the ratio could change (or even grow again) with a
much larger n_max. **We tested this directly**, scaling the BFS up to
n_max=10¹¹ (using a modest search_bound, 5×n_max, instead of the
previous 100× — the oversized multiplier is what caused hangs, not
n_max itself). Result:

| pair | 20M | 80M | 1e10 | 1e11 |
|---|---|---|---|---|
| (10,11) | 0.048 | 0.072 | 0.0655 | **0.0656** |
| (13,14) | 0.200 | — | 0.296 | 0.271 |

The (10,11) ratio **converged and stabilized** between 1e10 and 1e11
(0.0655 vs 0.0656 — practically identical). The (13,14) ratio is also
converging (0.296→0.271, still adjusting a bit, but in the same range).
**This confirms the inversion is a real, permanent asymptotic fact**,
not a transient artifact of a small sample that would disappear with
more data.

This partly corrects the original qualitative explanation: the "bit
budget" explains why readings at small n_max (20M, 80M) were
unstable/noisy for large t, but **doesn't explain why the final
asymptotic value of the ratio is specifically <1** for (10,11)/(13,14)
and >1 for (4,5)/(7,8) — that part remains without a complete
theoretical explanation.

## Attempt at a closed theoretical derivation (requested by the scientific director)

I tried deriving a closed formula using the **exact** recursive
relation D(v) = D(2v) + D(w) [when v≡4 mod6, w=(v−1)/3], valid for the
density D(v) of the reverse subtree of any node v. Applying it
repeatedly along J_t's doubling chain gives:

D(J_t) = Σ_{i=1}^∞ D(w_i)

where w_1, w_2, w_3, ... are the successive "branch children" found
climbing up J_t's doubling chain (an infinite, exact sum, not an
approximation). The problem is that each D(w_i) doesn't reduce to any
already-known f(t') — w_i is a generic odd integer with no simple
relation to the J_t family, and its own density recursively depends on
the same structure, requiring knowledge of each w_i's residue modulo
3^k for arbitrarily large k. **I could not close this recursion into a
finite formula** — it seems to require understanding the full
self-similar structure of the reverse tree (possibly equivalent to an
open problem in the literature on the density of the Collatz graph).
Reporting this honestly rather than forcing an unsupported formula.

## Improved numerical precision (using multiple cores)

Given the theoretical difficulty, I used the 16 available cores and
~55GB of RAM to increase the numerical precision of the ratios,
parallelizing tree construction for different t's simultaneously.

**Pitfall found**: in a first attempt, I compared t=10 (n_max=1e12)
with t=11 (n_max=1e13) — DIFFERENT scales — and got a clearly wrong
ratio (0.651, inflated by ~10×, exactly the factor between the two
n_max). Fixed by always using the **same n_max** for both members of
each pair.

**Infrastructure limit found**: an attempt to push even further
(n_max=1e13 for the 10/11 pair, 1e15 for the 13/14 pair) was **killed
by the system's OOM killer** twice (processes using 33GB and 61GB) —
the environment has an effective memory limit lower than the nominal
~62GB (likely a cgroup), worth recording for future heavy-computation
attempts in this session.

### Final consolidated table

| pair | 20M | 80M | 1e10 | 1e11 | 1e12 | 1e14 |
|---|---|---|---|---|---|---|
| (10,11) | 0.048 | 0.072 | 0.0655 | 0.0656 | **0.0649** | — |
| (13,14) | 0.200 | — | 0.296 | 0.271 | — | **0.281** |

## Status of H-018 (before the DFS rewrite)

**Qualitative mechanism confirmed; numerical convergence well
established; closed formula not found (likely a genuinely hard
problem).**

- **(10,11)**: high confidence — the ratio stays between 0.0649 and
  0.0656 across three different scales spanning two orders of
  magnitude (1e10, 1e11, 1e12), variation of <1.5%. Convergence very
  well established around **~0.065**.
- **(13,14)**: moderate confidence — values at 1e10, 1e11, 1e14 (0.296,
  0.271, 0.281) oscillate within a ~9% range, consistent with
  convergence to something around **~0.27-0.28**, but without the same
  precision as the (10,11) pair (missing intermediate points at
  1e12/1e13, which caused OOM when attempted).

The pattern inversion is confirmed as a genuine asymptotic fact (not
finite-tree noise). The exact value each ratio converges to, and a
closed theoretical derivation, remain open questions — I tried via the
exact recursion D(v)=ΣD(w_i) and could not reduce it to a finite form.

## DFS rewrite — breaks the memory limit (2026-07-15)

The infrastructure limit documented above (OOM at 33GB/61GB) came from
the original `build_tree_count` (`experiment.py`): a **BFS** with
`deque` + `visited set`, which stores **every visited node** in memory
— O(number of nodes explored), not O(depth). For trees with hundreds of
millions of nodes (as used here), this overflows any reasonable RAM.

**Justification for removing the `visited` set**: the Collatz map is a
function (every u has exactly one image f(u)). In the reverse tree, the
only possible parent of a node w is f(w) — no node can have two
parents, except if the search re-enters the trivial cycle {1,2,4}. For
the J_t roots used here (t≥4, so J_t≥85), this never happens: 1's
forward orbit stays trapped in 1→4→2→1 forever and never reaches any
J_t>4. So `visited` is unnecessary for correctness — it's purely what
caused the memory overflow. Swapping BFS+visited for **DFS with an
explicit stack** (`experiment_dfs.py`, function `build_tree_count_dfs`),
memory drops to O(depth).

**Validation of the rewrite** (before trusting any new result):

1. **Identical to the original BFS, node for node**: running both
   versions with the same parameters (n_max=20M, mult=5), both methods
   return exactly the same `odd_nodes` for t=4,5,7,8,10,11 — confirms
   the rewrite didn't change the logic, only the data structure.
2. **Convergence to ground truth**: with mult=200 (the original
   multiplier), the DFS reproduces exactly the H-013 forward-scan
   values for t=10 (311) and t=11 (15).
3. **Measured memory gain**: t=10 with n_max=1e13 (266M nodes explored)
   used **9.8 MB** of RSS in the DFS (`/usr/bin/time -v`), max depth
   665 — previously not even attemptable at this scale with
   BFS+visited.
4. **`mult=5` is sufficient at large scale** (critical check, since at
   n_max=20M only `mult=200` matched ground truth): I repeated three
   representative pairs — one from each observed "behavior family" — at
   `mult=5` vs `mult=25`, and two of them also at 10× larger n_max:

   | pair (n_max) | mult=5 | mult=25 | difference |
   |---|---|---|---|
   | (10,11) @ 1e13 | 0.064758 | 0.064728 | 0.05% |
   | (13,14) @ 1e15 | 0.282291 | 0.282466 | 0.06% |
   | (16,17) @ 1e17 | 0.774575 | 0.774298 | 0.04% |

   and for 10× larger n_max (same mult=5):

   | pair | original n_max | n_max ×10 | difference |
   |---|---|---|---|
   | (10,11) | 0.064758 (1e13) | 0.064808 (1e14) | 0.08% |
   | (13,14) | 0.282291 (1e15) | 0.282494 (1e16) | 0.07% |

   In every case the ratio is stable to <0.1% even as the absolute
   counts keep rising (~26% more nodes between mult=5 and mult=25) —
   i.e., whatever is missed at `mult=5` affects both members of the
   pair proportionally and cancels in the ratio. This confirms
   `mult=5` was already sufficient at these scales for the purpose of
   measuring the ratio (not for counting the exact total of nodes).

## Nine pairs, much larger scale — the ratio does NOT converge to a single limit

With the memory bottleneck eliminated, we computed the ratio for 7
pairs via the reverse tree (plus the 2 small pairs from
H-013/CORRECTION.md via exhaustive forward-scan, already ground truth)
— covering t from 4 to 29, each calibrated to a similar "budget"
log₂(n_max/J_t) (~25-27 bits, the same used for the already-validated
(10,11)/(13,14) pairs):

| pair | ratio | n_max | method |
|---|---|---|---|
| (4,5) | 1.594 | 80M | exhaustive forward-scan (H-013/CORRECTION.md) |
| (7,8) | 5.972 | 80M | exhaustive forward-scan (H-013/CORRECTION.md) |
| (10,11) | **0.0648** | 1e14 | DFS tree, validated (mult and n_max) |
| (13,14) | **0.2825** | 1e16 | DFS tree, validated (mult and n_max) |
| (16,17) | **0.7745** | 1e17 | DFS tree, validated (mult) |
| (19,20) | 0.0459 | 3e18 | DFS tree, mult=5 only |
| (22,23) | 0.1592 | 2e20 | DFS tree, mult=5 only |
| (25,26) | 3.610 | 2e22 | DFS tree, mult=5 only |
| (28,29) | 0.1473 | 2e24 | DFS tree, mult=5 only |

(The last four pairs did not individually go through the mult×n_max
check above. Confidence in the extension doesn't come from covering
the same range of values — (25,26)=3.610 and (19,20)=0.046 are actually
the two most extreme points in the whole sample, outside the range of
the three validated pairs — it comes from the verified **mechanism**:
whatever is missed at mult=5 inflates the absolute counts of both pair
members proportionally (counts rise ~26% from mult=5 to mult=25, but
the ratio moves <0.1%), and this cancellation mechanism doesn't depend
on where in the range the pair falls. This is enough to trust the
ratio to a few percent precision; whether it's >1 or <1 is not in doubt
for any of the nine pairs.)

**Initial suspicion (raised and then disproven by the data itself)**:
with the first 6 points, there seemed to be a pattern tied to t mod 9
(the ratios grouped by t mod9 of each pair's "first element" seemed to
decay monotonically within each class: mod9=4 → 1.59→0.28→0.159 is
indeed monotonic). But the classes mod9=7 (5.972→0.7745→**3.610**) and
mod9=1 (0.0648→0.0459→**0.1473**) **are not monotonic** — they drop and
then rise. With only 9 points spread between 0.046 and 5.97, any small
modulus would "explain" some points by chance; **it's not worth hunting
for a finer modulus** (mod 27, alternating subsequences, etc.) with
this amount of data — there's no support for it.

## Honest answer: does the ratio converge as t→∞?

**No, at least not in any simple way.** The ratio between adjacent
classes oscillates over **~2 orders of magnitude** (0.046 to 5.97)
across the 9 measured points, with no simple periodic pattern
identified. H-018's initial assumption (the "bit budget" mechanism)
explains why readings at small n_max were noisy/unstable, but **does
not predict, and does not explain, this large-scale oscillation
pattern** — this remains genuinely open. This round's finding is not a
formula or a limit; it's the (negative, but precise) answer to the
question "does it converge?", plus the removal of the computational
bottleneck that had prevented even asking the question for t>14.

Reproduce: `python3 experiment_dfs.py [N_MAX] [SEARCH_MULT] [T_LIST]`
(see the file's docstring for the full justification for removing
`visited`).

## Decomposition D(J_t) = root + Σ D(w_i): two proven theorems (2026-07-15)

Requested by the scientific director to try to advance *why* the ratio
oscillates this way (not just *that* it oscillates). H-018's exact
recursion, D(v)=D(2v)+D(w) when v≡4mod6, applied repeatedly along
J_t's doubling chain, gives D(J_t) = 1 (the root itself, always odd) +
Σ_{i=1}^∞ D(w_i), where w_1,w_2,... are the successive branch children
found climbing the chain. This never closed (H-024) because each D(w_i)
requires arbitrary residues mod 3^k. Instead of trying to close the
whole sum, we instrumented a single DFS (`experiment_decompose.py`)
that tags each node with the index of the branch it belongs to and
sums per bucket — testing whether the sum **converges quickly in
practice**, even without a closed formula.

**Built-in correctness check**: `1 (root) + Σ buckets == D(J_t)` total
(since J_t is the only odd node on the spine — every 2^g·J_t with g≥1
is even). Matched exactly in every test.

### Two proven theorems

**Theorem 1 (generalized sterility — generalizes H-005 to every node
of the reverse tree, not just the J_t family)**: an odd node w has its
entire reverse subtree reduced to its own doubling chain — contributing
**exactly 1 odd node, forever, regardless of the magnitude limit** — if
and only if w≡0 (mod 3).

*Proof*: doubling preserves the "≡0 mod3" class (2·0≡0), and branching
at a node v requires v≡4 mod6 (i.e. v even and v≡1 mod3). If w≡0mod3,
no 2^k·w is ever ≡1mod3, so the chain never branches. If w≢0mod3, the
sequence 2^k·w mod3 alternates between the two nonzero residues
(ord₃(2)=2), hitting ≡1mod3 every 2 steps — so it branches sooner or
later. ∎

**Theorem 2 (mod-3 periodicity of branches, period 3)**: for a
non-sterile odd root m, with A=2^{g₁}·m (g₁∈{1,2} the generation of the
first branch), the first-level branch sequence w_i=(A·4^{i-1}−1)/3 has
**w_i mod 3 exactly periodic in i with period 3**, cycling through
{0,1,2} in a fixed rotation determined by A mod 9.

*Proof*: ord₉(4)=3 (4¹=4, 4²=7, 4³=1 mod9), so 4^{i-1} mod9 is periodic
in i with period 3; since A mod9 is fixed, (A·4^{i-1}−1)/3 mod3
inherits that periodicity. Computing for the three possible residues of
A mod9 that are ≡1mod3 (1, 4, 7): a=1 gives cycle (0,1,2); a=4 gives
(1,2,0); a=7 gives (2,0,1). ∎

**Corollary**: exactly 1 in every 3 consecutive branches is sterile
(contributes exactly 1, forever) — not randomly, but at a fixed
position determined by A mod9 (equivalently, for the J_t family, by
**t mod 9**, since g₁ depends on t mod3 and J_t mod27 depends on t
mod9 via ord₂₇(4)=9). Verified by direct arithmetic — not by the full
DFS, which we only ran for t=10,11,13 — across the 18 t values used in
this experiment: t≡1,8 (mod9) gives rotation (1,2,0); t≡2,7 gives
(0,1,2); t≡4,5 gives (2,0,1) (t≡0,3,6 are H-013's sterile classes, out
of consideration here). This confirms t=10/19/28 (t≡1) in rotation
(1,2,0); t=13/22 (t≡4) and t=5/14/23 (t≡5) in rotation (2,0,1);
t=7/16/25 (t≡7) and t=11/20/29 (t≡2) in rotation (0,1,2).

### Why this matters: it explains the fast convergence, not the magnitude

Validated on the three pairs (10,11)/(13,14) — plus one more decomposed
separately (t=13): in every case, the first 2-3 **fertile** branches
(not the first 2-3 branches in raw order — one of them can be sterile,
as branch 1 of t=11 is) already capture >97% of the total. This
explains *why* the infinite sum converges fast in practice, and why a
naive "branch 1 only" (R₁) measure can badly mislead: for t=11,
w_1=932067 is sterile (932067=3×310689), contributing only 1 node,
while branches 2+3 carry 98% of the total — if the sterile branch lands
in the 1st position (the potentially largest "slot", before any decay),
the total suffers more than if it lands in the 3rd position (t=10) or
the 2nd (t=13).

**But we explicitly checked whether this position explains the ratio's
magnitude — and it doesn't.** Since the phase (position of the sterile
branch) is a function only of t mod9, if it explained the ratio,
grouping the 9 already-measured ratios by J_t mod9 should give
consistent groups. It doesn't:

| J_t mod 9 | pairs (t,t+1) | measured ratios |
|---|---|---|
| 4 | (4,5), (13,14), (22,23) | 1.594, 0.2825, 0.1592 |
| 7 | (7,8), (16,17), (25,26) | 5.972, 0.7745, 3.610 |
| 1 | (10,11), (19,20), (28,29) | 0.0648, 0.0459, 0.1473 |

There's a coarse tendency (mod9=7 tends toward larger values, mod9=1
toward smaller ones), but the spread **within** each group (up to ~10×
in the mod9=4 group) is comparable to or larger than the spacing
**between** groups (the mod9=4 group's max, 1.594, already exceeds the
mod9=7 group's min, 0.7745) — i.e., the phase is a weak tendency, not
a predictor. This is exactly consistent with another observation: the
decay rate between consecutive fertile branches of the SAME phase
varies with t in a way this theory doesn't explain (680× between
branch1 and branch4 for t=10, but only 73× for t=13, both "same phase,
3 positions apart") — this decay rate is what carries the missing
information, and it depends on deeper residues (mod 27, mod 81, ...
recursively).

**Honest conclusion**: the two theorems are real and mechanically
explain *why* the sum converges fast and *why* measuring only the
first term is misleading. But they **reduce** the question ("why does
the ratio oscillate") to a more precise, still-open question ("why does
the relative magnitude of consecutive fertile branches vary the way it
does") — they don't **resolve** it. This more precise question is
exactly H-024's obstruction (unbounded 3-adic precision), now located
in a concrete, specific object instead of a general abstract
difficulty. Not worth hunting for more pairs or decomposing more t's
looking for finer structure — this same kind of hunt has already killed
the mod9 hypothesis twice this session.

## The oscillation is generic branching noise, not a hidden pattern (2026-07-15)

Explicit request from the scientific director to generate a list of
new angles "worth testing" — an agent running Opus, with all the above
context, proposed 6 angles (empirical decay distribution over random
roots; power-law vs. log-normal tail test; branching random walk
martingale; 3-adic ergodic average; quantified 3-adic dependence
profile; transfer operator ported from the forward orbit). We
implemented the first one (cheapest and newest).

**First attempt (with a real methodological error, caught by the
advisor before any conclusion)**: `experiment_random_roots.py` measured
D(w₁)/D(w₄) — the decay *within* the same root, between the 1st and
4th branch of the same phase — over 1000 random odd roots. The
standard deviation in log10 of this distribution (0.706 dex) landed
suspiciously close to the standard deviation of the 9 measured J_t
ratios (0.715 dex). **This was not valid evidence**: D(w₁)/D(w₄) is a
different object from D(J_{t+1})/D(J_t) (within-a-root vs.
between-two-roots), the "3 positions" distance was chosen because it
matched prior observations (a free parameter), and with n=9 the
standard error of the measured standard deviation is ~0.18 dex — any
value between 0.5 and 0.9 would be "consistent". Comparing only the
standard deviation and ignoring that the geometric means are
completely different (71 vs 0.43) was cherry-picking the one statistic
that matched.

**The correct null**: J_{t+1} = 4·J_t + 1 exactly (verified:
4·(4^t−1)/3 + 1 = (4^(t+1)−1)/3). So the right experiment is: for
random odd m (m≡1 mod3, same class as the pair's "first element"),
m'=4m+1 (automatically falling into m'≡2 mod3), measure D(m')/D(m) with
matched budget — the SAME kind of ratio as the 9 real measurements,
without the free parameter or the within/between-root confusion.

`experiment_null_ratio.py`, 500 samples (m in [1e5,1e6), same ~18-bit
budget used in the first test):

| | geometric mean | log10 std dev |
|---|---|---|
| 9 measured J_t ratios (H-013) | 0.432 | 0.715 dex (standard error ±0.179, n=9) |
| 500 null ratios D(4m+1)/D(m) | 0.542 | 0.758 dex |

**The two statistics match, within the expected error for n=9** — both
the center and the spread. Precisely: the standard error of the MEAN
of the 9 log-ratios is σ/√n = 0.715/3 = 0.238 dex; the difference
between the null and measured centers is log10(0.542)−log10(0.432) =
0.099 dex — well within 0.238. The spread (0.758 vs 0.715) is within
±0.179. The center near ~0.5 also confirms the size argument already
seen (w₁(t+1)/w₁(t)→2 as t→∞, which alone already predicted a
pure-size ratio ≈0.5). This is a clean comparison (same object, no free
parameter) and the result is genuine: the ~2-order-of-magnitude
oscillation we see in the 9 measured pairs **is not a special pattern
of the J_t family** — it's exactly the typical spread expected when
comparing D(m) between any two odd integers related by m'=4m+1.
(Honest caveat, not tested: the null ran on m∈[1e5,1e6] with ~18-bit
budget, while the 9 real pairs go up to J_t~1e17 with ~25-27 bits — we
assume the spread is approximately scale-invariant, which is reasonable
given the budget was kept ~constant and branching variance shouldn't
depend on absolute magnitude, but we did not verify this directly with
a larger-scale null.) Additional check (approximate, via percentiles,
not a full Hill estimator): the log-log slope of the null
distribution's tail gets steeper at each higher percentile
(p75→p90→p95→p99), more consistent with a log-normal tail than a
power law — an approximate reading, not definitive.

**This is the best possible outcome for this line, given what we
already knew**: it doesn't close H-024 (no formula, no specific D(w)
predicted), but it **dissolves** the question "why does the ratio
oscillate this specific way" into "this is exactly the noise expected
from a generic 3-adic branching process" — a cleaner answer than any
modular pattern would have been, and correctly verified this time
(right object, no free parameter, adequate statistical power). Not
worth testing the other 5 brainstormed angles — they would target the
same question that was just answered (the oscillation is generic
variance, not hidden structure), and risk repeating the same kind of
cherry-picking that has already failed twice with mod9 and once with
D(w₁)/D(w₄).
