#!/usr/bin/env python3
"""
H-091 (2026-07-16, parte 3) - testa a sugestao #1 recebida de uma IA
externa (consultada com o prompt de contexto completo desta linha):
a discrepancia entre b~1,00 (teste agregado por classe, media
ARITMETICA de G antes do log) e b~0,96-0,98 (teste por-v, log G
individual) seria um efeito de desigualdade de Jensen - se log G
tem variancia intra-classe que ela mesma escala com a classe/mu, a
media de log (E[log G]) fica sistematicamente abaixo do log da media
(log E[G]), e isso pode enviesar o EXPOENTE ajustado, nao so o
intercepto.

Testa diretamente: para cada classe residual r mod 3^M, amostra MUITOS
v's com esse resíduo, computa G(v) (headroom=2000, ja bem convergido
por H-091 parte 2 - std(Delta) 2000->20000 e' so 0.024 dex), e compara:
  - log(E[G|r])          (media aritmetica, depois log - "agregado")
  - E[log G|r]            (media do log - "por-v")
  - gap(r) = log(E[G|r]) - E[log G|r]   (o termo de Jensen)

Se gap(r) correlacionar com log(mu_M(r)), isso explica por que a
regressao "por-v" (que efetivamente usa E[log G|r] no agregado latente)
da um b sistematicamente menor que a regressao "agregada" (que usa
log(E[G|r])).

Reproduzir: python3 experiment_jensen.py
"""
import math
import random
import statistics

from syrac_fast import syrac_distribution_np
from experiment import sample_odd_with_residue
from experiment_headroom import measure_G_headroom, window_for_mod_k


def linreg(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / n
    varx = sum((x - mx) ** 2 for x in xs) / n
    vary = sum((y - my) ** 2 for y in ys) / n
    b = cov / varx if varx > 0 else None
    a = my - b * mx if b is not None else None
    corr = cov / math.sqrt(varx * vary) if varx > 0 and vary > 0 else None
    return a, b, corr


def main():
    M = 8
    MULT = 2000
    N_CLASSES = 500
    N_PER_CLASS = 150

    mod_k = 3 ** M
    mu = syrac_distribution_np(M)
    all_r = [r for r in range(mod_k) if r % 3 != 0 and mu[r] > 0]
    rng0 = random.Random(11)
    sample_r = rng0.sample(all_r, min(N_CLASSES, len(all_r)))

    log_lo, log_hi = window_for_mod_k(mod_k, min_distinct=max(50, N_PER_CLASS * 3))
    rng = random.Random(2026)

    log_mu_r, log_mean_G_r, mean_log_G_r, gap_r, n_r = [], [], [], [], []

    for r in sample_r:
        vals = []
        for _ in range(N_PER_CLASS):
            v = sample_odd_with_residue(rng, mod_k, r, log_lo, log_hi)
            if v is None:
                continue
            G = measure_G_headroom(v, MULT)
            if G is not None and G > 0:
                vals.append(G)
        if len(vals) < 20:
            continue
        mean_G = statistics.mean(vals)
        mean_logG = statistics.mean(math.log(g) for g in vals)
        log_mean_G = math.log(mean_G)
        gap = log_mean_G - mean_logG  # termo de Jensen, sempre >= 0

        log_mu_r.append(math.log(mod_k * mu[r]))
        log_mean_G_r.append(log_mean_G)
        mean_log_G_r.append(mean_logG)
        gap_r.append(gap)
        n_r.append(len(vals))

    print(f"M={M}  mult={MULT}  n_classes_validas={len(log_mu_r)}  amostras/classe~{N_PER_CLASS}\n")

    a1, b1, corr1 = linreg(log_mu_r, log_mean_G_r)
    a2, b2, corr2 = linreg(log_mu_r, mean_log_G_r)
    print("Regressao 'agregada' (log da media aritmetica de G  vs  log mu):")
    print(f"  b = {b1:.4f}  corr = {corr1:.4f}")
    print("Regressao 'por-v latente' (media do log G  vs  log mu):")
    print(f"  b = {b2:.4f}  corr = {corr2:.4f}")
    print(f"\nDiferenca de expoente (b_agregado - b_por_v) = {b1 - b2:.4f}")

    print(f"\nEstatisticas do termo de Jensen gap(r) = log(E[G|r]) - E[log G|r]:")
    print(f"  media(gap) = {statistics.mean(gap_r):.4f}  desvio(gap) = {statistics.pstdev(gap_r):.4f}")
    print(f"  min={min(gap_r):.4f}  max={max(gap_r):.4f}")

    a3, b3, corr3 = linreg(log_mu_r, gap_r)
    print(f"\nCorrelacao entre gap(r) e log(mu_r): corr = {corr3:.4f}, slope = {b3:.4f}")
    print("(Se |corr| for grande, o termo de Jensen varia sistematicamente com a classe")
    print(" e explica (ao menos em parte) por que a regressao por-v da b menor que a agregada.)")


if __name__ == "__main__":
    main()
