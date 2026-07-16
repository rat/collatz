#!/usr/bin/env python3
"""
H-093 / item 087 - Tynski, "A Common Proof of the Riemann Hypothesis and
the Collatz Conjecture" (academia.edu, 99 paginas, ALEGACAO DE PROVA).

O nucleo da alegacao para Collatz (Teorema 8.59, via o "axioma (W6)" da
Definicao 8.63) e' um limite de Lyapunov DETERMINISTICO (nao estocastico,
palavras do proprio autor):

    log2(n_m) <= log2(n0) - m*delta + C*sqrt(m),    delta = 2 - log2(3)

alegado como "forcado" pela "restricao de residuo 2-adico fino" (eq 8.1)
e verificado apenas numericamente para n0 <= 3*10^4, com C<=5.

Isso e' exatamente o padrao de erro ja catalogado varias vezes neste
projeto (H-045/Mohammed, H-065/Boyle): tomar uma propriedade MEDIA/
ESPERADA (E[a_i]=2, logo delta=2-log2(3) em media) e trata-la como
garantia deterministica por trajetoria individual, sem prova real.

Este experimento testa diretamente se o "C<=5 universal" alegado se
sustenta: calcula, para cada n0 testado, o menor C que faz o limite
valer em TODOS os pontos m da trajetoria, e verifica se esse C_min
fica limitado (a favor da alegacao) ou cresce sem limite / excede 5
(contra a alegacao) conforme n0 cresce ou para "recordistas de atraso"
conhecidos (excursoes anormalmente longas ja catalogadas na literatura
de Collatz).

Reproduzir: python3 experiment.py
"""
import math
import random

DELTA = 2 - math.log2(3)


def trajectory_log2(n0):
    """Retorna a lista log2(n_m) para m=0,1,2,... ate n_m=1 (orbita
    ACELERADA, i.e. so contando valores impares apos aplicar T(n)=(3n+1)/2^a)."""
    logs = [math.log2(n0)]
    n = n0
    while n != 1:
        n = 3 * n + 1
        while n % 2 == 0:
            n //= 2
        logs.append(math.log2(n))
    return logs


def c_min_for_seed(n0):
    """C minimo necessario para que log2(n_m) <= log2(n0) - m*delta + C*sqrt(m)
    valha em TODO m>=1 da trajetoria de n0."""
    logs = trajectory_log2(n0)
    log_n0 = logs[0]
    c_min = 0.0
    worst_m = 0
    for m, log_nm in enumerate(logs):
        if m == 0:
            continue
        excess = log_nm - log_n0 + m * DELTA
        if excess > 0:
            c_needed = excess / math.sqrt(m)
            if c_needed > c_min:
                c_min = c_needed
                worst_m = m
    return c_min, worst_m, len(logs) - 1


def test_random_seeds(n_samples, log_lo, log_hi, seed=1):
    rng = random.Random(seed)
    print(f"=== C_min para {n_samples} seeds aleatorios, log10 n0 em [{log_lo},{log_hi}) ===")
    worst_overall = (0.0, None, None, None)
    for _ in range(n_samples):
        n0 = int(10 ** rng.uniform(log_lo, log_hi)) | 1
        c_min, worst_m, length = c_min_for_seed(n0)
        if c_min > worst_overall[0]:
            worst_overall = (c_min, n0, worst_m, length)
    c, n0, wm, length = worst_overall
    print(f"  Pior C_min encontrado: {c:.3f} em n0={n0} (m={wm} de {length} passos)")
    return worst_overall


def test_known_delay_records():
    """Numeros conhecidos por terem orbitas anormalmente longas/lentas
    para seu tamanho (recordistas de atraso/total stopping time,
    catalogados na literatura classica de Collatz e OEIS)."""
    print("\n=== C_min para recordistas de atraso conhecidos ===")
    known = [27, 703, 871, 6171, 77031, 837799, 8400511,
             63728127, 670617279, 9780657630, 75128138247, 989345275647]
    worst = (0.0, None, None, None)
    for n0 in known:
        c_min, worst_m, length = c_min_for_seed(n0)
        print(f"  n0={n0:>15}  C_min={c_min:.3f}  (m={worst_m} de {length} passos)")
        if c_min > worst[0]:
            worst = (c_min, n0, worst_m, length)
    return worst


def test_adversarial_long_a1_runs():
    """Constroi adversarialmente sementes com longas sequencias de
    a_i=1 (passo impar com valuacao minima, o caso que MAIS atrasa o
    decrescimo) para tentar quebrar o limite deliberadamente."""
    print("\n=== C_min para sementes adversariais (buscando longas sequencias a_i=1) ===")
    # gera candidatos: 2^k - 1 e variantes proximas tendem a ter
    # sequencias iniciais de valuacao baixa
    candidates = []
    for k in range(10, 60):
        candidates.append(2 ** k - 1)
        candidates.append(2 ** k + 1)
        candidates.append(3 * 2 ** k - 1)
    worst = (0.0, None, None, None)
    for n0 in candidates:
        if n0 % 2 == 0:
            continue
        c_min, worst_m, length = c_min_for_seed(n0)
        if c_min > worst[0]:
            worst = (c_min, n0, worst_m, length)
    c, n0, wm, length = worst
    print(f"  Pior C_min encontrado: {c:.3f} em n0={n0} (m={wm} de {length} passos)")
    return worst


if __name__ == "__main__":
    print(f"delta = 2 - log2(3) = {DELTA:.6f}\n")
    r1 = test_random_seeds(20000, 1, 4)      # ate 10^4, faixa testada pelo paper
    r2 = test_random_seeds(20000, 4, 9)      # muito alem da faixa testada pelo paper
    r3 = test_known_delay_records()
    r4 = test_adversarial_long_a1_runs()

    print("\n=== Resumo ===")
    print(f"Alegacao do paper: C <= 5 (universal, testado so ate n0<=3e4)")
    for label, r in [("aleatorio ate 1e4", r1), ("aleatorio 1e4-1e9", r2),
                     ("recordistas de atraso", r3), ("adversarial (runs de a=1)", r4)]:
        print(f"  {label}: pior C_min = {r[0]:.3f}  (n0={r[1]})")
