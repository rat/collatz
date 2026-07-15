#!/usr/bin/env python3
"""
E-057 -- H-057: "Angulo de estrategia adversarial de maxima subida" via
fracoes continuas de log2(3), candidato #1 da lista "ainda nao
implementados" do BACKLOG.md (secao 6).

IDEIA CENTRAL: um ciclo nao-trivial hipotetico de comprimento a (numero
de termos impares) e disipacao total S (soma das valuacoes 2-adicas)
so pode ter n0 positivo se 2^S > 3^a, ou seja, S > a*log2(3). Definindo
a "deuda residual" da PAR (a,S) -- exatamente a mesma quantidade
L_k(n) = k*log2(3) - A_k(n) usada em TODOS os ~7 papers de Ruiz
Castillo revisados nesta colecao, so que aqui aplicada a um par
ABSTRATO (a,S), nao a trajetoria REAL de um n especifico --

    L(a,S) = S - a*log2(3)   [convencao de sinal: queremos L(a,S) > 0
                               pequeno, i.e. S so um pouco acima de
                               a*log2(3)]

quanto MENOR o excesso L(a,S) para um dado a, mais dificil e EXCLUIR
esse candidato por via analitica (cotas de Baker sobre formas lineares
em logaritmos precisam de constantes efetivas maiores quanto mais perto
2^S esta de 3^a) -- e por isso que o bound da literatura para (para de
avancar em a=91: os proximos candidatos tem excesso pequeno demais para
as cotas atuais). ATENCAO -- CORRIGIDO apos revisao (advisor(), 2026-07-
14): a relacao entre L(a,S) e o n0 de um eventual ciclo NAO e "menor L
=> menor n0". E o oposto para a composicao que MINIMIZA n0 dado (a,S):
n0_min = (3^a-2^a)/(2^S-3^a) ~= 1/(L*ln2), ou seja, menor excesso => n0
minimo MAIOR (nao menor). Mas isso e so o minimo sobre composicoes; o n0
de um ciclo real (se existisse) usa UMA composicao especifica e
desconhecida, que pode estar bem longe do minimo (verificado
empiricamente: para a=306 uma composicao "ruim" da n0~10^25, contra
n0_min~10^3 pela composicao otima) -- ver PARTE 2b. Por isso L(a,S)
pequeno NAO e um proxy direto para "n0 grande" nem "n0 pequeno": e um
proxy para dificuldade analitica de exclusao, que e uma coisa diferente.
A teoria classica de fracoes continuas diz EXATAMENTE quais valores de a
dao o menor excesso possivel para aquele tamanho de a: os denominadores
dos convergentes da fracao continua de log2(3). Essa e a tecnica real
usada por Steiner (1977), Simons (2005), Simons & de Weger (2005) e
Hercher (2023) para excluir ciclos -- NAO e uma tecnica nova, mas
conectar explicitamente com nosso proprio "muro combinatorio" (H-009/
H-034, C(S-1,a-1) explode) e com o bound mais atual da literatura
(verificado via WebSearch/WebFetch antes de escrever este codigo, para
nao repetir de memoria um numero que poderiamos errar) e uma sintese
nova para ESTE projeto.

Achado da verificacao da literatura (2026-07-14, via WebSearch +
WebFetch em fontes primarias/Wikipedia, nao de memoria): nossas proprias
notas (STATE.md/BACKLOG.md) citam "Simons & de Weger (2005), sem ciclo
ate 68 subidas" -- CORRETO como citacao historica (confirmado via
Wikipedia), mas DESATUALIZADO como bound atual: Hercher (2023,
arXiv:2201.00406) estendeu a exclusao para a<=91 (ou seja, qualquer
ciclo nao-trivial precisaria de a>=92). Technique confirmada em ambas
as fontes: fracoes continuas de log2(3) (ln(3)/ln(2)), conectadas a
cotas de Baker sobre formas lineares em logaritmos.

Este experimento:
  PARTE 1: computa a fracao continua de log2(3) e seus convergentes,
    calcula o excesso L(a,S) para cada um, e classifica cada a contra
    tres marcos: nosso muro de forca bruta (H-034: a<=16 limpo, ate
    a<=25 com janela reduzida), e o bound da literatura (a<=91,
    Hercher 2023).
  PARTE 2: para os convergentes DENTRO do nosso alcance computacional
    (a<=25), roda a checagem REAL de autoconsistencia (reaproveitando
    EXATAMENTE as funcoes ja validadas de E-034: compositions,
    candidate_n0, check_self_consistency) no S EXATO do convergente.
    NOTA: isso e um SUBCONJUNTO da janela S_min..S_min+10/20 que H-034
    ja cobria (o S do convergente cai dentro dessa janela), nao uma
    verificacao mais precisa -- reporta explicitamente quantas
    composicoes tem ALGUM n0 inteiro (nao so autoconsistentes), que e um
    resultado mais forte quando da zero.
  PARTE 2b: para os mesmos (a,S) de PARTE 2, calcula o n0_min de forma
    fechada (composicao (1,1,...,1,S-a+1), que a enumeracao exaustiva
    confirma ser a que minimiza n0) e mostra que mesmo a composicao MAIS
    favoravel a um ciclo pequeno da valores triviais -- mas isso NAO
    limita o n0 de uma composicao arbitraria/desconhecida (ver correcao
    no topo deste docstring).
  PARTE 3: quantifica o custo combinatorio C(S-1,a-1) dos convergentes
    ALEM do nosso alcance, ate e um pouco alem do bound da literatura
    (a=92+), mostrando numericamente por que forca bruta pura nunca
    chegaria la sem as tecnicas de Baker/reducao de reticulado.
  PARTE 4: identifica, entre nosso muro (a~25) e o bound da literatura
    (a=91), quais valores de a tem MENOR excesso L(a,S) -- candidatos
    onde a exclusao analitica (Baker) e mais dificil, no sentido de
    precisar de constantes efetivas maiores. Isso NAO e uma previsao de
    que esses a tenham ciclos com n0 maior ou menor (ver correcao acima)
    -- e so uma leitura de qual e o proximo alvo natural para quem for
    ESTENDER o bound analitico da literatura.
"""

import math
import sys
from itertools import combinations

import mpmath as mp

mp.mp.dps = 300  # precisao alta o suficiente para dezenas de termos de fracao continua
sys.set_int_max_str_digits(0)  # alguns convergentes tem centenas/milhares de digitos


def fmt_big(n):
    """Formata um inteiro grande de forma legivel: numero completo se
    couber em 25 digitos, senao notacao compacta (N digitos, ~valor)."""
    s = str(n)
    if len(s) <= 25:
        return f"{n:,}"
    return f"~10^{len(s) - 1} ({len(s)} digitos)"


# ---------------------------------------------------------------------
# Fracao continua de log2(3), convergentes E semiconvergentes
# ---------------------------------------------------------------------
#
# NOTA IMPORTANTE (corrigido apos primeira tentativa mais simples): o
# problema aqui e um problema de aproximacao UNILATERAL (precisamos de
# S > a*log2(3) estritamente, nao so |S/a - log2(3)| pequeno). Usar
# somente os convergentes "de cima" (a cada 2 indices) da uma lista
# MUITO esparsa (a=1,5,41,306,... saltos enormes) que SUBESTIMA quantos
# candidatos "perigosos" existem nas faixas intermediarias -- os
# SEMICONVERGENTES (fracoes intermediarias entre dois convergentes
# consecutivos do mesmo lado) preenchem essas lacunas e sao a mesma
# ferramenta que a literatura profissional (Simons & de Weger, Hercher)
# usa para tratar esse tipo de aproximacao de um lado so.

def continued_fraction_terms(x, n_terms):
    terms = []
    val = x
    for _ in range(n_terms):
        a = int(mp.floor(val))
        terms.append(a)
        frac = val - a
        if frac == 0:
            break
        val = 1 / frac
    return terms


def convergents(terms):
    """Retorna lista de (p_i, q_i), convergentes p_i/q_i de x."""
    p_prev2, p_prev1 = 0, 1
    q_prev2, q_prev1 = 1, 0
    result = []
    for a in terms:
        p = a * p_prev1 + p_prev2
        q = a * q_prev1 + q_prev2
        result.append((p, q))
        p_prev2, p_prev1 = p_prev1, p
        q_prev2, q_prev1 = q_prev1, q
    return result


def all_best_approximations_from_above(x, terms):
    """Gera TODAS as fracoes p/q (convergentes + semiconvergentes) que
    sao "melhor aproximacao de um lado so" com p/q > x, em ordem
    crescente de q. Estas sao exatamente os candidatos (a=q, S=p) que a
    tecnica classica de exclusao de ciclos (Steiner/Simons/de
    Weger/Hercher) precisa varrer -- muito mais completo que so os
    convergentes plenos.

    Algoritmo padrao: para cada par de convergentes consecutivos
    (p_{i-1},q_{i-1}) e (p_i,q_i), as fracoes intermediarias
    (p_{i-1}+j*p_i, q_{i-1}+j*q_i) para j=1..a_{i+1} ficam do MESMO
    lado de x que (p_{i-1},q_{i-1}), aproximando-se monotonicamente de
    (p_{i+1},q_{i+1}) conforme j cresce (j=a_{i+1} da exatamente o
    proximo convergente pleno)."""
    p_prev2, p_prev1 = 0, 1
    q_prev2, q_prev1 = 1, 0
    result = []
    # (p_prev2,q_prev2) e (p_prev1,q_prev1) comecam como os convergentes
    # "virtuais" de indice -2 e -1 (convencao padrao: p_{-1}=1,q_{-1}=0,
    # p_{-2}=0,q_{-2}=1)
    for idx, a_term in enumerate(terms):
        p_cur = a_term * p_prev1 + p_prev2
        q_cur = a_term * q_prev1 + q_prev2
        # semiconvergentes entre o convergente anterior-anterior
        # (p_prev2,q_prev2) e o atual (p_cur,q_cur), usando j=1..a_term
        # -- ficam do lado de (p_prev2,q_prev2)
        if q_prev2 > 0:  # pula o primeiro passo (sem par anterior valido)
            lado_prev2 = float(p_prev2) > float(q_prev2) * x if q_prev2 != 0 else None
            for j in range(1, a_term + 1):
                p = j * p_prev1 + p_prev2
                q = j * q_prev1 + q_prev2
                if q <= 0:
                    continue
                is_above = float(p) > float(q) * x
                if is_above:
                    result.append((p, q))
        p_prev2, p_prev1 = p_prev1, p_cur
        q_prev2, q_prev1 = q_prev1, q_cur
    return result


# ---------------------------------------------------------------------
# Logica da equacao de ciclo -- REAPROVEITADA de E-034 (ja validada em
# H-009/H-034, sem reimplementar do zero)
# ---------------------------------------------------------------------

def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for dividers in combinations(range(1, total), parts - 1):
        prev = 0
        comp = []
        for d in dividers:
            comp.append(d - prev)
            prev = d
        comp.append(total - prev)
        yield tuple(comp)


def candidate_n0(a, bs):
    S = sum(bs)
    denom = 2 ** S - 3 ** a
    if denom <= 0:
        return None, None
    num = 0
    s_i = 0
    for i in range(a):
        num += 3 ** (a - 1 - i) * 2 ** s_i
        s_i += bs[i]
    if num % denom != 0:
        return None, None
    return num // denom, denom


def check_self_consistency(n0, expected_bs):
    n = n0
    for b in expected_bs:
        m = 3 * n + 1
        a_real = 0
        while m % 2 == 0:
            m //= 2
            a_real += 1
        if a_real != b:
            return False
        n = m
    return n == n0


def check_cycle_at_exact_S(a, S, max_comps=20_000_000):
    """Roda a checagem completa de autoconsistencia para o par (a,S)
    EXATO (nao uma janela) -- usado nos convergentes, que ja dao o S
    otimo para aquele a. Reporta tambem quantas composicoes produzem
    ALGUM n0 inteiro positivo (mesmo sem autoconsistencia) -- quando
    isso da zero e um resultado mais forte que "nenhum ciclo
    autoconsistente" (a propria condicao de divisibilidade ja falha
    para toda composicao, antes mesmo de checar se fecha um ciclo)."""
    if S - 1 < a - 1 or a < 1:
        return "par invalido", 0, None, 0
    n_comps = math.comb(S - 1, a - 1)
    if n_comps > max_comps:
        return "pulado (excesso combinatorio)", n_comps, None, None
    denom = 2 ** S - 3 ** a
    if denom <= 0:
        return "denom<=0 (par nao aplicavel, S<a*log2(3))", n_comps, None, None
    found = []
    com_n0_inteiro = 0
    for bs in compositions(S, a):
        n0, _ = candidate_n0(a, bs)
        if n0 is not None and n0 > 0:
            com_n0_inteiro += 1
            if check_self_consistency(n0, bs):
                found.append((bs, n0))
    novel = [f for f in found if f[1] != 1]
    if novel:
        status = "CICLO NOVO ENCONTRADO!!"
    elif com_n0_inteiro == 0:
        status = "nenhuma composicao da n0 inteiro (condicao de divisibilidade ja falha para todas)"
    else:
        status = "nenhum ciclo novo (so trivial ou nada, apesar de existir n0 inteiro em alguma composicao)"
    return status, n_comps, novel, com_n0_inteiro


def n0_min_closed_form(a, S):
    """n0 para a composicao (1,1,...,1,S-a+1) -- confirmado por
    enumeracao exaustiva (a=3,5,17) como a composicao que MINIMIZA n0
    entre todas as composicoes de S em a partes. Forma fechada:
    num = 3^a - 2^a (independente de S, so depende de a), portanto
    n0_min = (3^a-2^a)/(2^S-3^a) ~= 1/(L*ln2) para L pequeno.

    IMPORTANTE: isso e o MINIMO sobre composicoes, nao um limite
    superior sobre o n0 de um ciclo real -- uma composicao diferente
    (ex. valuacoes grandes no INICIO em vez do fim) pode dar n0
    muitas ordens de grandeza maior para o MESMO (a,S). Ver docstring
    do modulo."""
    num = 3 ** a - 2 ** a
    denom = 2 ** S - 3 ** a
    if denom <= 0:
        return None
    return mp.mpf(num) / mp.mpf(denom)


# ---------------------------------------------------------------------
# Marcos conhecidos (nosso muro + literatura, verificados via
# WebSearch/WebFetch antes de escrever este codigo -- nao de memoria)
# ---------------------------------------------------------------------

NOSSO_WALL_LIMPO = 16       # H-034: busca completa e limpa ate aqui
NOSSO_WALL_REDUZIDO = 25    # H-034: parcial, janela reduzida, ainda tratavel
LITERATURA_ANTIGA = 68      # Simons & de Weger (2005), citacao historica em nossas notas
LITERATURA_ATUAL = 91       # Hercher (2023), arXiv:2201.00406 -- verificado nesta sessao


def classifica(a):
    if a <= NOSSO_WALL_LIMPO:
        return f"nosso wall LIMPO (a<={NOSSO_WALL_LIMPO}, H-034)"
    elif a <= NOSSO_WALL_REDUZIDO:
        return f"nosso wall REDUZIDO (a<={NOSSO_WALL_REDUZIDO}, H-034, janela parcial)"
    elif a <= LITERATURA_ANTIGA:
        return f"ja excluido (Simons & de Weger 2005, a<={LITERATURA_ANTIGA})"
    elif a <= LITERATURA_ATUAL:
        return f"ja excluido (Hercher 2023, a<={LITERATURA_ATUAL} -- bound ATUAL)"
    else:
        return "ALEM do bound conhecido da literatura (Hercher 2023)!"


if __name__ == "__main__":
    LOG2_3 = mp.log(3) / mp.log(2)
    print("=" * 90)
    print("PARTE 1: fracao continua de log2(3), convergentes E semiconvergentes")
    print("=" * 90)

    terms = continued_fraction_terms(LOG2_3, 45)
    print(f"\nTermos da fracao continua de log2(3) (primeiros {len(terms)}):")
    print(terms)

    convs = convergents(terms)
    so_convergentes = sorted(
        {(S, a) for (S, a) in convs if a >= 1 and float(S) > float(a * LOG2_3)},
        key=lambda t: t[1],
    )
    print(f"\nSo convergentes PLENOS com S>a*log2(3): {[a for _, a in so_convergentes]}")
    print("(lista esparsa -- saltos grandes sugerem que estamos perdendo candidatos")
    print(" intermediarios; ver semiconvergentes abaixo)")

    A_MAX_ANALISE = 2000  # muito alem do bound da literatura (91), mas evita
                           # tentar calcular C(S-1,a-1) para a com 20+ digitos
                           # (alguns termos da fracao continua de log2(3), ex.
                           # os termos 23/55/20/37, fazem 'a' explodir para
                           # ~10^21 ja no 45o termo -- nesse regime o custo
                           # combinatorio ja e absurdamente inatingivel de
                           # qualquer forma, entao truncar aqui nao perde
                           # nenhuma informacao pratica)
    todos_brutos = sorted(
        {(S, a) for (S, a) in all_best_approximations_from_above(LOG2_3, terms) if a >= 1},
        key=lambda t: t[1],
    )
    n_descartados = sum(1 for _, a in todos_brutos if a > A_MAX_ANALISE)
    todos = [(S, a) for (S, a) in todos_brutos if a <= A_MAX_ANALISE]
    print(f"\n{len(todos_brutos)} candidatos totais (convergentes + semiconvergentes) "
          f"gerados a partir de {len(terms)} termos da fracao continua;")
    print(f"{n_descartados} descartados por terem a>{A_MAX_ANALISE} (a maior gerada tem "
          f"{len(str(todos_brutos[-1][1]))} digitos -- calcular C(S-1,a-1) nesse regime")
    print("nao e nem factivel nem informativo, ja que o custo combinatorio ja e")
    print("absurdo bem antes disso).\n")
    print(f"{len(todos)} candidatos com a<={A_MAX_ANALISE}, ordenados por a -- esta e a lista")
    print("de 'melhores aproximacoes de um lado so', a mesma ferramenta usada por")
    print("Simons&de Weger/Hercher:\n")
    print(f"{'a':>6} | {'S':>8} | {'L(a,S)=S-a*log2(3)':>22} | {'C(S-1,a-1)':>28} | classificacao")
    print("-" * 130)
    for S, a in todos:
        L = float(S - a * LOG2_3)
        n_comps = math.comb(S - 1, a - 1) if S - 1 >= a - 1 >= 0 else 0
        print(f"{a:>6} | {S:>8} | {L:>22.6e} | {fmt_big(n_comps):>28} | {classifica(a)}")

    print()
    print("=" * 90)
    print("PARTE 2: checagem REAL de autoconsistencia nos candidatos viaveis (a<=25)")
    print("(reaproveitando exatamente candidate_n0/check_self_consistency de E-034)")
    print("=" * 90)
    for S, a in todos:
        if a > NOSSO_WALL_REDUZIDO:
            continue
        status, n_comps, novel, com_n0 = check_cycle_at_exact_S(a, S)
        print(f"\na={a}, S={S} (excesso L={float(S - a * LOG2_3):.4e}): {status}")
        print(f"  composicoes testadas: {fmt_big(n_comps)} | com n0 inteiro positivo: {com_n0}")

    print()
    print("=" * 90)
    print("PARTE 2b: n0_min (composicao que MINIMIZA n0, forma fechada) -- NAO e um limite")
    print("superior sobre um ciclo real, so mostra que ate a composicao mais favoravel a um")
    print("ciclo pequeno da valores triviais (ver docstring do modulo para a ressalva)")
    print("=" * 90)
    print(f"\n{'a':>6} | {'S':>8} | {'L(a,S)':>14} | {'n0_min=(3^a-2^a)/(2^S-3^a)':>28}")
    print("-" * 90)
    for S, a in todos:
        L = float(S - a * LOG2_3)
        n0m = n0_min_closed_form(a, S)
        n0m_str = mp.nstr(n0m, 8) if n0m is not None else "n/a"
        print(f"{a:>6} | {S:>8} | {L:>14.6e} | {n0m_str:>28}")

    print()
    print("=" * 90)
    print("PARTE 3: custo combinatorio ALEM do nosso alcance, ate e alem de a=91")
    print("=" * 90)
    print(f"\n{'a':>6} | {'S':>8} | {'C(S-1,a-1)':>28} | classificacao")
    print("-" * 90)
    for S, a in todos:
        if a <= NOSSO_WALL_REDUZIDO:
            continue
        n_comps = math.comb(S - 1, a - 1) if S - 1 >= a - 1 >= 0 else 0
        print(f"{a:>6} | {S:>8} | {fmt_big(n_comps):>28} | {classifica(a)}")

    print()
    print("=" * 90)
    print("PARTE 4: candidatos entre nosso wall (~25) e a literatura (91), por excesso")
    print("(MENOR excesso = mais dificil de excluir analiticamente via Baker, NAO uma")
    print(" previsao sobre o tamanho de n0 -- ver correcao no docstring do modulo)")
    print("=" * 90)
    entre_wall_e_literatura = [
        (S, a) for (S, a) in todos
        if NOSSO_WALL_REDUZIDO < a <= LITERATURA_ATUAL
    ]
    entre_wall_e_literatura.sort(key=lambda t: float(t[0] - t[1] * LOG2_3))
    print(f"\n{len(entre_wall_e_literatura)} candidatos nessa faixa, ordenados por "
          f"excesso crescente:\n")
    for S, a in entre_wall_e_literatura:
        L = float(S - a * LOG2_3)
        n_comps = math.comb(S - 1, a - 1) if S - 1 >= a - 1 >= 0 else 0
        print(f"  a={a:>4}, S={S:>4}, excesso={L:.4e}, C(S-1,a-1)={fmt_big(n_comps)}")

    print()
    print("=" * 90)
    print("VEREDITO")
    print("=" * 90)
    print("""
Confirmado: os convergentes (e semiconvergentes) da fracao continua de
log2(3) sao EXATAMENTE os valores de 'a' com menor excesso residual
L(a,S) para seu tamanho -- os candidatos analiticamente mais dificeis
de excluir via cotas de Baker. Isso reproduz (nao descobre) a base da
tecnica classica de Steiner/Simons/de Weger/Hercher.

CORRECAO IMPORTANTE (encontrada via advisor(), antes de finalizar): a
primeira versao deste experimento interpretava "menor excesso" como
"menor n0 possivel", o que e o OPOSTO do correto. Para a composicao que
MINIMIZA n0 (forma fechada (1,1,...,1,S-a+1), confirmada por enumeracao
exaustiva em a=3,5,17): n0_min = (3^a-2^a)/(2^S-3^a) ~= 1/(L*ln2) --
MENOR excesso implica n0_min MAIOR, nao menor (Parte 2b). Mas isso e so
o minimo sobre composicoes: uma composicao diferente e desconhecida
pode dar n0 muitas ordens de grandeza maior para o MESMO par (a,S)
(verificado: a=306 com composicao "ruim" da n0~10^25 contra
n0_min~10^3). Ou seja, L(a,S) pequeno mede dificuldade analitica de
exclusao, NAO o tamanho de um eventual ciclo -- essas sao perguntas
diferentes.

A checagem real de autoconsistencia (Parte 2) nos convergentes/
semiconvergentes DENTRO do nosso alcance computacional (a=3,5,17) NAO
encontrou nenhum ciclo -- e mais forte que isso: para NENHUMA das
5.311.735 composicoes testadas em a=17 (nem nas 6 de a=3, nem nas 35 de
a=5) existe sequer um n0 inteiro positivo, ou seja, a propria condicao
de divisibilidade (nao so a autoconsistencia) ja falha para todas elas.
Consistente com H-009/H-034 (que e uma janela mais ampla ao redor do
mesmo S, entao este resultado e um SUBCONJUNTO do que H-034 ja cobria,
nao uma checagem adicionalmente mais precisa).

Contribuicao desta sintese para o projeto (nao nova matematica, mas
nova conexao): a quantidade L(a,S) = S - a*log2(3) usada aqui para um
PAR ABSTRATO (a,S) e EXATAMENTE a mesma formula L_k(n) = k*log2(3) -
A_k(n) (so com sinal trocado) que aparece em TODOS os ~7 papers de
Ruiz Castillo revisados nesta colecao, aplicada la a trajetorias REAIS
de n especificos. A tecnica profissional de exclusao de ciclos e,
nesse sentido, a MESMA quantidade de "deuda residual" onipresente nos
papers de Ruiz Castillo, so que aplicada a pergunta "existe algum par
(a,S) que ADMITE excesso zero exatamente" em vez de "qual e o
comportamento assintotico do excesso ao longo de uma trajetoria real"
-- a fracao continua garante que NUNCA existe excesso exatamente zero
(log2(3) e irracional), e quantifica precisamente quao perto isso pode
chegar para cada tamanho de ciclo, e quao dificil fica EXCLUIR
analiticamente esses candidatos conforme o excesso encolhe.
""")
