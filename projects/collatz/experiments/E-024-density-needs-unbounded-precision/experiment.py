#!/usr/bin/env python3
"""
E-024 - Testa H-024: a densidade D(v) do subarvore reverso de Collatz
depende so do residuo de v mod 3^K (K finito), ou precisa de precisao
3-adica ilimitada?

Escolhe varios v distintos, todos com o MESMO residuo mod 3^K, mas
magnitudes bem diferentes, e mede a densidade de cada um usando um
orcamento de magnitude PROPORCIONAL (evitando o erro de comparar
orcamentos desiguais, ja identificado em experiments anteriores).

Reproduzir: python3 experiment.py [K] [BUDGET_BITS]
"""
import sys
sys.path.insert(0, "../E-018-reverse-tree-branching")
from experiment import build_tree_count


def main():
    K = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    budget_bits = int(sys.argv[2]) if len(sys.argv) > 2 else 24

    mod = 3 ** K
    J4 = 85
    r = J4 % mod

    print(f"K={K} (mod 3^{K}={mod}), residuo alvo = {r}, orcamento = {budget_bits} bits")
    print()

    results = []
    for mult_extra in [0, 1, 5, 20, 100]:
        v = r + mult_extra * mod
        if v % 2 == 0:
            v += mod
        if v <= 0 or v % 3 == 0:
            continue
        n_max = v * (2 ** budget_bits)
        total, odd, gens = build_tree_count(v, n_max, n_max * 5)
        density = odd / (n_max / 2)
        results.append((v, density))
        print(f"v={v:12d} (mod {mod}={v % mod})  n_max={n_max:.2e}  D(v)={density:.6f}")

    print()
    densidades = [d for _, d in results]
    print(f"razao max/min entre as densidades = {max(densidades)/min(densidades):.1f}x")
    print("=> se essa razao for grande, D(v) NAO e funcao de residuo mod 3^K limitado.")


if __name__ == "__main__":
    main()
