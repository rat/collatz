"""
E-038 - Estrutura nao-linear entre features de n e features de m=(3n+1)/2^a,
alem do que H-025 (correlacao linear bit-a-bit) ja testou e refutou.

Motivado por uma resposta de IA externa sugerindo "Project PHI" (embedding
rico + busca de estrutura) e um "campo vetorial" Delta(n)=Phi(T(n))-Phi(n).
Ja identificamos que a formulacao linear dessa ideia (Koopman/DMD) reduz a
H-025 (BACKLOG.md: "Koopman operator/DMD vetorial - DESCARTADO"). Este
experimento testa a generalizacao honesta: existe dependencia NAO-linear
(mutual information, nao Pearson) entre um conjunto mais rico de features
de n (peso de Hamming, residuos mod primos nao usados na familia de
exclusao, a proxima valuacao a2) e features de m, condicionando em a fixo,
alem do que ja e explicado por a + carry?

Metodo: para cada par (feature de n, feature de m), calcula MI empirica
condicionada em a=k, e compara contra um null de embaralhamento (shuffle
de n dentro do mesmo grupo de a, preservando m) - se MI real nao for muito
maior que MI do null, nao ha estrutura alem de ruido de amostra finita.

Inclui dois "controles positivos" esperados (para validar que o metodo
funciona): mod9(n) vs mod9(m) (mecanismo ja conhecido, H-007/H-008/H-022) e
low4(n) vs low4(m) (mecanismo de carry ja identificado em H-025).
"""
import numpy as np
import random
import sys

random.seed(20260713)
np.random.seed(20260713)


def accel_step(n):
    m = 3 * n + 1
    a = 0
    while m % 2 == 0:
        m //= 2
        a += 1
    return m, a


def mutual_info(x, y):
    """MI empirica (bits) entre dois vetores inteiros (ja discretos)."""
    x = np.asarray(x)
    y = np.asarray(y)
    _, xidx = np.unique(x, return_inverse=True)
    _, yidx = np.unique(y, return_inverse=True)
    nx = xidx.max() + 1
    ny = yidx.max() + 1
    joint = np.zeros((nx, ny))
    np.add.at(joint, (xidx, yidx), 1)
    joint /= joint.sum()
    px = joint.sum(axis=1, keepdims=True)
    py = joint.sum(axis=0, keepdims=True)
    nz = joint > 0
    ratio = np.ones_like(joint)
    ratio[nz] = joint[nz] / (px * py)[nz]
    return float(np.sum(joint[nz] * np.log2(ratio[nz])))


def shuffled_mi_stats(x, y, n_shuffles=15):
    vals = []
    x = np.asarray(x).copy()
    for _ in range(n_shuffles):
        np.random.shuffle(x)
        vals.append(mutual_info(x, y))
    return float(np.mean(vals)), float(np.std(vals))


def build_sample(n_samples, bit_low=24, bit_high=25):
    lo, hi = 2 ** bit_low, 2 ** bit_high
    ns = []
    seen = set()
    while len(ns) < n_samples:
        cand = random.randrange(lo, hi) | 1  # forca impar
        if cand in seen:
            continue
        seen.add(cand)
        ns.append(cand)
    return ns


def features_n(n):
    # nota: bits baixos (~a+1 primeiros bits) sao fixados pela propria
    # condicao "a fixo" (H-025 ja mostrou/explicou isso) - NAO incluir
    # features de baixa ordem aqui, senao viram variaveis degeneradas
    # (variancia zero) e a MI fica trivialmente 0/indefinida.
    return {
        'hamming': bin(n).count('1'),
        'mod5': n % 5,
        'mod7': n % 7,
        'mod9': n % 9,
        'mod11': n % 11,
        'mid4_10_13': (n >> 10) & 0xF,   # janela distante do carry de baixa ordem
        'topbyte': (n >> 17) & 0xFF,      # bits altos (topo, longe do carry)
    }


def features_m(m, a2):
    return {
        'a2': a2,
        'hamming': bin(m).count('1'),
        'mod5': m % 5,
        'mod7': m % 7,
        'mod9': m % 9,
        'mod11': m % 11,
    }


def main(n_samples=300_000, a_values=(1, 2, 3, 4, 5, 6), n_shuffles=15):
    print(f"Amostrando {n_samples} n impares em [2^24, 2^25)...")
    ns = build_sample(n_samples)

    data = {k: [] for k in features_n(1)}
    data_m = {k: [] for k in features_m(1, 1)}
    a_list = []

    for n in ns:
        m, a = accel_step(n)
        _, a2 = accel_step(m)
        fn = features_n(n)
        fm = features_m(m, a2)
        for k, v in fn.items():
            data[k].append(v)
        for k, v in fm.items():
            data_m[k].append(v)
        a_list.append(a)

    a_arr = np.array(a_list)
    for k in data:
        data[k] = np.array(data[k])
    for k in data_m:
        data_m[k] = np.array(data_m[k])

    print(f"Distribuicao de a: ", {k: int(np.sum(a_arr == k)) for k in a_values})
    print()

    results = []
    for a_fix in a_values:
        mask = a_arr == a_fix
        n_in_group = int(mask.sum())
        if n_in_group < 200:
            print(f"a={a_fix}: amostra pequena demais ({n_in_group}), pulando.")
            continue
        print(f"=== a={a_fix} (n={n_in_group}) ===")
        for fn_name, fn_vals in data.items():
            x = fn_vals[mask]
            if len(np.unique(x)) < 2:
                continue  # variavel degenerada (variancia zero) - MI indefinida/trivial
            for fm_name, fm_vals in data_m.items():
                y = fm_vals[mask]
                if len(np.unique(y)) < 2:
                    continue
                mi_real = mutual_info(x, y)
                mi_null_mean, mi_null_std = shuffled_mi_stats(x, y, n_shuffles)
                if mi_null_std <= 1e-12:
                    continue  # null tambem degenerado, z-score nao interpretavel
                z = (mi_real - mi_null_mean) / mi_null_std
                results.append((a_fix, fn_name, fm_name, mi_real, mi_null_mean, mi_null_std, z))
        sys.stdout.flush()

    # pares "triviais": mesmo nome de residuo em n e m (ex: mod9 vs mod9) sao
    # explicados por identidade algebrica direta de (3n+1)/2^a mod k - servem
    # so como controle positivo (confirmam que o metodo de MI funciona).
    trivial_names = {'mod5', 'mod7', 'mod9', 'mod11'}

    def is_trivial(r):
        return r[1] == r[2] and r[1] in trivial_names

    trivial = [r for r in results if is_trivial(r)]
    interesting = [r for r in results if not is_trivial(r)]

    def print_table(rows, title):
        print(f"\n=== {title} ===")
        print(f"{'a':>3} {'feature(n)':<14} {'feature(m)':<10} {'MI_real':>10} {'MI_null':>10} {'std_null':>10} {'z':>10}")
        for r in rows:
            a_fix, fn_name, fm_name, mi_real, mi_null_mean, mi_null_std, z = r
            print(f"{a_fix:>3} {fn_name:<14} {fm_name:<10} {mi_real:>10.5f} {mi_null_mean:>10.5f} {mi_null_std:>10.5f} {z:>10.1f}")

    trivial.sort(key=lambda r: -r[-1])
    print_table(trivial, "Controle positivo (mod_k(n) vs mod_k(m), esperado deterministico)")

    interesting.sort(key=lambda r: -r[-1])
    print_table(interesting, "TODOS os pares nao-triviais, por z-score decrescente")

    return results


if __name__ == "__main__":
    n_samples = int(sys.argv[1]) if len(sys.argv) > 1 else 300_000
    main(n_samples=n_samples)
