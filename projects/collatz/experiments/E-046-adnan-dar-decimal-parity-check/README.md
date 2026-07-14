# E-046 — Verificação do paper #002 (Adnan & Dar, "Decimal-Parity-Based 3n+1 Mapping")

## Objetivo

Verificar "Behavior of a Decimal-Parity-Based 3n+1 Mapping" (J. Adnan,
S.A. Dar — Global Journal of Pure and Applied Mathematics, 2026). O
paper **não** alega provar/refutar a Conjectura de Collatz original —
propõe uma extensão ad hoc a decimais em (0,1) e conclui que ela
diverge.

## O que fizemos

1. Reproduzimos todos os exemplos numéricos do paper (Tables 1-2,
   Examples 1-3, a cadeia de 5 passos da Seção 6) com aritmética exata
   (`fractions.Fraction`) — todos batem.
2. Testamos se a regra de "paridade via último dígito significativo" é
   definida para números sem expansão decimal finita (1/3, 1/7, √2/10).
3. Testamos 200 decimais aleatórios em (0,1) sob a regra do paper.

## Resultado

**Aritmética do paper correta** — nenhum erro de cálculo nos exemplos.

**Problema conceitual em dois níveis**:
1. A regra de "paridade" só é definida para decimais com expansão
   finita — um subconjunto **contável** (medida zero) de (0,1). A "Lei
   Matemática" da conclusão do paper ("para todo n∈(0,1), o limite
   diverge") é uma afirmação sobre o contínuo, mas não está nem
   bem-definida para quase todo número real do domínio que alega
   cobrir (contra-exemplos triviais: 1/3, 1/7, qualquer irracional).
2. Mesmo restrita aos decimais finitos, a divergência é um artefato
   trivial (confirmado: 200/200 decimais aleatórios divergem em 30
   passos) — decorre de aplicar uma "paridade" sem relação algébrica
   com o valor numérico a uma constante aditiva (+1) nunca normalizada
   em relação à escala do domínio (0,1). Diferente do Collatz real,
   onde 3n+1 é sempre par para n ímpar por construção algébrica
   (garantindo divisão estrutural, não arbitrária), aqui não há
   mecanismo análogo — a divergência é esperada por construção, não
   uma descoberta.

Ver `hypotheses/H-046-adnan-dar-decimal-parity-review.md`.

## Como rodar

```
/home/rat/.venv/bin/python3 experiment.py
```
