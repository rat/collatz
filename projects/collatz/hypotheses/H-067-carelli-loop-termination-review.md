# H-067 — Revisão do paper #074 (Carelli, "Loop Termination and Generalized Collatz Sequences") — pesquisa teórica de CS, resultado condicional confirmado

Status: revisão externa concluída (escopo limitado ao conteúdo
relacionado a sequências de Collatz generalizadas) — 0 falhas
Criada em: 2026-07-15
Origem: item 074 da coleção (`literature/papers/INDEX.md`), já baixado
(`073_Loop-Termination-Generalized-Collatz.pdf`). Previamente "lido e
catalogado" em sessão anterior (ver `STATE.md`), sem revisão dedicada
até agora.

## O paper

Carelli, M. (2026), *Loop Termination and Generalized Collatz
Sequences*, arXiv:2605.15094 [cs.LO]. CISPA Helmholtz Center for
Information Security, Alemanha. Financiado por bolsa ERC (Grant HYPER
No. 101055412). Referências em venues de altíssimo nível para ciência
da computação teórica (STACS, LICS, CAV, ICALP) — classificação ACM
"Track B: Automata, Logic, Semantics".

**Este é um paper de ciência da computação teórica**, não de
matemática pura sobre Collatz. Estuda a decidibilidade de terminação
de *Single-Path Linear-Constraint Loops* (SLCs) de uma variável — um
problema em aberto há duas décadas na verificação de programas — e
conecta essa questão a *sequências de Collatz generalizadas*
(framework de Matthews/Watts/Möller, bem estabelecido na literatura
desde os anos 1980), das quais o Collatz clássico (`d=2, m=3`) é um
caso particular. **Não tenta resolver a conjectura clássica.**

## Resultado central (condicional, honesto sobre o próprio escopo)

**Teorema 20**: se a *Reachability Conjecture* (formulação mais fraca
da antiga *Uniform Distribution Conjecture* de Matthews & Watts) vale,
então a terminação de SLCs de uma variável é decidível em tempo
polinomial. O paper prova essa conjectura **apenas para `d=2`**
(Proposição 17) — os casos `d>2` permanecem **explicitamente em
aberto**, com o Exemplo 19 apresentando uma instância concreta ainda
não resolvida (`T(x)=⌊4x/3⌋`).

## Escopo desta revisão

Dado que o conteúdo central do paper é sobre teoria da computação
(decidibilidade de SLCs), não sobre a conjectura de Collatz em si, esta
revisão foca no que é **diretamente sobre sequências de Collatz
generalizadas** (Proposição 17, Exemplo 19) e faz apenas checagens
pontuais nos resultados de geometria computacional mais gerais que
usam essa linguagem como ingrediente de prova (Teorema 14, Proposição
11). A maquinaria mais ampla (decomposição de Minkowski-Weyl, Lemas
21/23/24/25 sobre "self-avoiding traces" de SLCs em geral) fica fora
do escopo — é sobre SLCs em geral, não sobre Collatz — seguindo o
mesmo princípio de escopo já aplicado a
[[H-060-csikos-dag-ness-review]].

## O que foi verificado

`experiments/E-067-carelli-loop-termination-check/experiment.py`,
cinco partes:

1. **Mecanismo algébrico da Proposição 17** — o ponto fixo
   `n=r_i/(m_i-d)` é a única forma de uma trajetória ficar presa para
   sempre numa única classe residual. Verificado algebricamente:
   1.469 combinações (mapeamento, classe), 500 com ponto fixo inteiro
   pertencente à própria classe, `T(n₀)=n₀` confirmado em todas.
2. **Teste empírico do conteúdo prático da Proposição 17** — 200
   mapeamentos de Collatz generalizados aleatórios × 100 pontos
   iniciais cada (19.989 trajetórias, 300 passos cada): 19.973
   escaparam da classe residual inicial; das 16 que ficaram presas,
   **todas** eram exatamente o ponto fixo — 0 exceções.
3. **Exemplo 19** (questão explicitamente **aberta** no paper,
   `T(x)=⌊4x/3⌋`, se todo `n≥3` atinge um múltiplo de 3): testado para
   `n=3` até 2.000.000 (limite de 2.000 passos) — **nenhum
   contraexemplo encontrado**. Isso não prova nem refuta a questão
   aberta, apenas não encontra contraexemplo na faixa testada (mesma
   limitação que o próprio paper reconhece).
4. **Teorema 14** (todo ciclo de SLC de uma variável tem comprimento
   ≤2) — checagem pontual: 500 SLCs aleatórios de 1 variável, busca de
   ciclos em faixa limitada — maior ciclo encontrado foi de
   comprimento 2, nenhum >2.
5. **Proposição 11** (construção de SLC com ciclo mínimo de comprimento
   exatamente `2^n`, via ciclo Hamiltoniano no hipercubo) — verificada
   a construção combinatória de base (código de Gray, ciclo fechado
   válido) para `n=1,2,3`. A alegação geométrica completa (que o
   politopo convexo não tem nenhum ponto inteiro espúrio) exigiria um
   solver de LP (indisponível neste ambiente) para `n=3` — não
   verificada, relatada como fora de escopo prático, não como falha.

## Resultado

**Nenhum erro encontrado** no conteúdo relacionado a sequências de
Collatz generalizadas. O paper é tecnicamente sólido, com estrutura
lemma-proposição-teorema rigorosa e honesta sobre seu próprio escopo
condicional (Teorema 20 explicitamente depende da Reachability
Conjecture; o próprio paper afirma "for most mappings (in particular,
all cases with d>2), the conjecture remains open").

## Por que isso é uma revisão positiva

Assim como os itens 057 (Reyes Jiménez) e 038/015 (Kayadibi), este é
mais um exemplo de pesquisa genuína e tecnicamente sofisticada dentro
desta coleção — aqui vindo de ciência da computação teórica (não
matemática pura), conectando "sequências de Collatz generalizadas" a
um problema de decidibilidade de duas décadas. A honestidade
epistêmica é exemplar: o resultado principal é condicional, o caso
resolvido (`d=2`) é explicitamente o mais fácil, e a conclusão lista
abertamente as questões que permanecem sem resposta.

## Novas hipóteses?

Nenhuma concreta para o programa de pesquisa deste projeto (o foco do
paper é decidibilidade de SLCs, não a conjectura clássica). Vale notar
para referência futura: o Exemplo 19 (`T(x)=⌊4x/3⌋`, `d=3`) é uma
instância aberta e concreta de uma questão number-theoretic
relacionada — não teve contraexemplo encontrado até `n=2.000.000`,
mas isso não é uma contribuição nova (o próprio Carelli já reporta
isso como em aberto).

## Atualizações

- 2026-07-15: paper lido por completo (22 páginas), 5 partes
  verificadas computacionalmente (escopo limitado ao conteúdo
  Collatz-relevante, conforme explicado acima). `INDEX.md` atualizado
  (item 074: Lido=Sim, Corrigido=Sim [nada a corrigir dentro do
  escopo revisado], Implementado=Sim).
