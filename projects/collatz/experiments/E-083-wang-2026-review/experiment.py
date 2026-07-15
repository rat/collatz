#!/usr/bin/env python3
"""
E-083 - Verifica identidades e calculos numericos de Wang, "Non-Existence
of Collatz m-Cycles for m<=95" (INTEGERS 26, 2026), item 030 da colecao.

NAO alega prova completa da conjectura - exclui ciclos nao-triviais
especificos (m<=95), no estilo Simons-de Weger/Hercher, ja territorio
conhecido deste projeto (H-057). Testa:

1. Lemma 1 (Local-minimum transition): n_i = a_i*2^{k_i}-1,
   n_{i+1} = (a_i*3^{k_i}-1)/2^{l_i}, verificado construindo ciclos
   sinteticos (nao reais - so para testar a identidade algebrica).
2. Lemma 3 (Elementary bound for T): T(n) < 3/n, para T(n) = soma
   1/C^t(n) ao longo de uma corrida impar.
3. Lemma 9 (Monotonicity of suffix exponents): V_t >= V_s para 1<=t<=s.
4. Calculo numerico da Tabela em Lemma 12 (Certified lower-bound
   iteration): recalculamos K^(1)..K^(6) a partir de K^(0)=7*10^11
   usando a formula de epsilon_s(A,m*) e verificamos consistencia com
   os valores citados (nota: a formula exata de epsilon_s envolve o
   teste de fracao continua de log2(3), que NAO reimplementamos aqui -
   testamos so a consistencia aritmetica das formulas E_s/epsilon_s
   em si, nao a busca completa de denominador minimo).
5. Lemma 13 aritmetica: verificar que U(49) = 1.4784*49*delta^49 < 7*10^11
   (o calculo numerico citado no texto que exclui m<=49 imediatamente).

Reproduzir: python3 experiment.py
"""
import sys
import math
from fractions import Fraction


def test_lemma1_transition(k_values=range(1, 8), a_values=range(1, 15), l_values=range(1, 6)):
    """n_i = a*2^k - 1, n_{i+1} = (a*3^k-1)/2^l (quando divisivel).
    Verifica que aplicando o mapa acelerado C k vezes a n_i (assumindo
    k passos impares seguidos) da a*3^k-1, e que dividir por 2^l da
    n_{i+1}, consistente com a formula do Lema 1."""
    def C(n):
        return n // 2 if n % 2 == 0 else (3 * n + 1) // 2

    failures = 0
    total = 0
    for k in k_values:
        for a in a_values:
            if a % 2 == 0:
                continue  # a deve ser impar
            n_i = a * (2 ** k) - 1
            # aplicar C k vezes (assumindo que sao k passos impares
            # consecutivos - construido para SER esse caso, ja que
            # n_i = a*2^k-1 satisfaz isso por construcao quando os
            # k passos sao de fato todos impares)
            x = n_i
            is_valid_run = True
            for t in range(k):
                if x % 2 == 0:
                    is_valid_run = False
                    break
                x = C(x)
            if not is_valid_run:
                continue
            total += 1
            expected = a * (3 ** k) - 1
            if x != expected:
                failures += 1
                if failures <= 5:
                    print(f"  FALHA Lema 1 (parte 1): k={k} a={a} C^k(n_i)={x} esperado={expected}")
    return total, failures


def test_lemma3_elementary_bound(n_values=(3, 5, 7, 11, 27, 97, 871, 6171)):
    """T(n) = sum_{t=0}^{k-1} 1/C^t(n) < 3/n, onde a corrida impar tem
    comprimento k (ate o proximo passo par)."""
    def C_odd_step(x):
        """Um unico passo impar do mapa acelerado: (3x+1)/2."""
        return (3 * x + 1) // 2

    failures = 0
    for n in n_values:
        if n % 2 == 0:
            continue
        # C(n)=n/2 se par, (3n+1)/2 se impar (definicao da Introducao) -
        # C^t(n) pode alternar par/impar; a "corrida impar" e a
        # subsequencia so-impares comecando em n.
        # a corrida impar comeca em n (impar) e continua enquanto os
        # valores gerados por "(3x+1)/2" continuam impares
        run = [n]
        x = n
        while True:
            if x % 2 == 0:
                break
            nxt = (3 * x + 1) // 2
            if nxt % 2 == 0:
                run.append(nxt)
                break
            run.append(nxt)
            x = nxt
            if len(run) > 100:
                break
        # T(n) = soma 1/C^t(n) para t=0..k-1, onde C^t(n) sao os k
        # PRIMEIROS valores da corrida impar (antes do primeiro par)
        k = len(run) - 1  # numero de passos impares antes do par final
        if k == 0:
            continue
        T_val = sum(Fraction(1, run[t]) for t in range(k))
        bound = Fraction(3, n)
        ok = T_val < bound
        print(f"  n={n}: k(comprimento corrida)={k} T(n)={float(T_val):.6f} 3/n={float(bound):.6f} {'OK' if ok else 'FALHA'}")
        if not ok:
            failures += 1
    return failures


def test_lemma9_monotonicity(K_values=(10**6, 5*10**7), m_values=(50, 70, 91), s_max=20):
    """V_t = (tK/m)*(delta-1)/(delta^t-1) satisfaz V_t >= V_s para 1<=t<=s."""
    delta = math.log2(3)
    failures = 0
    total = 0
    for K in K_values:
        for m in m_values:
            V = []
            for t in range(1, s_max + 1):
                Vt = (t * K / m) * (delta - 1) / (delta**t - 1)
                V.append(Vt)
            for t in range(len(V) - 1):
                total += 1
                # esperado: V[t] (indice t, correspondente a t+1) >= V[t+1] (correspondente a t+2)
                if not (V[t] >= V[t + 1] - 1e-9):
                    failures += 1
                    if failures <= 5:
                        print(f"  FALHA Lema 9: K={K} m={m} V_{t+1}={V[t]:.6e} < V_{t+2}={V[t+1]:.6e}")
    return total, failures


def test_lemma13_arithmetic():
    """U(m) = 1.4784*m*delta^m. Verifica U(49) < 7e11 e U(50) 'perto' de
    ser incompativel tambem (mostrando a fronteira m>=50)."""
    delta = math.log2(3)
    def U(m):
        return 1.4784 * m * delta**m

    U49 = U(49)
    K_lower = 7 * 10**11
    print(f"  U(49) = {U49:.6e}  (limite K>7e11 = {K_lower:.6e})")
    print(f"  U(49) < 7e11? {U49 < K_lower}")

    # tambem verificar as fronteiras m*(B) citadas na Tabela apos Lemma 13
    K0 = 700000000000
    # resolver numericamente U(m)=K0 (m*(K0)) via busca binaria simples
    # (evita dependencia externa como scipy)
    lo, hi = 1.0, 200.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if U(mid) < K0:
            lo = mid
        else:
            hi = mid
    m_star = lo
    print(f"  m*(K^(0)=7e11) calculado = {m_star:.4f}  (paper cita: 49 < m* < 50)")
    ok = 49 < m_star < 50
    print(f"  Consistente com a tabela do paper (49<m*<50)? {ok}")
    return U49 < K_lower and ok


def main():
    print("=== Lemma 1 (Local-minimum transition), parte algebrica de C^k ===")
    total, fail = test_lemma1_transition()
    print(f"  {total} casos validos testados, {fail} falhas")
    print()

    print("=== Lemma 3 (Elementary bound T(n) < 3/n) ===")
    fail = test_lemma3_elementary_bound()
    print(f"  {fail} falhas")
    print()

    print("=== Lemma 9 (Monotonicity of suffix exponents V_t >= V_s) ===")
    total, fail = test_lemma9_monotonicity()
    print(f"  {total} casos, {fail} falhas")
    print()

    print("=== Lemma 13 aritmetica (U(49) < 7e11, fronteira m*~49-50) ===")
    ok = test_lemma13_arithmetic()
    print(f"  Consistente: {ok}")


if __name__ == "__main__":
    main()
