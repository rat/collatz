"""
E-106 -- verificacao Monte Carlo da identidade exata de Jensen usada na
Proposicao C(b) de H-127 (parede de constantes da reducao da WCC).

Contexto: H-127 deriva, via identidade de Jensen (nao estimativa), que
o expoente de decaimento "anelado" (fases independentes, benchmark
pseudoaleatorio) do modelo tilted de gaps satisfaz Lambda = log(gamma_c)
exatamente, com gamma_c = 1+log_4(3) (limiar da WCC, c->0). Numericamente
gamma_c=1,7925, log(gamma_c)=0,5834 -- muito abaixo do log3=1,0986
necessario para a tecnica de Littlewood-Offord fechar (deficit ~2,2x
no orcamento de Fourier, ou ~7x com densidade realista rho~0,3).

Este script (originalmente gerado pelo Fable em scratchpad de sessao,
2026-07-19, script "lambda_mc.py") confirma numericamente essa
identidade via simulacao direta de Z = soma de fases aleatorias
ponderadas geometricamente, para dois modelos:

  Modelo 1 (Geom(1/2), i.i.d. "Syracuse" de Tao 2011): benchmark de
  referencia, nao o modelo relevante para a WCC.

  Modelo 2 (Geom tilted, media gamma_0=1+log_4(3), limiar da WCC): o
  modelo que entra na Proposicao C(b) -- Lambda deve dar log(gamma_0).

Ver hypotheses/H-127-reducao-z-number-dicotomia-espectral-wcc.md,
secao "Proposicao C", item (b).
"""
import numpy as np

rng = np.random.default_rng(42)
N = 2_000_000
G = 60
LOG3 = np.log(3.0)
GAMMA0 = 1 + np.log(3) / np.log(4)  # limiar WCC, c->0


def run(p_geom, label):
    g = np.arange(1, G + 1)
    w = p_geom * (1 - p_geom) ** (g - 1)
    w = w / w.sum()
    ez2 = (w ** 2).sum()  # E|Z|^2 exato = soma w_g^2

    tot_logs = []
    for _ in range(4):
        U = rng.random((N // 4, G))
        Z = (w * np.exp(2j * np.pi * U)).sum(axis=1)
        tot_logs.append(np.log(1.0 / np.abs(Z)))
    L = np.concatenate(tot_logs)
    lam, se = L.mean(), L.std() / np.sqrt(len(L))

    print(f"{label}: p={p_geom:.4f}  E|Z|^2={ez2:.5f}  "
          f"(1/2)log(1/E|Z|^2)={0.5*np.log(1/ez2):.4f}")
    print(f"   Lambda = E log(1/|Z|) = {lam:.4f} +/- {2*se:.4f}   "
          f"vs  log 3 = {LOG3:.4f}")
    veredito = ("Lambda > log3 (forca estrutura)" if lam - 2*se > LOG3 else
                "Lambda < log3 (orcamento cabe sem estrutura)" if lam + 2*se < LOG3 else
                "indeterminado")
    print(f"   veredito anelado: {veredito}")
    return lam, se


if __name__ == "__main__":
    lam1, se1 = run(0.5, "Modelo 1 (Geom(1/2), Syrac de Tao)")
    lam2, se2 = run(1.0 / GAMMA0, f"Modelo 2 (tilted, media {GAMMA0:.4f}, limiar WCC)")

    print(f"\nChecagem contra a identidade de Jensen prevista (Proposicao C(b)):")
    print(f"  log(gamma_0) previsto = {np.log(GAMMA0):.4f}")
    print(f"  Lambda medido (Modelo 2) = {lam2:.4f} +/- {2*se2:.4f}")
    print(f"  bate? {'SIM' if abs(lam2 - np.log(GAMMA0)) < 2*se2 else 'NAO'}")
