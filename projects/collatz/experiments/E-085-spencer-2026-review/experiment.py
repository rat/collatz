#!/usr/bin/env python3
"""
E-085 - Verifica a alegacao central de Spencer, "Rooted Surjectivity
from the Invariant E/O Refinement System" (academia.edu, 2026), item
037 da colecao - ALEGACAO DE PROVA COMPLETA. Mesmo autor do item 022
(ja refutado com contraexemplo direto em H-081).

Suspeita inicial: mesma anatomia de erro do item 022 ("classe residual
ocupada" != "inteiro especifico atingido"). A INVESTIGACAO NAO CONFIRMOU
essa suspeita - ver H-085 para o veredito completo e a diferenca
estrutural encontrada.

O paper usa o mapa acelerado T(m)=(3m+1)/2^v2(3m+1) e seu inverso
R(n;k)=(2^k*n-1)/3. Diferente da arvore de H-018/item 022 (grau <=2),
esta arvore tem GRAU INFINITO: para n fixo, ha infinitos k admissiveis
da paridade certa (k=2,4,6,... se n=1 mod6; k=1,3,5,... se n=5 mod6),
cada um dando um predecessor EXATO diferente sob T (nao uma classe
residual abstrata).

Reproduzir: python3 experiment.py
"""
import sys
from collections import deque


def admissible_k_parity(n):
    """Retorna 'even', 'odd', ou None (terminal) conforme n mod 6."""
    r = n % 6
    if r == 1:
        return "even"
    elif r == 5:
        return "odd"
    else:
        return None  # n = 3 mod 6, terminal como pai inverso


def R(n, k):
    """R(n;k) = (2^k*n - 1)/3, admissivel quando 2^k*n = 1 mod 3."""
    num = (2 ** k) * n - 1
    if num % 3 != 0:
        return None
    return num // 3


def build_rooted_tree(k_max, magnitude_max, node_budget):
    """Constroi a arvore reversa REAL a partir de n=1, usando R(n;k)
    para k na paridade admissivel ate k_max, respeitando um teto de
    magnitude e um orcamento de nos processados. Retorna o conjunto de
    todos os valores impares alcancados (<=magnitude_max)."""
    reached = {1}
    queue = deque([1])
    processed = 0
    while queue and processed < node_budget:
        n = queue.popleft()
        processed += 1
        parity = admissible_k_parity(n)
        if parity is None:
            continue
        k_values = range(2, k_max + 1, 2) if parity == "even" else range(1, k_max + 1, 2)
        for k in k_values:
            m = R(n, k)
            if m is None or m < 1:
                continue
            if m > magnitude_max:
                continue
            if m not in reached:
                reached.add(m)
                queue.append(m)
    return reached


def test_coverage_of_small_odds(reached, n_max):
    """Verifica se TODOS os inteiros impares ate n_max estao em
    'reached' - o que Teorema 14.2 alega para o componente enraizado."""
    return [m for m in range(1, n_max + 1, 2) if m not in reached]


def find_unique_predecessor_chain(target, max_steps=400):
    """Segue a cadeia de predecessores UNICOS (fatoracao de 3*target+1
    em 2^k*n, n impar) de volta ate a raiz 1, sem limite de magnitude -
    usado para diagnosticar se um valor "faltante" na BFS limitada e
    um gap estrutural real ou so limitacao de orcamento/magnitude."""
    n = target
    chain = [n]
    for _ in range(max_steps):
        val = 3 * n + 1
        k = 0
        while val % 2 == 0:
            val //= 2
            k += 1
        chain.append(val)
        if val == 1:
            return chain, True
        n = val
    return chain, False


def diagnose_missing_values(missing, max_steps=400):
    """Para cada valor 'faltante' da BFS limitada, verifica via a
    cadeia de predecessores unicos SEM limite de magnitude se ele de
    fato converge a raiz - distinguindo 'gap estrutural real' de
    'limitacao de orcamento computacional desta rodada'."""
    results = []
    for m in missing:
        chain, converged = find_unique_predecessor_chain(m, max_steps)
        results.append((m, converged, len(chain) - 1, max(chain) if chain else None))
    return results


def main():
    print("=== Construindo a arvore reversa REAL a partir de n=1, orcamento crescente ===")
    configs = [
        (20, 10 ** 6, 5_000_000),
        (25, 5 * 10 ** 6, 8_000_000),
        (30, 3 * 10 ** 7, 10_000_000),
    ]
    for k_max, magnitude_max, node_budget in configs:
        reached = build_rooted_tree(k_max, magnitude_max, node_budget)
        print(f"\n  k_max={k_max}, magnitude_max={magnitude_max:.0e}, orcamento={node_budget:.0e}")
        print(f"  total de valores impares distintos alcancados: {len(reached)}")
        for n_max in (1000, 10000):
            missing = test_coverage_of_small_odds(reached, n_max)
            total = (n_max + 1) // 2
            print(f"    ate n={n_max}: {total - len(missing)}/{total} cobertos, {len(missing)} faltando")

    print()
    print("=== Diagnostico: os 'faltantes' sao gap estrutural ou limitacao de orcamento? ===")
    print("(seguindo a cadeia de predecessores unicos SEM limite de magnitude)")
    reached_small = build_rooted_tree(20, 10 ** 6, 5_000_000)
    missing_small = test_coverage_of_small_odds(reached_small, 50000)
    sample = missing_small[:5]
    for m, converged, steps, peak in diagnose_missing_values(sample):
        status = f"CONVERGE a raiz em {steps} passos (pico={peak})" if converged else f"NAO convergiu em {steps} passos testados"
        print(f"  {m}: {status}")
    print()
    print("  Conclusao: se todos os 'faltantes' convergem a raiz quando seguidos")
    print("  sem limite de magnitude, o 'gap' observado na BFS e limitacao de")
    print("  orcamento computacional desta rodada, NAO um gap estrutural real -")
    print("  diferente do item 022 (H-081), onde o gap persistia e crescia")
    print("  independente do orcamento usado.")


if __name__ == "__main__":
    main()
