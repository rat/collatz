"""
E-041 - Verificacao independente do paper #005 (Seymour, "A Regular
Expression Language for the Collatz Graph").

Testa os resultados que o paper alega estarem PROVADOS (nao as partes
explicitamente rotuladas "Conjecture" - o proprio paper e honesto sobre
isso): Proposicao 3.1 (aritmetica do circuito Steiner via mapa natural
C), Teorema 3.6 (comprimento da corrida "7 mod 8"), e Corolario 2.2
(exit ping-pong mod 24).
"""
import random


def v2(m):
    v = 0
    while m % 2 == 0:
        m //= 2
        v += 1
    return v


def C(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1


def S(n):
    m = 3 * n + 1
    return m // (2 ** v2(m))


def verify_prop_3_1(trials=20_000, seed=5):
    random.seed(seed)
    ok = 0
    for _ in range(trials):
        a0 = random.randrange(1, 10**9) | 1
        alpha = v2(a0 + 1)
        m = (a0 + 1) // (2 ** alpha)
        x = a0
        for _ in range(alpha):
            x = C(x)
            x = C(x)
        expected_a_alpha = (3 ** alpha) * m - 1
        if x != expected_a_alpha:
            print(f"  MISMATCH (Prop 3.1) a0={a0}")
            continue
        beta = v2(expected_a_alpha)
        b = expected_a_alpha // (2 ** beta)
        y = x
        for _ in range(beta):
            y = C(y)
        if y != b:
            print(f"  MISMATCH (descida par) a0={a0}")
            continue
        ok += 1
    print(f"Proposicao 3.1: {ok}/{trials} casos corretos")
    return ok == trials


def verify_theorem_3_6(trials=50_000, seed=9):
    random.seed(seed)
    ok, tested = 0, 0
    for _ in range(trials):
        t = random.randrange(0, 10**8)
        n = 8 * t + 7
        s = v2(n + 1)
        if s < 3:
            continue
        tested += 1
        cur = n
        length = 0
        while cur % 8 == 7:
            cur = S(cur)
            length += 1
        if length == s - 2 and cur % 8 == 3:
            ok += 1
        else:
            print(f"  MISMATCH (Teorema 3.6) n={n}: length={length}, esperado={s-2}")
    print(f"Teorema 3.6: {ok}/{tested} casos corretos (com s>=3)")
    return ok == tested


def verify_corollary_2_2(trials=50_000, seed=11):
    random.seed(seed)
    ok_even = fail_even = ok_odd = fail_odd = 0
    for _ in range(trials):
        t = random.randrange(0, 10**8)
        n = 8 * t + 7
        s = v2(n + 1)
        if s < 3:
            continue
        ell = s - 2
        cur = n
        for _ in range(ell):
            cur = S(cur)
        got = cur % 24
        exp = 11 if t % 2 == 0 else 23
        if t % 2 == 0:
            ok_even += (got == exp)
            fail_even += (got != exp)
        else:
            ok_odd += (got == exp)
            fail_odd += (got != exp)
    print(f"Corolario 2.2: t par -> ok={ok_even}, falhou={fail_even}")
    print(f"               t impar -> ok={ok_odd}, falhou={fail_odd}")
    print("(esperado pelo paper: 11 se t par, 23 se t impar)")
    print("(valor real observado quando t impar: sempre 11, nunca 23 -- erro sistematico)")


if __name__ == "__main__":
    print("=== Verificacao de resultados alegados PROVADOS no paper #005 ===\n")
    verify_prop_3_1()
    print()
    verify_theorem_3_6()
    print()
    verify_corollary_2_2()
