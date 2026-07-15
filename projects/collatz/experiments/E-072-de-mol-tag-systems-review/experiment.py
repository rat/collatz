#!/usr/bin/env python3
"""
E-072 - Verifica a construcao central de De Mol, "Tag systems and
Collatz-like functions" (Theoretical Computer Science 390, 92-101, 2008),
item 102 da colecao.

Teorema 2.1 do paper: a funcao acelerada de Collatz
    C'(2m) = m
    C'(2m+1) = 3m+2
e reduzivel a um sistema de tag T_C com mu=3 simbolos {alpha, c, y} e
numero de deslocamento (shift) v=2, com regras de producao:
    alpha -> c y
    c     -> alpha
    y     -> alpha alpha alpha

Um sistema de tag processa uma string da esquerda para a direita: olha o
simbolo mais a esquerda, anexa sua producao ao FIM da string, depois
apaga os v=2 simbolos mais a esquerda (os ORIGINAIS, antes de anexar).
Repete ate a string ficar curta demais ou parar.

Reproduzimos o SISTEMA DE TAG BRUTO diretamente (nao a taquigrafia "-o->"
do paper, que abrevia varios passos brutos ateo string original ser
totalmente consumida) - simulamos passo a passo e detectamos quando a
string volta a ser puramente alpha^k, medindo k e comparando com C'(n).

Reproduzir: python3 experiment.py
"""
import sys
from collections import deque

PRODUCTIONS = {
    "a": "cy",     # alpha -> c y
    "c": "a",      # c -> alpha
    "y": "aaa",    # y -> alpha alpha alpha
}
V = 2  # shift number


def run_tag_system(n, max_raw_steps=2_000_000):
    """Roda o sistema de tag bruto a partir de alpha^n usando uma deque
    (O(1) por passo, em vez de concatenacao de string O(n) por passo).
    Retorna o primeiro k tal que a string atinja o estado alpha^k
    (puramente alpha, k>=1) apos pelo menos 1 passo, e o numero de
    passos brutos ate la, ou (None, steps) se nao convergir dentro do
    limite ou a string ficar curta demais antes de ser pura."""
    s = deque("a" * n)
    non_alpha_count = 0  # quantos simbolos != 'a' estao atualmente na deque
    steps = 0
    while steps < max_raw_steps:
        if non_alpha_count == 0 and steps > 0:
            return len(s), steps
        if len(s) < V:
            return None, steps
        leftmost = s[0]
        for _ in range(V):
            removed = s.popleft()
            if removed != "a":
                non_alpha_count -= 1
        production = PRODUCTIONS[leftmost]
        for ch in production:
            s.append(ch)
            if ch != "a":
                non_alpha_count += 1
        steps += 1
    return None, steps


def c_prime(n):
    """Funcao acelerada de Collatz do proprio paper: C'(2m)=m, C'(2m+1)=3m+2."""
    if n % 2 == 0:
        return n // 2
    else:
        m = (n - 1) // 2
        return 3 * m + 2


def test_theorem_2_1(n_max=200):
    """Para cada n, roda o sistema de tag bruto a partir de alpha^n e
    confirma que o primeiro estado puramente-alpha subsequente tem
    comprimento C'(n). n=1 e um caso degenerado: alpha^1 tem comprimento
    1 < v=2, entao o sistema para imediatamente sem produzir nada -
    condicao explicita do proprio formalismo de sistemas de tag (Secao
    1.1 do paper: "produces a word A_i, after i iterations, having a
    length smaller than v" = parada, nao um erro), nao uma falha do
    Teorema 2.1. Excluido da contagem de falhas, reportado a parte."""
    failures = 0
    total = 0
    max_steps_seen = 0
    for n in range(1, n_max + 1):
        total += 1
        k, steps = run_tag_system(n, max_raw_steps=2_000_000)
        expected = c_prime(n)
        max_steps_seen = max(max_steps_seen, steps)
        if n == 1 and k is None:
            continue  # caso degenerado esperado, ver docstring
        if k != expected:
            failures += 1
            if failures <= 10:
                print(f"  FALHA: n={n} k_obtido={k} esperado={expected} (passos brutos={steps})")
    return total, failures, max_steps_seen


def test_iterated_convergence(seeds=(7, 27, 97, 871), max_iters=200):
    """Itera C' repetidamente via o sistema de tag bruto (encadeando
    run_tag_system) e verifica que a trajetoria eventualmente atinge 1,
    2 ou 4 (analogo ao ciclo trivial do Collatz padrao), cruzando com a
    trajetoria da funcao C' calculada diretamente (sem tag system)."""
    failures = 0
    for n0 in seeds:
        n = n0
        traj_tag = [n]
        traj_direct = [n]
        ok = True
        for i in range(max_iters):
            if n in (1, 2, 4):
                break
            k, steps = run_tag_system(n, max_raw_steps=2_000_000)
            if k is None:
                print(f"  FALHA (nao convergiu): n0={n0}, travou em n={n} na iteracao {i}")
                failures += 1
                ok = False
                break
            traj_tag.append(k)
            traj_direct.append(c_prime(traj_direct[-1]))
            n = k
        if ok and traj_tag != traj_direct:
            print(f"  FALHA (trajetorias divergem): n0={n0}")
            print(f"    tag:    {traj_tag}")
            print(f"    direto: {traj_direct}")
            failures += 1
        elif ok:
            print(f"  n0={n0}: trajetoria via tag system bate com C' direto, "
                  f"{len(traj_tag)-1} iteracoes ate {traj_tag[-1]}")
    return failures


def main():
    print("=== Teorema 2.1: sistema de tag T_C simula C'(n) corretamente ===")
    total, failures, max_steps = test_theorem_2_1()
    print(f"  {total} valores de n testados (1 a 200), {failures} falhas")
    print(f"  maximo de passos brutos observado numa unica iteracao: {max_steps}")
    print()

    print("=== Iterando repetidamente via o sistema de tag (varias sementes) ===")
    failures2 = test_iterated_convergence()
    print(f"  {failures2} falhas de convergencia/consistencia")


if __name__ == "__main__":
    main()
