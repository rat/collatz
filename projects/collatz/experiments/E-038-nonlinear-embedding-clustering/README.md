# E-038 — Busca de estrutura não-linear (MI) além de H-025

Hipótese relacionada: [`H-038-nonlinear-mi-embedding-search.md`](../../hypotheses/H-038-nonlinear-mi-embedding-search.md)

## O que foi testado

Generalização honesta de "Project PHI" (ideia de IA externa, embedding
rico + busca de estrutura): existe dependência **não-linear** (mutual
information, não correlação tipo Pearson) entre features ricas de n
(peso de Hamming, resíduos mod5/7/9/11, janelas de bits) e de
m=(3n+1)/2^a, condicionando em a fixo, além do que H-025 (correlação
linear bit-a-bit) já testou e refutou?

## Arquivos

- `experiment.py`: busca principal — MI entre 7 features de n × 6
  features de m (incluindo a segunda valuação a2), condicionado em
  a∈{1,...,6}, comparado contra null de embaralhamento (15 shuffles).
- `control_check.py`: verificação do mecanismo — (1) confirma
  `popcount(m)==popcount(3n+1)` exatamente; (2) compara a MI real do
  Collatz contra transformações sintéticas de controle (5n+1, 7n+3,
  9n+5, e a família 2^k+1 para k=1..6).

## Resultado

Encontrada dependência real e muito robusta (z-score até ~2448) entre
peso de Hamming de n e de m, e entre janelas de bits e a segunda
valuação a2 — algo que H-025 (só bit-a-bit) não teria capturado.

**Mas o experimento de controle mostra que isso é genérico, não
específico do Collatz**: substituindo 3n+1 por 5n+1, 7n+3 ou 9n+5
(nada a ver com Collatz), a MESMA classe de dependência aparece (MI
não-nula, muito acima do null). Mecanismo: `popcount(m)` é sempre
exatamente `popcount(3n+1)` (dividir por 2^a só remove zeros à
direita), e a dependência entre `popcount(n)` e `popcount(3n+1)` é uma
propriedade clássica de propagação de carry em multiplicação por ímpar
+ soma — a mesma classe de mecanismo que H-025 já identificou, só vista
de outro ângulo (estatística agregada em vez de pares de bits).

## Reproduzir

```
python3 experiment.py [N_AMOSTRAS]     # busca principal (~20s para N=400000)
python3 control_check.py               # verificação de mecanismo (~3s)
```

## Status de H-038

**Refutada como estrutura nova** — achado real, mas mecanismo
identificado e confirmado como genérico de aritmética binária, não
específico de Collatz. Estende H-025 (método diferente, mesma
conclusão de fundo), não o contradiz.
