#!/usr/bin/env python3
"""
E-002 - Testa H-002: outliers de stopping time (tempo total de queda ate 1,
relativo ao tamanho de n) compartilham estrutura residual (mod potencias de 2 e
de 3) que os diferencia da populacao tipica do mesmo intervalo?

Nota metodologica (licao de E-001): aqui cada observacao e uma caracteristica do
proprio numero inicial n (residuo, stopping time), nao uma posicao dentro de uma
orbita compartilhada - entao a armadilha de colisao de orbitas (pseudo-replicacao
por cauda compartilhada) NAO se aplica da mesma forma. Cada n no intervalo e uma
observacao legitima e distinta, mesmo que orbitas de n's diferentes convirjam
depois.

Metrica de outlier: total_steps(n) / log2(n), onde total_steps e o numero de
passos do mapa PADRAO (nao acelerado: n/2 se par, 3n+1 se impar) ate atingir 1.
Calculado de forma barata reaproveitando a orbita acelerada (cada passo acelerado
de valuacao a custa exatamente 1+a passos no mapa padrao).

Reproduzir: python3 experiment.py [N_MAX_IMPAR] [PERCENTIL_OUTLIER] [SEED]
"""
import sys
import math
import random


def orbit_info(n, max_steps=1_000_000):
    """Retorna (total_steps no mapa padrao, lista de valuacoes a_i)."""
    total_steps = 0
    vals = []
    while n != 1:
        m = 3 * n + 1
        a = 0
        while m % 2 == 0:
            m //= 2
            a += 1
        vals.append(a)
        total_steps += 1 + a
        n = m
        if len(vals) > max_steps:
            raise RuntimeError("orbita suspeita de nao convergir")
    return total_steps, vals


def run_length_of_ones(vals):
    """Quantos a_i==1 consecutivos no INICIO da orbita (proxy de descida lenta)."""
    c = 0
    for a in vals:
        if a == 1:
            c += 1
        else:
            break
    return c


def chi_square_pvalue(x, k):
    if k <= 0:
        return float("nan")
    z = ((x / k) ** (1 / 3) - (1 - 2 / (9 * k))) / math.sqrt(2 / (9 * k))
    return 0.5 * math.erfc(z / math.sqrt(2))


def homogeneity_chi2(group_a_residues, group_b_residues, modulus):
    """Tabela de contingencia 2 x modulus (grupo x classe de residuo)."""
    counts_a = [0] * modulus
    counts_b = [0] * modulus
    for r in group_a_residues:
        counts_a[r] += 1
    for r in group_b_residues:
        counts_b[r] += 1

    n_a = len(group_a_residues)
    n_b = len(group_b_residues)
    n_total = n_a + n_b

    chi2 = 0.0
    for c in range(modulus):
        col_total = counts_a[c] + counts_b[c]
        if col_total == 0:
            continue
        expected_a = n_a * col_total / n_total
        expected_b = n_b * col_total / n_total
        if expected_a > 0:
            chi2 += (counts_a[c] - expected_a) ** 2 / expected_a
        if expected_b > 0:
            chi2 += (counts_b[c] - expected_b) ** 2 / expected_b
    dof = modulus - 1
    return chi2, dof, chi_square_pvalue(chi2, dof) if dof > 0 else float("nan")


def main():
    n_max_odd = int(sys.argv[1]) if len(sys.argv) > 1 else 2_000_000
    percentile = float(sys.argv[2]) if len(sys.argv) > 2 else 0.995  # top 0.5%
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 42

    rng = random.Random(seed)

    records = []  # (n, ratio, vals, run1)
    for n in range(3, n_max_odd, 2):
        total_steps, vals = orbit_info(n)
        ratio = total_steps / math.log2(n)
        records.append((n, ratio, vals))

    records.sort(key=lambda r: r[1])
    cutoff_idx = int(len(records) * percentile)
    typical_pool = records[:cutoff_idx]
    outliers = records[cutoff_idx:]

    print(f"n_max (impar) = {n_max_odd}, total de n analisados = {len(records)}")
    print(f"percentil de corte = {percentile} -> {len(outliers)} outliers")
    print(f"ratio (total_steps/log2(n)) minimo entre outliers = {outliers[0][1]:.3f}")
    print(f"ratio maximo geral = {records[-1][1]:.3f} (n={records[-1][0]})")
    print()

    # grupo "tipico" balanceado: amostra aleatoria do mesmo tamanho que outliers
    typical_sample = rng.sample(typical_pool, min(len(outliers), len(typical_pool)))

    print(f"grupo outliers: {len(outliers)}   grupo tipico (amostrado): {len(typical_sample)}")
    print()

    # --- estrutura residual mod potencias de 2 e 3 ---
    for modulus in [4, 8, 16, 32, 64, 3, 9, 27]:
        res_out = [n % modulus for n, _, _ in outliers]
        res_typ = [n % modulus for n, _, _ in typical_sample]
        chi2, dof, p = homogeneity_chi2(res_out, res_typ, modulus)
        sig = "***" if p < 0.01 else ("*" if p < 0.05 else "")
        print(f"  residuo mod {modulus:3d}: chi2={chi2:7.2f} dof={dof:3d} p={p:.3e} {sig}")
    print()

    # --- comprimento da corrida inicial de a_i == 1 (proxy mecanico, esperado tautologico) ---
    run1_out = [run_length_of_ones(vals) for _, _, vals in outliers]
    run1_typ = [run_length_of_ones(vals) for _, _, vals in typical_sample]
    mean_out = sum(run1_out) / len(run1_out)
    mean_typ = sum(run1_typ) / len(run1_typ)
    print(f"corrida inicial de a_i=1 -- media outliers={mean_out:.3f}  media tipico={mean_typ:.3f}")
    print("(esperado tautologico: outliers tem descida inicial mais lenta quase por definicao,")
    print(" e isso mecanicamente restringe os bits baixos de n mod 2^k)")
    print()

    # --- controle: mesma analise, mas condicionando em run1 fixo ---
    # remove a explicacao tautologica (run1 mais longo -> bits baixos de n restritos)
    # e testa se sobra ALGUMA estrutura residual alem disso.
    print("=== controle: condicionando em run1 fixo (remove confounder tautologico) ===")
    for fixed_run1 in [1, 2]:
        out_cond = [(n, vals) for n, _, vals in outliers if run_length_of_ones(vals) == fixed_run1]
        typ_cond = [(n, vals) for n, _, vals in typical_sample if run_length_of_ones(vals) == fixed_run1]
        if len(out_cond) < 20 or len(typ_cond) < 20:
            print(f"  run1={fixed_run1}: amostra insuficiente (outliers={len(out_cond)}, tipico={len(typ_cond)}), pulando.")
            continue
        print(f"  run1={fixed_run1} (outliers={len(out_cond)}, tipico={len(typ_cond)}):")
        for modulus in [8, 16, 32, 64, 3, 9, 27]:
            res_out = [n % modulus for n, _ in out_cond]
            res_typ = [n % modulus for n, _ in typ_cond]
            chi2, dof, p = homogeneity_chi2(res_out, res_typ, modulus)
            sig = "***" if p < 0.01 else ("*" if p < 0.05 else "")
            print(f"    residuo mod {modulus:3d}: chi2={chi2:7.2f} dof={dof:3d} p={p:.3e} {sig}")


if __name__ == "__main__":
    main()
