# H-044 — Revisão do paper #018/019 (Fu, Liu & Wang, "Gamma-Type Upward-Phase Statistics") — sem erros encontrados

Status: revisão externa concluída — paper de boa qualidade acadêmica,
mecanismo heurístico honestamente delimitado, sem erros encontrados
Criada em: 2026-07-14
Origem: sexto paper priorizado da coleção (item 019 no INDEX.md, arquivo
local `018_Emergence-of-Gamma-Type-Upward-Phase-Statistics.pdf`,
arXiv:2606.26811).

## O paper

"Emergence of Gamma-Type Upward-Phase Statistics in the Collatz Map: An
Effective Poisson Process Mechanism" — Weicheng Fu, Xiaobin Liu, Yisen
Wang (Tianshui Normal University / Lanzhou University / Lanzhou Center
for Theoretical Physics, China). Qualidade acadêmica claramente
superior à maioria dos itens processados até agora: afiliações
institucionais reais e verificáveis, financiamento por agências chinesas
legítimas (NSFC, grants nomeados), literatura extensa e genuína (Tao
2022, Terras 1976, Lagarias, Kontorovich-Lagarias, Barina, Sinai),
publicado como preprint arXiv com formatação de periódico de física
(estilo PRL/RevTeX). **Não alega provar a conjectura** — propõe um
mecanismo estatístico explicativo para uma regularidade empírica já
observada por um paper anterior do mesmo grupo (ref. [19]).

## Conteúdo matemático (resumo)

Decompõe a órbita de Collatz em fases "para cima" (passo ímpar 3X+1) e
"para baixo" (divisão por 2), e nota que, no mapa acelerado/Syracuse, o
número de fases para cima N↑ é exatamente o número de passos até atingir
1. Modela a ocorrência dessas fases como um processo de Poisson
homogêneo, combinado com a distribuição geométrica já conhecida da
valuação 2-ádica h=v₂(3X+1) (E[h]=2, Var(h)=2 — exatamente nosso próprio
H-001/H-011), derivando fórmulas fechadas para os parâmetros de uma
aproximação Gamma: escala θ_T=2/(2−log₂3)²≈11,61 (constante) e forma
K_T=(2−log₂3)/2·(1+log₂L) (cresce logaritmicamente com o limite superior
L da amostra X0=2L+1). Também deriva a condição de fechamento exata para
ciclos periódicos hipotéticos (2^{N↓}=∏(3+1/Xn)) e mostra que ciclos
não-triviais grandes exigiriam N↓/M aproximar log₂3 (irracional) com
precisão crescente — mas **afirma explicitamente que isso não é uma
prova de inexistência**, pois a correção finita 1/Xn não pode ser
descartada rigorosamente na dinâmica de inteiros.

## O que foi verificado (todos confirmados)

- **E[h]=2, Var(h)=2** para a valuação 2-ádica — confirmado até
  2.000.000 (`experiments/E-044-fu-liu-wang-gamma-poisson-check/`).
  Consistente com H-001/H-011.
- **Eq.6** (fórmula aproximada ligando N↓ a X0 e N↑): confirmada exata
  (após arredondamento) em 99999/99999 (100%) dos X0 ímpares testados
  de 3 a 200.001 — incluindo a órbita classicamente longa de X0=27 (41
  passos acelerados). Nossa hipótese inicial de que a aproximação
  quebraria em órbitas longas estava **errada**; a fórmula é mais
  robusta do que esperávamos.
- **Média de N↑**: bate com a previsão corrigida do paper (Eq.37) a
  ~2% em L=10⁴ e L=10⁵ — mesma ordem de precisão que o próprio paper
  relata (embora em escala bem menor que os 10⁵–10¹⁵ deles).
- **θ empírico**: fica ~8,5% abaixo de θ_T=11,61 nas nossas escalas.
  Isso **não é um erro** — o próprio paper (Fig.4a) mostra que θ só se
  aproxima do valor teórico lentamente com L, e mesmo em L=10¹⁵ o valor
  ajustado (11,245) ainda fica ~3% abaixo do teórico. Um gap maior em
  L=10⁴–10⁵ (ordens de magnitude menor que 10¹⁵) é o esperado, na
  direção correta — confirmação com escopo honestamente limitado por
  nosso orçamento computacional, não uma discrepância real.
- **Álgebra da condição de fechamento de ciclos (Eqs.30-34)**:
  conferida manualmente termo a termo — está correta. A cadeia de
  desigualdades (Eq.32→33→34) segue exatamente das hipóteses (Xn≥3
  para qualquer ciclo não-trivial; m=mín do ciclo) sem nenhum salto
  lógico.

## Contraste importante com H-043 (CTUHSK)

Este paper usa essencialmente a MESMA classe de argumento de "condição
de fechamento" que aparece (de forma mais tosca e malfeita) na tentativa
de prova do CTUHSK (H-043) — mas aqui os autores são **explícitos e
corretos** sobre seu alcance: "this asymptotic obstruction is not a
proof of the nonexistence of all nontrivial cycles" (Seção IV), e
explicam com precisão POR QUE não é (a correção finita 1/Xn determina a
valuação 2-ádica real e não pode ser descartada — é exatamente essa
correção que produz o próprio ciclo trivial conhecido). É o contraste
mais didático que já vimos na coleção entre uma prática de pesquisa
honesta (reconhecer o limite exato do que foi mostrado) e uma alegação
de prova completa mal-fundamentada (CTUHSK, H-043).

## Novas hipóteses?

Nenhuma. A distribuição geométrica de h e a condição de fechamento de
ciclos já fazem parte do nosso próprio banco de resultados
(H-001/H-011 e família de exclusão H-013/H-018/H-024/H-028, mencionada
em H-036). O paper não introduz mecanismo matematicamente novo para nós
— seu valor está na explicação estatística (Poisson) do porquê da forma
Gamma, que é uma pergunta diferente da nossa linha principal de
investigação (obstrução estrutural / precisão 3-ádica).

## Atualizações

- 2026-07-14: paper lido por completo (7 páginas), reivindicações
  centrais verificadas computacionalmente
  (`experiments/E-044-fu-liu-wang-gamma-poisson-check/`), nenhum erro
  encontrado. Verificado com `advisor()` (incluindo correção de
  precisão na descrição do gap de θ antes de finalizar). Flags
  atualizadas em `literature/papers/INDEX.md` (item 019: Lido=Sim,
  Corrigido=Sim [nada a corrigir], Implementado=Sim).
