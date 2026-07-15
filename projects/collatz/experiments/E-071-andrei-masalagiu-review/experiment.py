#!/usr/bin/env python3
"""
E-071 - Verifica os resultados centrais de Andrei & Masalagiu, "About the
Collatz conjecture" (Acta Informatica 35, 167-179, 1998), item 101 da
colecao.

Testa:
1. Teorema 3.1: f^(2p)(2^p*r + 2^p - 1) = 3^p*r + 3^p - 1, para todo p,r.
2. Lema 4.1: f^(2t+3)((2^(2t+2)-1)/3) = 1, para todo t>=0 (familia
   explicita de numeros para os quais a conjectura vale, caso p=1 do
   Teorema 4.2).
3. Teorema 4.2 (caso geral): f^(3^m*n+2m+2)((2^(m+1)*(2^(3^m*n)+1)-1)/3^(m+1))=1
   para n em {6t+1, 6t+5}.
4. Teorema 3.2: Racc(n) = niv(n)/pas(n) (razao de aceleracao) satisfaz
   1.5 <= Racc(n) <= i para 2^i<=n<2^(i+1), i>=2.
5. Conjectura 2 (nao provada pelo paper - so verificar numericamente a
   tendencia): media de Racc sobre uma faixa [2^n, 2^(n+1)) tende a 3
   quando n cresce.

Reproduzir: python3 experiment.py
"""
import sys


def f(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1


def f_iter(n, k):
    for _ in range(k):
        n = f(n)
    return n


def steps_to_1(n):
    """k tal que f^(k)(n)=1 (nao definido se n=1: retorna 0)."""
    if n == 1:
        return 0
    k = 0
    while n != 1:
        n = f(n)
        k += 1
        if k > 10_000_000:
            raise RuntimeError(f"não convergiu para n original")
    return k


def test_theorem_3_1(max_p=8, max_r=50):
    """f^(2p)(2^p*r + 2^p - 1) = 3^p*r + 3^p - 1"""
    failures = 0
    total = 0
    for p in range(0, max_p + 1):
        for r in range(0, max_r + 1):
            n0 = 2**p * r + 2**p - 1
            if n0 < 1:
                continue
            total += 1
            lhs = f_iter(n0, 2 * p)
            rhs = 3**p * r + 3**p - 1
            if lhs != rhs:
                failures += 1
                if failures <= 5:
                    print(f"  FALHA Teo 3.1: p={p} r={r} n0={n0} lhs={lhs} rhs={rhs}")
    return total, failures


def test_lemma_4_1(max_t=20):
    """f^(2t+3)((2^(2t+2)-1)/3) = 1"""
    failures = 0
    total = 0
    for t in range(0, max_t + 1):
        n0 = (2**(2 * t + 2) - 1) // 3
        assert (2**(2 * t + 2) - 1) % 3 == 0, f"não divisível, t={t}"
        total += 1
        k = 2 * t + 3
        result = f_iter(n0, k)
        if result != 1:
            failures += 1
            print(f"  FALHA Lema 4.1: t={t} n0={n0} k={k} f^k(n0)={result}")
    return total, failures


def test_theorem_4_2(max_m=4, max_t=10):
    """f^(3^m*n+2m+2)( 2^(m+1)*((2^(3^m*n)+1)/3^(m+1)) - 1 ) = 1
    para n em {6t+1, 6t+5 : t>=0}. IMPORTANTE: a divisao por 3^(m+1) e
    interna (so sobre 2^(3^m*n)+1, garantida exata por Teorema 4.1c do
    proprio paper), e so depois multiplica por 2^(m+1) e subtrai 1 -
    NAO e (2^(m+1)*(...)-1)/3^(m+1) como num parenteses malposto."""
    failures = 0
    total = 0
    for m in range(0, max_m + 1):
        for t in range(0, max_t + 1):
            for n in (6 * t + 1, 6 * t + 5):
                inner = 2**(3**m * n) + 1
                denom = 3**(m + 1)
                if inner % denom != 0:
                    failures += 1
                    print(f"  FALHA Teo 4.2 (Teo 4.1c falhou, nao divisivel): m={m} n={n} inner={inner} denom={denom}")
                    continue
                n0 = 2**(m + 1) * (inner // denom) - 1
                k = 3**m * n + 2 * m + 2
                total += 1
                result = f_iter(n0, k)
                if result != 1:
                    failures += 1
                    print(f"  FALHA Teo 4.2: m={m} n={n} n0={n0} k={k} f^k(n0)={result}")
    return total, failures


def racc(n):
    """Razao de aceleracao Racc(n) = niv(n)/pas(n).
    niv(n) = numero de passos do Algoritmo 1 (= steps_to_1 padrao).
    pas(n) = numero de passos do Algoritmo 2 (2 passos "3n+1,/2" contam
    como 1 "pas" cada vez que se aplica a regra composta do Teorema 3.1;
    na pratica, para n>1, pas(n) e o numero de ciclos do while1 externo).
    Reimplementamos via a definicao operacional do Algoritmo 2 (Fig. paper):
    a cada iteracao do laco externo, ou aplica-se o Teorema 3.1 (quando m
    e da forma 2^p*r+2^p-1) ou apenas uma divisao/multiplicacao (caso base).
    """
    # niv(n): passos padrao (Algoritmo 1)
    niv = steps_to_1(n)
    # pas(n): reimplementacao literal do Algoritmo 2 do paper.
    m = n
    pas = 0
    while m > 1:
        pas += 1
        k = 2
        k2 = 1
        modul = 1
        niv_local = 0
        while m % k == modul:
            k *= 2
            niv_local += 2
            modul = k - 1
            k2 *= 3
        while m % k == 0:
            k *= 2
            niv_local += 1
            k2 *= 3
        k = k // 2
        p = m // k
        p1 = k2 * p + k2 - 1
        if m % k != 0:
            m = p1
        else:
            m = p
    return niv, pas


def test_theorem_3_2(n_max=100_000):
    """Racc(n) >= 1.5 para n>2; Racc(n) <= i para 2^i<=n<2^(i+1), i>=2."""
    failures_lower = 0
    failures_upper = 0
    total = 0
    n = 3
    while n <= n_max:
        niv, pas = racc(n)
        r = niv / pas
        total += 1
        if n > 2 and r < 1.5 - 1e-9:
            failures_lower += 1
            if failures_lower <= 5:
                print(f"  FALHA Teo 3.2 (limite inferior): n={n} Racc={r:.4f}")
        # i = floor(log2(n))
        i = n.bit_length() - 1
        if i >= 2 and r > i + 1e-9:
            failures_upper += 1
            if failures_upper <= 5:
                print(f"  FALHA Teo 3.2 (limite superior): n={n} i={i} Racc={r:.4f}")
        n += 1
    return total, failures_lower, failures_upper


def test_conjecture_2(max_power=16):
    """Pmed(n) = media de Racc sobre [2^n, 2^(n+1)) -> conjectura diz tende a 3."""
    print("  n   Pmed(n)")
    for n in range(1, max_power + 1):
        lo, hi = 2**n, 2**(n + 1)
        total = 0.0
        count = 0
        for k in range(lo, hi):
            niv, pas = racc(k)
            total += niv / pas
            count += 1
        pmed = total / count
        print(f"  {n:2d}  {pmed:.6f}")


def main():
    print("=== Teorema 3.1: f^(2p)(2^p*r+2^p-1) = 3^p*r+3^p-1 ===")
    total, fail = test_theorem_3_1()
    print(f"  {total} casos testados, {fail} falhas")
    print()

    print("=== Lema 4.1: f^(2t+3)((2^(2t+2)-1)/3) = 1 ===")
    total, fail = test_lemma_4_1()
    print(f"  {total} casos testados, {fail} falhas")
    print()

    print("=== Teorema 4.2: familia geral f^(...)=1 para n em {6t+1,6t+5} ===")
    total, fail = test_theorem_4_2()
    print(f"  {total} casos testados, {fail} falhas")
    print()

    print("=== Teorema 3.2: 1.5 <= Racc(n) <= i (para 2^i<=n<2^(i+1)) ===")
    total, fail_lo, fail_hi = test_theorem_3_2()
    print(f"  {total} casos testados, {fail_lo} falhas limite inferior, {fail_hi} falhas limite superior")
    print()

    print("=== Conjectura 2 (nao provada): Pmed(n) -> 3 quando n->infinito ===")
    test_conjecture_2()


if __name__ == "__main__":
    main()
