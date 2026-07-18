#!/usr/bin/env python3
"""
Complemento ao experiment_ensemble.py (E-102, H-128): a conjectura de
Chang (2026) e sobre o comportamento de UMA orbita real quando T->infinito
ao longo dela (nao uma media sobre muitas orbitas curtas que terminam
rapido). O teste ensemble mistura orbitas de comprimento finito curto
(a maioria ja convergiu a n=1 bem antes do fim do max_steps testado),
entao o "platô" visto la pode ser artefato de esgotamento da amostra,
nao um limite genuino em T.

Aqui seguimos poucas orbitas UNICAS mas muito longas (n0 com centenas a
milhares de bits, usando inteiros Python de precisao arbitraria) e
registramos a evolucao cumulativa de B9(T)-B25(T) ao longo do indice
real de burst-ending dentro da MESMA orbita, do inicio ao fim.
"""
import random

random.seed(20260718)


def run_single_orbit(n0, log_every=None):
    n = n0
    n_prev = n
    X_prev = (n % 4 == 1)

    B9 = 0
    B25 = 0
    B_other = 0
    log = []  # (indice do burst-ending, B9, B25, ratio, deficit)
    i = 0  # indice de burst-ending dentro desta orbita

    steps = 0
    while n != 1 or steps == 0:
        m = 3 * n + 1
        v2 = 0
        while m % 2 == 0:
            m //= 2
            v2 += 1
        n = m
        steps += 1

        X_cur = (n % 4 == 1)
        if X_prev and not X_cur:
            cand = n_prev
            if cand % 8 == 1:
                mod32 = cand % 32
                i += 1
                if mod32 == 9:
                    B9 += 1
                elif mod32 == 25:
                    B25 += 1
                else:
                    B_other += 1
                if log_every and i % log_every == 0:
                    total = B9 + B25
                    ratio = B9 / total if total else float("nan")
                    log.append((i, steps, B9, B25, B_other, ratio, abs(ratio - 0.5)))

        n_prev = n
        X_prev = X_cur

        if n == 1 and steps > 1:
            break  # atingiu o ponto fixo, orbita "terminou"

    total = B9 + B25
    ratio = B9 / total if total else float("nan")
    log.append((i, steps, B9, B25, B_other, ratio, abs(ratio - 0.5)))
    return steps, B9, B25, B_other, log


def random_odd_with_bits(bits):
    return random.getrandbits(bits) | (1 << (bits - 1)) | 1


def main():
    print("=== E-102 (deep orbit): unica orbita longa, T crescendo dentro dela ===")
    print()
    for bits in [500, 1000, 2000, 4000, 8000]:
        n0 = random_odd_with_bits(bits)
        # log_every escalado para nao gerar log gigante
        log_every = max(1, bits // 5)
        steps, B9, B25, B_other, log = run_single_orbit(n0, log_every=log_every)
        print(f"-- n0 com {bits} bits, orbita com {steps} passos comprimidos, "
              f"{B9+B25+B_other} burst-endings na subclasse n=1 mod8 "
              f"(outros mod32 != 9,25: {B_other})")
        print(f"{'i (burst-end idx)':>18} {'passo':>8} {'B9':>8} {'B25':>8} "
              f"{'B9/total':>10} {'|ratio-0.5|':>12}")
        for row in log:
            i, s, b9, b25, bo, ratio, deficit = row
            print(f"{i:>18} {s:>8} {b9:>8} {b25:>8} {ratio:>10.5f} {deficit:>12.5f}")
        print()


if __name__ == "__main__":
    main()
