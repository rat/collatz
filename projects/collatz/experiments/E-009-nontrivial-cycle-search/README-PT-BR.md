# E-009 — Busca por ciclos não-triviais (força bruta, escala pequena)

Hipótese relacionada: [`H-009-nontrivial-cycles.md`](../../hypotheses/H-009-nontrivial-cycles.md)

## O que foi testado

Pergunta do diretor científico: assim como inteiros negativos têm 3 ciclos
conhecidos no mapa de Collatz estendido, existe um ciclo não-trivial análogo
para inteiros positivos? Buscamos diretamente via a equação de ciclo (ver
`hypotheses/H-009-nontrivial-cycles.md`), para número de subidas "a" de 1 até
14, enumerando composições de S (soma das valuações) por força bruta.

## Resultado

Nenhum ciclo genuinamente novo encontrado para a de 1 a 14 (dentro da janela
de busca coberta — algumas combinações (a,S) com contagem de composições
acima de 3 milhões foram puladas por custo computacional, ver saída do
script). Os únicos "ciclos" encontrados foram o ciclo trivial (n0=1)
percorrido "a" vezes seguidas (b=(2,2,...,2)) — não são ciclos novos, são o
mesmo ciclo 1→4→2→1 repetido.

Reproduzir: `python3 experiment.py 14 3000000` (~57s).

## Limitações honestas desta busca

- É força bruta simples, não usa as técnicas de fração contínua que Simons &
  de Weger (2005) usaram para provar rigorosamente que não há ciclo
  não-trivial com até **68** subidas — um resultado muito mais forte que o
  nosso.
- Algumas combinações (a,S) com muitas composições possíveis foram puladas
  (ver `skipped` na saída) — a busca não é 100% exaustiva para a maiores
  dentro da janela testada, embora cubra as combinações mais prováveis
  (S mais próximo do ótimo a·log₂3, que são as de menor contagem de
  composições e mais prováveis de gerar um n0 pequeno).
- Isso é uma **verificação própria, independente**, de um resultado já bem
  estabelecido — não é uma descoberta nova. O valor é ter feito a checagem
  nós mesmos, de forma reproduzível, e entender o mecanismo (equação de
  ciclo via frações contínuas de log₂3) em vez de só citar a literatura.

## Status de H-009

Consistente com a literatura (Steiner 1977, Simons 2005, Simons & de Weger
2005): nenhum ciclo não-trivial encontrado na faixa testada. Não refuta nem
prova a conjectura — apenas replica, em escala menor, um resultado já
estabelecido rigorosamente por outros.
