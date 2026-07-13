# E-032 — Frações contínuas de log₂(3) vs. anomalia de H-013

Hipótese relacionada: [`H-032-continued-fraction-h013-check.md`](../../hypotheses/H-032-continued-fraction-h013-check.md)

## O que foi testado

Se a qualidade da aproximação racional de log₂(3) (medida clássica via
convergentes de fração contínua, a ferramenta usada em limites de
comprimento de ciclo — Simons & de Weger) explica os pontos t onde a
anomalia de densidade de H-013/H-018 ocorre (t=4/5, 7/8 anomalia; 10/11,
13/14 inversão).

## Resultado

Sem correlação. Pares do mesmo tipo (duas anomalias, ou duas inversões)
mostram padrões opostos na distância de t·log₂(3) ao inteiro mais
próximo — se houvesse mecanismo real, deveriam concordar.

Reproduzir: `python3 experiment.py`.

## Status de H-032

**Refutada** — resultado negativo honesto de uma ideia bem motivada
(conexão real entre log₂(3) e o mecanismo de H-018, mas que não se
sustenta empiricamente nesta forma). Consistente com H-024: a obstrução
é 3-ádica (resíduos), não Arquimediana (proximidade numérica) — categorias
de precisão diferentes.
