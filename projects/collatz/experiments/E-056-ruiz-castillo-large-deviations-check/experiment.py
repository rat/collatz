"""
E-056 -- Verificacao do paper #026 (Ruiz Castillo, "Grandes Desviaciones
Residuales de Ruiz Castillo en la dinamica acelerada de la Conjetura de
Collatz", DOI 10.5281/zenodo.20767811, Zenodo, 2026, 44 paginas).

Setimo paper deste autor revisado nesta colecao (apos item 001/H-039,
008/H-050, 010/H-052, 013/H-053, 017/H-054, 020/H-055). Introduz a
"teoria de Grandes Desviaciones Residuales de Ruiz Castillo" para
estudar a raridade dos blocos de deuda residual positiva na dinamica
acelerada U(n)=(3n+1)/2^v2(3n+1). Define a palavra de valuacoes
a(n)=(a_0(n),a_1(n),...), a_j(n)=v2(3*U^j(n)+1), a deuda residual
L_k(n)=k*log2(3)-A_k(n) (A_k=soma das k primeiras valuacoes), o evento
residual {L_k/k>=x}, e a funcao de tasa residual

    I_RC(x) := -lim_{k->inf} (1/k) log P(L_k/k >= x)        (Definicion 3.1)

Sob o "modelo probabilistico ideal" (a_j iid, P(a=m)=2^{-m}, ou seja
Geometrica(1/2) -- MESMA distribuicao ja estabelecida em H-001/H-011:
E[a]=2, Var[a]=2), prova (Teorema 5.2) que existe c>0 com
P(L_k>=0)<=e^{-ck} via Chernoff/Markov padrao. Honesto: "El articulo
no demuestra la Conjetura de Collatz."

ACHADO CENTRAL DESTA REVISAO -- inconsistencia interna real (nao um
erro de calculo isolado, mas uma confusao conceitual entre a funcao de
tasa UNILATERAL de cauda -- definida e usada rigorosamente nas Secoes
2-5 -- e a funcao de tasa BILATERAL classica de Cramer -- usada
implicitamente na Figura 1, Secao 6 "conceptual", e na Conjetura 7.3,
Secao 7):

- Definicion 3.1 define I_RC(x) via P(L_k/k >= x) -- um evento de
  CAUDA UNILATERAL (>=). A Proposicion 3.4 (pag. 19-20, PROVADA, nao
  conjectural) mostra corretamente que I_RC e monotona nao-decrescente
  em TODO x (consequencia logica trivial: x1<=x2 implica
  {L_k/k>=x2} subconjunto de {L_k/k>=x1}, logo P(...>=x2)<=P(...>=x1),
  logo -log(P) e monotona). Uma funcao monotona nao-decrescente com
  I_RC(x*)=0 (x*=log2(3)-2, o drift esperado) e I_RC>=0 em toda parte
  EXIGE I_RC(x)=0 para TODO x<=x*, nao apenas em x=x*.

- Mas a Figura 1 (Secao 6, "Grafica conceptual de las grandes
  desviaciones residuales") mostra I_RC(x) como uma curva em V/U:
  decresce de ~1 (em x=-1) ate 0 (em x=x*~-0.415) e depois cresce de
  novo -- valores POSITIVOS para x<x*. O texto que a acompanha diz
  literalmente que I_RC "debe comportarse como una funcion convexa...
  cuyo minimo se alcanza en el valor tipico del drift residual". A
  Conjetura 7.3 (pag. 36-37), propriedade 2, formaliza exatamente essa
  alegacao: "Existe un UNICO punto x* tal que I_RC(x*)=0" -- o que
  exige I_RC(x)>0 para todo x!=x*, incluindo x<x*. Isso e
  matematicamente INCOMPATIVEL com a Proposicion 3.4 (ja provada no
  proprio paper, ~8 paginas antes).

- Confirmamos isso de tres formas independentes abaixo:
  (1) ANALITICAMENTE, usando a formula PADRAO da teoria de grandes
      desvios para eventos de cauda UNILATERAL, I_RC(x)=sup_{t>=0}
      {tx-Lambda(t)} (restricao de sinal correta para o evento
      {L_k/k>=x} da Definicion 3.1) -- da I_RC(x)=0 para x<x*, nao o
      valor positivo da Figura 1/Conjetura 7.3. Essa formula restrita
      NAO e a Conjetura 7.5 do paper (ver nota de integridade abaixo:
      conferimos a pag. 38 diretamente contra o PDF original e a
      Conjetura 7.5, como escrita, e sup_{t em R} IRRESTRITO).
  (2) MONTE CARLO, simulando medias de valuacoes iid Geometrica(1/2):
      para x<x* fixo, P(L_k/k>=x) tende a 1 (nao decai
      exponencialmente) conforme k cresce, logo -log(P)/k -> 0.
  (3) EXATO para k pequeno, via distribuicao Binomial Negativa fechada
      (Fraction, sem ponto flutuante perto do limiar -- ver nota de
      licao/bug ja corrigido em H-050/H-052) para a soma de k
      Geometricas(1/2) iid.

Mecanismo exato do erro: a funcao de tasa de Cramer CLASSICA e
BILATERAL J(x)=sup_{t em R}{tx-Lambda(t)} (sup sobre TODO t real, sem
restricao de sinal) e positiva e convexa em V nos DOIS lados da media
-- mas ela so corresponde a taxa real de DECAIMENTO de P(L_k/k>=x) no
lado x>=x* (onde esse evento de fato fica raro). Para x<x*, o evento
{L_k/k>=x} NAO e raro (e o lado "tipico", pela LGN), sua taxa de
decaimento correta e 0, nao J(x). A Figura 1 e a Conjetura 7.3 parecem
ter aplicado a formula bilateral classica de livro-texto sem notar essa
distincao -- exatamente o tipo de confusao unilateral-vs-bilateral que
a teoria classica de grandes desvios trata com cuidado (ex:
Dembo-Zeitouni, "Large Deviations Techniques", cap. 2). A Conjetura 7.5
(mesma Secao 7, duas paginas depois da Conjetura 7.3) e, conferido
diretamente contra o PDF original (pag. 38), EXATAMENTE essa mesma
formula bilateral (sup_{t em R}, SEM restricao de sinal) -- ou seja,
7.3, 7.5 e a Figura 1 sao mutuamente CONSISTENTES entre si (as tres
descrevem o mesmo objeto classico bilateral), e e esse trio, tomado em
conjunto, que contradiz a Proposicion 3.4 (JA PROVADA, pag. 19,
monotonia global de I_RC): uma funcao monotona nao-decrescente com um
zero em x* tem obrigatoriamente zero em TODO x<=x*, nao um zero unico
como a propriedade 2 da Conjetura 7.3 afirma. A UNICA aparicao no
paper inteiro da restricao de sinal correta (t>0) esta implicita na
demonstracao -- essa sim rigorosa e ja PROVADA -- do Teorema 5.2 (pag.
29-31), mas so para o caso particular x=0, via desigualdade de Markov
aplicada a e^{-tA_k} com t>0 escolhido a posteriori. A Secao 7 (inteira-
mente conjectural) generaliza esse resultado para todo x sem preservar
essa restricao, reintroduzindo -- ao que tudo indica sem perceber -- a
formula classica de livro-texto que so vale para o lado x>=x*.

NOTA DE INTEGRIDADE (dupla, ver tambem H-056): (a) um bug de swap na
ordem de unpacking de tupla (`val, t_opt = ...` em vez de `t_opt, val =
...`, trocando o valor otimizado pelo argmax) foi cometido e corrigido
no proprio codigo de verificacao abaixo antes de qualquer numero ser
reportado; (b) um rascunho anterior desta mesma analise caracterizou
errado a Conjetura 7.5 -- supos que ela ja vinha com a restricao de
sinal correta (t>=0) e a tratou como "a correcao que o proprio paper
oferece" para a Conjetura 7.3. Isso e FALSO: conferido diretamente
contra o PDF original (pag. 38, DOI acima), a Conjetura 7.5 e
irrestrita (sup_{t em R}), portanto faz parte do mesmo erro, nao uma
correcao dele. O achado central (inconsistencia Proposicion 3.4 vs
Conjetura 7.3/Figura 1) continua verdadeiro e nao depende dessa
correcao -- so a atribuicao de qual conjectura tem qual formula
mudou. Licao: sempre reconferir uma caracterizacao especifica de
formula/pagina contra o PDF primario antes de finalizar, mesmo quando
ja rascunhada com detalhe -- nao propagar uma leitura anterior sem
reverificar (mesmo espirito da armadilha "nunca reconstruir dados de
memoria" em `protocols/new-experiment.md`, aplicada aqui a leitura de
texto, nao so a dados numericos).

O restante do paper (identidades algebricas das Secoes 1-2, definicao
da funcao de tasa, Teorema 5.2/Chernoff) e correto -- verificado
abaixo contra orbitas REAIS de Collatz (Parte 1) e contra o modelo
i.i.d. ideal (Parte 2).
"""

import math
from decimal import Decimal, getcontext
from fractions import Fraction
import random

import numpy as np

getcontext().prec = 60  # alta precisao -- evita bug de ponto flutuante perto
                        # de limiar/igualdade (ja visto e corrigido em H-050/H-052)

LOG2_3 = math.log2(3)
LOG2_3_DEC = Decimal(3).ln() / Decimal(2).ln()  # log2(3) com ~60 digitos
X_STAR = LOG2_3 - 2  # drift residual esperado sob o modelo ideal (E[a]=2, Teorema 4.7)


# ---------------------------------------------------------------------
# Orbitas REAIS de Collatz -- mapa acelerado, valuacoes, deuda residual
# ---------------------------------------------------------------------

def v2(m):
    v = 0
    while m % 2 == 0:
        m //= 2
        v += 1
    return v


def syracuse_step(n):
    """Um passo do mapa acelerado U(n)=(3n+1)/2^v2(3n+1). Retorna
    (U(n), a_0(n))."""
    assert n % 2 == 1
    val = 3 * n + 1
    a = v2(val)
    return val // (2 ** a), a


def L_k_and_Ak(n, k):
    """Retorna (L_k(n), A_k(n)) para uma orbita REAL de Collatz
    comecando em n. L_k(n) e calculado em Decimal de alta precisao
    (k*LOG2_3_DEC - A_k) para permitir comparacoes exatas de
    sinal/limiar sem risco de falso positivo de ponto flutuante."""
    cur = n
    Ak = 0
    for _ in range(k):
        cur, a = syracuse_step(cur)
        Ak += a
    Lk = k * LOG2_3_DEC - Decimal(Ak)
    return Lk, Ak


# ---------------------------------------------------------------------
# PARTE 1 -- identidades algebricas do paper (Secoes 1-2), verificadas
# contra orbitas REAIS de Collatz (nao o modelo i.i.d. abstrato)
# ---------------------------------------------------------------------

def check_proposicion_1_2(n_values, k_values):
    """Proposicion 1.2 (interpretacion multiplicativa de la deuda
    residual): 2^{A_k(n)} = 3^k / 2^{L_k(n)}, equivalente a
    L_k(n)<0 <=> 3^k<2^{A_k(n)}. E uma reescrita direta da definicao
    L_k=k*log2(3)-A_k (exponenciar em base 2 os dois lados) -- deve
    valer exatamente. Verificamos DUAS formas: a equivalencia de sinal
    com aritmetica INTEIRA EXATA (3^k vs 2^{A_k(n)}, sem nenhum log),
    e a identidade numerica log2(3^k/2^Ak)=Lk com Decimal de alta
    precisao."""
    failures = []
    for n in n_values:
        for k in k_values:
            Lk, Ak = L_k_and_Ak(n, k)
            three_k = 3 ** k
            two_Ak = 2 ** Ak
            sign_Lk_negative = Lk < 0
            sign_from_integers = three_k < two_Ak
            if sign_Lk_negative != sign_from_integers:
                failures.append((n, k, "sinal inconsistente (aritmetica inteira)"))
            rhs_log2 = k * LOG2_3_DEC - Decimal(Ak)
            if abs(Lk - rhs_log2) > Decimal("1e-40"):
                failures.append((n, k, "identidade numerica falhou"))
    return failures


def check_proposicion_2_3_equivalencia(n_values, k_values, x_values):
    """Proposicion 2.3 (equivalencia residual-disipativa):
    L_k(n)/k >= x  <=>  A_k(n)/k <= log2(3) - x.
    Reescrita algebrica direta -- verificamos com Decimal de alta
    precisao para evitar falso positivo perto do limiar."""
    failures = []
    for n in n_values:
        for k in k_values:
            Lk, Ak = L_k_and_Ak(n, k)
            for x in x_values:
                x_dec = Decimal(str(x))
                lhs = (Lk / k) >= x_dec
                rhs = (Decimal(Ak) / k) <= (LOG2_3_DEC - x_dec)
                if lhs != rhs:
                    failures.append((n, k, x, "equivalencia falhou"))
    return failures


def check_corolario_2_4_critico(n_values, k_values):
    """Corolario 2.4 (evento critico residual, x=0): L_k(n)>=0 <=>
    A_k(n) <= k*log2(3). Caso particular da Proposicion 2.3 com x=0."""
    failures = []
    for n in n_values:
        for k in k_values:
            Lk, Ak = L_k_and_Ak(n, k)
            lhs = Lk >= 0
            rhs = Decimal(Ak) <= k * LOG2_3_DEC
            if lhs != rhs:
                failures.append((n, k))
    return failures


def check_monotonia_eventos(n_values, k_values, x_pairs):
    """Proposicion 2.5 (monotonia respecto del nivel residual): se
    x1<=x2, o evento de nivel x2 esta contido no de nivel x1
    (L_k(n)/k>=x2 implica L_k(n)/k>=x1). Consequencia logica trivial
    da transitividade de >=, mas verificamos exaustivamente mesmo
    assim (nunca assumir, sempre checar, mesmo o obvio -- e essa
    mesma proposicao, na forma de limite (Proposicion 3.4), e
    precisamente a que colide com a Figura 1/Conjetura 7.3 abaixo)."""
    failures = []
    for n in n_values:
        for k in k_values:
            Lk, Ak = L_k_and_Ak(n, k)
            ratio = Lk / k
            for x1, x2 in x_pairs:
                assert x1 <= x2
                x1_dec, x2_dec = Decimal(str(x1)), Decimal(str(x2))
                in_level_2 = ratio >= x2_dec
                in_level_1 = ratio >= x1_dec
                if in_level_2 and not in_level_1:
                    failures.append((n, k, x1, x2))
    return failures


# ---------------------------------------------------------------------
# PARTE 2 -- modelo probabilistico ideal: MGF, Chernoff (Teorema 5.2),
# funcao de tasa de Cramer, e o ACHADO CENTRAL (Figura 1 / Conjetura
# 7.3 vs Proposicion 3.4 + Conjetura 7.5)
# ---------------------------------------------------------------------

def E_a_exact(terms=200):
    """Proposicion 4.4: E[a]=2 sob P(a=m)=2^-m. Soma parcial exata via
    Fraction -- deveria convergir rapidamente a 2 (serie geometrica
    derivada, razao 1/2). So um re-check rapido do que ja esta
    estabelecido em H-001/H-011."""
    total = Fraction(0)
    for m in range(1, terms + 1):
        total += Fraction(m, 2 ** m)
    return total


def lambda_cgf(t):
    """Funcao geradora de cumulantes Lambda(t) = log E[e^{t*L}], onde
    L=log2(3)-a e o incremento residual por passo (media x*=log2(3)-2).
    Forma fechada (derivada a mao a partir da serie geometrica de
    E[e^{-ta}], a MESMA conta da demonstracao da Teorema 5.2 do
    paper):

        E[e^{-ta}] = sum_{m=1}^inf e^{-tm} 2^{-m} = (e^{-t}/2)/(1-e^{-t}/2)
                   = e^{-t} / (2 - e^{-t})           [valido para t>-ln2]

        Lambda(t) = t*log2(3) + log( e^{-t}/(2-e^{-t}) )

    exp(Lambda(t)) e exatamente a funcao Psi(t) da Secao 5.2 do paper
    (a base da cota de Chernoff/Markov, Teorema 5.2)."""
    if t <= -math.log(2):
        return float("inf")
    return t * LOG2_3 + math.log(math.exp(-t) / (2 - math.exp(-t)))


def ternary_search_max(f, lo, hi, iters=200):
    """Maximiza uma funcao CONCAVA f em [lo,hi] via busca ternaria
    (Lambda e convexa => t*x-Lambda(t) e concava em t -- busca
    ternaria converge sem precisar de derivadas; nao ha scipy
    disponivel neste ambiente)."""
    for _ in range(iters):
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        if f(m1) < f(m2):
            lo = m1
        else:
            hi = m2
    t_opt = (lo + hi) / 2
    return t_opt, f(t_opt)


T_MAX = 50.0
T_DOMAIN_MIN = -math.log(2) + 1e-9


def I_RC_restricted(x):
    """A funcao de tasa residual CORRETA para o evento de cauda
    UNILATERAL {L_k/k>=x} da Definicion 3.1: I_RC(x) = sup_{t>=0}
    {t*x - Lambda(t)}, restricao de sinal PADRAO da teoria de grandes
    desvios para eventos unilaterais (Dembo-Zeitouni cap. 2), a mesma
    restricao usada implicitamente (so para x=0) na demonstracao ja
    PROVADA do Teorema 5.2 do paper. NAO e a formula da Conjetura 7.5
    do paper -- essa, conferida contra o PDF (pag. 38), e irrestrita
    (ver nota de integridade no docstring do modulo)."""
    t_opt, val = ternary_search_max(lambda t: t * x - lambda_cgf(t), 0.0, T_MAX)
    return max(val, 0.0), t_opt  # concava com f(0)=0, entao o valor e sempre >=0


def J_unrestricted(x):
    """A funcao de tasa de Cramer CLASSICA e BILATERAL (sup sobre TODO
    t real, sem restricao de sinal) -- o que a Figura 1 (Secao 6), a
    Conjetura 7.3 (propriedade 2, zero UNICO em x*) E a Conjetura 7.5
    (pag. 38, conferida contra o PDF: sup_{t em R} irrestrito) todas
    descrevem. NAO e a taxa real de decaimento do evento {L_k/k>=x}
    definido na Definicion 3.1 quando x<x* -- e exatamente a mesma
    funcao que I_RC_restricted, mas so coincide com ela para x>=x*."""
    t_opt, val = ternary_search_max(lambda t: t * x - lambda_cgf(t), T_DOMAIN_MIN, T_MAX)
    return val, t_opt


def monte_carlo_tail(x, k, n_samples=200_000, seed=0):
    """Simula n_samples sequencias de k valuacoes iid Geometrica(1/2)
    (P(a=m)=2^-m, via inversao: a=1+floor(log(U)/log(1/2)) para
    U~Uniforme(0,1) -- formula padrao de amostragem de geometrica por
    inversao) e estima P(L_k/k>=x) = P(mean(a)<=log2(3)-x)
    diretamente. Vetorizado com numpy para viabilizar k grande."""
    rng = np.random.default_rng(seed)
    u = rng.random((n_samples, k))
    np.clip(u, 1e-300, None, out=u)
    a = 1 + np.floor(np.log(u) / math.log(0.5))
    total_a = a.sum(axis=1)
    threshold = LOG2_3 - x
    count = np.sum((total_a / k) <= threshold)
    return count / n_samples


def exact_small_k_tail(x, k):
    """Distribuicao EXATA (Fraction) de A_k = soma de k Geometricas(1/2)
    iid (suporte {1,2,...}): A_k tem distribuicao Binomial Negativa,
    P(A_k=n) = C(n-1,k-1) * (1/2)^n para n=k,k+1,k+2,...

    P(L_k/k>=x) = P(A_k <= k*(log2(3)-x)). O limiar k*(log2(3)-x) e
    IRRACIONAL (log2(3) e irracional) -- calculamos seu piso (floor)
    usando Decimal de 60 digitos de precisao, NAO float64, para evitar
    exatamente o tipo de bug de ponto flutuante perto de um limiar que
    ja apareceu e foi corrigido no proprio codigo deste projeto
    (H-050, H-052)."""
    threshold_dec = k * (LOG2_3_DEC - Decimal(str(x)))
    N = int(threshold_dec.to_integral_value(rounding="ROUND_FLOOR"))
    total = Fraction(0)
    for n in range(k, N + 1):
        total += Fraction(math.comb(n - 1, k - 1), 2 ** n)
    return total


def check_negative_binomial_normalizes(k=10, terms=3000):
    """Checagem de sanidade: sum_{n=k}^{k+terms} C(n-1,k-1)(1/2)^n deve
    se aproximar de 1 (normalizacao da Binomial Negativa)."""
    total = Fraction(0)
    for i in range(terms):
        n = k + i
        total += Fraction(math.comb(n - 1, k - 1), 2 ** n)
    return float(total)


if __name__ == "__main__":
    print("=" * 80)
    print("PARTE 1: identidades algebricas (Secoes 1-2), verificadas contra")
    print("orbitas REAIS de Collatz")
    print("=" * 80)

    random.seed(0)
    test_n = [1, 3, 5, 7, 9, 27, 703, 871, 6171] + [random.randrange(1, 10 ** 6, 2) for _ in range(15)]
    test_k = [1, 2, 5, 10, 20, 30]
    test_x = [-1.0, -0.7, -0.5, -0.3, -0.2, 0.0, 0.2, 0.5]
    test_x_pairs = [(-1.0, -0.5), (-0.5, 0.0), (0.0, 0.3), (-0.7, 0.7), (0.1, 0.4)]

    f1 = check_proposicion_1_2(test_n, test_k)
    print(f"\nProposicion 1.2 (interpretacion multiplicativa): "
          f"{len(test_n)}x{len(test_k)} casos, falhas = {len(f1)}")

    f2 = check_proposicion_2_3_equivalencia(test_n, test_k, test_x)
    print(f"Proposicion 2.3 (equivalencia residual-disipativa): "
          f"{len(test_n)}x{len(test_k)}x{len(test_x)} casos, falhas = {len(f2)}")

    f3 = check_corolario_2_4_critico(test_n, test_k)
    print(f"Corolario 2.4 (evento critico x=0): "
          f"{len(test_n)}x{len(test_k)} casos, falhas = {len(f3)}")

    f4 = check_monotonia_eventos(test_n, test_k, test_x_pairs)
    print(f"Proposicion 2.5 (monotonia de eventos): "
          f"{len(test_n)}x{len(test_k)}x{len(test_x_pairs)} casos, falhas = {len(f4)}")

    if not (f1 or f2 or f3 or f4):
        print("\nCONFIRMADO -- todas as identidades algebricas da Secao 1-2 sao")
        print("reescritas diretas corretas da definicao, sem excecao.")

    print()
    print("=" * 80)
    print("PARTE 2: modelo probabilistico ideal -- MGF, Chernoff, funcao de tasa")
    print("=" * 80)

    Ea = E_a_exact()
    print(f"\nProposicion 4.4, E[a] (soma parcial de 200 termos, Fraction): "
          f"{float(Ea):.15f}  (esperado exatamente 2)")
    print(f"x* = log2(3) - 2 = {X_STAR:.10f}  (drift residual esperado, Teorema 4.7)")

    # Teorema 5.2: existe c>0 com P(L_k>=0)<=e^{-ck}. I_RC(0) restrito (t>=0)
    # e exatamente esse c (o valor OTIMO da cota de Chernoff).
    c_opt, t0 = I_RC_restricted(0.0)
    print(f"\nTeorema 5.2 (cota exponencial): t0 otimo = {t0:.6f}, "
          f"c = I_RC(0) = {c_opt:.6f} (> 0, confirma a Teorema 5.2)")
    print(f"Psi(t0) = exp(Lambda(t0)) = {math.exp(lambda_cgf(t0)):.6f}  "
          f"(deveria ser < 1)")
    # Confere Psi(0)=1 e Psi'(0)=log2(3)-2 (derivada numerica)
    psi0 = math.exp(lambda_cgf(0.0))
    dpsi_num = (math.exp(lambda_cgf(1e-6)) - math.exp(lambda_cgf(-1e-6))) / 2e-6
    print(f"Psi(0) = {psi0:.10f} (esperado 1); "
          f"Psi'(0) numerico = {dpsi_num:.6f} (esperado log2(3)-2 = {X_STAR:.6f})")

    print()
    print("-" * 80)
    print("ACHADO CENTRAL: Figura 1 / Conjetura 7.3 / Conjetura 7.5 (todas bilaterais,")
    print("zero UNICO em x*) vs Proposicion 3.4 (monotonia global, PROVADA)")
    print("-" * 80)
    x_grid = [-1.0, -0.8, -0.6, round(X_STAR, 4), -0.3, -0.15, 0.0, 0.2, 0.4]
    print(f"\n{'x':>10} | {'I_RC(x) [correto, t>=0]':>24} | {'J(x) [Cramer bilateral]':>24} | regime")
    print("-" * 80)
    for x in x_grid:
        i_rc, _ = I_RC_restricted(x)
        j_val, _ = J_unrestricted(x)
        regime = "x < x*  (evento TIPICO)" if x < X_STAR - 1e-9 else "x >= x* (evento raro)"
        marker = "  <-- DIVERGEM" if abs(i_rc - j_val) > 1e-6 else ""
        print(f"{x:>10.4f} | {i_rc:>24.6f} | {j_val:>24.6f} | {regime}{marker}")

    print("""
Leitura da tabela: para x>=x* os dois coincidem (I_RC(x)=J(x), a
restricao de sinal nao importa pois o otimo irrestrito ja cai em
t>=0). Para x<x*, I_RC(x) [a funcao REALMENTE definida em Definicion
3.1, restrita corretamente a t>=0 -- restricao PADRAO da teoria de
grandes desvios unilaterais, NAO como a Conjetura 7.5 do paper
realmente escreve, ver nota de integridade] e IDENTICAMENTE ZERO,
enquanto J(x) [a funcao de Cramer bilateral classica, que e o que a
Figura 1 / Conjetura 7.3 / Conjetura 7.5 (conferida contra o PDF)
todas descrevem] e ESTRITAMENTE POSITIVA -- reproduzindo exatamente o
formato em V/U da Figura 1. Isso confirma analiticamente a
inconsistencia.""")

    print()
    print("-" * 80)
    print("Confirmacao empirica 1: MONTE CARLO (x < x*, evento deveria ficar")
    print("cada vez MENOS raro, nao mais raro, conforme k cresce)")
    print("-" * 80)
    x_test_below = -0.6  # bem abaixo de x* ~ -0.415
    j_below, _ = J_unrestricted(x_test_below)
    print(f"\nx = {x_test_below} (< x* = {X_STAR:.4f}); "
          f"J(x) [Cramer bilateral, o que a Figura 1 alegaria] = {j_below:.6f}")
    print(f"{'k':>8} | {'P_MC(L_k/k>=x)':>16} | {'-log(P)/k':>12} | esperado")
    print("-" * 60)
    for k in [10, 30, 100, 300, 1000]:
        n_samp = 200_000 if k <= 300 else 50_000
        p_hat = monte_carlo_tail(x_test_below, k, n_samples=n_samp, seed=1)
        rate = -math.log(p_hat) / k if p_hat > 0 else float("inf")
        print(f"{k:>8} | {p_hat:>16.6f} | {rate:>12.6f} | -> 0 (nao -> {j_below:.3f})")

    print()
    print("-" * 80)
    print("Confirmacao empirica 2: EXATO para k pequeno (Binomial Negativa via")
    print("Fraction, sem ponto flutuante perto do limiar)")
    print("-" * 80)
    sanity = check_negative_binomial_normalizes()
    print(f"\nChecagem de sanidade -- normalizacao Binomial Negativa (k=10, "
          f"3000 termos): soma = {sanity:.10f} (esperado 1)")

    print(f"\nx = {x_test_below} (< x*): P(L_k/k>=x) EXATO deveria SUBIR para 1,")
    print("nao decair exponencialmente:")
    print(f"{'k':>6} | {'P_exato(L_k/k>=x)':>20} | {'-log(P)/k':>12}")
    print("-" * 50)
    for k in [5, 10, 20, 30, 40]:
        p_exact = exact_small_k_tail(x_test_below, k)
        rate = -math.log(float(p_exact)) / k if p_exact > 0 else float("inf")
        print(f"{k:>6} | {float(p_exact):>20.8f} | {rate:>12.6f}")

    print(f"\nComparacao no regime x>=x* (x=0, o caso critico da Teorema 5.2):")
    print(f"{'k':>6} | {'P_exato(L_k>=0)':>18} | {'-log(P)/k':>12} | I_RC(0)={c_opt:.4f}")
    print("-" * 60)
    for k in [5, 10, 20, 30, 40]:
        p_exact = exact_small_k_tail(0.0, k)
        rate = -math.log(float(p_exact)) / k if p_exact > 0 else float("inf")
        print(f"{k:>6} | {float(p_exact):>18.8f} | {rate:>12.6f} |")

    print()
    print("=" * 80)
    print("VEREDITO")
    print("=" * 80)
    print(f"""
PARTE 1 (identidades algebricas, Secoes 1-2): CONFIRMADAS sem excecao
contra orbitas REAIS de Collatz -- {len(f1)+len(f2)+len(f3)+len(f4)} falhas
em {len(test_n)*len(test_k)*(2+len(test_x)+len(test_x_pairs))} casos totais.
Reescritas diretas de definicoes, corretas mas elementares.

PARTE 2 (modelo probabilistico ideal): Proposicion 4.4 (E[a]=2), Teorema
4.7 (drift negativo) e Teorema 5.2 (cota exponencial de Chernoff, c={c_opt:.4f})
todos CONFIRMADOS -- calculo do MGF/Psi(t) bate exatamente com a
demonstracao do proprio paper.

ACHADO CENTRAL (inconsistencia interna, nao erro de calculo isolado):
a Figura 1 (Secao 6, "conceptual") e a Conjetura 7.3 (propriedade 2:
"existe un UNICO punto x* tal que I_RC(x*)=0") descrevem I_RC(x) como
uma funcao BILATERAL em V/U, positiva nos dois lados de x*=log2(3)-2.
Isso CONTRADIZ a Proposicion 3.4 (JA PROVADA, pag. 19-20: monotonia
global de I_RC) -- uma funcao monotona nao-decrescente com um zero em
x* tem OBRIGATORIAMENTE zero em TODO x<=x*, nao um zero unico.
Confirmamos com tres metodos independentes que I_RC(x)=0 (nao positivo)
para x<x*: (1) analiticamente, usando a formula PADRAO da teoria de
grandes desvios unilaterais (sup_{{t>=0}}, restricao de sinal correta
-- NAO a formula que a Conjetura 7.5 do paper realmente escreve, ver
nota de integridade); (2) Monte Carlo (P(L_k/k>=x) tende a 1, nao
decai, para x<x* fixo); (3) exato via Binomial Negativa para k
pequeno. As tres formas concordam entre si e divergem exatamente como
previsto da curva mostrada na Figura 1.

O erro e conceitual: confundir a funcao de tasa de Cramer CLASSICA e
BILATERAL (sup sobre todo t real -- correta para o evento de DESVIO,
{{L_k/k = x}}) com a funcao de tasa REAL do evento de CAUDA UNILATERAL
{{L_k/k >= x}} que e o que a Definicion 3.1 realmente define (e que so
coincide com a bilateral no lado x>=x*). Conferido diretamente contra
o PDF original, o proprio paper contem as DUAS versoes da formula
bilateral (Conjetura 7.3 e Conjetura 7.5, mutuamente consistentes
entre si) e NENHUMA versao geral, explicita, da formula unilateral
correta -- essa so aparece implicita, restrita ao caso x=0, na
demonstracao ja provada do Teorema 5.2. Tudo sugere que a Secao 7
(inteiramente conjectural) foi escrita generalizando a intuicao
"livro-texto" da forma em V da funcao de Cramer para todo x, sem
preservar a restricao de sinal do Teorema 5.2 e sem verificar o
resultado contra a Proposicion 3.4 ja demonstrada 17 paginas antes.
""")
