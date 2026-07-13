#!/usr/bin/env python3
"""
E-007 - Verifica H-007: para todo N = 2 (mod 3), N > 2, M = (2N-1)/3 e um
inteiro impar menor que N cuja orbita passa por N exatamente 2 passos depois
(M -> 2N -> N), logo total_stopping_time(M) = total_stopping_time(N) + 2.
Isso prova que N nunca pode ser um recordista de stopping time (M ja o supera).
Unica excecao: N=2, onde M colapsaria em 1 (estado terminal).

Usa o mapa PADRAO (nao acelerado) para funcionar corretamente com N par ou
impar (bug encontrado em versoes anteriores: total_steps_only assumia entrada
sempre impar).

Reproduzir: python3 experiment.py [LIMIT]
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
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 200_000

    checked = 0
    edge_cases = 0
    failures = []

    for N in range(2, limit):
        if N % 3 != 2:
            continue
        assert (2 * N - 1) % 3 == 0, f"M nao e inteiro para N={N}"
        M = (2 * N - 1) // 3
        assert M % 2 == 1, f"M={M} nao e impar para N={N}"
        assert M < N, f"M={M} nao e menor que N={N}"

        if M == 1:
            edge_cases += 1
            continue

        ts_m = total_stopping_time(M)
        ts_n = total_stopping_time(N)
        checked += 1
        if ts_m - ts_n != 2:
            failures.append((N, M, ts_m, ts_n))

    print(f"limite = {limit}")
    print(f"casos verificados (N=2 mod 3, N>2) = {checked}")
    print(f"casos de borda (M=1, i.e. N=2) = {edge_cases}")
    print(f"falhas = {len(failures)}")
    if failures:
        for f in failures[:10]:
            print("  FALHA:", f)
    else:
        print("=> teorema CONFIRMADO sem excecao (fora do caso de borda N=2).")


if __name__ == "__main__":
    main()
