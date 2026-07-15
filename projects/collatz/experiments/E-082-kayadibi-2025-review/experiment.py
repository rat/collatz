#!/usr/bin/env python3
"""
E-082 - Verifica as identidades algebricas centrais de Kayadibi, "Exact
and Delayed Descent in Accelerated Odd Collatz Spines with AAS-Based
Metamorphic Separation" (Victoria University, 2026), item 025 da
colecao. NAO alega prova (o proprio texto diz explicitamente: "The
results do not prove the Collatz conjecture" e tem um "Remark 4.5
(Local Scope)" explicito).

Testa:
1. Lemma 3.1 (Spine Persistence Identity): T^j(n) = 3^j*2^(m-j)*q - 1
   para n=2^m*q-1, 0<=j<=m-1, e consequentemente T^j(n)>n para 1<=j<=m-1.
2. Lemma 3.2 (Spine Exit Formula): T^m(n) = (3^m*q-1)/2^s, s=v2(3^m*q-1).
3. Corollary 3.3 (Pre-Descent Lower Bound): tau(n)>=m se tau(n) existe.
4. Theorem 4.1 (Valuation Threshold): v2(3^m*q-1)>=kappa_m => tau(n)=m.
5. Lemma 5.4 (Shift Valuation Lemma): para q=q*_m+a mod 2^kappa_m,
   1<=a<2^kappa_m, tem-se v2(3^m*q-1)=v2(a).
6. Estatisticas empiricas citadas (Secao final): E_bar=6.7360,
   median(E)=4, max(E)=153, para N=10^7, m=2..23 (reproduzimos em
   escala menor, ja que N=10^7 e caro, mas confirmamos consistencia
   qualitativa e a formula E(n)=tau(n)-m).

Reproduzir: python3 experiment.py
"""
import sys
import math


def T(n):
    """Mapa acelerado T(n) = (3n+1)/2^v2(3n+1)."""
    x = 3 * n + 1
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return x


def v2(x):
    if x == 0:
        return float("inf")
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return v


def first_descent_time(n, max_steps=10000):
    """tau(n) = min{r>=1 : T^r(n) < n}."""
    x = n
    for r in range(1, max_steps + 1):
        x = T(x)
        if x < n:
            return r
    return None


def test_lemma_3_1(m_values=range(2, 15), q_values=range(1, 30)):
    """T^j(n) = 3^j*2^(m-j)*q - 1, para n=2^m*q-1, 0<=j<=m-1."""
    failures = 0
    total = 0
    for m in m_values:
        for q in q_values:
            n = 2**m * q - 1
            x = n
            for j in range(0, m):
                total += 1
                expected = 3**j * 2**(m - j) * q - 1
                if x != expected:
                    failures += 1
                    if failures <= 5:
                        print(f"  FALHA Lema 3.1: m={m} q={q} j={j} x={x} esperado={expected}")
                if j < m - 1:
                    x = T(x)
    return total, failures


def test_spine_exit_formula(m_values=range(2, 15), q_values=range(1, 30)):
    """T^m(n) = (3^m*q-1)/2^s, s=v2(3^m*q-1)."""
    failures = 0
    total = 0
    for m in m_values:
        for q in q_values:
            n = 2**m * q - 1
            x = n
            for _ in range(m):
                x = T(x)
            s = v2(3**m * q - 1)
            expected = (3**m * q - 1) // (2**s)
            total += 1
            if x != expected:
                failures += 1
                if failures <= 5:
                    print(f"  FALHA Formula de saida: m={m} q={q} T^m(n)={x} esperado={expected}")
    return total, failures


def test_valuation_threshold(m_values=range(2, 12), q_values=range(1, 200)):
    """Theorem 4.1: v2(3^m*q-1)>=kappa_m => tau(n)=m."""
    failures = 0
    total = 0
    for m in m_values:
        kappa_m = math.ceil(math.log2(3**m / (2**m - 1)))
        for q in q_values:
            n = 2**m * q - 1
            s = v2(3**m * q - 1)
            if s >= kappa_m:
                total += 1
                tau_n = first_descent_time(n)
                if tau_n != m:
                    failures += 1
                    if failures <= 5:
                        print(f"  FALHA Teo 4.1: m={m} q={q} n={n} s={s} kappa_m={kappa_m} tau(n)={tau_n} esperado={m}")
    return total, failures


def test_shift_valuation_lemma(m_values=range(2, 12), n_shifts_per_m=50):
    """Lemma 5.4: q=q*_m+a mod 2^kappa_m, 1<=a<2^kappa_m => v2(3^m*q-1)=v2(a)."""
    failures = 0
    total = 0
    for m in m_values:
        kappa_m = math.ceil(math.log2(3**m / (2**m - 1)))
        mod = 2**kappa_m
        q_star = pow(3**m, -1, mod)
        for a in range(1, min(n_shifts_per_m, mod)):
            q = (q_star + a) % mod
            if q == 0:
                q = mod
            total += 1
            lhs = v2(3**m * q - 1)
            rhs = v2(a)
            if lhs != rhs:
                failures += 1
                if failures <= 5:
                    print(f"  FALHA Lema 5.4: m={m} a={a} q={q} v2(3^m*q-1)={lhs} v2(a)={rhs}")
    return total, failures


def test_empirical_stats(m_values=range(2, 16), n_max=200_000):
    """Reproduz as estatisticas empiricas (E_bar, median, max) numa
    escala menor que N=10^7 do paper, verificando consistencia
    qualitativa (nao os valores exatos, que dependem de N=10^7)."""
    excesses = []
    for m in m_values:
        q = 1
        while True:
            n = 2**m * q - 1
            if n > n_max:
                break
            tau_n = first_descent_time(n)
            if tau_n is not None:
                e = tau_n - m
                excesses.append(e)
            q += 1
    if not excesses:
        return None
    excesses.sort()
    mean_e = sum(excesses) / len(excesses)
    median_e = excesses[len(excesses) // 2]
    max_e = max(excesses)
    all_nonneg = all(e >= 0 for e in excesses)
    print(f"  N_max={n_max}, m=2..{max(m_values)}: {len(excesses)} casos")
    print(f"  E_bar={mean_e:.4f}  median(E)={median_e}  max(E)={max_e}")
    print(f"  (paper, N=10^7, m=2..23: E_bar=6.7360 median=4 max=153)")
    print(f"  Todos os E(n)>=0 (consistente com Corollary 3.3, tau(n)>=m): {all_nonneg}")
    return all_nonneg


def main():
    print("=== Lemma 3.1 (Spine Persistence Identity) ===")
    total, fail = test_lemma_3_1()
    print(f"  {total} casos, {fail} falhas")
    print()

    print("=== Lemma 3.2 (Spine Exit Formula) ===")
    total, fail = test_spine_exit_formula()
    print(f"  {total} casos, {fail} falhas")
    print()

    print("=== Theorem 4.1 (Valuation Threshold => tau(n)=m exato) ===")
    total, fail = test_valuation_threshold()
    print(f"  {total} casos certificados testados, {fail} falhas")
    print()

    print("=== Lemma 5.4 (Shift Valuation Lemma) ===")
    total, fail = test_shift_valuation_lemma()
    print(f"  {total} casos, {fail} falhas")
    print()

    print("=== Estatisticas empiricas (reproducao em escala menor) ===")
    test_empirical_stats()


if __name__ == "__main__":
    main()
