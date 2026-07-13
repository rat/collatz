# E-007 — Prova de por que recordistas evitam resíduo 2 mod 3

Hipótese relacionada: [`H-007-why-record-holders-avoid-2-mod-3.md`](../../hypotheses/H-007-why-record-holders-avoid-2-mod-3.md)

## O que foi verificado

O teorema de H-007: para todo N ≡ 2 (mod 3) com N > 2, M = (2N−1)/3 é um
inteiro ímpar menor que N cuja órbita passa por N exatamente 2 passos depois
(M → 2N → N), logo total_stopping_time(M) = total_stopping_time(N) + 2. Isso
prova algebricamente que N nunca pode ser recordista — M sempre o supera.

## Nota técnica — bug encontrado e corrigido durante a verificação

A primeira tentativa de verificação usou a função `total_steps_only` de
E-004/E-006, que **assume implicitamente que a entrada é sempre ímpar** (ela
sempre existiu nesse contexto porque todos os scans anteriores iteravam só
sobre números ímpares — `range(1, limit, 2)`). Ao testar o teorema
diretamente com valores de N pares (ex: N=8, 14, 20, 26), a função quebrou
silenciosamente (aplicou "3n+1" a um número par, produzindo uma órbita
completamente errada — ex: `total_steps_only(2)` retornou 17 em vez do
correto 1). **Isso não afeta nenhum resultado anterior** (E-001 a E-006 nunca
chamaram essas funções com entrada par), mas é uma armadilha real: uma função
"acelerada" que assume paridade da entrada silenciosamente dá resultado errado
se usada fora do contexto para o qual foi escrita. Corrigido usando uma
função `total_stopping_time` genérica (mapa padrão, sem assumir paridade) só
para esta verificação.

## Resultado

Verificado sem exceção para todo N ≡ 2 (mod 3) de 2 até 1.000.000
(333.332 casos, incluindo N par e ímpar) — diferença de stopping time
exatamente 2 em 100% dos casos, única exceção sendo o caso de borda previsto
(N=2, onde M colapsaria em 1).

Reproduzir: `python3 experiment.py 1000000`

## Conclusão

**H-004 está agora completamente explicada, não só confirmada
estatisticamente.** Não é uma correlação misteriosa — é uma consequência
algébrica direta e simples da estrutura do mapa de Collatz. Fecha o principal
achado em aberto do projeto até agora.

## Status de H-007

**Confirmada** — prova algébrica curta + verificação computacional exaustiva
sem exceção (fora do caso de borda previsto).
