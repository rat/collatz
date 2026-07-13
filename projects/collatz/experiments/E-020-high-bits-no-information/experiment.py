#!/usr/bin/env python3
"""
E-020 - Testa H-020: bits baixos de n carregam informacao real sobre
total_stopping_time (esperado, via Terras/H-002); bits altos nao deveriam
(controle metodologico).

Agrupa n (comprimento de bits fixo) por 8 bits baixos vs 8 bits altos,
compara variancia das medias entre grupos (estilo ANOVA) nos dois casos.

Reproduzir: python3 experiment.py [BIT_LENGTH] [N_AMOSTRAS] [SEED]
"""
import sys
import math
import random

K_H010 = 3 / (2 - math.log2(3))  # constante teorica de H-010 (~7.2283)


def total_stopping_time(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


def between_group_stats(groups):
    """groups: dict grupo -> lista de valores. Retorna (var_entre_grupos, var_dentro_grupos)."""
    all_vals = [v for vs in groups.values() for v in vs]
    grand_mean = sum(all_vals) / len(all_vals)

    ss_between = 0.0
    ss_within = 0.0
    for vs in groups.values():
        m = sum(vs) / len(vs)
        ss_between += len(vs) * (m - grand_mean) ** 2
        ss_within += sum((v - m) ** 2 for v in vs)

    df_between = len(groups) - 1
    df_within = len(all_vals) - len(groups)
    ms_between = ss_between / df_between
    ms_within = ss_within / df_within
    f_stat = ms_between / ms_within
    return f_stat, ms_between, ms_within


def main():
    bit_length = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    n_samples = int(sys.argv[2]) if len(sys.argv) > 2 else 200_000
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 42
    rng = random.Random(seed)

    low = 2 ** (bit_length - 1)
    high = 2 ** bit_length

    groups_low_bits = {}
    groups_high_bits = {}
    groups_random_control = {}
    groups_high_bits_detrended = {}  # residuo apos remover a media K*log2(n) de H-010

    for _ in range(n_samples):
        n = rng.randrange(low, high) | 1  # forcar impar
        ts = total_stopping_time(n)
        residual = ts - K_H010 * math.log2(n)

        low_bits = n & 0xFF  # 8 bits mais baixos
        high_bits = (n >> (bit_length - 9)) & 0xFF  # 8 bits logo abaixo do lider
        random_group = rng.randrange(256)  # controle: rotulo aleatorio, sem relacao com n

        groups_low_bits.setdefault(low_bits, []).append(ts)
        groups_high_bits.setdefault(high_bits, []).append(ts)
        groups_random_control.setdefault(random_group, []).append(ts)
        groups_high_bits_detrended.setdefault(high_bits, []).append(residual)

    f_low, msb_low, msw_low = between_group_stats(groups_low_bits)
    f_high, msb_high, msw_high = between_group_stats(groups_high_bits)
    f_rand, msb_rand, msw_rand = between_group_stats(groups_random_control)

    print(f"bit_length={bit_length}, n_amostras={n_samples}")
    print(f"grupos (low bits) = {len(groups_low_bits)}, grupos (high bits) = {len(groups_high_bits)}")
    print()
    print(f"F-estatistica (bits BAIXOS, deveria ser >> 1): {f_low:.3f}")
    print(f"  MS_entre_grupos={msb_low:.2f}  MS_dentro_grupos={msw_low:.2f}")
    print()
    print(f"F-estatistica (bits ALTOS, deveria ser ~1): {f_high:.3f}")
    print(f"  MS_entre_grupos={msb_high:.2f}  MS_dentro_grupos={msw_high:.2f}")
    print()
    print(f"F-estatistica (CONTROLE: rotulo aleatorio, baseline de ruido puro): {f_rand:.3f}")
    print(f"  MS_entre_grupos={msb_rand:.2f}  MS_dentro_grupos={msw_rand:.2f}")

    f_high_dt, msb_high_dt, msw_high_dt = between_group_stats(groups_high_bits_detrended)
    print()
    print(f"F-estatistica (bits ALTOS, apos remover tendencia K*log2(n) de H-010): {f_high_dt:.3f}")
    print(f"  MS_entre_grupos={msb_high_dt:.2f}  MS_dentro_grupos={msw_high_dt:.2f}")


if __name__ == "__main__":
    main()
