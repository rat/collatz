#!/bin/sh
# E-133: the deep runs. Five processes, same roots, same checkpoints, same
# buffers, so every decade is comparable across all of them.
#
# Buffer 1e15 rather than 1e17. The stochastic controls have a heavy-tailed
# total progeny (tail index 1/0.650919 = 1.5363), so at 1e17 a single
# unlucky realization out of 300 dominates the wall time and the batch never
# ends. At 1e15 the deepest fully buffered decade is 1e9 -> 1e10, which is
# two decades deeper than the E-097 window and finishes in minutes.
#
# The arithmetic tree alone was also run to 1e17, since it has no such tail;
# see data/q5_arith_b17.txt and the deep table in the README.
cd "$(dirname "$0")" || exit 1
for m in "" "--cyc" "--iid" "--cycq 5.00000" "--cycq 5.05398"; do
  case "$m" in
    "")               tag=arith ;;
    "--cyc")          tag=cyc ;;
    "--iid")          tag=iid ;;
    "--cycq 5.00000") tag=cycq500 ;;
    "--cycq 5.05398") tag=cycq505 ;;
  esac
  echo "running $tag"
  # shellcheck disable=SC2086
  ./tree_counts --q 5 $m --roots 300 --cp 4 10 --buf 9 15 --out "data/q5_${tag}_b15.txt"
done
echo DEEP_DONE
