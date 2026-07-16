#!/usr/bin/env python3
"""
E-090 (extensao 2026-07-16, parte 3) - teste decisivo proposto pelo
Fable apos revisar a derivacao da ponte teorica entre G(v) e a medida
de Syracuse mu de Tao (Lemma 1.12).

Diagnostico do Fable: a identidade G(v) = soma_a 3*2^-a*(1+O(2^-a/v))*
G(w_a) + v/N so coincide EXATAMENTE com a recursao de mu no limite
headroom=N/v -> infinito. No codigo, measure_G usa headroom FIXO
(n_max=v*20, mult=20) para todo m - e cada digito 3-adico extra de
resolucao exige ~(4/3)^m mais folga de escala para nao truncar. Isso
prediz que o pico de correlacao (que observamos em m=3-4 com mult=20)
deveria DESLOCAR para m maior conforme aumentamos o headroom:
aproximadamente m~7 com mult=200, m~11-12 com mult=2000.

Tambem incorpora a segunda correcao do Fable: usar media ARITMETICA de
G por classe residual (nao media geometrica) - o operador da recursao
e linear, entao quem satisfaz a recursao e E[G|classe], nao a media
geometrica (que introduz vies multiplicativo correlacionado com a
classe, pela propria estrutura 3-adica da variancia de log G ja
identificada em H-087).

Reproduzir: python3 experiment_headroom.py
"""
import math
import random
import statistics

from experiment import (
    syrac_distribution_float,
    sample_odd_with_residue,
    build_tree_count_dfs,
)


def measure_G_headroom(v, mult):
    """Como measure_G, mas com headroom (mult) parametrizavel."""
    n_max = v * mult
    search_bound = n_max * 5
    total, odd, max_gen = build_tree_count_dfs(v, n_max, search_bound)
    D = odd / n_max if n_max > 0 else None
    if D is None or D <= 0:
        return None
    return D * v


def window_for_mod_k(mod_k, min_distinct=200, log_lo_base=6.0):
    log_lo = log_lo_base
    while (10 ** (log_lo + 1.0) - 10 ** log_lo) / mod_k < min_distinct:
        log_lo += 1.0
    return log_lo, log_lo + 1.0


def arithmetic_mean_G_by_residue(m, mult, residues, n_per_residue, seed):
    """Media ARITMETICA (nao geometrica) de G(v) por classe residual,
    conforme correcao do Fable - E[G|classe] e o alvo teorico correto
    (operador linear)."""
    mod_k = 3 ** m
    log_lo, log_hi = window_for_mod_k(mod_k, min_distinct=max(50, n_per_residue * 3))
    rng = random.Random(seed)
    out = {}
    for r in residues:
        vals = []
        for _ in range(n_per_residue):
            v = sample_odd_with_residue(rng, mod_k, r, log_lo, log_hi)
            if v is None:
                continue
            G = measure_G_headroom(v, mult)
            if G is not None and G > 0:
                vals.append(G)
        if vals:
            out[r] = statistics.mean(vals)
    return out


def log_log_fit(xs, ys):
    logs_x = [math.log10(x) for x in xs]
    logs_y = [math.log10(y) for y in ys]
    n = len(logs_x)
    mx = sum(logs_x) / n
    my = sum(logs_y) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(logs_x, logs_y)) / n
    varx = sum((x - mx) ** 2 for x in logs_x) / n
    vary = sum((y - my) ** 2 for y in logs_y) / n
    if varx == 0 or vary == 0:
        return None, None
    corr = cov / math.sqrt(varx * vary)
    b = cov / varx
    return corr, b


def test_point(m, mult, n_residues_sample, n_per_residue, seed=42):
    mod_k = 3 ** m
    mu = syrac_distribution_float(m, a_max=64)
    all_r = [r for r in range(mod_k) if r % 3 != 0]
    rng0 = random.Random(7)
    sample_r = rng0.sample(all_r, min(n_residues_sample, len(all_r)))

    mean_G = arithmetic_mean_G_by_residue(m, mult, sample_r, n_per_residue, seed)

    common_r = [r for r in sample_r if mu.get(r, 0) > 0 and r in mean_G]
    xs = [mod_k * mu[r] for r in common_r]
    ys = [mean_G[r] for r in common_r]
    if len(xs) < 5:
        return None
    corr, b = log_log_fit(xs, ys)
    return corr, b, len(xs)


def main():
    print("=== Teste decisivo (Fable): headroom fixo causa a degradacao? ===")
    print("Predicao: pico de correlacao desloca m~3-4 (mult=20) -> m~7 (mult=200) -> m~11-12 (mult=2000)\n")

    plan = {
        20:   [2, 3, 4, 6, 8, 10, 12],
        200:  [2, 4, 6, 7, 8, 9, 10, 12],
        2000: [4, 6, 8, 10, 11, 12, 13, 14],
    }

    for mult, ms in plan.items():
        print(f"--- headroom (mult) = {mult} ---")
        for m in ms:
            n_per_residue = 60 if mult <= 200 else 20
            n_residues_sample = 800
            result = test_point(m, mult, n_residues_sample, n_per_residue)
            if result is None:
                print(f"  m={m:2d}: dados insuficientes")
                continue
            corr, b, n = result
            print(f"  m={m:2d}: corr={corr:.4f}  b(expoente)={b:.4f}  n_res={n}")
        print()


if __name__ == "__main__":
    main()
