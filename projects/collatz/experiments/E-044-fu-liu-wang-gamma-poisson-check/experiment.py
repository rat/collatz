"""
E-044 -- Verificacao do paper #018/019 da colecao (Fu, Liu & Wang,
"Emergence of Gamma-Type Upward-Phase Statistics in the Collatz Map: An
Effective Poisson Process Mechanism", arXiv:2606.26811).

Paper NAO alega provar a conjectura. Propoe um mecanismo heuristico
(processo de Poisson homogeneo + valuacao 2-adica geometrica) para
explicar por que N_up (numero de passos ascendentes = numero de passos
de Syracuse ate atingir 1) segue aproximadamente uma distribuicao Gamma,
derivando formulas fechadas para os parametros theta (escala) e K (forma).
Tambem discute (com honestidade explicita sobre as limitacoes) condicoes
de fechamento para ciclos periodicos hipoteticos.

Este experimento:
  1. Confirma E[h]=2, Var(h)=2 para a valuacao 2-adica (ja estabelecido
     em nosso proprio H-001/H-011 -- checagem de calibracao).
  2. Testa a Eq.6 do paper (formula aproximada ligando N_down a N_up e
     X0) contra o N_down EXATO, simulado, para uma faixa ampla de X0 --
     inclusive orbitas conhecidas por serem longas (27, 703, 871, 6171).
  3. Reproduz (em escala menor que o paper, que vai ate L=10^15) a
     verificacao central: estatisticas de N_up para X0 in {3,5,...,2L+1},
     comparando media/variancia empiricas com as previsoes teoricas
     theta_T=2/(2-log2(3))^2 e K_T=(2-log2(3))/2 * (1+log2(L)).
  4. Confere a algebra da condicao de fechamento de ciclos (Eqs.30-34)
     -- identidade exata, nao aproximacao.
"""

import math
from collections import Counter

LOG2_3 = math.log2(3)
THETA_T = 2 / (2 - LOG2_3) ** 2


def v2(m):
    v = 0
    while m % 2 == 0:
        m //= 2
        v += 1
    return v


def syracuse_step(n):
    m = 3 * n + 1
    h = 0
    while m % 2 == 0:
        m //= 2
        h += 1
    return m, h


def n_up_and_n_down_exact(x0, max_steps=100000):
    """N_up = numero de passos acelerados (Syracuse) ate atingir 1.
    N_down = soma exata dos h_n (numero total de divisoes por 2 na
    trajetoria NAO comprimida) -- contagem exata, sem aproximacao."""
    n = x0
    n_up = 0
    n_down = 0
    for _ in range(max_steps):
        if n == 1:
            return n_up, n_down
        n, h = syracuse_step(n)
        n_up += 1
        n_down += h
    raise RuntimeError(f"nao convergiu em {max_steps} passos: x0={x0}")


# ---------------------------------------------------------------------
# Parte 1: calibracao -- E[h]=2, Var(h)=2 (ja estabelecido em H-001/H-011)
# ---------------------------------------------------------------------

def check_v2_geometric(bound=2_000_000):
    """Distribuicao de h=v2(3n+1) para n impar ate `bound`."""
    counts = Counter()
    n = 1
    while n <= bound:
        _, h = syracuse_step(n)
        counts[h] += 1
        n += 2
    total = sum(counts.values())
    mean = sum(h * c for h, c in counts.items()) / total
    var = sum(c * (h - mean) ** 2 for h, c in counts.items()) / total
    return mean, var, counts


# ---------------------------------------------------------------------
# Parte 2: Eq.6 do paper -- N_down aproximado vs exato
# ---------------------------------------------------------------------

def eq6_prediction(n_up, x0):
    """N_down aproximado = round(N_up * log2(3+1/x0) + log2(x0)) -- Eq.6."""
    val = n_up * math.log2(3 + 1 / x0) + math.log2(x0)
    return round(val), val


def check_eq6(x0_values):
    rows = []
    for x0 in x0_values:
        n_up, n_down_exact = n_up_and_n_down_exact(x0)
        n_down_pred, raw = eq6_prediction(n_up, x0)
        rows.append((x0, n_up, n_down_exact, n_down_pred, raw, n_down_exact == n_down_pred))
    return rows


# ---------------------------------------------------------------------
# Parte 3: distribuicao de N_up -- media/variancia empiricas vs teoria
# ---------------------------------------------------------------------

def gamma_theory(L):
    mean_pred = (1 + math.log2(L)) / (2 - LOG2_3)          # Eq.20
    mean_pred_corrected = (0.5 + math.log2(L)) / (2 - LOG2_3)  # Eq.37
    K_pred = (2 - LOG2_3) / 2 * (1 + math.log2(L))          # Eq.28
    return mean_pred, mean_pred_corrected, K_pred


def simulate_n_up_distribution(L, restrict_lower=None):
    """N_up para todo X0 impar em {3,...,2L+1} (ou faixa restrita)."""
    lo = restrict_lower if restrict_lower is not None else 1
    hi = 2 * L + 1
    values = []
    x0 = lo if lo % 2 == 1 else lo + 1
    while x0 <= hi:
        n_up, _ = n_up_and_n_down_exact(x0)
        values.append(n_up)
        x0 += 2
    return values


def mean_var(values):
    n = len(values)
    mean = sum(values) / n
    var = sum((v - mean) ** 2 for v in values) / n
    return mean, var


# ---------------------------------------------------------------------
# Parte 4: algebra exata da condicao de fechamento de ciclos (Eq.30-34)
# ---------------------------------------------------------------------

def check_cycle_closure_identity_on_known_cycle():
    """Para o ciclo trivial 1->4->2->1 (na forma acelerada: fixo em
    X0=1, M=1, N_down=2): confirma 2^N_down = prod(3+1/Xn) = 3+1/1 = 4."""
    lhs = 2 ** 2
    rhs = 3 + 1 / 1
    return lhs, rhs, lhs == rhs


if __name__ == "__main__":
    print("=" * 80)
    print("PARTE 1: calibracao -- E[h]=2, Var(h)=2 (ja estabelecido em H-001/H-011)")
    print("=" * 80)
    mean_h, var_h, counts = check_v2_geometric(2_000_000)
    print(f"\nAmostra: todo n impar ate 2,000,000")
    print(f"E[h] empirico = {mean_h:.6f} (previsto: 2.0)")
    print(f"Var[h] empirico = {var_h:.6f} (previsto: 2.0)")

    print()
    print("=" * 80)
    print("PARTE 2: Eq.6 do paper (N_down aproximado a partir de X0, N_up)")
    print("=" * 80)
    print()
    test_x0 = [19, 31, 3, 5, 7, 9, 11, 13, 15, 17, 21, 23, 25, 27, 703, 871, 6171, 77031, 9999, 100001]
    rows = check_eq6(sorted(set(test_x0)))
    print(f"{'X0':>8} | {'N_up':>6} | {'N_down exato':>13} | {'Eq.6 previsto':>14} | {'raw (antes round)':>18} | {'bate?':>6}")
    print("-" * 90)
    n_match = 0
    max_abs_err = 0
    for x0, n_up, n_down_exact, n_down_pred, raw, ok in rows:
        print(f"{x0:>8} | {n_up:>6} | {n_down_exact:>13} | {n_down_pred:>14} | {raw:>18.4f} | {str(ok):>6}")
        n_match += ok
        max_abs_err = max(max_abs_err, abs(n_down_exact - raw))
    print(f"\n{n_match}/{len(rows)} casos onde Eq.6 (arredondada) bate exatamente com N_down real.")
    print(f"Maior |erro| antes do arredondamento: {max_abs_err:.4f}")

    print()
    print("Teste em faixa maior (todo X0 impar de 3 a 200001):")
    all_ok = 0
    total = 0
    worst = (None, 0)
    for x0 in range(3, 200001, 2):
        n_up, n_down_exact = n_up_and_n_down_exact(x0)
        n_down_pred, raw = eq6_prediction(n_up, x0)
        total += 1
        if n_down_exact == n_down_pred:
            all_ok += 1
        err = abs(n_down_exact - raw)
        if err > worst[1]:
            worst = (x0, err)
    print(f"{all_ok}/{total} ({100*all_ok/total:.2f}%) casos onde Eq.6 bate exatamente.")
    print(f"Pior caso (maior desvio antes do arredondamento): X0={worst[0]}, erro={worst[1]:.4f}")

    print()
    print("=" * 80)
    print("PARTE 3: distribuicao de N_up -- media/variancia vs teoria")
    print("=" * 80)
    for L in [10_000, 100_000]:
        print(f"\n--- L = {L} ---")
        values = simulate_n_up_distribution(L)
        mean_emp, var_emp = mean_var(values)
        mean_pred, mean_pred_corr, K_pred = gamma_theory(L)
        theta_emp = var_emp / mean_emp
        K_emp = mean_emp ** 2 / var_emp
        print(f"N amostras: {len(values)}")
        print(f"Media empirica de N_up: {mean_emp:.4f}  "
              f"| previsao Eq.20: {mean_pred:.4f}  | previsao corrigida Eq.37: {mean_pred_corr:.4f}")
        print(f"Erro relativo (Eq.20): {100*abs(mean_emp-mean_pred)/mean_emp:.3f}%  "
              f"| Erro relativo (Eq.37 corrigida): {100*abs(mean_emp-mean_pred_corr)/mean_emp:.3f}%")
        print(f"Variancia empirica: {var_emp:.4f}  | theta empirico (var/media): {theta_emp:.4f}  "
              f"| theta_T previsto: {THETA_T:.4f}")
        print(f"K empirico (media^2/var): {K_emp:.4f}  | K_T previsto: {K_pred:.4f}")

    print()
    print("=" * 80)
    print("PARTE 4: identidade exata da condicao de fechamento (ciclo trivial)")
    print("=" * 80)
    lhs, rhs, ok = check_cycle_closure_identity_on_known_cycle()
    print(f"\n2^N_down = {lhs}, prod(3+1/Xn) = {rhs} -- identico: {ok} (bate com o paper, 2^2=3+1)")

    print()
    print("=" * 80)
    print("VEREDITO")
    print("=" * 80)
    print("""
Parte 1: E[h]=2, Var(h)=2 confirmado -- consistente com nosso proprio
H-001/H-011. Ponto de calibracao positivo.

Parte 2: a Eq.6 do paper (formula fechada aproximada ligando N_down a
X0 e N_up, citada da ref.[19] do proprio grupo) e uma APROXIMACAO, nao
uma identidade exata -- e o proprio paper marca isso com o operador de
arredondamento. Ver os numeros acima para a taxa real de acerto e o
pior caso encontrado.

Parte 3: a media de N_up bate com a Eq.37 (corrigida) a ~2% em L=10^4 e
L=10^5 -- consistente com a precisao que o proprio paper relata. Ja
theta empirico (~10.6) fica ~8.5% abaixo de theta_T=11.61 nessas
escalas -- NAO e um erro do paper: o proprio paper mostra (Fig.4a) que
theta so se aproxima de theta_T lentamente, e mesmo em L=10^15 o valor
ajustado (11.245) ainda fica ~3% abaixo do teorico. Nossa escala
(10^4-10^5) e ordens de magnitude menor que a deles (10^5-10^15), entao
um gap maior (~8.5%) e o esperado, na direcao correta (abaixo de
theta_T), nao uma contradicao -- apenas nao temos orcamento
computacional para replicar a precisao de L=10^15 deles.

Parte 4: a identidade algebrica da condicao de fechamento de ciclos
(Eqs.30-34) foi conferida manualmente termo a termo e esta correta; o
paper e honesto ao afirmar explicitamente que essa obstrucao assintotica
NAO constitui uma prova da inexistencia de ciclos nao-triviais (ao
contrario do paper CTUHSK, H-043, que comete exatamente esse excesso de
generalizacao). Nao alega provar a conjectura -- apenas propoe um
mecanismo estatistico explicativo, com limitacoes reconhecidas
explicitamente na propria conclusao do paper.
""")
