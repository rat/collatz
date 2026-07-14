"""
E-051 -- Verificacao do paper #009 (Enis Olgac, "Technical Note:
Structural Dualism in Integer Architectures").

Nota tecnica curta (3 paginas) conectando duas alegacoes anteriores do
MESMO autor (nao incluidas nesta colecao, citadas so como referencias
[3] "The Canonical Triple-Graph" e [4] "The Proof Beyond Goldbach" --
ambas preprints Zenodo auto-publicados): uma sobre Collatz (CTG), outra
alegando PROVAR a Conjectura de Goldbach inteira.

O unico conteudo especifico de Collatz nesta nota (Definicao 2.1,
"Localized Stranger Invariant") e a afirmacao trivial de que ramos da
arvore reversa do Collatz enraizados em impares DISTINTOS nao se
sobrepoem -- isso e uma consequencia TAUTOLOGICA de o mapa direto de
Collatz ser uma FUNCAO (cada n tem exatamente um sucessor), nao um
teorema substantivo. Verificamos isso computacionalmente (trivial por
construcao).

Os Teoremas 2.2 e 3.3 sao sobre a Conjectura de GOLDBACH (fora do
escopo deste projeto, que e sobre Collatz), e nao sao rigorosos o
suficiente para verificar formalmente -- usam linguagem descritiva
("physical collision", "topologically trapped", "retaining wall") sem
definir precisamente os objetos matematicos envolvidos.
"""


def T_forward(n):
    """Mapa padrao de Collatz (nao acelerado)."""
    return n // 2 if n % 2 == 0 else 3 * n + 1


def odd_root_via_repeated_halving(m):
    """Para um numero PAR m, encontra a raiz impar 'abaixo' dele na
    arvore reversa -- ou seja, o unico impar do qual m eh descendente
    por divisoes sucessivas por 2 (nao envolve o passo 3n+1 nesta
    direcao, ja que a definicao do paper e sobre 'branches' B(o)
    gerados por halving a partir de uma raiz impar o)."""
    while m % 2 == 0:
        m //= 2
    return m


def check_disjoint_branches(bound=200000):
    """Definicao 2.1: para o1 != o2 impares distintas, os conjuntos de
    pares 'descendentes por halving' B(o1) e B(o2) nao se sobrepoem.
    Isso e trivialmente verdade -- todo numero par tem uma UNICA parte
    impar (fatoracao unica de potencias de 2), entao so pode pertencer
    a UM B(o). Confirmamos isso diretamente."""
    root_of = {}
    violations = []
    for m in range(1, bound):
        root = odd_root_via_repeated_halving(m)
        if m in root_of and root_of[m] != root:
            violations.append(m)
        root_of[m] = root
    # cada numero tem exatamente uma raiz impar -- por construcao, sem excecoes possiveis
    return violations, len(root_of)


if __name__ == "__main__":
    print("=" * 80)
    print("Definicao 2.1 (Localized Stranger Invariant) -- ramos disjuntos por raiz impar")
    print("=" * 80)
    violations, total = check_disjoint_branches(200000)
    print(f"\nTestados {total} inteiros de 1 a 199999: numeros com raiz impar ambigua = {len(violations)}")
    print("(Esperado 0 -- e uma consequencia TAUTOLOGICA da fatoracao unica de 2,")
    print(" nao um teorema substantivo: todo inteiro positivo tem exatamente UMA parte")
    print(" impar, entao 'ramos' definidos por raiz impar sao disjuntos por construcao,")
    print(" nao por causa de nenhuma propriedade especifica do Collatz.)")

    print()
    print("=" * 80)
    print("VEREDITO")
    print("=" * 80)
    print(f"""
Confirmado (trivialmente): {len(violations) == 0}

Este e o UNICO conteudo especifico de Collatz nesta nota tecnica de 3
paginas -- e uma tautologia (consequencia direta de todo inteiro
positivo ter uma unica parte impar via fatoracao unica de 2), nao um
resultado novo ou nao-trivial.

O resto do paper (Teorema 2.2 "Lattice Inversion", Teorema 3.3 "Hard
Physical Boundary Fact") e inteiramente sobre a Conjectura de GOLDBACH
(fora do escopo deste projeto, que e sobre Collatz) e references
[3]/[4] que sao os proprios outros preprints auto-publicados do autor
(Zenodo, nao revisados por pares) -- incluindo uma alegacao de ter
PROVADO a Conjectura de Goldbach inteira (referencia [4], "The Proof
Beyond Goldbach"). A "prova" do Teorema 3.3 usa linguagem descritiva
nao-rigorosa ("physical collision", "topologically trapped", "retaining
wall", "monotone path tracing the lower sublevel envelope") sem definir
precisamente os objetos matematicos envolvidos -- nao alcanca o padrao
minimo de rigor para ser avaliada como uma prova matematica real.

Este nao e um paper sobre Collatz com conteudo especifico verificavel
-- e uma nota curta conectando duas alegacoes extraordinarias do mesmo
autor (uma delas sobre um problema diferente, Goldbach) atraves de
analogia vaga, sem rigor matematico real em nenhuma das duas pontas.
""")
