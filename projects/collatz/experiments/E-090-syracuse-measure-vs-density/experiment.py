#!/usr/bin/env python3
"""
E-090 - Testa a conexao proposta pelo modelo Fable: a medida de
Syracuse mu em Z_3 (identica a variavel aleatoria Syrac(Z/3^nZ) de
Tao 2022, Lemma 1.12, ja implementada e verificada em E-076) e a
densidade local exata de G(v)=D(v)*v (o residuo 3-adico de D(v)
identificado em H-086/H-087, depois de remover o termo trivial de
magnitude D(v)~C/v).

Fable validou a montagem (consulta desta sessao): a recursao de
Tao/Lemma 1.12 e EXATAMENTE a mesma equacao de auto-consistencia que
G deveria satisfazer (G(v) ~ soma_a 3*2^-a*G((2^a*v-1)/3)), entao a
conjectura testavel e: 3^m * mu_m(r) (a densidade local da medida,
escalada) deve ser proporcional a media de G(v) sobre v=r mod 3^m
(magnitude controlada, v nao multiplo de 3), com correlacao (em log)
crescendo com m.

Reaproveita a funcao syrac_distribution ja escrita e verificada em
E-076-tao-2022-review/experiment.py (calculada com Fraction exato para
m pequeno) e adiciona uma versao truncada em ponto flutuante
(a<=A_MAX) para m maior, mais barata computacionalmente - validada
contra a versao exata antes de usar.

Reproduzir: python3 experiment.py
"""
import sys
import os
import math
import random
import importlib.util
from fractions import Fraction

_here = os.path.dirname(os.path.abspath(__file__))


def _load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_tao_mod = _load_module(
    "e076_experiment",
    os.path.join(_here, "..", "E-076-tao-2022-review", "experiment.py"),
)
_dfs_mod = _load_module(
    "e018_experiment_dfs",
    os.path.join(_here, "..", "E-018-reverse-tree-branching", "experiment_dfs.py"),
)

syrac_distribution = _tao_mod.syrac_distribution
build_tree_count_dfs = _dfs_mod.build_tree_count_dfs


def syrac_distribution_float(m, a_max=64):
    """Versao truncada em ponto flutuante da recursao de Tao/Lemma 1.12
    - equivalente a syrac_distribution(m) mas com a limitado a a_max
    (erro por estado < 2^-a_max) em vez de somar exatamente ate 2*3^(m-1)
    com Fraction - MUITO mais barato para m grande."""
    dist = {0: 1.0}
    for level in range(m):
        modulus = 3 ** (level + 1)
        prev_modulus = 3 ** level
        new_dist = {x: 0.0 for x in range(modulus)}
        for x in range(modulus):
            if x % 3 == 0:
                continue  # sempre 0, nao precisa somar
            total = 0.0
            weight_sum = 0.0
            for a in range(1, a_max + 1):
                if (pow(2, a, 3) * x) % 3 == 1:
                    full = (2 ** a) * x - 1
                    assert full % 3 == 0
                    reduced = (full // 3) % prev_modulus
                    prob_prev = dist.get(reduced, 0.0)
                    w = 2.0 ** (-a)
                    total += w * prob_prev
                    weight_sum += w
            # normaliza pela soma dos pesos ja somados (aproxima o
            # denominador exato 1-2^-(2*3^(level)) que ~1 para a_max grande)
            new_dist[x] = total
        # renormaliza a distribuicao inteira para somar exatamente 1
        s = sum(new_dist.values())
        if s > 0:
            for x in new_dist:
                new_dist[x] /= s
        dist = new_dist
    return dist


def validate_float_version():
    """Confere a versao truncada/float contra a versao exata (Fraction)
    ja verificada em E-076, para m=1,2."""
    print("Validando versao truncada (float) contra a versao exata (Fraction, ja verificada em E-076):")
    for m in (1, 2):
        exact = syrac_distribution(m)
        approx = syrac_distribution_float(m, a_max=64)
        max_diff = max(abs(float(exact[x]) - approx[x]) for x in exact)
        print(f"  m={m}: diferenca maxima entre exato e truncado = {max_diff:.2e}")
    print()


def measure_G(v, n_max, mult=5):
    """G(v) = D(v)*v (residuo 3-adico depois de remover o termo trivial
    de magnitude, H-086/H-087)."""
    search_bound = n_max * mult
    total, odd, max_gen = build_tree_count_dfs(v, n_max, search_bound)
    D = odd / n_max if n_max > 0 else None
    if D is None or D <= 0:
        return None
    return D * v


def sample_odd_with_residue(rng, mod_k, target_residue, log_mag_lo, log_mag_hi, max_tries=5000):
    for _ in range(max_tries):
        log_mag = rng.uniform(log_mag_lo, log_mag_hi)
        mag = int(10 ** log_mag)
        if mag < mod_k:
            continue
        base = (mag // mod_k) * mod_k + target_residue
        if base < mag:
            base += mod_k
        v = base
        if v % 2 == 1 and v % 3 != 0:
            return v
    return None


def measure_mean_G_by_residue(m, n_samples_per_residue, log_mag_lo, log_mag_hi, seed=1):
    """Para cada residuo r mod 3^m com r%3!=0, amostra v's com esse
    residuo (magnitude controlada) e mede a media geometrica de G(v)."""
    rng = random.Random(seed)
    mod_k = 3 ** m
    results = {}
    for r in range(mod_k):
        if r % 3 == 0:
            continue
        logs = []
        for _ in range(n_samples_per_residue):
            v = sample_odd_with_residue(rng, mod_k, r, log_mag_lo, log_mag_hi)
            if v is None:
                continue
            n_max = v * 20
            G = measure_G(v, n_max)
            if G is not None and G > 0:
                logs.append(math.log10(G))
        if logs:
            mean_log = sum(logs) / len(logs)
            results[r] = 10 ** mean_log
    return results


def log_log_correlation(xs, ys):
    """Correlacao de Pearson entre log(xs) e log(ys)."""
    logs_x = [math.log10(x) for x in xs]
    logs_y = [math.log10(y) for y in ys]
    n = len(logs_x)
    mean_x = sum(logs_x) / n
    mean_y = sum(logs_y) / n
    cov = sum((x - mean_x) * (y - mean_y) for x, y in zip(logs_x, logs_y)) / n
    var_x = sum((x - mean_x) ** 2 for x in logs_x) / n
    var_y = sum((y - mean_y) ** 2 for y in logs_y) / n
    if var_x == 0 or var_y == 0:
        return None
    return cov / math.sqrt(var_x * var_y)


def test_correlation_for_m(m, n_samples_per_residue, log_mag_lo, log_mag_hi, a_max=64, seed=1):
    """Testa a correlacao entre 3^m*mu_m(r) (densidade local da medida
    de Syracuse) e a media geometrica de G(v) medida computacionalmente,
    sobre todos os residuos r mod 3^m com r%3!=0."""
    mu = syrac_distribution_float(m, a_max=a_max)
    mean_G = measure_mean_G_by_residue(m, n_samples_per_residue, log_mag_lo, log_mag_hi, seed=seed)

    common_r = sorted(set(mu.keys()) & set(mean_G.keys()))
    common_r = [r for r in common_r if r % 3 != 0 and mu[r] > 0]

    mod_k = 3 ** m
    xs = [mod_k * mu[r] for r in common_r]  # densidade local escalada
    ys = [mean_G[r] for r in common_r]

    if len(xs) < 5:
        return None, len(xs)

    corr = log_log_correlation(xs, ys)
    return corr, len(xs), list(zip(common_r, xs, ys))


def main():
    validate_float_version()

    print("=== Correlacao log-log entre 3^m*mu_m(r) (medida de Syracuse) e G(v) medido ===")
    print("(magnitude controlada, v nao multiplo de 3)")
    print()

    for m in [2, 3, 4]:
        n_per_residue = 8
        log_mag_lo, log_mag_hi = 5.0, 6.0
        corr, n_pts, pairs = test_correlation_for_m(m, n_per_residue, log_mag_lo, log_mag_hi)
        print(f"m={m} (mod 3^{m}={3**m}): correlacao log-log = {corr}, n_residuos={n_pts}")
        if m == 2 and pairs:
            print("  detalhe (r, 9*mu(r), G_medio(v)):")
            for r, x, y in sorted(pairs):
                print(f"    r={r}: 9*mu={x:.4f}  G_medio={y:.4f}")
        print()


if __name__ == "__main__":
    main()
