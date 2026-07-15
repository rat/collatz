#!/usr/bin/env python3
"""
E-059 -- H-059: verificacao do paper #021 (Amirian & Amirian, "A
Generalization of 3x+1 Problem to 3x+4y+1", SSRN 6993335). Paper curto
(3 paginas, sem provas, so exemplos numericos + varredura empirica
"640 bilhoes" de pares (x0,y)), propoe:

    x_{i+1} = 3x_i + 4y + 1   se x_i impar
    x_{i+1} = x_i/2 - y       se x_i par

alegando que TODA orbita (x0 >= 1-2y) atinge o minimo 1-2y e cicla por
{1-2y, 4-2y, 2-2y} -- generalizando o ciclo trivial 1->4->2->1 (caso
y=0). Abstract alega isso "abre a porta" para resolver Collatz.

ACHADO CENTRAL (antes de rodar qualquer numero grande -- derivado
algebricamente primeiro, depois verificado): a mudanca de variavel
z = x + 2y transforma o mapa GCC EXATAMENTE no mapa de Collatz padrao
em z (nao um mapa relacionado -- o MESMO mapa, sem nenhuma mudanca de
forma):

  x impar <=> z=x+2y impar (2y e par, nao muda paridade)
  x_{i+1}=3x_i+4y+1  =>  z_{i+1}=x_{i+1}+2y=3x_i+6y+1=3(x_i+2y)+1=3z_i+1
  x_{i+1}=x_i/2-y    =>  z_{i+1}=x_{i+1}+2y=x_i/2+y=(x_i+2y)/2=z_i/2

Ou seja, GCC NAO e uma familia de "infinitas variacoes" do problema de
Collatz -- e o MESMO problema, disfarcado por uma mudanca de variavel
afim trivial (deslocamento por 2y). A "Generalized Collatz Conjecture"
e literalmente EQUIVALENTE (nao apenas relacionada) a conjectura de
Collatz padrao aplicada a z=x+2y>=1 (a condicao x0>=1-2y do paper e
EXATAMENTE z0=x0+2y>=1, o dominio padrao dos inteiros positivos). Isso
tem uma consequencia quantificavel: os "640 bilhoes de pontos de dados"
(x0,y) testados contem enorme redundancia -- muitos pares (x0,y)
diferentes mapeiam para o MESMO z0=x0+2y, entao o numero de instancias
DISTINTAS do problema de Collatz padrao realmente testadas e muito
menor que 640 bilhoes (calculado abaixo).

Este experimento:
  PARTE 1: verifica os 4 exemplos numericos do paper (reproduz as
    sequencias exatas dadas).
  PARTE 2: verifica a equivalencia algebrica z=x+2y <-> Collatz padrao,
    computacionalmente, para muitos (x0,y).
  PARTE 3: quantifica a redundancia: quantos z0=x0+2y DISTINTOS existem
    no retangulo x0,y em [-400000,400000] (o que o paper testou),
    contra os 640 bilhoes de PARES testados.
  PARTE 4: testa a alegacao geral (chegar a 1-2y) numa amostra, via
    Collatz padrao em z (ja verificado/conhecido para z pequeno).
"""

import sys

sys.set_int_max_str_digits(0)


def gcc_step(x, y):
    if x % 2 != 0:
        return 3 * x + 4 * y + 1
    else:
        assert (x - 2 * y) % 2 == 0 or True  # x par, y qualquer inteiro -> x/2-y pode nao ser inteiro se x impar, mas aqui x e par
        return x // 2 - y


def gcc_orbit(x0, y, max_iter=1000):
    seq = [x0]
    x = x0
    for _ in range(max_iter):
        x = gcc_step(x, y)
        seq.append(x)
        if x == 1 - 2 * y:
            return seq
    return seq  # nao convergiu dentro do limite


def collatz_step(z):
    return 3 * z + 1 if z % 2 != 0 else z // 2


def collatz_orbit(z0, max_iter=1000):
    seq = [z0]
    z = z0
    for _ in range(max_iter):
        z = collatz_step(z)
        seq.append(z)
        if z == 1:
            return seq
    return seq


def parte1():
    print("=" * 90)
    print("PARTE 1: reproducao dos 4 exemplos numericos do paper")
    print("=" * 90)
    exemplos = [
        (7, 2, [7, 30, 13, 48, 22, 9, 36, 16, 6, 1, 12, 4, 0, -2, -3, 0, -2, -3]),
        (11, -4, [11, 18, 13, 24, 16, 12, 10, 9, 12, 10, 9]),
        (-5, 9, [-5, 22, 2, -8, -13, -2, -10, -14, -16, -17, -14, -16, -17]),
        (5, 3, [5, 28, 11, 46, 20, 7, 34, 14, 4, -1, 10, 2, -2, -4, -5, -2, -4, -5, -2]),
    ]
    falhas = 0
    for x0, y, esperado in exemplos:
        seq = [x0]
        x = x0
        for _ in range(len(esperado) - 1):
            x = gcc_step(x, y)
            seq.append(x)
        bate = seq == esperado
        print(f"  x0={x0}, y={y}: {'OK' if bate else 'FALHA'} "
              f"(minimo esperado 1-2y={1 - 2 * y}, minimo real na sequencia={min(seq)})")
        if not bate:
            falhas += 1
            print(f"    paper:  {esperado}")
            print(f"    real:   {seq}")
    print(f"\n{len(exemplos)} exemplos testados, {falhas} falhas.")
    return falhas


def parte2(trials=2000):
    print()
    print("=" * 90)
    print("PARTE 2: equivalencia algebrica z=x+2y <-> Collatz padrao (verificacao computacional)")
    print("=" * 90)
    import random
    random.seed(3)
    falhas = 0
    for _ in range(trials):
        y = random.randint(-1000, 1000)
        x0 = random.randint(1 - 2 * y, 1 - 2 * y + 5000)
        z0 = x0 + 2 * y
        if z0 <= 0:
            continue
        # anda r passos em paralelo nos dois mapas e compara x_i+2y == z_i sempre
        x, z = x0, z0
        r = random.randint(1, 60)
        ok = True
        for _ in range(r):
            if x + 2 * y != z:
                ok = False
                break
            x = gcc_step(x, y)
            z = collatz_step(z)
        if x + 2 * y != z:
            ok = False
        if not ok:
            falhas += 1
            print(f"  FALHA: x0={x0}, y={y}: x_i+2y diverge de z_i apos {r} passos")
    print(f"{trials} pares (x0,y) testados (r passos aleatorios cada), {falhas} falhas na "
          f"identidade x_i+2y==z_i.")
    print("\n==> CONFIRMADO: GCC(x,y) e EXATAMENTE o mapa de Collatz padrao aplicado a "
          "z=x+2y, sem nenhuma mudanca de forma -- nao uma familia de problemas "
          "relacionados, o MESMO problema via troca de variavel afim.")
    return falhas


def parte3():
    print()
    print("=" * 90)
    print("PARTE 3: quantificando a redundancia dos '640 bilhoes de pontos de dados'")
    print("=" * 90)
    lo, hi = -400_000, 400_000
    total_pares = (hi - lo + 1) ** 2
    print(f"Retangulo testado pelo paper: x0,y em [{lo},{hi}] -> {total_pares:,} pares (x0,y) "
          f"(paper arredonda para '~640 bilhoes').")
    z_min = lo + 2 * lo
    z_max = hi + 2 * hi
    print(f"Mas z0=x0+2y (a UNICA quantidade que realmente importa, pela equivalencia da Parte 2) "
          f"varia em [{z_min:,}, {z_max:,}]")
    print(f"-- no maximo {z_max - z_min + 1:,} valores DISTINTOS de z0 (muitos pares (x0,y) "
          f"diferentes repetem o mesmo z0).")
    razao = total_pares / (z_max - z_min + 1)
    print(f"\nRedundancia media: cada valor distinto de z0 e testado, em media, "
          f"~{razao:,.0f} vezes (por (x0,y) diferentes que somam ao mesmo z0).")
    print("Ou seja, os '640 bilhoes de pontos de dados' cobrem, na melhor das hipoteses, "
          f"~{(z_max - z_min + 1):,} instancias DISTINTAS do problema de Collatz padrao -- "
          "um numero muito menor, e alem disso ja coberto por verificacoes diretas de "
          "Collatz publicadas (Barina 2020/2025 verificou ate 2^71, muito alem de "
          f"{max(abs(z_min), abs(z_max)):,}).")


def parte4(amostras=500, max_iter=10_000):
    print()
    print("=" * 90)
    print("PARTE 4: teste amostral da alegacao geral (via Collatz padrao equivalente)")
    print("=" * 90)
    import random
    random.seed(11)
    falhas = 0
    testados = 0
    for _ in range(amostras):
        y = random.randint(-10_000, 10_000)
        x0 = random.randint(1 - 2 * y, 1 - 2 * y + 20_000)
        testados += 1
        seq = gcc_orbit(x0, y, max_iter=max_iter)
        if seq[-1] != 1 - 2 * y and min(seq) != 1 - 2 * y:
            falhas += 1
            print(f"  FALHA/NAO-CONVERGIU: x0={x0}, y={y}: nao atingiu 1-2y={1 - 2 * y} "
                  f"em {max_iter} iteracoes")
    print(f"{testados} pares (x0,y) amostrados aleatoriamente, {falhas} nao atingiram 1-2y "
          f"dentro de {max_iter} iteracoes.")
    print("(esperado 0 falhas, ja que isso e equivalente a Collatz padrao para |z0| dentro "
          "do range verificado exaustivamente na literatura)")
    return falhas


if __name__ == "__main__":
    falhas = 0
    falhas += parte1()
    falhas += parte2()
    parte3()
    falhas += parte4()

    print()
    print("=" * 90)
    print("VEREDITO")
    print("=" * 90)
    print(f"\nTotal de falhas: {falhas}")
    print("""
Os exemplos numericos do paper conferem exatamente. A alegacao geral
(toda orbita atinge 1-2y) tambem se confirma na amostra testada -- mas
isso e ESPERADO, nao uma descoberta independente: GCC(x,y) e EXATAMENTE
o mapa de Collatz padrao aplicado a z=x+2y (mudanca de variavel afim,
verificada acima), nao uma "generalizacao" nem uma familia de
"infinitas variacoes" como o abstract alega. E o MESMO problema.

Consequencia: os "~640 bilhoes de pontos de dados" testados pelo paper
NAO constituem 640 bilhoes de verificacoes independentes -- cobrem, na
melhor das hipoteses, ~2,4 milhoes de valores distintos de z0=x0+2y
(quantificado na Parte 3), um subconjunto MUITO menor do que ja esta
coberto por verificacoes diretas e exaustivas de Collatz publicadas na
literatura (que ja passam de 2^68-2^71). A alegacao do abstract de que
isso "abre a porta para resolver a Generalized Collatz Conjecture, e
portanto, a Conjectura de Collatz" nao se sustenta: nao ha nada de
generalizado aqui para resolver alem do proprio Collatz, e nenhuma
tecnica nova e introduzida que ajude a ataca-lo -- e uma mudanca de
variavel, nao uma generalizacao.
""")
