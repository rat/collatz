"""
E-037 - Verificacao independente da Conjectura 10.4 de Pratiher (2026,
arXiv:1608.03600): distribuicao assintotica das "formas recorrentes" mod9.

Motivacao original: H-035 estabeleceu que Freq_r(N) (fracao de {1,...,N}
cuja orbita atinge, PELA PRIMEIRA VEZ, uma potencia de 2 com residuo r
mod9) e uma MEDIA DE CONJUNTO, categoricamente diferente de D(v) (densidade
por-no que sofre a obstrucao de precisao ilimitada de H-024). A pergunta:
sera que Freq_r(N) e derivavel/verificavel por metodos de equidistribuicao,
ao inves de sofrer a mesma obstrucao?

O que encontramos ao tentar verificar: um argumento de paridade (identico
ao mecanismo de H-012 - 3x+1=2^M so tem solucao inteira/impar quando M e
PAR) mostra que a PRIMEIRA potencia de 2 atingida por qualquer orbita (que
nao comeca ja sendo uma potencia de 2) DEVE ter expoente PAR. Isso
contradiz a alegacao central do paper (forma dominante = 'a', que por a
Tabela 4.3 dele corresponde a M=3 mod6 -- IMPAR).

Este script computa diretamente (definicao literal 2.2+9.1 do paper: M =
expoente da primeira/maior potencia de 2 na trajetoria; forma = M mod 6
via a Tabela 4.3 do proprio paper) e compara com a Tabela na Observacao
10.2 dele.
"""
import sys

FORM_TABLE = {0: 'd (9n+1)', 1: 'c (9n+2)', 2: 'b (9n+4)',
              3: 'a (9n+8)', 4: 'f (9n+7)', 5: 'e (9n+5)'}


def build_forms(N):
    """Para cada n em [1,N], calcula M = expoente da primeira/maior
    potencia de 2 atingida pela trajetoria de Collatz de n (definicao
    literal 2.2+9.1 de Pratiher). Memoiza por convergencia de trajetorias."""
    form_cache = {}

    def resolve(n):
        path = []
        cur = n
        while cur not in form_cache:
            if cur & (cur - 1) == 0:  # potencia de 2
                M = cur.bit_length() - 1
                form_cache[cur] = M
                break
            path.append(cur)
            cur = cur // 2 if cur % 2 == 0 else 3 * cur + 1
        else:
            M = form_cache[cur]
        for p in path:
            form_cache[p] = M
        return M

    counts = [0] * 6
    for n in range(1, N + 1):
        M = resolve(n)
        counts[M % 6] += 1
    return counts


def report(N, counts):
    print(f"N={N}")
    for i in range(6):
        print(f"  M mod6={i} [{FORM_TABLE[i]}]: count={counts[i]:>10d}  "
              f"freq={counts[i]/N:.7f}")
    even = counts[0] + counts[2] + counts[4]
    odd = counts[1] + counts[3] + counts[5]
    print(f"  soma expoentes PARES (d+b+f) = {even/N:.7f}")
    print(f"  soma expoentes IMPARES (c+a+e) = {odd/N:.7f}")
    print()


if __name__ == "__main__":
    Ns = [10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]
    if len(sys.argv) > 1:
        Ns = [int(sys.argv[1])]
    for N in Ns:
        counts = build_forms(N)
        report(N, counts)
        sys.stdout.flush()
