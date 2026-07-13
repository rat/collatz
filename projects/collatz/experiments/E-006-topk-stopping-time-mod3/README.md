# E-006 — Tentativa de réplica com top-K por valor bruto (não recordistas estritos)

Hipótese relacionada: [`H-006-top-k-stopping-time-mod3.md`](../../hypotheses/H-006-top-k-stopping-time-mod3.md)

## O que foi testado

Tentamos aumentar o poder estatístico do achado mod-3 de H-004 usando os top-K
números por stopping time bruto (K=200, 1000) num intervalo grande (1M-30M),
em vez de exigir a definição estrita de "recordista" (bate todo m < n).

## Resultado

Nenhum viés mod-3 foi detectado no top-K bruto (distribuição ~uniforme,
32-35% em cada classe, p > 0.18 em todos os testes).

## Por que isso NÃO refuta H-004 (diagnóstico importante)

Investigando a discrepância, imprimimos os números reais do "top-50 por valor
bruto" e comparamos com a lista oficial de recordistas estritos (OEIS
A006877). São **populações diferentes**: só 5 dos 50 números do top-K bruto
são recordistas estritos de verdade (ex: 15733191, 14934241, 11200681,
8400511, 6649279); o resto são números que têm stopping time coincidentemente
alto mas que **nunca bateram um recorde** (um n menor já havia atingido valor
igual ou maior).

Isso significa que E-006 testou uma hipótese relacionada mas distinta de
H-004 — "números com stopping time alto em geral" em vez de "números que
batem um recorde novo". O viés mod-3 parece ser específico da segunda noção
(recordista estrito), não da primeira. Ver a análise corrigida e definitiva em
`experiments/E-004-true-record-holders/README.md` (usando a sequência oficial
completa de recordistas estritos, n=148), que confirma o achado com força
estatística esmagadora (p < 10^-13).

## Status de H-006

Não suportada como formulada (top-K bruto não reproduz o viés) — mas o
diagnóstico foi valioso: esclareceu que "recordista estrito" e "top-K bruto"
são populações genuinamente diferentes para esta pergunta, e ajudou a
identificar (indiretamente) o erro de transcrição corrigido em E-004.
