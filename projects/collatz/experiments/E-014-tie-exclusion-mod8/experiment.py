#!/usr/bin/env python3
"""
E-014 - Verifica H-014: para N=4u+1 com u impar (N = 5 mod 8),
total_stopping_time(N) == total_stopping_time(N-1) exatamente (empate por
coalescencia de trajetorias), o que exclui N como candidato a recordista.

Tambem verifica que nenhum dos 148 recordistas oficiais (OEIS A006877) e
=5 mod 8.

Reproduzir: python3 experiment.py [N_AMOSTRAS] [SEED]
"""
import sys
import random


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
    n_samples = int(sys.argv[1]) if len(sys.argv) > 1 else 200_000
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    rng = random.Random(seed)

    fails = 0
    for _ in range(n_samples):
        u = rng.randrange(1, 10 ** 6) * 2 + 1  # u impar
        N = 4 * u + 1
        if total_stopping_time(N) != total_stopping_time(N - 1):
            fails += 1
            if fails <= 5:
                print(f"  FALHA: N={N} sigma(N)={total_stopping_time(N)} sigma(N-1)={total_stopping_time(N-1)}")

    print(f"amostras (u impar) = {n_samples}, falhas na identidade sigma(N)=sigma(N-1) = {fails}")

    try:
        with open("../E-004-true-record-holders/oeis_A006877_record_holders.txt") as f:
            records = [int(line.strip()) for line in f if line.strip()]
        mod5_count = sum(1 for r in records if r % 8 == 5)
        print(f"recordistas oficiais (n={len(records)}) com residuo 5 mod 8: {mod5_count}")
    except FileNotFoundError:
        print("(arquivo de recordistas oficiais nao encontrado neste diretorio - pular checagem)")


if __name__ == "__main__":
    main()
