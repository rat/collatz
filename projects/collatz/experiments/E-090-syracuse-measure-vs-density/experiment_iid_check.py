#!/usr/bin/env python3
"""
E-090 (extensao 2026-07-16, parte 2) - testa diretamente a hipotese de
trabalho de que a heuristica de valuacoes i.i.d. Geometrica(1/2) por
tras da medida de Tao (Lemma 1.12) tende a falhar mais conforme
condicionamos v numa classe residual mod 3^m mais fina - o que
explicaria por que a correlacao 3^m*mu(r) vs G(v) medido PIORA para m
grande (ver experiment_extended.py).

Teste: gera a sequencia de valuacoes a_1,a_2,...,a_K da orbita de
Syracuse acelerada a partir de v (a_i = v_2(3*n_i+1)), para v amostrado
SEM restricao de residuo (baseline) vs. v amostrado com residuo FIXO
mod 3^m (para m crescente). Compara autocorrelacao lag-1 media da
sequencia (a_i) entre os grupos - se a heuristica i.i.d. vale (mesmo
condicionado ao residuo mod 3^m, que e coprimo com 2), a autocorrelacao
deveria ficar em ~0 em todos os casos (por CRT, residuo mod 3^m nao
deveria carregar informacao sobre a sequencia de valuacoes 2-adicas
completa - MAS a pergunta real e se a propria SEQUENCIA de valuacoes,
uma vez que sabemos que a orbita permanece consistente com aquele
residuo mod 3^m em CADA passo/nivel da recursao da arvore reversa
(nao so no v inicial), fica correlacionada.

Reproduzir: python3 experiment_iid_check.py
"""
import random
import statistics


def syracuse_valuations(n, k_steps):
    """Sequencia de valuacoes a_1..a_k da orbita acelerada de Syracuse
    partindo do impar n. Retorna None se n deixa de ser positivo (nao
    deveria acontecer para n grande e k_steps << log2(n))."""
    vals = []
    cur = n
    for _ in range(k_steps):
        m = 3 * cur + 1
        a = 0
        while m % 2 == 0:
            m //= 2
            a += 1
        vals.append(a)
        cur = m
        if cur <= 0:
            return None
    return vals


def lag1_autocorr(sequences):
    """Autocorrelacao lag-1 media, agregando todas as sequencias (cada
    uma contribui varios pares consecutivos (a_i, a_{i+1}))."""
    xs, ys = [], []
    for seq in sequences:
        for i in range(len(seq) - 1):
            xs.append(seq[i])
            ys.append(seq[i + 1])
    n = len(xs)
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    cov = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys)) / n
    var_x = sum((x - mean_x) ** 2 for x in xs) / n
    var_y = sum((y - mean_y) ** 2 for y in ys) / n
    corr = cov / (var_x * var_y) ** 0.5 if var_x > 0 and var_y > 0 else None
    return corr, statistics.mean(xs), statistics.pvariance(xs), n


def sample_v_with_residue(rng, mod_k, r, log_lo, log_hi, seen, max_tries=2000):
    """Amostra v distinto (nunca repetido dentro do grupo, ver seen) com
    v = r mod mod_k, na janela [10^log_lo, 10^log_hi)."""
    for _ in range(max_tries):
        mag = int(10 ** rng.uniform(log_lo, log_hi))
        if mag < mod_k:
            continue
        base = (mag // mod_k) * mod_k + r
        if base < mag:
            base += mod_k
        if base % 2 == 1 and base not in seen:
            seen.add(base)
            return base
    return None


def window_for_mod_k(mod_k, min_distinct=200):
    """Janela de magnitude ampla o suficiente para conter pelo menos
    min_distinct candidatos distintos com o residuo fixado - evita o
    bug de reamostragem do mesmo v repetidamente (ja visto em E-089)."""
    log_lo = 6.0
    while (10 ** (log_lo + 1.0) - 10 ** log_lo) / mod_k < min_distinct:
        log_lo += 1.0
    return log_lo, log_lo + 1.0


def run_group(label, mod_k, r_or_none, n_samples, k_steps, seed):
    rng = random.Random(seed)
    seqs = []
    seen = set()
    if mod_k is not None:
        log_lo, log_hi = window_for_mod_k(mod_k, min_distinct=max(200, n_samples // 2))
    else:
        log_lo, log_hi = 6.0, 7.0
    for _ in range(n_samples):
        if r_or_none is None:
            v = rng.randrange(10 ** 6, 10 ** 7) | 1
            while v in seen:
                v = rng.randrange(10 ** 6, 10 ** 7) | 1
            seen.add(v)
        else:
            v = sample_v_with_residue(rng, mod_k, r_or_none, log_lo, log_hi, seen)
        if v is None:
            continue
        seq = syracuse_valuations(v, k_steps)
        if seq is not None:
            seqs.append(seq)
    corr, mean_a, var_a, n_pairs = lag1_autocorr(seqs)
    print(f"{label:38s} n_traj={len(seqs):5d} n_pairs={n_pairs:6d} "
          f"autocorr_lag1={corr:+.4f}  E[a]={mean_a:.3f} Var[a]={var_a:.3f}")
    return corr


def main():
    print("=== Autocorrelacao lag-1 das valuacoes a_i, com e sem residuo fixo mod 3^m ===")
    print("(i.i.d. Geometrica(1/2) preveria autocorr ~ 0 em todos os casos)\n")

    K_STEPS = 25
    N_SAMPLES = 4000

    run_group("baseline (v irrestrito)", None, None, N_SAMPLES, K_STEPS, seed=1)

    for m in [2, 4, 6, 8, 10, 12]:
        mod_k = 3 ** m
        r = 1  # residuo fixo arbitrario, nao multiplo de 3
        run_group(f"residuo r=1 mod 3^{m}", mod_k, r, N_SAMPLES, K_STEPS, seed=1)


if __name__ == "__main__":
    main()
