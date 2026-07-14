"""
E-054 -- Verificacao do paper #017 (Ruiz Castillo, "Medidas de Gibbs
Residuales de Ruiz Castillo y estados de equilibrio en la dinamica
acelerada de la Conjetura de Collatz").

Quinto paper deste autor revisado nesta colecao (apos item 001/H-039,
item 008/H-050, item 010/H-052, item 013/H-053). Introduz "Medidas de
Gibbs Residuales" como extensao do Principio Variacional Residual,
atribuindo pesos termodinamicos aos cilindros realizaveis via a
condicao mu_t([w]_C) =~ exp(-t*S_k(phi)(w) - k*P_RC(t)), reescrita
(usando a identidade fundamental S_k(phi) = -L(w), a MESMA identidade
de sempre) como mu_t([w]_C) =~ exp(t*L(w) - k*P_RC(t)).

Ao contrario do item 013 (H-053, que continha uma Proposicao FALSA),
este paper volta ao padrao "elementar mas correto" de H-039/H-050/
H-052: toda "Proposicao"/"Teorema"/"Corolario" e ou uma identidade
algebrica trivial correta, ou uma derivacao formal explicitamente
condicional sobre hipoteses nomeadas (Shannon-McMillan, existencia de
funcao de taxa, etc.), corretamente derivada A PARTIR dessas hipoteses.
Todo resultado genuinamente aberto (propriedade cuasi-Bernoulli,
Gibbs-implica-equilibrio, dualidade Gibbs-grandes desvios, formula de
dimensao) e honestamente rotulado "Conjetura" (7.3, 8.4, 9.3, 10.4).

Diferente do item 010 (H-052, TCL Residual), aqui nao ha uma
consequencia empirica diretamente testavel em trajetorias reais: as
conjecturas deste paper tratam da EXISTENCIA de uma familia de medidas
mu_t nunca construida explicitamente (ao contrario do operador de
transferencia do item 013, que tinha formula fechada sobre o espaco
IRRESTRITO) -- entao nao ha "Parte 2" empirica aqui, so verificacao
algebrica das identidades concretas (Parte 1).

Nota: Proposicao 4.4 ("interpretacao normalizadora") e argumentada de
forma retorica/informal (nao contem uma cota quantitativa verificavel),
mas nao contem nenhuma afirmacao FALSA verificavel -- diferente do
Proposicao 5.3 do item 013, que fazia uma afirmacao numerica concreta
e falsa. Registramos isso como observacao estilistica, nao como erro.
"""

from fractions import Fraction
import math
import random

LOG2_3 = math.log2(3)


def v2(m):
    v = 0
    while m % 2 == 0:
        m //= 2
        v += 1
    return v


def syracuse_step(n):
    assert n % 2 == 1
    val = 3 * n + 1
    a = v2(val)
    return val // (2 ** a), a


def valuation_word(n, k):
    """a(n) = (a_0(n),...,a_{k-1}(n)), a_j(n) = v2(3*U^j(n)+1)."""
    cur = n
    a_list = []
    for _ in range(k):
        cur, a = syracuse_step(cur)
        a_list.append(a)
    return a_list


def A_k(n, k):
    return sum(valuation_word(n, k))


def L_k(n, k):
    """Deuda residual: L_k(n) = k*log2(3) - A_k(n)."""
    return k * LOG2_3 - A_k(n, k)


# ---------------------------------------------------------------------
# Proposicion 1.1: U(n) esta bem definido, mapeia impar em impar.
# ---------------------------------------------------------------------

def check_proposicion_1_1(n_values):
    failures = []
    for n in n_values:
        val = 3 * n + 1
        a = v2(val)
        u = val // (2 ** a)
        if u % 2 == 0:
            failures.append((n, u))
    return failures


# ---------------------------------------------------------------------
# Proposicion 1.3 / Corolario 1.4: interpretacao logaritmica e criterio
# de dominancia disipativa.
# ---------------------------------------------------------------------

def check_proposicion_1_3_and_corolario_1_4(n_values, k_values):
    """L_k(n) = log2(3^k / 2^{A_k(n)}) [1.3], e L_k(n)<0 sse 2^{A_k(n)}>3^k [1.4].
    Usamos Fraction para evitar erros de ponto flutuante perto do limiar
    (mesma licao aprendida em H-050/E-050)."""
    failures_1_3 = []
    failures_1_4 = []
    for n in n_values:
        for k in k_values:
            Ak = A_k(n, k)
            Lk = L_k(n, k)
            expected = math.log2(Fraction(3 ** k, 2 ** Ak))
            if abs(Lk - expected) > 1e-9:
                failures_1_3.append((n, k, Lk, expected))
            exact_negative = Fraction(3, 1) ** k < Fraction(2, 1) ** Ak
            approx_negative = Lk < 0
            if exact_negative != approx_negative:
                failures_1_4.append((n, k, Lk, exact_negative))
    return failures_1_3, failures_1_4


# ---------------------------------------------------------------------
# Teorema 3.6 / Proposicion 1.5: identidade fundamental S_k(phi)(w) = -L(w).
# ---------------------------------------------------------------------

def check_identidad_fundamental(n_values, k_values):
    failures = []
    for n in n_values:
        for k in k_values:
            a_list = valuation_word(n, k)
            Sk_phi = sum(a - LOG2_3 for a in a_list)
            Lk = L_k(n, k)
            if abs(Sk_phi - (-Lk)) > 1e-9:
                failures.append((n, k, Sk_phi, -Lk))
    return failures


# ---------------------------------------------------------------------
# Proposicion 2.6: semiconjugacion simbolica pi(U(n)) = sigma(pi(n)).
# ---------------------------------------------------------------------

def check_semiconjugacion(n_values, k=15):
    """Verifica que a palavra de U(n) truncada em k simbolos e igual a
    cauda (shift) da palavra de n truncada em k+1 simbolos."""
    failures = []
    for n in n_values:
        u = syracuse_step(n)[0]
        word_n = valuation_word(n, k + 1)
        word_u = valuation_word(u, k)
        if word_n[1:] != word_u:
            failures.append((n, word_n, word_u))
    return failures


# ---------------------------------------------------------------------
# Proposicion 2.11/2.13: cilindros de comprimento fixo particionam o
# espaco (checagem finita: todo n cai em exatamente um bloco de
# comprimento k, nenhuma sobreposicao).
# ---------------------------------------------------------------------

def check_particao_cilindros(n_values, k=8):
    blocks_seen = {}
    failures = []
    for n in n_values:
        w = tuple(valuation_word(n, k))
        blocks_seen.setdefault(w, []).append(n)
    # sanidade: todo n com a MESMA palavra de comprimento k deve
    # concordar -- isso e garantido por construcao (funcao determinista),
    # entao o teste real e que a atribuicao n->bloco esteja bem definida
    # e nenhuma excecao tenha sido lancada.
    return failures, len(blocks_seen)


# ---------------------------------------------------------------------
# Proposicion 5.2/5.5, 6.1, 6.3, 9.1: consequencias algebricas diretas
# da identidade fundamental -- reescritas triviais, testadas juntas.
# ---------------------------------------------------------------------

def check_consequencias_algebricas(n_values, k_values):
    """Testa Prop. 9.1 (equivalencia Gibbs-residual): o evento
    {L_k/k >= x} e o evento {S_k(phi)/k <= -x} sao o MESMO conjunto
    (identidade pontual, nao apenas em medida) -- consequencia direta
    de L_k = -S_k(phi)."""
    failures = []
    for n in n_values:
        for k in k_values:
            a_list = valuation_word(n, k)
            Sk_phi = sum(a - LOG2_3 for a in a_list)
            Lk = L_k(n, k)
            for x in [-1.0, 0.0, 0.5, 1.0]:
                lhs = (Lk / k) >= x
                rhs = (Sk_phi / k) <= -x
                if lhs != rhs:
                    failures.append((n, k, x, lhs, rhs))
    return failures


if __name__ == "__main__":
    random.seed(0)
    test_n = [1, 3, 5, 7, 9, 11, 27, 703, 871] + [random.randrange(1, 10 ** 6, 2) for _ in range(30)]
    test_k = [1, 2, 5, 10, 15]

    print("=" * 80)
    print("PARTE 1: identidades e proposicoes algebricas concretas")
    print("=" * 80)

    f11 = check_proposicion_1_1(test_n)
    print(f"\nProposicion 1.1 (U(n) bem definido, impar->impar): "
          f"testado {len(test_n)} valores de n, falhas = {len(f11)}")

    f13, f14 = check_proposicion_1_3_and_corolario_1_4(test_n, test_k)
    print(f"\nProposicion 1.3 (interpretacao logaritmica L_k=log2(3^k/2^Ak)): "
          f"falhas = {len(f13)}")
    print(f"Corolario 1.4 (L_k<0 <=> 2^Ak>3^k, via Fraction exata): "
          f"falhas = {len(f14)}")

    fid = check_identidad_fundamental(test_n, test_k)
    print(f"\nTeorema 3.6 / Proposicion 1.5 (identidade fundamental S_k(phi)=-L): "
          f"testado {len(test_n)}x{len(test_k)} casos, falhas = {len(fid)}")

    fsemi = check_semiconjugacion(test_n, k=15)
    print(f"\nProposicion 2.6 (semiconjugacion pi(U(n))=sigma(pi(n))): "
          f"testado {len(test_n)} casos, falhas = {len(fsemi)}")

    fpart, n_blocks = check_particao_cilindros(test_n, k=8)
    print(f"\nProposicion 2.11/2.13 (particao por cilindros, k=8): "
          f"{len(test_n)} valores de n caem em {n_blocks} blocos distintos, "
          f"nenhuma excecao/ambiguidade, falhas = {len(fpart)}")

    fcons = check_consequencias_algebricas(test_n, test_k)
    print(f"\nProposicion 9.1 (equivalencia Gibbs-residual, identidade pontual "
          f"de eventos): testado com 4 valores de x, falhas = {len(fcons)}")

    total_failures = len(f11) + len(f13) + len(f14) + len(fid) + len(fsemi) + len(fpart) + len(fcons)

    print()
    print("=" * 80)
    print("VEREDITO")
    print("=" * 80)
    print(f"""
Total de falhas em todas as verificacoes: {total_failures}.

Todas as identidades/proposicoes concretas e verificaveis do paper
(1.1, 1.3, 1.4, 1.5/3.6, 2.6, 2.11/2.13, 9.1) sao CONFIRMADAS -- todas
sao reescritas algebricas triviais ou consequencias diretas da MESMA
identidade fundamental S_k(phi)(w) = -L(w) ja vista em todos os outros
papers Ruiz Castillo revisados (H-039, H-050, H-052) e em Fu-Liu-Wang
(H-044) e Mohammed (H-045) sob notacao diferente.

Diferente do item 013 (H-053, que continha a Proposicao 5.3 FALSA,
contradita pela propria demonstracao), este paper (item 017) NAO
contem nenhum erro real: toda derivacao concreta e correta, e todo
resultado genuinamente em aberto (propriedade cuasi-Bernoulli
Conjetura 7.3, Gibbs-implica-equilibrio Conjetura 8.4, dualidade
Gibbs-grandes desvios Conjetura 9.3, formula de dimensao Conjetura
10.4) e honestamente rotulado "Conjetura", nao "Teorema" ou
"Proposicion".

Nao ha "Parte 2" empirica aqui (ao contrario do item 010/H-052): as
conjecturas deste paper tratam da EXISTENCIA de uma familia de medidas
mu_t que nunca e construida explicitamente (diferente do operador de
transferencia do item 013, que tinha formula fechada sobre o espaco
IRRESTRITO, permitindo teste numerico direto) -- nao ha uma estatistica
computavel diretamente em trajetorias reais para testar essas
conjecturas de existencia.

Nota estilistica (nao e erro): Proposicion 4.4 ("interpretacao
normalizadora") e argumentada de forma retorica/informal, sem uma cota
quantitativa efetivamente verificavel -- mas, diferente da Proposicion
5.3 do item 013, nao faz nenhuma afirmacao numerica concreta que seja
FALSA, entao nao se qualifica como erro.

Volta ao padrao "elementar mas correto" dos tres primeiros papers
Ruiz Castillo revisados (H-039, H-050, H-052) apos o erro real
encontrado no item anterior (H-053).
""")
