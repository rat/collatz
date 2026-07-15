#!/usr/bin/env python3
"""
E-018b - Reescreve build_tree_count usando DFS com pilha explicita em vez
de BFS com deque+visited (experiment.py original).

Justificativa: o mapa de Collatz e uma funcao (cada u tem exatamente uma
imagem f(u)). Na arvore reversa, o UNICO pai possivel de um no w e f(w) -
nenhum no pode ser alcancado por dois pais diferentes, exceto se a busca
reentrar no ciclo trivial {1,2,4}. Para as raizes J_t usadas aqui (t>=4,
logo J_t>=85), isso nunca acontece: a orbita direta de 1 fica presa em
1->4->2->1 para sempre e nunca alcanca nenhum J_t>4. Logo o `visited` set
do BFS original e desnecessario para corretude, e e exatamente o que
causava o estouro de memoria (O(nos explorados), nao O(profundidade)) que
limitava parallel_precision.py a n_max~1e13-1e15 antes de estourar (OOM em
33GB e 61GB, ver README). DFS com pilha explicita usa O(profundidade)
memoria em vez de O(nos).

Reproduzir: python3 experiment_dfs.py [N_MAX] [SEARCH_MULT] [T_LIST]
"""
import sys
import time


def build_tree_count_dfs(j_t, n_max, search_bound):
    """DFS (pilha explicita, sem visited) a partir de j_t."""
    total_nodes = 0
    odd_nodes = 0
    max_gen = 0

    stack = [(j_t, 0)]
    while stack:
        v, gen = stack.pop()
        if gen > max_gen:
            max_gen = gen
        if v <= n_max:
            total_nodes += 1
            if v % 2 == 1:
                odd_nodes += 1
        if v <= search_bound:
            if 2 * v <= search_bound:
                stack.append((2 * v, gen + 1))
            if v % 6 == 4:
                stack.append(((v - 1) // 3, gen + 1))

    return total_nodes, odd_nodes, max_gen


def main():
    n_max = int(sys.argv[1]) if len(sys.argv) > 1 else 20_000_000
    search_mult = int(sys.argv[2]) if len(sys.argv) > 2 else 5
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
        t0 = time.time()
        total, odd, max_gen = build_tree_count_dfs(j_t, n_max, search_bound)
        dt = time.time() - t0
        results[t] = odd
        print(f"t={t:2d}  J_t={j_t:12d}  nos_totais={total:9d}  nos_impares={odd:9d}  prof_max={max_gen:4d}  tempo={dt:.1f}s")

    print()
    print("--- comparacao com referencia exata (forward scan, H-013) ---")
    referencia = {4: 237828, 5: 377838, 7: 830, 8: 4810, 10: 311, 11: 15}
    for t in ts:
        if t in results and t in referencia:
            match = "OK" if results[t] == referencia[t] else f"DIFERENCA={results[t]-referencia[t]}"
            print(f"  t={t}: arvore reversa (DFS)={results[t]}  forward_scan={referencia[t]}  {match}")


if __name__ == "__main__":
    main()
