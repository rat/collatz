# E-059 — Verificação do paper #021 (Amirian & Amirian, "3x+4y+1")

Hipótese relacionada: [`H-059-amirian-3x4y1-review.md`](../../hypotheses/H-059-amirian-3x4y1-review.md)

## Paper

Amirian, R. & Amirian, A. (2026). *A Generalization of 3x+1 Problem to
3x+4y+1*. SSRN 6993335, 3 páginas, não revisado por pares. PDF local:
`literature/papers/021_Generalization-3x1-to-3x4y1.pdf`.

## O que foi testado

Propõe `x_{i+1}=3x_i+4y+1` (ímpar) / `x_i/2-y` (par), alegando que toda
órbita atinge `1-2y`. Sem provas, só exemplos + varredura numérica
("~640 bilhões de pontos"). Testamos:

1. Reprodução exata dos 4 exemplos numéricos do paper.
2. Verificação computacional da identidade `z=x+2y` ⟺ Collatz padrão.
3. Quantificação da redundância na varredura de "~640 bilhões".
4. Teste amostral (500 casos aleatórios) da alegação geral.

## Resultado

Exemplos e alegação geral corretos — mas **não porque seja uma
generalização real**: a mudança de variável `z=x+2y` transforma o mapa
proposto exatamente no Collatz padrão (mesma fórmula, símbolo a
símbolo), com o domínio `x_0≥1-2y` sendo exatamente `z_0≥1`. Não é uma
família de problemas, é o mesmo problema reparametrizado. Consequência
quantificada: os "~640 bilhões de pontos de dados" testados cobrem, na
melhor das hipóteses, ~2,4 milhões de instâncias distintas do Collatz
padrão (não 640 bilhões independentes) — já coberto por verificações
diretas publicadas na literatura (`2^68`–`2^71`).

## Como reproduzir

```
python3 experiment.py
```

Sem dependências além da stdlib. Roda em <0,1s.
