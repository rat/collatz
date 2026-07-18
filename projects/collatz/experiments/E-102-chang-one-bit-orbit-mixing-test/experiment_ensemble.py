#!/usr/bin/env python3
"""
Teste computacional da conjectura remanescente de Chang (2026,
arXiv:2603.25753), "A Structural Reduction of the Collatz Conjecture
to One-Bit Orbit Mixing" (H-128).

Definicoes exatas extraidas do paper (secoes 2, 4, 5):

  T(n) = (3n+1) / 2^v2(3n+1)   -- mapa comprimido impar-a-impar
  X_t  = 1[n_t == 1 mod 4]     -- indicador de "burst" no passo t
  burst-ending time t_i        -- ultimo t de um bloco maximal de X=1
                                  (X_{t_i}=1, X_{t_i+1}=0)

Prop. 5.1-5.5: restrito a n_{t_i} == 1 (mod 8),
  bit4(n_{t_i})=0  <=>  n_{t_i} == 9  (mod 32)  <=>  gap longo (G>=2)
  bit4(n_{t_i})=1  <=>  n_{t_i} == 25 (mod 32)  <=>  gap unitario (G=1)

Conjectura remanescente (Secao 5.9): na subclasse n==1 mod 8,
  | B9(T) - B25(T) | / (B9(T)+B25(T))  ->  <= delta  (limitado, nao explode)
onde B9, B25 contam ocorrencias de cada residuo nos burst-ending times
ao longo da orbita real ate o passo T.

Este script testa isso numa ENSEMBLE ampla (muitas orbitas moderadas,
nao uma unica orbita gigante -- ver experiment_deep_orbit.py para o
complemento de orbita unica longa). Vetorizado com numpy int64.
"""
import numpy as np

rng = np.random.default_rng(20260718)


def step_compressed(n):
    """Um passo do mapa comprimido impar-a-impar T(n) = (3n+1)/2^v2(3n+1).
    n: array numpy int64 de valores impares. Retorna o proximo n (impar)."""
    m = 3 * n + 1
    while True:
        mask = (m % 2 == 0)
        if not np.any(mask):
            break
        m = np.where(mask, m // 2, m)
    return m


def run_ensemble(n_orbits, bit_low, bit_high, max_steps):
    starts = rng.integers(1 << bit_low, 1 << bit_high, size=n_orbits, dtype=np.int64)
    starts |= 1  # garante impar

    n = starts.copy()
    X_prev = (n % 4 == 1)
    n_prev = n.copy()

    B9 = 0
    B25 = 0
    B_other = 0  # residuos 1,17 mod32 no burst-ending com n==1 mod8 (deveria ser ~0)
    n_burst_end_18 = 0  # total de burst-endings com n==1 mod8 (denominador)

    history = []  # (passo, B9, B25) para ver evolucao/convergencia

    checkpoints = {max_steps // 20 * k for k in range(1, 21)}

    for t in range(1, max_steps + 1):
        n = step_compressed(n)
        X_cur = (n % 4 == 1)

        # transicao burst -> gap: X_prev=1, X_cur=0. O n do burst-ending eh n_prev.
        trans = X_prev & (~X_cur)
        if np.any(trans):
            cand = n_prev[trans]
            mod8 = cand % 8
            sub = cand[mod8 == 1]  # subclasse dominante n==1 mod8
            if sub.size:
                mod32 = sub % 32
                B9 += int(np.sum(mod32 == 9))
                B25 += int(np.sum(mod32 == 25))
                B_other += int(np.sum((mod32 == 1) | (mod32 == 17)))
                n_burst_end_18 += int(sub.size)

        n_prev = n
        X_prev = X_cur

        if t in checkpoints:
            total = B9 + B25
            ratio = B9 / total if total else float("nan")
            deficit = abs(ratio - 0.5)
            history.append((t, B9, B25, B_other, total, ratio, deficit))

    return history


def main():
    print("=== E-102: teste ensemble da conjectura de mixing de Chang (2026) ===")
    print()
    configs = [
        dict(n_orbits=50_000, bit_low=20, bit_high=35, max_steps=150),
        dict(n_orbits=20_000, bit_low=35, bit_high=50, max_steps=250),
    ]
    for cfg in configs:
        print(f"-- config: {cfg}")
        history = run_ensemble(**cfg)
        print(f"{'passo':>6} {'B9':>10} {'B25':>10} {'outros(1,17)':>14} "
              f"{'total':>10} {'B9/total':>10} {'|ratio-0.5|':>12}")
        for row in history:
            t, b9, b25, bo, total, ratio, deficit = row
            print(f"{t:>6} {b9:>10} {b25:>10} {bo:>14} {total:>10} "
                  f"{ratio:>10.5f} {deficit:>12.5f}")
        print()


if __name__ == "__main__":
    main()
