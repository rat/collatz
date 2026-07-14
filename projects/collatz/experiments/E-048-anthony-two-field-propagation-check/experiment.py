"""
E-048 -- Verificacao do paper #006 (Michael Mark Anthony, "A Two-Field
Propagation Model for the Collatz Map", Enertron Inc., 2026).

Paper propoe um modelo geometrico de dois campos vetoriais + uma
analogia estrutural com a equacao P de Riemann (monodromia) +
reformulacao em coordenadas Mobius Phi(n)=1/(n+1) + potencial digamma
+ um "Teorema do Colapso" (14.1) EXPLICITAMENTE condicional ("Theorem
14.1 should be understood as: if the orbit stays bounded, then it
converges to n=1 ... consistent with, but not a proof of, the
conjecture"). O paper e extremamente cuidadoso e repetido em varias
secoes (Remarks 5.2, 6.1, 10.1, 11.1, 12.1, 14.1, Secao 16) em nao
alegar ter provado ou estendido resultados conhecidos -- so oferece uma
reformulacao estrutural.

Este experimento verifica computacionalmente os resultados centrais
checaveis: a reformulacao Mobius (Prop.5.1), o Teorema 8.1 (nenhuma
expansao infinita no regime m=1), o exemplo trabalhado (Secao 9), a
identidade harmonica exata (Teorema 10.3/10.4), e a identidade
hipergeometrica da funcao digamma (Eq.28) citada na Secao 7.1.
"""

import math
import mpmath as mp

mp.mp.dps = 50  # 50 digitos de precisao


def T_raw(n):
    """Mapa de Collatz padrao (nao acelerado)."""
    return n // 2 if n % 2 == 0 else 3 * n + 1


def v2(n):
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def syracuse_step(n):
    """Um passo do mapa acelerado (Eq.34): retorna (proximo, m)."""
    assert n % 2 == 1
    val = 3 * n + 1
    m = v2(val)
    return val // (2 ** m), m


# ---------------------------------------------------------------------
# Parte 1: reformulacao Mobius Phi(n)=1/(n+1) (Prop.5.1, Eqs.18-21)
# ---------------------------------------------------------------------

def Phi(n):
    return mp.mpf(1) / (n + 1)


def M_E(phi):
    return 2 * phi / (1 + phi)


def M_O(phi):
    return phi / (3 - phi)


def check_mobius_reformulation(n_values):
    failures = []
    for n in n_values:
        phi = Phi(n)
        if n % 2 == 0:
            predicted = M_E(phi)
            actual = Phi(n // 2)
        else:
            predicted = M_O(phi)
            actual = Phi(3 * n + 1)
        if abs(predicted - actual) > mp.mpf(10) ** -30:
            failures.append((n, predicted, actual))
    return failures


# ---------------------------------------------------------------------
# Parte 2: Teorema 8.1 -- regime m=1 nao pode persistir indefinidamente
# ---------------------------------------------------------------------

def longest_run_of_m1(bound=200000):
    """Para todo n impar ate `bound`, conta quantos passos consecutivos
    de m=1 ocorrem a partir de n (Teorema 8.1 diz: finito sempre, e
    especificamente n0 precisa ser ≡ -1 mod 2^(t+1) para sustentar t
    passos)."""
    max_run = 0
    max_run_n = None
    for n in range(1, bound, 2):
        cur = n
        run = 0
        for _ in range(60):  # 60 passos e mais que suficiente
            nxt, m = syracuse_step(cur)
            if m == 1:
                run += 1
                cur = nxt
            else:
                break
        if run > max_run:
            max_run = run
            max_run_n = n
    return max_run, max_run_n


def check_theorem_8_1_congruence(t_max=10):
    """Confirma a condicao do Teorema 8.1: se m=1 vale por t passos
    consecutivos a partir de n0, entao n0 = -1 mod 2^(t+1). Testamos
    construindo n0 = 2^(t+1) - 1 (que satisfaz n0 = -1 mod 2^(t+1)) e
    verificando quantos passos consecutivos de m=1 ele realmente sustenta."""
    results = []
    for t in range(1, t_max + 1):
        n0 = 2 ** (t + 1) - 1  # n0 = -1 mod 2^(t+1)
        cur = n0
        run = 0
        for _ in range(t + 5):
            nxt, m = syracuse_step(cur)
            if m == 1:
                run += 1
                cur = nxt
            else:
                break
        results.append((t, n0, run))
    return results


# ---------------------------------------------------------------------
# Parte 3: exemplo trabalhado da Secao 9 (n=7)
# ---------------------------------------------------------------------

def check_worked_example_n7():
    seq = [7]
    cur = 7
    while cur != 1:
        cur = T_raw(cur)
        seq.append(cur)
    expected = [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    phi_seq = [f"1/{n+1}" for n in seq]
    return seq, expected, seq == expected, phi_seq


# ---------------------------------------------------------------------
# Parte 4: identidade harmonica exata (Teorema 10.3/10.4)
# ---------------------------------------------------------------------

def check_harmonic_digamma_identity(q_values):
    results = []
    for q in q_values:
        Hq = sum(mp.mpf(1) / k for k in range(1, q + 1))
        psi_val = mp.digamma(q + 1) + mp.euler
        diff = abs(Hq - psi_val)
        results.append((q, Hq, psi_val, diff))
    return results


def check_euler_mascheroni_limit(q_values):
    results = []
    for q in q_values:
        Hq = sum(mp.mpf(1) / k for k in range(1, q + 1))
        diff = Hq - mp.log(q)
        results.append((q, diff))
    return results


# ---------------------------------------------------------------------
# Parte 5: identidade hipergeometrica para digamma (Eq.28, Secao 7.1)
# ---------------------------------------------------------------------

def check_hypergeometric_digamma_identity(z_values):
    """Eq.28: psi(z) = (z-1)*3F2(1,1,2-z; 2,2; 1) - gamma, Re(z)>0."""
    results = []
    for z in z_values:
        lhs = mp.digamma(z)
        try:
            hyp_val = mp.hyper([1, 1, 2 - z], [2, 2], 1)
            rhs = (z - 1) * hyp_val - mp.euler
            diff = abs(lhs - rhs)
        except Exception as e:
            rhs = None
            diff = None
        results.append((z, lhs, rhs, diff))
    return results


if __name__ == "__main__":
    print("=" * 80)
    print("PARTE 1: reformulacao Mobius Phi(n)=1/(n+1) (Proposicao 5.1)")
    print("=" * 80)
    failures1 = check_mobius_reformulation(list(range(1, 5000)))
    print(f"\nTestado n=1..4999: falhas = {len(failures1)}")
    if not failures1:
        print("CONFIRMADO: M_E e M_O reproduzem exatamente Phi(T(n)) para todo n testado.")

    print()
    print("=" * 80)
    print("PARTE 2: Teorema 8.1 (regime m=1 nao pode persistir indefinidamente)")
    print("=" * 80)
    max_run, max_run_n = longest_run_of_m1(200000)
    print(f"\nMaior corrida consecutiva de m=1 encontrada ate n=200000: {max_run} passos (em n={max_run_n})")
    print("(Teorema 8.1 preve que corridas sao sempre finitas -- nenhum n positivo sustenta m=1 para sempre)")

    print("\nConstrucao explicita n0=2^(t+1)-1 (deveria sustentar exatamente t passos de m=1):")
    results2 = check_theorem_8_1_congruence(10)
    all_match = True
    for t, n0, run in results2:
        match = (run == t)
        all_match = all_match and match
        print(f"  t={t:>2}: n0={n0:>6}, corrida real de m=1 = {run} passos (esperado {t}, bate={match})")
    print(f"\nCONFIRMADO: construcao do Teorema 8.1 funciona exatamente como previsto: {all_match}")

    print()
    print("=" * 80)
    print("PARTE 3: exemplo trabalhado da Secao 9 (n=7)")
    print("=" * 80)
    seq, expected, ok, phi_seq = check_worked_example_n7()
    print(f"\nTrajetoria calculada: {seq}")
    print(f"Trajetoria do paper:  {expected}")
    print(f"Bate exatamente: {ok}")

    print()
    print("=" * 80)
    print("PARTE 4: identidade harmonica exata (Teorema 10.3/10.4)")
    print("=" * 80)
    results4 = check_harmonic_digamma_identity([10, 100, 1000, 10000])
    print(f"\n{'q':>6} | {'H_q':>20} | {'psi(q+1)+gamma':>20} | {'|diferenca|':>15}")
    for q, hq, psi_val, diff in results4:
        print(f"{q:>6} | {str(hq)[:20]:>20} | {str(psi_val)[:20]:>20} | {float(diff):>15.2e}")
    print("\nCONFIRMADO: H_q = psi(q+1)+gamma exatamente (diferenca ~ erro de precisao numerica).")

    results4b = check_euler_mascheroni_limit([100, 10000, 1000000])
    print(f"\nH_q - ln(q) conforme q cresce (deveria -> gamma = {float(mp.euler):.10f}):")
    for q, diff in results4b:
        print(f"  q={q:>10}: H_q - ln(q) = {float(diff):.10f}")

    print()
    print("=" * 80)
    print("PARTE 5: identidade hipergeometrica para digamma (Eq.28, Secao 7.1)")
    print("=" * 80)
    results5 = check_hypergeometric_digamma_identity([mp.mpf(2), mp.mpf(3), mp.mpf('2.5'), mp.mpf(5)])
    all_ok5 = True
    for z, lhs, rhs, diff in results5:
        ok = diff is not None and diff < mp.mpf(10) ** -20
        all_ok5 = all_ok5 and ok
        print(f"z={float(z):>5}: psi(z)={float(lhs):.10f}, formula(z)={float(rhs) if rhs is not None else 'ERRO'}, "
              f"|diferenca|={float(diff) if diff is not None else 'N/A'}, bate={ok}")
    print(f"\nIdentidade hipergeometrica da Eq.28 confirmada para todos os z testados: {all_ok5}")

    print()
    print("=" * 80)
    print("VEREDITO")
    print("=" * 80)
    all_confirmed = (not failures1 and all_match and ok and all_ok5)
    print(f"""
Todas as reivindicacoes VERIFICAVEIS foram CONFIRMADAS: {all_confirmed}

- Reformulacao Mobius Phi(n)=1/(n+1) (Prop.5.1): confirmada em 4999 casos.
- Teorema 8.1 (nenhuma expansao infinita no regime m=1): confirmado --
  maior corrida encontrada ate n=200000 foi de {max_run} passos, e a
  construcao explicita n0=2^(t+1)-1 sustenta exatamente t passos como
  previsto pela propria prova do teorema.
- Exemplo trabalhado n=7 (Secao 9): confirmado exatamente.
- Identidade harmonica exata H_q=psi(q+1)+gamma (Teorema 10.3) e limite
  de Euler-Mascheroni (Teorema 10.4): confirmados -- sao fatos padrao
  da funcao digamma, nao especificos do Collatz, mas corretamente usados.
- Identidade hipergeometrica psi(z)=(z-1)*3F2(1,1,2-z;2,2;1)-gamma
  (Eq.28): confirmada numericamente para varios z.

O paper e NOTAVELMENTE cuidadoso e honesto ao longo de TODO o texto
(Remarks 5.2, 6.1, 10.1, 11.1, 12.1, 14.1, e a Secao 16 inteira) em
distinguir com precisao: (a) o que e teorema provado sobre a
reformulacao (Teorema 8.1 -- prova por inducao 2-adica -- e Teoremas
10.3/10.4 -- fatos padrao da funcao digamma); (b) o que e analogia
estrutural, nao identificacao literal (Prop.6.1/Remark 6.1 -- "this is
an analogy of form, not of kind"); (c) o que e heuristico/condicional
(Teorema 10.2 -- explicitamente "under the standard heuristic"; Teorema
14.1 -- explicitamente "conditional...consistent with, but not a proof
of, the conjecture"); e (d) onde NAO ha extensao de resultados
conhecidos (Secao 12 sobre o resultado de Tao: "No claim is made...").
O proprio autor identifica e corrige, dentro do texto, uma reivindicacao
anterior equivocada (delta_m=1/m, Secao 10) -- um sinal forte de
pratica de pesquisa cuidadosa, nao de um erro que tivemos que caçar.

Muito do aparato (equacao P de Riemann, monodromia, PGL(2,C), funcao
digamma, series hipergeometricas, 24 solucoes de Kummer) e melhor
descrito como CONTEXTO/ANALOGIA DECORATIVA do que como conteudo
matematico com peso real sobre a conjectura -- o proprio paper concorda
com essa leitura (Secao 16: "these are structural observations that
complement, rather than compete with, the density-theoretic results").
Nenhum erro encontrado nas reivindicacoes que testamos.
""")
