"""
E-103 Estagio 2 -- teste da hipotese log-periodica na cauda de W_v (q=5).

Motivacao: E-105 (H-129) levantou, como hipotese NAO TESTADA, que o
transiente k^-0,222 do teste de momento (Estagio/Rodada 3) pudesse vir
de um efeito de reticulado log-periodico na cauda de W_v, ja que os
pesos dos ramos sao potencias de 2. Consulta ao Fable derivou a
previsao teorica correta ANTES de rodar qualquer teste (evitando cair
na mesma armadilha do a* em H-129: nao escolher o periodo POR AJUSTE
aos dados).

Derivacao do Fable (dicotomia aritmetico/nao-aritmetico da teoria de
renovacao implicita, Goldie 1991): os multiplicadores A_a=(5*2^-a)^theta
formam um reticulado DESLOCADO por tipo (u0 mod 5), com deslocamento
b_i/s = (log_2(5) - a_0(i))/4 -- IRRACIONAL, pois log_2(5) e irracional
(5 nao e potencia de 2). Pela dicotomia de Goldie, isso e o caso
NAO-ARITMETICO: nao deve haver correcao log-periodica assintotica (h
converge a uma constante, teorema de Blackwell). Previsao: qualquer
oscilacao aparente em profundidade finita e artefato de mistura de fase
(a fase gira log_2(5) por nivel, irracional, entao "lava" com k
crescente) -- deveria aparecer, se aparecer, SO nos dois periodos
candidatos abaixo, com amplitude DECRESCENTE em k/headroom.

Periodos candidatos (log natural de x, theta=alpha_-(5)=0,650918639898):
  - "uniao" (artefato de k finito, uniao de todos os a): theta*log(2) = 0,4512
  - "por-tipo" (leitura ingenua, espacamento d=ord_5(2)=4): 4*theta*log(2) = 1,8047

Teste: ajusta lei de potencia pura via CSN (full_battery.py), calcula
residuo log(S_emp/S_pred) em funcao de t=log(x/xmin), e mede a potencia
do periodograma de Lomb-Scargle EXATAMENTE nesses dois periodos
(pre-registrados, nao escolhidos a posteriori), comparando contra o
nivel de ruido de fundo (grade ampla de periodos).
"""
import json
import numpy as np
from scipy.signal import lombscargle

import sys
sys.path.insert(0, ".")
from full_battery import csn_fit

THETA = 0.650918639898
PERIOD_UNIAO = THETA * np.log(2)
PERIOD_TIPO = 4 * THETA * np.log(2)


def analyze(H_str, W):
    x = np.array(sorted(w for w in W if w > 0))
    csn = csn_fit(x)
    if not csn:
        return None
    xmin, alpha_csn = csn["u"], csn["alpha_csn"]
    alpha_surv = alpha_csn - 1
    xt = x[x >= xmin]
    n_u = len(xt)

    rank_desc = np.arange(n_u, 0, -1)
    S_emp = rank_desc / n_u
    S_pred = (xt / xmin) ** (-alpha_surv)
    resid = np.log(S_emp) - np.log(S_pred)
    t = np.log(xt / xmin)

    mask = (t > 1e-9) & (rank_desc > 1)
    t_use, r_use = t[mask], resid[mask]
    if len(t_use) < 20:
        return None

    ang_freqs = 2 * np.pi / np.array([PERIOD_UNIAO, PERIOD_TIPO])
    power_pred = lombscargle(t_use, r_use - r_use.mean(), ang_freqs, normalize=True)

    bg_periods = np.linspace(0.05, 5.0, 500)
    bg_power = lombscargle(t_use, r_use - r_use.mean(), 2 * np.pi / bg_periods, normalize=True)

    return {
        "H": float(H_str), "n_tail": int(n_u), "xmin": float(xmin),
        "alpha_surv": float(alpha_surv), "t_span": float(t_use.max()),
        "ciclos_uniao": float(t_use.max() / PERIOD_UNIAO),
        "ciclos_tipo": float(t_use.max() / PERIOD_TIPO),
        "power_uniao": float(power_pred[0]), "power_tipo": float(power_pred[1]),
        "bg_mean": float(bg_power.mean()), "bg_p95": float(np.percentile(bg_power, 95)),
        "bg_max": float(bg_power.max()),
    }


def main():
    with open("/tmp/tail_index_q5_raw_samples.json") as f:
        raw = json.load(f)

    print(f"Periodos teoricos (Fable, nao ajustados aos dados): "
          f"uniao={PERIOD_UNIAO:.4f}, por-tipo={PERIOD_TIPO:.4f} (log natural)\n")

    results = []
    for H_str, W in sorted(raw.items(), key=lambda kv: float(kv[0])):
        r = analyze(H_str, W)
        if r is None:
            continue
        results.append(r)
        sig_uniao = "SIM" if r["power_uniao"] > r["bg_p95"] else "nao"
        sig_tipo = "SIM" if r["power_tipo"] > r["bg_p95"] else "nao"
        print(f"H={r['H']:.0e} (n_tail={r['n_tail']}, ciclos uniao={r['ciclos_uniao']:.1f}, "
              f"ciclos tipo={r['ciclos_tipo']:.1f}):")
        print(f"  potencia @ uniao = {r['power_uniao']:.4f}  (> p95 ruido={r['bg_p95']:.4f}? {sig_uniao})")
        print(f"  potencia @ tipo  = {r['power_tipo']:.4f}  (> p95 ruido={r['bg_p95']:.4f}? {sig_tipo})")
        print()

    with open("stage2_periodogram_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("Resultados salvos em stage2_periodogram_results.json")


if __name__ == "__main__":
    main()
