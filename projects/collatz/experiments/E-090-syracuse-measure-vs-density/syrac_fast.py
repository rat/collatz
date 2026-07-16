#!/usr/bin/env python3
"""
Versao vetorizada (numpy) da recursao de auto-consistencia de Tao
(Lemma 1.12) - syrac_distribution_float em experiment.py e pura Python
(loop duplo sobre estados x e expoentes a), o que fica inviavel em
tempo/memoria para m>=15 (3^15~14M estados, cada um com ate 64
iteracoes). Aqui a mesma recursao e' vetorizada: para x com x%3==1,
todos os a PARES sao validos simultaneamente; para x%3==2, todos os a
IMPARES - entao cada iteracao sobre a atualiza TODOS os x daquele
residuo de uma vez com indexacao fancy do numpy, em vez de um loop
Python por estado.

Validado abaixo contra syrac_distribution_float (pura Python, ja
validada em E-090/H-090 contra os valores exatos de Tao) para m<=12.

Cuidado de overflow: pow2a*xs e' calculado em int64; para m<=18,
modulus=3^m<=387420489, pow2a<modulus, xs<modulus, produto <
1.5e17 << int64 max (~9.2e18) - seguro. Nao usar para m>=19 sem revisar.
"""
import numpy as np


def syrac_distribution_np(m, a_max=64):
    dist = np.array([1.0])
    for level in range(m):
        modulus = 3 ** (level + 1)
        x = np.arange(modulus, dtype=np.int64)
        new_dist = np.zeros(modulus, dtype=np.float64)
        mod3 = x % 3
        mask_r1 = mod3 == 1  # precisa a par
        mask_r2 = mod3 == 2  # precisa a impar
        xs_r1 = x[mask_r1]
        xs_r2 = x[mask_r2]
        for a in range(1, a_max + 1):
            xs = xs_r1 if a % 2 == 0 else xs_r2
            if xs.size == 0:
                continue
            pow2a = pow(2, a, modulus)
            z = (pow2a * xs) % modulus
            y = (z - 1) // 3
            w = 2.0 ** (-a)
            new_dist[xs] += w * dist[y]
        s = new_dist.sum()
        if s > 0:
            new_dist /= s
        dist = new_dist
    return dist


def as_dict(dist_array):
    return {x: float(p) for x, p in enumerate(dist_array)}


if __name__ == "__main__":
    import time
    from experiment import syrac_distribution_float

    print("Validando syrac_distribution_np contra a versao pura Python (ja validada):")
    for m in [1, 2, 4, 6, 8, 10, 12]:
        t0 = time.time()
        exact = syrac_distribution_float(m, a_max=64)
        t_slow = time.time() - t0
        t0 = time.time()
        fast = syrac_distribution_np(m, a_max=64)
        t_fast = time.time() - t0
        max_diff = max(abs(exact[x] - fast[x]) for x in exact)
        print(f"  m={m:2d}: diff_max={max_diff:.2e}  t_slow={t_slow:.3f}s  t_fast={t_fast:.4f}s  speedup={t_slow/max(t_fast,1e-9):.0f}x")
