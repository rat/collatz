# H-008 — Classe 4 mod 9 nunca aparece em recordistas: tentativa de generalizar H-007

Status: RESOLVIDA COMPLETAMENTE — metade ímpar (N≡13 mod18) provada em
H-022 (técnica nova); metade par (N≡4 mod18) fechada em H-027 (corolário
direto de H-007 via N≡4 mod6, mais amplo que mod9)
Criada em: 2026-07-13

## Contexto

H-004 mostrou que, entre os 148 recordistas oficiais, a classe residual 4 mod 9
(que é ≡1 mod 3, portanto **não** excluída pela prova de H-007) nunca ocorre
(0 de 148). H-007 provou uma exclusão limpa para ≡2 mod 3 via um M=(2N-1)/3
construído algebricamente. Esta hipótese tentou generalizar essa técnica para
explicar a ausência da classe 4 mod 9.

## O que foi tentado

Para uma amostra de N ≡ 4 (mod 9) até 300, busquei computacionalmente o menor
M < N com total_stopping_time(M) ≥ total_stopping_time(N) (o que provaria que
N não pode ser recordista, do mesmo jeito que em H-007). Resultado: **não há
relação algébrica curta e fixa entre M e N** — o M encontrado varia sem
padrão claro (razão M/N de 0.02 a 0.87 na amostra), e frequentemente é só um
recordista "genérico" já forte (como 27, que domina 13 dos 33 N testados só
por já ter stopping time alto) em vez de um M construído especificamente a
partir de N via uma fórmula curta como em H-007.

## Interpretação

Isso sugere que, se a exclusão da classe 4 mod 9 for de fato permanente (nunca
vai aparecer um recordista nessa classe, para nenhum N por maior que seja),
a prova precisaria de uma técnica mais sofisticada que a de H-007 — talvez
uma cadeia de mais de 2 passos, ou um argumento não-construtivo. Também é
possível que essa exclusão **não seja permanente** — apenas um fato empírico
válido até onde a sequência oficial foi calculada (~1.47×10^19), sem garantia
de continuar para sempre. Sem uma prova, não sabemos qual dos dois casos é
verdadeiro.

## Status

Deixado como questão em aberto — não encontrei prova nem contraexemplo.
Registrar para retomar se surgir uma ideia melhor, em vez de forçar uma
explicação sem sustentação.

## Atualizações

- 2026-07-13: investigado, sem conclusão. Marcado como aberto/inconclusivo.
- 2026-07-13: **avanço real em H-022** — abordagem genuinamente diferente
  (relação multiplicativa via 2 passos acelerados, não deslocamento aditivo
  como H-015/H-016). Provado: todo N=18j+13 (a metade ímpar de N≡4 mod9)
  tem M=16j+11<N com total_stopping_time(M)=total_stopping_time(N)+5 —
  exclusão rigorosa, verificada sem exceção em 100.000 casos, e confirmada
  como não-redundante com H-007/H-014 (75% dos casos não eram já cobertos).
  A metade **par** (N≡4 mod18) continua sem prova — passos acelerados só
  alcançam ímpares, então a mesma técnica não se aplica diretamente. Ver
  `hypotheses/H-022-mod9-multiplicative-exclusion.md`.
- 2026-07-13: **H-008 FECHADA POR COMPLETO.** A metade par não era, na
  verdade, estruturalmente difícil — um único passo de halving (N par →
  N/2) já cai direto em M≡2 mod3, ao qual H-007 se aplica imediatamente.
  Isso mostra que a condição correta é N≡4 mod6 (mais ampla que mod9/18;
  o caso mod18 é só o subcaso k=3j), e fecha a metade par como corolário
  de H-007 em uma linha de álgebra — não uma técnica nova. Verificado sem
  exceção em 500.000 casos. Ver
  `hypotheses/H-027-mod6-corollary-closes-h008-even-half.md`. Com H-022
  (metade ímpar, técnica genuinamente nova) + H-027 (metade par,
  corolário), a classe 4 mod9 está agora completamente excluída de
  recordistas, com prova.
