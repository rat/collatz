#!/bin/sh
# E-133: the deep q=5 runs. Three modes, same roots, same window, same buffers.
# Roughly 15 minutes per mode on 16 cores at buffer 1e17.
cd "$(dirname "$0")" || exit 1
./tree_counts --q 5        --roots 300 --cp 4 12 --buf 9 17 --out data/q5_arith_b17.txt
./tree_counts --q 5 --cyc  --roots 300 --cp 4 12 --buf 9 17 --out data/q5_cyc_b17.txt
./tree_counts --q 5 --iid  --roots 300 --cp 4 12 --buf 9 17 --out data/q5_iid_b17.txt
echo ALLDONE
