#!/usr/bin/env python3
"""
Abordagem #2 (reformulada pelo Fable): em vez de PCA cru no espectro
do operador de transferencia (que tem armadilhas serias com poucas
amostras por classe - inflacao Marchenko-Pastur), testa diretamente se
a TAXA de decaimento da variancia residual difere entre classes
grosseiras (v1 mod 9, as 6 classes nao-esteireis) - se sim, confirma o
mecanismo de "mistura de taxas heterogeneas" ja sugerido pelo achado de
Jensen (H-099, gap variando ~46x entre classes).

Reusa a infraestrutura de pares casados (H-101): para cada classe
grosseira c (v1 mod 9 = c), gera pares (v1,v2) com v1 restrito a essa
classe, compartilhando m digitos 3-adicos, para dois niveis de m
(um raso, um profundo) - compara a razao de variancia entre os dois
niveis, por classe. Se a razao de decaimento diferir muito entre
classes, confirma heterogeneidade real de taxa.

Reproduzir: python3 experiment_stratified_variance.py
"""
import math
import random
import statistics

from experiment_headroom import measure_G_headroom

MULT = 20000
TARGET_REL_DIFF = 0.01
V1_LOG_LO, V1_LOG_HI = 12.5, 13.5


def sample_pair_in_class(rng, m, coarse_class, coarse_mod=9):
    """Como sample_pair, mas forca v1 mod coarse_mod == coarse_class."""
    pow3m = 3 ** m
    while True:
        mag = 10 ** rng.uniform(V1_LOG_LO, V1_LOG_HI)
        v1 = int(mag) | 1
        if v1 % 3 == 0:
            continue
        if v1 % coarse_mod != coarse_class:
            continue
        t_target = max(1, round(TARGET_REL_DIFF * v1 / pow3m))
        t = t_target if t_target % 2 == 0 else t_target + 1
        if t == 0:
            t = 2
        v2 = v1 + t * pow3m
        if v2 % 2 == 1 and v2 % 3 != 0:
            return v1, v2


def measure_delta(v1, v2, mult):
    G1 = measure_G_headroom(v1, mult)
    G2 = measure_G_headroom(v2, mult)
    if G1 is None or G2 is None or G1 <= 0 or G2 <= 0:
        return None
    return math.log10(G2) - math.log10(G1)


def run(coarse_class, m, n_pairs, seed):
    rng = random.Random(seed)
    deltas = []
    tries = 0
    while len(deltas) < n_pairs and tries < n_pairs * 50:
        tries += 1
        v1, v2 = sample_pair_in_class(rng, m, coarse_class)
        d = measure_delta(v1, v2, MULT)
        if d is not None:
            deltas.append(d)
    if len(deltas) < 20:
        return None
    return statistics.pvariance(deltas) / 2, len(deltas)


def main():
    classes = [1, 2, 4, 5, 7, 8]  # nao-esteireis, mod 9
    m_shallow, m_deep = 11, 23
    n_pairs = 400

    print(f"=== Decaimento de variancia estratificado por v1 mod 9 (m={m_shallow} vs m={m_deep}) ===\n")
    print(f"{'classe':>7} {'var(m=11)':>11} {'var(m=23)':>11} {'razao (23/11)':>14} {'n11':>5} {'n23':>5}")

    ratios = []
    for c in classes:
        r_shallow = run(c, m_shallow, n_pairs, seed=3000 + c)
        r_deep = run(c, m_deep, n_pairs, seed=4000 + c)
        if r_shallow is None or r_deep is None:
            print(f"{c:>7}  dados insuficientes")
            continue
        var_s, n_s = r_shallow
        var_d, n_d = r_deep
        ratio = var_d / var_s if var_s > 0 else None
        ratios.append(ratio)
        print(f"{c:>7} {var_s:>11.6f} {var_d:>11.6f} {ratio:>14.4f} {n_s:>5} {n_d:>5}")

    if ratios:
        print(f"\nRazao media entre classes: {statistics.mean(ratios):.4f}")
        print(f"Desvio-padrao da razao entre classes: {statistics.pstdev(ratios):.4f}")
        print("(Se o desvio-padrao for grande relativo a media, as classes tem taxas de")
        print(" decaimento bem diferentes - confirma mistura heterogenea de taxas, coerente")
        print(" com o achado de Jensen de H-099. Se for pequeno, a taxa e' aproximadamente")
        print(" uniforme entre classes grosseiras, e a heterogeneidade de Jensen vem de outro lugar.)")


if __name__ == "__main__":
    main()
