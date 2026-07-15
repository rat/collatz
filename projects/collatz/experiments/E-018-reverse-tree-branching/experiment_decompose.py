#!/usr/bin/env python3
"""
E-018c - Decompoe D(J_t) = raiz + soma_i D(w_i) num UNICO passe de DFS,
marcando cada no com o indice i do "galho de primeiro nivel" (a partir da
espinha de duplicacao pura de J_t) a que pertence. w_1, w_2, w_3, ... sao
os filhos sucessivos via (v-1)/3 encontrados subindo a cadeia 2^g*J_t
(g=0,1,2,...) - a mesma decomposicao da recursao exata de H-018.

Motivacao: D(J_t)=Sum D(w_i) e uma soma infinita que nao fecha em formula
finita (H-024: exige residuos mod 3^k arbitrario). Aqui testamos se ela
CONVERGE RAPIDO na pratica - ou seja, se os primeiros termos ja dominam
D(J_t). Isso REDUZ (nao resolve) "por que a razao D(J_t+1)/D(J_t) oscila"
a "por que a densidade da subarvore de w_1 oscila" - w_1(t) e w_1(t+1) tem
magnitude comparavel (razao -> 2 quando t->infinito: w_1(t)=(4^(t+1)-7)/9
para t=1mod3, w_1(t+1)=(2*4^(t+1)-5)/9 para t+1=2mod3), entao qualquer
efeito de TAMANHO de primeira ordem preveria razao ~0.5 sempre - o range
observado (0.046 a 5.97) tem que vir da DENSIDADE da subarvore, nao do
tamanho do no.

Checagem de corretude embutida: raiz(=1, J_t e sempre impar) + soma de
todos os buckets == contagem total de nos impares <=n_max (deve bater com
build_tree_count_dfs). Nenhum outro no da espinha (2^g*J_t, g>=1) e impar,
entao a raiz e o UNICO no fora de qualquer bucket.

Reproduzir: python3 experiment_decompose.py [N_MAX] [SEARCH_MULT] [T]
"""
import sys


def decompose(j_t, n_max, search_bound):
    total_odd = 0
    buckets = {}
    w_list = []

    # pilha: (v, on_spine, tag). on_spine=True so na cadeia pura de J_t
    # ainda nao ramificada; tag = indice do galho (None se on_spine).
    stack = [(j_t, True, None)]
    while stack:
        v, on_spine, tag = stack.pop()
        if v <= n_max and v % 2 == 1:
            total_odd += 1
            if tag is not None:
                buckets[tag] = buckets.get(tag, 0) + 1
        if v <= search_bound:
            if on_spine:
                if 2 * v <= search_bound:
                    stack.append((2 * v, True, None))
                if v % 6 == 4:
                    w = (v - 1) // 3
                    idx = len(w_list) + 1
                    w_list.append(w)
                    stack.append((w, False, idx))
            else:
                if 2 * v <= search_bound:
                    stack.append((2 * v, False, tag))
                if v % 6 == 4:
                    w = (v - 1) // 3
                    stack.append(((v - 1) // 3, False, tag))

    return total_odd, buckets, w_list


def main():
    n_max = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 13
    search_mult = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    t = int(sys.argv[3]) if len(sys.argv) > 3 else 10

    j_t = (4 ** t - 1) // 3
    search_bound = n_max * search_mult
    print(f"t={t}  J_t={j_t}  n_max={n_max}  search_bound={search_bound}")

    total_odd, buckets, w_list = decompose(j_t, n_max, search_bound)

    print(f"D(J_t) total (nos impares <=n_max) = {total_odd}")
    print(f"galhos de primeiro nivel encontrados = {len(w_list)}")
    print()
    print("--- contribuicao acumulada por galho ---")
    acc = 1  # raiz J_t, sempre impar e sempre <=n_max nos casos usados aqui
    print(f"  [raiz J_t]                    contrib=1           acumulado={acc:12d}  fracao={acc/total_odd:.6f}")
    for i in range(1, len(w_list) + 1):
        c = buckets.get(i, 0)
        acc += c
        frac = acc / total_odd if total_odd > 0 else float("nan")
        print(f"  galho {i:3d} (w_{i}={w_list[i-1]:15d})  contrib={c:12d}  acumulado={acc:12d}  fracao={frac:.6f}")

    print()
    check = 1 + sum(buckets.values())
    print(f"checagem: raiz(1) + soma_galhos({sum(buckets.values())}) = {check}  vs total={total_odd}  {'OK' if check == total_odd else 'ERRO'}")


if __name__ == "__main__":
    main()
