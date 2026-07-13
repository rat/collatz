# H-031 — Varredura sistemática de primos não testados (mod 5,7,11,13,17,19,23) e potências de 3

Status: refutada (resultado negativo, mas genuinamente não previsível a
priori — checagem nova, não repetição)
Criada em: 2026-07-13

## Enunciado

Toda a família de exclusão de recordistas construída até agora (H-007,
H-014, H-022, H-027) usa só os primos 2 e 3 — os únicos que aparecem
explicitamente no mapa 3n+1. Pergunta: existe alguma classe residual
mod p, para p primo ≠2,3 (ou potências maiores de 3, como 27 e 81), que
também esteja vazia nos recordistas reais, revelando uma exclusão
totalmente nova e independente da família mod-2/mod-3?

## Como foi testado

Distribuição dos 148 recordistas reais (OEIS A006877) mod 5, 7, 11, 13,
17, 19, 23, 25, 27, 49, 81. Para toda classe com contagem baixa/zero,
verificado se já é explicada por H-007 (2 mod3), H-027 (4 mod6), H-014
(5 mod8) ou H-008 (4 mod9) — usando o representante da classe mod M como
proxy (válido porque essas quatro regras são definidas em termos de
resíduos que dividem ou compartilham fator com M nos casos relevantes).

## Resultado

- **mod 5, 7, 11, 13, 17, 19, 23**: nenhuma classe vazia — todas as
  classes têm contagem consistente com o esperado sob distribuição
  aproximadamente uniforme. **Nenhuma evidência de exclusão nova.**
- **mod 27**: 12 classes com contagem ≤1; todas as 12 já explicadas por
  H-007 ou H-008 (a única com contagem=1, não 0, é a própria exceção
  trivial n=2).
- **mod 81**: mais classes com contagem baixa (esperado ~1,8/classe), mas
  a maioria já explicada por H-007/H-014/H-008/H-027. Restaram 3 classes
  com contagem exatamente 0 sem explicação (r=19,30,60) — mas isso é
  **consistente com ruído estatístico**: sob a hipótese nula (distribuição
  uniforme, 81 classes, ~1,8 esperado/classe), o número esperado de
  classes com contagem 0 só por acaso é ~13 (Poisson(1,8), P(0)≈0,165,
  81×0,165≈13,3) — encontrar apenas 3 "não explicadas" é MENOS do que o
  ruído de base esperaria, não mais. Não há sinal.

## Conclusão

Nenhuma exclusão nova encontrada além dos primos 2 e 3. Isso é consistente
com a expectativa teórica (só 2 e 3 aparecem na definição do mapa 3n+1),
mas **não era garantido a priori** — primos "estranhos" ao mapa poderiam,
em princípio, aparecer via alguma relação indireta (como aconteceu com
mod9, que não é óbvio a partir do mapa até se construir H-022). A
checagem foi genuína (resultado não previsível com certeza antes de
rodar), e o resultado negativo reforça a robustez da consolidação de
H-028: não faltou nenhuma exclusão óbvia nos primos pequenos testados.

## Atualizações

- 2026-07-13: varredura feita, resultado negativo limpo. Nenhuma
  exclusão nova; ruído estatístico devidamente descartado com o cálculo
  de Poisson antes de reportar como "sem sinal".
