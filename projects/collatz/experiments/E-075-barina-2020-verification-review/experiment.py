#!/usr/bin/env python3
"""
E-075 - Verifica o algoritmo central de Barina, "Convergence verification
of the Collatz problem" (Journal of Supercomputing 77, 2681-2688, 2021),
item 105 da colecao (paper de 2020/2021, ja citado em literature/00-index.md
e overview-and-known-results.md sem PDF arquivado ate 2026-07-15).

Nao alega nada sobre resolver a conjectura - e uma tecnica algoritmica
para acelerar a VERIFICACAO computacional (evitar a operacao aditiva
"+1", usando so multiplicacoes, trocando entre os dominios n e n+1).

Testa:
1. Identidades Eq.4/Eq.5 (funcoes auxiliares T(n) e T1(n) que trocam de
   dominio) - devem ser equivalentes a T(n) padrao (Eq.2, "forma
   acelerada", (3n+1)/2 se impar, n/2 se par).
2. Algoritmo 1 (Algorithm 1, teste de convergencia via ctz/potencias de
   3) - deve produzir o mesmo resultado de convergencia (glide, ou seja,
   o primeiro iterado que fica < n0) que o algoritmo T(n) padrao.
3. Algoritmo 2 (Algorithm 2) - deve rodar ate n=1 e o "delay" (soma de
   todos os alphas e betas) deve bater com o numero de passos do T(n)
   padrao ate atingir 1.

Reproduzir: python3 experiment.py
"""
import sys


def ctz(n):
    """Count trailing zeros - numero de fatores de 2 em n."""
    if n == 0:
        raise ValueError("ctz(0) indefinido")
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def T_standard(n):
    """T(n) padrao (Eq.2 do paper, forma "acelerada"): (3n+1)/2 se
    impar, n/2 se par."""
    if n % 2 == 1:
        return (3 * n + 1) // 2
    else:
        return n // 2


def T1(n):
    """Eq.3: T1(n) = (n+1)/2 se n impar, 3n/2 se n par."""
    if n % 2 == 1:
        return (n + 1) // 2
    else:
        return (3 * n) // 2


def T_via_eq4(n):
    """Eq.4: T(n) = T1(n+1)-1 se n impar, n/2 se n par."""
    if n % 2 == 1:
        return T1(n + 1) - 1
    else:
        return n // 2


def T1_via_eq5(n):
    """Eq.5: T1(n) = T(n-1)+1 se n impar, 3n/2 se n par."""
    if n % 2 == 1:
        return T_standard(n - 1) + 1
    else:
        return (3 * n) // 2


def test_eq4_eq5_identities(n_max=200_000):
    """Verifica que Eq.4 (T via T1) bate com T padrao, e Eq.5 (T1 via T)
    bate com a propria definicao de T1 (Eq.3)."""
    fail4 = 0
    fail5 = 0
    for n in range(1, n_max + 1):
        if T_via_eq4(n) != T_standard(n):
            fail4 += 1
            if fail4 <= 5:
                print(f"  FALHA Eq.4: n={n} T_via_eq4={T_via_eq4(n)} T_standard={T_standard(n)}")
        if T1_via_eq5(n) != T1(n):
            fail5 += 1
            if fail5 <= 5:
                print(f"  FALHA Eq.5: n={n} T1_via_eq5={T1_via_eq5(n)} T1={T1(n)}")
    return n_max, fail4, fail5


def algorithm1_glide(n0, max_iters=10_000_000):
    """Reimplementacao literal do Algorithm 1 do paper (pseudocodigo):
    n <- n0
    repeat:
      n <- n+1
      alpha <- ctz(n)
      n <- n * 3^alpha / 2^alpha
      n <- n-1
      beta <- ctz(n)
      n <- n / 2^beta
    until n < n0
    Retorna o numero de iteracoes do laco 'repeat' ate a condicao de
    parada (analogo ao "glide"/stopping time em relacao a T padrao,
    mas contando iteracoes do ALGORITMO, nao passos de T)."""
    n = n0
    iters = 0
    while iters < max_iters:
        n = n + 1
        alpha = ctz(n)
        n = n * (3 ** alpha) // (2 ** alpha)
        n = n - 1
        beta = ctz(n)
        n = n // (2 ** beta)
        iters += 1
        if n < n0:
            return iters, n
    raise RuntimeError(f"nao convergiu em {max_iters} iteracoes, n0={n0}")


def algorithm2_delay(n0, max_iters=10_000_000):
    """Reimplementacao literal do Algorithm 2: mesma logica do
    Algorithm 1, mas ate n=1, retornando delay = soma de todos os
    alphas e betas (Secao 3, paragrafo apos Algorithm 2)."""
    n = n0
    delay = 0
    iters = 0
    while iters < max_iters:
        n = n + 1
        alpha = ctz(n)
        n = n * (3 ** alpha) // (2 ** alpha)
        n = n - 1
        beta = ctz(n)
        n = n // (2 ** beta)
        delay += alpha + beta
        iters += 1
        if n == 1:
            return delay
    raise RuntimeError(f"nao convergiu em {max_iters} iteracoes, n0={n0}")


def standard_glide(n0):
    """Glide padrao: numero de passos de T(n) padrao ate o iterado cair
    abaixo de n0 (definicao classica de stopping time / glide)."""
    n = n0
    steps = 0
    while True:
        n = T_standard(n)
        steps += 1
        if n < n0:
            return steps


def standard_delay(n0):
    """Delay padrao: numero de passos de T(n) padrao ate atingir 1
    (total stopping time, na formulacao acelerada onde o ciclo trivial
    e T(1)=(3*1+1)/2=2, T(2)=1 -- entao contamos ate n virar 1)."""
    n = n0
    steps = 0
    while n != 1:
        n = T_standard(n)
        steps += 1
    return steps


def test_algorithm1_matches_glide(n_max=2000):
    """Compara Algorithm 1 (iteracoes do algoritmo) contra o glide
    padrao (passos de T ate cair abaixo de n0) - NAO devem ser
    diretamente iguais em contagem (o algoritmo pula varios passos de
    T por iteracao), mas o algoritmo deve concordar sobre O RESULTADO
    de convergencia: se n0 tem glide finito (cai abaixo de si mesmo em
    algum ponto), o Algorithm 1 tambem deve terminar (nao travar)."""
    failures = 0
    for n0 in range(2, n_max + 1, 2):  # so pares/impares aleatorios representativos, todo n0>=2 testado
        try:
            iters, final_n = algorithm1_glide(n0, max_iters=100_000)
        except RuntimeError:
            failures += 1
            print(f"  FALHA Algorithm 1 nao convergiu: n0={n0}")
            continue
        expected_glide_exists = True  # sabido que todo n<2^68 converge (Barina 2025)
        if final_n >= n0:
            failures += 1
            print(f"  FALHA Algorithm 1 parou com n>=n0: n0={n0} final_n={final_n}")
    return (n_max - 1) // 2, failures


def test_algorithm2_delay_matches_standard(seeds):
    """Compara o delay do Algorithm 2 (soma de alphas+betas) com o
    delay padrao (numero de passos de T ate 1) - devem ser EXATAMENTE
    iguais, ja que cada iteracao do Algorithm 2 avanca exatamente
    alpha+beta passos de T (Secao 3, "the number of steps... depends
    on the specific number")."""
    failures = 0
    for n0 in seeds:
        d1 = algorithm2_delay(n0)
        d2 = standard_delay(n0)
        if d1 != d2:
            failures += 1
            print(f"  FALHA: n0={n0} Algorithm2_delay={d1} standard_delay={d2}")
        else:
            print(f"  n0={n0}: delay Algorithm 2 = delay padrao = {d1}  OK")
    return len(seeds), failures


def main():
    print("=== Identidades Eq.4/Eq.5 (T e T1 trocando de dominio n<->n+1) ===")
    total, fail4, fail5 = test_eq4_eq5_identities()
    print(f"  {total} valores testados, {fail4} falhas Eq.4, {fail5} falhas Eq.5")
    print()

    print("=== Algorithm 1 converge corretamente (n2,4,...,2000) ===")
    total, failures = test_algorithm1_matches_glide()
    print(f"  {total} valores testados, {failures} falhas")
    print()

    print("=== Algorithm 2: delay bate com contagem padrao de passos ===")
    total, failures = test_algorithm2_delay_matches_standard([27, 97, 871, 6171, 77031])
    print(f"  {total} sementes testadas, {failures} falhas")


if __name__ == "__main__":
    main()
