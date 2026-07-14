"""
E-038 - Verificacao do mecanismo por tras da dependencia nao-linear
encontrada em experiment.py (hamming(n) vs hamming(m), etc).

Parte 1: confirma popcount(m) == popcount(3n+1) exatamente (dividir por
2^a so remove zeros a direita).

Parte 2: experimento de controle - substitui "3n+1" por transformacoes
sinteticas do mesmo tipo geral (multiplicador impar + constante) e mede
a mesma MI. Se transformacoes SEM relacao com Collatz mostram o mesmo
tipo de dependencia, isso descarta "e especifico do 3n+1" como
explicacao - e um fenomeno generico de propagacao de carry em
aritmetica binaria.
"""
import random
import numpy as np

random.seed(2026)
np.random.seed(2026)


def popcount(x):
    return bin(x).count('1')


def mutual_info(x, y):
    x = np.asarray(x)
    y = np.asarray(y)
    _, xidx = np.unique(x, return_inverse=True)
    _, yidx = np.unique(y, return_inverse=True)
    nx, ny = xidx.max() + 1, yidx.max() + 1
    joint = np.zeros((nx, ny))
    np.add.at(joint, (xidx, yidx), 1)
    joint /= joint.sum()
    px = joint.sum(axis=1, keepdims=True)
    py = joint.sum(axis=0, keepdims=True)
    nz = joint > 0
    ratio = np.ones_like(joint)
    ratio[nz] = joint[nz] / (px * py)[nz]
    return float(np.sum(joint[nz] * np.log2(ratio[nz])))


def part1_exact_popcount_identity(n_trials=200_000):
    print(f"Parte 1: verificando popcount(m) == popcount(3n+1) em {n_trials} casos...")
    mismatches = 0
    for _ in range(n_trials):
        n = random.randrange(2**24, 2**25) | 1
        val = 3 * n + 1
        while val % 2 == 0:
            val //= 2
        if popcount(val) != popcount(3 * n + 1):
            mismatches += 1
    print(f"  mismatches: {mismatches} de {n_trials} (esperado: 0)")
    return mismatches == 0


def test_transform(mult, add, label, a_fix=1, n_samples=200_000):
    hn, hm = [], []
    while len(hn) < n_samples:
        n = random.randrange(2**24, 2**25) | 1
        val = mult * n + add
        if val <= 0:
            continue
        a = 0
        while val % 2 == 0:
            val //= 2
            a += 1
        if a != a_fix:
            continue
        hn.append(popcount(n))
        hm.append(popcount(val))
    hn = np.array(hn)
    hm = np.array(hm)
    mi = mutual_info(hn, hm)
    print(f"  {label}: n={len(hn)}, MI(popcount(n);popcount(saida))={mi:.5f}")
    return mi


def part2_control_experiment():
    print("\nParte 2: controle com transformacoes sinteticas (a=1 fixo)...")
    test_transform(3, 1, "3n+1 (Collatz real)")
    test_transform(5, 1, "5n+1 (controle)")
    test_transform(7, 3, "7n+3 (controle)")
    test_transform(9, 5, "9n+5 (controle)")

    print("\nParte 2b: variando o deslocamento (multiplicador = 2^k+1, a=1 fixo)...")
    for k in range(1, 7):
        test_transform((1 << k) + 1, 1, f"mult=2^{k}+1={(1 << k) + 1} (shift={k})")


if __name__ == "__main__":
    ok = part1_exact_popcount_identity()
    part2_control_experiment()
    print(f"\nParte 1 confirmada exatamente: {ok}")
