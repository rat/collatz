"""
E-042 - Verificacao independente do paper #014 (Williams, "A Coordinate
System for Collatz Dynamics", arXiv:2607.01718).

Testa os dois resultados centrais alegados como provados: Teorema 3.6
(dinamica diagonal: o mapa de Collatz envia posicao (a,b) para
(a-1,b+1) dentro de um "esqueleto") e Teorema 4.1 (linhas k=2 mod4,
k>=6, do esqueleto principal L_1 nao contem primos).
"""
from math import gcd
from sympy import isprime


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


def verify_theorem_4_1(k_max=60):
    print("Teorema 4.1 (Zero-Prime Rows), L_1 (lambda=1):")
    all_ok = True
    for k in range(6, k_max, 4):  # k = 6,10,14,... (todos ≡2 mod4)
        row = [(2 ** a) * (3 ** (k - a)) - 1 for a in range(1, k + 1)]
        primes = [v for v in row if isprime(v)]
        if primes:
            all_ok = False
            print(f"  k={k}: CONTRAEXEMPLO, primos encontrados: {primes[:3]}")
        else:
            print(f"  k={k}: sem primos ({len(row)} elementos) - OK")
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


if __name__ == "__main__":
    ok1 = verify_theorem_3_6()
    print()
    ok2 = verify_theorem_4_1()
    print()
    print(f"Teorema 3.6: {'CONFIRMADO' if ok1 else 'FALHOU'}")
    print(f"Teorema 4.1: {'CONFIRMADO' if ok2 else 'FALHOU'}")
