"""
E-043 -- Verificacao da "prova" CTUHSK (paper #016 da colecao, Halemane,
"Collatz-Thwaites-Ulam-Hasse-Syracuse-Kakutani (CTUHSK) Theorem").

O paper alega provar a Conjectura de Collatz. A "prova" tem duas partes:
  (a) condicao necessaria: H^s (componente conectada ao ciclo trivial) e
      order-isomorfica a N via os axiomas de Dedekind-Peano -- isso e
      tautologico (H^s e DEFINIDO como quem alcanca o ciclo trivial).
  (b) condicao suficiente: nao existem ciclos extras (H^infinito) nem
      cadeias divergentes (H^&) -- isto e, H^s = H. Essa e a parte que
      carregaria o peso de uma prova real.

Este experimento ataca (b). O argumento do paper (Secao 10.2.1, pag.22-23)
e um reductio-ad-absurdum: assume um ciclo hipotetico X_theta, toma seu
elemento minimo do tipo (6m-1), e afirma que o predecessor desse elemento
DEVE ser o dado pela formula com v=1 (Eqn.8), obtendo um numero MENOR,
contradizendo a minimalidade.

O problema: a formula do paper para predecessores de um numero tipo (6m-1)
tem infinitas solucoes validas, uma para cada expoente impar v=1,3,5,7,...
-- nao apenas v=1. O paper nunca justifica por que o predecessor DENTRO DO
CICLO HIPOTETICO teria que ser exatamente o de v=1 (o menor de todos). Se
o predecessor real no ciclo corresponder a qualquer v>=3, o resultado e
MAIOR que o elemento original -- e a "contradicao de minimalidade" some.

Este script demonstra isso concretamente.
"""

from fractions import Fraction


def v2(m):
    v = 0
    while m % 2 == 0:
        m //= 2
        v += 1
    return v


def syracuse(n):
    """Um passo do mapa acelerado de Collatz (D#(U#(.)) do paper): 3n+1
    seguido de divisao por 2 ate ficar impar."""
    assert n % 2 == 1, f"syracuse espera entrada impar, recebeu {n}"
    m = 3 * n + 1
    while m % 2 == 0:
        m //= 2
    return m


def collatz_odd_trajectory(n, max_steps=2000):
    traj = [n]
    for _ in range(max_steps):
        if traj[-1] == 1:
            return traj, True
        traj.append(syracuse(traj[-1]))
    return traj, False


def mod6_type(n):
    assert n % 2 == 1
    r = n % 6
    if r == 1:
        return "6m-5 (tipo A, 1 mod 3)"
    if r == 5:
        return "6m-1 (tipo B, 2 mod 3)"
    if r == 3:
        return "6m-3 (tipo C, 0 mod 3, multiplo de 3)"
    raise ValueError(f"residuo mod6 inesperado para impar: {r}")


# ---------------------------------------------------------------------
# Parte 1: confirmar os fatos estruturais basicos do paper (corretos)
# ---------------------------------------------------------------------

def check_no_predecessor_for_multiples_of_3(bound=3000):
    """Eqn.9 do paper: BEL(6m-3) nao tem NENHUM predecessor.
    Verificacao por forca bruta: para todo multiplo impar de 3 abaixo de
    `bound`, procura algum m impar menor que produza esse valor via
    syracuse(m)."""
    failures = []
    for n in range(3, bound, 6):  # n = 3, 9, 15, 21, ... (impares mult. de 3)
        for m in range(1, 20 * n, 2):
            if syracuse(m) == n:
                failures.append((n, m))
                break
    return failures  # esperado: lista vazia


def check_predecessor_formula_typeB(n_values, v_max=9):
    """Confirma que, para n do tipo (6m-1), o candidato a predecessor
    dado por [(n * 2^v - 1) / 3] e valido (inteiro) para TODO v impar, e
    que syracuse(candidato) == n de fato (a formula do paper esta certa)."""
    rows = []
    for n in n_values:
        assert mod6_type(n).startswith("6m-1")
        for v in range(1, v_max + 1, 2):
            num = n * (2 ** v) - 1
            assert num % 3 == 0, f"formula deveria SEMPRE dar inteiro para v impar (n={n}, v={v})"
            pred = num // 3
            real = syracuse(pred)
            rows.append((n, v, pred, real, real == n, pred < n))
    return rows


# ---------------------------------------------------------------------
# Parte 2: o achado central -- demonstrar o furo logico da Secao 10.2.1
# ---------------------------------------------------------------------

def demonstrate_flaw_on_paper_example():
    """Reproduz o exemplo EXATO do paper: k=2, BEL(6k-1)=BEL(11).
    O paper afirma (aplicando Eqn.8 com v=1) que o predecessor de 11 "e"
    7, e como 7<11, isso contradiria a minimalidade de 11 num ciclo
    hipotetico. Mostramos que 7 e apenas UMA de infinitas escolhas."""
    n = 11
    print(f"Exemplo do proprio paper: BEL(6k-1) com k=2 -> n={n} ({mod6_type(n)})")
    print(f"Confirma: syracuse(7) = {syracuse(7)} (paper afirma que 7 e predecessor de 11 via v=1)")
    print()
    print(f"{'v (impar)':>10} | {'predecessor = (n*2^v - 1)/3':>30} | {'syracuse(pred)==n?':>20} | {'pred < n?':>10}")
    print("-" * 80)
    for v in range(1, 10, 2):
        pred = (n * 2 ** v - 1) // 3
        assert (n * 2 ** v - 1) % 3 == 0
        ok = syracuse(pred) == n
        smaller = pred < n
        print(f"{v:>10} | {pred:>30} | {str(ok):>20} | {str(smaller):>10}")
    print()
    print("Conclusao: TODOS os v impares dao um predecessor valido e real de 11.")
    print("Apenas v=1 (pred=7) e MENOR que 11. Todo v>=3 da um predecessor MAIOR.")
    print("O paper so testa/exclui o ramo v=1. Nao ha argumento excluindo que o")
    print("predecessor REAL dentro de um ciclo hipotetico corresponda a v=3,5,7,...")
    print("-- casos em que NENHUMA contradicao de minimalidade surgiria.")


def general_algebraic_argument(n_samples):
    """Generaliza o exemplo numerico: para QUALQUER n do tipo (6m-1),
    pred(v=1) = (2n-1)/3 < n sempre (pois 2n-1 < 3n para n>0), e
    pred(v=3) = (8n-1)/3 > n sempre (pois 8n-1 > 3n para n>0). Ou seja,
    o padrao "v=1 da o unico predecessor menor" NAO e uma coincidencia
    do exemplo n=11 -- e um fato algebrico geral. O furo do paper e,
    portanto, estrutural: nao um erro pontual de aritmetica."""
    results = []
    for n in n_samples:
        pred_v1 = Fraction(2 * n - 1, 3)
        pred_v3 = Fraction(8 * n - 1, 3)
        results.append((n, pred_v1, pred_v1 < n, pred_v3, pred_v3 > n))
    return results


def check_h_and_divergent_chain_argument():
    """Secao 10.2.2 (paginas 23-24): o paper usa 'exatamente o mesmo
    argumento reductio-ad-absurdum banking on [Eqn.17]' para o caso de
    cadeias divergentes H^&, com k=1 dando BEL(3) e BEL(5). Mesma falha:
    k=1 e escolhido por satisfazer as congruencias mod3, nao por ser o
    valor real definido pela cadeia hipotetica."""
    n = 5  # BEL(6k-1) com k=1
    print(f"Secao 10.2.2 (H^&): mesmo padrao. n={n} ({mod6_type(n)})")
    for v in range(1, 8, 2):
        pred = (n * 2 ** v - 1) // 3
        print(f"  v={v}: predecessor = {pred}, syracuse(pred)={syracuse(pred)}, "
              f"pred<n? {pred < n}")
    print("  Mesma conclusao: so v=1 (pred=3) e menor que 5. Furo identico ao de 10.2.1.")


def verify_papers_own_worked_example():
    """O proprio paper (pag. 29-30) exibe a trajetoria de 9 como
    9->7->11->17->13->5->1. Confirma que essa trajetoria (e portanto que
    7 e 11 pertencem trivialmente a H^s / convergem ao ciclo trivial) e
    exatamente o que o paper usa como "contradicao" na Secao 10.2.1 --
    ou seja, o proprio contra-exemplo do paper usa numeros que o paper
    reconhece pertencerem a trajetoria padrao, nao a nenhum ciclo
    hipotetico."""
    traj, converged = collatz_odd_trajectory(9)
    return traj, converged


if __name__ == "__main__":
    print("=" * 80)
    print("PARTE 1: fatos estruturais basicos do paper (esperado: todos corretos)")
    print("=" * 80)

    failures = check_no_predecessor_for_multiples_of_3(3000)
    print(f"\n[Eqn.9] Multiplos impares de 3 sem predecessor (ate 3000): "
          f"{'CONFIRMADO -- nenhuma falha' if not failures else f'FALHOU: {failures}'}")

    rows = check_predecessor_formula_typeB([5, 11, 17, 23, 29], v_max=7)
    all_ok = all(r[4] for r in rows)
    print(f"[Eqn.8] Formula de predecessor tipo (6m-1) valida para todo v impar testado: "
          f"{'CONFIRMADO' if all_ok else 'FALHOU'}")

    traj, converged = verify_papers_own_worked_example()
    print(f"\nTrajetoria de 9 (exemplo do proprio paper, pag.29-30): {' -> '.join(map(str, traj))}")
    print(f"Converge ao 1: {converged} (bate com a afirmacao do paper)")

    print()
    print("=" * 80)
    print("PARTE 2: o furo logico central da Secao 10.2.1 (condicao suficiente)")
    print("=" * 80)
    print()
    demonstrate_flaw_on_paper_example()

    print()
    print("-" * 80)
    print("Generalizacao algebrica (nao e coincidencia do exemplo n=11):")
    print("-" * 80)
    samples = [5, 11, 17, 23, 29, 35, 41, 47, 101, 1001]
    gen = general_algebraic_argument(samples)
    print(f"{'n':>6} | {'pred(v=1)':>12} | {'pred(v=1)<n?':>14} | {'pred(v=3)':>12} | {'pred(v=3)>n?':>14}")
    for n, p1, lt, p3, gt in gen:
        print(f"{n:>6} | {str(p1):>12} | {str(lt):>14} | {str(p3):>12} | {str(gt):>14}")
    print("\nPara TODO n do tipo (6m-1) testado: pred(v=1) < n e pred(v=3) > n.")
    print("Isso e um fato algebrico geral (2n-1 < 3n < 8n-1 para todo n>0), nao um")
    print("acidente do exemplo escolhido pelo paper. O 'furo' e estrutural.")

    print()
    print("-" * 80)
    print("Secao 10.2.2 (cadeias divergentes H^&): mesmo padrao de erro")
    print("-" * 80)
    check_h_and_divergent_chain_argument()

    print()
    print("=" * 80)
    print("VEREDITO")
    print("=" * 80)
    print("""
A 'condicao necessaria' (Secao 10.1) e tautologica: H^s e definido como o
componente conectado ao no-sink BEL(1), entao 'todo elemento de H^s alcanca
BEL(1)' e verdade por definicao, nao por prova.

A 'condicao suficiente' (Secao 10.2), que teria que fazer o trabalho real
(mostrar H^s = H, isto e, excluir ciclos extras e cadeias divergentes) tem
um furo logico decisivo: em ambas as Secoes 10.2.1 e 10.2.2, o argumento
so testa o predecessor de v=1 (o menor de infinitos candidatos validos) e
declara vitoria quando esse ramo especifico da contradicao. Nenhum
argumento e apresentado para excluir que o predecessor REAL de um
elemento minimo de um ciclo/cadeia hipotetico corresponda a v=3,5,7,... --
ramos que dao predecessores MAIORES e portanto NAO violam a minimalidade
assumida. A "prova" nao fecha o caso geral; fecha apenas um caso
particular (e arbitrariamente escolhido) dele.

Isso e o mesmo padrao de erro encontrado em outras "provas" da colecao
(cf. Santos 2018, `literature/unverified-proof-claims.md`): uma afirmacao
existencial ("existe um predecessor com tal propriedade") e usada como se
fosse uma afirmacao universal sobre o objeto hipotetico especifico em
questao.
""")
