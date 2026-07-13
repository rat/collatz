# H-020 — Bits altos de n não carregam informação sobre stopping time

Status: parcialmente confirmada (assimetria forte, mas "zero informação" não exata)
Criada em: 2026-07-13
Origem: ideia do brainstorm do modelo Fable ("H-F") — controle metodológico.

## Enunciado

Fixado o comprimento em bits de n, os bits **baixos** (via teorema de
Terras/H-002) determinam os primeiros passos e correlacionam com o
stopping time. Os bits **altos** (próximos ao bit líder) não deveriam
carregar nenhuma informação sobre o stopping time — servem só de baseline
metodológico para futuras análises de padrão binário (evita a armadilha
tautológica de H-002).

## Como testar

Amostrar n aleatórios de comprimento fixo (ex: 50 bits). Agrupar por (a) os
8 bits mais baixos, (b) os 8 bits mais altos (logo abaixo do bit líder,
que é sempre 1). Comparar a variância das médias de total_stopping_time
entre grupos nos dois casos — esperado: variação real (não-trivial) para
(a), variação desprezível (compatível com ruído) para (b).

## Atualizações

- 2026-07-13: hipótese aberta.
- 2026-07-13: testada em `experiments/E-020-high-bits-no-information/`.
  F-estatística: bits baixos=50.7 (forte, esperado), bits altos=1.80,
  controle aleatório=0.94. Bits altos NÃO batem exatamente com o controle
  de ruído puro. Removendo a tendência K·log₂n de H-010, F cai para 1.40 —
  ainda acima do controle, provavelmente por H-011 (variância também
  depende de log₂n, violando homogeneidade assumida pelo teste F).
  Assimetria forte confirmada (~25-36× menos informação nos bits altos),
  mas "zero informação exata" não estabelecida — registrado com essa
  ressalva honesta.
