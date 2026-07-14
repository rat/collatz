"""
E-050 -- Verificacao do paper #008 (Juan Carlos Ruiz Castillo, "Dissipative
Bounds and Ruiz Castillo Residual Decomposition in the Accelerated
Dynamics of the Collatz Conjecture").

Segundo paper de Ruiz Castillo revisado nesta colecao (o primeiro foi
item 001, H-039). Mesmo padrao: terminologia extensa e propria
("residual debt", "dissipative pressure", "normalized residue",
"residual decomposition") aplicada a um fato elementar ja conhecido --
a identidade exata de "desenrolar" o mapa acelerado,
U^k(n) = (3^k n + B_k(n)) / 2^{A_k(n)}, que e a mesma identidade de
"equacao de ciclo" usada (com outra notacao) em varios outros papers ja
revisados nesta colecao (Fu-Liu-Wang E-044, Mohammed E-045). O paper
explicitamente NAO alega prova ("does not claim to assert a final proof
of the Collatz Conjecture"). Ambas as figuras do paper sao rotuladas
"conceptual... does not represent real computational data" -- ou seja,
ZERO conteudo numerico real, mesmo padrao do primeiro paper Ruiz
Castillo (H-039: "zero conteudo numerico").

Este experimento verifica as identidades/proposicoes centrais.
"""

import math
import random
from fractions import Fraction

LOG2_3 = math.log2(3)


def v2(m):
    v = 0
    while m % 2 == 0:
        m //= 2
        v += 1
    return v


def U(n):
    assert n % 2 == 1
    m = 3 * n + 1
    return m // (2 ** v2(m))


def accelerated_orbit_data(n, k):
    """Retorna (n_k, lista de a_j(n) para j=0..k-1)."""
    cur = n
    a_list = []
    for _ in range(k):
        val = 3 * cur + 1
        a = v2(val)
        a_list.append(a)
        cur = val // (2 ** a)
    return cur, a_list


def A_k(a_list, k):
    return sum(a_list[:k])


def B_k_direct(n, k):
    """B_k(n) via a definicao original: U^k(n) = (3^k n + B_k(n)) / 2^{A_k(n)}."""
    nk, a_list = accelerated_orbit_data(n, k)
    Ak = sum(a_list)
    Bk = nk * (2 ** Ak) - (3 ** k) * n
    return Bk, Ak, a_list


def B_k_closed_form(a_list, k):
    """Proposicao 3.3: B_k(n) = sum_{i=0}^{k-1} 3^{k-1-i} 2^{A_i(n)}."""
    total = 0
    for i in range(k):
        Ai = sum(a_list[:i])
        total += 3 ** (k - 1 - i) * (2 ** Ai)
    return total


def L_k(k, Ak):
    return k * LOG2_3 - Ak


def R_k_from_B(Bk, Ak):
    return Fraction(Bk, 2 ** Ak)


def R_k_symbolic(a_list, k):
    """Proposicao 5.1: R_k(n) = sum_{i=0}^{k-1} 3^{k-1-i} 2^{A_i(n)-A_k(n)}."""
    Ak = sum(a_list)
    total = Fraction(0)
    for i in range(k):
        Ai = sum(a_list[:i])
        total += Fraction(3) ** (k - 1 - i) * Fraction(2) ** (Ai - Ak)
    return total


def check_exact_affine_and_decomposition(n_values, k_values):
    failures = []
    for n in n_values:
        for k in k_values:
            Bk_direct, Ak, a_list = B_k_direct(n, k)
            Bk_closed = B_k_closed_form(a_list, k)
            if Bk_direct != Bk_closed:
                failures.append(("B_k mismatch", n, k, Bk_direct, Bk_closed))
                continue
            # verifica U^k(n) = (3^k n + B_k(n)) / 2^{A_k(n)}
            nk_direct, _ = accelerated_orbit_data(n, k)
            rhs = Fraction(3 ** k * n + Bk_direct, 2 ** Ak)
            if Fraction(nk_direct) != rhs:
                failures.append(("affine identity mismatch", n, k))
                continue
            # verifica decomposicao residual U^k(n) = 2^{Lk}n + Rk
            Lk = L_k(k, Ak)
            Rk = R_k_from_B(Bk_direct, Ak)
            Rk_sym = R_k_symbolic(a_list, k)
            if abs(Rk - Rk_sym) > Fraction(1, 10**30):
                failures.append(("R_k symbolic mismatch", n, k))
                continue
            lhs_decomp = (2 ** Lk) * n + float(Rk)
            if abs(lhs_decomp - nk_direct) > 1e-6:
                failures.append(("decomposition mismatch", n, k, lhs_decomp, nk_direct))
    return failures


def check_no_exact_equilibrium(n_values, k_values):
    """Proposicao 2.14: L_k(n) nunca e exatamente 0 para k>=1 (equivale a
    2^{A_k(n)} = 3^k, impossivel por fatoracao unica)."""
    violations = []
    for n in n_values:
        for k in k_values:
            _, Ak, _ = B_k_direct(n, k)
            if 2 ** Ak == 3 ** k:
                violations.append((n, k))
    return violations


def check_sensitivity_to_order():
    """Proposicao 5.5: palavras (1,3) e (3,1) tem mesma soma A_2=4 mas
    R_2 diferente (5/16 vs 11/16)."""
    r1 = R_k_symbolic([1, 3], 2)
    r2 = R_k_symbolic([3, 1], 2)
    return r1, r2, r1 == Fraction(5, 16), r2 == Fraction(11, 16), r1 != r2


def check_universal_bound(n_values, k_values):
    """Proposicao 7.1: R_k(n) <= (3/2)^k - 1 sempre."""
    violations = []
    for n in n_values:
        for k in k_values:
            Bk, Ak, a_list = B_k_direct(n, k)
            Rk = R_k_from_B(Bk, Ak)
            bound = Fraction(3, 2) ** k - 1
            if Rk > bound:
                violations.append((n, k, float(Rk), float(bound)))
    return violations


def check_descent_criterion(n_values, k_values):
    """Teorema 8.7: U^k(n) < n  <=>  R_k(n) < (1 - 2^{L_k(n)}) n.

    IMPORTANTE: usar 2^{L_k(n)} = 3^k/2^{A_k(n)} EXATO (Fraction), nao
    2**(k*log2(3)-Ak) via float -- a primeira tentativa usando log2(3)
    em ponto flutuante deu 3 'falhas' espurias, todas em n=1 (o ponto
    fixo U^k(1)=1 para todo k), causadas por erro de arredondamento de
    ponto flutuante bem no limiar da desigualdade (onde ambos os lados
    sao exatamente iguais a n, entao qualquer erro de precisao pode
    empurrar para o lado errado de uma desigualdade estrita). Corrigido
    usando aritmetica exata -- confirma que o teorema do paper esta
    correto; o erro era no nosso proprio codigo de verificacao, nao no
    paper."""
    failures = []
    for n in n_values:
        for k in k_values:
            nk, a_list = accelerated_orbit_data(n, k)
            Ak = sum(a_list)
            Bk = nk * (2 ** Ak) - (3 ** k) * n
            two_pow_Lk = Fraction(3 ** k, 2 ** Ak)  # exato, evita log2(3) em float
            Rk = R_k_from_B(Bk, Ak)
            lhs = nk < n
            rhs = Rk < (1 - two_pow_Lk) * n
            if lhs != rhs:
                failures.append((n, k, lhs, rhs))
    return failures


if __name__ == "__main__":
    random.seed(1)
    test_n = [1, 3, 5, 7, 9, 11, 15, 27, 31, 41, 71, 127, 703, 871] + \
              [random.randrange(1, 200000, 2) for _ in range(30)]
    test_k = [1, 2, 3, 5, 8, 12]

    print("=" * 80)
    print("PARTE 1: identidade afim exata e decomposicao residual (Prop.3.1/3.3, Teo.4.3)")
    print("=" * 80)
    f1 = check_exact_affine_and_decomposition(test_n, test_k)
    print(f"\nTestados {len(test_n)} valores de n x {len(test_k)} valores de k: falhas = {len(f1)}")
    if f1:
        print("Exemplos:", f1[:5])
    else:
        print("CONFIRMADO: U^k(n)=(3^k n+B_k(n))/2^A_k(n), formula fechada de B_k(n), e")
        print("a decomposicao U^k(n)=2^{L_k(n)}n+R_k(n) todas batem exatamente.")

    print()
    print("=" * 80)
    print("PARTE 2: nao-existencia de equilibrio exato (Proposicao 2.14)")
    print("=" * 80)
    v2_ = check_no_exact_equilibrium(test_n, test_k)
    print(f"\nViolações (L_k(n)=0 exatamente) encontradas: {len(v2_)} "
          f"(esperado 0, garantido por fatoracao unica -- checagem de sanidade)")

    print()
    print("=" * 80)
    print("PARTE 3: sensibilidade a ordem da palavra de valuacao (Proposicao 5.5)")
    print("=" * 80)
    r1, r2, ok1, ok2, distinct = check_sensitivity_to_order()
    print(f"\nPalavra (1,3): R_2={r1} (paper afirma 5/16, bate={ok1})")
    print(f"Palavra (3,1): R_2={r2} (paper afirma 11/16, bate={ok2})")
    print(f"Mesma soma (A_2=4), R_2 diferente: {distinct}")

    print()
    print("=" * 80)
    print("PARTE 4: cota universal (Proposicao 7.1)")
    print("=" * 80)
    v4 = check_universal_bound(test_n, test_k)
    print(f"\nViolações de R_k(n) <= (3/2)^k - 1: {len(v4)} (esperado 0)")
    if v4:
        print("Exemplos:", v4[:5])

    print()
    print("=" * 80)
    print("PARTE 5: criterio de descida (Teorema 8.7)")
    print("=" * 80)
    f5 = check_descent_criterion(test_n, test_k)
    print(f"\nFalhas de equivalencia U^k(n)<n <=> R_k(n)<(1-2^Lk)n: {len(f5)} (esperado 0)")
    if f5:
        print("Detalhe das falhas (investigar se e erro real ou artefato de ponto flutuante):")
        for n, k, lhs, rhs in f5:
            print(f"  n={n}, k={k}: U^k(n)<n = {lhs}, R_k(n)<(1-2^Lk)n = {rhs}")

    print()
    print("=" * 80)
    print("VEREDITO")
    print("=" * 80)
    all_ok = not f1 and not v2_ and ok1 and ok2 and distinct and not v4 and not f5
    print(f"""
Todas as reivindicacoes VERIFICAVEIS foram CONFIRMADAS: {all_ok}

O paper e matematicamente CORRETO em tudo que verificamos -- mas o
conteudo e inteiramente ELEMENTAR: a "identidade afim exata" e apenas o
"desenrolar" padrao do mapa acelerado (a mesma "equacao de ciclo" usada,
com notacao diferente, em varios outros papers ja revisados nesta
colecao -- Fu-Liu-Wang E-044, Mohammed E-045), e as "cotas dissipativas"
sao series geometricas elementares. Nenhuma das proposicoes/teoremas
exige mais que inducao simples ou soma de serie geometrica.

Ambas as figuras do paper sao explicitamente rotuladas "conceptual...
does not represent real computational data" -- ZERO conteudo numerico
real em 44 paginas, mesmo padrao do primeiro paper Ruiz Castillo desta
colecao (item 001, H-039: "zero conteudo numerico, unica figura
explicitamente conceptual").

Referencias: 4 externas reais (Lagarias x2, Wirsching, Tao) e 12
autocitacoes do proprio Ruiz Castillo (75% autocitacao) -- a lista de
autocitacoes revela pelo menos mais ~12 papers com titulos quase
identicos ja escritos pelo mesmo autor sobre a mesma "decomposicao
residual" (ex: "Descending subcylinders...", "Residual drift and
average dissipative pressure...", "Ergodic interpretation of 2-adic
valuations...", etc.) -- forte indicio de que os demais papers Ruiz
Castillo ainda na fila desta colecao (itens 010, 013, 017, 020) seguirao
o mesmo padrao: matematica elementar correta, terminologia extensa,
zero verificacao numerica.

O paper e explicito e correto ao nao alegar prova: "The present work
does not claim to assert a final proof of the Collatz Conjecture."
""")
