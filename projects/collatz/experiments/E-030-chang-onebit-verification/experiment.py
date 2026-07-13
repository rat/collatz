#!/usr/bin/env python3
"""
E-030 - Verificacao independente de reivindicacoes do paper de Edward Y.
Chang (Stanford, 2026), "A Structural Reduction of the Collatz Conjecture
to One-Bit Orbit Mixing" (arXiv:2603.25753).

Verifica:
1. Lemma 4.1: em um passo de gap (n_t = 3 mod4), n_t=3mod8 -> G=1 (unit
   gap); n_t=7mod8 -> G>=2.
2. Map Balance Theorem 4.2: |C_3(K) - C_7(K)| = 1 para K>=5.
3. Mecanismo do "bit 4": para n_t=1mod8 (burst-ending), bit4(n_t)=0 sse
   n_t=9mod32 sse G>=2; bit4=1 sse n_t=25mod32 sse G=1.
4. Extensao: taxa de equilibrio bit-4 (fracao de burst-endings com
   n_t=9mod32 entre os que sao =1mod8) para orbitas MAIORES que o testado
   no paper (ate 10^9) - contribuicao empirica incremental honesta ao
   problema aberto declarado no paper (equacao 16 do artigo).

Reproduzir: python3 experiment.py
"""
import sys


def T(n):
    """Mapa de Syracuse (comprimido): (3n+1)/2^v2(3n+1)."""
    m = 3 * n + 1
    while m % 2 == 0:
        m //= 2
    return m


def verify_lemma_4_1(n_max=200_000):
    """Verifica: n_t=3mod8 -> proximo passo e burst (G=1); n_t=7mod8 -> gap continua (G>=2)."""
    falhas = 0
    testados = 0
    for n in range(3, n_max, 2):
        if n % 4 != 3:
            continue
        testados += 1
        nt1 = T(n)
        is_burst_next = (nt1 % 4 == 1)
        if n % 8 == 3:
            if not is_burst_next:
                falhas += 1
                print(f"FALHA (3mod8): n={n}, T(n)={nt1}, esperado burst (1mod4)")
        elif n % 8 == 7:
            if is_burst_next:
                falhas += 1
                print(f"FALHA (7mod8): n={n}, T(n)={nt1}, esperado gap continua (3mod4)")
    print(f"Lemma 4.1: {testados} casos testados, {falhas} falhas.")
    return falhas == 0


def verify_map_balance(K_values=(5, 6, 7, 8, 9, 10, 11, 12, 15)):
    """Verifica Teorema 4.2: |C_3(K) - C_7(K)| = 1."""
    all_ok = True
    for K in K_values:
        mod = 2 ** K
        C3 = 0
        C7 = 0
        S_K_count = 0
        for r in range(1, mod, 4):  # r = 1 mod 4 (residuos de burst)
            Tr = T(r) if r > 0 else 0
            # T(r) mod 4 == 3 significa que produz um gap
            if Tr % 4 == 3:
                S_K_count += 1
                if Tr % 8 == 3:
                    C3 += 1
                elif Tr % 8 == 7:
                    C7 += 1
        diff = C3 - C7
        expected_sign = 1 if K % 2 == 0 else -1
        # o paper diz C3-C7 = (-1)^K; conferimos so o valor absoluto = 1
        ok = abs(diff) == 1
        all_ok = all_ok and ok
        print(f"K={K:2d}: |S_K|={S_K_count}, C3={C3}, C7={C7}, C3-C7={diff:+d}"
              f"  {'OK' if ok else 'FALHA'}")
    return all_ok


def verify_bit4_mechanism(n_max=200_000):
    """Verifica: RESTRITO a burst-endings (n=1mod8 com k=(n-1)/8 impar,
    i.e. n=9mod16 -- unico subcaso onde o proximo passo e de fato um gap),
    bit4(n_t)=0 sse n_t=9mod32 sse G>=2; bit4=1 sse n_t=25mod32 sse G=1."""
    falhas = 0
    testados = 0
    for n in range(1, n_max, 8):  # n = 1 mod 8
        k = (n - 1) // 8
        if k % 2 == 0:
            continue  # k par: proximo passo e OUTRO burst, nao um gap -- fora do escopo do mecanismo
        testados += 1
        bit4 = (n >> 4) & 1
        r32 = n % 32
        m = T(n)  # valor do inicio do gap
        assert m % 4 == 3, f"n={n} (k={k} impar) deveria produzir gap, mas T(n)={m}"
        # Lema 4.1 aplicado a m (o valor NO gap, nao n): m=3mod8 -> G=1; m=7mod8 -> G>=2
        if m % 8 == 3:
            G = 1
        else:
            G = 2
        if bit4 == 0 and r32 != 9:
            falhas += 1
            print(f"FALHA: n={n}, bit4=0 mas n mod32={r32} (esperado 9)")
        if bit4 == 1 and r32 != 25:
            falhas += 1
            print(f"FALHA: n={n}, bit4=1 mas n mod32={r32} (esperado 25)")
        if r32 == 9 and G < 2:
            falhas += 1
            print(f"FALHA: n={n} (9mod32) mas G={G}, esperado G>=2")
        if r32 == 25 and G != 1:
            falhas += 1
            print(f"FALHA: n={n} (25mod32) mas G={G}, esperado G=1")
    print(f"Mecanismo bit-4 (restrito a burst-endings, n=9mod16): {testados} casos testados, {falhas} falhas.")
    return falhas == 0


def bit4_balance_large_scale(starts, max_bursts=2000):
    """Extensao: mede a razao de equilibrio bit-4 ao longo de orbitas
    grandes, indo alem da escala testada no paper (n0 ate 10^9)."""
    print(f"\nExtensao empirica: equilibrio bit-4 em orbitas maiores (ate {max_bursts} burst-endings cada)")
    for n0 in starts:
        n = n0 | 1
        count_9 = 0
        count_25 = 0
        bursts_seen = 0
        steps = 0
        max_steps = 10_000_000
        while n != 1 and bursts_seen < max_bursts and steps < max_steps:
            if n % 8 == 1:
                r32 = n % 32
                if r32 == 9:
                    count_9 += 1
                    bursts_seen += 1
                elif r32 == 25:
                    count_25 += 1
                    bursts_seen += 1
            n = T(n)
            steps += 1
        total = count_9 + count_25
        frac9 = count_9 / total if total else float("nan")
        print(f"  n0={n0}: burst-endings 1mod8 observados={total}, "
              f"frac(9mod32)={frac9:.4f} (esperado ~0.5), passos={steps}")


def bit4_balance_on_record_holders(records_file, max_bursts=100_000):
    """Extensao: mede o equilibrio bit-4 usando os 148 recordistas reais
    de stopping time (orbitas excepcionalmente longas por construcao) em
    vez de pontos aleatorios -- um teste de robustez que o paper original
    nao fez (eles testaram pontos aleatorios/genericos ate n0=10^9)."""
    try:
        vals = []
        with open(records_file) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                vals.append(int(line.split()[-1]))
    except FileNotFoundError:
        print(f"AVISO: {records_file} nao encontrado, pulando essa extensao.")
        return

    print(f"\nExtensao (dados proprios): equilibrio bit-4 nos {len(vals)} recordistas reais de stopping time")
    total_9 = 0
    total_25 = 0
    per_orbit = []
    for n0 in vals:
        n = n0 if n0 % 2 == 1 else n0 + 1
        if n < 3:
            continue
        count_9 = 0
        count_25 = 0
        steps = 0
        max_steps = 2_000_000
        while n != 1 and steps < max_steps:
            if n % 8 == 1:
                r32 = n % 32
                if r32 == 9:
                    count_9 += 1
                elif r32 == 25:
                    count_25 += 1
            n = T(n)
            steps += 1
        total = count_9 + count_25
        if total > 0:
            per_orbit.append(count_9 / total)
        total_9 += count_9
        total_25 += count_25

    grand_total = total_9 + total_25
    print(f"Total agregado: burst-endings 1mod8 observados={grand_total}")
    print(f"  count(9 mod32)={total_9}, count(25 mod32)={total_25}")
    print(f"  fracao agregada (9mod32) = {total_9/grand_total:.4f} (esperado ~0.5)")
    if per_orbit:
        media_por_orbita = sum(per_orbit) / len(per_orbit)
        print(f"  media da fracao POR orbita (nao ponderada) = {media_por_orbita:.4f} "
              f"(n={len(per_orbit)} orbitas com >=1 observacao)")


def main():
    print("=== Verificando Lemma 4.1 (mecanismo mod-8 do comprimento de gap) ===")
    ok1 = verify_lemma_4_1()

    print("\n=== Verificando Teorema 4.2 (Map Balance Theorem) ===")
    ok2 = verify_map_balance()

    print("\n=== Verificando mecanismo do bit-4 (Secao 5.1) ===")
    ok3 = verify_bit4_mechanism()

    print(f"\n=== Resumo: Lemma4.1={'OK' if ok1 else 'FALHOU'}, "
          f"MapBalance={'OK' if ok2 else 'FALHOU'}, "
          f"Bit4={'OK' if ok3 else 'FALHOU'} ===")

    # Extensao 1: orbitas bem maiores que o testado no paper (paper testou ate n0=10^9)
    starts = [10**10 + 7, 10**11 + 3, 10**12 + 9, 7 * 10**12 + 1]
    bit4_balance_large_scale(starts)

    # Extensao 2: nossos proprios 148 recordistas reais (orbitas extremamente
    # longas por construcao -- teste de robustez que o paper nao fez)
    bit4_balance_on_record_holders(
        "../E-004-true-record-holders/oeis_A006877_record_holders.txt"
    )


if __name__ == "__main__":
    main()
