#!/usr/bin/env python3
"""
E-022 - Testa H-022 (nova abordagem para H-008): para N=9K+4 impar (i.e.
N=18j+13), M=(8N-5)/9 = 16j+11 satisfaz: aplicando o passo acelerado a M
duas vezes (valuacoes a=1, b=2), chega-se exatamente em N. Como M<N sempre,
e total_stopping_time(M) = total_stopping_time(N) + 5 (2+3 passos padrao),
M domina N - excluindo N=18j+13 como recordista.

Busca tambem uma construcao analoga para o subcaso par (N=18j+4).

Reproduzir: python3 experiment.py [N_TESTES]
"""
import sys


def total_stopping_time(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


def step(n):
    m = 3 * n + 1
    a = 0
    while m % 2 == 0:
        m //= 2
        a += 1
    return m, a


def verify_odd_case(j_max):
    """N = 18j+13 (impar, =4 mod9), M = 16j+11. Verifica M<N e
    total_stopping_time(M) = total_stopping_time(N) + 5 para j=0..j_max."""
    failures = 0
    for j in range(j_max + 1):
        N = 18 * j + 13
        M = 16 * j + 11
        assert M < N, f"M>=N em j={j}"
        assert N % 9 == 4
        ts_N = total_stopping_time(N)
        ts_M = total_stopping_time(M)
        if ts_M - ts_N != 5:
            failures += 1
            if failures <= 5:
                print(f"  FALHA j={j}: N={N} M={M} ts_N={ts_N} ts_M={ts_M} diff={ts_M-ts_N} (esperado 5)")
    return failures


def search_even_case():
    """Busca uma construcao (a,b,...) analoga para N par, =4 mod9 (N=18j+4)."""
    # tentar 2 passos: M = (N*2^S - 3 - 2^a)/9, exigindo tambem que o segundo
    # passo NAO exija N impar (i.e., queremos que o "N" final seja alcancado
    # como o proximo termo IMPAR da orbita de M, entao N deve ser considerado
    # generico - mas para N par isso nao faz sentido diretamente, pois N par
    # nunca e "o proximo termo impar". Em vez disso, buscamos M tal que a
    # orbita de M alcance N/2^v (o proximo IMPAR na cadeia a partir de N).
    print("Nota: para N par =4 mod9, N nao pode ser 'o proximo termo impar'")
    print("de nenhuma orbita (todo termo alcancado via passo acelerado e IMPAR).")
    print("Portanto N par so pode ser excluido indiretamente via seu proprio N/2^v impar.")


def main():
    j_max = int(sys.argv[1]) if len(sys.argv) > 1 else 100_000

    print("=== caso impar: N=18j+13 (=4 mod9, impar), M=16j+11 ===")
    failures = verify_odd_case(j_max)
    print(f"testado j=0..{j_max}, falhas={failures}")
    print()

    print("=== caso par: N=18j+4 (=4 mod9, par) ===")
    search_even_case()

    # verificar diretamente: N par =4mod9 e sempre 2 * (algo), e algo=N/2
    # pode ter QUALQUER residuo mod9 (nao necessariamente 4) - entao N par
    # pode ser excluido apenas se, TODA VEZ que dividimos por 2 repetidamente
    # ate chegar num impar, esse impar tambem cair numa classe ja excluida.
    print()
    print("verificando se N par =4 mod9 sempre reduz (via divisao por 2) a um")
    print("impar em alguma classe ja conhecida como excluida (2 mod3 ou 5 mod8)...")
    excluidas_mod3 = {2}
    excluidas_mod8 = {5}
    exemplos_nao_cobertos = []
    for j in range(0, 2000):
        N = 18 * j + 4
        if N <= 2:
            continue
        m = N
        while m % 2 == 0:
            m //= 2
        # m e o primeiro impar alcancado dividindo N por 2 repetidamente
        coberto = (m % 3 in excluidas_mod3) or (m % 8 in excluidas_mod8)
        if not coberto:
            exemplos_nao_cobertos.append((N, m))
    print(f"exemplos de N par =4mod9 cujo impar associado NAO cai em classe conhecida: "
          f"{len(exemplos_nao_cobertos)} de 2000 testados")
    if exemplos_nao_cobertos:
        print("primeiros exemplos:", exemplos_nao_cobertos[:5])


if __name__ == "__main__":
    main()
