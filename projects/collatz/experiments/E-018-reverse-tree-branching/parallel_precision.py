#!/usr/bin/env python3
"""
Empurra a precisao das razoes (10,11) e (13,14) usando multiprocessing
(um processo por valor de t), aproveitando multiplos nucleos.

Cada t roda com um n_max proprio (calibrado pelo tamanho esperado da arvore,
para nao estourar tempo/memoria) e um multiplicador de busca modesto (5x,
que ja provou ser suficiente e evita os travamentos anteriores causados por
multiplicadores de busca exagerados).
"""
import time
from multiprocessing import Pool
from experiment import build_tree_count


def run_one(args):
    t, n_max, mult = args
    Jt = (4 ** t - 1) // 3
    search_bound = n_max * mult
    t0 = time.time()
    total, odd, gens = build_tree_count(Jt, n_max, search_bound)
    dt = time.time() - t0
    return (t, Jt, n_max, odd, dt)


def main():
    # IMPORTANTE: para comparar razoes entre t e t+1, PRECISA usar o MESMO
    # n_max para os dois - senao a razao fica contaminada pela razao dos
    # proprios n_max (erro cometido numa tentativa anterior: comparar t=10 em
    # 1e12 com t=11 em 1e13 deu razao inflada por 10x).
    # Par (10,11): mesmo n_max=1e13 para ambos (~120M nos esperados para t=10).
    # Par (13,14): mesmo n_max=1e15 para ambos (~130M nos esperados para t=13).
    configs = [
        (10, 10 ** 13, 5),
        (11, 10 ** 13, 5),
        (13, 10 ** 15, 5),
        (14, 10 ** 15, 5),
    ]

    print(f"Rodando {len(configs)} configuracoes em paralelo...")
    with Pool(processes=len(configs)) as pool:
        results = pool.map(run_one, configs)

    for t, Jt, n_max, odd, dt in sorted(results):
        print(f"t={t:2d}  J_t={Jt:12d}  n_max={n_max:.0e}  odd_nodes={odd:12d}  tempo={dt:.1f}s")

    print()
    by_t = {t: odd for t, Jt, n_max, odd, dt in results}
    if 10 in by_t and 11 in by_t:
        print(f"razao (10,11) = {by_t[11]/by_t[10]:.6f}")
    if 13 in by_t and 14 in by_t:
        print(f"razao (13,14) = {by_t[14]/by_t[13]:.6f}")


if __name__ == "__main__":
    main()
