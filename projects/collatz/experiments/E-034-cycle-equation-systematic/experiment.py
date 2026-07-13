#!/usr/bin/env python3
"""
E-034 - Motivado por um video ("Messing Around with Math") que redescobriu
de forma informal a equacao classica de ciclo (Steiner/Simons/de Weger) e
alegou ter achado n=13 como candidato quase-fechando um ciclo com 3
multiplicacoes e 5 divisoes.

Parte 1: verifica com a formula correta (ja usada em H-009/E-009) que NAO
existe candidato inteiro para (a=3, S=5) em nenhuma das 6 ordens possiveis -
a alegacao do video nao se sustenta sob derivacao rigorosa.

Parte 2: estende H-009/E-009 (que foi ate a=14) para um pouco alem, usando
uma janela de S mais estreita (S_min a S_min+10, em vez de +20) para manter
a explosao combinatoria sob controle, e documenta precisamente onde a
parede combinatoria pura torna forca bruta inviavel (quantificando por que
Simons & de Weger precisaram de tecnicas mais espertas - fracoes continuas
de log2(3) para restringir S, nao so mais poder computacional - para
chegar a a=68).

Reproduzir: python3 experiment.py [A_MAX] [JANELA_S] [MAX_COMPOSICOES]
"""
import sys
import math
from itertools import combinations


def compositions(total, parts):
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


def candidate_n0(a, bs):
    S = sum(bs)
    denom = 2 ** S - 3 ** a
    if denom <= 0:
        return None, None
    num = 0
    s_i = 0
    for i in range(a):
        num += 3 ** (a - 1 - i) * 2 ** s_i
        s_i += bs[i]
    if num % denom != 0:
        return None, None
    return num // denom, denom


def check_self_consistency(n0, expected_bs):
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


def part1_video_claim():
    print("=== Parte 1: verificando a alegacao do video (n=13, a=3, S=5) ===\n")
    found_any = False
    for bs in compositions(5, 3):
        n0, denom = candidate_n0(3, bs)
        if n0 is not None and n0 > 0:
            ok = check_self_consistency(n0, bs)
            print(f"  bs={bs}: n0={n0}  autoconsistente={ok}")
            found_any = True
    if not found_any:
        print("  NENHUM candidato inteiro positivo em nenhuma das 6 ordens.")
        print("  => A alegacao do video (n=13) nao se sustenta sob a formula correta.")
        print("     Provavel erro na derivacao informal deles (video explicitamente")
        print("     nao-rigoroso, 'so brincando por algumas horas').")
    print()


def part2_extended_search(a_max, window, max_comps):
    print(f"=== Parte 2: busca estendida ate a={a_max} (janela S=+{window}, "
          f"cap={max_comps:,}) ===\n")
    log2_3 = math.log2(3)
    found = []
    skipped = []

    for a in range(1, a_max + 1):
        s_min = math.floor(a * log2_3) + 1
        for S in range(s_min, s_min + window + 1):
            n_comps = math.comb(S - 1, a - 1)
            if n_comps > max_comps:
                skipped.append((a, S, n_comps))
                continue
            denom = 2 ** S - 3 ** a
            if denom <= 0:
                continue
            for bs in compositions(S, a):
                n0, _ = candidate_n0(a, bs)
                if n0 is not None and n0 > 0 and check_self_consistency(n0, bs):
                    found.append((a, S, bs, n0))

    novel = [f for f in found if f[3] != 1]
    print(f"pares (a,S) pulados por combinatoria excessiva: {len(skipped)}")
    if skipped:
        max_skip = max(skipped, key=lambda s: s[2])
        print(f"  maior pulado: a={max_skip[0]} S={max_skip[1]} "
              f"composicoes={max_skip[2]:,}")
    print(f"ciclos encontrados (bruto): {len(found)}")
    print(f"candidatos a ciclo GENUINAMENTE NOVO (n0 != 1): {len(novel)}")
    for a, S, bs, n0 in novel:
        print(f"  NOVO CANDIDATO: a={a} S={S} b={bs} => n0={n0}")
    if not novel:
        print(f"\n=> Nenhum ciclo novo em a=1..{a_max} "
              f"({'busca COMPLETA nesta janela' if not skipped else 'busca PARCIAL, ver pulados acima'}).")


def main():
    a_max = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    window = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    max_comps = int(sys.argv[3]) if len(sys.argv) > 3 else 3_000_000

    part1_video_claim()
    part2_extended_search(a_max, window, max_comps)


if __name__ == "__main__":
    main()
