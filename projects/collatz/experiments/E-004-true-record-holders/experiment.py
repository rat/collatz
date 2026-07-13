#!/usr/bin/env python3
"""
E-004 - Testa H-004: recordistas REAIS de stopping time (n tal que
total_stopping_time(n) > total_stopping_time(m) para todo m < n - a definicao
padrao da literatura, tipo tabela de Roosendaal) tem estrutura alem do
tautologico ja identificado em E-002?

Dois testes:
(a) Replica mod-2^k / mod-3^k / mod-primos-nao-relacionados (5,7,11,13) como
    controle, nos recordistas reais.
(b) Testa autocorrelacao lag-1 INTERNA da propria orbita de cada recordista
    (nao redutivel a residuo mod 2^k) contra uma amostra tipica de orbitas
    igualmente longas.

Reproduzir: python3 experiment.py [LIMIT] [MIN_LEN_AUTOCORR] [SEED]
"""
import sys
import math
import random


def orbit_info(n):
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
    return total_steps, vals


def total_steps_only(n):
    total_steps = 0
    while n != 1:
        m = 3 * n + 1
        while m % 2 == 0:
            m //= 2
            total_steps += 1
        total_steps += 1
        n = m
    return total_steps


def chi_square_pvalue(x, k):
    if k <= 0:
        return float("nan")
    z = ((x / k) ** (1 / 3) - (1 - 2 / (9 * k))) / math.sqrt(2 / (9 * k))
    return 0.5 * math.erfc(z / math.sqrt(2))


def normal_pvalue_two_sided(z):
    return math.erfc(abs(z) / math.sqrt(2))


def homogeneity_chi2(group_a_residues, group_b_residues, modulus):
    """Retorna (chi2, dof, p, valido). valido=False se a contagem esperada media
    por celula for < 5 (regra pratica para a aproximacao qui-quadrado ser confiavel)."""
    counts_a = [0] * modulus
    counts_b = [0] * modulus
    for r in group_a_residues:
        counts_a[r] += 1
    for r in group_b_residues:
        counts_b[r] += 1
    n_a, n_b = len(group_a_residues), len(group_b_residues)
    n_total = n_a + n_b
    chi2 = 0.0
    min_expected = float("inf")
    for c in range(modulus):
        col_total = counts_a[c] + counts_b[c]
        if col_total == 0:
            min_expected = 0
            continue
        expected_a = n_a * col_total / n_total
        expected_b = n_b * col_total / n_total
        min_expected = min(min_expected, expected_a, expected_b)
        if expected_a > 0:
            chi2 += (counts_a[c] - expected_a) ** 2 / expected_a
        if expected_b > 0:
            chi2 += (counts_b[c] - expected_b) ** 2 / expected_b
    dof = modulus - 1
    p = chi_square_pvalue(chi2, dof) if dof > 0 else float("nan")
    valido = min_expected >= 5
    return chi2, dof, p, valido


def lag1_autocorr(vals):
    """Correlacao de Pearson interna entre vals[:-1] e vals[1:] de UMA orbita."""
    xs, ys = vals[:-1], vals[1:]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / n
    vx = sum((x - mx) ** 2 for x in xs) / n
    vy = sum((y - my) ** 2 for y in ys) / n
    if vx == 0 or vy == 0:
        return None
    return cov / math.sqrt(vx * vy)


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 5_000_000
    min_len_autocorr = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 42
    rng = random.Random(seed)

    # --- passo 1: encontrar recordistas reais ---
    record_holders = []
    best = -1
    for n in range(1, limit, 2):
        ts = total_steps_only(n)
        if ts > best:
            best = ts
            record_holders.append(n)

    print(f"limite = {limit}, recordistas encontrados = {len(record_holders)}")
    print(f"primeiros recordistas: {record_holders[:10]}")
    print(f"ultimos recordistas: {record_holders[-10:]}")
    print()

    # --- amostra tipica (nao-recordista) para comparacao ---
    record_set = set(record_holders)
    typical_pool = []
    while len(typical_pool) < len(record_holders) * 20:
        n = rng.randrange(1, limit) | 1
        if n not in record_set:
            typical_pool.append(n)

    # --- teste (a): residuo mod 2^k, 3^k, primos nao relacionados ---
    print("=== (a) residuo: recordistas vs amostra tipica ===")
    for modulus in [4, 8, 16, 32, 64, 3, 9, 27, 5, 7, 11, 13]:
        res_rec = [n % modulus for n in record_holders]
        res_typ = [n % modulus for n in typical_pool]
        chi2, dof, p, valido = homogeneity_chi2(res_rec, res_typ, modulus)
        familia = "2^k" if modulus in (4, 8, 16, 32, 64) else ("3^k" if modulus in (3, 9, 27) else "primo n/relacionado")
        if not valido:
            print(f"  mod {modulus:3d} ({familia:>18}): AMOSTRA INSUFICIENTE (celula esperada < 5) - resultado nao confiavel")
            continue
        sig = "***" if p < 0.01 else ("*" if p < 0.05 else "")
        print(f"  mod {modulus:3d} ({familia:>18}): chi2={chi2:7.2f} dof={dof:3d} p={p:.3e} {sig}")
    print()

    # --- teste (b): autocorrelacao interna lag-1, recordistas vs tipico de orbita comparavel ---
    print(f"=== (b) autocorrelacao lag-1 interna (orbitas com >= {min_len_autocorr} passos) ===")
    rec_data = []  # (length, autocorr)
    for n in record_holders:
        _, vals = orbit_info(n)
        if len(vals) >= min_len_autocorr:
            r = lag1_autocorr(vals)
            if r is not None:
                rec_data.append((len(vals), r))

    typ_data = []
    for n in typical_pool:
        _, vals = orbit_info(n)
        if len(vals) >= min_len_autocorr:
            r = lag1_autocorr(vals)
            if r is not None:
                typ_data.append((len(vals), r))
        if len(typ_data) >= max(len(rec_data) * 15, 300):
            break

    print(f"  recordistas com orbita longa o suficiente: {len(rec_data)}")
    print(f"  amostra tipica com orbita longa o suficiente: {len(typ_data)}")

    if len(rec_data) < 5 or len(typ_data) < 5:
        print("  amostra insuficiente para comparar (aumente o limite ou reduza min_len_autocorr).")
        return

    rec_lens = [l for l, _ in rec_data]
    typ_lens = [l for l, _ in typ_data]
    rec_autocorrs = [r for _, r in rec_data]
    typ_autocorrs = [r for _, r in typ_data]

    mean_len_rec = sum(rec_lens) / len(rec_lens)
    mean_len_typ = sum(typ_lens) / len(typ_lens)
    print(f"  comprimento medio de orbita -- recordistas={mean_len_rec:.1f}  tipico={mean_len_typ:.1f}")
    print("  (recordistas tem orbitas mais longas por definicao - checar se isso e um confounder)")
    print()

    # comparacao ingenua (sem controlar comprimento)
    mean_rec = sum(rec_autocorrs) / len(rec_autocorrs)
    mean_typ = sum(typ_autocorrs) / len(typ_autocorrs)
    var_rec = sum((x - mean_rec) ** 2 for x in rec_autocorrs) / (len(rec_autocorrs) - 1)
    var_typ = sum((x - mean_typ) ** 2 for x in typ_autocorrs) / (len(typ_autocorrs) - 1)
    se = math.sqrt(var_rec / len(rec_autocorrs) + var_typ / len(typ_autocorrs))
    z = (mean_rec - mean_typ) / se if se > 0 else float("nan")
    p_diff = normal_pvalue_two_sided(z)
    print(f"  [ingenuo, SEM controlar comprimento] media rec={mean_rec:.4f}  media tip={mean_typ:.4f}")
    print(f"  z = {z:.3f}, p = {p_diff:.3e}")
    print()

    # controle: regressao autocorr ~ a + b/(length-1) usando SO o grupo tipico
    # (formula motivada pelo vies conhecido de autocorrelacao amostral em series i.i.d. curtas),
    # depois testar se o residuo dos recordistas (autocorr observado - previsto pelo seu proprio
    # comprimento, segundo o modelo ajustado nos tipicos) e diferente de zero.
    xs = [1.0 / (l - 1) for l in typ_lens]
    ys = typ_autocorrs
    n_typ = len(xs)
    mean_x = sum(xs) / n_typ
    mean_y = sum(ys) / n_typ
    sxx = sum((x - mean_x) ** 2 for x in xs)
    sxy = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    b = sxy / sxx if sxx > 0 else 0.0
    a = mean_y - b * mean_x

    print(f"  modelo ajustado no grupo tipico: autocorr ~= {a:.4f} + {b:.4f} * 1/(L-1)")
    residuals = []
    for l, r in rec_data:
        predicted = a + b * (1.0 / (l - 1))
        residuals.append(r - predicted)

    mean_resid = sum(residuals) / len(residuals)
    var_resid = sum((x - mean_resid) ** 2 for x in residuals) / (len(residuals) - 1)
    se_resid = math.sqrt(var_resid / len(residuals))
    z_resid = mean_resid / se_resid if se_resid > 0 else float("nan")
    p_resid = normal_pvalue_two_sided(z_resid)
    print(f"  [controlado por comprimento] residuo medio dos recordistas = {mean_resid:.4f}")
    print(f"  z = {z_resid:.3f}, p = {p_resid:.3e}")
    if p_resid < 0.01:
        print("  => MESMO controlando o comprimento da orbita, recordistas tem autocorrelacao")
        print("     maior que o previsto - diferenca parece real, nao so viés de amostra curta.")
    else:
        print("  => apos controlar o comprimento, a diferenca deixa de ser significativa -")
        print("     o resultado ingenuo provavelmente era so o vies de comprimento de amostra.")


if __name__ == "__main__":
    main()
