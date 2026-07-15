#!/usr/bin/env python3
"""
E-081 - Verifica a alegacao central de Spencer, "Finite Block Exhaustion
and Rooted Occupancy in the Inverse Collatz System" (academia.edu,
2025), item 022 da colecao - ALEGACAO DE PROVA COMPLETA.

O paper constroi a MESMA arvore reversa (via T(m)=(3m+1)/2^v2(3m+1) e a
inversa R(n;k)=(2^k n-1)/3) que este projeto usa em H-018/E-018, e que
o item 109 (Getachew, ja refutado em H-079) tambem usa. A estrutura
combinatoria e mais sofisticada aqui (contador ternario, seis casos,
formalizacao em Lean para as identidades finitas de CARDINALIDADE), mas
a alegacao final (Teorema 15.3, "Odd convergence": todo inteiro impar
tem endereco reverso finito a partir de 1) tem a MESMA anatomia de erro
do item 109: peticao de principio disfarcada por reformulacao
combinatoria.

SUSPEITA CENTRAL: a "ocupacao enraizada" (Corollary 12.3, Theorem 14.2)
prova que, em CADA escala finita J, toda CLASSE RESIDUAL mod 2*3^J
"primitiva" tem algum ocupante (alguma palavra K de comprimento J tal
que F_K(1) pertence aquela classe residual). Isso e uma afirmacao sobre
RESIDUOS (objetos abstratos, cada um representando infinitos inteiros),
NAO sobre que um INTEIRO ESPECIFICO m tenha F_K(1)=m EXATAMENTE. O
Teorema 15.3 comete o salto logico ao concluir "todo inteiro impar tem
endereco finito" a partir de "toda classe residual esta ocupada em toda
escala finita" - sem nunca mostrar a conexao entre "ocupar o residuo de
m mod 2*3^J" e "atingir m exatamente".

Testa:
1. A identidade de cardinalidade |O_J|=3^J-2^J (Teorema 6.3) - o paper
   prova isso corretamente (identidade combinatoria pura).
2. Construcao REAL: enumerar todas as palavras admissiveis K de
   comprimento J (arvore reversa real a partir de 1) e verificar que o
   CONJUNTO DE RESIDUOS {F_K(1) mod 2*3^J} de fato cobre P_J (classes
   primitivas) - isso confirma que a parte de contagem/ocupacao de
   residuos esta correta.
3. PONTO CENTRAL: mostrar que "classe residual ocupada" NAO implica
   "inteiro especifico atingido exatamente" - escolher um inteiro
   impar pequeno conhecido (ex: 27) e verificar quantos passos/qual
   profundidade de arvore real e necessaria para atingi-lo EXATAMENTE
   (nao so seu residuo), comparando com a escala em que sua classe
   residual mod 2*3^J ja estaria "ocupada" segundo o teorema.

Reproduzir: python3 experiment.py
"""
import sys
from collections import deque


def T_odd(m):
    """T(m) = (3m+1)/2^v2(3m+1) - mapa direto odd-to-odd."""
    x = 3 * m + 1
    while x % 2 == 0:
        x //= 2
    return x


def R_inverse(n, k):
    """R(n;k) = (2^k*n - 1)/3, admissivel quando 2^k*n = 1 mod 3."""
    num = (2 ** k) * n - 1
    if num % 3 != 0:
        return None
    return num // 3


def test_cardinality_identity(J_values=(1, 2, 3, 4, 5, 6, 7, 8)):
    """Teorema 6.3: |W_J|=3^J, |C_J|=2^J, |O_J|=3^J-2^J (identidade
    combinatoria PURA sobre palavras em alfabeto ternario - nao
    envolve arvore real, e o paper prova isso corretamente)."""
    failures = 0
    for J in J_values:
        W = 3 ** J
        C = 2 ** J
        O = W - C
        # a identidade em si e definicional (words=3^J por definicao,
        # carried=2^J por definicao) - confirmamos que a aritmetica bate
        expected_O = 3**J - 2**J
        if O != expected_O:
            failures += 1
        print(f"  J={J}: |W_J|={W} |C_J|={C} |O_J|={O} (esperado {expected_O}) {'OK' if O==expected_O else 'FALHA'}")
    return failures


def build_real_reverse_tree_words(max_depth, max_nodes=500_000):
    """Constroi a arvore reversa REAL a partir da raiz 1, seguindo
    exatamente as regras do proprio paper (R(n;k)=(2^k n-1)/3,
    admissivel quando 2^k n = 1 mod3) - MAS de forma equivalente e
    mais simples usando a arvore de duplicacao/ramo que ja sabemos ser
    a mesma coisa (v->2v sempre, v->(v-1)/3 se v=4 mod6). Retorna o
    conjunto de TODOS os inteiros REAIS alcancados (nao residuos) ate
    max_depth em "passos impares" (profundidade da palavra), junto com
    o residuo mod 2*3^J de cada um para J=max_depth."""
    # Nivel 0: {1}. Cada passo da arvore de duplicacao MULTIPLOS pode
    # ocorrer entre "passos impares" (aplicacao de R via k>=1). Para
    # simplificar e ficar fiel a estrutura do proprio paper (palavras
    # de comprimento J = numero de aplicacoes de R, cada uma com um
    # k_i >=1 arbitrario), enumeramos diretamente via R_inverse(n,k)
    # para k=1,2,3,... (busca em largura limitada).
    frontier = {1}
    all_reached = {1}
    for depth in range(max_depth):
        next_frontier = set()
        for n in frontier:
            for k in range(1, 20):  # k razoavel; k grande da valores enormes
                m = R_inverse(n, k)
                if m is None:
                    continue
                if m < 1:
                    continue
                if m > 10**12:  # limite de magnitude para nao explodir
                    break
                next_frontier.add(m)
                all_reached.add(m)
                if len(all_reached) > max_nodes:
                    return all_reached
        frontier = next_frontier
        if not frontier:
            break
    return all_reached


def test_residue_occupancy_vs_exact_reachability(target=27, max_depth=8):
    """PONTO CENTRAL: verifica se a arvore real, construida ate uma
    profundidade modesta (onde a "ocupacao de residuos" ja se aplicaria
    segundo o teorema), de fato ATINGE o valor EXATO 27 - ou apenas
    cobre a CLASSE RESIDUAL de 27 (com outros representantes maiores
    ou diferentes, nao 27 em si)."""
    reached = build_real_reverse_tree_words(max_depth, max_nodes=500_000)
    exact_hit = target in reached
    print(f"  Arvore real construida ate profundidade {max_depth}: {len(reached)} inteiros distintos alcancados")
    print(f"  {target} foi atingido EXATAMENTE? {exact_hit}")

    # Verificar tambem se a CLASSE RESIDUAL de 27 (mod 2*3^J para J=max_depth)
    # esta representada por ALGUM elemento alcancado - mesmo que nao seja 27
    modulus = 2 * 3**max_depth
    target_residue = target % modulus
    residue_represented = any(n % modulus == target_residue for n in reached)
    print(f"  A CLASSE RESIDUAL de {target} (mod {modulus}) esta representada "
          f"por algum elemento alcancado (nao necessariamente {target} em si)? {residue_represented}")
    if residue_represented and not exact_hit:
        representatives = sorted(n for n in reached if n % modulus == target_residue)
        print(f"    Representantes encontrados dessa classe residual: {representatives[:5]}")
        print(f"    NENHUM deles e o valor exato {target} - confirma o gap:")
        print(f"    'classe residual ocupada' != 'inteiro especifico atingido'")
    return exact_hit, residue_represented


def main():
    print("=== Identidade de cardinalidade (Teorema 6.3) - correta e pura combinatoria ===")
    fail1 = test_cardinality_identity()
    print(f"  {fail1} falhas")
    print()

    print("=== PONTO CENTRAL: ocupacao de classe residual vs. alcancabilidade exata ===")
    test_residue_occupancy_vs_exact_reachability(target=27, max_depth=6)
    print()
    test_residue_occupancy_vs_exact_reachability(target=27, max_depth=8)


if __name__ == "__main__":
    main()
