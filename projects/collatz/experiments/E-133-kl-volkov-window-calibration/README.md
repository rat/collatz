# E-133 -- calibrating the Kontorovich-Lagarias versus Volkov gate (H-113, O8)

Related hypotheses:
[`H-113`](../../hypotheses/H-113-statistical-gate-kontorovich-lagarias-vs-volkov.md),
[`H-162`](../../hypotheses/H-162-congruencia-de-irmaos-qx1.md).
Predecessor experiment: [`E-097`](../E-097-qx1-empirical-gate/).

## The question

Kontorovich and Lagarias (arXiv:0910.1944, Theorem 8.10) predict a
counting exponent `eta_5,BP ~ 0.650919` for the reverse tree of `5x+1`.
A competing branching model of Volkov, discussed in the same paper,
predicts `~0.678`. The two differ by `Delta = 0.027081`, and the
authors write that Volkov's data "seems insufficient to discriminate
between these two predicted exponents. It would be interesting for this
problem to be investigated further." E-097 measured `0.639` with a
bootstrap interval `[0.633, 0.645]`.

Nobody had measured what that estimator does to a process whose exponent
is already known. Doing so turns out to answer the original question
too, because the estimator's bias is larger than `Delta`, and the way
around that is to run the same estimator on processes built to have each
of the two disputed exponents and see which reading the arithmetic tree
matches.

## What is here

| file | what it does |
|------|--------------|
| `tree_counts.c` | the enumerator: arithmetic tree and three matched stochastic controls, one code path |
| `validate_vs_python.py` | byte-for-byte check of the C against the E-097 Python enumerator |
| `annealed_exact.py` | closed form for the exact annealed counting function of the model |
| `check_mean_vs_annealed.py` | the simulator reproduces that closed form |
| `compare_modes.py` | count distributions of the modes side by side |
| `within_root_spread.py` | separates across-root from within-root fluctuation |
| `cyc_vs_cycq.py` | checks that the integer and real-valued recursions agree |
| `buffer_squeeze.py` | bounds the error of the truncation extrapolation itself |
| `analyze.py` | the E-097 estimator, per-decade slopes, deficit against `alpha_-` |
| `summary.py` | the comparison table: every process, one estimator |
| `run_deep.sh` | the matched deep batch, checkpoints to `1e10`, buffers to `1e15` |

Build and reproduce:

```
gcc -O3 -march=native -fopenmp -o tree_counts tree_counts.c -lm
python3 validate_vs_python.py          # must print VALIDATION PASSED
python3 annealed_exact.py 5
./tree_counts --q 5       --roots 300 --cp 4 8 --buf 9 13 --out data/q5_arith_b13.txt
./tree_counts --q 5 --cyc --roots 300 --cp 4 8 --buf 9 13 --out data/q5_cyc_b13.txt
./tree_counts --q 5 --iid --roots 300 --cp 4 8 --buf 9 13 --out data/q5_iid_b13.txt
./tree_counts --q 5 --cycq 5.00000 --roots 300 --cp 4 8 --buf 9 13 --out data/q5_cycq500_b13.txt
./tree_counts --q 5 --cycq 5.05398 --roots 300 --cp 4 8 --buf 9 13 --out data/q5_cycq505_b13.txt
python3 summary.py                     # the comparison table
./run_deep.sh                          # the matched deep batch, tens of minutes
python3 summary.py b15 10              # the same table at decade 1e9->1e10
python3 buffer_squeeze.py data/q5_arith_b17.txt
```

## The four modes

They share one code path. The branch class of a node is either the true
residue or a draw, and nothing else differs:

- `arith`: `r = u mod q`, the real tree.
- `iid`: `r` drawn uniformly at every node. This is the branching random
  walk whose annealed pressure is `q^(alpha-1)/(2^alpha-1)`, so its
  counting exponent is provably `alpha_-(q) = 0.650919` at `q = 5`.
- `cyc`: the first sibling's class is drawn, and successive siblings
  advance by `c = ((2^d-1)/q) mod q`, which is what the arithmetic tree
  does exactly (H-162).
- `cycq qval`: the `cyc` structure with the value denominator replaced by
  a real `qval`, so the exponent becomes tunable. It solves
  `qval^alpha = q(2^alpha - 1)`: `qval = 5.00000` gives 0.650919 and
  `qval = 5.05398` gives 0.678.

Roots are fertile by construction in every mode. Getting this wrong
was a real error in the first pass here: the arithmetic roots are
sampled with `u mod q != 0` and are therefore always fertile, so a
control that drew the root residue from `{0..q-1}` killed one tree in
`q` outright and read `0.484` instead of `0.612`.

## The exact annealed count

For each integer `n >= 1`, a node's expected number of children at
exponent exactly `n` is `1/q`: the child exists iff `2^n r == 1 (mod q)`,
that is `r == 2^(-n)`, one residue class out of `q`. So the offspring
intensity is `(1/q) sum_{n>=1} delta_n`, a level-`k` node reached by
exponents `a_1..a_k` sits at value ratio `2^A/q^k` with `A = sum a_i`,
and

```text
E[# level-k nodes with sum a_i = A] = q^(-k) C(A-1, k-1).
```

Counting those with `2^A/q^k <= 10^t` means `A <= N_k(t)` with
`N_k(t) = floor((t + k log10 q)/log10 2)`, and the hockey-stick identity
`sum_{A=k}^{N} C(A-1,k-1) = C(N,k)` collapses the inner sum:

```text
M(t) := E[N(u0 * 10^t)] = sum_{k>=1} C(N_k(t), k) / q^k .
```

Checked against the brute-force double sum for `q = 3, 5, 7` and
`t = 1..4`, and against the simulator's mean count.

This matters because it settles a question the fitted extrapolations
could not. The annealed local slope reaches `0.6517` at `t = 3` and
`0.65079` at `t = 4`, against `alpha_-(5) = 0.650919`. The annealed side
of the model has essentially no finite-window bias at the scales E-097
worked in. Whatever bias the estimator has is therefore a
quenched-versus-annealed lag, the log-slope of one realization trailing
the log-slope of the mean, and not a correction exponent that could be
fitted away.

## Result, part 1: the estimator has a bias larger than the thing it measures

Standard E-097 window, `1e5..1e8`, 300 roots, truncation extrapolated to
infinite buffer by Aitken, identical estimator in every mode:

| mode | estimator | sd of log10 N(1e8) | true exponent |
|------|-----------|--------------------|---------------|
| iid | 0.6131 | 0.8014 | 0.650919 |
| cyc | 0.6294 | 0.6657 | 0.650919 |
| arith | 0.6382 | 0.5942 | disputed |

The estimator under-reads by 0.038 on a process whose exponent is known.
That is larger than `Delta = 0.027`. So the raw reading cannot be
compared against a theoretical prediction at all, which is what E-097
and H-113 did, and it is also why adding the bias back by hand is not
licensed: the bias itself depends on how much the process fluctuates,
and the three rows above have visibly different fluctuation.

## Result, part 2: compare readings, not a reading against a prediction

The fix is to stop comparing a biased reading to an unbiased prediction.
Run the same estimator on a process built to have exponent 0.650919 and
on one built to have exponent 0.678, and see which reading the
arithmetic tree matches. Mode `cycq` supplies both: same branching, same
sibling congruence, same roots, same window, same buffers, with only the
value denominator changed, `qval^alpha = q(2^alpha - 1)`.

From `summary.py`:

```
       process  true exponent             window estimator              decade 1e7->1e8
  cycq 5.00000       0.650919   0.63950 [0.63357,0.64647]   0.64796 [0.64426,0.65204]
  cycq 5.05398       0.678000   0.65943 [0.65290,0.66630]   0.67079 [0.66649,0.67585]
           cyc       0.650919   0.62943 [0.62213,0.63650]   0.64437 [0.64067,0.64819]
           iid       0.650919   0.61308 [0.60233,0.62415]   0.64068 [0.63276,0.64962]
         arith       disputed   0.63824 [0.63183,0.64474]   0.64791 [0.64391,0.65241]
```

The arithmetic tree reads 0.64791 on the deepest common decade. A
process with exponent 0.650919 reads 0.64796 there. A process with
exponent 0.678 reads 0.67079, and its interval does not overlap the
arithmetic one. Same conclusion on the window estimator.

All five rows use the `b13` grid, since the comparison needs the same
amount of buffer everywhere. More buffer moves the number down a little:
on the `b17` grid the arithmetic tree reads 0.6465 on that same decade
against 0.64791 here. The controls would move with it, and
`buffer_squeeze.py` bounds that shift at 0.002, well under the 0.023
separating the two hypotheses.

So E-097's `0.639` was never evidence against Kontorovich-Lagarias. It
is, to three decimals, what a process with their exponent returns under
that estimator.

The separation is conservative. Fluctuation of `log10 N(1e8)` runs 0.594
for `arith`, 0.629 for `cycq(5.000)`, 0.721 for `cycq(5.05398)`, 0.666
for `cyc` and 0.801 for `iid`. More fluctuation means more bias, so the
exponent-0.678 control carries the larger bias of the two (0.019 against
0.011 on the window estimator), which pulls its reading down toward the
arithmetic one. The bands still do not meet.

The same reasoning cuts the other way at the margin: `arith` fluctuates
slightly less than the 0.650919 control, so its own bias should be
slightly smaller, and reading the same value would then put its exponent
a hair below 0.650919. The deep run's 0.6505 is consistent with that,
and the gap is inside the 0.002 extrapolation uncertainty, so it is a
caveat and not a claim.

This is a measurement with calibrated controls, not a proof, and it
tests the exponent 0.678, not Volkov's model. That model is a complete
binary tree with a different encoding of the iterates, and it is not
implemented here.

Two systematics were checked rather than assumed. `cyc` and `cycq(5.0)`
are the same process by construction and differ by 0.0035 over six
seeds, 1.5 standard errors, so no implementation systematic above about
0.004 separates the integer recursion from the real-valued one
(`cyc_vs_cycq.py`). Putting a floor at value 1 on the real-valued walk,
where the integer recursion bottoms out, changes counts but leaves the
slope identical to five decimals.

## Deep run: the same comparison where the estimator is almost unbiased

The bias shrinks fast with depth. On the matched `b15` grid
(checkpoints `1e4..1e10`, buffers `1e9..1e15`, 300 roots, all five
processes), the per-decade bias of the controls falls to

| process | true exponent | L=6.5 | L=7.5 | L=8.5 | L=9.5 |
|---------|---------------|-------|-------|-------|-------|
| cycq 5.00000 | 0.650919 | +0.0134 | +0.0033 | +0.0010 | +0.0011 |
| cycq 5.05398 | 0.678000 | +0.0153 | +0.0060 | +0.0005 | +0.0005 |
| cyc | 0.650919 | +0.0165 | +0.0061 | +0.0013 | -0.0003 |
| iid | 0.650919 | +0.0355 | +0.0194 | +0.0087 | +0.0034 |

At decade `1e9 -> 1e10` the estimator returns the true exponent to
within 0.003 on every control, so at that depth the reading is the
exponent:

```
       process  true exponent             window estimator             decade 1e9->1e10
  cycq 5.00000       0.650919   0.63263 [0.62557,0.64025]   0.64981 [0.64884,0.65075]
  cycq 5.05398       0.678000   0.65971 [0.65310,0.66628]   0.67748 [0.67651,0.67846]
           cyc       0.650919   0.63097 [0.62435,0.63777]   0.65122 [0.65014,0.65223]
           iid       0.650919   0.61250 [0.60102,0.62336]   0.64751 [0.64387,0.65044]
         arith       disputed   0.63809 [0.63051,0.64661]   0.64926 [0.64818,0.65027]
```

Three independent processes whose exponent is 0.650919 read 0.6475,
0.6498 and 0.6512 there, the spread of 0.004 being how much the residual
bias still depends on how much each one fluctuates. The arithmetic tree
reads 0.6493, inside that band. The process whose exponent is 0.678
reads 0.6775, ten times the band away.

Pushing the arithmetic tree alone further, to checkpoints `1e12` and
buffers `1e17`, since it has no heavy tail to stall on:

| decade | slope | bootstrap | distance to 0.650919 |
|--------|-------|-----------|----------------------|
| 1e7 -> 1e8 | 0.6465 | [0.6425,0.6506] | 0.0044 |
| 1e8 -> 1e9 | 0.6487 | [0.6467,0.6506] | 0.0022 |
| 1e9 -> 1e10 | 0.6490 | [0.6479,0.6499] | 0.0020 |
| 1e10 -> 1e11 | 0.6506 | [0.6502,0.6510] | 0.0003 |
| 1e11 -> 1e12 | 0.6505 | [0.6503,0.6508] | 0.0004 |

Those bootstrap bands cover root resampling only. `buffer_squeeze.py`
bounds the other term: redoing a well-buffered decade with only the
three buffers the deepest decades have available moves it by at most
0.002, and by 0.0003 to 0.0004 from decade `1e8 -> 1e9` onward. Read the
deep decades as `0.6505 +/- 0.002`, against `alpha_-(5) = 0.650919` and
`0.678`.

The window estimator itself saturates at 0.63778 by buffer `1e17`, so
E-097's Aitken value of 0.639 for the infinite-buffer limit was right,
and the whole remaining gap to 0.6509 was window bias, not truncation.

## Notes

- `q = 7` has `d = ord_7(2) = 3 < 6`, so only the residues in `<2> =
  {1,2,4}` are fertile: four classes out of seven are sterile, not one.
  The pressure equation is unaffected, since the expected child count per
  exponent is still `1/q`.
- The enumerator needs no visited set. The forward map is a function, so
  in the reverse tree every node has at most one parent, and a cycle
  member is reachable only from inside its own cycle; roots are sampled
  outside every cycle.
