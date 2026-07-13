#!/usr/bin/env python3
"""
E-028 - Consolida a familia de exclusoes provadas (H-007, H-014, H-022,
H-027) numa unica caracterizacao mod 72 = lcm(8,9), e valida contra os
148 recordistas reais conhecidos (OEIS A006877).

Regras de exclusao provadas (recordistas nunca caem nestas classes,
exceto o caso-base n=2):
  - H-007: N = 2 (mod 3)
  - H-027: N = 4 (mod 6)   [corolario de H-007, cobre metade de 1 mod3]
  - H-014: N = 5 (mod 8)
  - H-008 (H-022+H-027): N = 4 (mod 9)

Reproduzir: python3 experiment.py
"""
import sys

RECORDS_FILE = "../E-004-true-record-holders/oeis_A006877_record_holders.txt"


def excluded(n, mod72):
    reasons = []
    if mod72 % 3 == 2:
        reasons.append("H-007 (2 mod3)")
    if mod72 % 6 == 4:
        reasons.append("H-027 (4 mod6)")
    if mod72 % 8 == 5:
        reasons.append("H-014 (5 mod8)")
    if mod72 % 9 == 4:
        reasons.append("H-008 (4 mod9)")
    return reasons


def main():
    excluded_residues = [r for r in range(72) if excluded(r, r)]
    allowed_residues = [r for r in range(72) if not excluded(r, r)]

    print(f"Residuos mod 72 excluidos (com prova): {len(excluded_residues)} de 72"
          f" ({100*len(excluded_residues)/72:.1f}%)")
    print(f"Residuos mod 72 permitidos: {len(allowed_residues)} de 72"
          f" ({100*len(allowed_residues)/72:.1f}%)")
    print()

    try:
        vals = []
        with open(RECORDS_FILE) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                vals.append(int(line.split()[-1]))
    except FileNotFoundError:
        print(f"AVISO: {RECORDS_FILE} nao encontrado, pulando validacao contra dados reais.")
        return

    print(f"Validando contra {len(vals)} recordistas reais (OEIS A006877)...")
    violacoes = []
    for n in vals:
        r = n % 72
        reasons = excluded(n, r)
        if reasons and n != 2:
            violacoes.append((n, r, reasons))

    if violacoes:
        print(f"VIOLACOES ENCONTRADAS: {len(violacoes)}")
        for n, r, reasons in violacoes:
            print(f"  n={n} (mod72={r}): deveria ser excluido por {reasons}")
    else:
        print("ZERO violacoes. Todos os 148 recordistas reais caem em residuos")
        print("mod72 permitidos (ou sao o caso-base n=2).")

    print()
    print("Residuos mod72 realmente OCUPADOS pelos recordistas reais:")
    ocupados = sorted(set(n % 72 for n in vals if n != 2))
    print(f"  {len(ocupados)} de {len(allowed_residues)} residuos permitidos "
          f"efetivamente aparecem na amostra de 148.")


if __name__ == "__main__":
    main()
