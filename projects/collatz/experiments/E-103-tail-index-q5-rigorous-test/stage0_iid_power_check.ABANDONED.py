#!/usr/bin/env python3
"""
ABANDONADO (2026-07-18): alem do problema de circularidade ja apontado
pelo Fable (o s* desse modelo i.i.d. cai exatamente na identidade de
pressao anelada, avaliada no ponto que ja provamos estar sempre
congelado -- o teste nao pode falhar por construcao), este script tem
um problema mais grave, descoberto ao rodar: a contagem BRUTA de nos
(nao ponderada) explode combinatoriamente sob fase i.i.d. independente
por no. Teste direto: para headroom=100, a arvore REAL aritmetica
(count_tree de empirical_qx1_tree.py) da 42 nos; esta versao i.i.d.
gerou >200000 nos antes de ser interrompida, para o MESMO headroom
relativo. A identidade de pressao anelada (Lema de bijeicao de fibra,
no paper) e sobre MOMENTOS PONDERADOS Z_k(alpha) = soma de pesos
(q*2^-a)^alpha, nao sobre contagem bruta de nos -- os dois sao objetos
matematicos diferentes, e nao ha garantia a priori de que a contagem
bruta fique sub-linear (x^0.65) so porque a soma ponderada em alpha_-
e subcritica. A correlacao real entre residuo do pai e do filho
(que este script remove, assumindo fase uniforme independente) parece
ser ESSENCIAL para manter a arvore rala -- ainda nao entendemos
exatamente por que, mas o fato empirico e claro. Substituido por uma
abordagem analitica (matriz de transferencia sobre residuos reais mod
5^m, sem simulacao de arvore i.i.d.) -- ver consulta ao Fable e
full_battery.py / stage1_*.py.
"""
import random, math, json, time

Q = 5
ORD_Q_2 = 4  # ord_5(2) = 4 (2^4=16=1 mod5)
ALPHA1 = 0.650918639898
A_MAX = 60  # trunca quando peso 5*2^-a fica desprezivel (a=60 -> 5*2^-60 ~ 4e-18)

N_ROOTS = 5000
H_LEVELS = [10**5, 10**6, 10**7, 10**8]
LOG2 = math.log(2)
LOGQ = math.log(Q)


def count_tree_iid(rng, log_x_max, checkpoints_logx):
    """
    DFS na arvore i.i.d.: cada no tem uma fase phi~Uniforme{1..4}
    independente, filhos em a=phi, phi+4, phi+8,... (log_size_filho =
    log_size_pai + a*log2 - logQ). Conta nos com log_size <= log_x_max,
    parando de descer quando log_size ja excede o maior checkpoint.
    """
    cps = sorted(checkpoints_logx)
    counts = [0] * len(cps)
    total = 0
    stack = [0.0]  # log_size da raiz = 0 (log(1), tamanho unitario normalizado)
    while stack:
        log_size = stack.pop()
        total += 1
        for i, cp in enumerate(cps):
            if log_size <= cp:
                counts[i] += 1
        if log_size > log_x_max:
            continue
        phi = rng.randrange(1, ORD_Q_2 + 1)
        a = phi
        while a <= A_MAX:
            child_log = log_size + a * LOG2 - LOGQ
            if child_log <= log_x_max:
                stack.append(child_log)
            a += ORD_Q_2
    return total, counts


def sample_one_root(rng, H_levels):
    log_x_max = math.log(H_levels[-1])
    checkpoints_logx = [math.log(H) for H in H_levels]
    tot, counts = count_tree_iid(rng, log_x_max, checkpoints_logx)
    return counts


def main():
    rng = random.Random(20260718)
    t0 = time.time()
    W_by_level = {H: [] for H in H_LEVELS}

    for idx in range(N_ROOTS):
        counts = sample_one_root(rng, H_LEVELS)
        for H, c in zip(H_LEVELS, counts):
            W = c / (H ** ALPHA1)
            W_by_level[H].append(W)
        if (idx + 1) % 500 == 0:
            dt = time.time() - t0
            print(f"  {idx+1}/{N_ROOTS} raizes sinteticas processadas ({dt:.1f}s)", flush=True)

    dt = time.time() - t0
    print(f"Total: {dt:.1f}s", flush=True)

    with open("/tmp/tail_index_q5_synthetic_iid_raw.json", "w") as f:
        json.dump({str(k): v for k, v in W_by_level.items()}, f)
    print("Amostras sinteticas salvas em /tmp/tail_index_q5_synthetic_iid_raw.json", flush=True)


if __name__ == "__main__":
    main()
