#!/usr/bin/env python3
"""
E-074 - Verifica a construcao central de Ballesteros, Pena & Renza,
"A Novel Image Encryption Scheme Based on Collatz Conjecture" (Entropy
20(901), 2018), item 104 da colecao.

NAO e sobre a conjectura em si - e um esquema de criptografia de imagem
que usa "codigos de Collatz" (codificacao de comprimento variavel
derivada da orbita de Collatz de cada valor de pixel) como primitiva.
A alegacao critica testada aqui (Secao 3.1, ponto 4): "every code
begins with the header '11' because this sequence is not viable with
the proposed iteration process. Therefore, if a number is odd, the
following number is always even, and the code corresponding to the
sequence odd-odd (i.e., '11') thus does not exist."

Isso e a base de TODO o esquema de decodificacao (Secao 3.2): o receptor
separa o fluxo de bits contiguo de volta em codigos individuais
procurando o cabecalho "11". Se a subsequencia "11" pudesse aparecer
DENTRO de um codigo (nao so como cabecalho), a decodificacao seria
ambigua e o esquema quebraria.

Reproduzir: python3 experiment.py
"""
import sys


def collatz_code_body(x):
    """Gera o corpo do 'codigo de Collatz' para x (SEM o cabecalho '11'),
    seguindo exatamente a descricao textual da Secao 3.1 / Figura 3:
    - a cada iteracao, se o dado atual e par, divide por 2 e poe bit 0
      (posicao MSB, i.e., cada novo bit vai ANTES dos bits ja postos -
      Figura 3 mostra o bit da iteracao 1 como LSB e o da ultima
      iteracao como MSB);
    - se e impar, aplica 3x+1 e poe bit 1;
    - repete ate o valor virar 1 (o proprio 1 nao gera mais bit, e o
      ultimo bit posto e sempre 0, ja que a iteracao final necessariamente
      divide um numero par ate chegar em 1).
    Retorna a string de bits do corpo (MSB primeiro, como no exemplo do
    paper: '1100000101' pros x=3, corpo seria '00000101' -- vamos conferir
    exatamente contra o exemplo do proprio paper abaixo)."""
    bits = []  # vamos construir do LSB para o MSB, depois inverter
    n = x
    if n == 1:
        return "0"  # x=1: "its corresponding code is 0" (texto da Secao 3.1)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            bits.append("0")
        else:
            n = 3 * n + 1
            bits.append("1")
    # bit de terminacao: "the value of 1 is reached. Its corresponding
    # code is 0" - um bit extra "0" alem das transicoes, correspondente
    # a iteracao final da Figura 3 (iteracao 8, input=1, bit=0 MSB)
    bits.append("0")
    # bits[0] e o LSB (primeira iteracao), bits[-1] e o MSB (ultima iteracao/terminacao)
    return "".join(reversed(bits))


def collatz_code(x):
    """Codigo completo: cabecalho '11' + corpo."""
    return "11" + collatz_code_body(x)


def test_worked_example():
    """Confere contra o exemplo explicito do paper (Figura 3, x=3):
    'Collatz code for the number 3 => 1100000101, length = 10'."""
    code = collatz_code(3)
    expected = "1100000101"
    print(f"  x=3: obtido={code}  esperado={expected}  {'OK' if code == expected else 'FALHA'}")
    return code == expected


def test_header_uniqueness(x_max=256):
    """Alegacao critica: a subsequencia '11' NUNCA aparece dentro do
    CORPO do codigo (ou seja, so aparece como o cabecalho artificial
    prefixado) - testado para x de 1 a 256 (o range de pixels+1 usado
    pelo proprio esquema, Secao 3.1 ponto 2: pixels 0-255 viram 1-256)."""
    failures = 0
    for x in range(1, x_max + 1):
        body = collatz_code_body(x)
        if "11" in body:
            failures += 1
            idx = body.index("11")
            print(f"  FALHA: x={x}, corpo='{body}' contem '11' na posicao {idx}")
    return x_max, failures


def test_unique_decodability(x_max=256):
    """Verifica que os 256 codigos completos (com cabecalho) sao
    todos distintos entre si - necessario para a decodificacao (Secao
    3.2) encontrar exatamente 1 match na estrutura embaralhada."""
    codes = [collatz_code(x) for x in range(1, x_max + 1)]
    unique = set(codes)
    return len(codes), len(unique)


def dp_decode_count(stream, valid_codes, max_len):
    """Programacao dinamica: quantas particoes DISTINTAS do stream em
    codigos validos existem, cobrindo o stream inteiro exatamente.
    ways[i] = numero de formas de particionar stream[0:i] usando so
    codigos do conjunto valid_codes. Testa decodificabilidade UNICA de
    forma correta - uma primeira tentativa ingenua (escanear a proxima
    ocorrencia de '11' como delimitador) deu falso negativo por usar um
    limite de comprimento (max_len) baixo demais, ainda por cima sendo
    conceitualmente fragil: um '11' pode aparecer 'a cavalo' de dois
    codigos (fim de um + inicio do cabecalho do proximo) sem que isso
    seja ambiguidade real, e a DP resolve isso corretamente por
    construcao."""
    n = len(stream)
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(n):
        if ways[i] == 0:
            continue
        for l in range(2, max_len + 1):
            if i + l > n:
                break
            if stream[i:i + l] in valid_codes:
                ways[i + l] += ways[i]
    return ways[n]


def test_stream_parseability(x_max=256, n_concat=1000, seed=1):
    """Testa a alegacao real do esquema: concatenando MUITOS codigos
    (com cabecalho) em sequencia (Figura 4, 'bs'), o fluxo resultante
    tem EXATAMENTE UMA decomposicao valida no conjunto dos 256 codigos
    possiveis - decodificabilidade unica, verificada via DP correta."""
    import random
    rng = random.Random(seed)
    pixels = [rng.randrange(1, x_max + 1) for _ in range(n_concat)]
    codes_by_x = {x: collatz_code(x) for x in range(1, x_max + 1)}
    valid_codes = set(codes_by_x.values())
    max_len = max(len(c) for c in valid_codes)
    codes = [codes_by_x[p] for p in pixels]
    stream = "".join(codes)
    ways = dp_decode_count(stream, valid_codes, max_len)
    return ways == 1, f"{len(codes)} codigos concatenados ({len(stream)} bits), {ways} particao(oes) valida(s) encontrada(s)"


def main():
    print("=== Exemplo do proprio paper (x=3) ===")
    ok = test_worked_example()
    print()

    print("=== Corpo do codigo nunca contem '11' (x=1..256) ===")
    total, failures = test_header_uniqueness()
    print(f"  {total} valores testados, {failures} falhas")
    print()

    print("=== Unicidade dos 256 codigos completos ===")
    total, unique = test_unique_decodability()
    print(f"  {total} codigos gerados, {unique} distintos {'OK' if total==unique else 'FALHA - HA COLISAO'}")
    print()

    print("=== Reparticionamento de um fluxo concatenado (1000 pixels aleatorios) ===")
    ok, msg = test_stream_parseability()
    print(f"  {'OK' if ok else 'FALHA'}: {msg}")


if __name__ == "__main__":
    main()
