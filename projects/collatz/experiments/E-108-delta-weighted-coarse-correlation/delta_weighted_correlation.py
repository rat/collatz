"""
E-108 — soma ponderada por Delta da correlacao grosseira (Prop. 2 de H-126).

Pergunta: H-126/Prop.2 prova Corr(Z1,Z2) = +1 se Delta = a2-a1 = 0 (mod 6),
e -1/2 caso contrario, para um par de folhas-irmas com expoentes de ramo
admissiveis a1 < a2 num pai comum v (q=3, d=ord_3(2)=2, logo Delta e
sempre par). Os pesos de ramo sao geometricos (q*2^-a), concentrando
massa em expoentes pequenos. Qual e a correlacao grosseira MEDIA, pesada
pela contribuicao natural de cada par de ramos ao segundo momento
E[Z1 Z2] (peso proporcional a 2^-a1 * 2^-a2)? Auditoria (2026-07-20)
e consulta ao Opus sugeriram que essa media e negativa, "consistente"
com o sinal do excesso residual observado na calibracao (H-110/secao 5
do paper) -- mas so qualitativamente. Este script calcula o valor
EXATO em forma fechada e confirma numericamente por soma direta
truncada.

Setup exato: para q=3, d=2, os expoentes admissiveis a partir de um
pai fixo u formam uma progressao a0, a0+2, a0+4, ... (a0 in {1,2}
dependendo de u mod 3). Um par de ramos DISTINTOS desse pai tem
expoentes a_i = a0+2n, a_j = a0+2n+2k (k=1,2,3,...), Delta=2k sempre
par. O peso natural de um par ordenado (i,j) no segundo momento e
proporcional a 2^-a_i * 2^-a_j = 2^-(2*a0+2n) * 2^-2k (a normalizacao
por a0 e comum a todo k, cancela).
"""

from fractions import Fraction


def p_delta_2k_closed_form(k_max=200):
    """P(Delta=2k) sob a medida size-biased pelo peso 2^-(a_i+a_j),
    somando sobre todos os pares (n>=0, k fixo). Retorna dict k->Fraction,
    exato via serie geometrica fechada."""
    # peso(k) = sum_{n=0}^inf 2^-(2n) * 2^-(2n+2k) [ate constante comum 2^-2a0]
    #         = 2^-2k * sum_{n=0}^inf 2^-4n = 2^-2k * (1/(1-1/16)) = 2^-2k * 16/15
    # entao peso(k) propto 2^-2k = 4^-k
    # P(Delta=2k) = 4^-k / sum_{k=1}^inf 4^-k = 4^-k / (1/3) = 3 * 4^-k
    probs = {}
    for k in range(1, k_max + 1):
        probs[k] = Fraction(3, 1) * Fraction(1, 4) ** k
    return probs


def p_delta_2k_numeric_direct_sum(k_max_check=6, n_max=2000):
    """Confirmacao numerica independente: soma direta (nao a forma
    fechada) dos pesos brutos 2^-(a_i+a_j) para n=0..n_max, normalizada
    sobre TODOS os k de 1 a k_max_check (usando o mesmo range de n para
    cada k, para nao introduzir viés de truncamento diferencial)."""
    raw = {}
    for k in range(1, k_max_check + 1):
        total = 0.0
        for n in range(n_max):
            a_i = 2 * n
            a_j = 2 * n + 2 * k
            total += 2.0 ** (-a_i) * 2.0 ** (-a_j)
        raw[k] = total
    norm = sum(raw.values())
    # nota: isso NAO soma a cauda k>k_max_check, entao serve so para
    # confirmar a FORMA (razao geometrica 1/4 entre k e k+1), nao a
    # normalizacao exata (essa vem da forma fechada, que soma k ate infinito).
    return raw


def expected_coarse_correlation():
    """Fecha as series geometricas infinitas analiticamente (nao soma
    termo a termo), para obter fracoes exatas e reduzidas.
    P(Delta=2k) = 3*4^-k. Delta=2k == 0 (mod 6) <=> k == 0 (mod 3).
    P(k == 0 mod 3) = sum_{m=1}^inf 3*4^-3m = 3*(1/64)/(1-1/64) = 3/63 = 1/21.
    """
    p_pos = Fraction(3, 1) * (Fraction(1, 64) / (1 - Fraction(1, 64)))
    p_neg = 1 - p_pos
    total = p_pos + p_neg
    corr_pos = Fraction(1, 1)
    corr_neg = Fraction(-1, 2)
    e_corr = p_pos * corr_pos + p_neg * corr_neg
    return p_pos, p_neg, total, e_corr


if __name__ == "__main__":
    print("=== Forma fechada: P(Delta=2k) = 3 * 4^-k ===")
    probs = p_delta_2k_closed_form(k_max=10)
    for k in range(1, 8):
        print(f"  k={k} (Delta={2*k}): P = {probs[k]} = {float(probs[k]):.6f}")
    tail = Fraction(3, 1) * (Fraction(1, 4) / (1 - Fraction(1, 4)))
    print(f"  soma total (fechada, k=1..infinito): {tail} = {float(tail):.10f}  (esperado: 1)")

    print()
    print("=== Confirmacao numerica independente (soma direta, nao fechada) ===")
    raw = p_delta_2k_numeric_direct_sum(k_max_check=6, n_max=5000)
    ratios = []
    ks = sorted(raw.keys())
    for i in range(len(ks) - 1):
        k1, k2 = ks[i], ks[i + 1]
        ratios.append(raw[k2] / raw[k1])
    print("  razoes sucessivas peso(k+1)/peso(k) (esperado: exatamente 0.25):")
    for k, r in zip(ks[:-1], ratios):
        print(f"    k={k}->{k+1}: {r:.10f}")

    print()
    print("=== P(Delta=6m) [correlacao +1] vs P(Delta != 6m) [correlacao -1/2] ===")
    p_pos, p_neg, total, e_corr = expected_coarse_correlation()
    print(f"  P(Delta = 0 mod 6)  = {p_pos} = {float(p_pos):.6f}")
    print(f"  P(Delta != 0 mod 6) = {p_neg} = {float(p_neg):.6f}")
    print(f"  soma = {total} (esperado 1)")
    print(f"  E[Corr] = P(+1 branch)*(+1) + P(-1/2 branch)*(-1/2)")
    print(f"          = {e_corr} = {float(e_corr):.6f}")
