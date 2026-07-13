# E-005 — Lema: resíduo mod 3 determinado pela paridade da valuação

Hipótese relacionada: [`H-005-mod3-valuation-parity-lemma.md`](../../hypotheses/H-005-mod3-valuation-parity-lemma.md)

## O que foi testado

Um lema algébrico (não estatístico): para T(n) = (3n+1)/2^{a(n)}, T(n) mod 3
depende só da paridade de a(n) — nunca do resíduo de n mod 3. Prova curta está
no arquivo da hipótese. Consequência: um valor divisível por 3 nunca reaparece
depois do primeiro passo ímpar da órbita.

Previsão derivada combinando este lema com a distribuição geométrica já
estabelecida de a(n) (H-001): entre termos subsequentes de qualquer órbita
(excluindo o número inicial), a proporção de resíduo 1 vs 2 mod 3 deveria ser
1:2 (não 1:1), e resíduo 0 nunca deveria aparecer.

## Resultado

- **(a) Verificação algébrica exata**: 0 violações em 777.748 passos verificados
  (20.000 órbitas, 40 passos cada) — confirma a identidade sem exceção, como
  esperado de uma demonstração (não é um resultado estatístico, é uma prova
  verificada computacionalmente).
- **(b) Proporção prevista**: residuo 1 mod 3 observado em 33.47% dos casos
  (previsto 33.33%), resíduo 2 mod 3 em 66.53% (previsto 66.67%), razão 1:2
  observada = 0.5032 (previsto exatamente 0.5). Excelente concordância.

Reproduzir: `python3 experiment.py 20000 40`

## Por que isso importa

É a primeira peça de estrutura **exata e provada** (não uma correlação
estatística) que encontramos no projeto — conecta diretamente o resultado de
H-001 (distribuição geométrica de a(n), independência) à estrutura aritmética
mod 3, dentro do framework "2-ádico/ergódico" da literatura
(`literature/approaches-2adic-ergodic.md`): a proporção 1:2 é essencialmente uma
afirmação de equidistribuição com respeito a uma medida não-uniforme induzida
pela dinâmica, exatamente o tipo de objeto que a teoria ergódica do mapa
2-ádico estuda.

## Relação com H-004 (importante, para não confundir)

Este lema explica o comportamento de termos **subsequentes** dentro de uma
órbita — não explica por que os **números iniciais** que são recordistas de
stopping time (H-004) evitam resíduo 2 mod 3. Essa continua sendo uma questão
em aberto. O lema aqui é uma peça de estrutura real e útil, mas não fecha o
achado de H-004.

## Status de H-005

**Confirmada** (prova algébrica + verificação computacional sem exceções).
