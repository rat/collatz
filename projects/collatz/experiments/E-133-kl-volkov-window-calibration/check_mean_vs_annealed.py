#!/usr/bin/env python3
"""
E-133, part 2: check that the i.i.d. simulator reproduces the exact annealed
count of `annealed_exact.py`.

One correction has to be applied before they can be compared. The closed
form lets the root be sterile with probability 1/q, while the enumerator
draws a fertile root residue in every mode, to match the arithmetic run
whose roots are sampled with u mod q != 0. Conditioning the root to be
fertile raises the level-1 intensity from 1/q to 1/d = 1/(q-1) per
exponent, and every deeper level inherits the same factor, so the
simulator's mean is q/(q-1) times the closed form. That factor is 1.25 at
q = 5 and is divided out below.

After that, the two must agree, and they do to within the sampling error of
a heavy-tailed mean:
the total progeny of this branching random walk has tail index
alpha_+/alpha_- = 1/0.650919 = 1.5363, so its variance is infinite and the
sample mean over any finite number of realizations sits below the true mean
and moves by several percent from seed to seed. The point of this check is
that the deficit does not grow with the sample and does not depend on the
truncation buffer, which is what a genuine implementation bug would do.

Run: python3 check_mean_vs_annealed.py
"""
import math
import statistics
import subprocess
import sys

import annealed_exact as ae

HERE = __file__.rsplit("/", 1)[0]
ROOT = 1000003
FERTILE_ROOT = 5.0 / 4.0   # q/(q-1): the enumerator always starts fertile


def run(seed, nroots, cp_lo, cp_hi, buf_lo, buf_hi, out):
    subprocess.run([HERE + "/tree_counts", "--q", "5", "--iid",
                    "--fixedroot", str(ROOT), "--roots", str(nroots),
                    "--seed", str(seed), "--cp", str(cp_lo), str(cp_hi),
                    "--buf", str(buf_lo), str(buf_hi), "--out", out],
                   check=True, capture_output=True)
    rows = []
    for line in open(out):
        if line.startswith("#"):
            continue
        rows.append([int(x) for x in line.split()[2:]])
    return rows


def main():
    n_buf = 3
    print("i.i.d. simulator mean count vs exact annealed M(t), root =", ROOT)
    print(f"{'seed':>6} {'n':>8} " + "  ".join(f"t={t}" for t in (1, 2, 3, 4)))
    for seed, n in ((11, 20000), (22, 20000), (33, 20000), (44, 200000)):
        rows = run(seed, n, 7, 10, 11, 13, f"{HERE}/data/mc_{seed}_{n}.txt")
        cells = []
        for ci in range(4):
            t = math.log10(10 ** (7 + ci) / ROOT)
            m = statistics.mean(r[ci * n_buf + 2] for r in rows) - 1.0
            ex = FERTILE_ROOT * 10 ** ae.logM(t, 5)
            cells.append(f"{m/ex:6.4f}")
        print(f"{seed:>6} {n:>8} " + "  ".join(cells))

    print("\nsame quantity at three truncation buffers (seed 44, n=200000):")
    rows = run(44, 200000, 7, 10, 11, 13, f"{HERE}/data/mc_44_200000.txt")
    for bi, b in enumerate((11, 12, 13)):
        cells = []
        for ci in range(4):
            t = math.log10(10 ** (7 + ci) / ROOT)
            m = statistics.mean(r[ci * n_buf + bi] for r in rows) - 1.0
            ex = FERTILE_ROOT * 10 ** ae.logM(t, 5)
            cells.append(f"{m/ex:6.4f}")
        print(f"  buffer 1e{b}: " + "  ".join(cells))

    # the tunable-exponent mode, against the same closed form with qval
    print("\nmode cycq against the closed form with a separate value denominator:")
    for qv in ("5.00000", "5.05398"):
        subprocess.run([HERE + "/tree_counts", "--q", "5", "--cycq", qv,
                        "--fixedroot", str(ROOT), "--roots", "40000",
                        "--seed", "77", "--cp", "7", "10", "--buf", "11", "13",
                        "--out", f"{HERE}/data/mc_cycq_{qv}.txt"],
                       check=True, capture_output=True)
        rows = []
        for line in open(f"{HERE}/data/mc_cycq_{qv}.txt"):
            if not line.startswith("#"):
                rows.append([int(x) for x in line.split()[2:]])
        cells = []
        for ci in range(4):
            t = math.log10(10 ** (7 + ci) / ROOT)
            m = statistics.mean(r[ci * n_buf + 2] for r in rows) - 1.0
            ex = FERTILE_ROOT * 10 ** ae.logM(t, 5, qval=float(qv))
            cells.append(f"{m/ex:6.4f}")
        print(f"  qval={qv}: " + "  ".join(cells))


if __name__ == "__main__":
    sys.exit(main())
