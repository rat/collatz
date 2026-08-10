# E-142: singularity diagnostic for H-161's Q2

A Codex consultation on H-161's pair anti-concentration inequality
(Q2) raised a structural point never previously registered in this
project: **Q2 implies the Syracuse measure limit is not Haar-singular**.
If `N_ell(U) -> 0` almost surely (Haar, `U` uniform on units), then for
any FIXED `x>0`, `P(N_ell(U)<=x)` and `P(pair both<=x)` both tend to 1
as `ell->infinity`, contradicting Q2's requirement of an upper bound
`C*x^{2 kappa}` for `x` in a range (`x>=exp(-c0*ell)`) that eventually
contains any fixed `x`. So if the limit is singular, Q2 is false while
`beta_eff->1` (equivalently the Weak Covering Conjecture, O2's actual
target) could still hold: Q2 may be strictly stronger than what the
paper needs.

Full transcript of the consultation that raised this:
`codex_consultation_transcript.txt` (2255 lines, `codex exec -s
read-only`, gpt-5.6-sol, unedited). Codex ran its own numerical checks
inside that session (reproduced independently here, not just read from
its output, see below).

## What this script measures

`python3 singularity_diagnostic.py`

**(a) Marginal diagnostic** (solid, uses ALL units mod `3^ell`, not a
subset): `E[-log N_ell(U)]` and `P(N_ell(U)<=x)` for fixed
`x=0.1,0.2,0.5`, `ell=4` to `16`. If the limit were singular, both
should trend toward `infinity`/`1` respectively; if non-singular with a
proper limiting density, both should stabilize.

**(b) Pair diagnostic, weaker than it first looks (corrected after a
critique round, see below)**: `P(N_ell(y(k))<=x AND N_ell(y(A(k)))<=x)`
for `y` via the `t0=1` branch representative `y=(3k+1)*inverse(2) mod
3^ell` at BOTH `k` and `A(k)` (same construction independently verified
against `float_levels`' own recorded min-N values in H-176's check).
**This is not H-161/Q2's actual pairing (F2)**, which crosses phases (a
`t0=1` child against a `t0=2` child); using `t0=1` at both ends always
picks the LARGER of each point's two children (F1: children are
`(3/2)W(k)` and `(3/4)W(k)`), biased against finding small values at
either end, hence against finding any signal here. An earlier version
of this README called it "the actual pairing H-161/Q2 uses"; that was
wrong, corrected here.

## Result

**(a)**: `E[-log N_ell(U)]` reproduces Codex's own numbers exactly at
matching levels (`0.182, 0.214, 0.236, 0.252` at `ell=8,10,12,14`) and
extends cleanly to `ell=16` (`0.264`). Increments are decreasing and
fit a power law in `ell` with exponent `-1.69` (whole range) to `-2.05`
(last 6 points), on the summable (`<=-1`) side of the threshold, so the
series is consistent with a FINITE limit, i.e. consistent with
non-singularity. **Caveat, added after a critique round**: 12-13
increments cannot reliably separate a summable power law from a
marginally divergent one (exponent close to `-1`, which would also look
decelerating over this short a range); "well past `-1`" oversold the
discriminating power of this fit in an earlier version of this README.
`P(N<=0.1)` grows from `0` (`ell=4`) to `0.024` (`ell=16`) with visibly
decelerating increments, not accelerating toward `1`.

**(b)**: zero observed pairs at fixed thresholds `0.1` and `0.2` through
`ell=16`. **This is not evidence of anti-concentration** (an earlier
version of this README read it that way; wrong, corrected here): the
script now also prints the pair count an INDEPENDENT model would
predict at this threshold (`n * d1(0.1) * d2(0.1)`), and that expected
count stays below `0.01` through `ell=16` too. Seeing 0 pairs when an
independent model would also typically show 0 pairs says nothing.
This is the same "fixed threshold has no discriminating power at
reachable `ell`" trap already documented three times elsewhere in this
line (E-131's original arc measurement, H-158's cost-band scan,
H-161's periodogram): a scaled threshold (`exp(-eps*ell)`, as
E-131/H-161 use) would be needed to get any signal here, not attempted
in this script (out of scope for a cheap diagnostic, and panel (b) uses
a biased branch anyway, see above). The marginal panel (a) is what this
experiment was actually built to answer.

## Honest verdict (Regra 10b)

Panel (a) is evidence AGAINST the limit being Haar-singular, from a
13-level finite range (Regra 11: measured, not proved; H-140's standing
lesson that no finite range decides an asymptotic question applies here
in full, and the caveat above narrows how much this specific fit can
discriminate). Not a proof either way. Panel (b) produced no usable
signal, honestly reported as such rather than read as a null result.
Together, sufficient to keep the B_kappa certification program (H-177)
a live option rather than a moot one, which is the question this
diagnostic was built to answer before investing further compute in
that program, without promoting it to "likely to succeed".

Not mirrored in `collatz-endogeny` (not yet cited by any paper text).
