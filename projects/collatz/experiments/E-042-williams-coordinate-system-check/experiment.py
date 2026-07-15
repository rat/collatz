"""
E-042 - Verificacao independente do paper #014 (Williams, "A Coordinate
System for Collatz Dynamics", arXiv:2607.01718).

Testa os dois resultados centrais alegados como provados: Teorema 3.6
(dinamica diagonal: o mapa de Collatz envia posicao (a,b) para
(a-1,b+1) dentro de um "esqueleto") e Teorema 4.1 (linhas k=2 mod4,
k>=6, do esqueleto principal L_1 nao contem primos).

ESTENDIDO em 2026-07-15 (retomada do item 014 dentro do lote "revisar
todos os papers ja baixados"; so entao percebemos que este paper ja
tinha sido revisado aqui como H-042 -- consolidado em vez de duplicar
como H-058). Partes novas: particao bijetora (Teorema 2.13), transicao
de fronteira (Proposicao 3.10), contagem "prime-admissible" (Teorema
4.2), formula de contagem de cadeias (Proposicao 6.2), referencias OEIS
(Secao 5.2), linhas acidentalmente sem primos (Observacao 6.3).
"""
import sys
from math import gcd
from sympy import isprime

sys.set_int_max_str_digits(0)


def C(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1


def verify_theorem_3_6(trials=20_000, seed=1):
    import random
    random.seed(seed)
    ok = tested = 0
    for _ in range(trials):
        lam = random.choice([1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35])
        a = random.randint(2, 15)
        b = random.randint(0, 10)
        n = lam * (2 ** a) * (3 ** b) - 1
        tested += 1
        x = C(n)
        while x % 2 == 0:
            x = C(x)
        expected = lam * (2 ** (a - 1)) * (3 ** (b + 1)) - 1
        if x == expected:
            ok += 1
        else:
            print(f"  MISMATCH lam={lam},a={a},b={b}: obtido {x}, esperado {expected}")
    print(f"Teorema 3.6 (dinamica diagonal): {ok}/{tested} casos corretos")
    return ok == tested


def verify_theorem_4_1(k_max=300):
    print(f"Teorema 4.1 (Zero-Prime Rows), L_1 (lambda=1), k=6..{k_max}:")
    all_ok = True
    linhas = 0
    for k in range(6, k_max + 1, 4):  # k = 6,10,14,... (todos == 2 mod 4)
        linhas += 1
        row = [(2 ** a) * (3 ** (k - a)) - 1 for a in range(1, k + 1)]
        primes = [v for v in row if isprime(v)]
        if primes:
            all_ok = False
            print(f"  k={k}: CONTRAEXEMPLO, primos encontrados: {primes[:3]}")
    print(f"  {linhas} linhas testadas (k=6,10,...,{k_max}), nenhum primo encontrado em nenhuma.")
    # excecao esperada k=2
    row2 = [(2 ** a) * (3 ** (2 - a)) - 1 for a in range(1, 3)]
    print(f"  k=2 (excecao esperada pelo paper): {row2}, primos: {[isprime(v) for v in row2]}")
    # controle: k fora do padrao deveria conter primos
    print("  Controle (k fora do padrao k=2 mod4, deveria ter primos):")
    for k in [7, 8, 9, 12, 15, 16]:
        row = [(2 ** a) * (3 ** (k - a)) - 1 for a in range(1, k + 1)]
        primes = [v for v in row if isprime(v)]
        print(f"    k={k}: {len(primes)} primos de {len(row)} elementos")
    return all_ok


# ---------------------------------------------------------------------
# Coordenadas (c,k,j) <-> n, para as partes novas (Teorema 2.13 e alem)
# ---------------------------------------------------------------------

def factor_3smooth(m):
    a = 0
    while m % 2 == 0:
        m //= 2
        a += 1
    b = 0
    while m % 3 == 0:
        m //= 3
        b += 1
    return a, b, m


def coords_from_n(n):
    if n % 2 == 1:
        a, b, lam = factor_3smooth(n + 1)
        return 2 * lam - 2, a + b, 2 * b + 1
    else:
        a, b, lam = factor_3smooth(n // 2 + 1)
        return 2 * lam - 2, a + b, 2 * b


def T_c(c, k, j):
    lam = (c + 2) // 2
    g = 2 if j % 2 == 0 else 1
    if j % 2 == 0:
        R = 2 ** (k - j // 2) * 3 ** (j // 2)
    else:
        R = 2 ** (k - (j - 1) // 2) * 3 ** ((j - 1) // 2)
    return g * (lam * R - 1)


def verify_theorem_2_13_partition(N=200_000):
    print(f"Teorema 2.13 (particao bijetora Z>=0 -> crown triangles), n=0..{N}:")
    falhas = 0
    vistos = {}
    for n in range(N + 1):
        c, k, j = coords_from_n(n)
        back = T_c(c, k, j)
        if back != n or not (0 <= j <= 2 * k):
            print(f"  FALHA: n={n} -> (c={c},k={k},j={j}) -> T_c={back}")
            falhas += 1
        if (c, k, j) in vistos:
            print(f"  FALHA: posicao ({c},{k},{j}) usada por n={n} e n={vistos[(c, k, j)]}")
            falhas += 1
        vistos[(c, k, j)] = n
    print(f"  {N + 1} valores testados, {falhas} falhas (round-trip + unicidade de posicao).")
    return falhas == 0


def verify_proposition_3_10_boundary(lam_max=25, b_max=8):
    print("Proposicao 3.10 (transicao na fronteira a=1):")
    falhas = testados = 0
    for lam in range(1, lam_max + 1, 2):
        if lam % 3 == 0:
            continue
        for b in range(0, b_max + 1):
            n = 2 * lam * 3 ** b - 1  # a=1
            testados += 1
            m = 3 * n + 1
            v_real = 0
            while m % 2 == 0:
                m //= 2
                v_real += 1
            lam3b1 = lam * 3 ** (b + 1) - 1
            v_lam3b1 = 0
            t = lam3b1
            while t % 2 == 0:
                t //= 2
                v_lam3b1 += 1
            if v_real != 1 + v_lam3b1:
                falhas += 1
                print(f"  FALHA: lam={lam},b={b}: v2(3n+1)={v_real} (esperado {1 + v_lam3b1})")
    print(f"  {testados} pares (lambda,b) testados, {falhas} falhas.")
    return falhas == 0


def verify_theorem_4_2_covering(k_max=300):
    print(f"Teorema 4.2 (contagem de posicoes 'prime-admissible'), k=2..{k_max}:")
    falhas = 0
    for k in range(2, k_max + 1):
        n_admissible = 0
        for a in range(1, k + 1):
            b = k - a
            dos = (a % 2 == 0 and b % 2 == 0)
            div5 = (a % 2 == 1 and b % 2 == 1 and (a % 4) == (b % 4))
            if not dos and not div5:
                n_admissible += 1
        if k % 2 == 1:
            esperado = k
        elif k % 4 == 0:
            esperado = k // 2
        else:
            esperado = 0
        if n_admissible != esperado:
            falhas += 1
            print(f"  FALHA: k={k}: contagem={n_admissible}, esperado={esperado}")
    print(f"  k=2..{k_max} testados, {falhas} discrepancias.")
    return falhas == 0


def verify_proposition_6_2_chain_count(N=10_000_000):
    """CUIDADO: o elemento MINIMO da linha k nao e T_c(k,0) (posicao par,
    g=2) -- e T_c(k,1) (posicao impar, g=1), = lam*2^k-1. Confirmado
    contra o Exemplo 2.9 do proprio paper: linha k=2 de L_1 e
    [6,3,10,5,16], minimo real 3 (em j=1), nao 6 (em j=0). Uma primeira
    tentativa desta verificacao usou T_c(k,0) por engano e concluiu
    (incorretamente) que a Proposicao 6.2 tinha um erro de fator 2 --
    pego pelo advisor() antes de entrar em H-058/H-042; nao e erro do
    paper, era bug da verificacao."""
    print(f"Proposicao 6.2 (R_k(N) = N/(6*2^(k-1)) + O(1)), N={N}:")
    falhas = 0
    for k in range(2, 8):
        limite = (N + 1) / (2 ** k)
        contagem = sum(1 for lam in range(1, int(limite) + 2) if lam % 2 != 0 and lam % 3 != 0
                        and (lam * 2 ** k - 1) <= N)
        formula = N / (6 * 2 ** (k - 1))
        razao = contagem / formula if formula > 0 else float("nan")
        if abs(razao - 1) > 0.05:
            falhas += 1
        print(f"  k={k}: direto={contagem}, formula={formula:.1f}, razao={razao:.4f}")
    print(f"  {falhas} discrepancias (razao deveria ficar proxima de 1.0).")
    return falhas == 0


A007494_TERMS = [0, 2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 32, 33, 35, 36]
A008594_TERMS = [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204, 216]
A017557_TERMS = [3, 15, 27, 39, 51, 63, 75, 87, 99, 111, 123, 135, 147, 159, 171, 183, 195, 207, 219]  # 12n+3
A017617_TERMS = [8, 20, 32, 44, 56, 68, 80, 92, 104, 116, 128, 140, 152, 164, 176, 188, 200]  # 12n+8, correta
A005105_TERMS = [2, 3, 5, 7, 11, 17, 23, 31, 47, 53, 71, 107, 127, 191, 383, 431, 647, 863, 971, 1151]


def verify_oeis_references():
    """Termos conferidos via curl direto em oeis.org em 2026-07-15 (nao
    de memoria -- ver feedback_oeis_access_method.md)."""
    print("Referencias OEIS da Secao 5.2 (conferidas via curl em oeis.org):")
    crowns = [c for c in range(0, 50) if c % 12 == 0 or c % 12 == 8]
    ok1 = crowns == [4 * x for x in A007494_TERMS if 4 * x < 50]
    print(f"  Crowns = 4*A007494: {ok1} (citacao correta)")
    ok2 = [c for c in crowns if c % 12 == 0] == [x for x in A008594_TERMS if x < 50]
    print(f"  Crowns==0mod12 = A008594: {ok2} (citacao correta)")
    crowns_8 = [c for c in crowns if c % 12 == 8]
    erro_017557 = crowns_8 != [x for x in A017557_TERMS if x < 50]
    correta_017617 = crowns_8 == [x for x in A017617_TERMS if x < 50]
    print(f"  ACHADO: A017557 (=12n+3, ==3mod12) NAO bate com crowns==8mod12: {erro_017557}")
    print(f"          A017617 (=12n+8) e a sequencia correta: {correta_017617}")
    primos_L1 = sorted({(2 ** a) * (3 ** (k - a)) - 1
                         for k in range(1, 12) for a in range(1, k + 1)
                         if isprime((2 ** a) * (3 ** (k - a)) - 1)})
    nota_005105 = primos_L1 == A005105_TERMS[1:len(primos_L1) + 1]
    print(f"  NOTA: 'primos em L_1 = A005105' precisa: {not nota_005105} "
          f"(A005105 inclui 2 via i=0, L_1 exige a>=1 -- diferem por 1 elemento)")
    return erro_017557 and correta_017617 and not nota_005105  # True == achados confirmados como esperado


def verify_observation_6_3(k_max=300):
    print(f"Observacao 6.3 (linhas 'acidentalmente' sem primos, k<={k_max}):")
    livres_0mod4 = [k for k in range(4, k_max + 1, 4)
                    if not any(isprime((2 ** a) * (3 ** (k - a)) - 1) for a in range(1, k + 1))]
    esperado_0mod4 = [84, 100, 116, 156, 176, 184, 188, 200, 252, 284, 300]
    livres_impar = [k for k in range(3, k_max, 2)
                     if not any(isprime((2 ** a) * (3 ** (k - a)) - 1) for a in range(1, k + 1))]
    esperado_impar = [149, 165, 261]
    ok = livres_0mod4 == esperado_0mod4 and livres_impar == esperado_impar
    print(f"  k==0mod4 sem primos: {livres_0mod4} (esperado {esperado_0mod4}) -- bate: {livres_0mod4 == esperado_0mod4}")
    print(f"  k impar sem primos:  {livres_impar} (esperado {esperado_impar}) -- bate: {livres_impar == esperado_impar}")
    return ok


if __name__ == "__main__":
    ok1 = verify_theorem_3_6()
    print()
    ok2 = verify_theorem_4_1()
    print()
    ok3 = verify_theorem_2_13_partition()
    print()
    ok4 = verify_proposition_3_10_boundary()
    print()
    ok5 = verify_theorem_4_2_covering()
    print()
    ok6 = verify_proposition_6_2_chain_count()
    print()
    ok7 = verify_oeis_references()
    print()
    ok8 = verify_observation_6_3()
    print()
    print(f"Teorema 3.6: {'CONFIRMADO' if ok1 else 'FALHOU'}")
    print(f"Teorema 4.1: {'CONFIRMADO' if ok2 else 'FALHOU'}")
    print(f"Teorema 2.13: {'CONFIRMADO' if ok3 else 'FALHOU'}")
    print(f"Proposicao 3.10: {'CONFIRMADO' if ok4 else 'FALHOU'}")
    print(f"Teorema 4.2: {'CONFIRMADO' if ok5 else 'FALHOU'}")
    print(f"Proposicao 6.2: {'CONFIRMADO' if ok6 else 'FALHOU'}")
    print(f"Observacao 6.3: {'CONFIRMADO' if ok8 else 'FALHOU'}")
    print(f"Referencias OEIS Secao 5.2: 2 problemas de citacao confirmados "
          f"(A017557->A017617; A005105 impreciso por 1 elemento) -- {'OK' if ok7 else 'INESPERADO'}")
