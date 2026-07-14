"""
E-040 - Verificacao independente do Teorema 5.1 do paper #004 (Seymour,
"First-Principles Derivation of the Steiner Sentence Length Distribution").

O paper afirma P(sentence length=k) = 3^(k-1)/4^k, e explicitamente
argumenta contra o modelo "ingenuo" P(length=k)=(1/2)^k. Este script
reimplementa as definicoes exatas do paper (Def 1.2 Steiner word,
Def 1.3 Steiner sentence, Teorema 2.1 - matriz de transicao mod 8) a
partir do zero e testa qual formula bate com a simulacao real.

Resultado: a matriz de transicao (Teorema 2.1) bate exatamente. Mas a
distribuicao de comprimento de sentenca bate com (1/2)^k, NAO com
3^(k-1)/4^k -- ou seja, o modelo que o paper chama de "ingenuo" e
tenta refutar parece ser o CORRETO.
"""
import random
from collections import Counter


def v2(m):
    v = 0
    while m % 2 == 0:
        m //= 2
        v += 1
    return v


def S(n):
    """Mapa de Syracuse: S(n) = (3n+1)/2^v2(3n+1), para n impar."""
    m = 3 * n + 1
    return m // (2 ** v2(m))


def verify_transition_matrix(N=200_000, seed=1):
    """Verifica o Teorema 2.1 (matriz de transicao mod 8) por amostragem direta."""
    random.seed(seed)
    counts = {a: Counter() for a in [1, 3, 5, 7]}
    for _ in range(N):
        n = random.randrange(1, 10**12) | 1
        a = n % 8
        b = S(n) % 8
        counts[a][b] += 1
    print("=== Verificacao do Teorema 2.1 (matriz de transicao) ===")
    expected = {
        1: {1: 0.25, 3: 0.25, 5: 0.25, 7: 0.25},
        3: {1: 0.5, 3: 0.0, 5: 0.5, 7: 0.0},
        5: {1: 0.25, 3: 0.25, 5: 0.25, 7: 0.25},
        7: {1: 0.0, 3: 0.5, 5: 0.0, 7: 0.5},
    }
    for a in [1, 3, 5, 7]:
        total = sum(counts[a].values())
        row = {b: counts[a][b] / total for b in [1, 3, 5, 7]}
        print(f"  P[{a}][*] observado = {row}")
        print(f"  P[{a}][*] esperado  = {expected[a]}")
    print()


def sentence_length(n):
    """Comprimento (numero de palavras Steiner) da sentenca que comeca em
    n (n deve ser ≡5 mod 8, conforme protocolo do proprio paper, Apendice B)."""
    assert n % 8 == 5
    cur = S(n)  # b0 = primeira entrada da nova sentenca
    words = 0
    while True:
        # consome UMA palavra: anda ate achar residuo terminal (1 ou 5)
        node = cur
        while node % 8 not in (1, 5):
            node = S(node)
        term = node % 8
        words += 1
        if term == 5:
            return words
        cur = S(node)  # node tem residuo 1 (palavra de abertura); proxima palavra comeca aqui


def empirical_distribution(N=300_000, Tmax=10**12, seed=42):
    random.seed(seed)
    lengths = Counter()
    for _ in range(N):
        t = random.randrange(1, Tmax)
        n = 8 * t + 5
        k = sentence_length(n)
        lengths[k] += 1
    return lengths


def report(lengths, kmax=12):
    total = sum(lengths.values())
    print(f"{'k':>3} {'empirico':>10} {'paper 3^(k-1)/4^k':>18} {'geometrica (1/2)^k':>20}")
    for k in range(1, kmax + 1):
        emp = lengths.get(k, 0) / total
        paper = (3 ** (k - 1)) / (4 ** k)
        geom = (1 / 2) ** k
        print(f"{k:>3} {emp:>10.5f} {paper:>18.5f} {geom:>20.5f}")
    print(f"\ntotal de amostras = {total}")


def hand_trace_counterexample():
    """Rastreio manual, aritmetica exata, de um caso concreto onde uma
    sentenca de comprimento 1 surge com b0=7 (nao b0=5), contradizendo
    a prova do Teorema 5.1 do paper (que so conta b0=5 para length=1)."""
    n = 68567
    print("=== Contraexemplo concreto (aritmetica exata, sem aleatoriedade) ===")
    print(f"n = {n} (n mod 8 = {n % 8})")
    cur = n
    seq = []
    for _ in range(5):
        seq.append(cur % 8)
        if cur % 8 in (1, 5) and cur != n:
            break
        m = 3 * cur + 1
        v = v2(m)
        nxt = m // (2 ** v)
        print(f"  n={cur} (mod8={cur%8}): 3n+1={m}=2^{v}*{m//(2**v)}, S(n)={nxt} (mod8={nxt%8})")
        cur = nxt
        if cur % 8 in (1, 5):
            seq.append(cur % 8)
            break
    print(f"Sequencia de residuos mod 8: {seq}")
    print("Isso casa com o regex (7*3)?(1|5) como UMA SO palavra Steiner,")
    print("terminando em letra 5 -- logo sentenca de length=1 com b0=7, nao b0=5.")


if __name__ == "__main__":
    verify_transition_matrix()
    hand_trace_counterexample()
    print()
    lengths = empirical_distribution()
    report(lengths)
