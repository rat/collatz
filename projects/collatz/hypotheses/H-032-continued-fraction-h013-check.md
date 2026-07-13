# H-032 — Frações contínuas de log₂(3) não explicam a anomalia de H-013

Status: refutada (resultado negativo, teste honesto de uma ideia bem motivada)
Criada em: 2026-07-13
Origem: pergunta do diretor científico sobre se abordagens geométricas
(especificamente a conexão frações-contínuas/geometria hiperbólica via
a árvore de Stern-Brocot e o grupo modular PSL(2,Z), que é a ferramenta
clássica usada para limites de comprimento de ciclo — Simons & de Weger)
poderiam ajudar em alguma questão nossa ainda aberta.

## Motivação

A única questão genuinamente aberta que resta no projeto é a fórmula
fechada para a anomalia de H-013/H-018 (por que a razão de densidades
entre gerações adjacentes t/t+1 é não-monotônica, com "anomalias" em
t=4/5 e 7/8, e "inversões" em t=10/11 e 13/14). O mecanismo de H-018
(orçamento log₂(n_max/J_t) encolhendo 2 bits por t) tem log₂(3) como
constante aditiva — e log₂(3) é exatamente a constante cujos convergentes
de fração contínua são a ferramenta clássica para limites de ciclo.
Pergunta natural: será que os pontos t onde a anomalia ocorre são
explicados pela qualidade da aproximação racional de log₂(3) nesses t
(ligada aos convergentes)?

## Como foi testado

Calculada a fração contínua de log₂(3) com alta precisão (Decimal,
30 dígitos): [1,1,1,2,2,3,1,5,2,23,2,...], convergentes com denominadores
1,1,2,5,12,41,53,306,665,... Para cada par flagged em H-013/H-018
(4,5 — anomalia; 7,8 — anomalia; 10,11 — inversão; 13,14 — inversão),
medida a distância de t·log₂(3) ao inteiro mais próximo (medida clássica
de "boa aproximação").

## Resultado

| par | tipo | mais próximo de inteiro |
|---|---|---|
| (4,5) | anomalia | t=5 (segundo) |
| (7,8) | anomalia (mesmo tipo) | t=7 (**primeiro**) |
| (10,11) | inversão | t=10 (primeiro) |
| (13,14) | inversão (mesmo tipo) | t=14 (**segundo**) |

**Pares do mesmo tipo mostram padrões opostos** — (4,5) e (7,8) são
classificados como o mesmo tipo de anomalia, mas um tem o segundo membro
mais próximo de um inteiro e o outro tem o primeiro. O mesmo acontece com
os dois pares de inversão. Se a proximidade a um inteiro (a assinatura
clássica dos convergentes de fração contínua) fosse o mecanismo real, os
pares do mesmo tipo deveriam mostrar o mesmo padrão — não mostram.

## Conclusão

**Sem correlação.** Este é um resultado negativo honesto de uma ideia
genuinamente bem motivada (não óbvia de antemão) — a conexão entre H-013
e frações contínuas de log₂(3) não se sustenta nesta forma simples.

Isso é consistente com (não superado por) H-024: a densidade D(v) exige
precisão 3-ádica ilimitada, uma obstrução de natureza diferente da
aproximação racional real (Arquimediana) que as frações contínuas de
log₂(3) capturam. Frações contínuas respondem "quão perto 2^a chega de
3^b" (útil para limites de ciclo, onde a comparação é sobre magnitude
total); a anomalia de H-013 depende de estrutura 3-ádica fina (quais
resíduos módulo 3^k, não apenas quão perto numericamente) — categorias
de precisão diferentes, não a mesma pergunta em disfarces diferentes.

## Atualizações

- 2026-07-13: testado e refutado. Resultado negativo limpo, reportado
  com honestidade em vez de forçar um ajuste que não existe.
