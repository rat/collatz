# E-042 — Verificação do paper #014 (Williams, "A Coordinate System for Collatz Dynamics")

Hipótese relacionada: [`H-042-williams-coordinate-system-review.md`](../../hypotheses/H-042-williams-coordinate-system-review.md)

## O que foi testado

Paper de boa qualidade acadêmica (afiliação institucional real,
literatura extensa, declaração honesta de uso de IA, código público no
GitHub). Oito verificações no total (2 originais de 2026-07-14 + 6
adicionadas em 2026-07-15, ao perceber — tarde — que este item já
tinha sido revisado aqui):

- **Teorema 3.6** (dinâmica diagonal) — 20.000 casos aleatórios.
- **Teorema 4.1** (Zero-Prime Rows) — exaustivo k=6,10,...,300 (74
  linhas). Exceção k=2 confirmada. Controles fora do padrão têm primos.
- **Teorema 2.13** (partição bijetora Z≥0→crown triangles) — n=0..200.000.
- **Proposição 3.10** (transição de fronteira a=1) — 81 casos.
- **Teorema 4.2** (contagem de posições "prime-admissible") — k=2..300.
- **Proposição 6.2** (fórmula assintótica de contagem de cadeias).
- **Observação 6.3** (linhas "acidentalmente" sem primos) — listas exatas.
- **Referências OEIS** (Seção 5.2) — conferidas via `curl` em oeis.org.

## Resultado

**Todos os teoremas confirmados sem exceção.** Dois erros de citação
OEIS na Seção 5.2 (não afetam nenhuma prova): `A017557` citado para
"crowns≡8 mod12" é na verdade `12n+3` (≡3 mod12) — a sequência correta
é `A017617` (`12n+8`); e "primos em `L_1`=A005105" deveria ser "A005105
sem o elemento 2" (diferença de um único elemento).

## Nota de integridade — erro próprio corrigido antes de finalizar

Uma primeira tentativa de verificar a Proposição 6.2 apontou
(incorretamente) um "erro de fator 2", usando `T_c(k,0)` como elemento
mínimo da linha `k`. Isso estava **errado — bug na verificação, não no
paper**: o mínimo real está em `T_c(k,1)` (posição ímpar), confirmado
contra o próprio Exemplo 2.9 do paper. `advisor()` apontou a
inconsistência antes de qualquer conclusão errada ser escrita. Ver
`H-042.md` para a lição registrada sobre ordem de suspeita ao
investigar discrepâncias.

## Reproduzir

`python3 experiment.py` (~1,4s)

## Status

Revisão concluída — nenhum erro matemático encontrado (só dois erros
de citação OEIS, isolados, não afetam nenhuma prova). Ponto de
calibração importante para a crítica cumulativa (nem todo paper da
coleção tem problemas).
