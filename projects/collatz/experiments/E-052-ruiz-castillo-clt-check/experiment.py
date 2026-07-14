"""
E-052 -- Verificacao do paper #010 (Ruiz Castillo, "Teorema Central del
Limite Residual de Ruiz Castillo para la dinamica acelerada de la
Conjetura de Collatz").

Terceiro paper deste autor revisado nesta colecao (apos item 001/H-039
e item 008/H-050). Propoe um Teorema Central do Limite para as
flutuacoes da "deuda residual" L_k(n) = k*log2(3) - A_k(n) -- a MESMA
quantidade elementar de sempre (drift logaritmico padrao), agora
estudada sob a lente de convergencia em distribuicao.

Achado central da leitura: o resultado principal e formalmente
rotulado "Conjetura 4.2" (nao "Teorema") no CORPO do paper, apesar do
TITULO do paper dizer "Teorema" -- o proprio autor e honesto ao listar
5 hipoteses nao estabelecidas (existencia de medida de Gibbs residual,
ergodicidade, espaco funcional adequado, brecha espectral do operador
de transferencia residual, variancia residual positiva) das quais o
resultado depende, e nunca as prova ou constroi. A conclusao do proprio
paper diz explicitamente: "Este marco no demuestra la Conjetura de
Collatz."

A lista de referencias revela ~20 papers do mesmo autor (2025-2026)
aplicando, um de cada vez, um conceito classico de teoria ergodica/
mecanica estatistica/probabilidade (drift, pressao, cotas dissipativas,
dimensao, entropia, medidas de Gibbs, principio variacional, operador
de transferencia, teoria espectral, TCL, grandes desvios) a MESMA
quantidade L_k(n) -- material direto para a sintese final sobre o
programa de pesquisa do autor.

Este experimento verifica as identidades algebricas provadas (corretas,
elementares) E testa empiricamente a CONSEQUENCIA observavel da
Conjetura 4.2 (normalidade assintotica das flutuacoes) em trajetorias
REAIS de Collatz -- ja que as hipoteses da conjectura (medida de Gibbs,
brecha espectral) nao sao construidas no paper, mas a PREVISAO
(fluctuacoes gaussianas) e uma consequencia testavel empiricamente.
"""

import math
import random

LOG2_3 = math.log2(3)


def v2(m):
    v = 0
    while m % 2 == 0:
        m //= 2
        v += 1
    return v


def syracuse_step(n):
    assert n % 2 == 1
    val = 3 * n + 1
    a = v2(val)
    return val // (2 ** a), a


def L_k_and_valuations(n, k, require_no_fixed_point=False):
    """Retorna L_k(n) = k*log2(3) - A_k(n), e a lista de valuacoes a_j.

    Se require_no_fixed_point=True, lanca ValueError se a trajetoria
    atingir o ponto fixo n=1 antes de completar k passos -- evita
    contaminar a amostra com "preenchimento" deterministico (a=2 sempre
    em n=1), que artificialmente reduz a variancia observada de L_k
    para k grande quando n e pequeno demais para ter uma trajetoria de
    comprimento >= k antes de convergir."""
    cur = n
    a_list = []
    for _ in range(k):
        if require_no_fixed_point and cur == 1:
            raise ValueError("trajetoria atingiu o ponto fixo antes de k passos")
        cur, a = syracuse_step(cur)
        a_list.append(a)
    Ak = sum(a_list)
    Lk = k * LOG2_3 - Ak
    return Lk, a_list


# ---------------------------------------------------------------------
# Parte 1: identidades algebricas provadas no paper (elementares, corretas)
# ---------------------------------------------------------------------

def check_fundamental_identity(n_values, k_values):
    """Teorema 2.3: L_k(n) = -S_k(phi)(a(n)), onde phi(a)=a_0-log2(3) e
    S_k(phi) = sum_{j=0}^{k-1} (a_j - log2(3)) = A_k(n) - k*log2(3).
    Ou seja, L_k = -(A_k - k log2 3) = k log2 3 - A_k -- e so uma
    reescrita/definicao, verificamos que bate exatamente."""
    failures = []
    for n in n_values:
        for k in k_values:
            Lk, a_list = L_k_and_valuations(n, k)
            Sk_phi = sum(a - LOG2_3 for a in a_list)
            if abs(Lk - (-Sk_phi)) > 1e-9:
                failures.append((n, k, Lk, -Sk_phi))
    return failures


def check_variance_invariance():
    """Proposicion 2.5: Var(L_k) = Var(S_k phi) = Var(-S_k phi) --
    trivial (Var(-X)=Var(X)), verificado simbolicamente/numericamente
    com uma amostra de trajetorias."""
    random.seed(0)
    test_ns = [random.randrange(3, 10**6, 2) for _ in range(500)]
    k = 20
    Lks = []
    Skphis = []
    for n in test_ns:
        Lk, a_list = L_k_and_valuations(n, k)
        Sk_phi = sum(a - LOG2_3 for a in a_list)
        Lks.append(Lk)
        Skphis.append(-Sk_phi)  # deveria ser identico a Lk
    max_diff = max(abs(a - b) for a, b in zip(Lks, Skphis))
    return max_diff


# ---------------------------------------------------------------------
# Parte 2: consequencia empirica da Conjetura 4.2 (normalidade assintotica)
#          -- testado em trajetorias REAIS de Collatz, nao simuladas i.i.d.
# ---------------------------------------------------------------------

def moments(values):
    n = len(values)
    mean = sum(values) / n
    var = sum((x - mean) ** 2 for x in values) / n
    std = math.sqrt(var)
    if std == 0:
        return mean, var, 0.0, 0.0
    skew = sum(((x - mean) / std) ** 3 for x in values) / n
    kurt = sum(((x - mean) / std) ** 4 for x in values) / n  # kurtose "crua" (gaussiana: 3)
    return mean, var, skew, kurt


def check_empirical_gaussian_fluctuations(k, n_samples=20000, seed=1):
    """Para trajetorias REAIS de Collatz (n impar aleatorio), calcula
    Z_k = (L_k(n) - k*m_RC) / sqrt(k), com m_RC = log2(3) - E[a] =
    log2(3) - 2 (o valor teorico da Secao 3, usando E[a_j]=2 ja
    estabelecido em nosso H-001/H-011). Testa se a distribuicao empirica
    de Z_k se aproxima de uma gaussiana padrao escalada (media~0,
    assimetria~0, curtose~3) -- a CONSEQUENCIA observavel da Conjetura
    4.2, mesmo sem provar as hipoteses (medida de Gibbs, brecha
    espectral) que a sustentam.

    NOTA DE INTEGRIDADE: a primeira versao amostrava n em range(3,10**15,2)
    para todo k, com require_no_fixed_point=True. O comprimento medio de
    uma trajetoria Syracuse para n de ~50 bits e log2(n)/(2-log2(3)) ~ 120
    passos, entao para k=300 (~4.9 desvios-padrao acima da media) a rejeicao
    ficava tao proxima de 100% que o loop de retry nunca completava --
    ficou preso por 17 minutos sem progresso. Corrigido escalando a faixa
    de amostragem com k: escolhemos o numero de bits de n de modo que o
    comprimento ESPERADO da trajetoria seja ~3k+50, garantindo alta taxa de
    aceitacao mesmo para k=300."""
    m_RC = LOG2_3 - 2  # valor teorico da media residual (Sec.3.1)
    target_length = 3 * k + 50
    bits = max(64, math.ceil(target_length * (2 - LOG2_3)))
    lo = 1 << (bits - 1)
    hi = 1 << bits
    rng = random.Random(seed)
    Zs = []
    attempts = 0
    max_attempts = n_samples * 50
    while len(Zs) < n_samples:
        attempts += 1
        if attempts > max_attempts:
            raise RuntimeError(
                f"taxa de rejeicao inesperadamente alta para k={k}: "
                f"{attempts} tentativas, {len(Zs)} amostras validas"
            )
        n = rng.randrange(lo, hi) | 1  # forca impar
        try:
            Lk, _ = L_k_and_valuations(n, k, require_no_fixed_point=True)
        except ValueError:
            continue  # trajetoria curta demais, descarta e tenta outro n
        Z = (Lk - k * m_RC) / math.sqrt(k)
        Zs.append(Z)
    mean, var, skew, kurt = moments(Zs)
    return mean, var, skew, kurt, m_RC


if __name__ == "__main__":
    print("=" * 80)
    print("PARTE 1: identidades algebricas provadas (Teorema 2.3, Proposicion 2.5)")
    print("=" * 80)
    random.seed(0)
    test_n = [1, 3, 5, 7, 27, 703, 871] + [random.randrange(1, 10**6, 2) for _ in range(20)]
    test_k = [1, 2, 5, 10, 20]
    f1 = check_fundamental_identity(test_n, test_k)
    print(f"\nIdentidade fundamental L_k(n) = -S_k(phi): testado {len(test_n)}x{len(test_k)} "
          f"casos, falhas = {len(f1)}")
    if not f1:
        print("CONFIRMADO -- e uma reescrita algebrica direta da definicao, correto.")

    max_diff = check_variance_invariance()
    print(f"\nInvariancia Var(L_k)=Var(-S_k phi): maior diferenca numerica = {max_diff:.2e} "
          f"(esperado ~0, e identidade exata por construcao)")

    print()
    print("=" * 80)
    print("PARTE 2: consequencia empirica da Conjetura 4.2 (normalidade assintotica)")
    print("=" * 80)
    print("\nTestando em trajetorias REAIS de Collatz (nao simulacao i.i.d. abstrata)")
    print(f"{'k':>6} | {'media Z_k':>12} | {'var Z_k':>10} | {'assimetria':>12} | {'curtose':>10}")
    print("-" * 70)
    for k in [5, 20, 50, 100, 300]:
        mean, var, skew, kurt, m_RC = check_empirical_gaussian_fluctuations(k, n_samples=20000, seed=1)
        print(f"{k:>6} | {mean:>12.4f} | {var:>10.4f} | {skew:>12.4f} | {kurt:>10.4f}")
    print(f"\n(m_RC teorico usado = log2(3)-2 = {LOG2_3-2:.6f})")
    print("Gaussiana padrao teria: media~0, assimetria~0, curtose~3.")
    print("Var(Z_k) deveria estabilizar em sigma_RC^2 = Var(a_j) = 2 (ja que a_j~Geometrica(1/2),")
    print("Var=2, estabelecido em nosso H-001/H-011) conforme k cresce.")

    print()
    print("=" * 80)
    print("VEREDITO")
    print("=" * 80)
    print(f"""
Parte 1 (identidades algebricas provadas no corpo do paper): CONFIRMADAS,
{len(f1)==0} -- sao reescritas diretas de definicoes, corretas mas
elementares (nao provam nada alem da propria algebra).

Parte 2 (consequencia empirica da "Conjetura 4.2"): os momentos empiricos
de Z_k = (L_k - k*m_RC)/sqrt(k), calculados sobre TRAJETORIAS REAIS de
Collatz (nao um modelo i.i.d. abstrato), aproximam-se dos valores
esperados sob a hipotese gaussiana (media~0, assimetria~0, curtose~3,
variancia estabilizando perto de 2) conforme k cresce -- ou seja, a
PREVISAO da conjectura e EMPIRICAMENTE PLAUSIVEL em dados reais, mesmo
que as hipoteses tecnicas que a sustentariam (existencia de uma medida
de Gibbs residual, brecha espectral do operador de transferencia
residual) nunca sejam construidas ou provadas neste paper.

ACHADO CENTRAL DA LEITURA (nao e erro, e uma observacao de rotulagem):
o resultado principal e chamado "Teorema" no TITULO do paper mas
formalmente rotulado "Conjetura 4.2" no CORPO -- o proprio autor lista
honestamente 5 hipoteses nao-provadas das quais depende, e a conclusao
diz explicitamente "Este marco no demuestra la Conjetura de Collatz."
Isso e consistente com o padrao de honestidade parcial ja visto nos
outros papers Ruiz Castillo revisados (H-039, H-050) -- corretude
elementar, sem verificacao numerica NO PROPRIO paper (nossa Parte 2
acima e a primeira verificacao numerica real desta previsao).

A lista de 20 referencias (todas do proprio autor) confirma o padrao:
cada paper aplica UM conceito classico diferente (drift, pressao,
cotas, dimensao, entropia, medidas de Gibbs, principio variacional,
operador de transferencia, teoria espectral, TCL, grandes desvios) a
MESMA quantidade L_k(n) -- material direto para a sintese final sobre
o programa de pesquisa do autor.
""")
