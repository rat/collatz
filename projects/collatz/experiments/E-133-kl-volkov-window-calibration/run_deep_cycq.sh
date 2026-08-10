#!/bin/sh
# E-133: the tunable-exponent controls at the same depth as run_deep.sh.
# qval solves qval^alpha = q(2^alpha - 1):
#   5.00000 -> alpha = 0.650919  (Kontorovich-Lagarias)
#   5.05398 -> alpha = 0.678     (Volkov)
# Same code, same roots, same window, same buffers, so the two readings are
# directly comparable and the difference between them is what discriminates.
cd "$(dirname "$0")" || exit 1
./tree_counts --q 5 --cycq 5.00000 --roots 300 --cp 4 12 --buf 9 17 --out data/q5_cycq500_b17.txt
./tree_counts --q 5 --cycq 5.05398 --roots 300 --cp 4 12 --buf 9 17 --out data/q5_cycq505_b17.txt
echo CYCQ_DONE
