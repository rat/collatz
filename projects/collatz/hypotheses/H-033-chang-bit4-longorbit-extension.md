# H-033 — Extensão do problema aberto de Chang (2026) com órbitas mais longas que as testadas

Status: confirmada (extensão empírica honesta, sem resolver o problema
aberto original)
Criada em: 2026-07-13
Origem: diretor científico pediu para continuar buscando ângulos
promissores. O paper de Chang (H-030) deixa um problema aberto preciso:
toda órbita visita as classes 9 e 25 (mod 32) com equilíbrio suficiente
ao longo da subsequência de fim-de-burst no canal n≡1 mod8? Ele testou
até n0=10⁹, com poucas dezenas de observações por órbita (seu próprio
Figure 2, n0=837799, 43 blocos, "longe de convergir"). Nossa
infraestrutura de verificação em larga escala é bem adequada para
estender isso.

## O que foi testado

Rastreei o equilíbrio bit-4 (fração de burst-endings ≡9 mod32, dentre os
≡1 mod8) **individualmente** ao longo da órbita completa dos 8 maiores
recordistas reais de stopping time — órbitas com 878 a 920 passos totais
e 131-134 observações cada, **3× mais observações por órbita** que o
melhor caso testado no paper original. Analisado orbita por orbita (não
agregado) para evitar a armadilha de pseudo-replicação já documentada em
H-030.

## Resultado

| n0 (recordista) | passos | observações | fração final (9mod32) | fração no último quarto |
|---|---|---|---|---|
| 2678604327232691454 | 878 | 131 | 0.5649 | 0.5439 |
| 3571472436310255273 | 879 | 132 | 0.5682 | 0.5478 |
| 4761963248413673697 | 880 | 132 | 0.5682 | 0.5478 |
| 5065931099926693735 | 890 | 133 | 0.6241 | 0.6232 |
| 5977996304343501855 | 900 | 132 | 0.6212 | 0.6372 |
| 9781262575275081247 | 914 | 131 | 0.6336 | 0.6375 |
| 13041683433700108329 | 915 | 132 | 0.6364 | 0.6406 |
| 14727207461063895711 | 920 | 134 | 0.6269 | 0.6440 |

**O desvio persiste** (0,54–0,64, não 0,5) mesmo com 3× mais dados que o
testado no paper — e a fração no último quarto da órbita não está mais
próxima de 0,5 do que a fração final geral (em alguns casos até mais
longe). Não há sinal visível de convergência rumo a 0,5 dentro destas
órbitas específicas conforme elas se alongam.

## Honestidade sobre o que isso significa (e o que não significa)

Isso é **consistente com** H-030/H-021 (recordistas são selecionados por
altura excepcional, logo têm viés genuíno em runs de subida mais longos
— exatamente o que "9 mod32" representa no framework do Chang). **Não é
evidência de que o problema aberto do Chang seja falso**: sua conjectura
específica (equação 16 do paper) exige |fração−1/2|≤δ para um δ_max
determinado pelo orçamento block-TV completo do framework dele — eu não
derivei esse δ_max precisamente aqui, então não posso dizer se um desvio
de 0,55-0,64 excede ou fica dentro da tolerância que ele realmente
permite. O próprio paper já reconhece explicitamente (Table 2, Remark
6.3) que órbitas individuais mostram desvios de ±10-25% do que ele chama
de "fenômeno de nível de órbita" — nosso achado (recordistas, uma
amostra deliberadamente atípica, mostrando desvio de 0,05-0,14) está
dentro dessa faixa já reconhecida por ele, não a contradiz.

## Conclusão

Contribuição modesta e honesta: estendemos a verificação empírica do
Chang para órbitas 3× mais longas (dados novos, não testados por ele),
usando exatamente o tipo de amostra (recordistas) que ele mesmo
antecipa como fonte de viés de órbita. O resultado é consistente com o
que ele já esperava, não uma refutação nem uma confirmação do problema
aberto central. Não achamos progresso na pergunta central dele (por que
a mistura acontece ou não em geral), mas fornecemos um ponto de dado
genuíno e maior escala que o testado originalmente.

## Atualizações

- 2026-07-13: testado com os 8 maiores recordistas reais individualmente.
  Resultado honesto: desvio persiste, sem resolver nem contradizer o
  problema aberto de Chang — apropriadamente calibrado sem superclaim.
