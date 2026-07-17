#!/usr/bin/env python3
"""
Teste computacional direto da "Weak Covering Conjecture for Mixed Power
Sums" de Wirsching (1998, Cap. V, Conjectura 3.9) - a conjectura em
aberto ha ~30 anos que H-112 identificou como estruturalmente
equivalente ao "ingrediente que falta" da barreira de endogenia
(H-110/H-111). Ate agora so lemos SOBRE ela via forks; este e' o
primeiro teste computacional direto do objeto exato do livro.

Definicao exata (Corolario II.5.8, p.127, confirmada verbatim contra o
PDF arquivado, item 131):

    R_{j,k} := { soma_{i=0}^{j} 2^{a_i}*3^i : j+k >= a_0>a_1>...>a_j >= 0 }

A conjectura (3.9, p.139) e' sobre a familia R_{j-1,j} (j termos,
expoentes escolhidos entre 0..2j-1): existe K(ell)>0 sub-exponencial
tal que |R_{j-1,j}| >= K(ell)*3^ell implica R_{j-1,j} cobre todos os
2*3^(ell-1) residuos invertiveis mod 3^ell.

Simplificacao estrutural (derivada pelo Fable, verificada
numericamente): para j>=ell, todo termo com indice i>=ell morre mod
3^ell, entao

    R_{j-1,j} mod 3^ell = 2^(j-ell) * R_{ell-1,j} mod 3^ell

(multiplicar por unidade nao afeta cobertura) - isto reduz o custo de
C(2j,j) para C(j+ell,ell) elementos.

Metodo: DP de bitset com rotacao ciclica. R_{ell-1,j} tem ell termos,
expoentes escolhidos (decrescentes) entre {0,...,ell+j-1}. Processando
os candidatos a expoente em ordem DECRESCENTE e mantendo, para cada
contagem c de termos ja escolhidos, o CONJUNTO de somas parciais
alcancaveis mod 3^ell como bitset (inteiro Python), escolher o
expoente v na posicao c corresponde a rotacionar o bitset por
2^v * 3^c mod 3^ell.

Toda soma em R_{j,k} e' automaticamente uma unidade mod 3 (o termo de
indice 0, maior expoente, contribui 2^a_0 nao-divisivel por 3; todos os
outros sao divisiveis por 3) - a contagem de bits do bitset final e'
diretamente o tamanho da imagem entre os residuos invertiveis.

Reproduzir: python3 experiment_wcc.py
"""
import math
import time


def image_size(ell, j):
    """Tamanho da imagem de R_{j-1,j} mod 3^ell (via R_{ell-1,j},
    formula equivalente apos o colapso estrutural)."""
    mod = 3 ** ell
    max_exp = ell + j - 1  # expoentes de 0 a ell+j-1, escolhe ell deles
    mask = (1 << mod) - 1
    state = [0] * (ell + 1)
    state[0] = 1  # soma vazia (0 termos escolhidos) = {0}
    for v in range(max_exp, -1, -1):
        p2 = pow(2, v, mod)
        for c in range(ell - 1, -1, -1):
            if state[c] == 0:
                continue
            p3 = pow(3, c, mod)
            offset = (p2 * p3) % mod
            rotated = ((state[c] << offset) | (state[c] >> (mod - offset))) & mask
            state[c + 1] |= rotated
    return state[ell].bit_count()


def find_j_star(ell, j_start=1, j_max=200):
    """Menor j tal que R_{j-1,j} cobre todos os 2*3^(ell-1) residuos
    invertiveis mod 3^ell."""
    target = 2 * 3 ** (ell - 1)
    j = j_start
    while j <= j_max:
        sz = image_size(ell, j)
        if sz == target:
            return j, sz
        j += 1
    return None, None


def validate_against_fable_table():
    """Fable relatou (via prova/calculo proprio, nao so leitura) a
    tabela de referencia j*(ell) para ell=1..7. Confirma a
    implementacao antes de qualquer producao."""
    reference = {1: 1, 2: 4, 3: 6, 4: 7, 5: 9, 6: 10, 7: 11}
    print("=== Validacao contra tabela de referencia do Fable (ell=1..7) ===")
    all_ok = True
    for ell, expected in reference.items():
        t0 = time.time()
        j_star, sz = find_j_star(ell)
        ok = j_star == expected
        all_ok &= ok
        print(f"  ell={ell}: j*={j_star} (esperado {expected}) "
              f"{'OK' if ok else 'DIVERGENCIA!'}  tempo={time.time()-t0:.3f}s")
    # segunda checagem pontual: ell=2, j=2 cobre {1,2,5,7} mod 9, faltando {4,8}
    sz22 = image_size(2, 2)
    print(f"\n  checagem pontual ell=2,j=2: tamanho imagem={sz22} (esperado 4, faltando {{4,8}} de 6 totais)")
    print(f"\n{'TODAS AS VALIDACOES PASSARAM' if all_ok and sz22==4 else 'FALHA NA VALIDACAO - NAO PROSSEGUIR'}")
    return all_ok and sz22 == 4


def main():
    if not validate_against_fable_table():
        print("\nAbortando: implementacao nao bate com a validacao. Consultar Fable antes de prosseguir.")
        return

    print("\n=== Producao: j*(ell), K_diag(ell) e razao j*/ell para ell=1..20 ===")
    print("K_diag(ell) = C(2*j*,j*)/3^ell (a literal da conjectura 3.9)")
    print("e(ell) = j*(ell) - ell*log_4(3)  (excesso sobre o limiar ingenuo log_4(3)~0.7925)")
    print("(ell=18-20: proximo do limite pratico de memoria em Python puro, ~1-9GB estimado)")
    log4_3 = math.log(3) / math.log(4)
    results = []
    t_total = time.time()
    for ell in range(1, 21):
        t0 = time.time()
        j_start = max(1, results[-1][1] - 2) if results else 1
        j_star, sz = find_j_star(ell, j_start=j_start)
        dt = time.time() - t0
        if j_star is None:
            print(f"  ell={ell}: j* nao encontrado ate o limite - parar aqui")
            break
        k_diag = math.comb(2 * j_star, j_star) / (3 ** ell)
        excess = j_star - ell * log4_3
        results.append((ell, j_star))
        print(f"  ell={ell:2d}  j*={j_star:3d}  j*/ell={j_star/ell:.4f}  "
              f"K_diag={k_diag:12.4f}  excesso e(ell)={excess:7.3f}  tempo={dt:6.2f}s  "
              f"total={time.time()-t_total:6.1f}s", flush=True)

    print("\n=== Diagnostico de regime (Fable, 3 hipoteses) ===")
    print("1. K_emp estabiliza/linear em ell -> suporte a 3.9 (e possivelmente 3.8)")
    print("2. K_emp polinomial mas crescente -> mata 3.8, 3.9 sobrevive")
    print("3. e(ell) cresce linearmente -> K_emp exponencial -> evidencia contra a propria 3.9")


if __name__ == "__main__":
    main()
