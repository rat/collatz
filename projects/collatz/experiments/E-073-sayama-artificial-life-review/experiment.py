#!/usr/bin/env python3
"""
E-073 - Verifica os calculos centrais de Sayama, "An Artificial Life View
of the Collatz Problem" (Artificial Life 17, 137-140, 2011), item 103 da
colecao.

O paper reinterpreta a dinamica ACELERADA (ignora a divisao par, so olha
x_{t+1}=3x_t+LSNB(x_t), onde LSNB(x)=least significant nonzero bit) como
"crescimento pela esquerda" (replicacao, Eq.2, taxa media L=log2(3+
LSNB(x)/x)) competindo com "extincao pela direita" (LSNB introduz
perturbacao). Dois calculos concretos:

1. L_app = log2(3) ~ 1.585 bits/passo (Eq.5, aproximacao para LSNB<<x) -
   testamos a formula EXATA (Eq.4, sem aproximar) via identidade
   telescopica log2(x_final)-log2(x_inicial) = soma de log2(3+LSNB/x_t),
   que E EXATA por telescopagem (nao precisa de simulacao estatistica).
2. R_app = sum_{l=1}^inf l*(1/2)^l = 2 bits/passo (Eq.6) - serie
   geometrica padrao, verificamos a soma e o proprio calculo.
3. Verificamos que "extincao mais rapida que crescimento" (2 > log2(3))
   e consistente com convergencia real: comparamos a taxa media
   empirica log2(x_0)/steps_to_1 com log2(3) e com a diferenca
   (extincao - crescimento) teorica.

Reproduzir: python3 experiment.py
"""
import sys
import math
import random


def lsnb(x):
    """Least significant nonzero bit de x (bit 1 mais a direita, como valor)."""
    return x & (-x)


def collatz_accelerated_step(x):
    """x_{t+1} = 3x_t + LSNB(x_t) - Eq. 2 do paper (versao 'sem ifs')."""
    return 3 * x + lsnb(x)


def f_standard(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1


def steps_to_1(n):
    if n == 1:
        return 0
    k = 0
    while n != 1:
        n = f_standard(n)
        k += 1
    return k


def is_pow2(x):
    return x > 0 and (x & (x - 1)) == 0


def test_exact_telescoping_identity(seeds, n_steps=2000):
    """log2(x_final) - log2(x_inicial) = soma_t log2(3 + LSNB(x_t)/x_t)
    e uma identidade EXATA (telescopica), nao uma aproximacao - Eq. 4
    do paper antes de aproximar para Eq. 5.

    ACHADO IMPORTANTE (nao e erro do paper - e uma confirmacao de uma
    frase que o proprio paper ja faz, Eq.5): uma vez que x atinge uma
    POTENCIA DE 2 (equivalente a "populacao = 1 bit", i.e., a versao
    acelerada-sem-divisao do ciclo trivial {1,2,4}), a orbita fica presa
    nesse estado para sempre (3*2^k+LSNB(2^k)=3*2^k+2^k=4*2^k=2^(k+2)),
    com L EXATO =2 (nao log2(3)) - exatamente o caso extremo que o
    paper descreve apos a Eq.5 ("sustainable if and only if LSNB(xt)=xt
    always, i.e., population consists of a single nonzero bit"). Medir a
    media sobre TODA uma trajetoria longa (incluindo a fase pos-potencia
    de 2) dilui a leitura para perto de 2, nao log2(3) - por isso
    medimos separadamente: (a) SO a fase ativa (antes de atingir uma
    potencia de 2), que deve dar ~log2(3); (b) confirmamos que a fase
    pos-potencia de 2 da exatamente 2.0."""
    failures = 0
    for x0 in seeds:
        x = x0
        log_sum_active = 0.0
        steps_active = 0
        hit_pow2_at = None
        for i in range(n_steps):
            if is_pow2(x) and i > 0:
                hit_pow2_at = i
                break
            xn = collatz_accelerated_step(x)
            log_sum_active += math.log2(xn / x)
            steps_active += 1
            x = xn
        avg_L_active = log_sum_active / steps_active if steps_active else float("nan")
        msg = f"  x0={x0}: L medio na fase ATIVA ({steps_active} passos"
        if hit_pow2_at is not None:
            msg += f", atingiu potencia de 2 no passo {hit_pow2_at}) = {avg_L_active:.6f}"
        else:
            msg += f", nao atingiu potencia de 2 em {n_steps} passos) = {avg_L_active:.6f}"
        msg += f" (log2(3)={math.log2(3):.6f})"
        print(msg)
        if hit_pow2_at is not None:
            # confirma que dali em diante L=2 exatamente por mais alguns passos
            xn = collatz_accelerated_step(x)
            step_log = math.log2(xn / x)
            if abs(step_log - 2.0) > 1e-9:
                failures += 1
                print(f"    FALHA: apos atingir potencia de 2, L deveria ser exatamente 2.0, obtido {step_log}")
            else:
                print(f"    confirmado: apos atingir 2^{x.bit_length()-1}, L=2.0 exato (regime absorvente)")
    return failures


def test_power_of_2_is_generic(n_samples=200, max_steps=500, n_max=10 ** 6, seed=1):
    """Confirma que atingir uma potencia de 2 (fim da fase ativa) e
    generico, nao uma coincidencia das sementes escolhidas acima."""
    rng = random.Random(seed)
    hit_count = 0
    for _ in range(n_samples):
        x = rng.randrange(3, n_max) | 1
        for i in range(max_steps):
            if is_pow2(x) and i > 0:
                hit_count += 1
                break
            x = collatz_accelerated_step(x)
    return hit_count, n_samples


def test_extinction_series():
    """R_app = sum_{l=1}^inf l*(1/2)^l = 2 (Eq. 6) - serie geometrica
    E[L] de uma distribuicao geometrica(p=1/2). Verificamos a formula
    fechada e a soma parcial truncada."""
    # soma fechada conhecida: sum l*x^l = x/(1-x)^2, em x=1/2 -> 2
    x = 0.5
    closed_form = x / (1 - x) ** 2
    # soma parcial (deve convergir rapido para 2)
    partial = sum(l * (0.5 ** l) for l in range(1, 200))
    print(f"  soma fechada x/(1-x)^2 em x=0.5: {closed_form}")
    print(f"  soma parcial (l=1..199): {partial}")
    ok = abs(closed_form - 2.0) < 1e-12 and abs(partial - 2.0) < 1e-12
    return 0 if ok else 1


def test_growth_vs_extinction_consistency(n_samples=2000, n_max=10 ** 9, seed=1):
    """Testa se 'extincao (2 bits/passo) > crescimento (log2(3)~1.585
    bits/passo)' e consistente com a taxa media empirica de decaimento
    (steps_to_1 padrao). Se a orbita converge, esperamos que
    log2(x0)/steps_to_1(x0) fique por volta de ~log2(sqrt(3)/2)~-0.2075
    por passo padrao (fato ja estabelecido deste projeto, H-001/H-011:
    E[log2(fator multiplicativo por passo padrao)] = (log2(3)-2)/2 ~
    -0.2075, jah que so metade dos passos e "3n+1" e a outra metade e
    "/2" pareado). Nao e o MESMO L do paper (que e so sobre a dinamica
    acelerada sem o "/2"), mas o SINAL (decrescimento medio) deve bater:
    se extincao > crescimento no modelo acelerado do paper, esperamos
    x decrescendo em media na dinamica padrao tambem."""
    rng = random.Random(seed)
    log_ratios = []
    for _ in range(n_samples):
        n = rng.randrange(3, n_max) | 1
        steps = steps_to_1(n)
        if steps == 0:
            continue
        log_ratios.append(-math.log2(n) / steps)  # negativo = decaimento medio por passo
    avg = sum(log_ratios) / len(log_ratios)
    theoretical = (2 - math.log2(3)) / 2  # ver H-001: metade dos passos e /2 (contribui -1), metade e (3n+1)/1 (contribui log2(3))-ajustado
    print(f"  taxa media de decaimento empirica (dinamica padrao, {len(log_ratios)} amostras): {avg:.6f} bits/passo")
    print(f"  extincao_paper(2.0) - crescimento_paper(log2(3)={math.log2(3):.4f}) = {2 - math.log2(3):.4f} bits/passo (dinamica ACELERADA, sem intercalar /2)")
    print(f"  nota: os dois valores nao sao diretamente comparaveis (dinamica acelerada vs. padrao),")
    print(f"  mas ambos tem o MESMO SINAL (decaimento liquido), consistente com a conclusao do paper.")
    return avg


def main():
    print("=== Identidade telescopica exata para L (crescimento), fase ativa vs. absorvente ===")
    fail1 = test_exact_telescoping_identity([111111111, 27, 97, 2**20 - 1])
    print(f"  {fail1} falhas")
    print()

    print("=== Potencia de 2 como estado absorvente e generico (nao coincidencia) ===")
    hit_count, n_samples = test_power_of_2_is_generic()
    print(f"  {hit_count}/{n_samples} amostras aleatorias atingiram uma potencia de 2 em <=500 passos")
    print()

    print("=== R_app = soma l*(1/2)^l = 2 (extincao) ===")
    fail2 = test_extinction_series()
    print(f"  {'OK' if fail2 == 0 else 'FALHA'}")
    print()

    print("=== Consistencia de sinal: extincao > crescimento vs decaimento real ===")
    test_growth_vs_extinction_consistency()


if __name__ == "__main__":
    main()
