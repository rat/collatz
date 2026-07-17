#!/usr/bin/env python3
"""
H-111 - oraculo de referencia para E[G_synth|tipo] via programacao
dinamica exata (proposto pelo Fable apos diagnosticar um erro na sua
PROPRIA derivacao inicial de criticidade, nao um bug do simulador).

Fable havia previsto E[G|tau=1]=1, E[G|tau=2]=2 (autovetor de Perron
h=(1,2) da matriz de intensidade, correto para a RAZAO entre tipos,
confirmado empiricamente ~2.0-2.07x). Mas a CONSTANTE ABSOLUTA omitia o
fator do teorema de renovacao de Markov: com fase uniforme, pi=(1/3,2/3),
deslocamentos medios tilted mu1=8/3-log2(3), mu2=5/3-log2(3), soma
pi.mu=2-log2(3)=log2(4/3), dando E[G|tau] -> h_tau/ln(4/3) = 3.4761
(tau=1) / 6.9521 (tau=2) SEM truncamento de busca. Com o truncamento
real (fator de busca 5 = mesmo search_bound/n_max do DFS real), o valor
exato (por DP, verificado abaixo) e' 2.618/5.240 - establizado, nao
converge a 1/2 conforme mult cresce (o gap e' do truncamento em 5x,
nao de tamanho finito de mult).

Uso: oraculo de validacao para o checklist (comparar media amostral do
simulador Monte Carlo contra este valor exato, em vez do "1.00/2.00"
originalmente proposto).
"""
import math

LAMBDA = math.log2(3)


def exact_mean(mult, root_type, factor=5.0, max_gen_cap=300):
    """Esperanca EXATA de G=count/mult para o processo do braco 1/2 com
    rho=0 (fase uniforme, sem acoplamento). Estado (tau,m,d) memoizado:
    s = m - d*LAMBDA, m = soma dos expoentes a acumulados."""
    L_COUNT = math.log2(mult)
    L_SEARCH = L_COUNT + math.log2(factor)
    memo = {}

    def E(tau, m, d):
        key = (tau, m, d)
        if key in memo:
            return memo[key]
        s = m - d * LAMBDA
        val = 1.0 if s <= L_COUNT else 0.0
        if tau != 0 and d < max_gen_cap:
            a0 = 2 if tau == 1 else 1
            k = 0
            while True:
                a = a0 + 2 * k
                if s + a > L_SEARCH:
                    break
                cm, cd = m + a, d + 1
                val += (E(0, cm, cd) + E(1, cm, cd) + E(2, cm, cd)) / 3.0
                k += 1
        memo[key] = val
        return val

    res = E(root_type, 0, 0) / mult
    return res


if __name__ == "__main__":
    print("constante de renovacao prevista (sem truncamento de busca):")
    print("  tau=1: 1/ln(4/3) = %.4f   tau=2: 2/ln(4/3) = %.4f" % (1 / math.log(4 / 3), 2 / math.log(4 / 3)))
    print()
    print("== DP exato, fator de busca 5 (igual ao experimento), cap 300 ==")
    for mult in (2000, 20000, 200000):
        r1 = exact_mean(mult, 1)
        r2 = exact_mean(mult, 2)
        print(f"mult={mult:7d}  E[G|tau=1]={r1:.4f}  E[G|tau=2]={r2:.4f}  razao={r2/r1:.4f}")
