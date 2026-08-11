# Outline — paper 04 (Kontorovich-Lagarias vs. Volkov)

Status: `main.tex` completo, em loop de crítica de convergência
(critério do pesquisador: 3 rodadas consecutivas limpas; rodadas 1-5
aplicadas 2026-08-10/11, ver `CRITIQUE.md` para o histórico completo e
a contagem de rodadas limpas consecutivas atual). 6 páginas, compila
limpo. Split de `01-syracuse-qx1-endogenia/main.tex`
§6, em 2026-08-10, a pedido do diretor científico ("divida o paper de
forma que todos tenham sua importância e possam receber citações").

Repositório de reprodutibilidade: `github.com/faculdade/collatz-kl-volkov`.

## Escopo

Hipóteses-fonte: H-113 (portão estatístico original, E-097), H-169
(congruência de irmãos, prova usada para construir os controles
casados), E-139 (recalibração com controles casados, achado principal
deste paper).

## Estrutura (numeração atual; a antiga §3 "A disputa" foi fundida na
introdução na rodada 2 do loop de crítica, por redundância)

1. Introdução — a disputa Kontorovich-Lagarias/Volkov (2009), o gap
   Δ=0,027, o que Volkov de fato conta ($Q(x)$, distinto de $\pi_5(x)$
   de KL), e duas frases finais dizendo o que o paper mede e encontra.
2. Setup — árvore reversa do mapa qx+1 acelerado, especializada a q=5;
   Remark distinguindo o Theorem 8.10 de KL (sobre a progênie do
   passeio ramificado, proxy heurístico para a contagem de inteiros) da
   contagem $N_u(x)$ deste paper; Lema da congruência de irmãos
   (H-169), usado para construir os controles sintéticos de expoente
   ajustável.
3. Método — enumeração exata, janela fixa, extrapolação de Aitken.
4. Resultado — `thm:kl`, leitura de janela fixa 0,639, não exclui
   nenhuma das duas hipóteses (resultado antigo, H-113).
5. Comparação calibrada — `thm:kl-calibrated`, o achado principal: o
   estimador de janela fixa tem viés maior que a disputa em si;
   construindo construções casadas por congruência de irmãos (mesma
   estrutura, só `q` trocado por um valor real ajustável) e uma
   construção irrestrita (só a lei de prole em comum), a árvore
   aritmética lê 0,64926 na década 1e9→1e10, dentro da banda das três
   construções a 0,650919 e separada por mais de sete larguras de banda
   de uma construção a 0,678 (0,02822/0,00371=7,6).
6. Discussão — dois sistemáticos (implementação, truncamento), ponte
   entre a construção irrestrita e o colapso acelerado do $B[5^0]$ de
   KL (só a cota superior do expoente transfere rigorosamente; a cota
   inferior é lead em aberto, `BACKLOG.md` item 10), e escopo preciso
   (testa o valor 0,678, não o modelo de Volkov em si).

## Rótulo do resultado (Regra 10b)

Medição empírica com controles calibrados, não prova. Não é prova
contra o modelo de ramificação de Volkov em si, só contra o valor do
expoente em disputa.

## Pendências

- `main-pt-br.tex`: não criado ainda, só sob pedido explícito (Regra 5,
  mesma política do paper 01).
- `CRITIQUE.md`: loop de crítica de convergência em andamento; ver a
  tabela de status e as seções datadas R1/R2/R3 no próprio arquivo para
  a contagem de rodadas limpas consecutivas.
- Bibliografia: três entradas (Kontorovich-Lagarias 2009, Volkov 2006,
  verificado contra a página de publicações do autor, e uma entrada
  provisória `PressureCompanion` apontando para o paper 06 "em
  preparação"). Atualizar a citação de `PressureCompanion` quando o 06
  tiver DOI/arXiv. Pendência real, não resolvida por mim: depende do
  paper 06 ganhar arXiv/DOI.
- README-PT-BR de `experiments/E-097-qx1-empirical-gate/` e
  `experiments/E-139-kl-volkov-window-calibration/` (e os espelhos
  correspondentes em `collatz-kl-volkov`) ainda dizem "dez larguras de
  banda" e "exclui Volkov com folga", números corrigidos nos READMEs em
  inglês em 2026-08-10 mas não propagados ao PT-BR (Regra "sem edição
  de PT-BR não solicitada"). Sinalizado, não corrigido.
- BACKLOG.md item 10: estender o teorema do paper 06 (transição
  estrutural, modelo i.i.d.) à lei de prole por classe de resíduo, para
  que a cota inferior do expoente também transfira à construção
  irrestrita deste paper. Investigação real ainda não feita.
