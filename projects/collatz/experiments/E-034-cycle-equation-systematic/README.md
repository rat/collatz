# E-034 — Segue-a-partir-do-vídeo: equação de ciclo e extensão de H-009

Hipótese relacionada: [`H-034-video-cycle-equation-followup.md`](../../hypotheses/H-034-video-cycle-equation-followup.md)

## O que foi testado

Parte 1: reproduz o achado específico de um vídeo informal (n=13 para 3
multiplicações + 5 divisões) com a fórmula correta e verificada (mesma de
H-009/E-009).

Parte 2: estende H-009 (que foi até a=14) para além disso, quantificando
precisamente onde a explosão combinatória de composições torna força
bruta inviável.

## Resultado

Parte 1: **refutado** — nenhum candidato inteiro existe para (a=3,S=5) em
nenhuma das 6 ordens. O achado do vídeo não se sustenta.

Parte 2: verificação completa e limpa até **a=16** (restringindo a
S=S_min exatamente). Além disso, a combinatória cresce rápido demais
(bilhões de composições por par a testar) para força bruta pura.

Reproduzir: `python3 experiment.py [A_MAX] [JANELA_S] [MAX_COMPOSICOES]`
(ex: `python3 experiment.py 16 0 5000000` para a busca limpa completa).

## Status de H-034

**Confirmada** — achado do vídeo tecnicamente refutado; H-009 estendido
de a=14 para a=16 (janela mais estreita); parede combinatória
quantificada com precisão, explicando por que a literatura profissional
(Simons & de Weger) precisa de frações contínuas + técnicas adicionais,
não apenas mais poder computacional.
