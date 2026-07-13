#!/usr/bin/env python3
"""
E-027 - Testa H-027: corolario de H-007 para TODO N=4 mod6 (nao so mod9/mod18).

Ideia: N=6k+4 e par, entao N/2 = M = 3k+2 e o proximo termo (1 passo de
halving). M satisfaz M = 2 mod 3 SEMPRE (3k=0mod3). Por H-007, existe
P=(2M-1)/3 < M, impar, com total_stopping_time(P) = total_stopping_time(M)+2.

Encadeando: total_stopping_time(N) = total_stopping_time(M)+1 (so um passo
de halving de N para M). Logo:
  total_stopping_time(P) = total_stopping_time(M)+2
                          = (total_stopping_time(N)-1)+2
                          = total_stopping_time(N)+1

E P = (2M-1)/3 = (2(3k+2)-1)/3 = (6k+3)/3 = 2k+1, que e sempre < N=6k+4.

Nota (revisao pos-derivacao): a prova NUNCA usa mod9, so N par com
N/2=2mod3 - ou seja, a classe correta e N=4 mod6 (mais ampla que mod9/18).
O caso N=18j+4 (metade par de H-008) e so o subcaso k=3j. Isso significa
que a "metade par" de H-008 nunca foi estruturalmente dificil - ela cai
direto em H-007 via um unico halving, sem precisar dos passos acelerados.
A parte genuinamente dificil era a metade IMPAR (H-022).

Reproduzir: python3 experiment.py [K_MAX]
"""
import sys


def total_stopping_time(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


def main():
    k_max = int(sys.argv[1]) if len(sys.argv) > 1 else 200_000

    falhas = 0
    testados = 0
    for k in range(1, k_max + 1):
        N = 6 * k + 4
        P = 2 * k + 1

        assert P < N, f"P={P} nao e menor que N={N} para k={k}"
        assert P % 2 == 1, f"P={P} nao e impar para k={k}"
        assert N % 2 == 0, f"N={N} nao e par para k={k}"

        tN = total_stopping_time(N)
        tP = total_stopping_time(P)
        testados += 1

        if tP != tN + 1:
            falhas += 1
            print(f"FALHA k={k}: N={N} tN={tN}, P={P} tP={tP} (esperado tP=tN+1={tN+1})")
            if falhas > 20:
                print("Muitas falhas, abortando.")
                break

    print(f"\nTestados: {testados} valores de k (1 a {k_max}) -- classe geral N=6k+4")
    print(f"Falhas: {falhas}")
    if falhas == 0:
        print("CONFIRMADO sem excecao: para todo N=6k+4 (k=1.." + str(k_max) + "),")
        print("existe P=2k+1 < N com total_stopping_time(P) = total_stopping_time(N)+1.")
        print("=> N (=4 mod6) nunca pode ser recordista. Isso subsume e fecha")
        print("   a metade par de H-008 (N=4 mod9 par = 4 mod18, caso k=3j).")


if __name__ == "__main__":
    main()
