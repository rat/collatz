# H-052 — Revisão do paper #010 (Ruiz Castillo, "Teorema Central del Límite Residual") — resultado central é rotulado "Conjetura", consequência empírica confirmada

Status: revisão externa concluída — identidades algébricas corretas
(elementares); resultado central honestamente rotulado conjectural no
corpo do texto apesar do título; consequência empírica testável
(normalidade assintótica) confirmada em trajetórias reais de Collatz
Criada em: 2026-07-14
Origem: paper baixado manualmente pelo diretor científico (item 010 da
coleção, `literature/papers/010_Teorema-Central-Limite-Ruiz-Castillo.pdf`,
Juan Carlos Ruiz Castillo, 29 páginas).

## O paper

"Teorema Central del Límite Residual de Ruiz Castillo para la dinámica
acelerada de la Conjetura de Collatz" — terceiro paper deste autor
revisado na coleção (o primeiro foi item 001/H-039, o segundo item
008/H-050). Propõe um Teorema Central do Limite para as flutuações da
"deuda residual" L_k(n) = k·log₂(3) − A_k(n) — a mesma quantidade
elementar de sempre (drift logarítmico padrão / equação de ciclo),
agora estudada sob a lente de convergência em distribuição.

O resultado principal é formalmente rotulado **"Conjetura 4.2"** (não
"Teorema") no CORPO do paper, apesar do TÍTULO dizer "Teorema" — o
próprio autor lista honestamente 5 hipóteses não estabelecidas
(existência de medida de Gibbs residual, ergodicidade, espaço
funcional adequado, brecha espectral do operador de transferência
residual, variância residual positiva) das quais o resultado depende,
e nunca as prova ou constrói. A conclusão do próprio paper diz
explicitamente: "Este marco no demuestra la Conjetura de Collatz."

A lista de referências revela ~20 papers do mesmo autor (2025-2026)
aplicando, um de cada vez, um conceito clássico de teoria
ergódica/mecânica estatística/probabilidade (drift, pressão, cotas
dissipativas, dimensão, entropia, medidas de Gibbs, princípio
variacional, operador de transferência, teoria espectral, TCL, grandes
desvios) à MESMA quantidade L_k(n).

## O que foi verificado

**Parte 1 — identidades algébricas provadas no corpo do paper**
(confirmadas, elementares):
- Teorema 2.3: L_k(n) = −S_k(φ), onde φ(a)=a₀−log₂(3) — reescrita
  algébrica direta da definição, 0 falhas em 27×5 casos testados.
- Proposición 2.5: Var(L_k)=Var(−S_k φ) — trivial (Var(−X)=Var(X)),
  confirmado numericamente (diferença máxima = 0).

**Parte 2 — consequência empírica testável da "Conjetura 4.2"**: como
as hipóteses técnicas (medida de Gibbs residual, brecha espectral)
nunca são construídas no paper, testamos a PREVISÃO observável
diretamente — normalidade assintótica de
Z_k = (L_k(n) − k·m_RC)/√k, m_RC = log₂(3)−2 — em trajetórias REAIS de
Collatz (não simulação i.i.d. abstrata), para k=5,20,50,100,300:

| k   | média Z_k | var Z_k | assimetria | curtose |
|-----|-----------|---------|------------|---------|
| 5   | -0,0201   | 2,0163  | -0,9590    | 4,3795  |
| 20  | 0,0037    | 1,9703  | -0,4592    | 3,3472  |
| 50  | 0,0081    | 1,9882  | -0,2916    | 3,1821  |
| 100 | 0,0070    | 1,9680  | -0,2366    | 3,0770  |
| 300 | -0,0031   | 1,9832  | -0,1002    | 2,9843  |

Variância estabiliza perto de 2 (=σ²_RC=Var(a_j), já estabelecido em
H-001/H-011), assimetria → 0 e curtose → 3 (valor gaussiano) conforme
k cresce — a previsão é **empiricamente plausível em dados reais**,
mesmo sem as hipóteses técnicas construídas. Esta é a primeira
verificação numérica real desta previsão (o próprio paper não contém
nenhuma). Ver `experiments/E-052-ruiz-castillo-clt-check/`.

## Nota de integridade: bug de amostragem no nosso código, corrigido antes de reportar

A primeira versão do experimento amostrava n uniformemente em
`range(3, 10**15, 2)` para todo k, com `require_no_fixed_point=True`.
O comprimento médio de uma trajetória Syracuse para n de ~50 bits é
log₂(n)/(2−log₂3) ≈ 120 passos; para k=300 (~4,9 desvios-padrão acima
da média) a rejeição ficava tão próxima de 100% que o loop de retry
nunca completava — o processo em background ficou preso 17 minutos sem
progredir. Diagnosticado e corrigido escalando a faixa de amostragem
com k (bits de n escolhidos para que o comprimento esperado da
trajetória seja ~3k+50), reduzindo o tempo de execução total para ~5
segundos. Não é um erro do paper — é um bug na nossa própria
verificação, identificado e corrigido antes de reportar qualquer
resultado.

## Caráter do paper — mesmo padrão dos dois Ruiz Castillo anteriores (H-039, H-050)

- **Rotulagem honesta**: "Teorema" no título, "Conjetura" no corpo —
  terceira vez que observamos o autor sendo transparente sobre o que
  de fato prova vs. o que apenas propõe, mesmo quando o título é mais
  ambicioso que o conteúdo.
- **Matemática elementar dressed em terminologia extensa**: a
  identidade fundamental (Teorema 2.3) é apenas uma reescrita da
  definição de L_k; a "invariância de variância" (Proposición 2.5) é
  trivial.
- **Zero conteúdo numérico real no próprio paper** — mesmo padrão de
  H-039 e H-050. A verificação empírica acima (Parte 2) é a primeira
  vez que a consequência observável desta família de conjecturas é
  efetivamente testada contra trajetórias reais.
- **~20 autocitações**, confirmando novamente o padrão: um conceito
  clássico por paper, aplicado à mesma quantidade L_k(n).

## Novas hipóteses?

Nenhuma. O mecanismo central (drift logarítmico padrão da equação de
ciclo) já é conhecido nosso (H-001/H-011, H-044, H-045, H-050). A
verificação empírica da Parte 2 é um resultado de calibração útil (a
previsão de normalidade assintótica é plausível), não uma nova
hipótese de pesquisa própria.

## Atualizações

- 2026-07-14: paper lido por completo (29 páginas), identidades
  algébricas verificadas (Parte 1) e consequência empírica testada em
  trajetórias reais de Collatz (Parte 2) via
  `experiments/E-052-ruiz-castillo-clt-check/`; um bug de amostragem
  no nosso próprio código (contaminação por trajetórias curtas
  demais) foi identificado e corrigido antes de reportar qualquer
  resultado. Nenhum erro real do paper encontrado. Flags atualizadas
  em `literature/papers/INDEX.md` (item 010: Lido=Sim, Corrigido=Sim
  [nada a corrigir no paper], Implementado=Sim).
