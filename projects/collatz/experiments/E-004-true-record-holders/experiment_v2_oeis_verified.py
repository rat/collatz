#!/usr/bin/env python3
"""
E-004 v2 - Reanalise usando a sequencia OFICIAL e completa de recordistas reais
de total stopping time (OEIS A006877, dados de Roosendaal via
http://www.ericr.nl/wondrous/delrecs.html), apos identificar que a lista usada
na v1 continha valores incorretos (ver CORRECTION.md).

Baixar os dados (uma vez): curl -A "Mozilla/5.0" https://oeis.org/A006877/b006877.txt
                            | grep -v '^#' | awk '{print $2}' > oeis_A006877_record_holders.txt

Reproduzir: python3 experiment_v2_oeis_verified.py
"""
import math
from collections import Counter


def chi2_gof_uniform(counts, k, n):
    expected = n / k
    return sum((counts.get(i, 0) - expected) ** 2 / expected for i in range(k))


def chi2_pvalue(x, dof):
    if dof <= 0:
        return float("nan")
    z = ((x / dof) ** (1 / 3) - (1 - 2 / (9 * dof))) / math.sqrt(2 / (9 * dof))
    return 0.5 * math.erfc(z / math.sqrt(2))


def main():
    with open("oeis_A006877_record_holders.txt") as f:
        records = [int(line.strip()) for line in f if line.strip()]

    n = len(records)
    print(f"n = {n} recordistas reais (OEIS A006877, fonte Roosendaal)")
    print(f"menor = {records[0]}, maior = {records[-1]}")
    print()

    for modulus in [3, 9, 27]:
        c = Counter(r % modulus for r in records)
        chi2 = chi2_gof_uniform(c, modulus, n)
        dof = modulus - 1
        p = chi2_pvalue(chi2, dof)
        expected = n / modulus
        valido = expected >= 5
        faltando = [r for r in range(modulus) if c.get(r, 0) == 0]
        print(f"mod {modulus}: {dict(sorted(c.items()))}")
        print(f"  classes com ZERO ocorrencias: {faltando}")
        print(f"  esperado uniforme/classe={expected:.1f}  chi2={chi2:.2f}  dof={dof}  p={p:.3e}"
              f"  {'(valido)' if valido else '(AMOSTRA INSUFICIENTE)'}")
        print()

    exceptions_mod3_res2 = [r for r in records if r % 3 == 2]
    print(f"unico(s) recordista(s) com residuo 2 mod 3: {exceptions_mod3_res2}")
    print("(n=2 e um caso trivial/de borda - excluindo-o, 0 de 147 recordistas restantes sao =2 mod 3)")


if __name__ == "__main__":
    main()
