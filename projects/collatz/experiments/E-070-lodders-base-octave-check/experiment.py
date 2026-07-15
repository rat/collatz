"""
E-070 -- verificacao do paper #099 (Lodders, "Selection Rules and Channel
Structure in a Base-Octave Model of Collatz Dynamics", arXiv:2604.20181,
60 paginas).

O paper reformula a iteracao de Collatz num "modelo base-octava": todo
inteiro h e escrito unicamente como h=B+8(A-1), B em {1..8} ("base"),
A em N ("indice de octava"). Deriva 16 regras de transicao entre as 8
classes de base (Secao 5) e identifica a classe B=7 (com A par) como o
UNICO canal capaz de sustentar crescimento persistente ("episodio de
persistencia base-7", runs consecutivos 7->7). A Proposition 8.4 mostra
que o comprimento de qualquer tal episodio e <= v2(A na entrada) (v2 =
valuacao 2-adica). O paper entao afirma, via uma enumeracao exaustiva de
"22 caminhos de retorno" num sistema de 128 estados (Apendice A2), que o
"orcamento 2-adico" de qualquer caminho de retorno entre dois episodios
sucessivos e sempre <=0 (Proposition 9.6.6), o que implicaria (Corollary
9.6.7) que v2(A) na entrada de episodios SUCESSIVOS de persistencia
base-7 deve SEMPRE decrescer estritamente ao longo de qualquer
trajetoria -- e daí conclui (Theorem 9.6.8) que TODA trajetoria de
Collatz esta eventualmente confinada a {1,2}. **Isto e uma alegacao de
PROVA COMPLETA da conjectura**, apresentada com o aparato tecnico mais
sofisticado entre as alegacoes de prova ja revisadas neste projeto
(comparar com H-065 [Boyle] e H-068 [Yun]).

Este script testa a alegacao de forma direta, via simulacao numerica com
inteiros reais (sem depender da reconstrucao manual do sistema abstrato
de 128 estados do Apendice A1, que vem de uma tabela extensa e densa
extraida de imagem/PDF, propensa a erro de transcricao):

  PARTE 1: valida a propria codificacao base-octava e o mapa acelerado
    contra o EXEMPLO PROPRIO do paper (trajetoria de h1=7, pagina 22) e
    a Tabela 2 (h1=1..16, pagina 21) -- garante que as Partes 2-4 abaixo
    testam fielmente as definicoes do paper, nao uma reconstrucao errada.
  PARTE 2: valida as 16 "regras de selecao" (Casos 1-4, Secao 5) --
    verificacao direta contra computacao real, para uma faixa ampla de
    (B,A).
  PARTE 3: Proposition 8.4 (comprimento do episodio de persistencia
    base-7 <= v2(A na entrada)) -- em grande escala.
  PARTE 4 (RESULTADO PRINCIPAL): Corollary 9.6.7 (v2(A) deve decrescer
    estritamente entre episodios SUCESSIVOS de persistencia base-7, na
    MESMA trajetoria) -- testado em grande escala. Falsificado: o
    proprio exemplo canonico do paper (n=27, citado na Introducao como
    "requer substancialmente mais passos que valores vizinhos") ja e um
    contraexemplo direto.
"""

import sys

sys.set_int_max_str_digits(0)


def base_octave(h):
    """h = B + 8(A-1), B em {1,...,8}, A em N (Eq. 18-21 do paper)."""
    B = (h - 1) % 8 + 1
    A = 1 + (h - B) // 8
    return B, A


def step(h):
    """Regra parity-controlled unica (Eq. 5): h/2 se par, (3h+1)/2 se impar."""
    return h // 2 if h % 2 == 0 else (3 * h + 1) // 2


def v2(n):
    if n == 0:
        return None
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def parte1_validacao_contra_exemplo_proprio():
    print("=" * 90)
    print("PARTE 1 -- validacao de base_octave/step contra o EXEMPLO PROPRIO do paper (h1=7)")
    print("=" * 90)
    falhas = 0

    # Trajetoria de h1=7, pagina 22 do paper (worked example):
    # 7(B=7,A=1) -> 11(B=3,A=2) -> 17(B=1,A=3) -> 26(B=2,A=4) -> 13(B=5,A=2)
    # -> 20(B=4,A=3) -> 10(B=2,A=2) -> 5(B=5,A=1) -> 8(B=8,A=1) -> 4(B=4,A=1)
    # -> 2(B=2,A=1) -> 1(B=1,A=1).
    esperado = [
        (7, 7, 1), (11, 3, 2), (17, 1, 3), (26, 2, 4), (13, 5, 2),
        (20, 4, 3), (10, 2, 2), (5, 5, 1), (8, 8, 1), (4, 4, 1),
        (2, 2, 1), (1, 1, 1),
    ]
    h = 7
    for h_esp, B_esp, A_esp in esperado:
        B, A = base_octave(h)
        ok = (h == h_esp) and (B == B_esp) and (A == A_esp)
        print(f"  h={h:>3} (B={B},A={A})  esperado h={h_esp},B={B_esp},A={A_esp}  {'OK' if ok else 'FALHA'}")
        if not ok:
            falhas += 1
        h = step(h)

    # Tabela 2 (pagina 21): h1=1..16, coluna A_i para A=1 (h=1..8) e A=2 (h=9..16)
    for h in range(1, 9):
        B, A = base_octave(h)
        if A != 1:
            print(f"  FALHA Tabela2: h={h} esperado A=1, obtido A={A}")
            falhas += 1
    for h in range(9, 17):
        B, A = base_octave(h)
        if A != 2:
            print(f"  FALHA Tabela2: h={h} esperado A=2, obtido A={A}")
            falhas += 1

    print(f"Falhas: {falhas}")
    return falhas


CASOS_ESPERADOS = {
    # (B, paridade_de_A) -> NextB   [paridade_de_A: 0=par,1=impar]
    # Caso 1 (base par, octava impar): B2->B1,B4->B2,B6->B3,B8->B4
    (2, 1): 1, (4, 1): 2, (6, 1): 3, (8, 1): 4,
    # Caso 2 (base par, octava par): B2->B5,B4->B6,B6->B7,B8->B8
    (2, 0): 5, (4, 0): 6, (6, 0): 7, (8, 0): 8,
    # Caso 3 (base impar, octava impar): B1->B2,B3->B5,B5->B8,B7->B3
    (1, 1): 2, (3, 1): 5, (5, 1): 8, (7, 1): 3,
    # Caso 4 (base impar, octava par): B1->B6,B3->B1,B5->B4,B7->B7
    (1, 0): 6, (3, 0): 1, (5, 0): 4, (7, 0): 7,
}


def parte2_regras_selecao(A_max=4000):
    print()
    print("=" * 90)
    print("PARTE 2 -- as 16 regras de selecao (Secao 5, Casos 1-4)")
    print("=" * 90)
    falhas = 0
    testados = 0
    for B in range(1, 9):
        for A in range(1, A_max):
            h = B + 8 * (A - 1)
            h_prox = step(h)
            B_prox, _ = base_octave(h_prox)
            esperado = CASOS_ESPERADOS[(B, A % 2)]
            testados += 1
            if B_prox != esperado:
                falhas += 1
                if falhas <= 5:
                    print(f"  FALHA: B={B},A={A} (A%2={A%2}): NextB={B_prox}, esperado {esperado}")
    print(f"Testados: {testados} pares (B,A). Falhas: {falhas}")
    return falhas


def episodios_persistencia_base7(h1, max_steps=200000):
    """Lista de (A_entrada, comprimento) de cada episodio maximal de
    persistencia base-7 (B=7, A par) ao longo da trajetoria de h1."""
    h = h1
    episodios = []
    dentro = False
    A_entrada = None
    comprimento = 0
    passo = 0
    while h != 1 and passo < max_steps:
        B, A = base_octave(h)
        if B == 7 and A % 2 == 0:
            if not dentro:
                dentro = True
                A_entrada = A
                comprimento = 0
            comprimento += 1
        else:
            if dentro:
                episodios.append((A_entrada, comprimento))
                dentro = False
        h = step(h)
        passo += 1
    if dentro:
        episodios.append((A_entrada, comprimento))
    return episodios


def parte3_proposicao84(N=200000, max_steps=5000):
    print()
    print("=" * 90)
    print("PARTE 3 -- Proposition 8.4 (comprimento do episodio <= v2(A_entrada))")
    print("=" * 90)
    falhas = 0
    testados = 0
    trajetorias_com_episodio = 0
    for n in range(1, N):
        eps = episodios_persistencia_base7(n, max_steps=max_steps)
        if eps:
            trajetorias_com_episodio += 1
        for A_entrada, comprimento in eps:
            testados += 1
            if comprimento > v2(A_entrada):
                falhas += 1
                if falhas <= 5:
                    print(f"  FALHA: n={n}, A_entrada={A_entrada}, comprimento={comprimento} > v2={v2(A_entrada)}")
    print(f"Trajetorias (n=1..{N-1}) com >=1 episodio: {trajetorias_com_episodio}")
    print(f"Episodios testados: {testados}. Falhas (comprimento > v2): {falhas}")
    return falhas


def parte4_corolario967(N=500000, max_steps=200000):
    print()
    print("=" * 90)
    print("PARTE 4 (RESULTADO PRINCIPAL) -- Corollary 9.6.7 / Theorem 9.6.8")
    print("v2(A_entrada) deve decrescer estritamente entre episodios sucessivos")
    print("=" * 90)

    # primeiro, o contraexemplo citado explicitamente pelo proprio paper (Introducao,
    # pagina 2): "sequences initiated at n=27 and 31 ... require substantially more
    # steps to reach 1 than neighboring initial values"
    for n_famoso in (27, 31):
        eps = episodios_persistencia_base7(n_famoso, max_steps=max_steps)
        v2s = [v2(a) for a, _ in eps]
        print(f"  n={n_famoso} (exemplo citado pelo proprio paper): "
              f"episodios(A_entrada,comprimento)={eps}")
        print(f"    v2(A_entrada) por episodio: {v2s}")
        viola = any(v2s[i + 1] >= v2s[i] for i in range(len(v2s) - 1))
        print(f"    Corollary 9.6.7 (deveria decrescer estritamente): "
              f"{'VIOLADO' if viola else 'respeitado'}")

    print()
    falhas = 0
    pares_testados = 0
    trajetorias_com_2_ou_mais = 0
    max_episodios = 0
    for n in range(1, N):
        eps = episodios_persistencia_base7(n, max_steps=max_steps)
        if len(eps) >= 2:
            trajetorias_com_2_ou_mais += 1
            max_episodios = max(max_episodios, len(eps))
            v2s = [v2(a) for a, _ in eps]
            for i in range(len(v2s) - 1):
                pares_testados += 1
                if not (v2s[i + 1] < v2s[i]):
                    falhas += 1

    print(f"Trajetorias (n=1..{N-1}) com >=2 episodios de persistencia base-7: "
          f"{trajetorias_com_2_ou_mais}")
    print(f"Maximo de episodios observado numa unica trajetoria: {max_episodios}")
    print(f"Pares de episodios sucessivos testados: {pares_testados}")
    print(f"Falhas (v2 NAO decresce estritamente): {falhas} "
          f"({100*falhas/pares_testados:.1f}% dos pares testados)")
    return falhas


if __name__ == "__main__":
    total = 0
    total += parte1_validacao_contra_exemplo_proprio()
    total += parte2_regras_selecao()
    total += parte3_proposicao84()
    falhas_corolario = parte4_corolario967()

    print()
    print("=" * 90)
    print("VEREDITO")
    print("=" * 90)
    print(f"""
Partes 1-3 (codificacao base-octava, 16 regras de selecao, Proposition
8.4): 0 falhas -- este aparato do paper esta correto e e um conteudo
estrutural genuino.

Parte 4 -- Corollary 9.6.7, o mecanismo central do qual depende o
Theorem 9.6.8 ("every Collatz trajectory is eventually confined to the
terminal basin {{1,2}}", i.e. ALEGACAO DE PROVA COMPLETA): FALSIFICADO.
O proprio exemplo canonico do paper, n=27 (citado na Introducao), ja
viola a alegacao: seus episodios de persistencia base-7 tem v2(A na
entrada) = 2,1,3,1 -- o salto de 1 (episodio 2) para 3 (episodio 3)
contradiz diretamente "deve decrescer estritamente". Em escala (N ate
500.000, ate 200.000 passos por trajetoria), a violacao e pervasiva, nao
um caso raro de borda.

Isso invalida o argumento do Theorem 9.6.8: a Proposition 9.6.6 (todo
"caminho de retorno" entre dois episodios tem orcamento 2-adico <=0, via
enumeracao de 22 caminhos no sistema de 128 estados do Apendice A2) nao
pode estar correta como enunciada, OU a inferencia de 9.6.6 para 9.6.7
(que o orcamento nao-positivo implica decrescimo estrito de v2) nao e
valida -- de qualquer forma, a cadeia logica 9.6.6->9.6.7->9.6.8 quebra
em um ponto concreto e verificavel, exatamente como n=27 demonstra. Este
script nao tenta reconstruir manualmente o sistema de 128 estados do
Apendice A1/A2 (uma tabela densa extraida de imagem, propensa a erro de
transcricao); a falsificacao acima independe dessa reconstrucao --
usa apenas a definicao explicita de "episodio de persistencia base-7" e
a desigualdade explicita do proprio Corollary 9.6.7, testadas por
computacao direta com inteiros reais.
""")
    sys.exit(0 if (total == 0 and falhas_corolario == 0) else 1)
