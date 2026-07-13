# H-021 — Erosão de runs de 1s terminais

Status: confirmada (mecanismo de erosão); parte (b) suportada com ressalva de tautologia
Criada em: 2026-07-13
Origem: ideia do brainstorm do modelo Fable ("H-G").

## Enunciado

Se n termina em binário com um run de t≥2 uns consecutivos (seguido de um
zero, ou n=2^k−1), o passo acelerado tem valuação a=1 (subida) e o run
terminal do resultado encolhe exatamente para t−1. Isso se repete run
após run até o run chegar a 1, quando o comportamento muda (valuação
maior, "redução forte").

**Nota de risco tautológico** (já sinalizado pelo próprio Fable): isso é
quase uma reformulação mecânica da definição de valuação — não esperamos
que seja uma "descoberta", só uma verificação de mecanismo.

## Como testar

Verificar a regra de erosão exaustivamente para muitos n com runs
terminais de diferentes tamanhos. Secundariamente, comparar a distribuição
de comprimentos de runs (não-terminais) entre órbitas de recordistas e
órbitas típicas de mesmo comprimento (com o cuidado de colisão de órbitas
já documentado em `protocols/new-experiment.md`).

## Atualizações

- 2026-07-13: hipótese aberta.
- 2026-07-13: testada em `experiments/E-021-terminal-run-erosion/`. Regra
  de erosão confirmada sem exceção (50k testes, t=2..20). Recordistas
  mostram runs de a=1 mais longos (média 2.512) que órbitas típicas (2.035,
  bate com previsão teórica de H-001, E[run]=2). Diferença real, mas
  registrada como parcialmente tautológica (records quase por definição
  exigem subidas mais longas) — não uma descoberta nova.
