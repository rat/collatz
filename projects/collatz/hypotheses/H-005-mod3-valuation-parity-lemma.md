# H-005 — Resíduo mod 3 de termos da órbita é determinado pela paridade da valuação

Status: confirmada (prova algébrica + verificação computacional sem exceções)
Criada em: 2026-07-13

## Enunciado (um lema, não uma hipótese estatística)

Para qualquer n ímpar (qualquer resíduo mod 3), seja T(n) = (3n+1)/2^{a(n)} o passo
acelerado. Então:

**T(n) mod 3 é determinado inteiramente pela paridade de a(n), independente do
resíduo de n mod 3**: T(n) ≡ 1 mod 3 se a(n) é par, T(n) ≡ 2 mod 3 se a(n) é ímpar.
T(n) nunca é ≡ 0 mod 3.

### Por que isso é verdade (prova curta)

3n+1 ≡ 1 mod 3 sempre (já que 3n ≡ 0 mod 3, para qualquer n). Dividir por 2 mod 3
equivale a multiplicar pelo inverso de 2 mod 3, que é o próprio 2 (2×2=4≡1). Como
2 ≡ -1 mod 3, dividir por 2 alterna o resíduo entre 1 e 2 a cada divisão. Depois
de a(n) divisões a partir do resíduo 1, o resultado é 1×(-1)^{a(n)} mod 3 — ou
seja, 1 se a(n) par, 2 (≡ -1) se a(n) ímpar. Como consequência: **um valor
divisível por 3 nunca reaparece depois do primeiro passo ímpar aplicado** — uma
vez que a órbita "sai" da classe divisível por 3, nunca mais volta (dividir por 2
preserva "ser múltiplo de 3", e o passo 3n+1 nunca produz um múltiplo de 3).

## Previsão testável derivada

Combinando este lema com o fato já estabelecido (marginal de a(n) é geométrica
1/2, ver `literature/overview-and-known-results.md` e H-001): P(a par) = 1/3,
P(a ímpar) = 2/3 (soma de uma progressão geométrica). Logo, para qualquer termo
de uma órbita que não seja o número inicial (i.e., já passou por pelo menos um
passo), a proporção esperada de resíduos mod 3 é **1:2 entre classe 1 e classe 2
(não 1:1), e nunca classe 0** — uma previsão numérica precisa, diferente da
uniformidade ingênua.

## Relação com H-002 e H-004

- Em H-002/H-004 testamos resíduo mod 3 do **número inicial** de cada órbita
  (outlier ou recordista) — esse número não tem "passo anterior", então o lema
  não se aplica diretamente a ele. O achado de H-004 (recordistas raramente ≡2
  mod 3) continua sendo uma questão empírica em aberto, não explicada por este
  lema.
- O lema, no entanto, explica por completo o comportamento de QUALQUER termo
  subsequente dentro de uma órbita — é uma peça de estrutura real, exata (não
  estatística), que ainda não havíamos formalizado.

## Como testar

1. Verificar a identidade algébrica computacionalmente (deve valer 100% das
   vezes, sem exceção — é uma prova, não uma hipótese estatística).
2. Verificar a proporção 1:2 prevista entre resíduos 1 e 2 mod 3 em termos
   subsequentes de órbitas reais.

## Atualizações

- 2026-07-13: hipótese/lema aberto.
- 2026-07-13: verificado em `experiments/E-005-mod3-valuation-parity/`. (a)
  Identidade algébrica confirmada sem nenhuma exceção em 777.748 passos
  verificados. (b) Proporção prevista 1:2 entre resíduos 1 e 2 mod 3 em termos
  subsequentes confirmada com excelente precisão (33.47% vs 33.33% previsto,
  razão 0.5032 vs 0.5 previsto). Lema confirmado — primeira peça de estrutura
  exata (não estatística) do projeto. Não explica o achado de H-004 (resíduo
  mod 3 do número inicial de recordistas), que continua em aberto.
