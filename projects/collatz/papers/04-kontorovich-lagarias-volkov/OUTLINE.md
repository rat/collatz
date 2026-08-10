# Outline — paper 04 (Kontorovich-Lagarias vs. Volkov)

Status: `main.tex` é um rascunho completo (4 páginas, compila limpo).
Split de `01-syracuse-qx1-endogenia/main.tex` §6, em 2026-08-10, a
pedido do diretor científico ("divida o paper de forma que todos
tenham sua importância e possam receber citações").

Repositório de reprodutibilidade: `github.com/faculdade/collatz-kl-volkov`.

## Escopo

Hipóteses-fonte: H-113 (portão estatístico original, E-097), H-169
(congruência de irmãos, prova usada para construir os controles
casados), E-139 (recalibração com controles casados, achado principal
deste paper).

## Estrutura

1. Introdução — a disputa Kontorovich-Lagarias/Volkov (2009), o gap
   Δ=0,027 nunca resolvido por falta de dado suficiente.
2. Setup — árvore reversa do mapa qx+1 acelerado, especializada a q=5;
   Lema da congruência de irmãos (H-169), usado para construir os
   controles sintéticos de expoente ajustável.
3. A disputa — enunciado preciso das duas previsões.
4. Método — enumeração exata, correção de contaminação de buffer,
   extrapolação de Aitken.
5. Resultado (§5) — `thm:kl`, leitura de janela fixa 0,639, não exclui
   nenhuma das duas hipóteses (resultado antigo, H-113).
6. Comparação calibrada (§6) — `thm:kl-calibrated`, o achado novo desta
   sessão: o estimador tem viés maior que a disputa em si; construindo
   controles casados (mesma estrutura de ramificação e de irmãos, só
   `q` trocado por um valor real ajustável), a árvore aritmética lê
   0,64926 [0,64818, 0,65027], separada de um controle a 0,678 por mais
   de sete larguras de banda (0,02822/0,00371=7,6), e bate com
   controles a 0,650919.
7. Discussão — escopo preciso (testa o valor 0,678, não o modelo de
   Volkov em si, que tem estrutura de árvore diferente e não foi
   implementado).

## Rótulo do resultado (Regra 10b)

Medição empírica com controles calibrados, não prova. Not a proof
against Volkov's actual branching model, only against the disputed
exponent value.

## Pendências

- Abstract marcado no `main.tex` como rascunho, precisa de reescrita à
  mão pelo pesquisador (Regra 4b, divisão de trabalho).
- `main-pt-br.tex`: não criado ainda, só sob pedido explícito (Regra 5,
  mesma política do paper 01).
- `CRITIQUE.md`: existe e está fechado (2026-08-10, 23 achados, todos
  resolvidos: 22 corrigidos, 1 rejeitado com motivo registrado).
- Bibliografia: só 2 entradas (Kontorovich-Lagarias 2009, e uma entrada
  provisória `PressureCompanion` apontando para o paper 06 "em
  preparação" — atualizar a citação quando 06 tiver DOI/arXiv). Pendência
  real, não resolvida por mim: depende do paper 06 ganhar arXiv/DOI.
- README-PT-BR de `experiments/E-097-qx1-empirical-gate/` e
  `experiments/E-139-kl-volkov-window-calibration/` (e os espelhos
  correspondentes em `collatz-kl-volkov`) ainda dizem "dez larguras de
  banda" e "exclui Volkov com folga", números corrigidos nos READMEs em
  inglês em 2026-08-10 mas não propagados ao PT-BR (Regra "sem edição
  de PT-BR não solicitada"). Sinalizado, não corrigido.
