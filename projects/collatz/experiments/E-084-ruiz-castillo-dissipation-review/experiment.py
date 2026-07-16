#!/usr/bin/env python3
"""
E-084 - Verifica as identidades concretas de Ruiz Castillo, "Disipacion
Promedio de Ruiz Castillo y medidas de equilibrio en la dinamica
acelerada de la Conjetura de Collatz" (2026), item 035 da colecao -
OITAVO paper da mesma serie ja revisada (H-039, H-050, H-052 a H-056).

Mesmo padrao: reveste a identidade classica L_k(n)=k*log2(3)-A_k(n)
(deuda residual, ja conhecida deste projeto via H-001/H-011 e outros
papers desta serie) com um vocabulario formal novo - aqui, dinamica
simbolica/teoria ergodica (medidas invariantes sobre um espaco
simbolico, potencial dissipativo, teorema ergodico de Birkhoff). NAO
alega provar a conjectura (texto explicito: "El proposito de este
trabajo no es afirmar una demostracion definitiva").

Testa:
1. Proposicion 1.2 (Interpretacao multiplicativa): 2^{L_k(n)} = 3^k/2^{A_k(n)}.
2. Proposicion 2.4 (Semiconjugacao simbolica): pi(U(n)) = sigma(pi(n)),
   onde U e o mapa acelerado e sigma e o deslocamento simbolico.
3. Proposicion 3.2 (Classificacao local do potencial): phi(a)<0 sse
   a_0=1; phi(a)>0 sse a_0>=2; phi(a)=0 nunca ocorre (a_0 inteiro,
   log2(3) irracional).
4. Relacao entre a_j(n) e A_k(n): A_k(n) = soma dos primeiros k
   valores de valuacao 2-adica ao longo da orbita acelerada.

Reproduzir: python3 experiment.py
"""
import sys
import math


def v2(x):
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return v


def U(n):
    """Mapa acelerado: (3n+1)/2^v2(3n+1)."""
    x = 3 * n + 1
    while x % 2 == 0:
        x //= 2
    return x


def a_j_sequence(n, k_max):
    """Gera a_0(n),...,a_{k_max-1}(n), onde a_j(n)=v2(3*U^j(n)+1)."""
    seq = []
    x = n
    for _ in range(k_max):
        seq.append(v2(3 * x + 1))
        x = U(x)
    return seq


def A_k(n, k):
    """A_k(n) = soma dos primeiros k valores a_j(n), j=0..k-1."""
    return sum(a_j_sequence(n, k))


def L_k(n, k):
    """Deuda residual: L_k(n) = k*log2(3) - A_k(n)."""
    return k * math.log2(3) - A_k(n, k)


def test_proposicion_1_2(n_values=(3, 5, 7, 27, 97, 871), k_values=(1, 5, 10, 20)):
    """2^{L_k(n)} = 3^k / 2^{A_k(n)}."""
    failures = 0
    total = 0
    for n in n_values:
        if n % 2 == 0:
            continue
        for k in k_values:
            total += 1
            Lk = L_k(n, k)
            lhs = 2 ** Lk
            Ak = A_k(n, k)
            rhs = 3 ** k / 2 ** Ak
            if abs(lhs - rhs) / rhs > 1e-9:
                failures += 1
                print(f"  FALHA Prop 1.2: n={n} k={k} lhs={lhs} rhs={rhs}")
    return total, failures


def test_semiconjugacao(n_values=(3, 5, 7, 9, 11, 27, 97), k_max=15):
    """pi(U(n)) = sigma(pi(n)): a_j(U(n)) = a_{j+1}(n)."""
    failures = 0
    total = 0
    for n in n_values:
        if n % 2 == 0:
            continue
        Un = U(n)
        seq_n = a_j_sequence(n, k_max + 1)
        seq_Un = a_j_sequence(Un, k_max)
        for j in range(k_max):
            total += 1
            lhs = seq_Un[j]  # a_j(U(n))
            rhs = seq_n[j + 1]  # a_{j+1}(n)
            if lhs != rhs:
                failures += 1
                print(f"  FALHA Prop 2.4: n={n} j={j} a_j(U(n))={lhs} a_(j+1)(n)={rhs}")
    return total, failures


def test_classificacao_potencial(a0_values=range(1, 20)):
    """phi(a)=a_0-log2(3): <0 sse a_0=1; >0 sse a_0>=2; nunca =0."""
    log2_3 = math.log2(3)
    failures = 0
    for a0 in a0_values:
        phi = a0 - log2_3
        if a0 == 1:
            ok = phi < 0
        else:
            ok = phi > 0
        exactly_zero = (phi == 0)
        if not ok or exactly_zero:
            failures += 1
            print(f"  FALHA Prop 3.2: a0={a0} phi={phi}")
    return len(list(a0_values)), failures


def test_A_k_growth_is_plausible(n_values=(27, 97, 871, 6171), k_max=30):
    """Checagem de sanidade (nao uma identidade do paper): A_k(n) deve
    crescer aproximadamente como k*log2(3) em media, ja que cada a_j
    tem valor esperado ~2 (distribuicao geometrica) e o "orcamento"
    critico por passo e log2(3)~1.585 - consistente com L_k(n) ficando
    tipicamente positivo (dissipacao superavitaria em media), o que
    concorda com o mapa de Collatz ser conhecido como contrativo em
    media (H-001/H-011 deste projeto). NOTA: uma tentativa anterior de
    testar uma suposta identidade "3^k*n=U^k(n)*2^{A_k(n)}" estava
    ERRADA (nao e uma alegacao do paper, e minha propria suposicao
    incorreta - ignora os termos "+1" que se acumulam a cada passo, a
    relacao real e mais complexa que uma multiplicacao simples).
    Removida; substituida por esta checagem de sanidade mais modesta."""
    for n in n_values:
        Ak = A_k(n, k_max)
        expected_order = k_max * math.log2(3)
        Lk = k_max * math.log2(3) - Ak
        print(f"  n={n}: A_{k_max}(n)={Ak}  k*log2(3)={expected_order:.2f}  L_{k_max}(n)={Lk:.2f}")
    return True


def main():
    print("=== Proposicion 1.2 (Interpretacao multiplicativa da deuda residual) ===")
    total, fail = test_proposicion_1_2()
    print(f"  {total} casos, {fail} falhas")
    print()

    print("=== Proposicion 2.4 (Semiconjugacao simbolica pi(U(n))=sigma(pi(n))) ===")
    total, fail = test_semiconjugacao()
    print(f"  {total} casos, {fail} falhas")
    print()

    print("=== Proposicion 3.2 (Classificacao local do potencial dissipativo) ===")
    total, fail = test_classificacao_potencial()
    print(f"  {total} casos, {fail} falhas")
    print()

    print("=== Checagem de sanidade: crescimento de A_k(n) (nao e identidade do paper) ===")
    test_A_k_growth_is_plausible()


if __name__ == "__main__":
    main()
