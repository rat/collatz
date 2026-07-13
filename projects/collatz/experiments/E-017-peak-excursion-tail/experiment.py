#!/usr/bin/env python3
"""
E-017 - Testa H-017: a cauda do pico da orbita decai com fator EXATO de 2
por bit de excursao (Delta = log2(pico/n)), sem parametro livre (expoente
de Cramer theta*=1, verificado analiticamente antes de rodar isso).

Reproduzir: python3 experiment.py [N_AMOSTRAS] [LOW] [HIGH] [SEED]
"""
import sys
import math
import random


def peak_delta(n):
    """Retorna Delta = log2(pico/n), pico = maior valor na orbita completa."""
    n0 = n
    peak = n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        if n > peak:
            peak = n
    return math.log2(peak / n0)


def main():
    n_samples = int(sys.argv[1]) if len(sys.argv) > 1 else 500_000
    low = int(sys.argv[2]) if len(sys.argv) > 2 else 10 ** 9
    high = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 12
    seed = int(sys.argv[4]) if len(sys.argv) > 4 else 42
    rng = random.Random(seed)

    deltas = []
    for _ in range(n_samples):
        n = rng.randrange(low // 2, high // 2) * 2 + 1
        deltas.append(peak_delta(n))

    deltas.sort()
    n_total = len(deltas)

    print(f"amostras = {n_total}, n em [{low}, {high}]")
    print()
    print(f"{'x (bits)':>10} {'P(Delta>=x) empirico':>22} {'previsto ~2^-x':>16} {'contagem':>10}")

    xs_used = []
    logps_used = []
    import bisect
    for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
        idx = bisect.bisect_left(deltas, x)
        count = n_total - idx
        p_emp = count / n_total
        p_pred = 2 ** (-x)
        print(f"{x:>10} {p_emp:>22.6f} {p_pred:>16.6f} {count:>10}")
        if count >= 30:  # so usar pontos com contagem estatisticamente razoavel
            xs_used.append(x)
            logps_used.append(math.log2(p_emp))

    def fit_slope(xs, ys):
        n_pts = len(xs)
        mean_x = sum(xs) / n_pts
        mean_y = sum(ys) / n_pts
        sxx = sum((x - mean_x) ** 2 for x in xs)
        sxy = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
        return sxy / sxx

    slope_all = fit_slope(xs_used, logps_used)
    print()
    print(f"inclinacao empirica (todos os x com contagem>=30) = {slope_all:.4f}  (previsto -1.0)")

    # cauda distante (x>=6): aproximacao assintotica deveria ser mais precisa
    tail_pairs = [(x, y) for x, y in zip(xs_used, logps_used) if x >= 6]
    if len(tail_pairs) >= 3:
        xs_tail, ys_tail = zip(*tail_pairs)
        slope_tail = fit_slope(list(xs_tail), list(ys_tail))
        print(f"inclinacao empirica (so cauda x>=6)          = {slope_tail:.4f}  (previsto -1.0)")
        print(f"diferenca relativa (cauda) = {abs(slope_tail - (-1)) * 100:.2f}%")


if __name__ == "__main__":
    main()
