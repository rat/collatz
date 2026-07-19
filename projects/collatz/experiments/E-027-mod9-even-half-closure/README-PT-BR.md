# E-027 — Corolário de H-007 que fecha a metade par de H-008

Hipótese relacionada: [`H-027-mod6-corollary-closes-h008-even-half.md`](../../hypotheses/H-027-mod6-corollary-closes-h008-even-half.md)

Origem: tentativa de fechar a metade par de H-008 (N≡4 mod18), deixada
pendente desde H-022 com o registro (impreciso, ver abaixo) de que estaria
bloqueada por depender de passos acelerados.

## O que foi testado

Se N par com N/2 ≡ 2 (mod 3) — o que, após um único passo de halving,
cai direto na classe já excluída por H-007 — fornece uma exclusão válida
para N.

## Correção durante o desenvolvimento

A primeira versão do script parametrizava por j (N=18j+4, mirando
especificamente mod9/mod18) e testava só 300k casos DESSA subclasse. Ao
revisar a prova antes de reportar (consulta ao advisor), ficou claro que
a derivação nunca usa mod9 — a condição real é só N≡4 mod6, uma classe
3× mais ampla. Reescrito para testar a classe geral N=6k+4 (k=1..500.000).

## Resultado

Zero exceções em 500.000 casos. Confirma: para todo N≡4 mod6, P=2k+1<N
tem total_stopping_time(P) = total_stopping_time(N)+1. N nunca pode ser
recordista.

Reproduzir: `python3 experiment.py 500000`

## Avaliação honesta

Isto fecha H-008 completamente (a metade par é o subcaso k=3j deste fato
mais geral), mas **não é um resultado novo independente** — é um
corolário de uma linha de álgebra sobre H-007. A metade par de H-008
nunca foi estruturalmente difícil; só parecia bloqueada porque H-022 a
enquadrou em termos de passos acelerados (que de fato não alcançam N
par diretamente), quando um único halving simples já resolve.

## Status de H-027 / H-008

**H-027 confirmada.** **H-008 agora RESOLVIDA POR COMPLETO**: H-022
(metade ímpar, técnica nova) + H-027 (metade par, corolário) juntas
excluem toda a classe 4 mod9 de recordistas, com prova.
