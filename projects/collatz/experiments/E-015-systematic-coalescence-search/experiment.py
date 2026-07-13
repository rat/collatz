#!/usr/bin/env python3
"""
E-015 - Testa H-015: busca sistematica de coalescencias mod 2^d, generalizando
H-014 (que e o caso d=3, k=1).

Para N = 2^d*K + r (K livre), simulamos simbolicamente ate o coeficiente de K
virar impar (ponto em que a orbita deixa de ser previsivel sem mais bits).
Representamos o estado como (C, D) onde o valor atual = C*K + D.

Para cada par (r1, r2=r1-k) com o MESMO K (mesmo d), se os dois terminam no
mesmo (C, D), as orbitas colidem para TODO K - e se steps(M) <= steps(N),
temos total_stopping_time(M) >= total_stopping_time(N) para todo K, excluindo
N=2^d*K+r1 como recordista (M=N-k < N sempre).

Reproduzir: python3 experiment.py [D_MAX] [K_MAX]
"""
import sys


def simulate(C0, D0, max_steps=500):
    """Simula ate o coeficiente de K (C) ficar impar. Retorna (C, D, steps)."""
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


def main():
    d_max = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    k_max = int(sys.argv[2]) if len(sys.argv) > 2 else 30

    # classes ja conhecidas de sessoes anteriores, para nao redescobrir como "novas"
    known_exclusions = [(3, 5)]  # H-014: N = 5 mod 8

    novos = []  # (d, r1, r2, k, steps_N, steps_M) - genuinamente novos, nao implicados por achado menor

    for d in range(2, d_max + 1):
        mod = 2 ** d
        found_this_level = []
        for r1 in range(mod):
            # pular se ja implicado por uma exclusao de modulo menor (conhecida ou achada nesta busca)
            implied = any(r1 % (2 ** d0) == r0 for d0, r0 in known_exclusions)
            if implied:
                continue
            res_N = simulate(mod, r1)
            if res_N is None:
                continue
            C_N, D_N, steps_N = res_N
            best = None
            for k in range(1, k_max + 1):
                r2 = r1 - k
                if r2 < 0:
                    continue
                res_M = simulate(mod, r2)
                if res_M is None:
                    continue
                C_M, D_M, steps_M = res_M
                if C_N == C_M and D_N == D_M and steps_M <= steps_N:
                    if best is None or k < best[0]:
                        best = (k, r2, steps_N, steps_M)
            if best is not None:
                k, r2, steps_N, steps_M = best
                found_this_level.append((d, r1, r2, k, steps_N, steps_M))

        for item in found_this_level:
            known_exclusions.append((item[0], item[1]))
            novos.append(item)

    print(f"d_max={d_max}, k_max={k_max}")
    print(f"classes conhecidas usadas como filtro inicial: {known_exclusions[:1]}")
    print(f"classes GENUINAMENTE NOVAS encontradas (nao implicadas por achado de modulo menor): {len(novos)}")
    print()

    # estatistica cumulativa: fracao de residuos mod 2^d excluidos (contando H-014 + novos ate esse d)
    print("--- fracao cumulativa de residuos mod 2^d excluidos por esta tecnica ---")
    excluidos_por_d = {}
    for d0, r0 in known_exclusions:
        for d in range(d0, d_max + 1):
            excluidos_por_d.setdefault(d, set())
            mult = 2 ** (d - d0)
            for j in range(mult):
                excluidos_por_d[d].add(r0 + j * (2 ** d0))
    for d in range(2, d_max + 1):
        count = len(excluidos_por_d.get(d, set()))
        frac = count / (2 ** d)
        print(f"  d={d:2d}: {count:6d} / {2**d:6d} residuos excluidos ({frac:.4f})")
    print()

    # verificacao contra os 148 recordistas oficiais: nenhum deveria cair numa classe excluida
    try:
        with open("../E-004-true-record-holders/oeis_A006877_record_holders.txt") as f:
            records = [int(line.strip()) for line in f if line.strip()]
        violacoes = 0
        for n in records:
            r = n % (2 ** d_max)
            if r in excluidos_por_d.get(d_max, set()):
                violacoes += 1
                print(f"  ATENCAO: recordista {n} cai em classe supostamente excluida (r={r} mod 2^{d_max})")
        print(f"verificacao contra {len(records)} recordistas oficiais: {violacoes} violacoes")
    except FileNotFoundError:
        print("(arquivo de recordistas oficiais nao encontrado - pular verificacao)")

    print()
    print("Nota: esta busca e restrita a modulo 2^d (potencias de 2) - por construcao,")
    print("NAO pode dizer nada sobre classes mod 9 (H-008), ja que 2^d e 9 sao coprimos")
    print("(nenhuma restricao mod 2^d implica nada sobre o residuo mod 9, via CRT).")


if __name__ == "__main__":
    main()
