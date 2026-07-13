#!/usr/bin/env python3
"""
E-031 - Testa H-031: existe alguma classe residual mod p (p primo != 2,3)
ou potencia maior de 3 (27, 81) vazia nos recordistas reais, revelando
exclusao nova independente da familia mod-2/mod-3 ja conhecida?

Reproduzir: python3 experiment.py
"""
import math

RECORDS_FILE = "../E-004-true-record-holders/oeis_A006877_record_holders.txt"


def load_records():
    vals = []
    with open(RECORDS_FILE) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            vals.append(int(line.split()[-1]))
    return vals


def already_excluded(n):
    if n % 3 == 2 and n != 2:
        return "H-007 (2mod3)"
    if n % 6 == 4:
        return "H-027 (4mod6)"
    if n % 8 == 5:
        return "H-014 (5mod8)"
    if n % 9 == 4:
        return "H-008 (4mod9)"
    return None


def scan_primes(vals, moduli):
    for mod in moduli:
        dist = {}
        for n in vals:
            r = n % mod
            dist[r] = dist.get(r, 0) + 1
        expected = len(vals) / mod
        empty_or_low = [(r, dist.get(r, 0)) for r in range(mod) if dist.get(r, 0) <= 1]
        print(f"mod {mod:3d}: esperado~{expected:.2f}/classe, "
              f"{len(empty_or_low)} classes com contagem<=1")
        if empty_or_low:
            print(f"    {empty_or_low}")


def scan_with_explanation(vals, moduli):
    for mod in moduli:
        print(f"\n=== mod {mod} (checando explicacao de classes vazias/raras) ===")
        unexplained = []
        for r in range(mod):
            count = sum(1 for n in vals if n % mod == r)
            if count <= 1:
                reason = already_excluded(r)
                if reason is None:
                    unexplained.append((r, count))
                    print(f"  r={r:3d}: count={count}  *** NAO EXPLICADO ***")
        if unexplained:
            expected = len(vals) / mod
            p_zero = math.exp(-expected)
            expected_zero_classes = mod * p_zero
            n_zero_unexplained = sum(1 for r, c in unexplained if c == 0)
            print(f"  -> {n_zero_unexplained} classes com contagem=0 nao explicadas.")
            print(f"     Esperado por acaso (Poisson, {mod} classes): ~{expected_zero_classes:.1f}")
            if n_zero_unexplained < expected_zero_classes:
                print("     => CONSISTENTE COM RUIDO (menos que o esperado por acaso).")
            else:
                print("     => MAIS que o esperado por acaso -- investigar melhor.")
        else:
            print("  Nenhuma classe nao-explicada encontrada.")


def main():
    vals = load_records()
    print(f"Total recordistas: {len(vals)}\n")

    print("=== Primos nao testados antes (5,7,11,13,17,19,23) ===")
    scan_primes(vals, [5, 7, 11, 13, 17, 19, 23])

    print("\n=== Potencias maiores de 3 (27, 81) - checando se ja explicadas ===")
    scan_with_explanation(vals, [27, 81])


if __name__ == "__main__":
    main()
