#!/usr/bin/env python3
"""
E-033 - Estende o problema aberto do paper de Chang (2026, H-030):
"toda orbita de Collatz visita as classes 9 e 25 (mod 32) com equilibrio
suficiente ao longo de sua subsequencia esparsa de fim-de-burst?"

O proprio Chang testou ate n0=10^9 (poucos blocos por orbita, ~40-50) e
reportou (Figure 2, n0=837799, 43 blocos): fracao "longe de convergir".
Aqui usamos nossos proprios recordistas reais de stopping time (orbitas
excepcionalmente LONGAS por construcao) para ver se o equilibrio melhora
(converge para 0.5) numa escala de MUITOS MAIS blocos por orbita -
analisando cada orbita INDIVIDUALMENTE (nao agregando entre orbitas, para
evitar a armadilha de pseudo-replicacao ja documentada em H-030/E-030).

Reproduzir: python3 experiment.py
"""
import sys

RECORDS_FILE = "../E-004-true-record-holders/oeis_A006877_record_holders.txt"


def T(n):
    m = 3 * n + 1
    while m % 2 == 0:
        m //= 2
    return m


def track_orbit_bit4_balance(n0, report_every=None):
    """Percorre a orbita completa de n0, registrando burst-endings no canal
    n=1mod8 (i.e., n=9mod16) e classificando por bit4 (9 ou 25 mod32).
    Retorna a lista de fracoes acumuladas (running fraction de 9mod32)."""
    n = n0 if n0 % 2 == 1 else n0 + 1
    count_9 = 0
    count_25 = 0
    running_fracs = []
    steps = 0
    max_steps = 5_000_000
    while n != 1 and steps < max_steps:
        if n % 16 == 9:  # burst-ending no canal n=1mod8 (k=(n-1)/8 impar)
            r32 = n % 32
            if r32 == 9:
                count_9 += 1
            elif r32 == 25:
                count_25 += 1
            total = count_9 + count_25
            running_fracs.append((total, count_9 / total))
        n = T(n)
        steps += 1
    return running_fracs, steps


def main():
    try:
        vals = []
        with open(RECORDS_FILE) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                vals.append(int(line.split()[-1]))
    except FileNotFoundError:
        print(f"AVISO: {RECORDS_FILE} nao encontrado.")
        return

    top_records = sorted(vals)[-8:]

    print("Analisando o equilibrio bit-4 (9 vs 25 mod32) INDIVIDUALMENTE")
    print("nos maiores recordistas reais (orbitas mais longas disponiveis):\n")

    for n0 in top_records:
        fracs, steps = track_orbit_bit4_balance(n0)
        if not fracs:
            print(f"n0={n0}: nenhum burst-ending no canal 1mod8 encontrado.")
            continue
        final_total, final_frac = fracs[-1]
        # deriva de 0.5 ao longo do caminho (min e max, e nos ultimos 25%)
        last_quarter = fracs[len(fracs) * 3 // 4:]
        avg_last_quarter = sum(f for _, f in last_quarter) / len(last_quarter)
        max_dev = max(abs(f - 0.5) for _, f in fracs)
        print(f"n0={n0} ({steps} passos totais):")
        print(f"  burst-endings no canal 1mod8: {final_total}")
        print(f"  fracao final (9mod32): {final_frac:.4f}")
        print(f"  fracao media no ultimo quarto da orbita: {avg_last_quarter:.4f}")
        print(f"  desvio maximo de 0.5 observado: {max_dev:.4f}")
        print()


if __name__ == "__main__":
    main()
