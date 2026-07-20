"""
E-109 — H-130, passo 2: a esterilidade extra (q=7, 2 nao raiz primitiva)
reescala W_u por tipo do mesmo jeito que a familia de escala ja
confirmada para q=5 (E-103 Estagio 4)?

Contexto: para q=7, ord_7(2)=3 < phi(7)=6, entao so os residuos em
<2>={1,2,4} mod 7 sao nao-esterceis (tem filhos); {3,5,6} (e 0) sao
esterceis (achado da 3a rodada de auditoria do paper, corrigido na
Sec.2). A familia de escala ja confirmada para q=5 (todos os 4
residuos nao-nulos sao nao-esterceis, ja que 2 e raiz primitiva mod 5)
prediz W_i =d 2^(-a0(i)*theta) * W*, theta=alpha_-(q). Este experimento
testa se a MESMA relacao vale entre os 3 tipos nao-esterceis de q=7,
apesar da esterilidade extra alhures na arvore.

q=31 (o caso mais extremo da tabela de H-130, so 5/30 residuos
nao-nulos nao-esterceis) foi considerado mas descartado: theta_31 ~
0.0552 e tao pequeno que o crescimento populacional H^0.0552 exige H
astronomico para dar amostra razoavel (H^0.0552=100 exigiria H~10^36).
q=7 (theta=0.3735, ja usado no resto do projeto) e o teste viavel mais
proximo do espirito de H-130.

Predicao (a0: 1->3, 2->2, 4->1, theta=0.373501):
  W_1/W_4 = 2^(-(3-1)*theta) = 2^(-0.747) ~ 0.5955
  W_2/W_4 = 2^(-(2-1)*theta) = 2^(-0.3735) ~ 0.7716
  W_1/W_2 = 2^(-(3-2)*theta) = 2^(-0.3735) ~ 0.7716  (mesma razao, pois
  a0 decresce em passos de 1 entre os 3 tipos)
"""

import random
import time
from tree_lib import count_tree, CYCLES  # mesma pasta

Q = 7
THETA = 0.37350103443077054
A0 = {1: 3, 2: 2, 4: 1}
N_ROOTS_PER_TYPE = 5000
V_RANGE = (10_001, 2_000_001)
HEADROOM = 10**7


def sample_roots(residue, n, rng, exclude):
    roots = []
    tried = 0
    while len(roots) < n and tried < n * 50:
        tried += 1
        v = rng.randrange(V_RANGE[0], V_RANGE[1], 2)
        if v % Q != residue:
            continue
        if v in exclude:
            continue
        roots.append(v)
    return roots


def median(xs):
    s = sorted(xs)
    n = len(s)
    mid = n // 2
    return s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2


def geomean(xs):
    logs = [__import__("math").log(x) for x in xs if x > 0]
    return __import__("math").exp(sum(logs) / len(logs))


def main():
    rng = random.Random(20260720)
    exclude = CYCLES.get(Q, set())
    results = {}
    t0 = time.time()
    for residue in (1, 2, 4):
        roots = sample_roots(residue, N_ROOTS_PER_TYPE, rng, exclude)
        Ws = []
        for v in roots:
            n_max = v * HEADROOM
            total, counts = count_tree(Q, v, n_max, checkpoints=[n_max])
            w = counts[0] / (float(HEADROOM) ** THETA)
            Ws.append(w)
        mean_w = sum(Ws) / len(Ws)
        med_w = median(Ws)
        gm_w = geomean(Ws)
        results[residue] = {"mean": mean_w, "median": med_w, "geomean": gm_w, "Ws": Ws}
        print(f"tipo u={residue} (a0={A0[residue]}): {len(Ws)} raizes "
              f"({time.time()-t0:.1f}s acumulado) -- "
              f"W medio={mean_w:.4f} mediana={med_w:.4f} media_geom={gm_w:.4f} "
              f"min={min(Ws):.4f} max={max(Ws):.4f}")

    print()
    for stat in ("mean", "median", "geomean"):
        print(f"=== Razoes observadas ({stat}) vs. previstas (2^-(a0(i)-a0(j))*theta) ===")
        pairs = [(1, 4), (2, 4), (1, 2)]
        for i, j in pairs:
            obs = results[i][stat] / results[j][stat]
            pred = 2.0 ** (-(A0[i] - A0[j]) * THETA)
            print(f"  W_{i}/W_{j}: observado={obs:.4f}  previsto={pred:.4f}  "
                  f"razao obs/previsto={obs/pred:.4f}")
        print()


if __name__ == "__main__":
    main()
