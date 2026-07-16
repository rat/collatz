#!/usr/bin/env python3
"""
E-086 - Testa a critica do modelo Fable a H-024: H-024 mostrou que D(v)
nao e funcao do residuo de v mod 3^K sozinho, testando 5 valores
v=85,1543,4459,14665,72985 (todos =85 mod 729) com magnitudes MUITO
diferentes (fator ~860x). Fable apontou: isso NAO separa o efeito do
residuo do efeito da magnitude - se D(v) fatora como
    D(v) ~ F(log v; n_max) * G(v mod 3^K)
a variacao de 300x pode ser majoritariamente o termo F (arquimediano),
nao o termo G (3-adico), e a atribuicao "profundidade 3-adica infinita"
estaria mal-diagnosticada mesmo com a conclusao formal correta.

Este experimento reaproveita build_tree_count_dfs (ja validado em
E-018) para medir D(v) EM JANELAS DE MAGNITUDE ESTREITAS - fixando v
dentro de [N, 2N) para varios K crescentes, e comparando a variancia
de log(D) DENTRO da janela (so efeito de residuo, magnitude quase
fixa) contra a variancia TOTAL medida antes (residuo fixo, magnitude
livre) e contra a variancia ENTRE janelas de N diferentes (so efeito
de magnitude, residuo variando).

Reproduzir: python3 experiment.py
"""
import sys
import math
import random
from collections import Counter

sys.path.insert(0, "../E-018-reverse-tree-branching")
from experiment_dfs import build_tree_count_dfs


def measure_D(v, n_max, mult=5):
    """Densidade D(v) = fracao de impares <= n_max na subarvore de v,
    normalizada por n_max (comparavel entre v diferentes com o MESMO
    n_max - a comparacao classica ja usada no projeto)."""
    search_bound = n_max * mult
    total, odd, max_gen = build_tree_count_dfs(v, n_max, search_bound)
    return odd / n_max if n_max > 0 else None


def sample_odd_in_window(rng, lo, hi, mod_k, target_residue):
    """Amostra um v impar em [lo, hi) com v % mod_k == target_residue,
    tentando ate achar (rejection sampling simples)."""
    lo, hi = int(lo), int(hi)
    for _ in range(10000):
        v = rng.randrange(lo, hi)
        if v % 2 == 1 and v % mod_k == target_residue:
            return v
    return None


def test_within_window_variance(K_values, n_samples_per_K=15, window_width_factor=2,
                                  base_magnitude=10**5, n_max=None, seed=1):
    """Para cada K (modulo 3^K), fixa a JANELA de magnitude [N, 2N) e
    sorteia varios v dentro dela, todos com o MESMO residuo mod 3^K
    (fixo, escolhido uma vez por K). Mede a variancia de log(D) dentro
    dessa janela - isolando o efeito de residuos MAIS FINOS que 3^K
    (ja que o residuo mod 3^K esta fixo, mas os digitos mais profundos
    variam livremente dentro da janela)."""
    rng = random.Random(seed)
    if n_max is None:
        n_max = base_magnitude * window_width_factor * 20  # orcamento generoso

    results = {}
    for K in K_values:
        mod_k = 3 ** K
        # escolhe um residuo mod 3^K compativel com v impar e nao-esteril
        # (v % 3 != 0, ja que v=0 mod3 e esteril, D trivial)
        target_residue = None
        for cand in range(1, mod_k, 2):
            if cand % 3 != 0:
                target_residue = cand
                break
        lo, hi = base_magnitude, base_magnitude * window_width_factor

        logs = []
        for _ in range(n_samples_per_K):
            v = sample_odd_in_window(rng, lo, hi, mod_k, target_residue)
            if v is None:
                continue
            D = measure_D(v, n_max)
            if D is not None and D > 0:
                logs.append(math.log10(D))

        if len(logs) >= 3:
            mean_log = sum(logs) / len(logs)
            var_log = sum((x - mean_log) ** 2 for x in logs) / len(logs)
            std_log = math.sqrt(var_log)
        else:
            std_log = None
        results[K] = (len(logs), std_log, logs)
        print(f"  K={K:2d} (mod 3^{K}={mod_k}), residuo_fixo={target_residue}, "
              f"janela=[{lo},{hi}): {len(logs)} amostras validas, "
              f"desvio_log10(D) DENTRO da janela = {std_log}")
    return results


def test_between_window_variance(K, n_windows=15, window_width_factor=2,
                                   base_magnitude=10**5, magnitude_growth=1.5,
                                   n_max=None, seed=2):
    """Para o MESMO residuo mod 3^K fixo, mede D(v) em varias janelas de
    magnitude DIFERENTES (cada uma internamente estreita) - isolando o
    efeito PURO de magnitude (residuo mod 3^K fixo em todas)."""
    rng = random.Random(seed)
    mod_k = 3 ** K
    target_residue = None
    for cand in range(1, mod_k, 2):
        if cand % 3 != 0:
            target_residue = cand
            break

    logs = []
    mag = base_magnitude
    for i in range(n_windows):
        lo, hi = int(mag), int(mag * window_width_factor)
        local_n_max = n_max if n_max else hi * 20
        v = sample_odd_in_window(rng, lo, hi, mod_k, target_residue)
        if v is not None:
            D = measure_D(v, local_n_max)
            if D and D > 0:
                logs.append((mag, math.log10(D)))
        mag *= magnitude_growth

    if len(logs) >= 3:
        vals = [x[1] for x in logs]
        mean_log = sum(vals) / len(vals)
        var_log = sum((x - mean_log) ** 2 for x in vals) / len(vals)
        std_log = math.sqrt(var_log)
    else:
        std_log = None
    print(f"  residuo fixo={target_residue} (mod 3^{K}), {len(logs)} janelas de magnitude testadas")
    print(f"  desvio_log10(D) ENTRE janelas de magnitude = {std_log}")
    for mag, logD in logs:
        print(f"    mag~{mag:.0f}: log10(D)={logD:.4f}")
    return std_log


def main():
    print("=== Teste 1: variancia de log(D) DENTRO de uma janela de magnitude estreita ===")
    print("(residuo mod 3^K fixo, magnitude quase fixa, digitos mais profundos livres)")
    results = test_within_window_variance(K_values=[2, 4, 6], n_samples_per_K=12,
                                            base_magnitude=200_000, window_width_factor=1.5)
    print()

    print("=== Teste 2: variancia de log(D) ENTRE janelas de magnitude diferentes ===")
    print("(residuo mod 3^6 fixo, magnitude variando por fator 1.5x por passo)")
    std_between = test_between_window_variance(K=6, n_windows=10, base_magnitude=50_000,
                                                  magnitude_growth=2.0)
    print()

    print("=== Comparacao com H-024 original (residuo mod 3^6=729 fixo, magnitude livre ~860x) ===")
    print("  H-024 original: desvio_log10(D) ~ log10(300) / 2 ~ 1.24 dex (variacao de 300x, ordem de grandeza)")
    for K, (n, std, logs) in results.items():
        if std is not None:
            print(f"  DENTRO de janela estreita, K={K}: desvio = {std:.4f} dex")
    if std_between is not None:
        print(f"  ENTRE janelas de magnitude, K=6: desvio = {std_between:.4f} dex")
    print()
    print("  Interpretacao: se o desvio DENTRO de janela estreita for << o desvio")
    print("  ENTRE janelas (ou << o desvio original de H-024), a maior parte da")
    print("  variacao de 300x era efeito de MAGNITUDE, nao de residuo profundo -")
    print("  confirmando a critica do Fable. Se os desvios forem comparaveis,")
    print("  a dependencia 3-adica profunda genuina sobrevive.")


if __name__ == "__main__":
    main()
