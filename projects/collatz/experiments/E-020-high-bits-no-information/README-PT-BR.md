# E-020 — Controle: bits altos carregam pouca (não zero) informação

Hipótese relacionada: [`H-020-high-bits-no-information.md`](../../hypotheses/H-020-high-bits-no-information.md)

## O que foi testado

Comparação de F-estatística (estilo ANOVA, variância entre grupos / dentro
de grupos) para total_stopping_time agrupado por: (a) 8 bits mais baixos de
n, (b) 8 bits mais altos (logo abaixo do bit líder), (c) rótulo aleatório
(controle de ruído puro), todos com n de comprimento fixo (50 bits),
200.000 amostras.

## Resultado

| agrupamento | F |
|---|---|
| bits baixos | **50.70** |
| bits altos | 1.80 |
| controle aleatório (ruído puro) | 0.94 |
| bits altos, após remover tendência K·log₂n (H-010) | 1.40 |

## Interpretação honesta

Bits baixos carregam informação real e forte (F=50.7, esperado — Terras/
H-002). Bits altos têm F muito menor (1.80) mas **não exatamente igual ao
ruído puro** (0.94) — não é uma confirmação limpa de "zero informação".

Parte do excesso é explicada pela tendência já conhecida (H-010: stopping
time médio cresce com log₂n, e dentro de um intervalo de comprimento fixo,
os bits altos correlacionam com a posição exata de n no intervalo, logo com
log₂n). Removendo essa tendência, F cai de 1.80 para 1.40 — ainda acima do
controle (0.94), mas mais perto. O resíduo provavelmente vem de H-011 (a
**variância** também depende de log₂n, não só a média) — um agrupamento por
bits altos corresponde a faixas estreitas de log₂n com variâncias
ligeiramente diferentes, o que viola a suposição de variância homogênea do
teste F e infla seu valor mesmo sem informação nova genuína.

Reproduzir: `python3 experiment.py 50 200000`.

## Conclusão

Bits altos carregam **muito menos** informação que bits baixos (fator de
~25-36×), consistente com a expectativa geral. Mas não confirmamos
exatamente "zero informação" — o pequeno excesso observado é plausivelmente
explicado por efeitos já conhecidos (H-010/H-011), não por uma descoberta
nova. Registrado com essa ressalva em vez de superclaimar um resultado mais
limpo do que os dados sustentam.

## Status de H-020

**Parcialmente confirmada** — assimetria forte confirmada, mas "zero
informação" nos bits altos não foi estabelecido com precisão total.
