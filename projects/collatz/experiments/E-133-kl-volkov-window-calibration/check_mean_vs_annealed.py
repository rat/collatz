#!/usr/bin/env python3
"""
E-133, part 2: check that the i.i.d. simulator reproduces the exact annealed
count of `annealed_exact.py`.

The simulator and the closed form describe the same object, so their means
must agree. They agree to within the sampling error of a heavy-tailed mean:
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
            ex = 10 ** ae.logM(t, 5)
            cells.append(f"{m/ex:6.4f}")
        print(f"{seed:>6} {n:>8} " + "  ".join(cells))

    print("\nsame quantity at three truncation buffers (seed 44, n=200000):")
    rows = run(44, 200000, 7, 10, 11, 13, f"{HERE}/data/mc_44_200000.txt")
    for bi, b in enumerate((11, 12, 13)):
        cells = []
        for ci in range(4):
            t = math.log10(10 ** (7 + ci) / ROOT)
            m = statistics.mean(r[ci * n_buf + bi] for r in rows) - 1.0
            ex = 10 ** ae.logM(t, 5)
            cells.append(f"{m/ex:6.4f}")
        print(f"  buffer 1e{b}: " + "  ".join(cells))


if __name__ == "__main__":
    sys.exit(main())
