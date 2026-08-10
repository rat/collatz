# H-177: certificado de operador B_kappa para a desigualdade de par (Q2)

Status: backlog

Criada: 2026-08-10

Origem: proposto por uma consulta ao Codex (Regra 11b) sobre a
Questão 2 de H-161 (desigualdade de anti-concentração de pares).
Transcrição completa da consulta em
`experiments/E-142-singularity-diagnostic/codex_consultation_transcript.txt`.
Número escolhido para não colidir com outros agentes rodando em
paralelo nesta sessão (estado do repositório nesta rodada ia até
H-176); renumerar na integração se necessário.

## O que se pede

Construir e certificar um operador positivo homogêneo `B_kappa`
(formalismo de Perron-Frobenius/Collatz-Wielandt não-linear) sobre o
semigrupo afim 3-ádico alcançável a partir dos dois pontos `g_1, g_2`
da órbita de `A` (H-161), tal que `B_kappa h <= h` para alguma função
positiva `h` provaria, por indução, a desigualdade de par de Q2 com
`kappa=3/5` (melhorando `beta_eff<=1,882712` de H-166 para
`beta_eff<=1+1/(2*0,6)=1,833`).

Programa concreto proposto pelo Codex (não verificado linha a linha por
nós, ver H-161 para o que foi corroborado versus não verificado):

1. Manter os termos de menor índice em cada classe (`s=0,1,2`) e
   acrescentar os seguintes (`j+3,j+6,...`); descartar termos é válido
   (dá cota superior), só enfraquece.
2. Representar `h(alpha,beta)` por cilindros mod `3^K`. `K=4` dá 39366
   estados; `K=5` dá 354294, ambos viáveis computacionalmente.
3. Resolver numericamente a equação própria não-linear em `log h`, com
   otimização convexa sobre o acoplamento `pi` em cada estado.
4. Verificar `B_{3/5} h <= h` com aritmética de intervalo dirigida
   (coeficientes são racionais; só as potências de expoente `3/5`
   precisam de envelope intervalar).
5. Se o certificado global falhar, repetir no subconjunto FECHADO de
   estados realmente alcançável a partir de `g_1, g_2` (não tomar um
   "pior lift" independente em cada nível, recriaria a inconsistência
   adversarial que o programa de Weyl já mostrou ser vazia).

**Ressalva do próprio Codex, importante**: os momentos observados
parecem convergir a uma constante positiva, então o raio espectral
crítico provavelmente é EXATAMENTE 1, não estritamente menor. Pode ser
necessário certificar uma função subinvariante com igualdade em alguns
estados, ou uma condição tipo Foster-Lyapunov
(`B_kappa h <= rho*h + D`, `rho<1`), não um certificado de um passo
simples.

## Por que não foi tentado ainda (decisão explícita, não esquecimento)

Consultado o advisor: os próprios números intermediários que o Codex
computou durante a consulta (fatores `z` entre `1,27` e `1,98` para o
certificado ingênuo de um passo, em `kappa` entre `0,4` e `0,6`, em
vários estados) já mostram que um certificado de UM PASSO simples
falha nos parâmetros relevantes. Combinado com a suspeita de raio
crítico exatamente 1 (que pede a construção mais elaborada de
Foster-Lyapunov), isto é engenharia-mais-teoria substancial, não um
teste barato: um certificado ingênuo que falhasse não teria decidido
nada (não refuta nem prova Q2), e o esforço de construir a versão
elaborada está fora do escopo de uma sessão dedicada a fechar backlog,
não a abrir um programa de pesquisa novo.

## Pré-requisito antes de investir

H-161/E-142 mediram evidência (não prova) de que o limite da medida de
Syracuse não é Haar-singular (`E[-log N_ell]` convergente por ajuste de
lei de potência, expoente `-1,7` a `-2,1`, bem abaixo do limiar `-1` de
divergência). Se fosse singular, Q2 seria falsa e este programa inteiro
seria fútil (ver H-161, achado do Codex: Q2 implica não-singularidade).
A evidência atual aponta a favor de prosseguir, não é decisiva. Antes
de investir tempo real no operador `B_kappa`, valeria estender o
diagnóstico de singularidade (mais níveis, se uma implementação sem o
array denso `3^ell` completo puder ser escrita, já que o método atual
esbarra em memória por volta de `ell~17-19`, mesmo problema já visto
duas vezes nesta investigação).

## Primeiro passo, se retomado

Implementar o operador para `K=4` primeiro (39366 estados, o menor caso
viável), sem aritmética de intervalo ainda (só ponto flutuante), para
ver se a estrutura numérica se comporta como o Codex previu antes de
investir no aparato de verificação certificada. Se o raio espectral
medido (não certificado) já ficar claramente acima de 1 para
`kappa=3/5`, a rota morre rápido e barato; se ficar perto de 1 ou
abaixo, vale investir na certificação de verdade.
