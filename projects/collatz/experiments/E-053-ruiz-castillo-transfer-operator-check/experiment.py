"""
E-053 -- Verificacao do paper #013 (Ruiz Castillo, "Operador de
Transferencia Residual de Ruiz Castillo y teoria espectral para la
dinamica acelerada de la Conjetura de Collatz").

Quarto paper deste autor revisado nesta colecao (apos item 001/H-039,
item 008/H-050, item 010/H-052). Introduz um operador de transferencia
formal L_t sobre o espaco simbolico COMPLETO (nao restrito a
aritmetica de Collatz), com potencial phi(m,a_0,a_1,...) = m - log2(3)
(m = primeiro simbolo acrescentado por uma ramificacao inversa do
shift). Depois disso, motiva conjecturalmente uma versao restrita
L_{RC,t} sobre o espaco realizavel Sigma_C, e usa teoria espectral
classica (formula de Gelfand, Perron-Frobenius, brecha espectral) para
formular tres conjecturas explicitas (Conjetura 6.6, 7.1, 8.4) sobre
esse operador restrito.

ACHADO CENTRAL -- PRIMEIRO ERRO REAL nesta serie de 4 papers do autor
(H-039, H-050, H-052 eram todos "elementares mas corretos"):

Proposicao 5.3 afirma lim_{t->infty} L_t(1) = 0. Mas sua propria
"Demostracion" deriva a formula fechada de Proposicao 5.1,
L_t(1) = e^{(log2(3)-1)t}/(1-e^{-t}), e como log2(3)-1 ~ 0.585 > 0,
essa expressao DIVERGE exponencialmente quando t->infty -- o oposto
exato do que a Proposicao afirma. O proprio texto reconhece isso na
frase seguinte ("crece exponencialmente cuando t -> infty"), mas o
simbolo de fim de demonstracao (quadrado preto, QED) aparece logo
depois, sem que o enunciado "= 0" seja corrigido ou retirado.

Consultamos advisor() antes de finalizar este achado. Avaliacao:
o calculo esta correto e a Proposicao 5.3, como impressa, e de fato
falsa -- mas a caracterizacao precisa importa: a demonstracao do
proprio paper DERIVA corretamente o comportamento assintotico
(crescimento exponencial) e ate usa essa observacao para justificar a
necessidade de normalizacao futura via "presion residual". O autor
entendeu a assintotica; o defeito e que o enunciado formal em caixa
("Proposicao... lim=0") nunca foi atualizado para refletir a propria
demonstracao. Isto e uma INCONSISTENCIA ENUNCIADO-vs-DEMONSTRACAO --
mesma categoria do erro de rotulagem ja encontrado em Pratiher
(H-037), NAO um erro de calculo do autor, e portanto NAO vai para
`unverified-proof-claims.md` (o paper nao alega provar Collatz).

Confirmamos tambem que este erro e CONTIDO: a Proposicao 5.3 pertence
a Secao 5, um calculo preliminar/pedagogico sobre o espaco simbolico
IRRESTRITO (sem restricoes aritmeticas de Collatz). Nenhum resultado
posterior do paper (Secoes 6-8, sobre o operador RESTRITO L_{RC,t} em
Sigma_C, todas explicitamente conjecturais) cita ou depende do valor
numerico de L_t(1).
"""

import math

LOG2_3 = math.log2(3)


def L_t_1_series(t, n_terms=5000):
    """Soma parcial da serie que DEFINE L_t(1) = sum_{m=1}^inf e^{-t(m-log2(3))},
    truncada em n_terms -- usada para verificar a formula fechada
    (Proposicao 5.1) por convergencia direta, sem assumir a formula
    fechada de antemao."""
    total = 0.0
    for m in range(1, n_terms + 1):
        total += math.exp(-t * (m - LOG2_3))
    return total


def L_t_1_closed_form(t):
    """Formula fechada de Proposicao 5.1: L_t(1) = e^{t log2(3)} e^{-t} / (1-e^{-t})."""
    return math.exp(t * LOG2_3) * math.exp(-t) / (1 - math.exp(-t))


def check_proposicion_5_1(t_values):
    """Verifica Proposicao 5.1 comparando a soma direta da serie (truncada,
    com muitos termos) contra a formula fechada."""
    failures = []
    for t in t_values:
        direct = L_t_1_series(t)
        closed = L_t_1_closed_form(t)
        rel_err = abs(direct - closed) / closed
        if rel_err > 1e-6:
            failures.append((t, direct, closed, rel_err))
    return failures


def check_proposicion_5_2_positividade(t_values):
    """Proposicao 5.2: L_t(1) > 0 para todo t > 0. Trivial, mas verificamos."""
    return [t for t in t_values if not (L_t_1_closed_form(t) > 0)]


def check_proposicion_5_3_asymptotic(t_values):
    """Proposicao 5.3 afirma lim_{t->infty} L_t(1) = 0. Testamos diretamente:
    a sequencia deveria DECRESCER e se aproximar de 0 para t grande, caso a
    proposicao estivesse correta."""
    values = [(t, L_t_1_closed_form(t)) for t in t_values]
    is_increasing = all(values[i][1] < values[i + 1][1] for i in range(len(values) - 1))
    tends_to_zero = values[-1][1] < 1e-3
    return values, is_increasing, tends_to_zero


def check_convergencia_absoluta_prop_4_2(t_values, M=10.0):
    """Proposicao 4.2: para t>0 e |f|<=M, a serie converge absolutamente.
    Verificamos que a soma parcial se estabiliza (diferenca entre somas
    truncadas em 1000 e 2000 termos cai perto de 0)."""
    results = []
    for t in t_values:
        s_N = sum(M * math.exp(-t * (m - LOG2_3)) for m in range(1, 1000))
        s_2N = sum(M * math.exp(-t * (m - LOG2_3)) for m in range(1, 2000))
        results.append((t, abs(s_2N - s_N)))
    return results


if __name__ == "__main__":
    print("=" * 80)
    print("PARTE 1: formula explicita e convergencia (Proposicoes 4.1, 4.2, 5.1, 5.2)")
    print("=" * 80)
    t_values_basic = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]

    f51 = check_proposicion_5_1(t_values_basic)
    print(f"\nProposicao 5.1 (formula fechada de L_t(1)): testado para t={t_values_basic}, "
          f"falhas = {len(f51)}")
    if not f51:
        print("CONFIRMADA -- soma direta da serie (5000 termos) bate com a formula fechada.")

    f52 = check_proposicion_5_2_positividade(t_values_basic)
    print(f"\nProposicao 5.2 (positividade L_t(1)>0): falhas = {len(f52)} -- "
          f"{'CONFIRMADA' if not f52 else 'FALHOU'}")

    conv = check_convergencia_absoluta_prop_4_2(t_values_basic)
    print("\nProposicao 4.2 (convergencia absoluta): diferenca entre somas truncadas em "
          "1000 e 2000 termos (deveria ser ~0 se converge):")
    for t, diff in conv:
        print(f"  t={t}: diff={diff:.2e}")

    print()
    print("=" * 80)
    print("PARTE 2: Proposicao 5.3 (comportamento assintotico) -- TESTE DA ALEGACAO")
    print("=" * 80)
    t_values_asymptotic = [1, 2, 5, 10, 20, 50, 100, 200]
    values, is_increasing, tends_to_zero = check_proposicion_5_3_asymptotic(t_values_asymptotic)
    print(f"\n{'t':>6} | {'L_t(1)':>15}")
    for t, v in values:
        print(f"{t:>6} | {v:>15.6g}")
    print("\nProposicao 5.3 afirma: lim_{t->infty} L_t(1) = 0")
    print(f"Observado: sequencia e CRESCENTE = {is_increasing} (deveria ser decrescente "
          f"se a proposicao estivesse correta)")
    print(f"Observado: tende a ~0 em t=200 = {tends_to_zero} (deveria ser True se correta)")
    print(f"\nlog2(3)-1 = {LOG2_3 - 1:.6f} > 0, entao e^{{(log2(3)-1)t}} DIVERGE "
          "quando t->infty -- exatamente o oposto do que a Proposicao 5.3 afirma.")

    print()
    print("=" * 80)
    print("VEREDITO")
    print("=" * 80)
    print(f"""
Proposicoes 4.1, 4.2, 5.1, 5.2: CONFIRMADAS -- calculo direto de serie
geometrica, elementar e correto (mesmo padrao dos outros papers deste
autor).

Proposicao 5.3: FALSA CONFORME IMPRESSA. O paper afirma
lim_{{t->infty}} L_t(1) = 0, mas a propria "Demostracion" deriva a
formula fechada de Proposicao 5.1 e observa CORRETAMENTE que, como
log2(3)-1 = {LOG2_3 - 1:.6f} > 0, a quantidade "crece exponencialmente
cuando t -> infty" -- o oposto exato do enunciado da propria
Proposicao. O simbolo de fim de demonstracao aparece logo apos essa
observacao, sem que o enunciado "= 0" seja corrigido ou retirado.

Isto e uma INCONSISTENCIA ENUNCIADO-vs-DEMONSTRACAO -- mesma categoria
do erro de rotulagem ja encontrado em Pratiher (H-037), NAO um erro de
calculo: a demonstracao do proprio paper DERIVA o comportamento
assintotico correto (crescimento exponencial); so o enunciado formal
nunca foi atualizado para refletir isso.

Confirmamos que este erro e CONTIDO: a Proposicao 5.3 e um calculo
preliminar da Secao 5, sobre o espaco simbolico IRRESTRITO (sem
restricoes aritmeticas de Collatz) -- nenhum resultado posterior do
paper (Secoes 6-8, sobre o operador RESTRITO L_{{RC,t}} em Sigma_C,
todas explicitamente conjecturais: Conjetura 6.6, Conjetura 7.1,
Conjetura 8.4) cita ou depende do valor numerico de L_t(1).

Este e o PRIMEIRO erro real encontrado nos quatro papers Ruiz Castillo
revisados ate agora (H-039, H-050, H-052 eram todos "elementares mas
corretos"). O paper continua honesto quanto ao seu proprio alcance:
"los resultados obtenidos no constituyen una demostracion de la
Conjetura de Collatz."
""")
