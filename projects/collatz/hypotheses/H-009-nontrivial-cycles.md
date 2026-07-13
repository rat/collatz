# H-009 — Busca por ciclos não-triviais em inteiros positivos

Status: consistente com a literatura (nenhum ciclo novo até a=14; Simons & de Weger já provaram até a=68)
Criada em: 2026-07-13

## Enunciado

Pergunta do diretor científico: para inteiros negativos existem 3 ciclos
conhecidos no mapa de Collatz estendido. Existe um ciclo análogo (diferente do
trivial 1→4→2→1) para inteiros positivos?

Já é conhecido (ver `literature/nontrivial-cycles.md`) que não existe ciclo
não-trivial com até 68 "subidas" (Simons & de Weger, 2005) nem com menos de
~2.18×10^11 elementos totais (limite de 2025). Não vamos superar esses
resultados — o objetivo é **verificar isso nós mesmos**, de forma
independente e reproduzível, para uma faixa menor, usando a equação de ciclo
diretamente.

## Equação de ciclo

Um ciclo com "a" passos ímpares (acelerados) e valuações b_1,...,b_a (cada
≥1, soma S) satisfaz:

n_0 = [Σ_{i=0}^{a-1} 3^(a-1-i) · 2^(S_i)] / (2^S − 3^a)

onde S_0=0, S_i = b_1+...+b_i. Para n_0 ser um ciclo válido, precisa ser um
inteiro positivo, e a órbita a partir de n_0 precisa reproduzir exatamente a
sequência b_1,...,b_a (autoconsistência).

## Como testar

Para cada número de subidas "a" (de 1 até um limite tratável), enumerar
composições de S (próximo ao ótimo a·log₂3) em "a" partes positivas, calcular
n_0, checar se é inteiro positivo, e se for, verificar autoconsistência
rodando a órbita real. Esperado: só a=1, S=2 (b_1=2) produz n_0=1 — o ciclo
trivial. Nenhum outro deveria aparecer.

## Atualizações

- 2026-07-13: hipótese aberta.
- 2026-07-13: testada em `experiments/E-009-nontrivial-cycle-search/` via
  busca por força bruta na equação de ciclo, para a=1 até 14. Único resultado:
  o ciclo trivial (n0=1) percorrido múltiplas vezes — nenhum ciclo
  genuinamente novo. Consistente com Steiner (1977, sem ciclo de 1),
  Simons (2005, sem ciclo de 2) e Simons & de Weger (2005, sem ciclo até
  a=68 — resultado muito mais forte que o nosso, usando frações contínuas em
  vez de força bruta). Não é uma descoberta nova, é uma verificação própria
  e independente de um resultado já estabelecido.
- 2026-07-13: **estendida em H-034/E-034** (motivada por um vídeo que
  redescobriu esta mesma técnica informalmente). Com janela de S mais
  estreita (S=S_min exatamente), verificação limpa até a=16. Além disso,
  a combinatória de composições explode (bilhões por par a=20+),
  quantificando precisamente por que força bruta pura não alcança o a=68
  de Simons & de Weger sem as técnicas de fração contínua deles.
