# Outline — paper 06 (equação de pressão qx+1)

Status: `main.tex` é um rascunho completo (13 páginas, compila limpo).
Split de `01-syracuse-qx1-endogenia/main.tex` §3 (mais §4.2, "Precise
regime of the tail exponent", que encaixa melhor aqui do que em 01), em
2026-08-10, a pedido do diretor científico.

Repositório de reprodutibilidade: `github.com/faculdade/collatz-qx1-pressure`.

## Escopo

Hipóteses-fonte: H-109 (identidade de pressão), H-138 (martingale
q-ádico), H-139 (singularidade na raiz congelada), H-141 (critério de
colisão L^p), H-132 (índice de cauda no modelo iid, via Liu 2000),
H-129 (atribuída aqui em 2026-08-10; formalizada como
`conj:real-tree-tail`, o fator de escala de crescimento na árvore real,
distinto de `conj:tail-index`).

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
`thm:lp-collision`, `thm:frozen-singular`, `prop:always-frozen` (agora
via `lem:log-convex`, movido para o §3, em vez de depender para frente
do §6), `thm:transition-model`, `thm:iid-tail`. `thm:transition-model`
ganhou uma segunda prova própria na rodada de convergência de
2026-08-10 (critério de 4 níveis, ver `CRITIQUE.md`): a alegação
original de que a prova de Kontorovich-Lagarias 2010 (Teorema 8.10)
"transfere sem mudança" para q geral era falsa (o modelo B[5^0] deles
tem função de pressão diferente da deste paper, $m_{KL}(\theta)=
2^{-\theta}(1+5^{\theta-1})\ne\rho_{\mathrm{ann}}(\theta)$, ainda que
compartilhem exatamente as mesmas raízes por uma identidade algébrica
agora registrada num Remark); o limite inferior foi reescrito como um
argumento autocontido de Galton-Watson em blocos (tilt exponencial na
raiz de pressão + truncamento em K filhos por bloco para evitar
qualquer condição de momento delicada), verificado passo a passo e
revisado pelo Codex antes de entrar no texto.
Condicional/conjectural, marcado como tal no texto: `conj:transition-fine`
(antigo `prop:transition-fine`, renomeado de Proposition para
Conjecture na mesma rodada: o enunciado abre com "conjecturally" e
`conj:real-tree-tail` já dependia dele, então rotulá-lo como resultado
provado violava a Regra 10b; é estritamente mais forte que
`thm:transition-model`, fixa a constante, não só o expoente).
Conjectura: `conj:transition-arithmetic` (= problema aberto desde 1995
para q=3), `conj:tail-index` (martingale Haar-q-ádica $W_q$),
`conj:real-tree-tail` (fator de escala de crescimento na árvore real,
`conj:transition-fine`; formaliza H-129 — objeto distinto de
`conj:tail-index`, mesmo expoente previsto pelo mesmo mecanismo de
renovação implícita, sem prova de equivalência entre os dois).

## Dependência de outros papers

Este paper é a base dos outros três: 01 (guarda-chuva) usa `α_-(q)`, a
transição congelado/descongelado, e o índice de cauda; 04 (KL vs
Volkov) cita o valor `α_-(5)=0,650919` daqui; 05 (Wirsching) é
independente. Citações `\cite{BarrierCompanion}` e
`\cite{KLVolkovCompanion}` neste `main.tex` apontam para os outros dois
como "companion paper, in preparation" — atualizar para o arXiv ID real
assim que cada um for submetido.

## Pendências

- `main-pt-br.tex`: não criado. Deixado deliberadamente aberto na
  rodada de crítica de 2026-08-10 (C-30 em `CRITIQUE.md`): a política
  interna deste projeto é só traduzir sob pedido explícito, o que tensiona
  com a letra da Regra 5 (todo paper é bilíngue). Registrado como
  tensão a resolver com o pesquisador, não como pendência técnica.

## Rodada de crítica (Regra 8/15) fechada

Rodada de 2026-08-10: 30 achados (`CRITIQUE.md`), 29 corrigidos, 1
deixado `open` com motivo (C-30, acima). Abstract reescrito por
completo (não é mais rascunho), `thm:transition-model` ganhou prova
própria, o lema de log-convexidade foi generalizado e movido para o
§3, todas as citações do item C-21 foram verificadas contra fonte
primária (uma delas, PDF de Villemonais-Zalduendo 2025, baixado e lido
para resolver C-22).

## Passagem de redação final (2026-08-10, mesma sessão)

H-129 atribuída aqui (decisão do diretor científico) e formalizada
como `conj:real-tree-tail`. Ao formalizar, a evidência empírica de q=3
e as três baterias de raízes de q=5, antes atribuídas a
`conj:tail-index`, foram reatribuídas: medem o fator de escala da
árvore real (`prop:transition-fine`), não a martingale Haar-q-ádica.
Verificado com Codex antes de editar. Abstract reescrito de novo
(Regra 8b) para refletir os dois objetos separadamente. Checklist da
Regra 4b/seção 10 aplicado ao `main.tex` inteiro. Recompila limpo,
bibliografia e referências cruzadas conferidas por script, sem órfãos.
