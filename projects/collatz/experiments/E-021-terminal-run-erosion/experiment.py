#!/usr/bin/env python3
"""
E-021 - Testa H-021: se n termina em run de t>=2 uns consecutivos em
binario, o passo acelerado tem valuacao a=1 e o resultado tem run terminal
de tamanho t-1 (erosao exata). Tambem compara distribuicao de runs entre
recordistas e orbitas tipicas.

Reproduzir: python3 experiment.py [N_TESTES]
"""
import sys
import random


def trailing_ones(n):
    count = 0
    while n & 1:
        count += 1
        n >>= 1
    return count


def step(n):
    m = 3 * n + 1
    a = 0
    while m % 2 == 0:
        m //= 2
        a += 1
    return m, a


def verify_erosion(n_tests, seed=1):
    rng = random.Random(seed)
    checked_by_t = {}
    failures = 0
    for _ in range(n_tests):
        t = rng.randint(2, 20)
        # construir um n com exatamente t uns terminais: (bits aleatorios)0 seguido de t uns
        prefix_bits = rng.randrange(1, 2 ** 10)  # bit t fica 0 por construcao (fora do prefixo e do run)
        n = (prefix_bits << (t + 1)) | ((1 << t) - 1)
        # garantir que o bit logo acima do run seja 0 (para o run ser EXATAMENTE t)
        assert trailing_ones(n) == t, f"construcao errada: trailing_ones={trailing_ones(n)} esperado {t}"

        m, a = step(n)
        checked_by_t[t] = checked_by_t.get(t, 0) + 1
        if a != 1 or trailing_ones(m) != t - 1:
            failures += 1
            if failures <= 5:
                print(f"  FALHA: n={n} (t={t}) -> m={m}, a={a} (esperado 1), "
                      f"trailing_ones(m)={trailing_ones(m)} (esperado {t-1})")
    return checked_by_t, failures


def orbit_run_lengths(n, max_steps=100_000):
    """Retorna lista de valuacoes a_i de toda a orbita (ate 1)."""
    vals = []
    while n != 1:
        n, a = step(n)
        vals.append(a)
        if len(vals) > max_steps:
            break
    return vals


def runs_of_ones(vals):
    """Comprimentos de runs consecutivos de a_i==1 na sequencia de valuacoes."""
    runs = []
    current = 0
    for a in vals:
        if a == 1:
            current += 1
        else:
            if current > 0:
                runs.append(current)
            current = 0
    if current > 0:
        runs.append(current)
    return runs


def main():
    n_tests = int(sys.argv[1]) if len(sys.argv) > 1 else 50_000

    print("=== (a) verificacao da regra de erosao ===")
    checked_by_t, failures = verify_erosion(n_tests)
    print(f"testes = {n_tests}, falhas = {failures}")
    print(f"distribuicao de t testados: {dict(sorted(checked_by_t.items()))}")
    print()

    print("=== (b) comparacao de runs (nao-terminais) entre recordistas e orbitas tipicas ===")
    try:
        with open("../E-004-true-record-holders/oeis_A006877_record_holders.txt") as f:
            records = [int(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        print("(arquivo de recordistas nao encontrado, pulando parte b)")
        return

    rec_runs = []
    for r in records:
        if r <= 2:
            continue
        vals = orbit_run_lengths(r)
        rec_runs.extend(runs_of_ones(vals))

    rng = random.Random(7)
    typ_runs = []
    for _ in range(200):
        n = rng.randrange(10 ** 6, 10 ** 12) | 1
        vals = orbit_run_lengths(n)
        typ_runs.extend(runs_of_ones(vals))

    mean_rec = sum(rec_runs) / len(rec_runs)
    mean_typ = sum(typ_runs) / len(typ_runs)
    print(f"recordistas: {len(rec_runs)} runs, media={mean_rec:.3f}")
    print(f"tipico:      {len(typ_runs)} runs, media={mean_typ:.3f}")
    print("(esperado sob H-001: geometrica com media 1, ja que P(a=1)=0.5 => E[run]=1/(1-0.5)=2... "
          "na verdade run de a=1's e geometrico com p=0.5 de PARAR, entao E[run]=1/0.5=2 aprox)")


if __name__ == "__main__":
    main()
