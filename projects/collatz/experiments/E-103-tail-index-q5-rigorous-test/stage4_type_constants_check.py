"""
E-103 Estagio 4 -- teste da previsao colateral do Fable (H-129,
2026-07-19): constantes de cauda por TIPO de residuo do raiz (u0 mod 5).

Derivacao do Fable: a matriz media de posto 1 do processo de ramificacao
multi-tipo, M(kappa)_ij=(1/5)c_i(kappa) com c_i(kappa)=Soma_a (5*2^-a)^
(theta*kappa) sobre a progressao admissivel do tipo i, tem autovetor
DIREITO de Perron C_i proporcional a c_i(kappa) = 2^(-a0(i)*theta*kappa),
com kappa=alpha_+/alpha_-=1/0.650918639898=1.536290 (theta*kappa=1
exatamente, raiz alpha_+=1). Tabela a0(i) (menor a admissivel p/ tipo
i=u0 mod 5): a0(1)=4, a0(2)=3, a0(3)=1, a0(4)=2.

Previsao FALSIFICAVEL (nao testada antes desta sessao): condicionado ao
tipo de raiz i, a cauda de W_v tem constante de escala proporcional a
C_i. Para uma probabilidade de cauda fixa p, o quantil x_i(p) (tal que
P(W_i>x_i)=p) deveria satisfazer x_i/x_j = (C_i/C_j)^(1/kappa).

Pre-registro (antes de olhar os dados): comparamos RAZOES de quantis
entre tipos, em 3 niveis de probabilidade de cauda (top 30%, 20%, 10%
dentro de cada tipo), nas 4 amostras de headroom ja existentes.
Reportamos tanto a razao observada quanto a prevista, E o tamanho de
amostra por tipo -- se n por tipo for pequeno (<50), marcamos como
subpotente em vez de forcar conclusao.
"""
import json, sys, random
import numpy as np

sys.path.insert(0, "/home/rat/Google/Projetos/Claude/ResearchOS/projects/collatz/experiments/E-097-qx1-empirical-gate")
import types
mod = types.ModuleType("eqt_funcs")
src = open("/home/rat/Google/Projetos/Claude/ResearchOS/projects/collatz/experiments/E-097-qx1-empirical-gate/empirical_qx1_tree.py").read()
exec(src.split("# ---------- Parte 1")[0], mod.__dict__)
CYCLES = mod.CYCLES

N_ROOTS = 5000
V_RANGE = (1001, 200001)
SEED = 20260718
THETA = 0.650918639898
KAPPA = 1.0 / THETA  # = alpha_+/alpha_- = 1.536290, ja que alpha_+=1
A0 = {1: 4, 2: 3, 3: 1, 4: 2}
C = {i: 2.0 ** (-A0[i] * THETA * KAPPA) for i in A0}  # theta*kappa=1 exatamente


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
    types_ = np.array([v % 5 for v in roots])

    with open("/tmp/tail_index_q5_raw_samples.json") as f:
        raw = json.load(f)

    print(f"Constantes previstas C_i (i=1..4): {C}")
    print(f"Razoes previstas C_i/C_1: {{i: C[i]/C[1] for i in C}}")
    print(f"kappa = {KAPPA:.6f}\n")

    results = {}
    for H_str, W in sorted(raw.items(), key=lambda kv: float(kv[0])):
        W = np.array(W)
        print(f"=== H={float(H_str):.0e} ===")
        by_type = {i: W[types_ == i] for i in [1, 2, 3, 4]}
        for i in [1, 2, 3, 4]:
            print(f"  tipo {i} (a0={A0[i]}): n={len(by_type[i])}")

        entry = {"H": float(H_str), "n_by_type": {i: int(len(by_type[i])) for i in [1,2,3,4]}}
        for tailp, label in [(0.30, "top30%"), (0.20, "top20%"), (0.10, "top10%")]:
            quantiles = {i: float(np.quantile(by_type[i], 1 - tailp)) for i in [1, 2, 3, 4]}
            print(f"  --- {label} (quantil 1-{tailp}) ---")
            row = {}
            for i in [2, 3, 4]:
                obs_ratio = quantiles[i] / quantiles[1]
                pred_ratio = (C[i] / C[1]) ** (1.0 / KAPPA)
                row[i] = {"obs": obs_ratio, "pred": pred_ratio}
                print(f"    x_{i}/x_1: observado={obs_ratio:.3f}  previsto={pred_ratio:.3f}  "
                      f"razao(obs/prev)={obs_ratio/pred_ratio:.3f}")
            entry[label] = row
        results[H_str] = entry
        print()

    with open("stage4_type_constants_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("Resultados salvos em stage4_type_constants_results.json")


if __name__ == "__main__":
    main()
