#!/usr/bin/env python3
"""
Ideia B da segunda rodada de sugestoes externas ("espectro via
Transformada de Chrestenson"), reformulada pelo Fable: ele mostrou que
para o grupo ciclico Z/3^mZ a transformada e' equivalente (ate
precisao de maquina) a uma ANOVA aninhada simples - e a ANOVA e' a
melhor implementacao (mais facil de auditar, permite excluir v=0 mod 3,
e evita o nome tecnicamente incorreto "Chrestenson" que e' para o
grupo produto (Z/3Z)^m).

Correcoes obrigatorias apontadas pelo Fable:
(i) usar ANOVA aninhada, nao FFT crua;
(ii) VIES DE AMOSTRA FINITA: na profundidade t, cada classe tem
    n=3^(m-t) representantes - sem correcao de Bessel (dividir por n-1,
    nao por n), o residuo estimado vai a ZERO artificialmente quando
    t se aproxima de m (overfitting puro). Corrigido usando variancia
    amostral com ddof=1, e parando em t<=m-4 (n>=81) para manter a
    correcao estavel;
(iii) um bloco so' mede bem t <~ log_3(tamanho do bloco) - complementa
    os pares casados (H-101, que alcancou m=29), nao substitui;
(iv) usar 2+ blocos em magnitudes diferentes de v para checar
    consistencia/obter barras de erro.

Reproduzir: python3 experiment_nested_anova.py
"""
import math
import statistics
import time
from multiprocessing import Pool

from experiment_headroom import measure_G_headroom


def _worker(v):
    return v, measure_G_headroom(v, 20000)


def compute_block(v0, m, n_workers=16):
    """Computa G(v) para v_j = v0 + 2j, j=0..3^m-1 (cobre cada residuo
    mod 3^m exatamente uma vez, ja que 2 e' invertivel mod 3^m)."""
    n_points = 3 ** m
    vs = [v0 + 2 * j for j in range(n_points)]
    with Pool(n_workers) as pool:
        results = pool.map(_worker, vs, chunksize=max(1, n_points // (n_workers * 8)))
    return {v: G for v, G in results if G is not None and G > 0}


def nested_variance_decomposition(log_g_by_v, m, max_t):
    """Para cada t=1..max_t, agrupa por v mod 3^t (excluindo v=0 mod 3
    do calculo inteiro) e calcula a variancia residual media (dentro de
    classe), com correcao de Bessel (ddof=1) por classe."""
    items = [(v, lg) for v, lg in log_g_by_v.items() if v % 3 != 0]
    print(f"  {len(items)} pontos nao-esteireis de {len(log_g_by_v)} totais no bloco.")

    total_var = statistics.variance([lg for _, lg in items])
    print(f"  Variancia total (t=0, sem condicionar): {total_var:.6f}\n")

    results = []
    for t in range(1, max_t + 1):
        mod_k = 3 ** t
        groups = {}
        for v, lg in items:
            groups.setdefault(v % mod_k, []).append(lg)
        weighted_var_sum = 0.0
        total_n = 0
        for r, vals in groups.items():
            n = len(vals)
            if n < 2:
                continue
            var_class = statistics.variance(vals)  # ja usa ddof=1 (statistics.variance)
            weighted_var_sum += var_class * n
            total_n += n
        resid_var = weighted_var_sum / total_n if total_n > 0 else None
        results.append((t, resid_var, len(groups), total_n))
    return total_var, results


def main():
    M = 11
    MAX_T = M - 4  # margem de seguranca contra o vies de amostra pequena (Fable)

    blocks = [
        ("bloco 1 (v0~1e11)", 10 ** 11 + 1),
        ("bloco 2 (v0~5e11)", 5 * 10 ** 11 + 1),
    ]

    all_results = {}
    for label, v0 in blocks:
        print(f"=== {label}: computando G(v) para 3^{M}={3**M} pontos consecutivos (v0={v0}) ===")
        t0 = time.time()
        G_by_v = compute_block(v0, M)
        print(f"  {len(G_by_v)} valores computados em {time.time()-t0:.1f}s")
        log_g_by_v = {v: math.log(G) for v, G in G_by_v.items()}
        total_var, results = nested_variance_decomposition(log_g_by_v, M, MAX_T)
        all_results[label] = results
        print(f"\n  {'t':>3} {'resid_var':>11} {'resid_std':>10} {'n_classes':>10} {'n_pontos':>9}")
        for t, rv, n_classes, n_pts in results:
            if rv is not None:
                print(f"  {t:>3} {rv:>11.6f} {math.sqrt(rv):>10.4f} {n_classes:>10} {n_pts:>9}")
        print()

    print("=== Comparacao entre blocos ===")
    print(f"{'t':>3}", end="")
    for label, _ in blocks:
        print(f" {label:>20}", end="")
    print()
    for i, t in enumerate(range(1, MAX_T + 1)):
        print(f"{t:>3}", end="")
        for label, _ in blocks:
            rv = all_results[label][i][1]
            print(f" {rv:>20.6f}" if rv is not None else f" {'N/A':>20}", end="")
        print()


if __name__ == "__main__":
    main()
