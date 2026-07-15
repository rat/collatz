#!/usr/bin/env python3
"""
E-060 -- H-060: verificacao do conteudo especifico de Collatz no paper
#028 (Csikos, "A Continuous Multi-Component Measure of Directed
Acyclicity (DAG-ness)", arXiv:2606.22205). O paper e, no fundo, um
paper de TEORIA DE GRAFOS/ciencia de redes (Binghamton University +
Moravian University) -- propoe uma metrica generica de "quao perto"
um grafo dirigido arbitrario esta de ser aciclico. Collatz aparece
apenas na Secao 5.2 ("The Collatz Graph"), meia pagina, como UM
exemplo numerico entre varios (Kaprekar 6174, Collatz, arvores
sinteticas) -- nao e um paper sobre Collatz.

ESCOPO DESTA REVISAO: dado que o aparato geral de teoria de grafos
(Secoes 2-4: SCCs, MFAS, raio espectral, o framework de 4 componentes
A/F/M/S) nao e especifico de Collatz e nao faz nenhuma alegacao SOBRE
a conjectura, esta revisao verifica apenas o conteudo Collatz-especifico
(Secao 5.2), sem revisar o framework geral de teoria de grafos
(fora do escopo deste projeto).

Definicao do mapa usada PELO PROPRIO PAPER (Secao 5.2): T(n) = n/2 se
n par, 3n+1 se n impar (mapa de Collatz padrao, nao acelerado).
Restringe a graph aos primeiros 2228 inteiros positivos.

PARTE 1: verifica que o "unico SCC ciclico" e de fato {1,2,4} com o
ciclo trivial, e que nenhum outro ciclo existe no grafo induzido
n=1..2228 (ou seja, todo n nesse intervalo eventualmente atinge esse
ciclo -- consistente com verificacao exaustiva de Collatz muito alem
deste intervalo, ja publicada na literatura).
PARTE 2: verifica a DIRECAO do ciclo dada as arestas reais do mapa T
definido no proprio paper -- o texto diz "the well-known 1->2->4->1
cycle", mas as arestas reais de T sao 1->4, 4->2, 2->1 (percorrendo
1->4->2->1, nao 1->2->4->1).
PARTE 3: verifica a aritmetica do Composite Score D(G) para a linha
"Collatz (1-2-4 cycle)" da Tabela 1, dados os componentes A,F,M,S que
o proprio paper afirma.
"""


def T(n):
    """Mapa de Collatz PADRAO (nao acelerado), exatamente como definido
    na Secao 5.2 do paper."""
    return n // 2 if n % 2 == 0 else 3 * n + 1


def parte1(N=2228, max_iter=10_000):
    print("=" * 90)
    print(f"PARTE 1: todo n=1..{N} atinge o ciclo {{1,2,4}}, nenhum outro ciclo existe")
    print("=" * 90)
    falhas = 0
    ciclos_encontrados = set()
    for n0 in range(1, N + 1):
        n = n0
        visitados = []
        for _ in range(max_iter):
            visitados.append(n)
            n = T(n)
            if n in visitados:
                # fechou um ciclo -- identifica
                idx = visitados.index(n)
                ciclo = tuple(sorted(visitados[idx:]))
                ciclos_encontrados.add(ciclo)
                break
        else:
            falhas += 1
            print(f"  FALHA: n0={n0} nao atingiu nenhum ciclo em {max_iter} iteracoes")
    print(f"n0=1..{N} testados, {falhas} nao resolvidos.")
    print(f"Ciclo(s) unico(s) encontrado(s): {ciclos_encontrados}")
    esperado = {(1, 2, 4)}
    print(f"Esperado pelo paper (SCC ciclico unico = {{1,2,4}}): "
          f"{'CONFIRMADO' if ciclos_encontrados == esperado else 'DIVERGE'}")
    return falhas, ciclos_encontrados


def parte2():
    print()
    print("=" * 90)
    print("PARTE 2: direcao do ciclo -- arestas reais de T(n) vs. o texto do paper")
    print("=" * 90)
    edges = {1: T(1), 2: T(2), 4: T(4)}
    print(f"T(1)={edges[1]}  (aresta real: 1 -> {edges[1]})")
    print(f"T(2)={edges[2]}  (aresta real: 2 -> {edges[2]})")
    print(f"T(4)={edges[4]}  (aresta real: 4 -> {edges[4]})")
    caminho_real = []
    n = 1
    for _ in range(3):
        caminho_real.append(n)
        n = T(n)
    print(f"\nPercorrendo as arestas reais a partir de 1: {' -> '.join(map(str, caminho_real))} -> {n} (fecha o ciclo)")
    alegado_pelo_paper = [1, 2, 4]
    print(f"O paper escreve (Secao 5.2): \"the well-known 1->2->4->1 cycle\"")
    edges_alegadas = [(alegado_pelo_paper[i], alegado_pelo_paper[(i + 1) % 3]) for i in range(3)]
    print(f"Isso implicaria as arestas: {edges_alegadas}")
    for a, b in edges_alegadas:
        real = T(a)
        bate = real == b
        print(f"  aresta alegada {a}->{b}: T({a})={real}, {'existe' if bate else 'NAO EXISTE (T(' + str(a) + ')=' + str(real) + ', nao ' + str(b) + ')'}")
    print("\n==> ACHADO: a direcao do ciclo esta invertida no texto. Pelas arestas reais")
    print("    de T(n) (definido no proprio paper), o ciclo e 1->4->2->1, nao 1->2->4->1.")
    print("    Nao afeta nenhum resultado numerico do paper (M(G), S(G), D(G) dependem so")
    print("    do TAMANHO do ciclo e da estrutura espectral, nao da ordem em que e descrito")
    print("    em palavras) -- e um erro de descricao textual, nao um erro de calculo.")


def parte3():
    print()
    print("=" * 90)
    print("PARTE 3: aritmetica do Composite Score D(G) (Tabela 1, linha 'Collatz')")
    print("=" * 90)
    A, F, M, S = 1.000, 1.000, 0.999, 0.500
    D = 0.25 * A + 0.25 * F + 0.25 * M + 0.25 * S
    print(f"A(G)={A}, F(G)={F}, M(G)={M}, S(G)={S} (valores citados pelo paper, Tabela 1)")
    print(f"D(G) = 0.25*(A+F+M+S) = {D:.4f}  (paper cita D(G)=0.875)")
    print(f"Bate (arredondado a 3 casas): {round(D, 3) == 0.875}")

    # confere tambem M(G)=1-2/2227 exatamente como o texto explica
    M_formula = 1 - 2 / 2227
    print(f"\nM(G) = 1 - (|V_max_scc|-1)/(|V_>2|-1) = 1 - (3-1)/(2228-1) = 1 - 2/2227 = {M_formula:.6f}")
    print(f"Arredondado a 3 casas: {round(M_formula, 3)} (paper cita M(G)=0.999): "
          f"{'bate' if round(M_formula, 3) == 0.999 else 'DIVERGE'}")


if __name__ == "__main__":
    falhas1, ciclos = parte1()
    parte2()
    parte3()

    print()
    print("=" * 90)
    print("VEREDITO")
    print("=" * 90)
    print(f"""
Conteudo Collatz-especifico do paper (Secao 5.2, meia pagina -- o
resto e teoria de grafos generica, fora do escopo desta revisao):
restringir T(n) aos primeiros 2228 inteiros positivos realmente produz
exatamente um SCC ciclico, {{1,2,4}} (confirmado, {falhas1} nao
resolvidos), consistente com verificacao exaustiva de Collatz muito
alem deste intervalo ja publicada. A aritmetica do Composite Score
D(G)=0.875 confere com os componentes citados.

Unico achado: o texto descreve o ciclo como "1->2->4->1", mas pelas
arestas reais do proprio mapa T(n) definido no paper, a direcao correta
e 1->4->2->1 (T(1)=4, T(4)=2, T(2)=1). Erro de descricao textual sem
consequencia numerica (nenhum dos calculos de A/F/M/S/D depende da
ordem em que o ciclo e escrito em palavras).

O paper nao faz nenhuma alegacao sobre a Conjectura de Collatz em si --
usa o grafo de Collatz restrito a um intervalo pequeno e ja conhecido
apenas como exemplo ilustrativo de sua metrica de teoria de grafos.
""")
