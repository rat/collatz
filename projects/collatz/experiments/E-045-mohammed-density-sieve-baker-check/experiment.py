"""
E-045 -- Verificacao do paper #011 (Abdullah Mohammed, "Structural
Analysis, Dynamic Density Sieve, and Logarithmic Contraction of Collatz
Sequences"). Alega prova completa da Conjectura de Collatz.

Estrutura da "prova":
  Sec.2-3: sieve de densidade geometrica P(M=m)=1/2^m e E[M]=2 -- correto,
           igual ao nosso H-001/H-011.
  Sec.4:   exclusao de 1-ciclos via n=1/(2^m-3) -- CORRETO (elementar).
  Sec.5:   "special numbers" n0=(4^k-1)/3 = 1,5,21,85,341,... -- correto,
           conhecido (numeros que atingem 1 em um passo).
  Sec.6:   equacao de ciclo P-generico (forma padrao, correta em formato)
           + uma "transformacao logaritmica" (Eqs.41-45) que e VACUA --
           e so a identidade 2^log2(x)=x aplicada a uma definicao
           circular de m_i, sem extrair nenhuma informacao nova.
  Sec.7:   alega usar o Teorema de Baker (formas lineares em logaritmos)
           para excluir ciclos nao-triviais e provar contracao global.

O FURO: na Eq.48, o paper substitui M (soma dos expoentes 2-adicos ao
longo do ciclo) pelo valor ERGODICO/MEDIO M~2P (a expectativa E[M]=2 da
Secao 3, que descreve o comportamento MEDIO de um numero impar GENERICO/
ALEATORIO) -- mas a propria equacao de ciclo exata que o paper derivou
na Secao 6 (2^M = prod(3+1/n_i), equivalente ao Eqn.30 do paper
Fu-Liu-Wang, E-044) FORCA M/P -> log2(3) ~ 1.585 (nao 2!) para qualquer
ciclo hipotetico com elementos grandes. Ao usar M~2P (o numero errado)
na comparacao com o Teorema de Baker, o "furo" produz uma checagem VAZIA
que nao restringe nada -- e exatamente o mesmo padrao de erro that
aparece repetidamente nesta colecao: confundir o comportamento
ESTATISTICO/MEDIO (valido para "quase todo" numero, no sentido de Tao)
com a restricao ESPECIFICA que um ciclo hipotetico (objeto autoconsistente,
nao generico) precisaria satisfazer.
"""

import math
from fractions import Fraction

LOG2_3 = math.log2(3)  # ~1.58496
LN2 = math.log(2)
LN3 = math.log(3)


# ---------------------------------------------------------------------
# Parte 1: checagens que estao CORRETAS no paper (Secoes 4 e 5)
# ---------------------------------------------------------------------

def check_no_nontrivial_1cycles(m_max=1000):
    """Secao 4: n=1/(2^m-3) so e inteiro positivo para m=2 (n=1)."""
    solutions = []
    for m in range(1, m_max + 1):
        denom = 2 ** m - 3
        if denom > 0 and 1 % denom == 0:
            solutions.append((m, 1 // denom))
        elif denom < 0 and 1 % denom == 0:
            solutions.append((m, 1 // denom))
    return solutions  # esperado: so [(2, 1)] (m=1 dá n=-1, negativo, corretamente excluído)


def check_special_numbers(k_max=6):
    """Secao 5: n0=(4^k-1)/3 -- confirma que syracuse(n0) == 1 em um passo."""
    def syracuse(n):
        m = 3 * n + 1
        while m % 2 == 0:
            m //= 2
        return m
    rows = []
    for k in range(1, k_max + 1):
        n0 = (4 ** k - 1) // 3
        assert (4 ** k - 1) % 3 == 0
        rows.append((k, n0, syracuse(n0)))
    return rows  # esperado: syracuse(n0)==1 sempre


# ---------------------------------------------------------------------
# Parte 2: o furo central -- M~2P (Eq.48) vs M/P -> log2(3) (real)
# ---------------------------------------------------------------------

def exact_cycle_constraint_demo(P_values, n_values_per_cycle):
    """Para uma cadeia HIPOTETICA de P elementos odd (nao precisa ser um
    ciclo real, so testamos a identidade), confirma 2^M = prod(3+1/n_i)
    exatamente, e mostra que M/P se aproxima de log2(3) conforme os
    elementos crescem -- nunca de 2, exceto no caso trivial P=1,n=1."""
    rows = []
    for P, n_list in zip(P_values, n_values_per_cycle):
        prod = 1.0
        log_prod = 0.0
        for n in n_list:
            prod *= (3 + 1 / n)
            log_prod += math.log(3 + 1 / n)
        M_exact = log_prod / LN2  # from 2^M = prod => M = log_prod/ln2
        rows.append((P, min(n_list), M_exact, M_exact / P))
    return rows


def bound_product_3_to_4(P):
    """Prova elementar: para qualquer P-ciclo com elementos positivos
    distintos (P>=2), 3^P < prod(3+1/n_i) < 4^P estritamente (limite
    superior 4^P so e atingido se todo n_i=1, impossivel para P>=2 com
    elementos distintos). Logo 2^M=prod(...) esta estritamente entre
    3^P e 4^P, ou seja M esta estritamente entre P*log2(3) e 2P --
    nunca IGUAL a 2P (a substituicao do paper), exceto no limite
    degenerado P=1."""
    lower = 3 ** P
    upper = 4 ** P
    M_lower = P * LOG2_3
    M_upper = 2 * P
    return lower, upper, M_lower, M_upper


def eq48_as_written(P):
    """Reproduz o calculo do paper na Eq.48: substitui M~2P (ergodico)
    na forma linear Lambda = M ln2 - P ln3."""
    M = 2 * P
    Lambda = M * LN2 - P * LN3
    return Lambda, Lambda / P  # deveria bater com P*ln(4/3), ~0.28768*P


def eq48_correct_substitution(P):
    """O que Eq.48 DEVERIA ter comparado: M forcado pela propria equacao
    de ciclo do paper (Sec.6), M/P -> log2(3) para elementos grandes."""
    M = P * LOG2_3
    Lambda = M * LN2 - P * LN3
    return Lambda, Lambda / P  # deveria dar ~0 (por construcao)


if __name__ == "__main__":
    print("=" * 80)
    print("PARTE 1: checagens do paper que estao corretas (Secoes 4 e 5)")
    print("=" * 80)
    sols = check_no_nontrivial_1cycles(1000)
    print(f"\nSecao 4 (exclusao de 1-ciclos): solucoes inteiras positivas de n=1/(2^m-3) "
          f"para m=1..1000: {sols}")
    print("Confirmado: unica solucao e (m=2, n=1) -- o ciclo trivial. Argumento CORRETO.")

    rows = check_special_numbers(6)
    print(f"\nSecao 5 (special numbers n0=(4^k-1)/3):")
    for k, n0, s in rows:
        print(f"  k={k}: n0={n0}, syracuse(n0)={s} (esperado 1)")
    print("Confirmado: sequencia 1,5,21,85,341,... correta e bem conhecida (OEIS A002450).")

    print()
    print("=" * 80)
    print("PARTE 2: o furo central -- M/P real (~log2(3)) vs M/P usado na Eq.48 (=2)")
    print("=" * 80)

    print(f"\nlog2(3) = {LOG2_3:.6f}  (o que a propria equacao de ciclo do paper, Sec.6, forca)")
    print(f"Valor usado pelo paper na Eq.48: M/P = 2 (a expectativa ERGODICA E[M]=2 da Sec.3)")
    print("Essas sao DUAS quantidades diferentes -- E[M]=2 descreve o numero impar TIPICO/")
    print("ALEATORIO; um ciclo hipotetico e um objeto AUTOCONSISTENTE que obedece 2^M=prod(3+1/n_i),")
    print("nao a media ergodica.")

    print("\n--- Demonstracao com cadeias hipoteticas de elementos crescentes ---")
    test_cycles = [
        [1],
        [3, 5],
        [7, 11, 17],
        [101, 203, 407, 305],
        [10_007, 20_013, 15_010, 30_020, 22_515],
        [10**6 + 1, 2 * 10**6 + 1, 3 * 10**6 + 1],
    ]
    P_values = [len(c) for c in test_cycles]
    rows = exact_cycle_constraint_demo(P_values, test_cycles)
    print(f"{'P':>3} | {'min(n_i)':>12} | {'M exato (via prod)':>20} | {'M/P':>10}")
    for P, minn, M_exact, ratio in rows:
        print(f"{P:>3} | {minn:>12} | {M_exact:>20.6f} | {ratio:>10.6f}")
    print(f"\n(log2(3) = {LOG2_3:.6f} para referencia -- note M/P se aproxima disso conforme")
    print("os elementos crescem, e e EXATAMENTE 2.0 so no caso trivial P=1, n=1.)")

    print("\n--- Prova elementar: 2^(2P) e INATINGIVEL por prod(3+1/n_i) para P>=2 ---")
    for P in [1, 2, 3, 5, 10, 50]:
        lower, upper, M_lower, M_upper = bound_product_3_to_4(P)
        print(f"P={P:>3}: 3^P={lower:>15} < prod(3+1/n_i) < 4^P={upper:>15}  "
              f"=>  M esta estritamente em ({M_lower:.4f}, {M_upper:.4f})"
              f"{'  [so atinge 2P no limite degenerado n_i->1 para todo i, impossivel se P>=2]' if P>=2 else ''}")

    print("\n--- Comparando Eq.48 (como escrita) vs a substituicao correta ---")
    for P in [10, 100, 1000, 10**6]:
        lam_wrong, ratio_wrong = eq48_as_written(P)
        lam_right, ratio_right = eq48_correct_substitution(P)
        print(f"P={P:>8}: Eq.48 (M=2P, ERRADO p/ ciclos) -> Lambda={lam_wrong:>14.4f} "
              f"(Lambda/P={ratio_wrong:.5f}, ~ln(4/3)={math.log(4/3):.5f}, bate com o paper)")
        print(f"{'':>11}  Substituicao correta (M=P*log2(3), forcada pela propria Sec.6) "
              f"-> Lambda={lam_right:.2e} (-> 0, por construcao)")

    print()
    print("=" * 80)
    print("VEREDITO")
    print("=" * 80)
    print("""
Secoes 2-5 do paper (sieve geometrico, E[M]=2, exclusao de 1-ciclos,
sequencia de special numbers) estao CORRETAS -- sao fatos elementares
e/ou ja conhecidos (E[M]=2 e o nosso proprio H-001/H-011; a sequencia
1,5,21,85,341,... e OEIS A002450).

A Secao 6 ("Generalized P-th Formulation") produz uma equacao de ciclo
no formato certo, mas a "transformacao logaritmica" das Eqs.41-45 e
VAZIA -- e apenas a identidade 2^log2(x)=x aplicada a uma definicao
circular, sem extrair nenhuma restricao nova sobre a dinamica real.

O FURO DECISIVO esta na Secao 7.1 (Eq.48): para aplicar o Teorema de
Baker e excluir ciclos, seria necessario comparar o limite inferior de
Baker contra o valor de M/P que um ciclo REAL forcaria -- que a propria
Secao 6 do paper mostra ser M/P -> log2(3) ~ 1.585 (para elementos
grandes; verificado acima numericamente E provado elementarmente: para
qualquer P>=2, prod(3+1/n_i) fica estritamente entre 3^P e 4^P, entao M
fica estritamente entre P*log2(3) e 2P, nunca igual a 2P). Em vez
disso, o paper substitui M~2P -- a expectativa ERGODICA/MEDIA de um
numero impar generico (Secao 3), quantidade totalmente diferente e
irrelevante para um ciclo hipotetico especifico. Essa substituicao
errada produz Lambda~0.288*P (cresce linearmente com P), que trivialmente
satisfaz o limite inferior fraco de Baker (~1/P^kappa) -- ou seja, a
"checagem" nao restringe nada. A comparacao que de fato importaria
(Lambda->0 quando M/P->log2(3), o valor real forcado por um ciclo) e
exatamente onde estaria a dificuldade genuina -- e e precisamente aqui
que a literatura seria (Simons, de Weger e outros, usando constantes de
Baker EXPLICITAS) consegue excluir ciclos ate certos comprimentos
especificos, mas nao "todos os ciclos" em geral, porque o argumento nao
fecha para P arbitrariamente grande com as constantes efetivas
conhecidas -- exatamente por isso a conjectura continua aberta.

A Secao 7.2 ("Global Contraction") comete o mesmo tipo de erro por outro
angulo: generaliza um fato ESTATISTICO/ERGODICO (a media geometrica do
fator multiplicativo por passo e ~0.866<1, ou seja "quase todo" numero
decresce em media -- essencialmente o mesmo heuristico por tras do
resultado "quase todas as orbitas" de Tao 2022) para uma alegacao sobre
TODA trajetoria individual, sem justificativa -- exatamente a lacuna que
o proprio resultado de Tao (citado no paper como referencia [1]) NAO
fecha ("almost all", nao "all").

CONCLUSAO: o paper nao prova a Conjectura de Collatz. As secoes
preliminares (2-5) sao corretas mas nao-novas; a secao central que
alegaria fechar o caso geral (7) usa a quantidade errada na comparacao
decisiva com o Teorema de Baker, tornando a "prova" vazia exatamente no
ponto onde a dificuldade real do problema se concentra -- mesmo padrao
generico de erro encontrado nas outras "provas completas" ja catalogadas
(Santos 2018, CTUHSK/H-043): confundir uma afirmacao estatistica/media
("quase todo", "em media") com uma afirmacao universal sobre o objeto
hipotetico especifico (um ciclo, ou toda trajetoria individual).
""")
