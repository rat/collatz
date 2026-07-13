#!/usr/bin/env python3
"""
E-019 - Testa H-019: partindo de extremos de densidade de bits (2^k-1, todos
1; 2^k+1, quase todos 0), quantos passos ate a densidade (popcount/bitlength)
relaxar para perto de 1/2? Previsao: tempo de mistura cresce linear em k
(nao constante), porque 3n+1 e uma operacao local.

Reproduzir: python3 experiment.py [K_LIST]
"""
import sys


def bit_density(n):
    return bin(n).count("1") / n.bit_length()


def steps_to_mix(n, tol=0.08, max_steps=2_000_000):
    steps = 0
    while n > 4 and abs(bit_density(n) - 0.5) > tol:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
        if steps > max_steps:
            return None
    return steps


def main():
    ks = [int(x) for x in sys.argv[1].split(",")] if len(sys.argv) > 1 else [8, 16, 32, 64, 128, 256, 512]

    print(f"{'k':>5} {'n=2^k-1 (denso)':>18} {'n=2^k+1 (esparso)':>18}")
    for k in ks:
        n_denso = 2 ** k - 1
        n_esparso = 2 ** k + 1
        s_denso = steps_to_mix(n_denso)
        s_esparso = steps_to_mix(n_esparso)
        print(f"{k:>5} {str(s_denso):>18} {str(s_esparso):>18}")

    print()
    print("--- razao passos/k (deveria ser aprox constante se crescimento e linear em k) ---")
    for k in ks:
        n_denso = 2 ** k - 1
        n_esparso = 2 ** k + 1
        s_denso = steps_to_mix(n_denso)
        s_esparso = steps_to_mix(n_esparso)
        r_d = s_denso / k if s_denso else None
        r_e = s_esparso / k if s_esparso else None
        print(f"  k={k:4d}: denso/k={r_d}  esparso/k={r_e}")


if __name__ == "__main__":
    main()
