#!/usr/bin/env python3
"""
H-092 / item 071 - Koyuncu, Sathiyakumar, Alayode, Ellis, Thomas,
"Parity-Based Level-Set Approach to the Collatz Conjecture" (Mathematics
2026, 14, 1763, MDPI, peer-reviewed).

Verifica:
1. Lemma 1 (formula exata de n a partir do codigo de paridade e das
   posicoes dos passos impares) contra trajetorias reais de Collatz.
2. Reproduz o experimento central do paper (Secao 3): para L=10..50,
   particiona l_x por numero de passos impares k, calcula media por
   classe, regride log(media) contra k, confere slope b ~ -log(6) e
   R^2 proximo de 1.
3. Compara o slope empirico com o valor teorico -log(6) (o proprio
   paper nao faz essa comparacao explicita, so' relata "estavel").
"""
import math
import statistics


def collatz_trajectory(n):
    traj = [n]
    while traj[-1] != 1:
        a = traj[-1]
        traj.append(3 * a + 1 if a % 2 == 1 else a // 2)
    return traj


def parity_code(n):
    traj = collatz_trajectory(n)
    return [1 if a % 2 == 1 else 0 for a in traj[:-1]]


def verify_lemma1(n_values):
    """n = 2^(x-k)/3^k - sum_r 2^(t_r+1-r)/3^r, onde t_r sao as posicoes
    (0-indexed) dos passos impares (r=1..k)."""
    print("=== Verificacao do Lemma 1 (formula exata de n) ===")
    all_ok = True
    for n in n_values:
        p = parity_code(n)
        x = len(p)
        positions = [t for t, bit in enumerate(p) if bit == 1]
        k = len(positions)
        from fractions import Fraction
        total = Fraction(2) ** (x - k) / Fraction(3) ** k
        for r, t in enumerate(positions, start=1):
            total -= Fraction(2) ** (t + 1 - r) / Fraction(3) ** r
        ok = (total == n)
        all_ok &= ok
        print(f"  n={n:6d}  x={x:3d}  k={k:2d}  formula={total}  bate={ok}")
    print(f"Todos batem exatamente: {all_ok}\n")
    return all_ok


def collatz_length(n, cache):
    if n in cache:
        return cache[n]
    orig = n
    steps = 0
    path = []
    while n != 1:
        path.append(n)
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2
        steps += 1
        if n in cache:
            steps += cache[n]
            break
    total = steps
    # preenche cache para todos os n do caminho (comprimento decrescente)
    running = total
    for v in path:
        cache[v] = running
        running -= 1
    return total


def odd_step_count(n):
    k = 0
    while n != 1:
        if n % 2 == 1:
            n = 3 * n + 1
            k += 1
        else:
            n = n // 2
    return k


def build_level_sets(n_max, l_min, l_max):
    cache = {1: 0}
    length_of = {}
    for n in range(2, n_max + 1):
        length_of[n] = collatz_length(n, cache)
    level_sets = {x: [] for x in range(l_min, l_max + 1)}
    for n, x in length_of.items():
        if l_min <= x <= l_max:
            level_sets[x].append(n)
    return level_sets


def linreg(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / n
    varx = sum((x - mx) ** 2 for x in xs) / n
    vary = sum((y - my) ** 2 for y in ys) / n
    b = cov / varx if varx > 0 else None
    a = my - b * mx if b is not None else None
    r2 = (cov ** 2 / (varx * vary)) if varx > 0 and vary > 0 else None
    return a, b, r2


def reproduce_table1(n_max, l_min, l_max):
    print(f"=== Reproducao do experimento central (n<= {n_max}, L={l_min}..{l_max}) ===")
    level_sets = build_level_sets(n_max, l_min, l_max)
    theoretical_slope = -math.log(6)
    print(f"Slope teorico -log(6) = {theoretical_slope:.4f}\n")
    print(f"{'L':>3} {'|l_L|':>7} {'clusters':>8} {'b':>9} {'R2':>8}")
    slopes = []
    for x in range(l_min, l_max + 1):
        ns = level_sets[x]
        if not ns:
            continue
        by_k = {}
        for n in ns:
            k = odd_step_count(n)
            by_k.setdefault(k, []).append(n)
        ks = sorted(by_k)
        if len(ks) < 3:
            continue
        log_means = [math.log(statistics.mean(by_k[k])) for k in ks]
        a, b, r2 = linreg(ks, log_means)
        slopes.append(b)
        print(f"{x:>3} {len(ns):>7} {len(ks):>8} {b:>9.4f} {r2:>8.4f}")
    print(f"\nSlope medio observado: {statistics.mean(slopes):.4f} "
          f"(desvio-padrao {statistics.pstdev(slopes):.4f})")
    print(f"Diferenca vs. teorico -log(6)={theoretical_slope:.4f}: "
          f"{statistics.mean(slopes) - theoretical_slope:+.4f}")


if __name__ == "__main__":
    verify_lemma1([17, 27, 97, 671, 6171, 837799])
    reproduce_table1(n_max=100_000, l_min=10, l_max=30)
