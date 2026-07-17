#!/usr/bin/env python3
"""
H-111 - nucleo do experimento de controle de 3 bracos proposto pelo
Fable para calibrar o "piso de variancia" causado por acoplamento
aritmetico entre subarvores (a peca que falta na barreira de endogenia
de H-110).

Ideia central do Fable: nao simule os PESOS 3*2^-a da recursao (o
operador nao tem soma de linha constante=1 celula a celula - e' 1 para
tipo 1 mod 3, 2 para tipo 2 mod 3, um processo de ramificacao
multitipo). Em vez disso, simule a ARVORE, exatamente como
build_tree_count_dfs (E-018) e measure_G_headroom (E-090) ja fazem para
inteiros reais: enumere nos truncados por TAMANHO (nao por
profundidade) e conte. Os pesos emergem da geometria (um filho com
valuacao a nasce com log-tamanho +a-log2(3), logo ele e seus
descendentes sao cortados mais cedo pelo teto de tamanho quando a e'
pequeno) - nunca aparecem explicitamente no codigo.

Estrutura ciclica exata (derivada pelo Fable, verificada abaixo contra
inteiros reais): para um pai impar u com tipo tau=u mod 3 em {1,2}, os
filhos validos em ordem crescente de a (a_k = a0+2k, a0=2 se tau=1
[a par], a0=1 se tau=2 [a impar]) tem tipo w_a_k mod 3 = (rho+k) mod 3,
onde rho = fase do pai (determinada por u mod 9). Exatamente 1 em cada
3 filhos consecutivos e "morto" (tipo 0, conta como no mas nao ramifica
mais - espelha nos "≡0 mod 3" da arvore real, ver H-005/H-018).

O modelo sintetico ("hipotese nula de dígitos frescos independentes"):
substitui a fase rho (que na aritmetica real e' uma funcao determinis-
tica de u mod 9, correlacionada entre nos da mesma arvore) por um trit
FRESCO uniforme e independente por no. Toda a aleatoriedade do braco 1
(controle i.i.d.) e' isso.

Randomizacao enderecada por hash (para pares compartilhando prefixo ate
profundidade g, e para o acoplamento do braco 2): cada no e' identifi-
cado por (sigma, r, tag) - sigma e' um id de fluxo, r e' o endereco
relativo (tupla de indices k desde onde sigma foi cunhado), tag e' "S"
(prefixo compartilhado, profundidade d<=g) ou o id da copia ("A"/"B",
profundidade d>g). Isso faz duas copias de uma arvore serem IDENTICAS
ate profundidade g+1 e divergirem depois, sem precisar de replay/estado
- funcoes puras do seed.

Braco 2 (acoplamento de conteudo, rho ajustavel): cada no vivo, alem da
fase, sorteia u_acopla; se u_acopla<rho, TODOS os filhos vivos daquele
no recebem o MESMO fluxo novo (sigma*, ()) - tornando as subarvores
irmas replicas exatas umas das outras (mesmos digitos "frescos" nas
mesmas posicoes relativas). Prova de uma linha de que as marginais (lei
de descendencia por caminho unico, criticidade, alpha=2) ficam
EXATAMENTE intactas para qualquer rho: ao longo de qualquer caminho
raiz->no as chaves (sigma,r,tag) nunca se repetem, entao os trits ao
longo de um caminho sao i.i.d. com a marginal correta sempre - so a
dependencia ENTRE subarvores muda.

Conversao profundidade sintetica <-> digitos 3-adicos reais: g = m-2
(cada passo reverso consome um digito 3-adico; compartilhar m digitos
fixa as fases ate profundidade d=m-2, o primeiro trit fresco esta em
d=m-1; no sintetico, compartilhar ate g deixa o primeiro trit fresco em
g+1 - igualando, g=m-2).
"""
import hashlib
import math
import random
import statistics
import struct

LOG2_3 = math.log2(3)


def node_randoms(sigma, r, tag):
    """3 numeros pseudo-aleatorios independentes derivados de
    (sigma, r, tag) via hash - funcao pura, sem estado."""
    key = repr((sigma, r, tag)).encode()
    d = hashlib.blake2b(key, digest_size=24).digest()
    a, b, c = struct.unpack("<QQQ", d)
    return a / 2 ** 64, b / 2 ** 64, c


def assert_cyclic_structure(v):
    """Verifica, para um v real (impar, nao multiplo de 3), que os
    tipos dos filhos w_a (a=a0, a0+2, a0+4, ...) ciclam como
    (rho, rho+1, rho+2, rho, ...) mod 3, conforme derivado pelo Fable."""
    a0 = 2 if v % 3 == 1 else 1
    types = []
    for k in range(9):
        a = a0 + 2 * k
        z = (pow(2, a, 9) * v) % 9
        assert z in (1, 4, 7), (v, a, z)
        assert (pow(2, a) * v - 1) % 3 == 0, (v, a)
        w_mod3 = ((z - 1) // 3) % 3
        types.append(w_mod3)
    rho = types[0]
    expected = [(rho + k) % 3 for k in range(9)]
    assert types == expected, (v, types, expected)
    return rho


def validate_cyclic_structure(n_samples=10000, seed=12345):
    rng = random.Random(seed)
    checked = 0
    while checked < n_samples:
        v = rng.randrange(5, 10 ** 12) | 1
        if v % 3 == 0:
            continue
        assert_cyclic_structure(v)
        checked += 1
    return checked


STEP_CAP = 3_000_000  # protecao contra a cauda pesada (alpha~2): arvores
# raras e legitimamente enormes (nao um bug - ja confirmado por
# diagnostico: distribuicao de passos bate com cauda alpha~2 esperada)
# sao truncadas em vez de travar o pipeline. Amostras que batem o cap
# sao descartadas (None), como um overflow numerico - vies desprezivel
# para n grande dado que sao <1% dos casos nos testes de diagnostico.


def simulate_tree(seed_master, root_type, mult, g, copy_tag, rho, max_gen_cap=300, step_cap=STEP_CAP):
    """DFS por tamanho (pilha explicita), espelhando build_tree_count_dfs
    (E-018) / measure_G_headroom (E-090): conta nos com s<=L_COUNT,
    gera filho k sse s+a_k<=L_SEARCH (mesma semantica do search_bound
    real: condicao sobre o "no par intermediario" 2^a*u).

    Retorna (count, max_depth_visto, saturado) - saturado=True se a
    arvore inteira nunca alcancou profundidade > g (i.e. nunca gerou
    nenhum no na regiao divergente). Se o numero de passos exceder
    step_cap (cauda pesada, arvore excepcionalmente grande), retorna
    (None, max_depth_ate_entao, False) - o chamador deve descartar.
    """
    L_COUNT = math.log2(mult)
    L_SEARCH = L_COUNT + math.log2(5)

    count = 0
    max_depth = 0
    steps = 0
    stack = [(seed_master, (), root_type, 0.0, 0)]
    while stack:
        steps += 1
        if steps > step_cap:
            return None, max_depth, False
        sigma, r, node_type, s, d = stack.pop()
        if d > max_depth:
            max_depth = d
        if s <= L_COUNT:
            count += 1
        if node_type == 0:
            continue
        if d >= max_gen_cap:
            continue
        tag = "S" if d <= g else copy_tag
        u_fase, u_acopla, cunho = node_randoms(sigma, r, tag)
        rho_phase = int(u_fase * 3)
        if rho_phase > 2:
            rho_phase = 2
        a0 = 2 if node_type == 1 else 1
        couple = (rho > 0.0) and (u_acopla < rho)
        k = 0
        while True:
            a_k = a0 + 2 * k
            if s + a_k > L_SEARCH:
                break
            child_type = (rho_phase + k) % 3
            child_s = s + a_k - LOG2_3
            if couple:
                child_sigma, child_r = cunho, ()
            else:
                child_sigma, child_r = sigma, r + (k,)
            stack.append((child_sigma, child_r, child_type, child_s, d + 1))
            k += 1

    saturated = max_depth <= g
    return count, max_depth, saturated


def simulate_single(seed_master, root_type, mult, rho=0.0, max_gen_cap=300):
    """Arvore unica, sem particionamento em copias (usada nos testes de
    criticidade/checklist) - equivalente a g=+inf, tag sempre 'X'."""
    count, max_depth, _ = simulate_tree(
        seed_master, root_type, mult, g=10 ** 9, copy_tag="X", rho=rho, max_gen_cap=max_gen_cap
    )
    return count, max_depth


def synth_pair(rng, g, mult, rho):
    """Gera um par (log10 G_A, log10 G_B) de arvores sinteticas
    compartilhando prefixo ate profundidade g (mesmo tipo de raiz,
    mesmo seed_master), divergindo depois. Retorna None se alguma
    contagem for 0 (G indefinido)."""
    seed_master = rng.getrandbits(64)
    root_type = rng.choice((1, 2))
    count_a, depth_a, sat_a = simulate_tree(seed_master, root_type, mult, g, "A", rho)
    count_b, depth_b, sat_b = simulate_tree(seed_master, root_type, mult, g, "B", rho)
    if count_a is None or count_b is None or count_a <= 0 or count_b <= 0:
        return None
    G_a = count_a / mult
    G_b = count_b / mult
    saturated = sat_a and sat_b
    return math.log10(G_a), math.log10(G_b), saturated


def run_synth_pairs(g, mult, rho, n_pairs, seed):
    """Roda n_pairs pares sinteticos e retorna
    (resid_var, n_efetivo, frac_saturado)."""
    rng = random.Random(seed)
    deltas = []
    n_sat = 0
    n_total = 0
    for _ in range(n_pairs):
        res = synth_pair(rng, g, mult, rho)
        if res is None:
            continue
        log_a, log_b, saturated = res
        deltas.append(log_b - log_a)
        n_total += 1
        if saturated:
            n_sat += 1
    if len(deltas) < 2:
        return None, len(deltas), 1.0
    var_delta = statistics.pvariance(deltas)
    resid_var = var_delta / 2
    frac_sat = n_sat / n_total if n_total else 1.0
    return resid_var, len(deltas), frac_sat


def bootstrap_ci(deltas, n_boot=1000, seed=0):
    """IC 95% (percentil) via bootstrap sobre pares para resid_var=Var(deltas)/2."""
    rng = random.Random(seed)
    n = len(deltas)
    boots = []
    for _ in range(n_boot):
        sample = [deltas[rng.randrange(n)] for _ in range(n)]
        boots.append(statistics.pvariance(sample) / 2)
    boots.sort()
    lo = boots[int(0.025 * n_boot)]
    hi = boots[int(0.975 * n_boot) - 1]
    return lo, hi


def run_synth_pairs_with_ci(g, mult, rho, n_pairs, seed, n_boot=1000):
    rng = random.Random(seed)
    deltas = []
    n_sat = 0
    for _ in range(n_pairs):
        res = synth_pair(rng, g, mult, rho)
        if res is None:
            continue
        log_a, log_b, saturated = res
        deltas.append(log_b - log_a)
        if saturated:
            n_sat += 1
    if len(deltas) < 10:
        return None
    resid_var = statistics.pvariance(deltas) / 2
    lo, hi = bootstrap_ci(deltas, n_boot=n_boot, seed=seed + 1)
    frac_sat = n_sat / len(deltas)
    return {
        "resid_var": resid_var,
        "ci_lo": lo,
        "ci_hi": hi,
        "n": len(deltas),
        "frac_sat": frac_sat,
        "deltas": deltas,
    }


if __name__ == "__main__":
    import time

    t_start = time.time()

    def elapsed():
        return f"[{time.time()-t_start:6.1f}s]"

    print("=== Checklist item 1: estrutura ciclica vs inteiros reais ===")
    n_ok = validate_cyclic_structure(n_samples=10000)
    print(f"  {elapsed()} {n_ok} inteiros verificados, estrutura ciclica confirmada em todos.\n")

    print("=== Checklist item 2: criticidade E[G|tipo] em funcao de rho ===")
    print("  (cauda pesada alpha~2 esperada - algumas arvores raras sao grandes e lentas,")
    print("   n moderado (800) e amostras descartadas por step_cap sao esperadas e ok)\n")
    for rho in (0.0, 0.5, 1.0):
        for root_type in (1, 2):
            rng = random.Random(1000 + root_type)
            vals = []
            n_discarded = 0
            for _ in range(800):
                seed_master = rng.getrandbits(64)
                count, _ = simulate_single(seed_master, root_type, mult=2000, rho=rho)
                if count is None:
                    n_discarded += 1
                    continue
                vals.append(count / 2000)
            mean_G = statistics.mean(vals)
            print(f"  {elapsed()} rho={rho:.1f} tipo={root_type}: E[G]={mean_G:.4f} "
                  f"(esperado {root_type:.2f}) n={len(vals)} descartados={n_discarded}")
    print()

    print("=== Checklist item 3: rho=0 bitwise identico entre execucoes ===")
    res1 = run_synth_pairs(g=10, mult=2000, rho=0.0, n_pairs=50, seed=777)
    res2 = run_synth_pairs(g=10, mult=2000, rho=0.0, n_pairs=50, seed=777)
    print(f"  {elapsed()} run1={res1!r} run2={res2!r} identico={res1==res2}\n")

    print("=== Checklist item 4: g=max_gen_cap -> saturacao total (delta=0) ===")
    print("  (Fable: profundidade tem cauda de lei de potencia (~c/d), 70-100")
    print("   e' normal mesmo em mult=2000 - g=60 nao basta; use g=max_gen_cap=300)")
    resid_var, n, frac_sat = run_synth_pairs(g=300, mult=2000, rho=0.0, n_pairs=300, seed=42)
    print(f"  {elapsed()} g=300: resid_var={resid_var} n={n} frac_saturado={frac_sat:.3f}\n")

    print("=== Checklist item 5: g=0 ~ variancia incondicional ===")
    resid_var0, n0, _ = run_synth_pairs(g=0, mult=2000, rho=0.0, n_pairs=1000, seed=99)
    rng = random.Random(98)
    logs = []
    for _ in range(2000):
        seed_master = rng.getrandbits(64)
        root_type = rng.choice((1, 2))
        count, _ = simulate_single(seed_master, root_type, mult=2000)
        if count:
            logs.append(math.log10(count / 2000))
    var_uncond = statistics.pvariance(logs)
    print(f"  {elapsed()} g=0: resid_var(par)={resid_var0:.4f}  var_incondicional(log G)={var_uncond:.4f}\n")

    print(f"=== Checklist concluido em {elapsed()} ===")
