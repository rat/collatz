#!/usr/bin/env python3
"""
E-079 - Verifica a alegacao central de Getachew, "Unfolding the Collatz
Tree: An Indirect Structural Proof of the Collatz Conjecture" (Research
in Mathematics 12(1), 2025), item 109 da colecao - ALEGACAO DE PROVA
COMPLETA.

O paper constroi a arvore reversa g(n) (identica a de H-018 deste
projeto: todo no v tem filho 2v sempre, e filho extra (v-1)/3 se v par
e v-1 divisivel por 3, i.e. v=4 mod6) e alega provar 3 propriedades
(Teorema 9.1): (1) Cobertura - todo n aparece na arvore; (2) Aciclicidade
- unico ciclo e o trivial {1,2,4}; (3) Terminacao - todo caminho de volta
(parent-chain) e finito. A alegacao e que (1)+(2)+(3) juntas provam a
conjectura, pois o parent-chain (m/2 se par, 3m+1 se impar) e IDENTICO
ao mapa de Collatz direto - entao "n esta na arvore" + "caminho de volta
finito" = "orbita direta de n atinge 1".

SUSPEITA CENTRAL (testada aqui): o Teorema 5.1 (cobertura) prova a
igualdade da SOMA de uma formula de indexacao com N(N+1)/2 - mas essa
formula, a_{n,m}=(2n+1)*2^m, e APENAS a decomposicao unica de qualquer
inteiro positivo em parte impar vezes potencia de 2 (fato aritmetico
trivial, TOTALMENTE INDEPENDENTE de qualquer regra de ramificacao
especifica de Collatz). Isso NAO estabelece que os numeros sao
realmente ALCANCAVEIS a partir da raiz 1 pela construcao recursiva
real da arvore g(n) - que e exatamente a questao nao-trivial
equivalente a propria conjectura.

Testa:
1. A identidade de indexacao/soma do Teorema 5.1 (que o paper prova
   corretamente).
2. Que essa MESMA identidade vale de forma IDENTICA para qualquer
   regra de ramificacao (inclusive nenhuma ramificacao, so a espinha
   dorsal de potencias de 2) - provando que ela nao usa nem depende
   da regra especifica de Collatz, logo nao pode provar "cobertura"
   da arvore CONSTRUIDA (que so contem os numeros REALMENTE
   alcancaveis via a regra de ramificacao real).
3. Construcao real da arvore via BFS a partir da raiz 1 (usando a
   regra de ramificacao verdadeira) ate um limite - comparando o
   conjunto de nos REALMENTE alcancados com o conjunto {1,...,N} que
   a "prova" de cobertura alega cobrir. Para N pequeno (onde Collatz
   ja e conhecido verdadeiro), os dois devem coincidir - mas isso e
   porque sabemos empiricamente que a conjectura vale ali, nao porque
   o Teorema 5.1 tenha provado isso.

Reproduzir: python3 experiment.py
"""
import sys
from collections import deque


def indexing_sum_identity(N):
    """Formula do Teorema 5.1 (Eq. 5/6): soma de a_{n,m}=(2n+1)*2^m
    para n=0..floor((N-1)/2), m=0..floor(log2(N/(2n+1))). Deve bater
    com N(N+1)/2."""
    import math
    max_n = (N - 1) // 2
    total = 0
    for n in range(0, max_n + 1):
        k = 2 * n + 1
        max_m = int(math.log2(N / k))
        for m in range(0, max_m + 1):
            a = k * (2 ** m)
            if a <= N:
                total += a
    return total


def test_theorem_5_1(N_values=(5, 10, 15, 20, 100, 1000)):
    """Confirma que a formula de indexacao do Teorema 5.1 realmente
    bate com N(N+1)/2 - isso o paper prova corretamente, e confirmamos
    aqui por completude antes de atacar a alegacao mais forte."""
    failures = 0
    for N in N_values:
        s = indexing_sum_identity(N)
        expected = N * (N + 1) // 2
        ok = s == expected
        print(f"  N={N}: soma indexada={s}  N(N+1)/2={expected}  {'OK' if ok else 'FALHA'}")
        if not ok:
            failures += 1
    return failures


def indexing_set(N):
    """Conjunto de valores a_{n,m}=(2n+1)*2^m <= N, para n,m no range
    do Teorema 5.1 - deve ser exatamente {1,...,N} (decomposicao unica
    odd*2^m de qualquer inteiro positivo, fato aritmetico universal)."""
    import math
    max_n = (N - 1) // 2
    values = set()
    for n in range(0, max_n + 1):
        k = 2 * n + 1
        if k > N:
            continue
        max_m = int(math.log2(N / k)) if N >= k else -1
        for m in range(0, max_m + 1):
            a = k * (2 ** m)
            if a <= N:
                values.add(a)
    return values


def test_indexing_is_generic_arithmetic_fact(N=1000):
    """PONTO CENTRAL: mostra que o conjunto coberto pela formula de
    indexacao e SEMPRE {1,...,N}, TRIVIALMENTE, para qualquer N -
    porque e so a decomposicao unica odd*2^m, independente de QUALQUER
    regra de ramificacao de Collatz. Ou seja: a "prova" de cobertura
    (Teorema 5.1) usa uma identidade que nem MENCIONA a regra de
    ramificacao g(n) (Eq. 2) - ela venceria de forma identica mesmo se
    a arvore real (construida via g(n) a partir da raiz 1) so tivesse
    a espinha dorsal e NENHUM galho."""
    idx_set = indexing_set(N)
    full_set = set(range(1, N + 1))
    match = idx_set == full_set
    print(f"  N={N}: conjunto indexado == {{1,...,N}}? {match}")
    print(f"  (Este resultado NAO depende da regra de ramificacao g(n) -")
    print(f"   e so a decomposicao unica de qualquer inteiro em odd*2^m,")
    print(f"   valida para QUALQUER N, sempre, por definicao.)")
    return match


def real_reverse_collatz_tree_bfs(n_max, max_nodes=2_000_000):
    """Constroi a arvore reversa REAL via BFS a partir da raiz 1,
    usando a regra de ramificacao verdadeira do paper (identica a
    H-018 deste projeto): todo no v tem filho 2v sempre; filho extra
    (v-1)/3 se v par e (v-1) divisivel por 3 (i.e. v=4 mod6).
    Retorna o conjunto de nos <= n_max REALMENTE alcancados a partir
    da raiz por esta construcao (nao um argumento aritmetico
    independente, mas o grafo de fato)."""
    visited = {1}
    queue = deque([1])
    reached_le_nmax = {1}
    nodes_processed = 0
    while queue and nodes_processed < max_nodes:
        v = queue.popleft()
        nodes_processed += 1
        children = [2 * v]
        if v % 2 == 0 and (v - 1) % 3 == 0:
            branch_child = (v - 1) // 3
            if branch_child >= 1:
                children.append(branch_child)
        for c in children:
            if c not in visited:
                visited.add(c)
                queue.append(c)
                if c <= n_max:
                    reached_le_nmax.add(c)
    return reached_le_nmax


def test_real_tree_vs_claimed_coverage(n_max=1000):
    """Compara o conjunto REALMENTE alcancado pela construcao
    recursiva verdadeira (BFS a partir da raiz 1) com {1,...,n_max}
    (o que o Teorema 5.1 alega cobrir). Para valores pequenos onde
    Collatz ja e empiricamente verificado, os dois devem coincidir -
    mas isso e uma CONSEQUENCIA de sabermos que a conjectura vale
    nessa faixa (verificacao computacional independente), NAO uma
    demonstracao logica derivada do Teorema 5.1 (que nunca usa a
    regra de ramificacao g(n) em sua prova, como mostrado acima)."""
    reached = real_reverse_collatz_tree_bfs(n_max)
    full_set = set(range(1, n_max + 1))
    missing = full_set - reached
    match = len(missing) == 0
    print(f"  n_max={n_max}: nos realmente alcancados (BFS real a partir de 1) cobre {{1,...,{n_max}}}? {match}")
    if missing:
        print(f"  faltando: {sorted(missing)[:20]}{'...' if len(missing)>20 else ''}")
    print(f"  (Este match, quando ocorre, e porque Collatz JA E SABIDO verdadeiro")
    print(f"   nesta faixa por verificacao computacional independente - NAO e")
    print(f"   uma consequencia do argumento de indexacao do Teorema 5.1, que")
    print(f"   nunca usa g(n) e vale identicamente mesmo sem nenhuma ramificacao.)")
    return match


def main():
    print("=== Teorema 5.1: identidade de soma (o paper prova isso corretamente) ===")
    fail1 = test_theorem_5_1()
    print(f"  {fail1} falhas")
    print()

    print("=== PONTO CENTRAL: a formula de indexacao e um fato aritmetico universal ===")
    print("=== (independente de QUALQUER regra de ramificacao de Collatz) ===")
    match = test_indexing_is_generic_arithmetic_fact()
    print()

    print("=== Comparacao: arvore REAL (BFS via g(n) real) vs. alegacao de cobertura ===")
    test_real_tree_vs_claimed_coverage()


if __name__ == "__main__":
    main()
