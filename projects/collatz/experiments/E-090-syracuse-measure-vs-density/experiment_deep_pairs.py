#!/usr/bin/env python3
"""
H-100/H-101 (2026-07-16) - teste decisivo proposto pelo Fable apos
criticar a extrapolacao ingenua de H-100 (que sugeria um "piso" de
resid_std~0,042 dex, mas e' estatisticamente fragil - mistura de taxas
heterogeneas entre classes, ou lei de potencia, imitam um piso mesmo
quando o limite real e zero).

Ideia: gera pares (v1, v2) com v2 = v1 + t*3^m para t pequeno (mesmos
m primeiros digitos 3-adicos por construcao, ja que t*3^m ~= 0 mod
3^m), com v1 grande o suficiente para que v2/v1 fique bem proximo de 1
(diferenca de magnitude desprezivel). NAO precisa computar mu_M nem
montar arrays mod 3^m - evita completamente o overflow int64 que
limitava M a 18 na abordagem anterior, e alcanca profundidades m ate
23 (muito alem de M=18).

Var(log G(v2) - log G(v1)) / 2 estima a variancia NAO explicada pelos
m primeiros digitos 3-adicos de v - sem qualquer referencia a mu. Se
essa variancia continuar caindo ate convergir ao "piso de ruido de
headroom" (~0,004-0,01 dex^2 em escala de variancia, medido
independentemente em H-091/H-100 via convergencia pareada por headroom),
entao (S) esta confirmada ate a precisao de medicao - o "piso" anterior
era artefato de mistura/extrapolacao. Se estabilizar bem acima disso,
ha uma dependencia genuina de v alem do resíduo 3-adico.

Reproduzir: python3 experiment_deep_pairs.py
"""
import math
import random
import statistics

from experiment_headroom import measure_G_headroom

MULT = 20000  # headroom moderado, bem convergido (H-091: 20000->100000 da std(Delta)~0.01 dex)
V1_LOG_LO, V1_LOG_HI = 12.5, 13.5  # v1 ~ 1e12.5 a 1e13.5
TARGET_REL_DIFF = 0.01  # ~1% de diferenca de magnitude entre v1 e v2


def sample_pair(rng, m):
    """Gera v1 (impar, nao multiplo de 3) e v2=v1+t*3^m (mesmos m
    primeiros digitos 3-adicos), com t escolhido para manter v2/v1
    proximo de 1 (t par para preservar paridade impar de v2)."""
    pow3m = 3 ** m
    while True:
        mag = 10 ** rng.uniform(V1_LOG_LO, V1_LOG_HI)
        v1 = int(mag) | 1
        if v1 % 3 == 0:
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


def run_for_m(m, n_pairs, seed):
    rng = random.Random(seed)
    deltas = []
    rel_diffs = []
    for _ in range(n_pairs):
        v1, v2 = sample_pair(rng, m)
        d = measure_delta(v1, v2, MULT)
        if d is not None:
            deltas.append(d)
            rel_diffs.append((v2 - v1) / v1)
    var_delta = statistics.pvariance(deltas)
    residual_var = var_delta / 2
    residual_std = math.sqrt(residual_var)
    return residual_std, residual_var, statistics.mean(rel_diffs), len(deltas)


def fit_models(ms, variances):
    """Ajusta 3 modelos em escala de VARIANCIA (nao desvio-padrao),
    conforme recomendado pelo Fable, e compara por soma de quadrados
    dos residuos (proxy simples para AIC, mesmo numero de parametros
    nos 3 modelos: 2 livres + o piso fixado em 0 nos modelos "zero")."""
    import math as _m

    def sse_floor_geometric(params):
        # var(m) = floor + c*q^m
        floor, log_c, q = params
        if not (0 < q < 1) or floor < 0:
            return float("inf")
        pred = [floor + _m.exp(log_c) * (q ** m) for m in ms]
        return sum((p - v) ** 2 for p, v in zip(pred, variances))

    def sse_zero_geometric(params):
        # var(m) = c*q^m
        log_c, q = params
        if not (0 < q < 1):
            return float("inf")
        pred = [_m.exp(log_c) * (q ** m) for m in ms]
        return sum((p - v) ** 2 for p, v in zip(pred, variances))

    def sse_zero_powerlaw(params):
        # var(m) = c*m^(-alpha)
        log_c, alpha = params
        if alpha <= 0:
            return float("inf")
        pred = [_m.exp(log_c) * (m ** (-alpha)) for m in ms]
        return sum((p - v) ** 2 for p, v in zip(pred, variances))

    # busca em grade simples (sem scipy) para cada modelo
    best = {}

    best_sse = float("inf")
    for floor in [0.0001, 0.0005, 0.001, 0.002, 0.003, 0.005, 0.008, 0.012]:
        for log_c in [x / 10 for x in range(-50, 10)]:
            for q in [x / 100 for x in range(50, 99)]:
                s = sse_floor_geometric((floor, log_c, q))
                if s < best_sse:
                    best_sse = s
                    best = {"floor_geometric": (floor, log_c, q, s)}

    best_sse2 = float("inf")
    for log_c in [x / 10 for x in range(-50, 10)]:
        for q in [x / 100 for x in range(50, 99)]:
            s = sse_zero_geometric((log_c, q))
            if s < best_sse2:
                best_sse2 = s
                best["zero_geometric"] = (log_c, q, s)

    best_sse3 = float("inf")
    for log_c in [x / 10 for x in range(-50, 20)]:
        for alpha in [x / 100 for x in range(10, 400)]:
            s = sse_zero_powerlaw((log_c, alpha))
            if s < best_sse3:
                best_sse3 = s
                best["zero_powerlaw"] = (log_c, alpha, s)

    return best


def main():
    print("=== Teste de pares casados profundos (proposto pelo Fable) ===")
    print(f"headroom={MULT}, v1 ~ 10^{V1_LOG_LO}-10^{V1_LOG_HI}, diferenca relativa alvo ~{TARGET_REL_DIFF*100:.1f}%\n")
    print(f"{'m':>3} {'resid_std':>10} {'resid_var':>11} {'diff_rel_media':>15} {'n_pares':>8}")

    ms = [8, 11, 14, 17, 20, 23]
    results = []
    for m in ms:
        n_pairs = 2000
        resid_std, resid_var, mean_rel_diff, n = run_for_m(m, n_pairs, seed=100 + m)
        results.append((m, resid_std, resid_var))
        print(f"{m:>3} {resid_std:>10.4f} {resid_var:>11.6f} {mean_rel_diff*100:>14.3f}% {n:>8}")

    print("\nComparacao: piso de ruido de headroom estimado independentemente")
    print("(H-091/H-100, convergencia pareada headroom 100000->1000000): std~0.0044 dex, var~0.0000194")
    print("\nSe resid_std convergir para perto de 0.004-0.01 dex conforme m cresce, o 'piso' de H-100 era")
    print("artefato de extrapolacao/mistura de taxas - (S) confirmada ate a precisao de medicao.")
    print("Se estabilizar bem acima disso, ha estrutura genuina nao explicada pelos digitos 3-adicos.")

    print("\n=== Ajuste de modelos (escala de variancia, busca em grade) ===")
    variances = [r[2] for r in results]
    best = fit_models(ms, variances)
    for name, vals in best.items():
        print(f"  {name}: params={vals[:-1]}  SSE={vals[-1]:.8f}")


if __name__ == "__main__":
    main()
