#!/usr/bin/env python3
"""
E-076 - Verifica exemplos numericos e identidades explicitas concretas
de Tao, "Almost all orbits of the Collatz map attain almost bounded
values" (Forum of Mathematics, Pi 10:e12, 2022), item 106 da colecao -
o resultado mais forte ja estabelecido sobre a conjectura.

Nao "cacamos erros" neste paper como fizemos com preprints de baixo
rigor - e um paper revisado por pares num periodico de primeira linha,
de um dos matematicos mais renomados vivos. O objetivo aqui e apenas
verificar computacionalmente as poucas afirmacoes CONCRETAS e
numericamente checaveis que o proprio texto apresenta como exemplos,
como disciplina de verificacao (nao ceticismo).

Testa:
1. Mapa de Siracusa Syr(N) = maior fator impar de 3N+1 - exemplos
   explicitos do texto: Syr(1)=1, Syr(3)=5, Syr(5)=1, Syr(7)=11.
2. Identidade (1.2): Col_min(N) = Syr_min(N/2^v2(N)).
3. Distribuicao exata de Syrac(Z/3^nZ) para n=1,2 (Secao 1.4, apos o
   Lemma 1.12) - calculada via a formula recursiva do proprio Lemma
   1.12, e verificada contra os valores explicitos que o texto da:
   n=1: 0,1,2 mod 3 com probabilidades 0,1/3,2/3
   n=2: 0..8 mod 9 com probabilidades 0,8/63,16/63,0,11/63,4/63,0,2/63,22/63

Reproduzir: python3 experiment.py
"""
import sys
from fractions import Fraction


def collatz_map(N):
    """Col(N) = 3N+1 se N impar, N/2 se N par (Definicao 1.1 do paper)."""
    return 3 * N + 1 if N % 2 == 1 else N // 2


def v2(M):
    """2-valuacao: maior potencia de 2 que divide M."""
    if M == 0:
        return float("inf")
    a = 0
    while M % 2 == 0:
        M //= 2
        a += 1
    return a


def syracuse_map(N):
    """Syr(N) = maior fator impar de 3N+1 (definicao textual, Secao 1.2)."""
    M = 3 * N + 1
    while M % 2 == 0:
        M //= 2
    return M


def col_min(N, max_iters=1_000_000):
    """Col_min(N) = infimo da orbita de Collatz de N."""
    seen_min = N
    n = N
    for _ in range(max_iters):
        n = collatz_map(n)
        if n < seen_min:
            seen_min = n
        if n == 1:
            break
    return seen_min


def syr_min(N, max_iters=1_000_000):
    """Syr_min(N) = infimo da orbita de Siracusa de N (N deve ser impar)."""
    assert N % 2 == 1
    seen_min = N
    n = N
    for _ in range(max_iters):
        n = syracuse_map(n)
        if n < seen_min:
            seen_min = n
        if n == 1:
            break
    return seen_min


def test_syracuse_examples():
    """Syr(1)=1, Syr(3)=5, Syr(5)=1, Syr(7)=11 (texto, Secao 1.2)."""
    examples = {1: 1, 3: 5, 5: 1, 7: 11}
    failures = 0
    for N, expected in examples.items():
        got = syracuse_map(N)
        ok = got == expected
        print(f"  Syr({N}) = {got} (esperado {expected}) {'OK' if ok else 'FALHA'}")
        if not ok:
            failures += 1
    return failures


def test_identity_1_2(n_max=2000):
    """Col_min(N) = Syr_min(N / 2^v2(N)) para todo N (Eq. 1.2)."""
    failures = 0
    for N in range(1, n_max + 1):
        a = v2(N)
        odd_part = N // (2 ** a)
        lhs = col_min(N)
        rhs = syr_min(odd_part)
        if lhs != rhs:
            failures += 1
            if failures <= 5:
                print(f"  FALHA: N={N} Col_min={lhs} Syr_min(N/2^v2(N))={rhs}")
    return n_max, failures


def syrac_distribution(n, geom_p=Fraction(1, 2)):
    """Calcula a distribuicao exata de Syrac(Z/3^nZ) via Lemma 1.12
    (formula recursiva), usando aritmetica de fracoes exatas (nao ponto
    flutuante) para poder comparar exatamente com os valores do texto.

    Lemma 1.12: P(Syrac(Z/3^(n+1)Z) = x) =
        sum_{a: 1<=a<=2*3^n, 2^a*x=1 mod 3} 2^-a * P(Syrac(Z/3^nZ) = (2^a*x-1)/3)
        / (1 - 2^(-2*3^n))

    Base: Syrac(Z/3^0Z) = 0 mod 1 com probabilidade 1.
    """
    # dist[n] = dicionario {valor: Fraction(probabilidade)} para Z/3^nZ
    dist = {0: Fraction(1, 1)}  # n=0: Z/1Z, unico valor 0
    for level in range(n):
        modulus = 3 ** (level + 1)
        prev_modulus = 3 ** level
        new_dist = {x: Fraction(0) for x in range(modulus)}
        # para cada x em Z/3^(level+1)Z, soma sobre a de 1 a 2*3^level
        # tal que 2^a * x = 1 mod 3
        max_a = 2 * prev_modulus
        for x in range(modulus):
            total = Fraction(0)
            for a in range(1, max_a + 1):
                if (pow(2, a, 3) * x) % 3 == 1:
                    # (2^a * x - 1) / 3, reduzido mod 3^level
                    val = (pow(2, a, modulus * 3) * x - 1)
                    # precisamos (2^a*x - 1)/3 como elemento de Z/3^level Z;
                    # calculamos 2^a*x - 1 exatamente (inteiro grande, a pequeno aqui)
                    full = (2 ** a) * x - 1
                    assert full % 3 == 0, f"nao divisivel: a={a} x={x} full={full}"
                    reduced = (full // 3) % prev_modulus
                    prob_prev = dist.get(reduced, Fraction(0))
                    total += Fraction(1, 2 ** a) * prob_prev
            denom = 1 - Fraction(1, 2 ** (2 * prev_modulus))
            new_dist[x] = total / denom
        dist = new_dist
    return dist


def test_syrac_distribution_n1():
    """Syrac(Z/3Z) toma valores 0,1,2 com probabilidades 0,1/3,2/3."""
    dist = syrac_distribution(1)
    expected = {0: Fraction(0), 1: Fraction(1, 3), 2: Fraction(2, 3)}
    failures = 0
    for x in range(3):
        got = dist[x]
        exp = expected[x]
        ok = got == exp
        print(f"  P(Syrac(Z/3Z)={x}) = {got} (esperado {exp}) {'OK' if ok else 'FALHA'}")
        if not ok:
            failures += 1
    total = sum(dist.values())
    print(f"  soma das probabilidades = {total} {'OK' if total == 1 else 'FALHA (nao soma 1)'}")
    return failures + (0 if total == 1 else 1)


def test_syrac_distribution_n2():
    """Syrac(Z/9Z) toma valores 0..8 mod 9 com probabilidades
    0, 8/63, 16/63, 0, 11/63, 4/63, 0, 2/63, 22/63 (texto, apos Lemma 1.12)."""
    dist = syrac_distribution(2)
    expected = [Fraction(0), Fraction(8, 63), Fraction(16, 63), Fraction(0),
                Fraction(11, 63), Fraction(4, 63), Fraction(0), Fraction(2, 63),
                Fraction(22, 63)]
    failures = 0
    for x in range(9):
        got = dist[x]
        exp = expected[x]
        ok = got == exp
        print(f"  P(Syrac(Z/9Z)={x}) = {got} (esperado {exp}) {'OK' if ok else 'FALHA'}")
        if not ok:
            failures += 1
    total = sum(dist.values())
    print(f"  soma das probabilidades = {total} {'OK' if total == 1 else 'FALHA (nao soma 1)'}")
    return failures + (0 if total == 1 else 1)


def main():
    print("=== Exemplos do mapa de Siracusa (Secao 1.2) ===")
    fail1 = test_syracuse_examples()
    print(f"  {fail1} falhas")
    print()

    print("=== Identidade (1.2): Col_min(N) = Syr_min(N/2^v2(N)) ===")
    total, fail2 = test_identity_1_2()
    print(f"  {total} valores testados (N=1..2000), {fail2} falhas")
    print()

    print("=== Distribuicao exata de Syrac(Z/3Z) (n=1, via Lemma 1.12) ===")
    fail3 = test_syrac_distribution_n1()
    print(f"  {fail3} falhas")
    print()

    print("=== Distribuicao exata de Syrac(Z/9Z) (n=2, via Lemma 1.12) ===")
    fail4 = test_syrac_distribution_n2()
    print(f"  {fail4} falhas")


if __name__ == "__main__":
    main()
