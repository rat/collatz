#!/usr/bin/env python3
"""
E-077 - Verifica as afirmacoes numericas concretas de Clay, "The Long
Search for Collatz Counterexamples" (Journal of Humanistic Mathematics
13(2), 2023), item 107 da colecao.

Paper expositivo (nao um artigo tecnico de prova), cobrindo peneiramento
por classes residuais mod 2^k - territorio ja conhecido deste projeto
(H-005, H-007, H-014, H-015). Testa:

1. As tres formulas de "stopping length" nas notas de rodape (Secao 3):
   (a) 2k (par) tem length 2 [sequencia (2k,k)]
   (b) 4k+1 (~1 mod4) tem length 4 [sequencia (4k+1,12k+4,6k+2,3k+1)]
   (c) 16k+3 (~3 mod16) tem length 7 [sequencia de 7 termos ate 9k+2]
   "Length" aqui conta o NUMERO DE TERMOS da sequencia incluindo o
   valor inicial e o valor final abaixo da altitude de partida - nao o
   numero de passos (arestas).

2. A alegacao de que apos excluir classes mod 32/128/256, restam 7.4%
   de altitudes "nao domadas" (Secao 3, paragrafo final) - as classes
   excluidas sao explicitamente listadas na nota de rodape 4: 11,23
   mod32; 7,15,59 mod128; 39,79,95,123,175,199,219 mod256.

3. A arvore da Figura 2 (classes livres de contraexemplo ate mod 128):
   0 mod2, 1 mod4, 3 mod16, 11 mod16, 23 mod32, 7,15,59 mod128.

Reproduzir: python3 experiment.py
"""
import sys
from fractions import Fraction


def collatz_step(n):
    return 3 * n + 1 if n % 2 == 1 else n // 2


def stopping_sequence(n0, max_steps=1000):
    """Sequencia completa desde n0 (inclusive) ate o primeiro valor
    estritamente menor que n0 (inclusive esse valor final)."""
    seq = [n0]
    n = n0
    for _ in range(max_steps):
        n = collatz_step(n)
        seq.append(n)
        if n < n0:
            return seq
    raise RuntimeError(f"nao dipou em {max_steps} passos, n0={n0}")


def test_footnote_formulas(k_values=range(1, 200)):
    """Verifica as tres formulas algebricas exatas das notas de rodape,
    testando k simbolico via varios valores concretos de k (a formula
    deve valer identicamente em k, entao testar varios k confirma isso
    com alta confianca sem precisar de algebra simbolica)."""
    failures = {"a": 0, "b": 0, "c": 0}
    for k in k_values:
        # (a) 2k -> k < 2k, sequencia de 2 termos
        n0 = 2 * k
        seq = stopping_sequence(n0)
        if len(seq) != 2 or seq != [2 * k, k]:
            failures["a"] += 1
            if failures["a"] <= 3:
                print(f"  FALHA (a): k={k} seq={seq}")

        # (b) 4k+1 -> 12k+4 -> 6k+2 -> 3k+1 < 4k+1, sequencia de 4 termos
        n0 = 4 * k + 1
        seq = stopping_sequence(n0)
        expected = [4 * k + 1, 12 * k + 4, 6 * k + 2, 3 * k + 1]
        if seq != expected:
            failures["b"] += 1
            if failures["b"] <= 3:
                print(f"  FALHA (b): k={k} seq={seq} esperado={expected}")

        # (c) 16k+3 -> 48k+10 -> 24k+5 -> 72k+16 -> 36k+8 -> 18k+4 -> 9k+2 < 16k+3
        n0 = 16 * k + 3
        seq = stopping_sequence(n0)
        expected = [16 * k + 3, 48 * k + 10, 24 * k + 5, 72 * k + 16, 36 * k + 8, 18 * k + 4, 9 * k + 2]
        if seq != expected:
            failures["c"] += 1
            if failures["c"] <= 3:
                print(f"  FALHA (c): k={k} seq={seq} esperado={expected}")

    return failures


def test_tame_classes_figure2(mod=128, n_samples_per_class=20):
    """Testa que as classes 'domadas' (tame) da Figura 2 (livres de
    contraexemplo ate mod 128) de fato sempre dipam abaixo do valor
    inicial - i.e., tem stopping time finito e o resultado cai abaixo
    de n0, para muitas instancias de k dentro de cada classe."""
    tame_classes_mod = {
        2: [0],
        4: [1],
        16: [3, 11],
        32: [23],
        128: [7, 15, 59],
    }
    failures = 0
    total = 0
    for m, residues in tame_classes_mod.items():
        for r in residues:
            for k in range(0, n_samples_per_class):
                n0 = m * k + r
                if n0 <= 1:
                    continue  # n0=1 e o proprio destino final, nao ha "abaixo de si mesmo" para testar
                total += 1
                try:
                    seq = stopping_sequence(n0, max_steps=2000)
                except RuntimeError:
                    failures += 1
                    print(f"  FALHA: classe {r} mod {m}, k={k}, n0={n0} nao dipou")
                    continue
                if seq[-1] >= n0:
                    failures += 1
                    print(f"  FALHA: classe {r} mod {m}, k={k}, n0={n0} nao caiu abaixo de si mesmo")
    return total, failures


def test_7_4_percent_claim():
    """Verifica a aritmetica da alegacao '7.4% restante' (Secao 3,
    ultimo paragrafo antes do titulo 'Thoughts along such lines...').

    IMPORTANTE (erro proprio corrigido antes de reportar): a primeira
    tentativa confundiu as classes da Figura 2 (que usa 3 mod16 E 11
    mod16 como par de classes irmas no refinamento de 3/16 mod16) com
    as classes da nota de rodape 4 (que exclui adicionalmente 11 mod32,
    nao 11 mod16 - um refinamento posterior e DIFERENTE, apos already
    ter restado 3/16). O texto principal (Secao 3) so vai ate "0 mod2,
    1 mod4, 3 mod16" (deixando 3/16), e SEPARADAMENTE a nota de rodape 4
    lista as exclusoes adicionais que levam a 7.4%: 11 e 23 mod32 (nao
    3 e 11 mod16 - essas ja estavam contabilizadas no 3/16 anterior),
    7,15,59 mod128, e 39,79,95,123,175,199,219 mod256.

    Calculo correto: partindo de 3/16 (restante apos excluir 0mod2,
    1mod4, 3mod16 - confirmado pelo proprio texto "leaving 3/16"),
    subtrai-se 11,23 mod32 (2/32 do TOTAL) + 7,15,59 mod128 (3/128) +
    7 classes mod256 (7/256)."""
    remaining_before_footnote4 = Fraction(3, 16)
    footnote4_excluded = Fraction(2, 32) + Fraction(3, 128) + Fraction(7, 256)
    remaining = remaining_before_footnote4 - footnote4_excluded
    remaining_pct = float(remaining) * 100
    print(f"  restante apos '0 mod2, 1 mod4, 3 mod16' (confirmado pelo texto): {remaining_before_footnote4} = {float(remaining_before_footnote4)*100:.2f}%")
    print(f"  excluido adicionalmente pela nota de rodape 4: {footnote4_excluded} = {float(footnote4_excluded)*100:.4f}%")
    print(f"  fracao restante final ('nao domada'): {remaining} = {remaining_pct:.4f}%")
    print(f"  paper afirma: 7.4%")
    return remaining_pct


def main():
    print("=== Formulas algebricas das notas de rodape (Secao 3) ===")
    failures = test_footnote_formulas()
    print(f"  (a) 2k par: {failures['a']} falhas em 199 valores de k")
    print(f"  (b) 4k+1: {failures['b']} falhas em 199 valores de k")
    print(f"  (c) 16k+3: {failures['c']} falhas em 199 valores de k")
    print()

    print("=== Classes 'domadas' da Figura 2 sempre dipam corretamente ===")
    total, failures = test_tame_classes_figure2()
    print(f"  {total} instancias testadas, {failures} falhas")
    print()

    print("=== Aritmetica da alegacao '7.4% restante' ===")
    pct = test_7_4_percent_claim()


if __name__ == "__main__":
    main()
