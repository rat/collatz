#!/usr/bin/env python3
"""
E-012 - Verifica H-012: 2^k tem predecessor impar genuino na arvore reversa
de Collatz (via 3m+1=2^k) se e somente se k e par, e nesse caso o
predecessor e exatamente soma_{i=0}^{k/2-1} 4^i (sempre impar).

Reproduzir: python3 experiment.py [K_MAX]
"""
import sys


def main():
    k_max = int(sys.argv[1]) if len(sys.argv) > 1 else 40

    for k in range(1, k_max + 1):
        v = 2 ** k
        has_pred = (v - 1) % 3 == 0
        if k % 2 == 0:
            assert has_pred, f"k={k} par deveria ter predecessor, nao teve"
            pred = (v - 1) // 3
            formula = sum(4 ** i for i in range(k // 2))
            assert pred == formula, f"formula nao bate em k={k}"
            assert pred % 2 == 1, f"predecessor nao e impar em k={k}"
            assert 3 * pred + 1 == v
        else:
            assert not has_pred, f"k={k} impar nao deveria ter predecessor, teve"

    print(f"Verificado para k=1..{k_max}: predecessor impar existe <=> k par,")
    print("formula fechada (soma de potencias de 4) confirmada, sempre impar.")


if __name__ == "__main__":
    main()
