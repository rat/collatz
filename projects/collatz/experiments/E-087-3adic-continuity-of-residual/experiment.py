#!/usr/bin/env python3
"""
E-087 - Testa continuidade 3-adica do RESIDUO G(v) = D(v)*v (depois de
remover o termo trivial de magnitude D(v)~C/v encontrado em H-086),
em vez de testar D(v) bruto como H-024 fez originalmente.

Motivacao: H-086 mostrou que quase toda a variacao de 300x que H-024
atribuiu a "profundidade 3-adica infinita" era na verdade o termo
arquimediano D(v)~C/v. O que sobra (~1.26x de variacao) pode ou nao
ter estrutura 3-adica genuina - este experimento testa isso
diretamente, de forma metodologicamente correta (evitando o erro que
o Fable apontou em H-024): para cada nivel de precisao K (residuo mod
3^K), sorteamos v com ESSE residuo fixo mas MAGNITUDE VARIANDO
LIVREMENTE por varias ordens de grandeza - e medimos a VARIANCIA de
log10(G(v)) entre essas amostras.

Interpretacao:
- Se a variancia de log10(G(v)) DIMINUI conforme K cresce (mais
  digitos base-3 fixados), G se comporta como funcao (aproximadamente)
  continua do inteiro 3-adico v - abre a porta para expansao de
  Mahler (ideia 1 do Fable) ou a medida de Syracuse em Z_3 (ideia 2).
- Se a variancia NAO diminui com K (fica no mesmo patamar,
  independente de quantos digitos fixamos), G nao e uma funcao
  continua do 3-adico v no sentido usual - seria mais parecido com um
  campo aleatorio indexado por v, sem estrutura de continuidade a
  explorar por essa via.

Reproduzir: python3 experiment.py
"""
import sys
import math
import random

sys.path.insert(0, "../E-018-reverse-tree-branching")
from experiment_dfs import build_tree_count_dfs


def measure_D(v, n_max, mult=5):
    search_bound = n_max * mult
    total, odd, max_gen = build_tree_count_dfs(v, n_max, search_bound)
    return odd / n_max if n_max > 0 else None


def measure_G(v, n_max, mult=5):
    """G(v) = D(v) * v - o residuo depois de remover o termo trivial
    de magnitude D(v)~C/v encontrado em H-086."""
    D = measure_D(v, n_max, mult)
    if D is None or D <= 0:
        return None
    return D * v


def sample_odd_with_residue(rng, mod_k, target_residue, log_mag_lo, log_mag_hi, max_tries=20000):
    """Sorteia um v impar, nao-esteril (v%3!=0), com v % mod_k ==
    target_residue, com magnitude log-uniforme entre 10^log_mag_lo e
    10^log_mag_hi."""
    for _ in range(max_tries):
        log_mag = rng.uniform(log_mag_lo, log_mag_hi)
        mag = int(10 ** log_mag)
        if mag < mod_k:
            continue
        # ajusta para o proximo v >= mag com o residuo certo
        base = (mag // mod_k) * mod_k + target_residue
        if base < mag:
            base += mod_k
        v = base
        if v % 2 == 1 and v % 3 != 0:
            return v
    return None


def test_variance_vs_K(K_values, n_samples=25, log_mag_lo=2, log_mag_hi=7, seed=1):
    """Para cada K, fixa um residuo mod 3^K (escolhido de forma
    NESTED - ou seja, cada K usa o mesmo 'prefixo' 3-adico dos K
    anteriores, aproximando um unico inteiro 3-adico), sorteia varios
    v com esse residuo e magnitude log-uniforme livre, mede G(v), e
    calcula a variancia de log10(G(v))."""
    rng = random.Random(seed)

    # constroi um residuo NESTED: comeca com um digito base-3 e vai
    # acrescentando digitos aleatorios (mas fixos, uma vez escolhidos)
    # de forma que o residuo mod 3^(K+1) seja consistente com mod 3^K
    # o primeiro digito (mod 3) NAO PODE ser 0 - isso daria uma classe
    # esteril inteira (v%3==0), onde nenhum v e valido (nao-esteril por
    # definicao). Fixamos o primeiro digito em 1 ou 2 (nao-esteril) e
    # deixamos os digitos mais profundos (que refinam o residuo sem
    # alterar mod3) livres.
    digit_rng = random.Random(seed + 1000)
    residue_digits = [digit_rng.choice([1, 2])]

    results = {}
    for K in sorted(K_values):
        while len(residue_digits) < K:
            residue_digits.append(digit_rng.randrange(3))
        mod_k = 3 ** K
        target_residue = sum(d * (3 ** i) for i, d in enumerate(residue_digits))
        # garante v impar: ajusta o residuo para ser impar somando mod_k se necessario
        # (residuo mod 3^K nao determina paridade sozinho, entao aceitamos qualquer
        # residuo e filtramos por impar na amostragem via ajuste de base)
        logs = []
        for _ in range(n_samples):
            v = sample_odd_with_residue(rng, mod_k, target_residue, log_mag_lo, log_mag_hi)
            if v is None:
                continue
            n_max = v * 20
            G = measure_G(v, n_max)
            if G is not None and G > 0:
                logs.append(math.log10(G))

        if len(logs) >= 5:
            mean_log = sum(logs) / len(logs)
            var_log = sum((x - mean_log) ** 2 for x in logs) / len(logs)
            std_log = math.sqrt(var_log)
        else:
            std_log = None
        results[K] = (len(logs), std_log)
        print(f"  K={K:2d} (mod 3^{K}={mod_k}), residuo={target_residue}: "
              f"{len(logs)} amostras validas, desvio_log10(G) = {std_log}")
    return results


def main():
    print("=== Continuidade 3-adica de G(v)=D(v)*v: variancia vs. numero de digitos fixados (K) ===")
    print("(residuo mod 3^K NESTED - cada K refina o anterior; magnitude livre em [10^2, 10^7])")
    print("(repetido com 5 SEEDS/cadeias de residuo independentes, para nao confiar numa unica")
    print(" cadeia - mesmo cuidado que ja derrubou a falsa hipotese mod9 antes nesta sessao)")
    print()

    K_values = [1, 2, 4, 6, 8]
    all_results = {K: [] for K in K_values}
    for seed in range(1, 6):
        print(f"--- seed {seed} ---")
        results = test_variance_vs_K(K_values=K_values, n_samples=15, seed=seed)
        for K, (n, std) in results.items():
            if std is not None:
                all_results[K].append(std)
        print()

    print("=== Resumo agregado (media +- desvio-padrao do desvio, sobre 5 cadeias) ===")
    for K in K_values:
        vals = all_results[K]
        if vals:
            mean_v = sum(vals) / len(vals)
            if len(vals) > 1:
                var_v = sum((x - mean_v) ** 2 for x in vals) / len(vals)
                std_v = math.sqrt(var_v)
            else:
                std_v = 0.0
            print(f"  K={K}: media do desvio_log10(G) = {mean_v:.4f} +- {std_v:.4f}  (n_cadeias={len(vals)})")
        else:
            print(f"  K={K}: sem dados validos")


if __name__ == "__main__":
    main()
