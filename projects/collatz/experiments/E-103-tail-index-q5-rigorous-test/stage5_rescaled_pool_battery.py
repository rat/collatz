"""
E-103 Estagio 5 -- teste de kappa (indice de cauda) no pool RESCALADO
por tipo, seguindo o Fable (consulta 2026-07-19, correcao do Estagio 4).

O Estagio 4 confirmou a familia de escala exata prevista: W_i =_d
2^(-a0(i)*theta)*W*, com a mesma distribuicao W* para todo tipo de
residuo do raiz (i=1,2,3,4; a0=(4,3,1,2)). Essa relacao NAO testa kappa
(o expoente cancela algebricamente na razao de quantis por construcao)
-- mas se ela e real, entao MISTURAR os 4 tipos SEM reescalar (o que
`full_battery.py` fez, Rodada 2 original) junta 4 copias de W* em
escalas diferentes (ate 8x entre tipo 3 e tipo 1), o que pode-se
explicar a razao pela qual a Rodada 2 deu resultado misto (GPD sem
plato limpo, Vuong favorecendo lognormal em 3/4 headrooms) -- mistura
de escalas pode desfigurar o formato aparente da cauda mesmo que o
kappa verdadeiro seja o mesmo em todos os tipos.

Este script reescala cada amostra por 2^(+a0(tipo)*theta) (para
"colapsar" de volta a escala comum W*) e roda a MESMA bateria de 4
estimadores (full_battery.py) no pool reescalado -- um teste mais
limpo (e potencialmente mais poderoso) do indice de cauda kappa.
"""
import json, sys, random
import numpy as np

sys.path.insert(0, ".")
from full_battery import run_all, PREDICTED_ALPHA, PREDICTED_XI

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
A0 = {1: 4, 2: 3, 3: 1, 4: 2}


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
    rescale = np.array([2.0 ** (A0[t] * THETA) for t in types_])

    with open("/tmp/tail_index_q5_raw_samples.json") as f:
        raw = json.load(f)

    print(f"Reescala por tipo: {{i: 2**(a0*theta) for i,a0 in A0.items()}} = "
          f"{{i: round(2.0**(A0[i]*THETA), 4) for i in A0}}\n")
    print(f"Previsto: alpha_sobrevivencia={PREDICTED_ALPHA:.4f}  xi_GPD={PREDICTED_XI:.4f}\n")

    all_results = {}
    for H_str, W in sorted(raw.items(), key=lambda kv: float(kv[0])):
        W = np.array(W)
        W_rescaled = W * rescale
        all_results[H_str] = run_all(W_rescaled, f"H={float(H_str):.0e} (POOL RESCALADO por tipo)")

    with open("stage5_rescaled_pool_results.json", "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print("\nResultados salvos em stage5_rescaled_pool_results.json")


if __name__ == "__main__":
    main()
