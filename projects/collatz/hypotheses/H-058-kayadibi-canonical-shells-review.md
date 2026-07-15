# H-058 — Revisão do paper #015 (Kayadibi, "Canonical Shells and Residue-Cover Trees") — framework condicional honesto, sem erros encontrados

Status: revisão externa concluída — toda a maquinaria algébrica provada
confirmada; framework explicitamente condicional (não alega provar
Collatz), sem erros encontrados
Criada em: 2026-07-15
Origem: item 015 da coleção (`literature/papers/INDEX.md`), já baixado
(`015_Canonical-Shells-Residue-Cover-Trees.pdf`).

## O paper

Kayadibi, S.Y. (2026), *Canonical Shells and Residue-Cover Trees in a
Conditional First-Descent Approach to the Collatz Problem*. Victoria
University, Melbourne, Austrália. 45 páginas, estrutura
lemma-proposição-teorema-corolário bem formal e densa. Constrói sobre
dois papers anteriores da própria autora (referências [11] e [12] do
próprio texto — [11] é exatamente o item 038 desta coleção, "A modular
classification of pre-descent resistance in accelerated odd Collatz
dynamics", ainda não revisado nesta sessão; útil ter isso em mente
quando chegarmos lá).

Organiza os inteiros ímpares positivos em "canonical shells"
`S°_m = {n : v₂(n+1)=m}`, decompõe cada shell em componente
"certificada" (`D°_m`, descida exata garantida em `τ(n)=m`) e
"não-certificada" (`N°_m`), e propõe uma rota condicional para cobertura
universal de "primeira descida" (que implicaria convergência de Collatz
via argumento de contraexemplo mínimo), reduzindo tudo a dois requisitos
estruturais **não provados em geral**: (1) a "dyadic gap condition"
(separação diofantina entre potências de 2 e 3) e (2) "closure" de toda
"residue-cover tree" não certificada — ambos verificados apenas
computacionalmente, em faixa finita (`2≤m≤100000` e `N=10⁷`
respectivamente).

## Honestidade epistêmica — explícita e correta

A Seção 15 (Conclusão) é inequívoca: *"The framework developed here
does NOT prove the Collatz conjecture unconditionally. Rather, it
reduces the first-descent problem to two explicit structural tasks...
The finite computations reported in this paper support the proposed
mechanism over the tested range, but they remain finite evidence only.
A full proof through this route would require establishing both
structural conditions for all shell levels and all non-certified
branches."* Nenhuma alegação de prova completa. Mesmo padrão de
honestidade de Williams (H-042) e da maioria dos papers de Ruiz
Castillo revisados (H-052 a H-056).

## O que foi verificado

`experiments/E-058-kayadibi-canonical-shells-check/experiment.py`,
cinco partes, contra simulação REAL do mapa de Collatz acelerado
(não reconstruindo as fórmulas do próprio paper):

1. **Persistence Identity (Lemma 3.1) + Corolário 3.2** — 3120 casos
   `(m,q,j)`, 0 falhas; 2730 casos confirmando "sem descida precoce".
2. **First-Exit Formula (Lemma 4.1) + Certified Exact Descent (Teorema
   4.5)** — 1414 casos, 191 identificados como certificados (`q≡q*
   mod 2^κ_m`), `τ(n)=m` exato confirmado em todos. 0 falhas.
3. **Dyadic Gap Condition (Definição 5.1)** — reproduzida com inteiros
   nativos exatos (mais simples que os 800 dígitos `mpmath` do paper —
   Python `int` já é exato) para `2≤m≤20.000`. 0 falhas. Valores da
   Tabela 1 do paper (denominadores de convergentes superiores de
   `log₂3`: 5, 41, 306, 15.601, e seus `K_m`: 8, 65, 485, 24.727)
   reproduzidos **exatamente**.
4. **Cumulative Affine Formula (Teorema 7.3) + Residue Cylinder
   (Teorema 8.2)** — 2000 casos aleatórios `(n,r)` para a fórmula
   afim; 500 pares `(n, n+2^(A+1))` confirmando que elementos do mesmo
   cilindro compartilham o mesmo padrão de valuação. 0 falhas.
5. **Reprodução em escala menor da Tabela 2/3** (`N=10⁶`, `L=2000` —
   não `10⁷`/`10000` do paper, por custo computacional): 0 descidas
   precoces (`τ<m`, que nunca deveria ocorrer — o invariante realmente
   crítico), 0 casos não resolvidos, split limpo entre exato (106.866)
   e atrasado (143.134) consistente com o que o paper reporta em
   escala maior.

## Resultado

**Nenhum erro encontrado.** Toda a maquinaria algébrica que o paper
efetivamente PROVA (não a parte condicional) resistiu à verificação
computacional independente sem exceção, incluindo reprodução exata dos
valores numéricos específicos citados no próprio paper (Tabela 1). A
parte condicional (dyadic gap global + fechamento de toda residue-cover
tree) permanece genuinamente em aberto — nem o paper afirma tê-la
resolvido, nem esta revisão tentou resolvê-la (fora de escopo: exigiria
um resultado matemático novo, não uma verificação).

## Novas hipóteses?

Nenhuma concreta. Nota para o futuro: a "dyadic gap condition" reduzida
a uma obstrução de fração contínua esparsa (Corolário 6.6 do paper) é
estruturalmente parecida com a técnica que testamos em H-057 (frações
contínuas de `log₂3` aplicadas à exclusão de ciclos) — mesma ferramenta
clássica, aplicada aqui a um problema diferente (descida, não exclusão
de ciclo). Não investigado a fundo; mencionar na síntese final se
relevante.

## Atualizações

- 2026-07-15: paper lido por completo (45 páginas), 5 partes
  verificadas computacionalmente, nenhum erro encontrado. `INDEX.md`
  atualizado (item 015: Lido=Sim, Corrigido=Sim [nada a corrigir],
  Implementado=Sim).
