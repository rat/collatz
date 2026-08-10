# Outline — paper 06 (equação de pressão qx+1)

Status: `main.tex` é um rascunho completo (13 páginas, compila limpo).
Split de `01-syracuse-qx1-endogenia/main.tex` §3 (mais §4.2, "Precise
regime of the tail exponent", que encaixa melhor aqui do que em 01), em
2026-08-10, a pedido do diretor científico.

Repositório de reprodutibilidade: `github.com/faculdade/collatz-qx1-pressure`.

## Escopo

Hipóteses-fonte: H-109 (identidade de pressão), H-138 (martingale
q-ádico), H-139 (singularidade na raiz congelada), H-141 (critério de
colisão L^p), H-132 (índice de cauda no modelo iid, via Liu 2000).

## Estrutura

1. Introdução.
2. Setup (§2) — mapa qx+1 acelerado, árvore reversa, o funcional G.
3. O operador de pressão (§3) — exemplo do autômato mod-q ingênuo (não
   bem definido, correção de um argumento anterior), lema da bijeção
   de fibra, teorema da identidade de pressão anelada exata, martingale
   de densidade q-ádica, critério de colisão L^p, singularidade na raiz
   congelada.
4. Congelado vs. descongelado (§4) — transição de congelamento, tabela
   de limiares `alpha_c(q)`.
5. Transição estrutural em q=5 (§5) — teorema no modelo iid, proposição
   condicional mais fina, conjectura na árvore aritmética (= Growth
   Exponent Conjecture de Kontorovich-Lagarias/Applegate-Lagarias para
   q=3), conjectura do índice de cauda, teorema do índice de cauda no
   modelo iid (prova via Liu 2000).
6. Regime preciso do expoente de cauda em q=3 (§6) — classificação
   contra a teoria crítica de smoothing transform multivariado
   (Kolesko-Mentemeier), não é o caso crítico.
7. Confirmação empírica em árvores reversas reais (§7).

## Rótulo dos resultados (Regra 10b)

Teorema (prova completa): `thm:pressure`, `thm:qadic-martingale`,
`thm:lp-collision`, `thm:frozen-singular`, `prop:always-frozen`,
`thm:transition-model`, `thm:iid-tail`. Condicional/heurístico, marcado
como tal no texto: `prop:transition-fine` (condicional a um refinamento
tipo renovação, não provado). Conjectura: `conj:transition-arithmetic`
(= problema aberto desde 1995 para q=3), `conj:tail-index`.

## Dependência de outros papers

Este paper é a base dos outros três: 01 (guarda-chuva) usa `α_-(q)`, a
transição congelado/descongelado, e o índice de cauda; 04 (KL vs
Volkov) cita o valor `α_-(5)=0,650919` daqui; 05 (Wirsching) é
independente. Citações `\cite{BarrierCompanion}` e
`\cite{KLVolkovCompanion}` neste `main.tex` apontam para os outros dois
como "companion paper, in preparation" — atualizar para o arXiv ID real
assim que cada um for submetido.

## Pendências

- Abstract marcado como rascunho, precisa de reescrita à mão.
- `main-pt-br.tex`: não criado, só sob pedido explícito.
- `CRITIQUE.md`: não existe ainda.
- Nota de estilo herdada do `main.tex` original: o
  Remark~`rem:transfer-basis` tinha uma frase de meta-honestidade
  ("We are precise about the status of this because...") banida pela
  Regra 4b; já reescrita nesta versão sem a frase-gatilho, mas vale
  conferir se sobrou algo parecido em outros trechos copiados
  verbatim antes de submeter.
