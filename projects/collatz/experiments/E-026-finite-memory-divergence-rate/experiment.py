#!/usr/bin/env python3
"""
E-026 - Extensao de H-024/H-013: dado que a densidade D(v) do subarvore
reverso NAO e funcao de residuo 3-adico limitado (H-024), qual e a TAXA na
qual uma aproximacao de memoria finita (v mod 3^K) diverge do valor real,
conforme a magnitude de v cresce mantendo o residuo mod 3^K fixo?

H-024 respondeu "existe aproximacao exata de dimensao finita?" (nao).
Este experimento pergunta "a que taxa ela se degrada, e essa taxa muda com
K?" - uma pergunta nova, nao respondida antes.

Metodologia: fixa um residuo r mod 3^K (mesma base 85 = J_4, reduzida mod
3^K). Para cada K, mede D(v) para v = r + m*3^K (m crescente), com
orcamento de magnitude PROPORCIONAL (budget_bits fixo), e compara com o
D(v) do menor v daquele residuo (m=0) - o "baseline" que uma aproximacao de
memoria K usaria para prever todos os v daquele residuo.

Reproduzir: python3 experiment.py [budget_bits] [K1,K2,...] [max_mult]
"""
import sys
import time
sys.path.insert(0, "../E-018-reverse-tree-branching")
from experiment import build_tree_count

J4 = 85


def measure(v, budget_bits):
    n_max = v * (2 ** budget_bits)
    total, odd, gens = build_tree_count(v, n_max, n_max * 5)
    density = odd / (n_max / 2)
    return density


def main():
    budget_bits = int(sys.argv[1]) if len(sys.argv) > 1 else 22
    Ks = [int(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 else [4, 6, 8]
    mults = [int(x) for x in sys.argv[3].split(",")] if len(sys.argv) > 3 else [0, 2, 4, 10, 20, 40, 100, 200, 600]

    print(f"budget_bits={budget_bits} (orcamento log2(n_max/v) fixo)")
    print(f"K's testados: {Ks}")
    print()

    for K in Ks:
        mod = 3 ** K
        r = J4 % mod
        print(f"=== K={K} (mod 3^{K}={mod}), residuo alvo r={r} ===")

        baseline = None
        rows = []
        for m in mults:
            v = r + m * mod
            if v % 2 == 0:
                v += mod
            if v <= 0 or v % 3 == 0:
                continue
            t0 = time.time()
            D = measure(v, budget_bits)
            dt = time.time() - t0
            if baseline is None:
                baseline = D
            import math
            log_ratio = math.log(D / baseline) if D > 0 and baseline > 0 else float("nan")
            rows.append((m, v, D, log_ratio, dt))
            print(f"  m={m:5d}  v={v:12d}  D(v)={D:.6f}  log(D/D0)={log_ratio:+.4f}  ({dt:.1f}s)")

        print()

    print("=> se |log(D/D0)| crescer sem limite conforme m cresce (para K fixo),")
    print("   confirma divergencia continua (nao so ausencia de formula exata).")
    print("=> comparar a TAXA de crescimento entre K's diferentes: K maior deveria")
    print("   'aguentar' mais (erro menor para o mesmo m) se a profundidade extra")
    print("   de memoria realmente ajuda antes da estrutura mais profunda dominar.")


if __name__ == "__main__":
    main()
