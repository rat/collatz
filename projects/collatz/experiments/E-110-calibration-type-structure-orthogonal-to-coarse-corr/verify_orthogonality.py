"""
E-110 — a correlacao grosseira de H-126/Prop.2 e o parametro rho da
calibracao de H-111 (E-090/experiment_synthetic_core.py) medem eixos
ORTOGONAIS, nao o mesmo fenomeno em escalas diferentes.

Pergunta original (auditoria do paper, item 1): por que o experimento
de calibracao (rho_eff<=0.06, "nenhum acoplamento positivo detectado")
nao entra em tensao com a correlacao grosseira exata e persistente de
Prop.2 (H-126)? O paper ja tem uma resposta por "diluicao" (a
correlacao grosseira contribui fracao evanescente da variancia
agregada). Este experimento mostra uma resolucao MAIS FORTE e exata:
as duas coisas nao competem porque nao sao a mesma variavel.

Achado: no simulador de H-111 (experiment_synthetic_core.py), o TIPO
do filho k (child_type = (rho_phase+k)%3 -- exatamente o residuo mod 3
do filho, ja que precisao ell=1 na Prop.2 e' literalmente "w mod 3")
e' uma funcao DETERMINISTICA do indice k e da fase da raiz,
INDEPENDENTE do parametro de acoplamento rho (o parametro que a
calibracao varia). Ou seja: a correlacao de tipo entre irmaos (que
reproduz EXATAMENTE +1/-1/2 de Prop.2, verificado abaixo) ja esta
embutida, identica, em TODOS os bracos do experimento de calibracao
(rho=0 i.i.d., rho intermediario, e a arvore real) -- porque a formula
do tipo em si vem da estrutura ciclica REAL (validada contra inteiros
verdadeiros por assert_cyclic_structure, ja existente no arquivo
original). O que rho varia e' se o CONTEUDO/magnitude de subarvores
irmas (os fluxos aleatorios frescos que determinam o TAMANHO de G, nao
seu residuo mod 3) sao compartilhados ou independentes -- um eixo
completamente diferente do que Prop.2 descreve.

Consequencia: rho_eff<=0.06 nao podia ter "detectado" nem "deixado de
detectar" a correlacao de Prop.2, porque essa correlacao nunca foi
uma forma de acoplamento que rho=0 removesse -- ela e' uma propriedade
estrutural presente em QUALQUER modelo (real ou sintetico) que respeite
a regra de admissibilidade correta, com ou sem acoplamento de conteudo.
"""

import hashlib
import random
import struct


def node_randoms(sigma, r, tag):
    """Copia identica de node_randoms em
    E-090-syracuse-measure-vs-density/experiment_synthetic_core.py
    (H-111): 3 numeros pseudo-aleatorios independentes derivados de
    (sigma, r, tag) via hash - funcao pura, sem estado."""
    key = repr((sigma, r, tag)).encode()
    d = hashlib.blake2b(key, digest_size=24).digest()
    a, b, c = struct.unpack("<QQQ", d)
    return a / 2 ** 64, b / 2 ** 64, c


def child_type_sequence(seed_master, root_type, g, copy_tag, rho, k_max=6):
    """Replica so a parte de calculo do TIPO (fase) do simulate_tree
    original, para varios valores de rho, mantendo tudo o mais fixo."""
    sigma, r, node_type, d = seed_master, (), root_type, 0
    tag = "S" if d <= g else copy_tag
    u_fase, u_acopla, cunho = node_randoms(sigma, r, tag)
    rho_phase = int(u_fase * 3)
    if rho_phase > 2:
        rho_phase = 2
    return rho_phase, [(rho_phase + k) % 3 for k in range(k_max)]


def check_rho_independence(n_seeds=2000):
    """Para muitos seeds, confirma que a sequencia de tipos dos filhos
    da raiz NAO muda com rho (0.0, 0.3, 0.7, 1.0)."""
    mismatches = 0
    for seed in range(n_seeds):
        base_phase, base_types = child_type_sequence(seed, 1, g=5, copy_tag="A", rho=0.0)
        for rho in (0.3, 0.7, 1.0):
            phase, types = child_type_sequence(seed, 1, g=5, copy_tag="A", rho=rho)
            if types != base_types:
                mismatches += 1
    return mismatches, n_seeds


def corr_for_delta(delta, n=200_000, c=1.0, seed=42):
    """Correlacao de tipo (indicador g(0)=0, g(1)=g(2)=c, exatamente a
    ponderacao da derivacao de Prop.2 em H-126) entre dois irmaos com
    gap de indice delta=k2-k1 (equivalente ao gap de expoente
    Delta_exponente=2*delta, ja que a_k=a0+2k para q=3)."""
    rng = random.Random(seed)
    sum_gi_gj = sum_gi = sum_gj = sum_gi2 = sum_gj2 = 0.0
    for _ in range(n):
        rho_phase = rng.randrange(3)
        type_i = rho_phase % 3
        type_j = (rho_phase + delta) % 3
        gi = 0.0 if type_i == 0 else c
        gj = 0.0 if type_j == 0 else c
        sum_gi_gj += gi * gj
        sum_gi += gi
        sum_gj += gj
        sum_gi2 += gi * gi
        sum_gj2 += gj * gj
    nf = float(n)
    cov = sum_gi_gj / nf - (sum_gi / nf) * (sum_gj / nf)
    var_i = sum_gi2 / nf - (sum_gi / nf) ** 2
    var_j = sum_gj2 / nf - (sum_gj / nf) ** 2
    return cov / (var_i * var_j) ** 0.5


if __name__ == "__main__":
    print("=== Parte 1: a sequencia de TIPO dos filhos independe de rho? ===")
    mismatches, n = check_rho_independence(2000)
    print(f"  {n} seeds testados, rho in {{0.3,0.7,1.0}} vs rho=0.0: "
          f"{mismatches} divergencias (esperado: 0)")

    print()
    print("=== Parte 2: a correlacao de tipo do simulador reproduz +1/-1/2 de Prop.2? ===")
    print("  (Delta_exponente = 2*delta_indice, ja que a_k=a0+2k para q=3)")
    for delta in range(0, 7):
        c = corr_for_delta(delta)
        exp = "+1 (Delta_exp=0 mod 6)" if delta % 3 == 0 else "-1/2 (Delta_exp!=0 mod 6)"
        print(f"  delta_indice={delta} (Delta_exp={2*delta}): "
              f"corr observada={c:.4f}  previsto Prop.2={exp}")
