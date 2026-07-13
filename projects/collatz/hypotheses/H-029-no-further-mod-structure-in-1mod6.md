# H-029 — Classe 1 mod 6 não tem sub-estrutura modular adicional (checagem rápida)

Status: refutada (checagem negativa rápida, não uma investigação profunda)
Criada em: 2026-07-13

## Contexto

Depois de H-028 (consolidação via CRT), sabemos que recordistas reais só
existem em {0, 1, 3} mod 6. A classe **1 mod 6** é a única puramente
ímpar dessas três, e a única para a qual não temos NENHUMA técnica de
exclusão (0 e 3 mod6 vêm de 0 mod3, sem exclusão também, mas são um caso
"duplo" par/ímpar; 1 mod6 é o resto de 1 mod3 depois de H-027 excluir a
metade par 4 mod6). Pergunta: será que 1 mod6 tem alguma sub-estrutura
(algum resíduo mod 12, 18, 24, etc. dentro dele) que também é excluída,
do mesmo jeito que H-027 excluiu metade de 1 mod3?

## Como foi testado

Contagem direta da distribuição dos 62 recordistas reais (OEIS A006877)
que caem em 1 mod6, sub-divididos por resíduo mod 12, 18, 24, 36 e 48.

## Resultado

| mod | distribuição |
|---|---|
| 12 | {1: 30, 7: 32} |
| 18 | {1: 35, 7: 27} |
| 24 | {1: 30, 7: 25, 19: 7} |
| 36 | {1: 19, 7: 16, 19: 16, 25: 11} |
| 48 | {1: 13, 7: 10, 25: 17, 31: 15, 43: 7} |

**Nenhum sub-resíduo está vazio** em nenhum desses módulos — todos têm
vários recordistas reais. Diferente do que aconteceu com 4 mod6 (H-027,
zero recordistas) ou 4 mod9 (H-008/H-022, zero recordistas), aqui não há
nenhum candidato óbvio a classe vazia nessa faixa de módulos pequenos.

## Interpretação

Checagem rápida e barata (não uma investigação exaustiva) — apenas
contagem, sem tentativa de prova. Consistente com a ideia de que 1 mod6 é
a classe "genérica" onde os recordistas realmente vivem (sem mecanismo de
exclusão conhecido), ao contrário de 2, 4, 5 mod6, que têm mecanismos
algébricos específicos (H-007, H-027) que as esvaziam. Não encontrei
motivo para insistir em módulos maiores sem uma ideia algébrica nova — a
ausência de classes vazias até mod 48 sugere que, se houver alguma
exclusão parcial adicional aqui, ela não é do tipo simples (mod pequeno)
que já exploramos.

## Atualizações

- 2026-07-13: checagem rápida feita, negativa. Não motiva investir mais
  tempo em módulos pequenos adicionais para esta classe especificamente.
