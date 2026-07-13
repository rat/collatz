#!/usr/bin/env python3
"""
E-009 - Testa H-009: busca por ciclos nao-triviais do mapa de Collatz em
inteiros positivos, usando a equacao de ciclo diretamente (forca bruta sobre
composicoes de S em "a" partes positivas), para "a" (numero de subidas)
pequeno. Resultado esperado: so o ciclo trivial (a=1, b=[2], n_0=1) aparece.

Formula (ver H-009): para uma sequencia de valuacoes b_1..b_a (soma S),
n_0 = [sum_{i=0}^{a-1} 3^(a-1-i) * 2^(S_i)] / (2^S - 3^a)
onde S_0=0, S_i = b_1+...+b_i.

Reproduzir: python3 experiment.py [A_MAX] [MAX_COMPOSITIONS_POR_PAR]
"""
import sys
import math
from itertools import combinations


def compositions(total, parts):
    """Gera todas as composicoes de `total` em `parts` inteiros positivos."""
    if parts == 1:
        yield (total,)
        return
    for dividers in combinations(range(1, total), parts - 1):
        prev = 0
        comp = []
        for d in dividers:
            comp.append(d - prev)
            prev = d
        comp.append(total - prev)
        yield tuple(comp)


def check_self_consistency(n0, expected_bs):
    """Roda a orbita acelerada real a partir de n0 e confere se reproduz
    exatamente a sequencia de valuacoes esperada, retornando ao proprio n0."""
    n = n0
    for b in expected_bs:
        m = 3 * n + 1
        a_real = 0
        while m % 2 == 0:
            m //= 2
            a_real += 1
        if a_real != b:
            return False
        n = m
    return n == n0


def main():
    a_max = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    max_comps = int(sys.argv[2]) if len(sys.argv) > 2 else 2_000_000

    log2_3 = math.log2(3)
    found = []
    skipped = []

    for a in range(1, a_max + 1):
        s_min = math.floor(a * log2_3) + 1
        s_max = s_min + 20
        for S in range(s_min, s_max + 1):
            n_comps = math.comb(S - 1, a - 1)
            if n_comps > max_comps:
                skipped.append((a, S, n_comps))
                continue
            denom = 2 ** S - 3 ** a
            if denom <= 0:
                continue
            for bs in compositions(S, a):
                # numerador: sum_{i=0}^{a-1} 3^(a-1-i) * 2^(S_i), S_0=0
                num = 0
                s_i = 0
                for i in range(a):
                    num += 3 ** (a - 1 - i) * 2 ** s_i
                    s_i += bs[i]
                if num % denom != 0:
                    continue
                n0 = num // denom
                if n0 <= 0:
                    continue
                if check_self_consistency(n0, bs):
                    found.append((a, S, bs, n0))

    print(f"a_max = {a_max}, max_composicoes_por_par = {max_comps}")
    print(f"pares (a,S) pulados por combinatoria excessiva: {len(skipped)}")
    if skipped:
        for s in skipped[:5]:
            print(f"  pulado: a={s[0]} S={s[1]} composicoes={s[2]}")
    print()
    # n0=1 com b=(2,2,...,2) e so o ciclo trivial 1->4->2->1 percorrido "a"
    # vezes seguidas - nao e um ciclo novo. So interessa n0 != 1.
    trivial_repeats = [f for f in found if f[3] == 1]
    novel = [f for f in found if f[3] != 1]

    print(f"ciclos encontrados (bruto): {len(found)}")
    print(f"  dos quais repeticoes do ciclo trivial (n0=1, b todo =2): {len(trivial_repeats)}")
    print(f"  candidatos a ciclo GENUINAMENTE NOVO (n0 != 1): {len(novel)}")
    for a, S, bs, n0 in novel:
        print(f"  NOVO CANDIDATO: a={a} S={S} b={bs} => n0={n0}")

    if trivial_repeats and not novel:
        print()
        print("=> Apenas repeticoes do ciclo trivial encontradas - nenhum ciclo")
        print("   novo. Consistente com Steiner/Simons/de Weger.")
    elif not found:
        print()
        print("=> ERRO: nem o ciclo trivial apareceu - bug na busca.")
    else:
        print()
        print("=> ATENCAO: candidato(s) a ciclo alem do trivial! Verificar com cuidado.")


if __name__ == "__main__":
    main()
