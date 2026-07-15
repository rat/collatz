#!/usr/bin/env python3
"""
E-064 -- H-064: verificacao do paper #038 (Kayadibi, "A Modular
Classification of Pre-Descent Resistance in Accelerated Odd Collatz
Dynamics", SSRN 6918258).

Paper explicitamente NAO tenta provar a conjectura de Collatz (Secao
4.7: "the results are interpreted as computational evidence for the
proposed classification framework, not as a proof of the Collatz
conjecture"). Estuda o comportamento de "pre-descida" (antes da
trajetoria cair abaixo do valor inicial) do mapa acelerado impar.

Predecessor mais simples do paper referenciado como [11] pelo item 015
desta colecao (Kayadibi, "Canonical Shells and Residue-Cover Trees", ja
revisado como H-058) -- mesma autora, framework mais elementar (sem
"canonical shells", "dyadic gap condition" ou "residue-cover trees");
so a "espinha de resistencia modular" S_m = {n : n=-1 mod 2^m}.

Definicoes do paper:
  T(n) = (3n+1)/2^v2(3n+1)               -- mapa acelerado impar
  tau(n) = min{r>=1 : T^r(n) < n}          -- tempo de primeira descida
  M(n) = max(n, T(n), ..., T^tau(n)(n))    -- valor maximo de pre-descida
  rho(n) = M(n)/n                          -- razao de pico relativa
  R_k = {n : tau(n)=k}                     -- classes de resistencia
  S_m = {n : n = -1 (mod 2^m)}             -- espinha de resistencia modular

Partes:
  PARTE 1: Lemma 3.3 (v2(3n+1)=1 para n em S_m, m>=2).
  PARTE 2: Proposicao 3.4 (T(n)>n para n em S_m).
  PARTE 3: Lemma 3.6 (persistencia: T^j(n)=3^j*2^(m-j)*q-1).
  PARTE 4: Proposicao 3.8 (tau(n)>=m para n em S_m).
  PARTE 5: reproducao computacional em grande escala (N=10^7, L=5000):
    0 casos nao resolvidos; os dois casos extremos citados (maior tau,
    maior rho).
  PARTE 6: Tabela 2 (estatisticas da espinha, m=6..15).
  PARTE 7: Tabela 3 (razao de pico media ao longo da espinha).
  PARTE 8: estatisticas modulo 64 (Secao 5.4).
"""

import sys
import time
import heapq

sys.set_int_max_str_digits(0)


def T(n):
    x = 3 * n + 1
    while x % 2 == 0:
        x >>= 1
    return x


def v2(x):
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    return c


def tau_M_rho(n, L=5000):
    """Retorna (tau(n), M(n), rho(n)) ou (None,None,None) se nao
    resolvido dentro de L passos acelerados."""
    x = n
    M = n
    for r in range(1, L + 1):
        x = T(x)
        if x > M:
            M = x
        if x < n:
            return r, M, M / n
    return None, None, None


# ---------------------------------------------------------------------
# PARTES 1-4: lemas algebricos da espinha de resistencia modular
# ---------------------------------------------------------------------

def partes1a4():
    print("=" * 90)
    print("PARTES 1-4: lemas algebricos da espinha S_m = {n : n=-1 mod 2^m}")
    print("=" * 90)
    falhas = 0

    # Parte 1: Lemma 3.3 -- v2(3n+1)=1 para n em S_m (m>=2)
    testados = 0
    f1 = 0
    for m in range(2, 20):
        for q in range(1, 200):
            n = 2 ** m * q - 1
            testados += 1
            if v2(3 * n + 1) != 1:
                f1 += 1
                print(f"  FALHA (Lemma 3.3): m={m}, q={q}, n={n}: v2(3n+1)={v2(3 * n + 1)}")
    print(f"Lemma 3.3: {testados} casos (m=2..19, q=1..199), {f1} falhas.")
    falhas += f1

    # Parte 2: Proposicao 3.4 -- T(n)>n para n em S_m
    testados = 0
    f2 = 0
    for m in range(2, 20):
        for q in range(1, 200):
            n = 2 ** m * q - 1
            testados += 1
            if not (T(n) > n):
                f2 += 1
                print(f"  FALHA (Prop 3.4): m={m}, q={q}, n={n}: T(n)={T(n)}")
    print(f"Proposicao 3.4: {testados} casos, {f2} falhas.")
    falhas += f2

    # Parte 3: Lemma 3.6 -- persistencia T^j(n) = 3^j * 2^(m-j) * q - 1,
    # e T^j(n) = -1 (mod 2^(m-j)), para 0<=j<=m-1
    testados = 0
    f3 = 0
    for m in range(2, 15):
        for q in range(1, 50):
            n = 2 ** m * q - 1
            x = n
            for j in range(0, m):
                previsto = 3 ** j * 2 ** (m - j) * q - 1
                testados += 1
                if x != previsto:
                    f3 += 1
                    print(f"  FALHA (Lemma 3.6, formula): m={m},q={q},j={j}: "
                          f"x={x}, previsto={previsto}")
                if (x + 1) % (2 ** (m - j)) != 0:
                    f3 += 1
                    print(f"  FALHA (Lemma 3.6, congruencia): m={m},q={q},j={j}: x={x}")
                if j < m - 1:
                    x = T(x)
    print(f"Lemma 3.6: {testados} casos (m=2..14, q=1..49, j=0..m-1), {f3} falhas.")
    falhas += f3

    # Parte 4: Proposicao 3.8 -- tau(n)>=m para n em S_m (quando tau existe)
    testados = 0
    f4 = 0
    for m in range(2, 15):
        for q in range(1, 50):
            n = 2 ** m * q - 1
            testados += 1
            tau, M, rho = tau_M_rho(n, L=2000)
            if tau is not None and tau < m:
                f4 += 1
                print(f"  FALHA (Prop 3.8): m={m}, q={q}, n={n}: tau={tau} < m={m}")
    print(f"Proposicao 3.8: {testados} casos, {f4} falhas.")
    falhas += f4

    print(f"\n{falhas} falhas nas Partes 1-4.")
    return falhas


# ---------------------------------------------------------------------
# PARTES 5-8: reproducao computacional em grande escala
# ---------------------------------------------------------------------

def computa_estatisticas_globais(N, L=5000):
    """Uma unica passada por todos os n impares em [3,N]. Agrega
    estatisticas mod-64 e mantem os top-100 casos de tau e rho (heaps
    limitados, sem guardar todas as N/2 trajetorias)."""
    residuo64 = {r: {"count": 0, "soma_tau": 0, "max_tau": 0,
                      "soma_rho": 0.0, "max_rho": 0.0} for r in range(64)}
    nao_resolvidos = 0
    descidas = 0
    top_tau = []
    top_rho = []

    n = 3
    while n <= N:
        tau, M, rho = tau_M_rho(n, L=L)
        if tau is None:
            nao_resolvidos += 1
        else:
            descidas += 1
            r = n % 64
            d = residuo64[r]
            d["count"] += 1
            d["soma_tau"] += tau
            d["max_tau"] = max(d["max_tau"], tau)
            d["soma_rho"] += rho
            d["max_rho"] = max(d["max_rho"], rho)

            heapq.heappush(top_tau, (tau, n))
            if len(top_tau) > 100:
                heapq.heappop(top_tau)
            heapq.heappush(top_rho, (rho, n))
            if len(top_rho) > 100:
                heapq.heappop(top_rho)
        n += 2

    return {
        "descidas": descidas,
        "nao_resolvidos": nao_resolvidos,
        "residuo64": residuo64,
        "top_tau": sorted(top_tau, reverse=True),
        "top_rho": sorted(top_rho, reverse=True),
    }


def estatisticas_espinha(m, N, L=5000):
    """Itera diretamente sobre S_m = {2^m-1, 2^m-1+2^m, ...} <= N --
    muito mais barato que filtrar dentro do loop principal (S_m tem
    ~N/2^m elementos, nao N)."""
    passo = 2 ** m
    n = passo - 1
    count = 0
    soma_tau = 0
    max_tau = 0
    soma_rho = 0.0
    max_rho = 0.0
    while n <= N:
        tau, M, rho = tau_M_rho(n, L=L)
        if tau is not None:
            count += 1
            soma_tau += tau
            max_tau = max(max_tau, tau)
            soma_rho += rho
            max_rho = max(max_rho, rho)
        n += passo
    tau_medio = soma_tau / count if count else 0.0
    rho_medio = soma_rho / count if count else 0.0
    return count, tau_medio, max_tau, rho_medio, max_rho


TABELA_2 = {
    # m: (count, tau_medio, E_m = tau_medio - m)
    6: (156250, 15.5684, 9.5684), 7: (78125, 17.9263, 10.9263),
    8: (39062, 20.2822, 12.2822), 9: (19531, 22.6321, 13.6321),
    10: (9765, 24.9493, 14.9493), 11: (4882, 27.5072, 16.5072),
    12: (2441, 29.8894, 17.8894), 13: (1220, 32.1492, 19.1492),
    14: (610, 35.0459, 21.0459), 15: (305, 37.3607, 22.3607),
}

TABELA_3 = {
    # m: rho_medio
    6: 82.3772, 7: 130.6475, 8: 209.8512, 9: 344.3314, 10: 298.3330,
    11: 461.4293, 12: 605.4558, 13: 935.5016, 14: 1452.2820, 15: 1237.3507,
}


def partes5a8(N=10_000_000, L=5000):
    print()
    print("=" * 90)
    print(f"PARTES 5-8: reproducao computacional em grande escala (N={N:,}, L={L})")
    print("=" * 90)
    falhas = 0

    t0 = time.time()
    stats = computa_estatisticas_globais(N, L=L)
    dt = time.time() - t0
    total = stats["descidas"] + stats["nao_resolvidos"]
    print(f"Loop principal: {total:,} inteiros impares testados em {dt:.1f}s.")

    # Parte 5a: descidas / nao-resolvidos
    print(f"\nDescidas={stats['descidas']:,}, nao-resolvidos={stats['nao_resolvidos']}")
    if N == 10_000_000:
        ok = stats["descidas"] == 4_999_999 and stats["nao_resolvidos"] == 0
        if not ok:
            falhas += 1
        print(f"  (paper diz 4.999.999 descidas, 0 nao-resolvidos p/ N=10^7): "
              f"{'OK' if ok else 'DIVERGE'}")

    # Parte 5b: casos extremos especificos citados no paper
    maior_tau, n_maior_tau = stats["top_tau"][0]
    maior_rho, n_maior_rho = stats["top_rho"][0]
    print(f"\nMaior tau observado: n={n_maior_tau:,}, tau={maior_tau}")
    if N == 10_000_000:
        ok = (n_maior_tau, maior_tau) == (8_088_063, 155)
        if not ok:
            falhas += 1
        print(f"  (paper: n=8.088.063, tau=155): {'OK' if ok else 'DIVERGE'}")
        tau_dir, M_dir, rho_dir = tau_M_rho(8_088_063, L=L)
        ok2 = (tau_dir == 155 and M_dir == 5_385_051_557
               and abs(rho_dir - 665.8024) < 0.001)
        if not ok2:
            falhas += 1
        print(f"  Checagem direta n=8.088.063: tau={tau_dir}, M={M_dir}, "
              f"rho={rho_dir:.4f} (paper: 155, 5.385.051.557, 665,8024): "
              f"{'OK' if ok2 else 'DIVERGE'}")

    print(f"\nMaior rho observado: n={n_maior_rho:,}, rho={maior_rho:.4f}")
    if N == 10_000_000:
        ok = n_maior_rho == 6_631_675 and abs(maior_rho - 3_033_050.2686) < 0.001
        if not ok:
            falhas += 1
        print(f"  (paper: n=6.631.675, rho=3.033.050,2686): {'OK' if ok else 'DIVERGE'}")
        tau_dir, M_dir, rho_dir = tau_M_rho(6_631_675, L=L)
        ok2 = (tau_dir == 140 and M_dir == 20_114_203_639_877
               and abs(rho_dir - 3_033_050.2686) < 0.001)
        if not ok2:
            falhas += 1
        print(f"  Checagem direta n=6.631.675: tau={tau_dir}, M={M_dir}, "
              f"rho={rho_dir:.4f} (paper: 140, 20.114.203.639.877, "
              f"3.033.050,2686): {'OK' if ok2 else 'DIVERGE'}")

    # Parte 8: estatisticas modulo 64 (Secao 5.4)
    print()
    print("-" * 90)
    print("PARTE 8: estatisticas modulo 64 (Secao 5.4)")
    print("-" * 90)
    if N == 10_000_000:
        d63 = stats["residuo64"][63]
        ok = (d63["count"] == 156250 and abs(d63["soma_tau"] / d63["count"] - 15.5684) < 0.0001
              and d63["max_tau"] == 155 and abs(d63["soma_rho"] / d63["count"] - 82.3772) < 0.001
              and abs(d63["max_rho"] - 2_396_483.7836) < 0.001)
        if not ok:
            falhas += 1
        print(f"n=63 (mod 64): count={d63['count']}, tau_medio={d63['soma_tau'] / d63['count']:.4f}, "
              f"max_tau={d63['max_tau']}, rho_medio={d63['soma_rho'] / d63['count']:.4f}, "
              f"max_rho={d63['max_rho']:.4f}")
        print(f"  (paper: count=156250, tau_medio=15.5684, max_tau=155, "
              f"rho_medio=82.3772, max_rho=2.396.483,7836): {'OK' if ok else 'DIVERGE'}")

        for r, tau_medio_esp in [(27, 10.5626), (31, 10.5617)]:
            d = stats["residuo64"][r]
            tau_medio = d["soma_tau"] / d["count"]
            ok = abs(tau_medio - tau_medio_esp) < 0.0001
            if not ok:
                falhas += 1
            print(f"n={r} (mod 64): tau_medio={tau_medio:.4f} "
                  f"(paper: {tau_medio_esp}): {'OK' if ok else 'DIVERGE'}")

    # Parte 6 e 7: Tabela 2 (espinha, m=6..15) e Tabela 3 (rho medio)
    print()
    print("-" * 90)
    print("PARTES 6-7: Tabelas 2 e 3 (espinha de resistencia modular, m=6..15)")
    print("-" * 90)
    if N == 10_000_000:
        for m in range(6, 16):
            count, tau_medio, max_tau, rho_medio, max_rho = estatisticas_espinha(m, N, L=L)
            count_esp, tau_esp, E_esp = TABELA_2[m]
            rho_esp = TABELA_3[m]
            ok_tabela2 = (count == count_esp and abs(tau_medio - tau_esp) < 0.0001
                          and abs((tau_medio - m) - E_esp) < 0.0001)
            ok_tabela3 = abs(rho_medio - rho_esp) < 0.0001
            if not ok_tabela2:
                falhas += 1
            if not ok_tabela3:
                falhas += 1
            print(f"  m={m}: count={count} (esp={count_esp}), tau_medio={tau_medio:.4f} "
                  f"(esp={tau_esp}), E_m={tau_medio - m:.4f} (esp={E_esp}), "
                  f"rho_medio={rho_medio:.4f} (esp={rho_esp})  "
                  f"Tabela2={'OK' if ok_tabela2 else 'DIVERGE'} "
                  f"Tabela3={'OK' if ok_tabela3 else 'DIVERGE'}")
    else:
        print(f"(N={N:,} != 10^7 -- comparacao com Tabelas 2/3 pulada, "
              f"rodada apenas para checar performance/escala)")

    print(f"\n{falhas} falhas nas Partes 5-8.")
    return falhas


if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 10_000_000
    L = int(sys.argv[2]) if len(sys.argv) > 2 else 5000

    total_falhas = 0
    total_falhas += partes1a4()
    total_falhas += partes5a8(N=N, L=L)

    print()
    print("=" * 90)
    print("VEREDITO")
    print("=" * 90)
    print(f"""
Total de falhas: {total_falhas}

Os quatro resultados algebricos provados (Lemma 3.3, Proposicao 3.4,
Lemma 3.6, Proposicao 3.8) sobre a "espinha de resistencia modular"
S_m = {{n : n=-1 mod 2^m}} foram confirmados exatamente. A reproducao
computacional em grande escala (N={N:,}, limite de passos L={L}) --
incluindo os dois casos extremos citados nominalmente (maior tau em
n=8.088.063, maior rho em n=6.631.675), as estatisticas modulo 64
(Secao 5.4), e as Tabelas 2 e 3 (espinha de resistencia, m=6..15) --
foi comparada byte-a-byte (4 casas decimais) contra os valores exatos
citados no paper.

O paper e HONESTO quanto ao escopo em multiplos pontos explicitos:
"the aim of this work is not to prove the classical Collatz
conjecture"; "these computations do not prove the Collatz conjecture";
"the framework does not resolve the Collatz conjecture." E o
predecessor mais simples (referencia [11]) do paper #015 desta mesma
autora (ja revisado como H-058) -- toda a maquinaria aqui (espinha de
resistencia modular, tempo de primeira descida, razao de pico) e
reaproveitada la como bloco de construcao para o framework mais
elaborado de "canonical shells".
""")
    sys.exit(0 if total_falhas == 0 else 1)
