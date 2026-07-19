# E-015 — Busca sistemática de coalescências mod 2^d

Hipótese relacionada: [`H-015-systematic-coalescence-search.md`](../../hypotheses/H-015-systematic-coalescence-search.md)

## O que foi testado

Generalização direta da técnica de H-014: para cada classe residual
N≡r₁ (mod 2^d), buscar M=N−k (mesmo "K" livre, k pequeno) cuja órbita
simbólica colide exatamente com a de N, excluindo N como recordista. Busca
para d=2 até 16, k=1 até 40, com deduplicação (uma classe só conta como
"nova" se não for refinamento de uma exclusão de módulo menor já
encontrada).

## Resultado — quantitativo

**2.374 classes residuais genuinamente novas encontradas** (além de H-014).
Fração cumulativa de resíduos excluídos por módulo:

| d (mod 2^d) | excluídos | fração |
|---|---|---|
| 3 | 1/8 | 12.5% |
| 6 | 26/64 | 40.6% |
| 9 | 276/512 | 53.9% |
| 12 | 2532/4096 | 61.8% |
| 16 | 45430/65536 | **69.3%** |

A fração cresce rapidamente e continua subindo com d maior (busca não
exaustiva — parou em d=16 por escopo de tempo, não por limite teórico).

## Verificação crítica (armadilha encontrada e resolvida)

Primeira tentativa de verificar os achados contra órbitas reais em K=0
**falhou** para todos os casos testados — investigando, descobri que é um
efeito de borda: para K muito pequeno, o valor real N=2^d·K+r é pequeno
demais e a trajetória "colapsa" (atinge 1 ou um valor pequeno) antes do
prefixo simbólico assumido se completar. Testando com K≥10, **todos os casos
verificados bateram exatamente** (diferença de stopping time = previsto,
sem exceção).

Isso tem um paralelo direto com N=2 em H-007 (onde o M dominante colapsa em 1
— o mesmo tipo de exceção de número pequeno).

## Verificação contra os 148 recordistas oficiais

6 recordistas "violam" alguma classe excluída: **3, 6, 7, 9, 18, 25** — todos
entre os primeiros 8 recordistas da lista oficial (números muito pequenos).
Nenhum recordista maior (a partir de 27) viola qualquer exclusão encontrada.
Isso é exatamente o efeito de borda esperado — a técnica é válida para N
suficientemente grande dentro de cada classe; os recordistas pequenos são
exceções conhecidas, análogas ao N=2 de H-007.

## Limitação importante (por construção, não por falta de esforço)

Esta busca é restrita a módulo 2^d. Como 2^d e 9 são coprimos, **nenhuma
restrição mod 2^d pode dizer algo sobre o resíduo mod 9** (via teorema chinês
do resto) — logo esta técnica **não pode, por construção, resolver H-008**
(a ausência da classe 4 mod 9). Isso não é uma falha da busca, é uma
limitação estrutural clara, documentada para não perder tempo tentando essa
mesma técnica para H-008 no futuro — precisaria de uma técnica mod-3^b
separada (ex: uma generalização de H-005 para mod 9).

Reproduzir: `python3 experiment.py 16 40` (~6s).

## Status de H-015

**Confirmada como técnica geral e válida** (com a ressalva de N grande o
suficiente). Não resolve H-008. Resultado quantitativo (69% dos resíduos mod
2^16 excluídos) é, por si só, um achado interessante sobre quão "raro"
estruturalmente é sobreviver como candidato a recordista.
