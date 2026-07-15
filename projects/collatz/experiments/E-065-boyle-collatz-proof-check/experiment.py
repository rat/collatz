#!/usr/bin/env python3
"""
E-065 -- H-065: verificacao do paper #049 (Boyle, "The Collatz
Conjecture is True", alegacao de prova completa).

Este e um paper de ALEGACAO DE PROVA (nao peer-reviewed, rxiverse.org).
A estrutura do "proof by induction" (Secao 4) e:
  Teorema 4.1 + Lemma 4.2 (sem divergencia) + Lemma 4.3 (sem ciclo
  nao-trivial) + Lemma 4.4 (logo, alcanca 1) => Teorema 4.5 (Collatz
  vale para todo n).

GAP PRINCIPAL (fatal, localizado no Lemma 4.2): o argumento de
"nao-divergencia" (Secao 3, Teorema 3.2) deriva P{C^k(n) par}->2/3
tratando a paridade de C^k(n) como um processo de moeda (cara/coroa)
com P=1/2 a cada passo -- mas isso vem do Lema 3.1, que e uma
afirmacao de DENSIDADE sobre o conjunto de todos os pares (metade dos
pares, ao dividir por 2, da par), nao um fato sobre a orbita
DETERMINISTICA de um n especifico. O Lemma 4.2 entao SUBSTITUI esses
valores de "e" e "o" (=2/3, 1/3), derivados sob uma hipotese de "n
aleatorio", diretamente na Equacao 4.4, que e sobre UMA trajetoria
hipotetica ESPECIFICA e FIXA (a gerada por n+1, assumida divergente).
Nao ha nenhuma razao logica para que a frequencia assintotica de
paridade de uma orbita deterministica especifica seja forcada a igualar
a media heuristica do "ensemble" de todos os n. Esta e exatamente a
falacia do "argumento probabilistico" ja bem documentada na literatura
(citada pelo proprio paper como fonte da tecnica: Rocherz [6], um post
de StackExchange sobre um argumento heuristico -- nao uma prova).

GAP SECUNDARIO (Lemma 4.3, equacoes 4.28-4.35): a fatoracao
2^(n+1)-1 = (2^((n+1)/2)-1)(2^((n+1)/2)+1) pressupoe que n+1 e PAR
(para que (n+1)/2 seja um expoente inteiro). O caso n+1 IMPAR nunca e
tratado separadamente. Verificamos computacionalmente (Parte 2) que a
CONCLUSAO NUMERICA (unica solucao nao-degenerada e n=1) sobrevive --
mas a demonstracao, como escrita, tem essa lacuna nao endereçada.

Partes:
  PARTE 1: verificacao algebrica das exclusoes de ciclo de 2,3,4 termos
    (Equacoes 4.6-4.16) -- aritmetica simples, correta no paper.
  PARTE 2: busca exaustiva de solucoes da equacao diofantina
    2^(n+1)-3^m=1 (Equacao 4.26), incluindo o caso n+1 impar que o
    paper nao trata -- confirma que so (n+1,m)=(1,0) e (2,1) existem
    no intervalo testado (a conclusao do paper sobrevive apesar do gap).
  PARTE 3 (o ponto central): verificacao da aritmetica da serie
    geometrica (Equacao 3.3-3.5, arredondamento correto do limite 2/3),
    e -- mais importante -- demonstracao quantitativa de que a fracao
    REALIZADA de passos pares varia substancialmente de trajetoria
    individual para trajetoria individual (mesmo entre as conhecidas,
    que convergem), refutando a premissa implicita de que 2/3 seria
    uma restricao rigida por trajetoria em vez de uma media de
    ensemble. Tambem reproduz o proprio calculo do paper (Fig 3).
"""

import sys
import random
import statistics

sys.set_int_max_str_digits(0)


def C(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1


# ---------------------------------------------------------------------
# PARTE 1: exclusoes de ciclo de 2, 3, 4 termos (Eq 4.6-4.16)
# ---------------------------------------------------------------------

def parte1():
    print("=" * 90)
    print("PARTE 1: aritmetica das exclusoes de ciclo de 2, 3 e 4 termos")
    print("=" * 90)
    falhas = 0
    from fractions import Fraction as F

    # Eq 4.6-4.7: 2k = 3k+1 => k=-1
    k = F(1, 1)  # resolvendo 2k-3k=1 => -k=1 => k=-1
    k_calc = -F(1, 1)
    ok = (2 * k_calc == 3 * k_calc + 1)
    if not ok:
        falhas += 1
    print(f"Eq 4.6-4.7 (ciclo de 2 termos): k=-1 satisfaz 2k=3k+1? {ok}")

    # Eq 4.8-4.9: 2k = (3k+1)/2 => k=1
    k_calc = F(1, 1)
    ok = (2 * k_calc == F(3 * k_calc + 1, 2))
    if not ok:
        falhas += 1
    print(f"Eq 4.8-4.9 (ciclo de 3 termos, k=1): 2k=(3k+1)/2? {ok} "
          f"(k=1 recupera o ciclo trivial 1,4,2)")

    # Eq 4.13-4.14: 2k = (9k+5)/2 => k=-1
    k_calc = -F(1, 1)
    ok = (2 * k_calc == F(9 * k_calc + 5, 2))
    if not ok:
        falhas += 1
    print(f"Eq 4.13-4.14 (ciclo de 4 termos, ramo O): k=-1 satisfaz 2k=(9k+5)/2? {ok}")

    # Eq 4.15-4.16: 2k = (3k+1)/4 => k=1/5
    k_calc = F(1, 5)
    ok = (2 * k_calc == F(3 * k_calc + 1, 4))
    if not ok:
        falhas += 1
    print(f"Eq 4.15-4.16 (ciclo de 4 termos, ramo E): k=1/5 satisfaz 2k=(3k+1)/4? {ok}")
    print("(nenhum dos k encontrados para 2, 3 ou 4 termos e um novo natural > 1 -- "
          "aritmetica correta, sem falhas nesta parte)")

    print(f"\n{falhas} falhas na Parte 1.")
    return falhas


# ---------------------------------------------------------------------
# PARTE 2: equacao diofantina 2^(n+1) - 3^m = 1 (Eq 4.26), incluindo
# o caso n+1 IMPAR que o paper nao trata
# ---------------------------------------------------------------------

def parte2(limite=2000):
    print()
    print("=" * 90)
    print(f"PARTE 2: solucoes de 2^(n+1)-3^m=1 para n+1=1..{limite} (par E impar)")
    print("=" * 90)
    solucoes = []
    for expo in range(1, limite + 1):
        val = 2 ** expo - 1
        # val = 3^m ?
        m = 0
        v = val
        while v % 3 == 0:
            v //= 3
            m += 1
        if v == 1:
            solucoes.append((expo, m, expo % 2 == 0))

    print(f"Solucoes encontradas (n+1, m, n+1_e_par): {solucoes}")
    esperado = [(1, 0, False), (2, 1, True)]
    ok = solucoes == esperado
    print(f"Esperado (conclusao do paper: so n=1, ou seja n+1=2): {esperado}")
    print(f"Bate exatamente: {ok}")
    print()
    print("NOTA: a derivacao do paper (Eq 4.28: fatoracao como diferenca de "
          "quadrados) so faz sentido se n+1 for PAR -- o caso n+1 IMPAR nunca e "
          "tratado separadamente no texto. A busca exaustiva acima INCLUI ambos "
          "os casos e confirma que a solucao impar (n+1=1, m=0, grau degenerado "
          "sem fatores de 3) nao produz um ciclo genuino adicional -- a conclusao "
          "numerica do paper sobrevive, mas a demonstracao como escrita tem essa "
          "lacuna nao endereçada.")

    falhas = 0 if ok else 1
    print(f"\n{falhas} falhas na Parte 2 (quanto a conclusao numerica; a lacuna "
          f"de caso par/impar na DEMONSTRACAO em si e reportada textualmente, "
          f"nao como falha computacional).")
    return falhas


# ---------------------------------------------------------------------
# PARTE 3: o ponto central -- ensemble vs. trajetoria individual
# ---------------------------------------------------------------------

def parte3_serie_geometrica():
    print()
    print("=" * 90)
    print("PARTE 3a: aritmetica da serie geometrica (Eq 3.3-3.5)")
    print("=" * 90)
    from fractions import Fraction as F
    # soma parcial P_k = 1 - 1/2 + 1/4 - ... + (-1/2)^k, limite deveria ser 2/3
    falhas = 0
    parcial = F(0)
    for k in range(0, 200):
        parcial += F((-1) ** k, 2 ** k) if k > 0 else F(1)
        # a formula do paper e uma soma alternada comecando em 1
    limite_calc = F(1) / (1 - F(-1, 2))
    ok = limite_calc == F(2, 3)
    if not ok:
        falhas += 1
    print(f"Limite da serie geometrica a=1, r=-1/2: soma=1/(1-r)={limite_calc} "
          f"(esperado 2/3): {ok}")
    print("(a aritmetica da serie em si esta correta -- o problema NAO e um erro "
          "de calculo, e a validade conceitual de aplicar esse modelo probabilistico "
          "a uma trajetoria deterministica especifica, testado abaixo)")
    print(f"\n{falhas} falhas na Parte 3a.")
    return falhas


def parte3_variancia_individual(n_trials=20000, max_n=10 ** 12, seed=1, K=10):
    print()
    print("=" * 90)
    print("PARTE 3b: variancia da fracao de passos pares ENTRE trajetorias "
          "individuais (vs. a media de ensemble alegada = 2/3)")
    print("=" * 90)
    random.seed(seed)

    # (i) reproduz o metodo do proprio paper (Fig 3): fracao de PARES entre
    # os primeiros K termos, para uma amostra grande de n aleatorios.
    contagem_par_por_termo = [0] * (K + 1)
    amostra = [random.randint(1, max_n) | 1 for _ in range(n_trials)]  # so impares, como no paper (comeca de n aleatorio)
    for n0 in amostra:
        x = n0
        for t in range(1, K + 1):
            x = C(x)
            if x % 2 == 0:
                contagem_par_por_termo[t] += 1
    print("Reproducao do metodo da Fig 3 do paper (fracao par por termo, "
          f"{n_trials} trajetorias aleatorias):")
    for t in range(1, K + 1):
        frac = contagem_par_por_termo[t] / n_trials
        print(f"  termo {t}: fracao par observada = {frac:.4f}")
    print("(consistente com o proprio Fig 3/5 do paper: aproxima-se de 2/3 GRADUALMENTE "
          "e por MEDIA sobre muitas trajetorias -- nao e um valor fixo a cada termo)")

    # (ii) o ponto central: para trajetorias INDIVIDUAIS completas (ate
    # alcancar 1), qual e a fracao de passos pares REALIZADA por essa
    # unica trajetoria? Mostra variancia substancial entre trajetorias.
    fracoes_individuais = []
    for n0 in random.sample(range(3, 10 ** 6, 2), 3000):
        x = n0
        pares = 0
        total = 0
        visto = set()
        while x != 1 and total < 100000:
            x = C(x)
            total += 1
            if x % 2 == 0:
                pares += 1
        if x == 1 and total > 0:
            fracoes_individuais.append(pares / total)

    media = statistics.mean(fracoes_individuais)
    desvio = statistics.stdev(fracoes_individuais)
    minimo = min(fracoes_individuais)
    maximo = max(fracoes_individuais)
    print(f"\nFracao de passos pares REALIZADA por trajetoria individual completa "
          f"(n=3..10^6, amostra de {len(fracoes_individuais)} trajetorias ate 1):")
    print(f"  media={media:.4f} (proximo de 2/3={2 / 3:.4f}, como esperado -- "
          f"isso e o QUE O PAPER MOSTRA em Fig 3/5)")
    print(f"  desvio-padrao={desvio:.4f}, min={minimo:.4f}, max={maximo:.4f}")
    frac_longe = sum(1 for f in fracoes_individuais if abs(f - 2 / 3) > 0.05) / len(fracoes_individuais)
    print(f"  fracao de trajetorias com |fracao_par - 2/3| > 0,05: {frac_longe:.2%}")
    print()
    print("INTERPRETACAO: a MEDIA sobre muitas trajetorias diferentes se aproxima "
          "de 2/3 (fato de densidade/heuristico bem conhecido, e o que o paper "
          "verifica empiricamente em Fig 3/5). Mas a fracao REALIZADA por cada "
          "trajetoria INDIVIDUAL varia com desvio-padrao e alcance substanciais -- "
          f"{frac_longe:.1%} das trajetorias testadas desviam de 2/3 por mais de "
          "0,05. Isso demonstra concretamente que '2/3' e uma propriedade de "
          "ENSEMBLE (media sobre muitos n aleatorios), nao uma restricao "
          "determinista sobre CADA trajetoria individual -- exatamente a "
          "distincao que o Lemma 4.2 do paper apaga ao substituir e=2/3, o=1/3 "
          "(derivados sob a hipotese de 'n aleatorio' do Teorema 3.2) diretamente "
          "na Equacao 4.4, que e sobre UMA trajetoria hipotetica ESPECIFICA e FIXA "
          "(a gerada por n+1, suposta divergente). Nada na dinamica determinista "
          "obriga essa trajetoria especifica a ter frequencia assintotica de "
          "paridade igual a media heuristica do ensemble.")

    return 0  # esta parte e demonstrativa/interpretativa, nao um teste pass/fail


if __name__ == "__main__":
    falhas = 0
    falhas += parte1()
    falhas += parte2()
    falhas += parte3_serie_geometrica()
    falhas += parte3_variancia_individual()

    print()
    print("=" * 90)
    print("VEREDITO")
    print("=" * 90)
    print(f"""
Falhas em partes verificaveis computacionalmente (Partes 1, 2, 3a): {falhas}.
(A Parte 3b e demonstrativa -- quantifica a distincao ensemble/trajetoria
individual, o cerne do gap logico, e nao um teste pass/fail.)

CONCLUSAO: este NAO e uma prova valida da Conjectura de Collatz.

O GAP FATAL esta no Lemma 4.2 ("a sequencia gerada por n+1 nao diverge
para infinito"). Sua demonstracao depende do Teorema 3.2 (Secao 3), que
deriva lim P(C^k(n) par)=2/3 tratando a paridade de C^k(n) como um
processo aleatorio de probabilidade 1/2 a cada passo (Lema 3.1) -- mas
o Lema 3.1 e apenas uma afirmacao de DENSIDADE sobre o CONJUNTO de todos
os numeros pares (metade deles, ao dividir por 2, ainda e par), nao um
fato sobre a orbita DETERMINISTICA de um n especifico e fixo. A Equacao
4.4 do Lemma 4.2 entao substitui e=2/3, o=1/3 -- validos apenas como
MEDIA DE ENSEMBLE sob a hipotese de "n aleatorio" -- diretamente numa
alegacao sobre UMA trajetoria hipotetica especifica (a gerada por n+1,
suposta divergente), derivando uma "contradicao" que na verdade nao se
segue logicamente. A Parte 3b acima demonstra quantitativamente que
trajetorias REAIS e individuais variam substancialmente ao redor da
media de 2/3 -- longe de ser uma restricao rigida por trajetoria.

Esta e exatamente a falacia do "argumento do passeio aleatorio" (random
walk heuristic), bem documentada na literatura de Collatz desde Crandall
e Lagarias como uma fonte de INTUICAO sobre por que a conjectura e
provavelmente verdadeira, mas explicitamente INSUFICIENTE como prova --
e a propria referencia [6] citada pelo paper para essa tecnica e um post
de forum (StackExchange) sobre um argumento heuristico, nao uma prova
publicada.

GAP SECUNDARIO (Lemma 4.3, Eq 4.28): a fatoracao como diferenca de
quadrados pressupoe implicitamente que n+1 e par, sem nunca tratar o
caso n+1 impar. A Parte 2 confirma computacionalmente que a CONCLUSAO
NUMERICA (unica solucao nao-trivial em n=1) sobrevive mesmo incluindo o
caso impar -- mas a demonstracao como escrita tem essa lacuna.

O restante do aparato do paper (exclusao de ciclos curtos, Parte 1;
aritmetica da serie geometrica, Parte 3a) esta correto -- o problema e
estritamente estrutural/logico (a substituicao ensemble->trajetoria
especifica), nao um erro de calculo.
""")
    sys.exit(0 if falhas == 0 else 1)
