#!/usr/bin/env python3
"""
E-016 - Testa H-016: busca de coalescencia usando modulo conjunto 9*2^d,
tentando encontrar uma exclusao para a classe N=4 (mod 9) - a questao em
aberto de H-008.

Generaliza o simulador simbolico de E-015 (V=C*K+D) para C0=9*2^d em vez de
so 2^d: como 9 e impar, ele nunca e removido pelas divisoes por 2, entao
D_final mod 9 no final do prefixo deterministico e EXATAMENTE o residuo mod
9 do valor alcancado - permitindo rastrear mod 9 e mod 2^d ao mesmo tempo.

Reproduzir: python3 experiment.py [D_MAX] [K_MAX]
"""
import sys


def simulate(C0, D0, max_steps=1000):
    """Simula ate o coeficiente de K (C) ficar sem fatores de 2 removiveis
    (ou seja, ate C ficar impar). Retorna (C, D, steps)."""
    C, D = C0, D0
    steps = 0
    while C % 2 == 0:
        if D % 2 == 0:
            C //= 2
            D //= 2
        else:
            C, D = 3 * C, 3 * D + 1
        steps += 1
        if steps > max_steps:
            return None
    return C, D, steps


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
    d_max = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    k_max = int(sys.argv[2]) if len(sys.argv) > 2 else 60

    findings = []
    for d in range(1, d_max + 1):
        C0 = 9 * (2 ** d)
        for r1 in range(4, C0, 9):  # r1 = 4 mod 9, dentro de [0, C0)
            res_N = simulate(C0, r1)
            if res_N is None:
                continue
            C_N, D_N, steps_N = res_N
            for k in range(1, k_max + 1):
                r2 = r1 - k
                if r2 < 0:
                    continue
                res_M = simulate(C0, r2)
                if res_M is None:
                    continue
                C_M, D_M, steps_M = res_M
                if C_N == C_M and D_N == D_M and steps_M <= steps_N:
                    findings.append((d, r1, r2, k, steps_N, steps_M))

    print(f"d_max={d_max}, k_max={k_max}")
    print(f"coalescencias encontradas para N=4 mod 9: {len(findings)}")
    print()
    if findings:
        print(f"{'d':>3} {'C0=9*2^d':>10} {'r1':>8} {'r2':>8} {'k':>4} {'steps_N':>8} {'steps_M':>8}")
        for d, r1, r2, k, steps_N, steps_M in findings[:30]:
            C0 = 9 * (2 ** d)
            print(f"{d:>3} {C0:>10} {r1:>8} {r2:>8} {k:>4} {steps_N:>8} {steps_M:>8}")

        # verificar uma amostra com orbitas reais, K grande o suficiente (licao de E-015)
        print()
        print("--- verificacao contra orbitas reais (K de 20 a 30) ---")
        d, r1, r2, k, steps_N, steps_M = findings[0]
        C0 = 9 * (2 ** d)
        ok_count = 0
        for K in range(20, 30):
            N = C0 * K + r1
            M = C0 * K + r2
            tsN = total_stopping_time(N)
            tsM = total_stopping_time(M)
            esperado = steps_N - steps_M
            if tsN - tsM == esperado:
                ok_count += 1
            else:
                print(f"  FALHA K={K}: N={N} M={M} diff={tsN-tsM} esperado={esperado}")
        print(f"achado d={d} r1={r1} r2={r2} k={k}: {ok_count}/10 K's confirmados")
    else:
        print("Nenhuma coalescencia encontrada para a classe 4 mod 9 nesta busca.")
        print("(nao prova que nao existe - so que nao foi encontrada neste escopo)")


if __name__ == "__main__":
    main()
