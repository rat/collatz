#!/usr/bin/env python3
"""
E-089 - Reteste corrigido de H-026 ("K maior atrasa a divergencia de
memoria finita?"), seguindo o desenho proposto pelo modelo Fable apos
ele apontar que H-026 original testou a variavel errada (D(v) bruto,
dominado pelo termo trivial de magnitude D~C/v de H-024/H-086) em vez
do residuo G(v)=D(v)*v que de fato mostra continuidade 3-adica (H-087).

Desenho corrigido (analogo a E-087, mas testando a pergunta especifica
de H-026 - K maior reduz a DISPERSAO de G dentro de uma janela de
magnitude?):
- Variavel: log10(G(v)) = log10(D(v)*v).
- Fatores: K em {2,4,6,8} x faixas de magnitude B (janelas log-largas).
- Amostragem: N amostras por celula (cadeia, K, B), residuo mod 3^K
  fixo (nested entre K's), magnitude log-uniforme dentro da janela.
- Replicacao: multiplas cadeias de residuo independentes (sementes
  diferentes), reportando media +- desvio entre cadeias - nunca uma
  cadeia so (mesmo cuidado que ja evitou a falsa hipotese mod9).
- Metrica: dispersao (desvio-padrao de log10 G) POR CELULA (K, faixa),
  nao uma unica medicao - responde a pergunta certa: K maior comprime
  a dispersao de G dentro da mesma janela de magnitude?

Reproduzir: python3 experiment.py
"""
import sys
import math
import random

sys.path.insert(0, "../E-018-reverse-tree-branching")
from experiment_dfs import build_tree_count_dfs


def measure_G(v, n_max, mult=5):
    """G(v) = D(v)*v, o residuo depois de remover o termo trivial de
    magnitude D(v)~C/v (H-086)."""
    search_bound = n_max * mult
    total, odd, max_gen = build_tree_count_dfs(v, n_max, search_bound)
    D = odd / n_max if n_max > 0 else None
    if D is None or D <= 0:
        return None
    return D * v


def build_nested_residue(K_max, seed):
    """Constroi uma cadeia de digitos base-3 nested: o primeiro digito
    (mod3) e sempre 1 ou 2 (nao-esteril), os seguintes sao livres -
    garante que o residuo mod 3^K para qualquer K<=K_max e consistente
    (prefixo do mesmo inteiro 3-adico)."""
    rng = random.Random(seed)
    digits = [rng.choice([1, 2])]
    while len(digits) < K_max:
        digits.append(rng.randrange(3))
    return digits


def residue_mod_3K(digits, K):
    return sum(d * (3 ** i) for i, d in enumerate(digits[:K]))


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


def measure_dispersion_in_window(K, digits, log_mag_lo, log_mag_hi, n_samples, seed):
    """Para um K e janela de magnitude fixos, amostra n_samples valores
    DISTINTOS de v com o mesmo residuo mod 3^K (derivado de digits),
    mede G(v), e retorna o desvio-padrao de log10(G) dentro dessa
    janela+K. Retorna None se a janela nao contiver valores distintos
    suficientes (evita o artefato de "janela degenerada" - se o
    espacamento mod 3^K exceder a largura da janela, so existe 1 valor
    possivel e a dispersao medida seria zero por amostragem repetida,
    nao por um resultado real)."""
    rng = random.Random(seed)
    mod_k = 3 ** K
    target_residue = residue_mod_3K(digits, K)

    # verifica quantos valores DISTINTOS com esse residuo existem na janela
    mag_lo, mag_hi = int(10 ** log_mag_lo), int(10 ** log_mag_hi)
    n_distinct_possible = max(0, (mag_hi - mag_lo) // mod_k)
    if n_distinct_possible < n_samples:
        return None, 0  # janela degenerada para este K - nao mede nada

    seen_v = set()
    logs = []
    attempts = 0
    while len(logs) < n_samples and attempts < n_samples * 50:
        attempts += 1
        v = sample_odd_with_residue(rng, mod_k, target_residue, log_mag_lo, log_mag_hi)
        if v is None or v in seen_v:
            continue
        seen_v.add(v)
        n_max = v * 20
        G = measure_G(v, n_max)
        if G is not None and G > 0:
            logs.append(math.log10(G))
    if len(logs) < 5:
        return None, len(logs)
    mean_log = sum(logs) / len(logs)
    var_log = sum((x - mean_log) ** 2 for x in logs) / len(logs)
    return math.sqrt(var_log), len(logs)


def main():
    K_values = [2, 4, 6, 8]
    # janelas largas o suficiente para conter multiplos valores distintos
    # mesmo para K=8 (mod 3^8=6561): janela [1e6,1e6.6) tem largura ~3e6,
    # ainda dando ~450 valores distintos possiveis por residuo - seguro.
    windows = [(6.0, 6.6), (7.0, 7.6), (8.0, 8.6)]
    n_chains = 5
    n_samples_per_cell = 12

    print("=== Teste corrigido de H-026: dispersao de log10(G) por K, em janelas de magnitude estreitas ===")
    print(f"({n_chains} cadeias de residuo independentes, {n_samples_per_cell} amostras por celula)")
    print()

    # agrega por K (media sobre janelas e cadeias)
    agg_by_K = {K: [] for K in K_values}

    for K in K_values:
        print(f"--- K={K} (mod 3^{K}={3**K}) ---")
        for lo, hi in windows:
            stds = []
            for chain in range(1, n_chains + 1):
                digits = build_nested_residue(max(K_values), seed=1000 * chain + K)
                std, n = measure_dispersion_in_window(K, digits, lo, hi, n_samples_per_cell,
                                                        seed=2000 * chain + K)
                if std is not None:
                    stds.append(std)
            if stds:
                mean_std = sum(stds) / len(stds)
                agg_by_K[K].append(mean_std)
                print(f"  janela log10(v) in [{lo},{hi}): desvio medio (sobre {len(stds)} cadeias) = {mean_std:.4f}")
            else:
                print(f"  janela log10(v) in [{lo},{hi}): sem dados suficientes")
        print()

    print("=== Resumo: dispersao media de log10(G) por K (agregando todas as janelas) ===")
    for K in K_values:
        vals = agg_by_K[K]
        if vals:
            print(f"  K={K}: dispersao media = {sum(vals)/len(vals):.4f}  (n_janelas={len(vals)})")
        else:
            print(f"  K={K}: sem dados")

    print()
    print("Interpretacao: se a dispersao CAI conforme K aumenta (mesmo dentro de")
    print("janelas de magnitude bem controladas), confirma que K maior de fato")
    print("'aguenta mais' - a pergunta original de H-026, agora testada sobre a")
    print("variavel certa (G, nao D bruto).")


if __name__ == "__main__":
    main()
