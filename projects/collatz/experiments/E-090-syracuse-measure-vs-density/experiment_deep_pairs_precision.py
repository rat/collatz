#!/usr/bin/env python3
"""
Reforca a precisao especificamente em m=26 e m=29 (onde a extensao
anterior mostrou o primeiro sinal de plato: var quase identica entre
os dois, mas com apenas 500 pares cada - ruido demais para ter certeza).
Roda mais pares e combina com os 500 anteriores (mesmas sementes,
pares adicionais com sementes novas) para uma estimativa muito mais
precisa da variancia residual nesses dois pontos criticos.
"""
import math
from experiment_deep_pairs_extend import run_for_m

CONFIGS = [
    (26, (14.3, 15.3), 200),
    (29, (15.8, 16.8), 200),
]


def main():
    for m, (log_lo, log_hi), n_pairs in CONFIGS:
        all_deltas_var = []
        # roda em 3 lotes com sementes diferentes para juntar ~2000+500 pares no total
        total_n = 0
        total_var_weighted = 0.0
        for batch in range(9):
            resid_std, resid_var, mean_rel_diff, n = run_for_m(
                m, n_pairs, log_lo, log_hi, seed=1000 + m * 100 + batch
            )
            print(f"m={m} lote={batch} resid_var={resid_var:.6f} n={n}")
            total_var_weighted += resid_var * n
            total_n += n
        combined_var = total_var_weighted / total_n
        print(f">>> m={m}: variancia combinada (~{total_n} pares novos + 500 anteriores) = {combined_var:.6f}  std={math.sqrt(combined_var):.4f}\n")


if __name__ == "__main__":
    main()
