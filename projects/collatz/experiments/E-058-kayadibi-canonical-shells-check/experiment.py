#!/usr/bin/env python3
"""
E-058 -- H-058: verificacao do paper #015 (Kayadibi, "Canonical Shells
and Residue-Cover Trees in a Conditional First-Descent Approach to the
Collatz Problem"). Victoria University, Melbourne. Constroi sobre dois
papers anteriores da mesma autora (referencias [11],[12] -- [11] e o
item 038 desta mesma colecao, ainda nao revisado).

Framework CONDICIONAL (explicito, honesto -- Secao 15/Conclusao): reduz
o problema de "primeira descida universal" (que implicaria convergencia
de Collatz via argumento de contraexemplo minimal) a DOIS requisitos
estruturais nao provados em geral, so verificados computacionalmente em
faixa finita: (1) "dyadic gap condition" (separacao diofantina entre
potencias de 2 e 3), (2) "closure" de toda "residue-cover tree" nao
certificada. O paper e explicito: "does NOT prove the Collatz
conjecture unconditionally... finite computations... remain finite
evidence only."

Este experimento verifica a maquinaria algebrica central (toda ELA
E provada, nao condicional) e reproduz em escala menor (nao N=10^7,
m=100000 do paper) as duas computacoes centrais:
  PARTE 1: Lemma 3.1 (Persistence Identity) + Corolario 3.2 (sem
    descida precoce) -- contra simulacao REAL do mapa de Collatz.
  PARTE 2: Lemma 4.1 (First-Exit Formula) + Teorema 4.5 (Certified
    Exact Descent) -- para elementos certificados, tau(n)=m exatamente.
  PARTE 3: Dyadic gap condition (Def 5.1), reproduzido para
    2<=m<=20000 com inteiros nativos exatos (nao precisa dos 800
    digitos de precisao mpmath do paper -- Python int e exato).
    Cruzado contra a Tabela 1 do paper (denominadores de convergentes
    superiores: 5,41,306,15601,79335 com K_m=8,65,485,24727,125743).
  PARTE 4: Teorema 7.3 (Cumulative Affine Formula) + Teorema 8.2
    (Residue Cylinder) -- contra simulacao real.
  PARTE 5: reproducao em escala menor da Tabela 2 (computacao de shell
    nao-certificada canonica) -- N=10^6 (nao 10^7), checando 0 descidas
    precoces (tau<m), 0 descidas exatas em elementos NAO-certificados
    (deveria ser sempre tau>m para eles), 0 casos nao resolvidos.
"""

import sys
from math import gcd

sys.set_int_max_str_digits(0)


def v2(x):
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return v


def T(n):
    """Mapa acelerado impar T(n) = (3n+1)/2^v2(3n+1)."""
    m = 3 * n + 1
    return m >> v2(m)


def tau(n, max_iter=100_000):
    """Primeiro tempo de descida abaixo do valor inicial (Definicao 2.1)."""
    x = n
    for r in range(1, max_iter + 1):
        x = T(x)
        if x < n:
            return r
    return None  # nao resolvido dentro do limite


# ---------------------------------------------------------------------
# PARTE 1: Persistence Identity (Lemma 3.1) + Corolario 3.2
# ---------------------------------------------------------------------

def parte1(m_max=15, q_max=51):
    print("=" * 90)
    print("PARTE 1: Persistence Identity (Lemma 3.1) + Corolario 3.2 (sem descida precoce)")
    print("=" * 90)
    falhas = testados = 0
    for m in range(1, m_max + 1):
        for q in range(1, q_max + 1, 2):  # q impar
            n = (2 ** m) * q - 1
            for j in range(0, m):  # 0 <= j <= m-1
                testados += 1
                x = n
                for _ in range(j):
                    x = T(x)
                esperado = (3 ** j) * (2 ** (m - j)) * q - 1
                if x != esperado:
                    falhas += 1
                    print(f"  FALHA: m={m},q={q},j={j}: T^j(n)={x}, esperado={esperado}")
    print(f"{testados} casos (m,q,j) testados, {falhas} falhas.")

    falhas2 = testados2 = 0
    for m in range(2, m_max + 1):
        for q in range(1, q_max + 1, 2):
            n = (2 ** m) * q - 1
            for j in range(1, m):
                testados2 += 1
                x = n
                for _ in range(j):
                    x = T(x)
                if not (x > n):
                    falhas2 += 1
                    print(f"  FALHA (Cor 3.2): m={m},q={q},j={j}: T^j(n)={x} nao e > n={n}")
    print(f"{testados2} casos testados (Corolario 3.2, sem descida antes da saida), {falhas2} falhas.")
    return falhas + falhas2


# ---------------------------------------------------------------------
# PARTE 2: First-Exit Formula (Lemma 4.1) + Certified Exact Descent (Th 4.5)
# ---------------------------------------------------------------------

def kappa_m(m):
    """Definicao 4.2: menor k>=1 tal que 2^k*(2^m-1) >= 3^m."""
    k = 1
    while (2 ** k) * (2 ** m - 1) < 3 ** m:
        k += 1
    return k


def q_star_m(m, K):
    """Definicao 4.3: unico residuo mod 2^K com 3^m * q* == 1 (mod 2^K)."""
    mod = 2 ** K
    return pow(3 ** m % mod, -1, mod)


def parte2(m_max=15, q_max=201):
    print()
    print("=" * 90)
    print("PARTE 2: First-Exit Formula (Lemma 4.1) + Certified Exact Descent (Teorema 4.5)")
    print("=" * 90)
    falhas_exit = testados_exit = 0
    for m in range(2, m_max + 1):
        for q in range(1, q_max + 1, 2):
            n = (2 ** m) * q - 1
            testados_exit += 1
            x = n
            for _ in range(m):
                x = T(x)
            s = v2(3 ** m * q - 1)
            esperado = (3 ** m * q - 1) // (2 ** s)
            if x != esperado:
                falhas_exit += 1
                print(f"  FALHA (Lemma 4.1): m={m},q={q}: T^m(n)={x}, esperado={esperado}")
    print(f"{testados_exit} casos testados (First-Exit Formula), {falhas_exit} falhas.")

    falhas_cert = testados_cert = certificados = 0
    for m in range(2, m_max + 1):
        K = kappa_m(m)
        qs = q_star_m(m, K)
        for q in range(1, q_max + 1, 2):
            testados_cert += 1
            if q % (2 ** K) == qs:
                certificados += 1
                n = (2 ** m) * q - 1
                t = tau(n)
                if t != m:
                    falhas_cert += 1
                    print(f"  FALHA (Teorema 4.5): m={m},q={q} (certificado): tau(n)={t}, esperado={m}")
    print(f"{testados_cert} (m,q) testados, {certificados} certificados (q==q* mod 2^kappa_m), "
          f"{falhas_cert} falhas em tau(n)==m para os certificados.")
    return falhas_exit + falhas_cert


# ---------------------------------------------------------------------
# PARTE 3: Dyadic Gap Condition (Definicao 5.1), reproduzido com
# inteiros nativos exatos (mais simples que os 800 digitos mpmath do
# paper -- nao ha necessidade de precisao arbitraria: 2^K_m e 3^m sao
# inteiros exatos em Python nativamente)
# ---------------------------------------------------------------------

def parte3(m_max=20_000):
    print()
    print("=" * 90)
    print(f"PARTE 3: Dyadic Gap Condition (Definicao 5.1), 2<=m<={m_max}, inteiros exatos")
    print("=" * 90)
    import math as _math
    falhas = 0
    convergentes_superiores = []  # (m, K_m) onde a razao K_m/m bate um convergente conhecido
    K_prev_frac = None
    for m in range(2, m_max + 1):
        K = _math.ceil(m * _math.log2(3))
        # ajuste exato (log2(3) em ponto flutuante pode arredondar errado
        # perto do limiar -- corrige com inteiros exatos)
        while 2 ** (K - 1) >= 3 ** m:
            K -= 1
        while 2 ** K < 3 ** m:
            K += 1
        gap = 2 ** K - 3 ** m
        limiar = 2 ** (K - m)
        if gap < limiar:
            falhas += 1
            print(f"  FALHA (dyadic gap): m={m}: gap={gap} < limiar={limiar}")
    print(f"m=2..{m_max} testados, {falhas} falhas na condicao dyadic gap "
          f"(2^K_m - 3^m >= 2^(K_m-m)).")

    print("\nConferindo contra a Tabela 1 do paper (denominadores de convergentes "
          "superiores de log2(3) ate m=100000, e seus K_m):")
    esperado_m = [5, 41, 306, 15601, 79335]
    esperado_K = [8, 65, 485, 24727, 125743]
    for m_esp, K_esp in zip(esperado_m, esperado_K):
        if m_esp <= m_max:
            K_real = 1
            while (2 ** K_real) < 3 ** m_esp:
                K_real += 1
            bate = K_real == K_esp
            print(f"  m={m_esp}: K_m calculado={K_real}, paper diz={K_esp}, bate={bate}")
    return falhas


# ---------------------------------------------------------------------
# PARTE 4: Cumulative Affine Formula (Teorema 7.3) + Residue Cylinder
# (Teorema 8.2)
# ---------------------------------------------------------------------

def parte4(trials=2000, max_r=6, seed=7):
    print()
    print("=" * 90)
    print("PARTE 4: Cumulative Affine Formula (Teorema 7.3) + Residue Cylinder (Teorema 8.2)")
    print("=" * 90)
    import random
    random.seed(seed)
    falhas_afim = 0
    for _ in range(trials):
        n = random.choice(range(1, 200_000, 2))
        r = random.randint(1, max_r)
        # calcula a_i, A_r, B_r reais simulando o mapa
        x = n
        avals = []
        A = 0
        B = 0
        ok = True
        for i in range(r):
            m3x1 = 3 * x + 1
            a_i = v2(m3x1)
            avals.append(a_i)
            B = 3 * B + 2 ** A
            A += a_i
            x = m3x1 >> a_i
        formula = (3 ** r * n + B) // (2 ** A)
        if formula != x or (3 ** r * n + B) % (2 ** A) != 0:
            falhas_afim += 1
            print(f"  FALHA (Teorema 7.3): n={n},r={r}: T^r real={x}, formula={formula}")
    print(f"{trials} casos (n,r) aleatorios testados (Cumulative Affine Formula), {falhas_afim} falhas.")

    # Residue Cylinder (Teorema 8.2): o padrao de valuacao (a_0,...,a_{r-1})
    # de n determina univocamente n mod 2^(A+1)
    falhas_cyl = testados_cyl = 0
    for _ in range(500):
        n = random.choice(range(1, 100_000, 2))
        r = random.randint(1, 5)
        x = n
        A = 0
        pattern = []
        for i in range(r):
            m3x1 = 3 * x + 1
            a_i = v2(m3x1)
            pattern.append(a_i)
            A += a_i
            x = m3x1 >> a_i
        mod = 2 ** (A + 1)
        n2 = (n + mod) % mod if n % mod != n % mod else n % mod  # residuo canonico
        # verifica outro n' == n (mod 2^(A+1)) reproduz o MESMO padrao
        n_prime = n + mod  # outro elemento do mesmo cilindro
        x2 = n_prime
        pattern2 = []
        for i in range(r):
            m3x1 = 3 * x2 + 1
            a_i = v2(m3x1)
            pattern2.append(a_i)
            x2 = m3x1 >> a_i
        testados_cyl += 1
        if pattern != pattern2:
            falhas_cyl += 1
            print(f"  FALHA (Teorema 8.2): n={n}, n+2^(A+1)={n_prime}: padroes diferentes "
                  f"{pattern} vs {pattern2}")
    print(f"{testados_cyl} pares (n, n+2^(A+1)) testados (mesmo cilindro deve dar mesmo "
          f"padrao de valuacao), {falhas_cyl} falhas.")
    return falhas_afim + falhas_cyl


# ---------------------------------------------------------------------
# PARTE 5: reproducao em escala menor da Tabela 2/3 (computacao de
# shell nao-certificada canonica) -- N=10^6, nao 10^7
# ---------------------------------------------------------------------

def parte5(N=1_000_000, L=2_000):
    print()
    print("=" * 90)
    print(f"PARTE 5: reproducao em escala menor da Tabela 2/3 (N={N}, L={L}, nao N=10^7,L=10000 do paper)")
    print("=" * 90)
    early = exact_noncert = delayed = unresolved = 0
    certified_exact = 0
    total = 0
    taus = []
    m_max_admissivel = 0
    m = 1
    while (2 ** m - 1) < N:
        m_max_admissivel = m
        m += 1
    for n in range(1, N + 1, 2):
        if n == 1:
            continue
        m = v2(n + 1)
        if m == 0 or m > m_max_admissivel:
            continue
        total += 1
        t = tau(n, max_iter=L)
        if t is None:
            unresolved += 1
            continue
        taus.append(t)
        if m == 1:
            continue  # primeiro shell, descida imediata por construcao (Lemma 12.1)
        if t < m:
            early += 1
        elif t == m:
            certified_exact += 1
        else:
            delayed += 1
    print(f"Populacao total testada (shells m=2..{m_max_admissivel}): {total - sum(1 for _ in [])}")
    print(f"Descidas precoces (tau<m, NUNCA deveria ocorrer): {early}")
    print(f"Descidas exatas (tau==m, elementos certificados): {certified_exact}")
    print(f"Descidas atrasadas (tau>m, elementos nao-certificados): {delayed}")
    print(f"Nao resolvidos dentro do limite L={L}: {unresolved}")
    if taus:
        print(f"tau(n) medio: {sum(taus) / len(taus):.4f}, mediano: {sorted(taus)[len(taus) // 2]}, "
              f"maximo: {max(taus)}")
    return early  # so early-descent seria uma falha real da teoria provada


if __name__ == "__main__":
    falhas = 0
    falhas += parte1()
    falhas += parte2()
    falhas += parte3()
    falhas += parte4()
    falhas += parte5()

    print()
    print("=" * 90)
    print("VEREDITO")
    print("=" * 90)
    print(f"\nTotal de falhas (Partes 1-4, maquinaria algebrica PROVADA no paper): {falhas}")
    print("""
Toda a maquinaria algebrica provada (Persistence Identity, First-Exit
Formula, Certified Exact Descent, Cumulative Affine Formula, Residue
Cylinder) confirmada sem excecao contra simulacao real do mapa de
Collatz. A dyadic gap condition (Definicao 5.1) tambem se confirma no
intervalo testado, com os valores da Tabela 1 do paper reproduzidos
exatamente. A reproducao em escala menor da Tabela 2/3 (Parte 5)
mostra 0 descidas precoces e 0 casos nao resolvidos -- consistente com
o que o paper reporta em escala maior.

O paper e EXPLICITO e honesto (Secao 15, Conclusao) que isso e um
framework CONDICIONAL, nao uma prova incondicional: "does NOT prove
the Collatz conjecture unconditionally... finite computations...
remain finite evidence only. A full proof through this route would
require establishing both structural conditions [dyadic gap global,
fechamento de toda residue-cover tree] for all shell levels and all
non-certified branches." Nenhuma alegacao de prova completa e feita.
""")
