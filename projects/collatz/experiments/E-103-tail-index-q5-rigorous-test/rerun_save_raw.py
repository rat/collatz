#!/usr/bin/env python3
"""
Reroda a mesma enumeracao de experiment_tail_index_q5.py, mas desta vez
salva as amostras BRUTAS de W_v (nao so estatisticas agregadas), para
permitir aplicar a bateria completa de estimadores (GI, Hill com
correcao de vies, MLE de GPD, CSN+Vuong) sem repetir o DFS (~20min).
"""
import sys, random, time, json

sys.path.insert(0, "/home/rat/Google/Projetos/Claude/ResearchOS/projects/collatz/experiments/E-097-qx1-empirical-gate")
import types
mod = types.ModuleType("eqt_funcs")
src = open("/home/rat/Google/Projetos/Claude/ResearchOS/projects/collatz/experiments/E-097-qx1-empirical-gate/empirical_qx1_tree.py").read()
src_funcs = src.split("# ---------- Parte 1")[0]
exec(src_funcs, mod.__dict__)
count_tree = mod.count_tree
CYCLES = mod.CYCLES

ALPHA1 = 0.650918639898

N_ROOTS = 5000
H_LEVELS = [10**5, 10**6, 10**7, 10**8]
V_RANGE = (1001, 200001)
SEED = 20260718


def sample_roots(n, rng):
    roots = []
    tried = 0
    while len(roots) < n and tried < n * 3:
        tried += 1
        v = rng.randrange(V_RANGE[0], V_RANGE[1], 2)
        if v % 5 == 0 or v in CYCLES[5]:
            continue
        roots.append(v)
    return roots


def main():
    rng = random.Random(SEED)
    roots = sample_roots(N_ROOTS, rng)
    print(f"Amostrando {len(roots)} raizes, headrooms {H_LEVELS}, range v em {V_RANGE}", flush=True)
    t0 = time.time()

    W_by_level = {H: [] for H in H_LEVELS}

    for idx, v in enumerate(roots):
        checkpoints = [v * H for H in H_LEVELS]
        tot, counts = count_tree(5, v, v * H_LEVELS[-1], checkpoints)
        for H, c in zip(H_LEVELS, counts):
            W = c / (H ** ALPHA1)
            W_by_level[H].append(W)
        if (idx + 1) % 500 == 0:
            dt = time.time() - t0
            print(f"  {idx+1}/{len(roots)} raizes processadas ({dt:.1f}s)", flush=True)

    dt = time.time() - t0
    print(f"Total: {dt:.1f}s", flush=True)

    with open("/tmp/tail_index_q5_raw_samples.json", "w") as f:
        json.dump({str(k): v for k, v in W_by_level.items()}, f)
    print("Amostras brutas salvas em /tmp/tail_index_q5_raw_samples.json", flush=True)


if __name__ == "__main__":
    main()
