#!/usr/bin/env python3
"""
H-096 / item 050 - Roif, "On the Convergence of the Collatz Function"
(academia.edu, V4, ALEGACAO DE PROVA).

O gap fatal esta na Secao 9 ("Closing the Gap: The Empty Container
Argument"): a "Lemma 4.3" do proprio paper afirma que todo A subset Z+
com densidade assintotica zero (d-barra(A)=0) satisfaz A=vazio. Isso e'
falso como fato matematico geral - basta um contraexemplo de conjunto
infinito com densidade zero.

Este experimento demonstra numericamente, sem ambiguidade, que
conjuntos infinitos classicos (quadrados perfeitos, potencias de 2)
tem densidade tendendo a zero mas sao obviamente infinitos e nao-vazios
- refutando "Lemma 4.3" tal como enunciada.

Reproduzir: python3 experiment.py
"""
import math


def density_of_squares(N):
    count = int(math.isqrt(N))
    return count / N


def density_of_powers_of_2(N):
    count = int(math.log2(N)) + 1
    return count / N


def main():
    print("=== Contraexemplo a 'Lemma 4.3' (densidade zero => conjunto vazio) ===\n")
    print("Conjunto A = quadrados perfeitos (obviamente infinito e nao-vazio: "
          "1,4,9,16,25,...)\n")
    print(f"{'N':>12} {'|A intersect [1,N]|':>20} {'densidade d(A)':>16}")
    for N in [10**2, 10**4, 10**6, 10**8, 10**10, 10**12]:
        count = int(math.isqrt(N))
        d = count / N
        print(f"{N:>12} {count:>20} {d:>16.2e}")
    print("\nDensidade -> 0 conforme N cresce, mas A e' claramente infinito "
          "(contem todo k^2 para todo k>=1) e nao-vazio.")
    print("Isso refuta 'Lemma 4.3' do paper tal como enunciada: "
          "densidade zero NAO implica conjunto vazio, nem mesmo finito.\n")

    print("Segundo exemplo, mesma conclusao: A = potencias de 2 "
          "(1,2,4,8,16,...)")
    print(f"{'N':>12} {'|A intersect [1,N]|':>20} {'densidade d(A)':>16}")
    for N in [10**2, 10**4, 10**6, 10**8, 10**10, 10**12]:
        count = int(math.log2(N)) + 1
        d = count / N
        print(f"{N:>12} {count:>20} {d:>16.2e}")


if __name__ == "__main__":
    main()
