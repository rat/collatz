#!/usr/bin/env python3
"""Custo minimo exato da variavel de Syracuse modulo 3^ell.

Para a_1,...,a_n >= 1, defina A_m = a_1+...+a_m e

    S_n = sum_{m=1}^n 3^(m-1) 2^(-A_m)  (mod 3^L).

Usamos W_m = 2^A_m S_m, que satisfaz

    W_m = 2^a_m W_(m-1) + 3^(m-1).

O DP booleano registra a existencia de uma tupla para cada par (W,custo).
No fim, S_n=z e equivalente a W_n=2^c z. A implementacao e validada
contra enumeracao direta em niveis pequenos.
"""

from __future__ import annotations

import argparse
import itertools
import math

import numpy as np


JSTAR = {
    1: 1, 2: 4, 3: 6, 4: 7, 5: 9, 6: 10, 7: 11,
    8: 12, 9: 13, 10: 15, 11: 16, 12: 17, 13: 18, 14: 19,
    15: 20, 16: 20, 17: 21, 18: 22, 19: 23, 20: 24,
}


def reachable_w(n: int, level: int, cost_max: int) -> np.ndarray:
    """Retorna D[w,c]: existe tupla de comprimento n, custo c, com W_n=w."""
    modulus = 3**level
    residues = np.arange(modulus, dtype=np.int64)
    state = np.zeros((modulus, cost_max + 1), dtype=np.bool_)
    state[0, 0] = True

    for m in range(1, n + 1):
        nxt = np.zeros_like(state)
        shift = pow(3, m - 1, modulus)
        max_a = cost_max - (m - 1)
        power2 = 1
        for a in range(1, max_a + 1):
            power2 = (2 * power2) % modulus
            target = (power2 * residues + shift) % modulus
            nxt[target, a:] |= state[:, : cost_max + 1 - a]
        state = nxt
    return state


def min_costs(n: int, level: int, cost_max: int) -> np.ndarray:
    """Menor custo de Syracuse para cada residuo; -1 se nao alcancado."""
    modulus = 3**level
    state = reachable_w(n, level, cost_max)
    z = np.arange(modulus, dtype=np.int64)
    possible = np.zeros_like(state)
    power2 = 1
    for cost in range(cost_max + 1):
        if cost:
            power2 = (2 * power2) % modulus
        possible[:, cost] = state[(z * power2) % modulus, cost]

    reached = possible.any(axis=1)
    result = np.full(modulus, -1, dtype=np.int64)
    result[reached] = np.argmax(possible[reached], axis=1)
    return result


def brute_min_costs(n: int, level: int, cost_max: int) -> np.ndarray:
    """Enumeracao por composicoes do custo, independente da recursao W."""
    modulus = 3**level
    inverse2 = pow(2, -1, modulus)
    result = np.full(modulus, -1, dtype=np.int64)

    def compositions(total: int, parts: int):
        for cuts in itertools.combinations(range(1, total), parts - 1):
            points = (0,) + cuts + (total,)
            yield tuple(points[i + 1] - points[i] for i in range(parts))

    for cost in range(n, cost_max + 1):
        for values in compositions(cost, n):
            partial = 0
            residue = 0
            for m, a in enumerate(values):
                partial += a
                residue += pow(3, m, modulus) * pow(inverse2, partial, modulus)
            residue %= modulus
            if result[residue] < 0:
                result[residue] = cost
    return result


def validate() -> None:
    for n, level, cost_max in ((2, 2, 9), (3, 3, 12), (3, 4, 13), (4, 4, 15)):
        dynamic = min_costs(n, level, cost_max)
        brute = brute_min_costs(n, level, cost_max)
        if not np.array_equal(dynamic, brute):
            bad = np.flatnonzero(dynamic != brute)
            raise AssertionError(
                f"DP diverge da forca bruta em n={n}, L={level}, "
                f"primeiros residuos={bad[:10].tolist()}"
            )
        print(f"validacao n={n} L={level} custo<={cost_max}: OK")


def next_distribution(previous: np.ndarray, level: int, tail: int = 120) -> np.ndarray:
    """Lei de Syrac modulo 3^level pela recursao de Tao.

    Se nu e a lei de 1+3*S_(level-1), a equacao memoryless e

        mu(y) = 1/2 nu(2y) + 1/2 mu(2y).

    A multiplicacao por 2 percorre todas as unidades modulo 3^level.
    A serie geometrica e truncada em ``tail``; o erro total e menor que
    2^-tail vezes uma constante absoluta.
    """
    modulus = 3**level
    period = 2 * 3 ** (level - 1)
    nu = np.zeros(modulus, dtype=np.float64)
    nu[1 + 3 * np.arange(previous.size)] = previous

    orbit = np.empty(period, dtype=np.int64)
    orbit[0] = 1
    for k in range(1, period):
        orbit[k] = (2 * orbit[k - 1]) % modulus
    along = nu[orbit]

    values = np.zeros(period, dtype=np.float64)
    for s in range(tail):
        values += 2.0 ** (-(s + 1)) * np.roll(along, -(s + 1))

    distribution = np.zeros(modulus, dtype=np.float64)
    distribution[orbit] = values
    return distribution


def scan_weighted(max_level: int) -> None:
    distribution = np.array([1.0], dtype=np.float64)
    print("\nell  c_ell                 beta_eff  3^ell*c_ell  argmin")
    for level in range(1, max_level + 1):
        distribution = next_distribution(distribution, level)
        units = np.flatnonzero(np.arange(3**level) % 3 != 0)
        probs = distribution[units]
        c_ell = float(probs.min())
        argmin = int(units[np.argmin(probs)])
        beta = -math.log(c_ell) / (level * math.log(3))
        normalized = 3**level * c_ell
        if abs(float(distribution.sum()) - 1.0) > 1e-12:
            raise AssertionError(f"massa nao normalizada em ell={level}")
        if level == 1 and abs(c_ell - 1 / 3) > 1e-14:
            raise AssertionError("c_1 diverge de 1/3")
        if level == 2 and abs(c_ell - 2 / 63) > 1e-14:
            raise AssertionError("c_2 diverge de 2/63")
        print(
            f"{level:3d} {c_ell:21.14e} {beta:9.6f} "
            f"{normalized:13.6e} {argmin:8d}"
        )


def scan(max_level: int, slack: int) -> None:
    print("ell  Bmax  j_equiv  jstar  Bmax-ell*log2(3)  argmax")
    for level in range(1, max_level + 1):
        cost_max = JSTAR.get(level, 2 * level) + level + slack
        costs = min_costs(level, level, cost_max)
        units = np.flatnonzero(np.arange(3**level) % 3 != 0)
        unit_costs = costs[units]
        if np.any(unit_costs < 0):
            missing = int(np.count_nonzero(unit_costs < 0))
            raise RuntimeError(
                f"custo_max={cost_max} insuficiente em ell={level}: {missing} unidades"
            )
        maximum = int(unit_costs.max())
        argmax = int(units[np.argmax(unit_costs)])
        j_equiv = maximum - level
        jstar = JSTAR.get(level)
        gap = maximum - level * math.log2(3)
        print(
            f"{level:3d} {maximum:5d} {j_equiv:8d} "
            f"{str(jstar) if jstar is not None else '-':>5} "
            f"{gap:19.6f} {argmax:8d}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-level", type=int, default=12)
    parser.add_argument("--slack", type=int, default=2)
    args = parser.parse_args()
    validate()
    scan(args.max_level, args.slack)
    scan_weighted(args.max_level)


if __name__ == "__main__":
    main()
