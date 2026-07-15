#!/usr/bin/env python3
"""
E-078 - Verifica o "Period Theorem" de Wei Ren, "Reduced Collatz
dynamics is periodical and the period equals 2 to the power of the
count of x/2" (Research in Mathematics 12(1), 2025), item 108 da colecao.

O paper usa T(x)=(3x+1)/2 se x impar, x/2 se x par ("dinamica reduzida",
equivalente ao mapa acelerado ja usado por este projeto). d_r(x) e a
"dinamica reduzida" - a SEQUENCIA de operacoes I ((3x+1)/2) e O (x/2)
desde x ate o primeiro iterado ESTRITAMENTE MENOR que x (definicao 2.6,
analoga ao "stopping time"/glide). O resultado central (Teorema 3.22):
se d_r(x) existe, entao d_r(x+2^L) existe E E IGUAL a d_r(x), onde
L=|d_r(x)| (comprimento da sequencia).

Testa:
1. Exemplos do proprio paper: d_r(3)=IIOO, d_r(5)=IO, d_r(7)=IIIOIOO,
   d_r(9)=IO, d_r(11)=IIOIO (Remark 2.8).
2. Teorema 3.22 (Period Theorem): d_r(x+2^L) = d_r(x), testado
   exaustivamente para muitos x.
3. Corollary 3.24 (extensao): d_r(x+k*2^L) = d_r(x) para todo k>=1
   inteiro positivo.
4. Corollary 4.3/4.4/4.5 (Form Corollary do apendice): relacoes entre
   CntI(s) (contagem de I) e CntO(s) (contagem de O) em qualquer
   dinamica reduzida valida.

Reproduzir: python3 experiment.py
"""
import sys
import math


def T_step(x):
    """T(x) = (3x+1)/2 se x impar, x/2 se x par - retorna (novo_x, simbolo)."""
    if x % 2 == 1:
        return (3 * x + 1) // 2, "I"
    else:
        return x // 2, "O"


def reduced_dynamics(x0, max_steps=10_000):
    """d_r(x0): sequencia de simbolos I/O desde x0 ate o primeiro
    iterado ESTRITAMENTE MENOR que x0 (Definicao 2.6). Retorna a string
    de simbolos, ou None se nao encontrar dentro de max_steps (nao
    esperado para x0 pequeno, dado que sabemos que Collatz converge
    para todos os valores testados aqui)."""
    x = x0
    symbols = []
    for _ in range(max_steps):
        x, sym = T_step(x)
        symbols.append(sym)
        if x < x0:
            return "".join(symbols)
    return None


def test_paper_examples():
    """Remark 2.8: d_r(3)=IIOO, d_r(5)=IO, d_r(7)=IIIOIOO, d_r(9)=IO,
    d_r(11)=IIOIO."""
    examples = {3: "IIOO", 5: "IO", 7: "IIIOIOO", 9: "IO", 11: "IIOIO"}
    failures = 0
    for x, expected in examples.items():
        got = reduced_dynamics(x)
        ok = got == expected
        print(f"  d_r({x}) = {got} (esperado {expected}) {'OK' if ok else 'FALHA'}")
        if not ok:
            failures += 1
    return failures


def test_period_theorem(x_max=500, max_steps=10_000):
    """Teorema 3.22: d_r(x+2^L) = d_r(x), onde L=|d_r(x)|.
    Testado para todo x de 2 a x_max."""
    failures = 0
    total = 0
    for x in range(2, x_max + 1):
        dr_x = reduced_dynamics(x, max_steps)
        if dr_x is None:
            continue
        L = len(dr_x)
        P = 2 ** L
        total += 1
        dr_xP = reduced_dynamics(x + P, max_steps)
        if dr_xP != dr_x:
            failures += 1
            if failures <= 5:
                print(f"  FALHA: x={x} L={L} P={P} d_r(x)={dr_x} d_r(x+P)={dr_xP}")
    return total, failures


def test_corollary_3_24(x_values, k_max=5, max_steps=10_000):
    """Corollary 3.24: d_r(x+k*2^L) = d_r(x) para todo k inteiro
    positivo (nao so k=1, extensao iterativa do Teorema 3.22)."""
    failures = 0
    total = 0
    for x in x_values:
        dr_x = reduced_dynamics(x, max_steps)
        if dr_x is None:
            continue
        L = len(dr_x)
        P = 2 ** L
        for k in range(1, k_max + 1):
            total += 1
            dr_xkP = reduced_dynamics(x + k * P, max_steps)
            if dr_xkP != dr_x:
                failures += 1
                print(f"  FALHA: x={x} k={k} P={P} d_r(x)={dr_x} d_r(x+k*P)={dr_xkP}")
    return total, failures


def cnt_i(s):
    return s.count("I")


def cnt_o(s):
    return s.count("O")


def test_form_corollary(x_max=2000, max_steps=10_000):
    """Corollary 4.2 (Form Corollary): para s=d_r(x) (x>=2, x em Set_rd),
    CntO(s) = ceil(log2(1.5) * CntI(s)), e para todo prefixo proprio s'
    de s (s'=Substr(s,1,i), i=1..|s|-1), CntO(s') < ceil(log2(1.5)*CntI(s')).
    Testamos a primeira parte (igualdade para a sequencia completa) e a
    segunda (desigualdade estrita para TODO prefixo proprio nao-vazio)."""
    lam = math.log2(1.5)
    failures_eq = 0
    failures_prefix = 0
    total = 0
    for x in range(2, x_max + 1):
        s = reduced_dynamics(x, max_steps)
        if s is None or s == "O":
            continue  # caso especial x em [0]_2 puro (s=O) tratado a parte no proprio Corollary 4.3
        total += 1
        ci = cnt_i(s)
        co = cnt_o(s)
        expected_co = math.ceil(lam * ci)
        if co != expected_co:
            failures_eq += 1
            if failures_eq <= 5:
                print(f"  FALHA (igualdade): x={x} s={s} CntO={co} esperado={expected_co}")
        # testar todos os prefixos proprios nao-vazios (i=1..|s|-1)
        for i in range(1, len(s)):
            prefix = s[:i]
            ci_p = cnt_i(prefix)
            co_p = cnt_o(prefix)
            expected_bound = math.ceil(lam * ci_p) if ci_p > 0 else 0
            if not (co_p < expected_bound if ci_p > 0 else co_p == 0):
                # caso ci_p=0: CntO(prefix) deveria ser 0 tambem (todo I no inicio)
                if ci_p == 0 and co_p != 0:
                    failures_prefix += 1
                elif ci_p > 0 and co_p >= expected_bound:
                    failures_prefix += 1
                    if failures_prefix <= 5:
                        print(f"  FALHA (prefixo): x={x} s={s} prefixo={prefix} CntO={co_p} CntI={ci_p} limite={expected_bound}")
    return total, failures_eq, failures_prefix


def main():
    print("=== Exemplos do proprio paper (Remark 2.8) ===")
    fail1 = test_paper_examples()
    print(f"  {fail1} falhas")
    print()

    print("=== Period Theorem (Teorema 3.22): d_r(x+2^L) = d_r(x) ===")
    total, fail2 = test_period_theorem()
    print(f"  {total} valores testados (x=2..500), {fail2} falhas")
    print()

    print("=== Corollary 3.24: d_r(x+k*2^L) = d_r(x) para k=1..5 ===")
    total, fail3 = test_corollary_3_24(list(range(2, 51)))
    print(f"  {total} casos testados, {fail3} falhas")
    print()

    print("=== Form Corollary (Corollary 4.2, apendice) ===")
    total, fail_eq, fail_prefix = test_form_corollary()
    print(f"  {total} valores de x testados (2..2000)")
    print(f"  {fail_eq} falhas na igualdade CntO(s)=ceil(log2(1.5)*CntI(s))")
    print(f"  {fail_prefix} falhas na desigualdade estrita para prefixos proprios")


if __name__ == "__main__":
    main()
