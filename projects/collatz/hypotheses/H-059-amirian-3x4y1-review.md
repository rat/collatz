# H-059 — Revisão do paper #021 (Amirian & Amirian, "3x+4y+1") — não é uma generalização, é o próprio Collatz via mudança de variável

Status: revisão externa concluída — exemplos numéricos corretos;
achado central: a "generalização" proposta é algebricamente idêntica
ao Collatz padrão (mudança de variável afim, não um problema novo)
Criada em: 2026-07-15
Origem: item 021 da coleção (`literature/papers/INDEX.md`), já baixado
(`021_Generalization-3x1-to-3x4y1.pdf`).

## O paper

Amirian, R. & Amirian, A. (2026), *A Generalization of 3x+1 Problem to
3x+4y+1*, SSRN 6993335, 3 páginas, preprint não revisado por pares.
Propõe o mapa

```
x_{i+1} = 3x_i + 4y + 1   se x_i ímpar
x_{i+1} = x_i/2 - y       se x_i par
```

para `x_0 ≥ 1-2y`, `y` inteiro qualquer (positivo, negativo ou zero —
reduz ao Collatz padrão em `y=0`), alegando que toda órbita atinge o
mínimo `1-2y` e cicla por `{1-2y, 4-2y, 2-2y}`. Sem nenhuma prova —
só 4 exemplos numéricos manuais e uma varredura empírica descrita como
"~640 bilhões de pontos de dados" (`x_0,y ∈ [-400.000, 400.000]`). O
abstract conclui: *"We believe this generalization opens the door to
solving the Generalized Collatz Conjecture, and thus, Collatz
Conjecture."*

## O que foi verificado

`experiments/E-059-amirian-3x4y1-check/experiment.py`, quatro partes:

1. Reprodução exata dos 4 exemplos numéricos do paper. 0 falhas.
2. Verificação computacional (2000 casos aleatórios) da identidade
   algébrica central (ver abaixo). 0 falhas.
3. Quantificação da redundância na varredura "~640 bilhões".
4. Teste amostral (500 pares aleatórios) da alegação geral. 0 falhas.

## Achado central — não é uma generalização

Fazendo a mudança de variável `z = x + 2y` (deslocamento afim
constante, não uma transformação nova): como `2y` é sempre par, `z`
tem exatamente a mesma paridade que `x`. Substituindo:

- Se `x` ímpar: `x_{i+1} = 3x_i+4y+1` ⟹ `z_{i+1} = x_{i+1}+2y =
  3x_i+6y+1 = 3(x_i+2y)+1 = 3z_i+1`.
- Se `x` par: `x_{i+1} = x_i/2-y` ⟹ `z_{i+1} = x_{i+1}+2y = x_i/2+y =
  (x_i+2y)/2 = z_i/2`.

Ou seja, `z_i = x_i+2y` satisfaz **exatamente** a recorrência de
Collatz padrão (`3z+1` se ímpar, `z/2` se par) — não uma versão
modificada, a mesma fórmula, símbolo a símbolo. E a condição de domínio
do paper, `x_0 ≥ 1-2y`, é **exatamente** `z_0 = x_0+2y ≥ 1`, o domínio
padrão dos inteiros positivos de Collatz. O ciclo terminal alegado
`{1-2y, 4-2y, 2-2y}` é exatamente `{1,4,2}` traduzido de volta por
`x=z-2y`.

**Conclusão**: o "GCC" (Generalized Collatz Conjecture) não é uma
família de "infinitas variações" do problema de Collatz, como o
abstract afirma — é **literalmente o mesmo problema**, disfarçado por
uma troca de variável afim trivial. Verificar GCC para um par `(x_0,y)`
qualquer é *exatamente* verificar Collatz padrão para `z_0=x_0+2y`, nem
mais nem menos. Isso não é um erro de cálculo (os 4 exemplos e a
varredura numérica estão corretos, dado que decorrem necessariamente
da equivalência) — é uma leitura equivocada do que foi de fato
demonstrado.

## Quantificando o overclaim da varredura numérica

O retângulo testado (`x_0,y ∈ [-400.000,400.000]`) dá exatamente
`800.001² = 640.001.600.001` pares — bate com o "~640 bilhões"
alegado. Mas, pela equivalência acima, `z_0=x_0+2y` é a **única**
quantidade relevante, e ela varia em `[-1.200.000, 1.200.000]` — no
máximo **2.400.001 valores distintos**. Ou seja, os "640 bilhões de
pontos de dados" contêm redundância massiva (~266 mil repetições em
média por valor de `z_0`) e cobrem, na melhor das hipóteses, ~2,4
milhões de instâncias distintas do Collatz padrão — um subconjunto
**muito menor** do que já está coberto por verificações diretas e
exaustivas publicadas na literatura (que já passam de `2^68`–`2^71`,
ordens de magnitude além de 1.200.000). A varredura não constitui
evidência numérica nova para Collatz além do que já é conhecido.

## Por que isso importa (e por que não é "só uma crítica pedante")

A alegação do abstract — "isso abre a porta para resolver a
Generalized Collatz Conjecture, e portanto, a Conjectura de Collatz" —
não se sustenta: não existe nenhum problema "generalizado" aqui além
do próprio Collatz, e nenhuma técnica nova é introduzida que ajude a
atacá-lo. A "generalização" é uma reparametrização, não uma extensão
do espaço do problema (diferente, por exemplo, de generalizações reais
como `3x+d` para `d` ímpar coprimo com 3, ou mudar a base de 2/3 para
outros primos, que de fato mudam a estrutura do problema).

## Novas hipóteses?

Nenhuma. Nota de padrão para a síntese futura: este é o segundo caso
nesta coleção (depois de itens já vistos com "generalizações" triviais)
de um paper apresentar uma reparametrização como se fosse uma extensão
substantiva — vale considerar como uma categoria própria de
"pseudo-generalização" ao escrever a síntese final do levantamento.

## Atualizações

- 2026-07-15: paper lido por completo (3 páginas), equivalência
  algébrica com Collatz padrão derivada e verificada computacionalmente
  em duas frentes independentes (identidade direta + reprodução dos
  exemplos). `INDEX.md` atualizado (item 021: Lido=Sim, Corrigido=Sim,
  Implementado=Sim).
