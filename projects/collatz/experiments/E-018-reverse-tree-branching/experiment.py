#!/usr/bin/env python3
"""
E-018 - Testa H-018: constroi a arvore reversa de Collatz explicitamente
(BFS a partir de J_t, respeitando a regra de ramificacao mod 6) e compara
com os dados empiricos de H-013 (deve bater exatamente, pois e o mesmo
conjunto por construcao).

Regra: todo no v tem predecessor 2v sempre; e (v-1)/3 se v par e v=4 mod6.

CUIDADO (bug corrigido): um "filho" via ramo impar ((v-1)/3) pode ser MENOR
que n_max mesmo que o "pai" v (alcancado so apos varias duplicacoes) exceda
n_max - cortar a busca assim que v>n_max perde essas excursoes. A busca
precisa de um limite generoso (SEARCH_BOUND >> n_max) separado do limite de
CONTAGEM final (n_max).

Reproduzir: python3 experiment.py [N_MAX] [SEARCH_MULT] [T_LIST]
"""
import sys
from collections import deque


def predecessors(v, search_bound):
    preds = [2 * v] if 2 * v <= search_bound else []
    if v % 6 == 4:
        m = (v - 1) // 3
        preds.append(m)  # sempre menor que v, nunca precisa checar bound aqui
    return preds


def build_tree_count(j_t, n_max, search_bound):
    """BFS a partir de j_t. Explora ate search_bound, conta nos <= n_max."""
    total_nodes = 0
    odd_nodes = 0
    gen_counts_within_nmax = []

    queue = deque([(j_t, 0)])
    visited = set()
    while queue:
        v, gen = queue.popleft()
        if v in visited:
            continue
        visited.add(v)
        if v <= n_max:
            total_nodes += 1
            if v % 2 == 1:
                odd_nodes += 1
            while len(gen_counts_within_nmax) <= gen:
                gen_counts_within_nmax.append(0)
            gen_counts_within_nmax[gen] += 1
        if v <= search_bound:
            for p in predecessors(v, search_bound):
                if p not in visited:
                    queue.append((p, gen + 1))

    return total_nodes, odd_nodes, gen_counts_within_nmax


def main():
    n_max = int(sys.argv[1]) if len(sys.argv) > 1 else 20_000_000
    search_mult = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    ts = [int(x) for x in sys.argv[3].split(",")] if len(sys.argv) > 3 else [4, 5, 7, 8, 10, 11]

    search_bound = n_max * search_mult
    print(f"n_max = {n_max}, search_bound = {search_bound} (mult={search_mult})")
    print()
    results = {}
    for t in ts:
        j_t = (4 ** t - 1) // 3
        if j_t > n_max:
            print(f"t={t}: J_t={j_t} > n_max, pulando")
            continue
        total, odd, gen_counts = build_tree_count(j_t, n_max, search_bound)
        results[t] = odd
        print(f"t={t:2d}  J_t={j_t:9d}  nos_totais={total:8d}  nos_impares={odd:8d}")

    print()
    print("--- comparacao com H-013 (contagem exata via forward scan) ---")
    referencia = {4: 237828, 5: 377838, 7: 830, 8: 4810, 10: 311, 11: 15}
    for t in ts:
        if t in results and t in referencia:
            match = "OK" if results[t] == referencia[t] else f"diferenca={results[t]-referencia[t]}"
            print(f"  t={t}: arvore reversa={results[t]}  forward_scan={referencia[t]}  {match}")

    print()
    print("--- geracao do primeiro checkpoint (mod6=4) na cadeia de duplicacao de J_t ---")
    for t in ts:
        j_t = (4 ** t - 1) // 3
        v = j_t
        gen = 0
        while v % 6 != 4 and gen < 20:
            v *= 2
            gen += 1
        print(f"  t={t:2d}  J_t mod3={j_t%3}  primeiro checkpoint na geracao (duplicacoes)={gen}")


if __name__ == "__main__":
    main()
