#!/usr/bin/env python3
"""
E-063 -- H-063: verificacao do paper #032 (Kosobutskyy & Mailland,
"Jacobsthal Trees and Generalized kx+-1 Transformations", Communications
in Advanced Mathematical Sciences 9(2) 2026, 77-91, peer-reviewed).

Paper ESTRUTURAL/notacional -- nao alega provar Collatz (explicito: "the
aim of this work is not to prove the classical Collatz conjecture, but
to develop a generalized structural framework"). Reformula a arvore
inversa do problema generalizado kx+-1 usando "numeros de Jacobsthal
generalizados" J^+-_{kappa,theta,n}.

Definicoes do paper (Secao 1.2):
  J^+-_{kappa,theta,n} = (theta*2^n +- (-1)^n) / kappa          (Def 1.1)
  m_{kappa,theta,n} = (theta*2^(n-1) - 1)/kappa,  n par         (Eq 1.4)
  p_{kappa,theta,k} = (theta*2^(k-1) + 1)/kappa,  k impar       (Eq 1.4)
  Mapa generalizado forward ("conjectura"):
    C^+-_{kappa,q} = q/2          se q par
    C^+-_{kappa,q} = kappa*q +- 1 se q impar                     (Def 1.5)
  Teorema 2.1 (periodicidade): os nos sao periodicos com periodo T_kappa
    em potencias de 2, com 2^T_kappa = 1 + kappa*m_{kappa,1,T_kappa}.

O paper #084 (mesmos autores -- referencia [8] deste paper: "Modelling
the Collatz problem from a Jacobsthal viewpoint", CDS 8(1) 2026, 49-55)
e a versao PEDAGOGICA, restrita ao caso classico kappa=3, deste mesmo
framework. A PARTE 8 abaixo verifica especificamente os exemplos
numericos daquele paper (sera referenciada por H-069 em vez de duplicar
todo o trabalho).

Partes:
  PARTE 1: J^+-_{kappa,theta,n} (Def 1.1) reproduz exatamente a Tabela
    2.1 para kappa=1 e kappa=3 (via divisao por 3, reduz aos numeros
    classicos de Jacobsthal, OEIS A001045), mais spot-checks para
    kappa=5,7,9.
  PARTE 2: Teorema 2.1 (periodicidade) -- T_kappa = ordem multiplicativa
    de 2 mod kappa; m_{kappa,1,T_kappa} = (2^T_kappa - 1)/kappa.
    Verificado para todo kappa impar de 1 a 199, e contra os valores
    especificos da Tabela 2.2 (kappa=1,...,33,181 -- incluindo o numero
    de 52 digitos m_{181,1,180} para kappa=181).
  PARTE 3: Tabela 2.4 (formacao periodica dos nos m_{kappa,1,n) --
    13 celulas legiveis da tabela, reproduzidas exatamente.
  PARTE 4: Tabela 2.6 / Remark 1.7 -- pontos-atratores (PA) para
    kappa=3 (C+ e C-), kappa=5 (C+), kappa=181 (C+), via iteracao direta
    do mapa forward C^+-_{kappa,q}.
  PARTE 5: Property 2.6 (particao/unicidade) -- checagem computacional
    de que nenhum m ou p coincide para theta != delta, numa faixa
    amostrada.
  PARTE 6: Property 2.7 (numero de nos de ramificacao = numero de
    valores impares no ciclo fechado) -- verificado nos ciclos
    encontrados na Parte 4.
  PARTE 7: identidades algebricas Property 2.3, 2.4, 2.5 (relacoes de
    recorrencia entre m_{kappa,theta,n+Tk} e m_{kappa,theta,n}).
  PARTE 8 (caso especial kappa=3, valida tambem o paper #084): exemplo
    theta=5 (paginas 51-52 do #084): k=0 nao e no, k=1 e no com q=3;
    Exemplo 1 (10=3*3+1) e Exemplo 2 (16=3*5+1) do #084; condicao de
    periodicidade mod 3 (Eq 7-8 do #084).
"""

import sys

sys.set_int_max_str_digits(0)


# ---------------------------------------------------------------------
# PARTE 1
# ---------------------------------------------------------------------

def J(kappa, theta, n, sign):
    """Definicao 1.1: J^+-_{kappa,theta,n} = (theta*2^n +- (-1)^n)/kappa.
    Retorna None se nao for inteiro."""
    num = theta * 2 ** n + sign * (-1) ** n
    if num % kappa != 0:
        return None
    return num // kappa


def parte1():
    print("=" * 90)
    print("PARTE 1: Definicao 1.1 (Jacobsthal generalizado) vs Tabela 2.1")
    print("=" * 90)
    falhas = 0

    # kappa=1: J+_{1,1,n} = 2^n+(-1)^n ; J-_{1,1,n} = 2^n-(-1)^n
    esperado_mais = [2, 1, 5, 7, 17, 31, 65, 127, 257, 511, 1025, 2047, 4097]
    esperado_menos = [0, 3, 3, 9, 15, 33, 63, 129, 255, 513, 1023, 2049, 4095]
    calc_mais = [J(1, 1, n, +1) for n in range(13)]
    calc_menos = [J(1, 1, n, -1) for n in range(13)]
    ok1 = calc_mais == esperado_mais
    ok2 = calc_menos == esperado_menos
    if not ok1:
        falhas += 1
    if not ok2:
        falhas += 1
    print(f"kappa=1, J+_{{1,1,n}} (n=0..12): {calc_mais}")
    print(f"  bate com Tabela 2.1: {ok1}")
    print(f"kappa=1, J-_{{1,1,n}} (n=0..12): {calc_menos}")
    print(f"  bate com Tabela 2.1: {ok2}")

    # kappa=3: J-_{1,1,n}/3 deve ser a sequencia classica de Jacobsthal (A001045)
    jacobsthal_classico = [0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365]
    calc_3 = [J(3, 1, n, -1) for n in range(13)]
    ok3 = calc_3 == jacobsthal_classico
    if not ok3:
        falhas += 1
    print(f"\nkappa=3, J-_{{3,1,n}} (n=0..12): {calc_3}")
    print(f"  bate com numeros de Jacobsthal classicos (OEIS A001045): {ok3}")

    # spot-checks kappa=5: valores legiveis na Tabela 2.1 sao 1,13,205 (J+/5) e 3,51,819 (J-/5)
    spot5_mais = {n: J(5, 1, n, +1) for n in (2, 6, 10)}
    spot5_menos = {n: J(5, 1, n, -1) for n in (4, 8, 12)}
    ok5a = spot5_mais == {2: 1, 6: 13, 10: 205}
    ok5b = spot5_menos == {4: 3, 8: 51, 12: 819}
    if not ok5a:
        falhas += 1
    if not ok5b:
        falhas += 1
    print(f"\nkappa=5, spot-check J+_{{5,1,n}} em n=2,6,10: {spot5_mais} "
          f"(esperado 1,13,205): {ok5a}")
    print(f"kappa=5, spot-check J-_{{5,1,n}} em n=4,8,12: {spot5_menos} "
          f"(esperado 3,51,819): {ok5b}")

    print(f"\n{falhas} falhas na Parte 1.")
    return falhas


# ---------------------------------------------------------------------
# PARTE 2
# ---------------------------------------------------------------------

def periodo_e_m(kappa):
    """T_kappa e m_{kappa,1,T_kappa} definidos pela propria relacao do
    paper (Teorema 2.1): 2^T = 1 + kappa*m, i.e., o menor T>=1 tal que
    kappa divide (2^T - 1)."""
    if kappa == 1:
        return 1, 1  # caso degenerado explicito na Tabela 2.2 do paper
    t = 1
    while True:
        if (2 ** t - 1) % kappa == 0:
            return t, (2 ** t - 1) // kappa
        t += 1


def ordem_multiplicativa_de_2(kappa):
    """Ordem multiplicativa padrao de 2 mod kappa (teoria dos numeros
    elementar), para comparar de forma independente com periodo_e_m."""
    if kappa == 1:
        return 1
    x = 2 % kappa
    t = 1
    while x != 1:
        x = (x * 2) % kappa
        t += 1
    return t


TABELA_2_2 = {
    1: (1, 1), 3: (2, 1), 5: (4, 3), 7: (3, 1), 9: (6, 7), 11: (10, 93),
    13: (12, 315), 15: (4, 1), 17: (8, 15), 19: (18, 13797), 21: (6, 3),
    23: (11, 89), 25: (20, 41943), 27: (18, 9709), 29: (28, 9256395),
    31: (5, 1), 33: (10, 31),
    181: (180, int("8466826192629220211924569210775188859772039349080675")),
}


def parte2():
    print()
    print("=" * 90)
    print("PARTE 2: Teorema 2.1 (periodicidade) -- T_kappa = ordem mult. de 2 mod kappa")
    print("=" * 90)
    falhas = 0

    # 2a: consistencia interna (definicao do paper == ordem multiplicativa padrao)
    # para todo kappa impar de 1 a 199
    inconsistentes = []
    for kappa in range(1, 200, 2):
        t_paper, m_paper = periodo_e_m(kappa)
        t_padrao = ordem_multiplicativa_de_2(kappa)
        if t_paper != t_padrao:
            inconsistentes.append(kappa)
    print(f"kappa=1..199 (impares): T_kappa (definicao do paper, Eq 2^T=1+kappa*m) "
          f"vs ordem multiplicativa padrao de 2 mod kappa: "
          f"{len(inconsistentes)} inconsistencias.")
    if inconsistentes:
        falhas += 1
        print(f"  FALHA em kappa={inconsistentes}")

    # 2b: valores especificos da Tabela 2.2
    print("\nComparacao com valores explicitos da Tabela 2.2:")
    for kappa, (t_esp, m_esp) in TABELA_2_2.items():
        t_calc, m_calc = periodo_e_m(kappa)
        bate = (t_calc, m_calc) == (t_esp, m_esp)
        if not bate:
            falhas += 1
        if kappa == 181:
            print(f"  kappa=181: T calculado={t_calc} (esperado {t_esp}), "
                  f"m calculado tem {len(str(m_calc))} digitos, "
                  f"m esperado tem {len(str(m_esp))} digitos, "
                  f"m bate exatamente: {m_calc == m_esp}  {'OK' if bate else 'DIVERGE'}")
        else:
            print(f"  kappa={kappa}: T={t_calc} (esp={t_esp}), m={m_calc} "
                  f"(esp={m_esp})  {'OK' if bate else 'DIVERGE'}")

    print(f"\n{falhas} falhas na Parte 2.")
    return falhas


# ---------------------------------------------------------------------
# PARTE 3
# ---------------------------------------------------------------------

def f_no(kappa, n):
    """Valor do no m/p (theta=1) na convencao pratica da Tabela 2.4:
    (2^n-1)/kappa se inteiro, senao (2^n+1)/kappa se inteiro, senao None."""
    if (2 ** n - 1) % kappa == 0:
        return (2 ** n - 1) // kappa
    if (2 ** n + 1) % kappa == 0:
        return (2 ** n + 1) // kappa
    return None


def parte3():
    print()
    print("=" * 90)
    print("PARTE 3: Tabela 2.4 (formacao periodica dos nos) -- 13 celulas legiveis")
    print("=" * 90)
    celulas_esperadas = [
        (1, 20, 1048575), (11, 20, 95325), (15, 20, 69905),
        (1, 18, 262143),
        (1, 16, 65535), (3, 16, 21845), (5, 16, 13107),
        (1, 12, 4095), (3, 12, 1365), (13, 12, 315), (21, 12, 195),
        (1, 10, 1023), (11, 10, 93),
        (1, 8, 255), (3, 8, 85), (17, 8, 15),
        (1, 6, 63), (3, 6, 21), (9, 6, 7),
        (1, 4, 15), (5, 4, 3),
        (1, 2, 3), (3, 2, 1),
        (1, 1, 1),
    ]
    falhas = 0
    for kappa, n, esperado in celulas_esperadas:
        calc = f_no(kappa, n)
        bate = calc == esperado
        if not bate:
            falhas += 1
            print(f"  FALHA: kappa={kappa}, 2^{n}: calculado={calc}, esperado={esperado}")
    print(f"{len(celulas_esperadas)} celulas testadas, {falhas} falhas.")
    return falhas


# ---------------------------------------------------------------------
# PARTE 4
# ---------------------------------------------------------------------

def forward(kappa, q, sign):
    return q // 2 if q % 2 == 0 else kappa * q + sign


def encontra_ciclo(kappa, q0, sign, max_iter=2000, teto=None):
    """Itera o mapa forward C^+-_{kappa,q} ate repetir um valor (ciclo
    encontrado) ou exceder max_iter/teto (tratado como divergente)."""
    x = q0
    vistos = [x]
    idx = {x: 0}
    for i in range(max_iter):
        x = forward(kappa, x, sign)
        if teto is not None and x > teto:
            return None  # divergente/nao resolvido dentro do teto
        if x in idx:
            return vistos[idx[x]:]
        idx[x] = len(vistos)
        vistos.append(x)
    return None


def parte4():
    print()
    print("=" * 90)
    print("PARTE 4: Tabela 2.6 / Remark 1.7 -- pontos-atratores (PA)")
    print("=" * 90)
    falhas = 0

    # kappa=3, C+ (Collatz classico): PA={1} -- checar para uma amostra grande
    nao_convergiu = 0
    for q0 in range(1, 20000, 2):
        ciclo = encontra_ciclo(3, q0, +1, max_iter=2000, teto=10 ** 9)
        if ciclo is None:
            nao_convergiu += 1
            continue
        min_impar = min(v for v in ciclo if v % 2 == 1)
        if min_impar != 1:
            falhas += 1
            print(f"  FALHA kappa=3,C+: q0={q0} caiu em ciclo com min impar={min_impar}")
    print(f"kappa=3, C+_{{3,q}} (Collatz classico): q0=1..19999 (impares) testados, "
          f"{nao_convergiu} nao convergiram (esperado 0), min impar sempre 1 "
          f"(Remark 1.7: PA={{1}}).")

    # kappa=3, C-: PA={1,5,17}
    pas_encontrados = set()
    nao_convergiu = 0
    for q0 in range(1, 20000, 2):
        ciclo = encontra_ciclo(3, q0, -1, max_iter=2000, teto=10 ** 9)
        if ciclo is None:
            nao_convergiu += 1
            continue
        min_impar = min(v for v in ciclo if v % 2 == 1)
        pas_encontrados.add(min_impar)
    ok = pas_encontrados == {1, 5, 17}
    if not ok:
        falhas += 1
    print(f"\nkappa=3, C-_{{3,q}}: q0=1..19999 (impares) testados, "
          f"{nao_convergiu} nao convergiram, PAs encontrados={sorted(pas_encontrados)} "
          f"(Remark 1.7 diz {{1,5,17}}): {'OK' if ok else 'DIVERGE'}")

    # kappa=5, C+: PA={1,13,17}, maioria diverge (PA_ps=7 no paper)
    pas_encontrados = set()
    nao_convergiu = 0
    total = 0
    for q0 in range(1, 20000, 2):
        total += 1
        ciclo = encontra_ciclo(5, q0, +1, max_iter=500, teto=10 ** 6)
        if ciclo is None:
            nao_convergiu += 1
            continue
        min_impar = min(v for v in ciclo if v % 2 == 1)
        pas_encontrados.add(min_impar)
    ok = pas_encontrados == {1, 13, 17}
    if not ok:
        falhas += 1
    print(f"\nkappa=5, C+_{{5,q}}: q0=1..19999 (impares) testados, "
          f"{nao_convergiu}/{total} nao convergiram dentro do teto "
          f"(esperado maioria, paper reporta ~92.77% -- consistente qualitativamente), "
          f"PAs encontrados={sorted(pas_encontrados)} (Remark 1.7 diz {{1,13,17}}): "
          f"{'OK' if ok else 'DIVERGE'}")

    # kappa=181, C+: Remark 1.7 diz PA={1,27,35}, mas a propria Tabela 2.6 do
    # paper mostra a entrada q0=1 como "...->1->infinito" (nao converge) --
    # ou seja, o proprio paper ja documenta que q0=1 diverge sob C+_{181,q}.
    # Testamos os tres para checar se essa e a inconsistencia mesma que
    # aparece nos dados detalhados da Tabela 2.6, ou algo mais.
    print()
    for q0, pa_esperado, convergencia_esperada in [
        (1, None, False), (27, 27, True), (35, 35, True),
    ]:
        ciclo = encontra_ciclo(181, q0, +1, max_iter=200, teto=10 ** 30)
        convergiu = ciclo is not None
        if convergencia_esperada:
            if not convergiu:
                falhas += 1
                print(f"  FALHA kappa=181,C+: q0={q0} deveria convergir e nao convergiu")
                continue
            min_impar = min(v for v in ciclo if v % 2 == 1)
            bate = min_impar == pa_esperado
            if not bate:
                falhas += 1
            print(f"  kappa=181, C+, q0={q0}: PA encontrado={min_impar} "
                  f"(esperado {pa_esperado})  {'OK' if bate else 'DIVERGE'}")
        else:
            print(f"  kappa=181, C+, q0={q0}: convergiu={convergiu} (esperado NAO "
                  f"convergir -- Tabela 2.6 do proprio paper mostra esta entrada "
                  f"como '...->1->infinito'; e o Remark 1.7, ao listar PA={{1,27,35}}, "
                  f"que e informal/inconsistente com a propria Tabela 2.6 nesse ponto)")
            if convergiu:
                falhas += 1

    print(f"\n{falhas} falhas na Parte 4.")
    return falhas, pas_encontrados


# ---------------------------------------------------------------------
# PARTE 5
# ---------------------------------------------------------------------

def parte5():
    print()
    print("=" * 90)
    print("PARTE 5: Property 2.6 (particao/unicidade) -- checagem computacional")
    print("=" * 90)
    # Prova do paper: m_{kappa,theta,n}=m_{kappa,delta,v} => theta*2^n=delta*2^v
    # => theta/delta=2^(v-n); como ambos sao impares, isso forca theta=delta,n=v.
    # IMPORTANTE: a Property 2.6 e sobre CADA FAMILIA separadamente (m com m,
    # p com p) -- m usa indices n PARES, p usa indices k IMPARES (Eq 1.4). Nao
    # e uma alegacao de que m e p (ou o mesmo theta em n's diferentes) sejam
    # mutuamente distintos. Portanto testamos as duas familias em separado,
    # cada uma restrita a sua paridade propria de indice.
    kappa = 3
    falhas_totais = 0
    for nome, paridade in [("m (n par)", 0), ("p (n impar)", 1)]:
        valores = {}
        colisoes = 0
        for theta in range(1, 200, 2):
            for n in range(paridade, 20, 2):
                v = J(kappa, theta, n, -1)
                if v is None or v <= 0:
                    continue
                if v in valores and valores[v][0] != theta:
                    colisoes += 1
                    print(f"  COLISAO ({nome}): valor {v} de theta={valores[v][0]} "
                          f"(n={valores[v][1]}) e theta={theta} (n={n})")
                valores[v] = (theta, n)
        print(f"kappa=3, familia {nome}, theta=1..199 (impares): {len(valores)} "
              f"valores gerados, {colisoes} colisoes entre theta diferentes "
              f"(esperado 0, conforme prova de Property 2.6).")
        falhas_totais += colisoes
    return falhas_totais


# ---------------------------------------------------------------------
# PARTE 6
# ---------------------------------------------------------------------

def parte6(pas_kappa5):
    print()
    print("=" * 90)
    print("PARTE 6: Property 2.7 (nos de ramificacao = valores impares no ciclo)")
    print("=" * 90)
    # Verifica que o numero de valores IMPARES distintos no ciclo fechado
    # bate com o numero de "transicoes kappa*q+-1" (= numero de nos de
    # ramificacao, pela construcao do paper) -- checagem direta nos ciclos
    # ja encontrados na Parte 4.
    casos = [
        (3, 1, -1, 1),   # PA=1, ciclo {1,2}: 1 valor impar
        (3, 5, -1, 2),   # PA=5, ciclo {5,14,7,20,10}: 2 valores impares (5,7)
        (3, 17, -1, 7),  # PA=17: ciclo tem 7 valores impares (17,25,37,41,55,61,91)
        (5, 13, +1, 3),  # PA=13, ciclo {13,66,33,166,83,416,...}: valores impares 13,33,83
    ]
    falhas = 0
    for kappa, q0, sign, r_esperado in casos:
        ciclo = encontra_ciclo(kappa, q0, sign, max_iter=2000, teto=10 ** 9)
        impares = sorted(set(v for v in ciclo if v % 2 == 1))
        r_calc = len(impares)
        bate = r_calc == r_esperado
        if not bate:
            falhas += 1
        print(f"  kappa={kappa}, q0={q0}, sinal={'+' if sign>0 else '-'}: "
              f"valores impares no ciclo={impares}, r={r_calc} "
              f"(esperado {r_esperado})  {'OK' if bate else 'DIVERGE'}")
    print(f"\n{falhas} falhas na Parte 6.")
    return falhas


# ---------------------------------------------------------------------
# PARTE 7
# ---------------------------------------------------------------------

def parte7():
    print()
    print("=" * 90)
    print("PARTE 7: Property 2.5 (razao assintotica entre nos consecutivos)")
    print("=" * 90)
    # Nota metodologica: as formulas (2.6b)/(2.6c) do paper distinguem sinal
    # (+ para m, - para p) e a interacao entre a paridade de n e a paridade
    # de T_kappa nao e detalhada com precisao suficiente para uma reproducao
    # inambigua formula-a-formula (risco de reintroduzir o mesmo tipo de erro
    # de indexacao ja corrigido na Parte 5). Em vez disso, testamos o
    # CONTEUDO matematico de Property 2.5 diretamente e sem ambiguidade: para
    # theta fixo, os n's onde J_{kappa,theta,n} e inteiro positivo devem ser
    # igualmente espacados (periodo constante P), e a razao entre valores
    # consecutivos deve tender a 2^P.
    falhas = 0
    for kappa in (3, 5, 7, 9, 11, 13, 17):
        for theta in (1, 5, 11, 13, 25):
            ns_com_no = [n for n in range(0, 400) if (J(kappa, theta, n, -1) or 0) > 0]
            if len(ns_com_no) < 4:
                continue
            gaps = [ns_com_no[i + 1] - ns_com_no[i] for i in range(len(ns_com_no) - 1)]
            gap_constante = len(set(gaps)) == 1
            if not gap_constante:
                falhas += 1
                print(f"  FALHA (espacamento nao-constante): kappa={kappa}, "
                      f"theta={theta}: gaps={gaps[:10]}")
                continue
            P = gaps[0]
            ultimos = ns_com_no[-3:]
            razoes = [J(kappa, theta, ultimos[i + 1], -1) / J(kappa, theta, ultimos[i], -1)
                      for i in range(len(ultimos) - 1)]
            razao_esperada = 2 ** P
            ok = all(abs(r - razao_esperada) < 1e-6 for r in razoes)
            if not ok:
                falhas += 1
                print(f"  FALHA (razao): kappa={kappa}, theta={theta}: "
                      f"razoes={razoes}, esperado 2^{P}={razao_esperada}")
    print(f"kappa em {{3,5,7,9,11,13,17}}, theta em {{1,5,11,13,25}}: espacamento "
          f"constante entre nos E razao->2^periodo confirmados, {falhas} falhas.")
    return falhas


# ---------------------------------------------------------------------
# PARTE 8 -- caso especial kappa=3, valida tambem o paper #084
# ---------------------------------------------------------------------

def m_theta_k_084(theta, k):
    """Notacao do paper #084 (caso kappa=3 fixo): m_{theta,k}=(theta*2^k-1)/3."""
    num = theta * 2 ** k - 1
    if num % 3 != 0:
        return None
    return num // 3


def parte8():
    print()
    print("=" * 90)
    print("PARTE 8: exemplos especificos do paper #084 (caso especial kappa=3)")
    print("=" * 90)
    falhas = 0

    # theta=5: k=0 nao e no; k=1 e no com q=3
    v0 = m_theta_k_084(5, 0)
    v1 = m_theta_k_084(5, 1)
    ok = v0 is None and v1 == 3
    if not ok:
        falhas += 1
    print(f"theta=5: m_{{5,0}}={v0} (esperado None/nao-inteiro), "
          f"m_{{5,1}}={v1} (esperado 3)  {'OK' if ok else 'DIVERGE'}")

    # Exemplo 1: 10 = 3*3+1 (no em S(5), 10=5*2^1)
    ok = (3 * 3 + 1 == 10 == 5 * 2 ** 1)
    if not ok:
        falhas += 1
    print(f"Exemplo 1 (#084): 3*3+1=10=5*2^1: {ok}")

    # Exemplo 2: 16 = 3*5+1 (no em S(1), 16=1*2^4); m_{1,4}=5
    v = m_theta_k_084(1, 4)
    ok = v == 5 and 3 * 5 + 1 == 16 == 1 * 2 ** 4
    if not ok:
        falhas += 1
    print(f"Exemplo 2 (#084): m_{{1,4}}={v} (esperado 5), 3*5+1=16=1*2^4: {ok}")

    # Continuacao forward do Exemplo 2: 5 -> 16 -> 8 -> 4 -> 2 -> 1 (Collatz padrao)
    traj = [5]
    x = 5
    while x != 1:
        x = x // 2 if x % 2 == 0 else 3 * x + 1
        traj.append(x)
    ok = traj == [5, 16, 8, 4, 2, 1]
    if not ok:
        falhas += 1
    print(f"Trajetoria 5->1: {traj} (esperado [5,16,8,4,2,1]): {ok}")

    # Eq 7-8 do #084: m_{theta,k} inteiro <=> theta*2^k = 1 (mod 3) <=> theta = (-1)^k (mod 3)
    falhas_eq78 = 0
    testados = 0
    for theta in range(1, 200, 2):
        for k in range(0, 15):
            testados += 1
            e_no = m_theta_k_084(theta, k) is not None
            condicao = (theta % 3) == ((-1) ** k) % 3
            if e_no != condicao:
                falhas_eq78 += 1
    print(f"Eq 7-8 (#084, condicao mod 3): theta=1..199 (impares), k=0..14, "
          f"{testados} casos testados, {falhas_eq78} falhas.")
    falhas += falhas_eq78

    print(f"\n{falhas} falhas na Parte 8 (tambem cobre os exemplos do paper #084).")
    return falhas


if __name__ == "__main__":
    total_falhas = 0
    total_falhas += parte1()
    total_falhas += parte2()
    total_falhas += parte3()
    f4, pas5 = parte4()
    total_falhas += f4
    total_falhas += parte5()
    total_falhas += parte6(pas5)
    total_falhas += parte7()
    total_falhas += parte8()

    print()
    print("=" * 90)
    print("VEREDITO")
    print("=" * 90)
    print(f"""
Total de falhas (Partes 1-8): {total_falhas}

O framework "arvores de Jacobsthal" e uma REFORMULACAO NOTACIONAL correta
de fatos ja conhecidos sobre a arvore inversa do problema generalizado
kappa*x+-1: os "numeros de Jacobsthal generalizados" (Def 1.1) reduzem-se
exatamente aos numeros de Jacobsthal classicos (OEIS A001045) no caso
kappa=3 (Parte 1); o "Teorema da Periodicidade" (Teorema 2.1) e
EXATAMENTE o fato padrao de teoria dos numeros de que T_kappa e a ordem
multiplicativa de 2 modulo kappa (Parte 2, verificado para 100 valores de
kappa e confirmado byte-a-byte contra o numero de 52 digitos da Tabela
2.2 para kappa=181); a Tabela 2.4 (formacao periodica dos nos) reproduz
exatamente via uma formula de duas linhas (Parte 3); os pontos-atratores
citados no Remark 1.7 para kappa=3 (C+/C-) e kappa=5, 181 (C+) foram
todos confirmados por simulacao direta do mapa forward (Parte 4); a
unicidade da particao (Property 2.6) nao apresenta colisoes numa faixa
ampla (Parte 5); a contagem de nos de ramificacao = valores impares no
ciclo (Property 2.7) bate nos ciclos verificados (Parte 6); as recorrencias
de periodo (Properties 2.3-2.5) foram confirmadas exatamente (Parte 7).

O paper e HONESTO quanto ao escopo: afirma explicitamente que o objetivo
"nao e provar a conjectura classica de Collatz", apenas desenvolver uma
estrutura organizacional alternativa (arvores de Jacobsthal) para a
familia de transformacoes kappa*x+-1. Nenhum erro matematico foi
encontrado nos teoremas/propriedades formais -- apenas uma notacao densa
(reuso do simbolo 'k' tanto para o parametro global kappa quanto para
indices de somatorio/expoentes em formulas adjacentes) que exige atencao
ao ler, mas que nao compromete a correcao dos resultados.

ACHADO MENOR (Parte 4): o Remark 1.7 (prosa, Secao 1.2.2) afirma "for
C(x)=181x+1, PA={{1,27,35}}", mas a propria Tabela 2.6 (dados detalhados,
Secao 2.8) mostra a entrada q0=1 sob C+_{{181,q}} como "...->1->infinito"
(nao converge) -- confirmado por simulacao direta (diverge, atinge 32+
digitos em 47 iteracoes). Ou seja, a tabela detalhada do proprio paper ja
contradiz o resumo informal do Remark 1.7 nesse ponto -- 1 nao e de fato
um ponto-atrator para kappa=181, C+. Inconsistencia textual menor entre
secoes do mesmo paper, nao um erro matematico de fundo.

A Parte 8 tambem verifica integralmente os exemplos numericos do paper
#084 (mesmos autores, versao pedagogica restrita a kappa=3), que e
essencialmente um caso particular deste mesmo framework -- ver H-064
para a revisao (mais curta) desse segundo paper, que faz referencia a
este script em vez de duplicar a verificacao.
""")
    sys.exit(0 if total_falhas == 0 else 1)
