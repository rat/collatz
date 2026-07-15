#!/usr/bin/env python3
"""
E-061 -- H-061: verificacao do paper #029 (Alic, "Collatz Progressions
Reframed: Exponent Representation, Algorithmic Hierarchies, and Record
Computations", IEEE Access, peer-reviewed). Diferente de todos os
papers revisados ate aqui nesta colecao: nao faz NENHUMA alegacao
matematica sobre a conjectura (o proprio paper diz explicitamente "The
Collatz conjecture remains unproven"). E um paper de ENGENHARIA/
ALGORITMOS: propoe representar inteiros como vetores de expoentes de
potencias de 2 (P2ER: n = soma de 2^k_i, k estritamente decrescente --
literalmente as posicoes dos bits 1 na representacao binaria de n),
mostra que a etapa impar (3n+1) vira uma operacao algebrica simples
sobre o vetor de expoentes (Eq. 2/3), e que a etapa par (/2) fica
"gratis" (so desloca todos os expoentes por uma subtracao, sem
iterar). Compara 5 algoritmos construidos sobre essa representacao e
faz uma "computacao recorde" (2^{1.024.001}-1, a progressao de Collatz
mais longa ja computada, 13.8 milhoes de passos, 7.3-9.44h).

ESCOPO desta revisao: como nao ha alegacao matematica para verificar
(nenhum teorema sobre Collatz, so um teorema de representacao/algebra),
o que importa verificar e se a ALGEBRA central (Eq. 2/3: a etapa impar
como "concat + consolidate" sobre o vetor de expoentes) realmente
reproduz o mapa de Collatz de verdade -- se estiver certa, os
benchmarks de performance sao sobre a coisa certa; se estiver errada,
tudo mais no paper mede outra coisa. A "computacao recorde" em si
(2^1.024.001, 13.8 milhoes de passos) e computacionalmente inviavel de
reproduzir nesta sessao (o proprio paper levou horas numa maquina
dedicada) -- NAO reproduzida, tratada como nao verificada.

PARTE 1: verifica a algebra do passo IMPAR (Eq. 2/3: concat + consolidate
via carry binario) contra o calculo direto 3n+1, para muitos n aleatorios
grandes, muitos passos cada.
PARTE 2: verifica a algebra do passo PAR (deslocamento por min(k)) contra
divisao direta repetida por 2.
PARTE 3: reproduz o exemplo numerico do paper (Figura 1, n=15): a
sequencia decimal completa 15->46->23->...->1, e os vetores de expoente
especificos mostrados para os 2 primeiros passos (15->[3,2,1,0]->
consolidate->[5,3,2,1]=46->desloca(min=1)->23).
PARTE 4: verifica os dois exemplos numericos extras do texto (pag. 5):
"waiting line" k=[8,5,3,2,1,0] e "end-gap" k=[15,8,4,0].
"""

import sys

sys.set_int_max_str_digits(0)


def to_kvector(n):
    """Converte n para seu vetor de expoentes (posicoes dos bits 1,
    ordem decrescente) -- a codificacao P2ER."""
    k = []
    p = 0
    while n > 0:
        if n & 1:
            k.append(p)
        n >>= 1
        p += 1
    return sorted(k, reverse=True)


def from_kvector(k):
    """Decodifica um vetor de expoentes de volta para inteiro."""
    return sum(1 << e for e in k)


def consolidate(histogram):
    """Recebe um dict {expoente: multiplicidade} e propaga carries
    binarios (varredura linear unica, low->high, carregando o excesso
    para a proxima posicao) ate sobrar no maximo 1 em cada posicao --
    exatamente a soma binaria com vai-um. Retorna o k-vector resultante
    (lista ordenada decrescente). O(faixa de expoentes), nao O(n^2)."""
    if not histogram:
        return []
    e = min(histogram.keys())
    max_e = max(histogram.keys())
    result = []
    carry = 0
    while e <= max_e or carry > 0:
        c = histogram.get(e, 0) + carry
        if c & 1:
            result.append(e)
        carry = c >> 1
        e += 1
    return sorted(result, reverse=True)


def odd_step_p2er(k):
    """Eq. 2/3 do paper: k_novo = consolidate(concat(k+1, k, [k(end)])).
    Precondicao: n=from_kvector(k) e impar, ou seja k(end)==0."""
    assert k[-1] == 0, "odd_step_p2er exige n impar (k(end)==0)"
    hist = {}
    for e in k:
        hist[e + 1] = hist.get(e + 1, 0) + 1  # k+1 (representa 2n)
    for e in k:
        hist[e] = hist.get(e, 0) + 1  # k (representa n)
    hist[k[-1]] = hist.get(k[-1], 0) + 1  # k(end)=0 (representa +1)
    return consolidate(hist)


def even_step_p2er(k):
    """Divisao por 2 ate ficar impar: desloca TODOS os expoentes por
    min(k) numa unica operacao O(|k|), sem iterar bit a bit."""
    m = k[-1]  # menor expoente = numero de divisoes por 2 necessarias
    return [e - m for e in k], m


def parte1(trials=500, steps_per_trial=40, seed=1):
    print("=" * 90)
    print("PARTE 1: algebra do passo IMPAR (Eq. 2/3, concat+consolidate) vs. 3n+1 direto")
    print("=" * 90)
    import random
    random.seed(seed)
    falhas = testados = 0
    for _ in range(trials):
        n = random.getrandbits(random.randint(10, 4000))
        if n == 0:
            continue
        if n % 2 == 0:
            n += 1  # garante impar para o primeiro passo
        k = to_kvector(n)
        for _ in range(steps_per_trial):
            if n % 2 == 0:
                break
            testados += 1
            n_direto = 3 * n + 1
            k_p2er = odd_step_p2er(k)
            n_p2er = from_kvector(k_p2er)
            if n_p2er != n_direto:
                falhas += 1
                print(f"  FALHA: n={n}: 3n+1 direto={n_direto}, P2ER={n_p2er}")
                break
            n = n_direto
            k = k_p2er
            # aplica a parte par tambem para preparar o proximo passo impar
            if n % 2 == 0:
                k, _ = even_step_p2er(k)
                n = from_kvector(k)
    print(f"{testados} passos impares testados (via {trials} trajetorias aleatorias, "
          f"n de ate 4000 bits), {falhas} falhas.")
    return falhas


def parte2(trials=500, seed=2):
    print()
    print("=" * 90)
    print("PARTE 2: algebra do passo PAR (deslocamento por min(k)) vs. divisao repetida por 2")
    print("=" * 90)
    import random
    random.seed(seed)
    falhas = testados = 0
    for _ in range(trials):
        n = random.getrandbits(random.randint(10, 2000))
        if n == 0:
            continue
        n *= (1 << random.randint(1, 20))  # garante par, com varias divisoes possiveis
        k = to_kvector(n)
        testados += 1
        n_direto = n
        while n_direto % 2 == 0:
            n_direto //= 2
        k_p2er, _ = even_step_p2er(k)
        n_p2er = from_kvector(k_p2er)
        if n_p2er != n_direto:
            falhas += 1
            print(f"  FALHA: n={n}: direto={n_direto}, P2ER={n_p2er}")
    print(f"{testados} casos testados, {falhas} falhas.")
    return falhas


def parte3():
    print()
    print("=" * 90)
    print("PARTE 3: exemplo numerico do paper (Figura 1, n=15)")
    print("=" * 90)
    n = 15
    k = to_kvector(n)
    print(f"n=15 -> k-vector = {k} (esperado pelo paper: [3, 2, 1, 0])")
    assert k == [3, 2, 1, 0]

    k_odd = odd_step_p2er(k)
    val_odd = from_kvector(k_odd)
    print(f"Passo impar (3n+1): k_novo={k_odd}, valor={val_odd} "
          f"(esperado: [5,3,2,1]=46)")

    k_even, divs = even_step_p2er(k_odd)
    val_even = from_kvector(k_even)
    print(f"Passo par (/2 ate impar): k_novo={k_even}, valor={val_even}, "
          f"divisoes={divs} (esperado: [4,2,1,0]=23, 1 divisao)")

    # reproduz a sequencia decimal completa 15->46->23->...->1 (Collatz padrao)
    seq = [15]
    x = 15
    while x != 1:
        x = x // 2 if x % 2 == 0 else 3 * x + 1
        seq.append(x)
    esperado = [15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    print(f"\nSequencia completa (Collatz padrao): {seq}")
    print(f"Esperado pelo texto (17 passos, valores intermediarios): {esperado}")
    print(f"Bate: {seq == esperado}")

    up_steps = sum(1 for i in range(len(seq) - 1) if seq[i] % 2 == 1)
    print(f"\nNumero de passos IMPARES ('UP'): {up_steps} (paper diz 5)")
    print(f"Total de passos (stopping time padrao): {len(seq) - 1} (paper diz 17)")
    return k != [3, 2, 1, 0] or val_odd != 46 or val_even != 23 or seq != esperado


def parte4():
    print()
    print("=" * 90)
    print("PARTE 4: exemplos de 'waiting line' e 'end-gap' (pag. 5 do paper)")
    print("=" * 90)
    k_wl = [8, 5, 3, 2, 1, 0]
    n_wl = from_kvector(k_wl)
    print(f"Waiting-line k={k_wl} representa n={n_wl}")
    deltas = [k_wl[i] - k_wl[i + 1] for i in range(len(k_wl) - 1)]
    print(f"Diferencas consecutivas Delta={deltas} (paper diz waiting-line de "
          f"comprimento 3 no final, Delta=[1,1,1]): {'bate' if deltas[-3:] == [1, 1, 1] else 'DIVERGE'}")

    k_eg = [15, 8, 4, 0]
    n_eg = from_kvector(k_eg)
    print(f"\nEnd-gap k={k_eg} representa n={n_eg}")
    gap = k_eg[-2] - k_eg[-1]
    print(f"Gap entre os 2 ultimos elementos (4 e 0): {gap} (paper diz end-gap de tamanho 4): "
          f"{'bate' if gap == 4 else 'DIVERGE'}")


if __name__ == "__main__":
    falhas = 0
    falhas += parte1()
    falhas += parte2()
    falhas += parte3()
    parte4()

    print()
    print("=" * 90)
    print("VEREDITO")
    print("=" * 90)
    print(f"""
Total de falhas (Partes 1-3): {falhas}

A algebra central do paper (P2ER: representar n como vetor de
expoentes de potencias de 2, com o passo impar 3n+1 implementado como
concatenacao de multiset + consolidacao via carry binario, Eq. 2/3, e
o passo par como deslocamento em bloco pelo menor expoente) reproduz
EXATAMENTE o mapa de Collatz padrao, verificado em centenas de
trajetorias aleatorias (n de ate 4000 bits) e no exemplo numerico
especifico do proprio paper (Figura 1, n=15). Isso da confianca de que
os benchmarks de performance do paper (comparando PASA/REN/UPX/ACCEL/
POW2BASIC) estao de fato medindo implementacoes corretas do mapa de
Collatz, nao um mapa diferente por engano de representacao.

NAO verificado (fora de escopo, computacionalmente inviavel nesta
sessao): a "computacao recorde" em si (2^{{1.024.001}}-1, 13.8 milhoes
de passos, que o proprio paper levou 7.3-9.44h numa maquina dedicada
para computar) -- nao reproduzida, tratada como nao verificada, nao
como confirmada.

O paper nao faz nenhuma alegacao sobre a Conjectura de Collatz em si
(o texto e explicito: "The Collatz conjecture remains unproven") --
e um paper de representacao/algoritmos, com contribuicao numerica
apenas no sentido de recorde de COMPUTACAO (progressao mais longa ja
executada), nao de descoberta matematica.
""")
