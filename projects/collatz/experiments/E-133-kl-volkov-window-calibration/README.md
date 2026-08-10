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

The question this experiment answers is not "what is the exponent". It
is "how much bias does that estimator carry", which nobody had
measured, and which decides whether the measurement can settle anything
at all.

## What is here

| file | what it does |
|------|--------------|
| `tree_counts.c` | the enumerator: arithmetic tree and two matched stochastic controls, one code path |
| `validate_vs_python.py` | byte-for-byte check of the C against the E-097 Python enumerator |
| `annealed_exact.py` | closed form for the exact annealed counting function of the model |
| `check_mean_vs_annealed.py` | the simulator reproduces that closed form |
| `compare_modes.py` | count distributions of the three modes side by side |
| `within_root_spread.py` | separates across-root from within-root fluctuation |
| `analyze.py` | the E-097 estimator, per-decade slopes, deficit against `alpha_-` |
| `run_deep.sh` | the deep runs, checkpoints to `1e12`, buffers to `1e17` |

Build and reproduce:

```
gcc -O3 -march=native -fopenmp -o tree_counts tree_counts.c -lm
python3 validate_vs_python.py          # must print VALIDATION PASSED
python3 annealed_exact.py 5
./tree_counts --q 5       --roots 300 --cp 4 8 --buf 9 13 --out data/q5_arith_b13.txt
./tree_counts --q 5 --cyc --roots 300 --cp 4 8 --buf 9 13 --out data/q5_cyc_b13.txt
./tree_counts --q 5 --iid --roots 300 --cp 4 8 --buf 9 13 --out data/q5_iid_b13.txt
python3 compare_modes.py data/q5_arith_b13.txt data/q5_cyc_b13.txt data/q5_iid_b13.txt
./run_deep.sh                          # about 45 minutes on 16 cores
```

## The three modes

They share one code path. The branch class of a node is either the true
residue or a draw, and nothing else differs:

- `arith`: `r = u mod q`, the real tree.
- `iid`: `r` drawn uniformly at every node. This is the branching random
  walk whose annealed pressure is `q^(alpha-1)/(2^alpha-1)`, so its
  counting exponent is provably `alpha_-(q) = 0.650919` at `q = 5`.
- `cyc`: the first sibling's class is drawn, and successive siblings
  advance by `c = ((2^d-1)/q) mod q`, which is what the arithmetic tree
  does exactly (H-162).

Roots in all three modes are fertile by construction. Getting this wrong
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

## Result

Standard E-097 window, `1e5..1e8`, 300 roots, truncation extrapolated to
infinite buffer by Aitken, identical estimator in all three modes:

| mode | estimator | sd of log10 N(1e8) | truth |
|------|-----------|--------------------|-------|
| iid | 0.6119 | 0.8014 | 0.650919 |
| cyc | 0.6283 | 0.6657 | 0.650919 |
| arith | 0.6364 | 0.5942 | disputed |

**The estimator under-reads by 0.039 on a process whose exponent is
known.** That is larger than the separation `Delta = 0.027` it was built
to resolve. The E-097 measurement is therefore silent on Kontorovich-
Lagarias versus Volkov, in both directions.

The obvious next step, adding 0.039 back to the arithmetic reading to
get `0.675`, is not licensed. The bias was measured on a process whose
fluctuation is visibly larger than the arithmetic tree's (sd 0.80
against 0.59), so it is not the same bias regime, and a bias measured in
one regime does not transfer to another.

Per-decade slopes, each extrapolated in the truncation buffer
separately, behave much better than the three-decade window estimator.
At the deepest decade of the standard run, `1e7 -> 1e8`, the control
bias is already down to `0.0102`, below `Delta/2`. The deep run pushes
that to decade `1e11 -> 1e12`; see `data/` and the table below.

## Deep run

Checkpoints `1e4..1e12`, buffers `1e9..1e17`, 300 roots, all three
modes. Filled in from `analyze.py` output.

Running; results land in `data/q5_{arith,cyc,iid}_b17.txt`.

## Notes

- `q = 7` has `d = ord_7(2) = 3 < 6`, so only the residues in `<2> =
  {1,2,4}` are fertile: four classes out of seven are sterile, not one.
  The pressure equation is unaffected, since the expected child count per
  exponent is still `1/q`.
- The enumerator needs no visited set. The forward map is a function, so
  in the reverse tree every node has at most one parent, and a cycle
  member is reachable only from inside its own cycle; roots are sampled
  outside every cycle.
