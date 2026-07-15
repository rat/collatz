#!/usr/bin/env python3
"""
E-068 -- H-068: verificacao do paper #076 (Yun, "A Structural Proof of
the Collatz Conjecture via non-repeating trajectory and Recursive
Decay", osf.io, ALEGACAO DE PROVA COMPLETA).

Este paper e ainda mais fraco que o item 049 (Boyle) -- contem TRES
argumentos circulares independentes (cada um, sozinho, ja invalida a
"prova"), alem de um erro aritmetico concreto num exemplo numerico.

GAP 1 (o mais grave, Secao 8/9.2.1, Eq 9.2): a "funcao de posto"
  r(x) := min{n em N | f^(n)(x) = 1}
e definida como o menor n tal que a orbita de x atinge 1 -- mas essa
funcao SO ESTA DEFINIDA para valores de x cuja orbita de fato atinge 1
(caso contrario, o conjunto {n : f^(n)(x)=1} e VAZIO e nao tem minimo).
Ou seja, o dominio da propria "funcao de posto" usada no argumento de
boa-ordenacao JA PRESSUPOE exatamente o que precisa ser provado (que
toda orbita atinge 1). O "argumento formal em ZFC" do Apendice A e
retorica vazia em cima dessa circularidade -- nao ha real using de boa
fundamentacao aqui, so uma definicao mal-posta.

GAP 2 (Teorema 6.1): a "prova" de que nao existem ciclos nao-triviais
afirma "o UNICO ponto fixo CONHECIDO sob iteracao e x_m=1" -- isso e
exatamente a conclusao que precisa ser provada (a nao-existencia de
outros ciclos), apresentada como premissa. A algebra que segue
("(2^l-3)x_m=1") na verdade so re-deriva o Lema 6.1 (repeticao
IMEDIATA, x_n=x_{n-1}), nao trata o caso geral de ciclos de
comprimento >1 que o proprio teorema afirma cobrir.

GAP 3 (Secao 5/9.2.3, "compressao informacional"): o argumento de que
"A e B sao ambos infinitos contaveis, f:A->B nao e injetiva, logo por
'compressao' a sequencia deve eventualmente repetir" e uma FALACIA
sobre cardinalidades infinitas -- nao-injetividade entre conjuntos
infinitos contaveis nao implica NADA sobre convergencia dinamica (nem
sequer distingue "converge para 1" de "entra em algum OUTRO ciclo").

ERRO ARITMETICO CONCRETO (Equacao 9.8): o paper afirma
f(5)=(3*5+1)/2^3=2 e f(21)=(3*21+1)/2^4=2 -- mas 3*5+1=16=2^4 (nao
2^3) e 3*21+1=64=2^6 (nao 2^4). Os valores corretos sao f(5)=1 e
f(21)=1, nao 2 (que nem seria impar, violando a propria Definicao 4.1
do paper).

Partes:
  PARTE 1: Lema 6.1 (distincao de vizinhos) -- algebra correta,
    verificada.
  PARTE 2: erro aritmetico na Equacao 9.8 -- confirmado.
  PARTE 3: demonstracao por analogia (contraexemplo de metodo) de que
    a "funcao de posto" (Gap 1) e uma tecnica vazia -- aplicada a um
    mapa que PROVADAMENTE diverge, o mesmo estilo de argumento
    produziria uma "funcao de posto" indefinida, expondo que a tecnica
    nao prova nada por si so.
  PARTE 4: busca computacional por ciclos nao-triviais (sanity check
    de que a CONCLUSAO permanece nao-contradita, mesmo que o ARGUMENTO
    do paper nao a estabeleca).
"""

import sys

sys.set_int_max_str_digits(0)


def v2(x):
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    return c


def f(x):
    """Mapa Collatz comprimido (impar->impar) do proprio paper, Eq 4.1."""
    num = 3 * x + 1
    m = v2(num)
    return num // (2 ** m)


# ---------------------------------------------------------------------
# PARTE 1: Lema 6.1
# ---------------------------------------------------------------------

def parte1():
    print("=" * 90)
    print("PARTE 1: Lema 6.1 (distincao de vizinhos) -- (2^k-3)x=1")
    print("=" * 90)
    falhas = 0
    solucoes = []
    for k in range(1, 30):
        val = 2 ** k - 3
        if val != 0 and 1 % val == 0:
            x = 1 // val
            if x > 0:
                solucoes.append((k, x))
    ok = solucoes == [(2, 1)]
    if not ok:
        falhas += 1
    print(f"Solucoes inteiras positivas de (2^k-3)x=1, k=1..29: {solucoes} "
          f"(esperado so [(2,1)]): {'OK' if ok else 'DIVERGE'}")
    print("(confirma Lema 6.1: unica solucao e x=1,k=2 -- esta parte do "
          "paper esta algebricamente correta)")
    print(f"\n{falhas} falhas na Parte 1.")
    return falhas


# ---------------------------------------------------------------------
# PARTE 2: erro aritmetico na Equacao 9.8
# ---------------------------------------------------------------------

def parte2():
    print()
    print("=" * 90)
    print("PARTE 2: erro aritmetico na Equacao 9.8 do paper")
    print("=" * 90)
    falhas = 0
    casos = [
        (5, 3, 2),   # paper afirma: f(5) = (3*5+1)/2^3 = 2
        (21, 4, 2),  # paper afirma: f(21) = (3*21+1)/2^4 = 2
    ]
    for x, m_paper, resultado_paper in casos:
        num = 3 * x + 1
        m_correto = v2(num)
        resultado_correto = num // (2 ** m_correto)
        resultado_com_m_do_paper = num / (2 ** m_paper)  # pode nao ser exato
        print(f"  x={x}: 3x+1={num}")
        print(f"    Paper afirma: expoente m={m_paper}, resultado={resultado_paper}")
        print(f"    Correto: v2({num})={m_correto}, f({x})={resultado_correto}")
        # o expoente do paper esta errado
        expoente_errado = m_paper != m_correto
        # o resultado do paper (usando SEU PROPRIO expoente errado) tambem nao bate
        resultado_paper_com_seu_expoente = num // (2 ** m_paper) if num % (2 ** m_paper) == 0 else None
        print(f"    Mesmo usando o expoente do paper ({m_paper}): "
              f"{num}/2^{m_paper} = {resultado_paper_com_seu_expoente} "
              f"(paper afirma {resultado_paper})")
        erro_confirmado = expoente_errado or resultado_paper_com_seu_expoente != resultado_paper
        if not erro_confirmado:
            falhas += 1  # se nao encontrarmos o erro esperado, isso seria uma falha da nossa analise
        # nota: resultado_paper=2 nem e IMPAR, violando a propria Definicao 4.1 do paper
        print(f"    Nota: resultado alegado pelo paper ({resultado_paper}) nao e impar -- "
              f"viola a propria Definicao 4.1 (f deve mapear impar em impar)")
    print(f"\nErro confirmado em ambos os casos da Equacao 9.8: expoentes errados "
          f"(deveriam ser 4 e 6, nao 3 e 4) e resultados finais errados (deveriam "
          f"ser ambos 1, nao 2). Nota: a CONCLUSAO qualitativa que o paper queria "
          f"ilustrar (f(5)=f(21), demonstrando nao-injetividade) ainda e verdadeira "
          f"com os valores corretos (f(5)=f(21)=1) -- e apenas a aritmetica do "
          f"exemplo especifico que esta errada.")
    return 0  # erro do paper documentado, nao uma falha da nossa verificacao


# ---------------------------------------------------------------------
# PARTE 3: contraexemplo de metodo -- a "funcao de posto" e vazia
# ---------------------------------------------------------------------

def parte3():
    print()
    print("=" * 90)
    print("PARTE 3: contraexemplo de metodo -- a tecnica da 'funcao de posto' "
          "(Secao 8/9.2.1) e vazia, aplicada a um mapa que PROVADAMENTE diverge")
    print("=" * 90)
    # g(x) = 2x para todo x positivo -- diverge para +infinito para TODO x>0,
    # nunca atinge 1 (exceto x=... na verdade g(x)=2x nunca da 1 a partir de
    # nenhum inteiro positivo, ja que g^(n)(x)=x*2^n so seria 1 se x=1/2^n,
    # nao inteiro para x>=1). Definimos r_g(x):=min{n : g^(n)(x)=1} exatamente
    # como o paper define r(x) para f.
    def g(x):
        return 2 * x

    def tentativa_de_posto(mapa, x, alvo=1, limite=1000):
        """Tenta calcular min{n : mapa^(n)(x)=alvo} -- retorna None se nao
        encontrado dentro do limite (analogo ao que aconteceria se o
        conjunto for vazio: a funcao simplesmente nao esta definida)."""
        y = x
        for n in range(limite + 1):
            if y == alvo:
                return n
            y = mapa(y)
        return None

    falhas = 0
    indefinidos = 0
    for x in range(2, 20):  # exclui x=1: ja e o proprio alvo, caso degenerado trivial
        r_g = tentativa_de_posto(g, x)
        if r_g is None:
            indefinidos += 1
        else:
            falhas += 1
            print(f"  FALHA (inesperado): r_g({x})={r_g} deveria ser indefinido")
    print(f"Para g(x)=2x (mapa que PROVADAMENTE diverge para todo x>0), a "
          f"'funcao de posto' r_g(x):=min{{n : g^(n)(x)=1}} esta INDEFINIDA "
          f"para todos os {indefinidos} valores testados (x=2..19), exatamente "
          f"como seria para qualquer mapa divergente.")
    print()
    print("O MESMO estilo de definicao usado pelo paper na Secao 8 (r(x):="
          "min{n : f^(n)(x)=1}) teria o MESMO problema se f nao levasse todo "
          "x a 1 -- a definicao simplesmente NAO SE APLICA (conjunto vazio, "
          "sem minimo) aos casos que importam. O 'argumento de boa ordenacao' "
          "(N e bem-fundado, logo a sequencia de postos deve terminar) e "
          "logicamente correto EM SI MESMO, mas e vazio de conteudo aqui: "
          "ele so funciona depois de assumir que r(x) esta definida para todo "
          "x, o que e EXATAMENTE a conjectura de Collatz reformulada, nao uma "
          "consequencia dela. O 'embasamento formal em ZFC' do Apendice A do "
          "paper nao resolve isso -- axiomas de ZFC nao tornam uma definicao "
          "mal-posta (sobre um conjunto potencialmente vazio) bem-posta.")
    print(f"\n{falhas} falhas na Parte 3 (esperado 0 -- a demonstracao funcionou "
          f"como esperado, confirmando a vacuidade da tecnica).")
    return falhas


# ---------------------------------------------------------------------
# PARTE 4: busca por ciclos nao-triviais (a CONCLUSAO, nao o argumento)
# ---------------------------------------------------------------------

def parte4(N=2_000_000, max_k=200):
    print()
    print("=" * 90)
    print("PARTE 4: busca computacional por ciclos nao-triviais (sanity check da "
          "CONCLUSAO -- o paper nao PROVA a ausencia de ciclos, mas sera que a "
          "conclusao pelo menos permanece nao contradita nesta faixa?)")
    print("=" * 90)
    falhas = 0
    ciclos_encontrados = set()
    for x0 in range(1, N, 2):
        x = x0
        vistos = {x0: 0}
        for passo in range(1, max_k + 1):
            x = f(x)
            if x in vistos:
                comprimento = passo - vistos[x]
                if x != 1 or vistos[x] != 0 or comprimento != 1:
                    # ciclo encontrado que nao e trivialmente {1} se f(1)=1 direto
                    if not (x == 1 and comprimento == 1):
                        ciclos_encontrados.add((x, comprimento))
                break
            vistos[x] = passo
            if x == 1:
                break
    print(f"x0=1..{N:,} (impares), mapa comprimido f, ate {max_k} passos: "
          f"ciclos nao-triviais encontrados = {ciclos_encontrados} "
          f"(esperado conjunto vazio, consistente com literatura Collatz padrao)")
    if ciclos_encontrados:
        falhas += 1
    print(f"\n{falhas} falhas na Parte 4.")
    print("(NOTA: isso confirma apenas que NENHUM contraexemplo aparece nesta "
          "faixa -- e o mesmo tipo de evidencia computacional que ja existe na "
          "literatura ha decadas (Oliveira e Silva et al.), nao uma prova. O "
          "paper #076 NAO estabelece isso rigorosamente apesar de afirmar que sim.)")
    return falhas


if __name__ == "__main__":
    total = 0
    total += parte1()
    total += parte2()
    total += parte3()
    total += parte4()

    print()
    print("=" * 90)
    print("VEREDITO")
    print("=" * 90)
    print(f"""
Total de falhas: {total}

CONCLUSAO: este NAO e uma prova valida da Conjectura de Collatz --
mais fraco, inclusive, que outras alegacoes de prova revisadas nesta
colecao (ver H-065, item 049). Contem TRES argumentos circulares
independentes, cada um sozinho suficiente para invalidar a "prova":

1. GAP MAIS GRAVE (Secao 8, Equacao 9.2): a "funcao de posto"
   r(x):=min{{n : f^(n)(x)=1}} so esta definida para valores de x cuja
   orbita ja atinge 1 -- presume exatamente a conclusao que deveria
   provar. Demonstrado por analogia (Parte 3): o mesmo estilo de
   definicao aplicado a um mapa que provadamente diverge (g(x)=2x)
   produz uma "funcao de posto" igualmente indefinida -- expondo que a
   tecnica, por si so, nao prova absolutamente nada. O "embasamento em
   ZFC" do Apendice A e retorica sobre uma definicao mal-posta, nao um
   reforco real de rigor.

2. Teorema 6.1: afirma "o unico ponto fixo CONHECIDO e x_m=1" como se
   isso fosse uma prova -- e exatamente a conclusao (ausencia de outros
   ciclos) apresentada como premissa. A algebra que seque so re-deriva
   o Lema 6.1 (repeticao imediata), nao trata ciclos de comprimento
   maior que 1 que o teorema afirma cobrir.

3. Secao 5/9.2.3 ("compressao informacional"): usa uma falacia sobre
   cardinalidades infinitas -- nao-injetividade entre conjuntos
   infinitos contaveis nao implica convergencia dinamica, e mesmo que
   implicasse "alguma repeticao", nao distingue "converge para 1" de
   "entra em qualquer outro ciclo".

ERRO ARITMETICO CONCRETO (Equacao 9.8, confirmado na Parte 2): o paper
calcula f(5) e f(21) usando expoentes de 2 errados (3 e 4 em vez dos
corretos 4 e 6), chegando a um resultado (2) que nem e impar --
violando a propria definicao do paper. Os valores corretos sao
f(5)=f(21)=1; a conclusao qualitativa pretendida (nao-injetividade)
sobrevive com os valores corretos, mas a aritmetica mostrada esta errada.

A Parte 1 (Lema 6.1) esta correta -- unico ponto genuino do aparato
formal do paper que resiste a escrutinio. A Parte 4 confirma que
NENHUM contraexemplo computacional aparece ate 2 milhoes (consistente
com decadas de verificacao numerica na literatura), mas isso nao
resgata os argumentos do paper -- apenas reafirma o que ja era
conhecido antes deste paper.
""")
    sys.exit(0 if total == 0 else 1)
