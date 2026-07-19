#!/usr/bin/env python3
"""
H-129 (teste de otimização ergódica): diagnóstico direto de concentração
da medida de Gibbs quenched na trajetória GULOSA (sempre o menor a
admissível a cada passo), conforme a profundidade k cresce.

Motivação (ver H-129, addendum do Fable): o congelamento já provado
(Proposição prop:always-frozen, raiz MAIOR alpha_+ sempre congelada)
deveria, na leitura de otimização ergódica/formalismo termodinâmico a
temperatura zero, corresponder a uma medida de Gibbs que se CONCENTRA
numa órbita/medida maximizante conforme a profundidade cresce -- ao
contrário da fase não-congelada (raiz menor alpha_-), onde a entropia
combinatória de caminhos concorrentes deveria manter a massa espalhada.

O ramo guloso (menor a admissível a cada passo) tem sempre o MAIOR peso
individual (q*2^-a)^alpha (decrescente em a) -- é o candidato natural a
"órbita otimizante" citado no addendum do Fable, MESMO sabendo (Fable,
item 4) que ele só é um ponto fixo genuino para q=2^a-+1 (Mersenne/
Fermat). Aqui testamos algo mais fraco e mais robusto: não se o ramo
guloso é um CICLO fechado, mas se a medida de Gibbs quenched concentra
NELE (probabilidade de seguir o ramo guloso em TODOS os k passos)
conforme k cresce -- prevista -> 1 na fase congelada (alpha_+), e
prevista ficar longe de 1 (ou decair) na fase não-congelada (alpha_-).

Método: reusa a mesma DP memoizada Z_k(alpha; u) já validada em
stage1_exact_moment_test.py (E-103) e verify_freezing_clean.py, mas
para uma raiz FIXA (nao populacao inteira -- muito mais barato em
profundidade). Define

    p_greedy(k) = P_quenched(caminho de k passos = sempre o ramo guloso)
                = prod_{i=1}^{k} peso(a0_i) / Z_k(alpha; u0)

calculado incrementalmente ao longo do proprio caminho guloso (nao
precisa recomputar do zero a cada k).
"""
import sys, math, json, time

sys.setrecursionlimit(200000)


def make_Z(q, alpha, a_max=60):
    memo = {}

    def Z(depth, u0):
        if depth == 0:
            return 1.0
        key = (depth, u0)
        cached = memo.get(key)
        if cached is not None:
            return cached
        mod_next = q ** (depth - 1)
        u0_modq = u0 % q
        total = 0.0
        if u0_modq != 0:
            for a in range(1, a_max + 1):
                if (pow(2, a, q) * u0_modq) % q != 1:
                    continue
                weight = (q * 2.0 ** (-a)) ** alpha
                if weight < 1e-16:
                    break
                num = (2 ** a) * u0 - 1
                w = (num // q) % mod_next
                total += weight * Z(depth - 1, w)
        memo[key] = total
        return total

    return Z, memo


def a0(u0_modq, q, a_max=60):
    """menor a admissivel para u0 mod q (ramo guloso)."""
    for a in range(1, a_max + 1):
        if (pow(2, a, q) * u0_modq) % q == 1:
            return a
    return None


def greedy_path_residues(u0, q, k_max):
    """retorna lista de (a_i, residuo_apos_passo_i mod q^{k_max-i}) seguindo
    sempre o ramo guloso, e o produto acumulado de pesos (sem alpha, guardamos
    a lista de a_i para aplicar alpha depois)."""
    residues = [u0 % (q ** k_max)]
    a_list = []
    u = u0 % (q ** k_max)
    mod_cur = q ** k_max
    for i in range(k_max):
        r = u % q
        a = a0(r, q)
        assert a is not None, f"residuo {r} mod {q} sem ramo guloso (gcd(u,q)!=1?)"
        mod_next = q ** (k_max - i - 1)
        num = (2 ** a) * u - 1
        assert num % q == 0
        u = (num // q) % mod_next
        mod_cur = mod_next
        a_list.append(a)
        residues.append(u)
    return a_list, residues


def run(q, alpha, alpha_label, u0_seed, k_max, a_max=60):
    Z, memo = make_Z(q, alpha, a_max=a_max)
    a_list, residues = greedy_path_residues(u0_seed, q, k_max)

    print(f"--- q={q} alpha={alpha:.6f} ({alpha_label}) u0_seed={u0_seed} ---", flush=True)
    results = []
    log_weight_cum = 0.0
    for k in range(1, k_max + 1):
        a_k = a_list[k - 1]
        weight_k = (q * 2.0 ** (-a_k)) ** alpha
        log_weight_cum += math.log(weight_k)

        u0_at_depth_k = u0_seed % (q ** k)
        t0 = time.time()
        Zk = Z(k, u0_at_depth_k)
        dt = time.time() - t0

        if Zk <= 0:
            p_greedy = None
        else:
            p_greedy = math.exp(log_weight_cum) / Zk if log_weight_cum > -700 else 0.0

        print(f"  k={k:3d}  a_k={a_k:3d}  Z_k={Zk:.6e}  p_greedy={p_greedy}  "
              f"memo={len(memo):>9d}  tempo={dt:.2f}s", flush=True)
        results.append({"k": k, "a_k": a_k, "Z_k": Zk, "p_greedy": p_greedy, "memo_size": len(memo)})

    return results


def main():
    all_results = {}

    # q=3: alpha_plus=2 (congelada), alpha_minus=1 (nao-congelada)
    all_results["q3_alpha_plus"] = run(3, 2.0, "congelada (alpha_+)", u0_seed=1, k_max=20)
    print(flush=True)
    all_results["q3_alpha_minus"] = run(3, 1.0, "nao-congelada (alpha_-)", u0_seed=1, k_max=20)
    print(flush=True)

    # q=5: alpha_plus=1 (congelada), alpha_minus=0.650918639898 (nao-congelada)
    all_results["q5_alpha_plus"] = run(5, 1.0, "congelada (alpha_+)", u0_seed=1, k_max=16)
    print(flush=True)
    all_results["q5_alpha_minus"] = run(5, 0.650918639898, "nao-congelada (alpha_-)", u0_seed=1, k_max=16)
    print(flush=True)

    with open("greedy_concentration_results.json", "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print("Resultados salvos em greedy_concentration_results.json")


if __name__ == "__main__":
    main()
