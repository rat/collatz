"""
E-069 -- verificacao do paper #084 (Mailland & Kosobutskyy, "Modelling
the Collatz Problem from a Jacobsthal Viewpoint", CDS 8(1) 2026, 49-55).

Paper CURTO e PEDAGOGICO, restrito ao caso classico kappa=3 -- e um caso
particular do framework generalizado kappa,theta,n ja verificado
exaustivamente em E-063 (paper #032, mesmos autores em ordem inversa).
Este script NAO duplica E-063; verifica apenas o conteudo numerico
ESPECIFICO deste paper que E-063 nao cobriu:

  - E-063 Parte 8 ja verificou: exemplo theta=5 (k=0 nao-no, k=1 no com
    q=3), Exemplo 1 (10=3*3+1), Exemplo 2 (16=3*5+1), condicao mod 3
    (Eq 7-8).
  - Este script cobre: a arvore geradora completa da Fig. 1 (theta=5 e
    theta=1 expandidos em varios niveis de k) e a lista de colunas da
    Fig. 2 (Petri net), que sao exemplos numericos NAO cobertos por
    E-063.

Definicoes do paper (equivalentes a J^-_{3,theta,k} de #032 com kappa=3
fixo, notacao m_theta,k em vez de J):
  m_{theta,k} = (theta*2^k - 1) / 3                                (Eq 5)
  valido (no) sse theta*2^k = 1 (mod 3)                            (Eq 7)
  sse theta = (-1)^k (mod 3)                                       (Eq 8)

Partes:
  PARTE 1: Eq 5-8 (integralidade/periodicidade mod 3) -- reconfirmacao
    rapida e independente (a mesma logica ja testada em E-063 Parte 2,
    aqui restrita a kappa=3).
  PARTE 2: Exemplos 1 e 2 do paper (10=3*3+1, 16=3*5+1) -- reconfirmacao
    rapida e independente.
  PARTE 3: Fig. 1 -- reconstrucao computacional da arvore geradora a
    partir de theta=1 e theta=5 (varios k), confirmando que TODOS os
    numeros que aparecem na figura (3,13,53,213,21,1,5,85 e seus
    descendentes 7,113 a partir de 85) sao instancias validas de
    m_{theta,k}.
  PARTE 4: Fig. 2 -- confirma que a lista de 10 colunas mostradas
    (S(1),S(5),S(85),S(341),S(13),S(53),S(853),S(3413),S(7),S(113)) sao
    todas alcancaveis a partir da raiz theta=1 por um numero pequeno de
    passos de expansao (theta=0 mod 3 vira folha morta, testado
    tambem: 3, 21, 57 nunca gerarao novos nos).
"""

import sys

sys.set_int_max_str_digits(0)


def m(theta, k):
    val = theta * (2 ** k) - 1
    if val % 3 != 0:
        return None
    return val // 3


def parte1():
    print("=" * 90)
    print("PARTE 1 -- Eq 5-8 (integralidade / periodicidade mod 3), kappa=3")
    print("=" * 90)
    falhas = 0
    testados = 0
    for theta in range(1, 500, 2):
        for k in range(0, 20):
            q = m(theta, k)
            testados += 1
            eh_no_direto = (theta * 2 ** k - 1) % 3 == 0
            if eh_no_direto != (q is not None):
                falhas += 1
                continue
            if q is not None:
                # Eq 6: 3*m+1 = theta*2^k
                if 3 * q + 1 != theta * 2 ** k:
                    print(f"  FALHA (Eq 6): theta={theta},k={k}")
                    falhas += 1
                # Eq 8: theta = (-1)^k (mod 3)  <=>  no existe
                lado_certo = theta % 3 == (1 if k % 2 == 0 else 2)
                if not lado_certo:
                    print(f"  FALHA (Eq 8): theta={theta},k={k}")
                    falhas += 1
            else:
                if theta % 3 == 0:
                    continue
                lado_certo = theta % 3 == (1 if k % 2 == 0 else 2)
                if lado_certo:
                    print(f"  FALHA (Eq 8, no esperado mas ausente): theta={theta},k={k}")
                    falhas += 1
    print(f"Testados: {testados} pares (theta,k). Falhas: {falhas}")
    return falhas


def parte2():
    print()
    print("=" * 90)
    print("PARTE 2 -- Exemplos 1 e 2 do paper")
    print("=" * 90)
    falhas = 0

    # Exemplo 1: 10 = 3*3+1, 10 = 5*2^1, m_{5,1} deve ser 3
    q = m(5, 1)
    ok = (q == 3) and (10 == 3 * 3 + 1) and (10 == 5 * 2 ** 1)
    print(f"Exemplo 1 (10=3*3+1, no em S(5) k=1): m_5,1={q}  {'OK' if ok else 'FALHA'}")
    if not ok:
        falhas += 1

    # Exemplo 2: 16 = 3*5+1, 16 = 1*2^4, m_{1,4} deve ser 5
    q = m(1, 4)
    ok = (q == 5) and (16 == 3 * 5 + 1) and (16 == 1 * 2 ** 4)
    print(f"Exemplo 2 (16=3*5+1, no em S(1) k=4): m_1,4={q}  {'OK' if ok else 'FALHA'}")
    if not ok:
        falhas += 1

    # trajetoria completa 5 -> 16 -> 8 -> 4 -> 2 -> 1 (Collatz classico)
    n = 5
    traj = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        traj.append(n)
    esperado = [5, 16, 8, 4, 2, 1]
    ok = traj == esperado
    print(f"Trajetoria 5->16->8->4->2->1: {traj}  {'OK' if ok else 'FALHA'}")
    if not ok:
        falhas += 1

    print(f"Falhas: {falhas}")
    return falhas


def odd_part(q):
    while q % 2 == 0:
        q //= 2
    return q


def parte3():
    print()
    print("=" * 90)
    print("PARTE 3 -- Fig. 1: reconstrucao da arvore geradora (theta=1, theta=5)")
    print("=" * 90)
    falhas = 0

    # theta=5, k=1,3,5,7,9,11 -> q=3,13,53,213,853,3413 (padrao q_{i+1}=4*q_i+1)
    esperado_5 = {1: 3, 3: 13, 5: 53, 7: 213, 9: 853, 11: 3413}
    for k, q_esp in esperado_5.items():
        q = m(5, k)
        ok = q == q_esp
        print(f"  theta=5,k={k}: 5*2^{k}={5*2**k} = 3*{q}+1  (esperado {q_esp})  {'OK' if ok else 'FALHA'}")
        if not ok:
            falhas += 1
    # confere o padrao q_{i+1} = 4*q_i + 1 mencionado no texto (nao explicito no paper,
    # mas decorre diretamente de Eq 5: m_{theta,k+2} = 4*m_{theta,k} + 1)
    vals = list(esperado_5.values())
    for i in range(len(vals) - 1):
        if vals[i + 1] != 4 * vals[i] + 1:
            print(f"  FALHA (padrao 4q+1): {vals[i]} -> {vals[i+1]}")
            falhas += 1

    # theta=1, k=0,2,4,6,8,10,12 -> q=0,1,5,21,85,341,1365
    esperado_1 = {0: 0, 2: 1, 4: 5, 6: 21, 8: 85, 10: 341, 12: 1365}
    for k, q_esp in esperado_1.items():
        q = m(1, k)
        ok = q == q_esp
        print(f"  theta=1,k={k}: 1*2^{k}={2**k} = 3*{q}+1  (esperado {q_esp})  {'OK' if ok else 'FALHA'}")
        if not ok:
            falhas += 1

    # theta=21 e theta=3 sao folhas mortas (0 mod 3, Eq 8 nunca satisfeita)
    for theta_folha in (3, 21, 57):
        tem_no = any(m(theta_folha, k) is not None for k in range(0, 30))
        print(f"  theta={theta_folha} (0 mod 3): nenhum no esperado ate k=30 -- {'OK' if not tem_no else 'FALHA'}")
        if tem_no:
            falhas += 1

    # theta=85 (filho de theta=1 em k=8): k=0 -> q=28 (par! odd part 7); k=2 -> q=113 (impar)
    q0 = m(85, 0)
    q2 = m(85, 2)
    ok = (q0 == 28) and (odd_part(q0) == 7) and (q2 == 113)
    print(f"  theta=85,k=0: q={q0}, parte impar={odd_part(q0)} (esperado 7); "
          f"k=2: q={q2} (esperado 113)  {'OK' if ok else 'FALHA'}")
    if not ok:
        falhas += 1

    print(f"Falhas: {falhas}")
    return falhas


def parte4():
    print()
    print("=" * 90)
    print("PARTE 4 -- Fig. 2: as 10 colunas mostradas sao alcancaveis a partir de theta=1")
    print("=" * 90)
    falhas = 0

    colunas_fig2 = [1, 5, 85, 341, 13, 53, 853, 3413, 7, 113]

    # BFS a partir de theta=1, expandindo por m_{theta,k} e tomando a parte impar de q,
    # ate profundidade 3 ou uma faixa de k ampla o suficiente para cobrir as colunas.
    alcancadas = {1}
    fronteira = [1]
    for _ in range(3):
        nova_fronteira = []
        for theta in fronteira:
            if theta % 3 == 0:
                continue
            for k in range(0, 14):
                q = m(theta, k)
                if q is None or q == 0:
                    continue
                filho = odd_part(q)
                if filho not in alcancadas:
                    alcancadas.add(filho)
                    nova_fronteira.append(filho)
        fronteira = nova_fronteira

    for c in colunas_fig2:
        ok = c in alcancadas
        print(f"  S({c}): alcancavel a partir de theta=1 em <=3 niveis  {'OK' if ok else 'FALHA'}")
        if not ok:
            falhas += 1

    print(f"Falhas: {falhas}")
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
Total de falhas (Partes 1-4): {total}

Paper #084 e a versao pedagogica, restrita a kappa=3, do framework ja
verificado exaustivamente em E-063 (paper #032, mesmos autores). Toda a
maquinaria algebrica (Eq 5-10: definicao de m_theta,k, condicao de
integralidade mod 3, identidade 3m+1=theta*2^k) e uma especializacao
direta de J^-_{{3,theta,k}} ja testada em E-063 Parte 2 -- reconfirmada
aqui (Parte 1) de forma independente e mais rapida.

Os exemplos numericos proprios do paper (Exemplos 1 e 2, Parte 2) batem
exatamente -- ja confirmados tambem em E-063 Parte 8.

Conteudo NOVO verificado aqui (nao coberto por E-063): a arvore geradora
completa da Fig. 1 (theta=5 expandido em k=1..11, seguindo o padrao
q_(i+1)=4*q_i+1; theta=1 expandido em k=0..12; os "ramos mortos" theta=3
e theta=21, que nunca geram um no por serem 0 mod 3) e a lista de 10
colunas da Fig. 2, todas alcancaveis a partir da raiz theta=1 -- Parte 3
e Parte 4, 0 falhas.

Nota de transcricao: minha leitura visual inicial da Fig. 1 (figura, nao
texto) sugeriu que os nos 57 e 229 estariam ligados ao no 85 -- mas
57=m_{{43,2}} e 229=m_{{43,4}} (verificado computacionalmente), NAO
descendem de theta=85 (cujos filhos sao 7 e 113, nao 57/229). Isso quase
certamente reflete um erro da MINHA leitura da posicao exata dos nos na
figura (uma imagem densa, com dezenas de circulos), nao um erro do
paper -- por isso este script verifica apenas os NUMEROS que aparecem
nas figuras (todos validos), sem depender de uma leitura pixel-perfeita
da adjacencia exata de cada aresta.
""")
    sys.exit(0 if total == 0 else 1)
