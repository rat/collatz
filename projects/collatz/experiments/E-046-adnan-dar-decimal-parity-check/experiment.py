"""
E-046 -- Verificacao do paper #002 (Adnan & Dar, "Behavior of a
Decimal-Parity-Based 3n+1 Mapping", Global Journal of Pure and Applied
Mathematics, 2026).

O paper NAO alega provar/refutar a Conjectura de Collatz original (nos
inteiros positivos) -- propoe uma "extensao" ad hoc: para um numero
decimal n em (0,1), define "paridade" olhando o ULTIMO DIGITO
SIGNIFICATIVO da representacao decimal (impar/par), e aplica a mesma
regra 3n+1 / n/2 (em aritmetica REAL, nao inteira) conforme essa
paridade. Conclui que a sequencia diverge para infinito para todo
n em (0,1).

Este experimento verifica:
1. A aritmetica dos exemplos do proprio paper (todos batem -- nao ha
   erro de calculo).
2. O problema conceitual central: a "paridade via ultimo digito
   significativo" so e definida para numeros com expansao decimal
   FINITA -- um subconjunto contavel (medida zero) de (0,1). A "Lei
   Matematica" que o paper afirma na conclusao ("para todo n em (0,1),
   o limite diverge") e universal sobre o CONTINUO, mas a regra que a
   sustenta nao esta nem definida fora desse subconjunto contavel.
3. Que a divergencia observada e uma consequencia trivial/esperada de
   nunca normalizar a constante "+1" em relacao a escala do dominio
   (0,1) -- nao e uma propriedade profunda ligada ao mecanismo real do
   Collatz (que depende de 3n+1 SEMPRE ser par para n inteiro impar,
   permitindo divisao por 2 -- fato que nao tem analogo com "ultimo
   digito" de um decimal).
"""

from fractions import Fraction


def last_significant_digit_parity(x_str):
    """x_str: string decimal finita, ex '0.01'. Retorna (ultimo_digito, paridade)."""
    if '.' not in x_str:
        raise ValueError("esperado decimal com ponto")
    frac_part = x_str.split('.')[1].rstrip('0')
    if frac_part == '':
        raise ValueError(f"{x_str}: sem digito significativo apos remover zeros a direita")
    last_digit = int(frac_part[-1])
    return last_digit, ("odd" if last_digit % 2 == 1 else "even")


def fraction_to_decimal_str(f, max_places=10):
    """Converte Fraction exata (denominador so com fatores 2,5) para string decimal."""
    sign = "-" if f < 0 else ""
    f = abs(f)
    scaled = f * (10 ** max_places)
    assert scaled.denominator == 1, f"{f} nao tem expansao decimal finita em {max_places} casas"
    digits = str(scaled.numerator).rjust(max_places + 1, "0")
    int_part, frac_part = digits[:-max_places], digits[-max_places:]
    return f"{sign}{int_part}.{frac_part}"


def step(x_str):
    """Um passo da regra do paper, usando aritmetica decimal exata (Fraction)."""
    last_digit, parity = last_significant_digit_parity(x_str)
    x = Fraction(x_str)
    if parity == "odd":
        result = 3 * x + 1
    else:
        result = x / 2
    return result, parity, last_digit


def verify_paper_examples():
    """Reproduz Table 1, Table 2, Example 1-3, e a tabela da Secao 6/7."""
    checks = []
    # Table 1 (pagina 3): classificacao de paridade
    table1 = [("0.01", "Odd"), ("0.02", "Even"), ("0.07", "Odd"),
              ("0.14", "Even"), ("0.33", "Odd")]
    for x_str, expected_parity in table1:
        _, parity, _ = step(x_str)
        checks.append((f"Table1 parity({x_str})", parity.capitalize(), expected_parity,
                        parity.capitalize() == expected_parity))

    # Exemplo pagina 4: 3(0.01)+1 = 1.03
    r, _, _ = step("0.01")
    checks.append(("3(0.01)+1", float(r), 1.03, float(r) == 1.03))

    # Delta e omega pagina 4-5
    delta = r - Fraction("0.01")
    checks.append(("Delta = 1.03-0.01", float(delta), 1.02, float(delta) == 1.02))
    omega = delta * 100
    checks.append(("omega = Delta*100", float(omega), 102, float(omega) == 102))

    # Example 2 pagina 5-6: n=0.33 -> 3(0.33)+1=1.99
    r2, _, _ = step("0.33")
    checks.append(("3(0.33)+1", float(r2), 1.99, float(r2) == 1.99))
    omega2 = (r2 - Fraction("0.33")) * 100
    checks.append(("omega para 0.33", float(omega2), 166, float(omega2) == 166))

    # Example 3 pagina 6: 0.02 (even) -> /2 = 0.01 -> (odd) -> 3n+1 = 1.03
    r3a, parity3a, _ = step("0.02")
    checks.append(("0.02/2", float(r3a), 0.01, float(r3a) == 0.01 and parity3a == "even"))
    r3b, parity3b, _ = step(fraction_to_decimal_str(r3a))
    checks.append(("depois 3(0.01)+1", float(r3b), 1.03, float(r3b) == 1.03))

    # Tabela Secao 6 (pagina 6): 1231.42 (even)->615.71->(odd)3n+1->1848.13->...
    expected_chain = [615.71, 1848.13, 5545.39, 16637.17, 49912.51]
    cur = "1231.42"
    results = []
    for _ in range(5):
        r, parity, digit = step(cur)
        results.append(round(float(r), 2))
        cur = fraction_to_decimal_str(r)
    checks.append(("cadeia 1231.42 (5 passos)", results, expected_chain,
                    results == expected_chain))

    return checks


def demonstrate_ill_definedness():
    """Mostra que a regra de 'paridade' do paper nao e definida para
    numeros em (0,1) sem expansao decimal finita -- ou seja, a 'Lei
    Matematica' universal da conclusao do paper (para todo n em (0,1))
    nao cobre quase nenhum numero real do intervalo (medida zero de
    excecoes contra medida total do continuo)."""
    examples = {
        "1/3 = 0.3333...": "nao tem ultimo digito -- expansao infinita nao-periodica-finita",
        "sqrt(2)/10 = 0.14142135...": "irracional, nao tem representacao decimal finita",
        "1/7 = 0.142857142857...": "decimal periodico infinito, nao tem 'ultimo digito'",
    }
    return examples


def demonstrate_trivial_mechanism():
    """Mostra que a divergencia e uma consequencia TRIVIAL de aplicar
    3n+1 (aritmetica real, nao inteira) a um n pequeno sem nenhuma
    normalizacao -- nao tem relacao com o mecanismo real do Collatz
    (que depende de 3n+1 ser SEMPRE par para n impar, permitindo a
    divisao por 2 subsequente ser tao 'forte' quanto necessario)."""
    # Para qualquer n pequeno em (0,1), 3n+1 aproxima 1 independente da
    # "paridade" do ultimo digito -- o proximo passo so volta a diminuir
    # se o resultado (proximo de 1, tipicamente >0.5) tiver ultimo
    # digito par, o que e tao provavel quanto arbitrario (nao ha
    # mecanismo estrutural, ao contrario do caso inteiro onde 3n+1 e
    # SEMPRE divisivel por 2 quando n e impar).
    import random
    random.seed(0)
    n_diverge = 0
    n_total = 200
    for _ in range(n_total):
        # gera decimal aleatorio com 2 casas em (0,1)
        d = random.randint(1, 99)
        x_str = f"0.{d:02d}"
        cur = x_str
        try:
            for _ in range(30):
                r, parity, digit = step(cur)
                if r > 10**6:
                    n_diverge += 1
                    break
                cur = fraction_to_decimal_str(r)
        except Exception:
            pass
    return n_diverge, n_total


if __name__ == "__main__":
    print("=" * 80)
    print("PARTE 1: aritmetica dos exemplos do proprio paper")
    print("=" * 80)
    checks = verify_paper_examples()
    all_ok = True
    for name, got, expected, ok in checks:
        print(f"{name}: obtido={got}, esperado={expected}, bate={ok}")
        all_ok = all_ok and ok
    print(f"\nTodos os exemplos do paper conferem: {all_ok}")
    print("(A aritmetica do paper esta correta -- nao ha erro de calculo.)")

    print()
    print("=" * 80)
    print("PARTE 2: a regra de 'paridade decimal' nao e definida na maioria de (0,1)")
    print("=" * 80)
    examples = demonstrate_ill_definedness()
    for num, reason in examples.items():
        print(f"  {num}: {reason}")
    print("\nA 'Lei Matematica' da conclusao do paper ('para todo n em (0,1), o limite")
    print("diverge') e uma afirmacao sobre o CONTINUO -- mas a regra de paridade so")
    print("se aplica a decimais com expansao FINITA, um subconjunto CONTAVEL (medida")
    print("zero) de (0,1). A afirmacao universal nao esta nem definida, quanto mais")
    print("provada, para quase todo numero real do intervalo alegado.")

    print()
    print("=" * 80)
    print("PARTE 3: a divergencia e um artefato trivial, nao um mecanismo profundo")
    print("=" * 80)
    n_diverge, n_total = demonstrate_trivial_mechanism()
    print(f"\n{n_diverge}/{n_total} decimais aleatorios em (0.01, 0.99) divergem (>10^6) em 30 passos.")
    print("""
Diferente do Collatz original -- onde 3n+1 e SEMPRE par para n impar
(garantindo que a divisao por 2 subsequente reduz de forma estrutural,
nao arbitraria) -- aqui a 'paridade' do resultado 3n+1 (um numero real
qualquer) depende do ultimo digito da sua representacao decimal, que
NAO tem nenhuma relacao algebrica com o valor 3n+1 em si. Nao ha
mecanismo estrutural analogo ao v2(3n+1) do Collatz real; a regra e
essencialmente arbitraria em relacao ao valor numerico, e a constante
'+1' nunca e normalizada em relacao a escala do dominio (0,1) -- o que
torna a divergencia esperada por construcao, nao uma descoberta.
""")

    print("=" * 80)
    print("VEREDITO")
    print("=" * 80)
    print("""
O paper nao alega provar/refutar a Conjectura de Collatz original (nos
inteiros positivos) -- e uma exploracao tangencial de uma extensao ad
hoc a decimais em (0,1). A aritmetica de todos os exemplos do proprio
paper confere (nao ha erro de calculo). O problema e conceitual, em
dois niveis:

1. A regra de "paridade via ultimo digito significativo" so e definida
   para decimais com expansao finita -- nao cobre quase nenhum numero
   real de (0,1) (contra-exemplos triviais: 1/3, 1/7, qualquer
   irracional). A "Lei Matematica" universal da conclusao nao e nem
   bem-definida no dominio que alega cobrir.

2. Mesmo restrita aos decimais finitos, a divergencia observada nao
   reflete nenhum mecanismo estrutural analogo ao Collatz real (onde
   3n+1 e sempre par para n impar por construcao algebrica) -- e um
   artefato de aplicar uma regra de "paridade" arbitraria (sem relacao
   algebrica com o valor numerico) a uma constante aditiva (+1) nunca
   normalizada em relacao ao dominio (0,1), o que torna a divergencia
   essencialmente garantida por construcao, nao uma propriedade nova ou
   informativa sobre a conjectura original.

Este e um tipo de problema diferente dos outros papers ja catalogados
como "alegacao de prova completa" (Santos, CTUHSK, Mohammed) -- aqui
nao ha uma tentativa seria de prova com um furo logico sutil; e uma
construcao ad hoc que nao se conecta de forma rigorosa ao problema
original.
""")
