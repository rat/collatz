#!/usr/bin/env python3
"""
E-005 - Verifica H-005: T(n) mod 3 e determinado pela paridade de a(n)
(T(n) = (3n+1)/2^a(n)), independente do residuo de n mod 3. Preve tambem que,
para termos subsequentes de uma orbita (nao o n inicial), a proporcao de
residuo 1 vs 2 mod 3 deve ser ~1:2 (nao 1:1), e nunca residuo 0.

Parte (a) e uma verificacao algebrica EXATA (deve ser 100%, nao estatistica).
Parte (b) e uma checagem de frequencia numa amostra grande de termos reais.

Reproduzir: python3 experiment.py [K_ORBITAS] [PASSOS_POR_ORBITA] [SEED]
"""
import sys
import random


def step(n):
    m = 3 * n + 1
    a = 0
    while m % 2 == 0:
        m //= 2
        a += 1
    return m, a


def main():
    k_orbits = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    steps_per_orbit = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 42
    rng = random.Random(seed)

    # --- parte (a): verificacao algebrica exata ---
    print("=== (a) verificacao exata: T(n) mod 3 == 1 se a par, 2 se a impar ===")
    total_checked = 0
    violations = 0
    residue0_after_step = 0

    for _ in range(k_orbits):
        n = rng.randrange(10 ** 6, 10 ** 9) | 1
        for _ in range(steps_per_orbit):
            m, a = step(n)
            total_checked += 1
            predicted = 1 if a % 2 == 0 else 2
            actual = m % 3
            if actual == 0:
                residue0_after_step += 1
            elif actual != predicted:
                violations += 1
                if violations <= 5:
                    print(f"  VIOLACAO: n={n} a={a} m={m} m%3={actual} previsto={predicted}")
            n = m
            if n == 1:
                break

    print(f"  total de passos verificados = {total_checked}")
    print(f"  violacoes da identidade = {violations}")
    print(f"  vezes que residuo 0 apareceu apos um passo = {residue0_after_step}")
    if violations == 0 and residue0_after_step == 0:
        print("  => identidade CONFIRMADA sem excecao (como esperado de uma prova algebrica).")
    else:
        print("  => ATENCAO: identidade falhou - revisar a demonstracao ou o codigo.")
    print()

    # --- parte (b): proporcao 1:2 prevista entre residuos 1 e 2 mod 3 ---
    print("=== (b) proporcao de residuo 1 vs 2 mod 3 em termos subsequentes (previsto 1:2) ===")
    count_1 = 0
    count_2 = 0
    for _ in range(k_orbits):
        n = rng.randrange(10 ** 6, 10 ** 9) | 1
        for _ in range(steps_per_orbit):
            m, a = step(n)
            r = m % 3
            if r == 1:
                count_1 += 1
            elif r == 2:
                count_2 += 1
            n = m
            if n == 1:
                break

    total = count_1 + count_2
    frac_1 = count_1 / total
    frac_2 = count_2 / total
    print(f"  residuo 1 mod 3: {count_1} ({frac_1:.4f})  -- previsto 1/3 = 0.3333")
    print(f"  residuo 2 mod 3: {count_2} ({frac_2:.4f})  -- previsto 2/3 = 0.6667")
    print(f"  razao observada 1:2 = {count_1/count_2:.4f}  (previsto 0.5000)")


if __name__ == "__main__":
    main()
