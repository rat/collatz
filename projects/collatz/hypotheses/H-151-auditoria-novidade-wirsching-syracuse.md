# H-151: auditoria dirigida de novidade da ponte Wirsching-Syracuse

Status: fechada-inconclusiva quanto a prioridade, confirmada quanto a comparação textual

Criada: 2026-08-07

## Pergunta

As provas e identidades de H-133 e H-143 a H-148 já aparecem nas fontes
primárias ou em trabalhos posteriores localizáveis por busca dirigida?

## Fontes verificadas

1. G. J. Wirsching, *On the problem of positive predecessor density in
   3n+1 dynamics*, DCDS 9(3), 771-787 (2003), DOI
   `10.3934/dcds.2003.9.771`.
2. T. Tao, *Almost all orbits of the Collatz map attain almost bounded
   values*, Forum of Mathematics, Pi 10 (2022), e12,
   arXiv:1909.03562.
3. J. C. Lagarias, *The 3x+1 problem: an annotated bibliography, II
   (2000-2009)*, arXiv:math/0608208v6.
4. Buscas por título exato, notação dos geradores, condições `(?1)` e
   `(?2)`, Syracuse random variables, fixed cost, microcanonical e
   equivalence of ensembles.

## Comparação exata

Wirsching define `g_ell`, `p_ell` e registra

```text
e_ell = p_ell * g_ell,
ebar_ell = p_ell * gbar_ell.
```

Ele também registra a interpretação de `2*3^(ell-1) gbar_ell(k)` como
o número de distribuições em urnas limitadas. A passagem de `(?2)` para
`(?1)` é denominada Conjectura 1. A fonte não cancela as duas funções
geradoras nem estima a cauda da convolução. A bibliografia anotada de
Lagarias ainda descreve o artigo como contendo três conjecturas abertas.
Logo H-133 resolve exatamente uma implicação que a fonte publicada deixa
como conjectura.

Tao define a lei de Syracuse a partir de expoentes geométricos e prova
mistura 3-ádica em escalas finas. O artigo não usa os geradores de custo
fixo de Wirsching, não condiciona pela soma dos custos dobrados e não
formula a decomposição microcanônica de H-143. A busca dirigida não
encontrou uma fonte posterior que faça essa identificação.

As equivalências de ensembles de H-145 e H-146 são aplicações de um
mecanismo probabilístico padrão, condicionamento de somas independentes
e teorema local do limite, mas a aplicação aos geradores de Wirsching e
às projeções da lei de Syracuse não foi localizada. A desigualdade de
verossimilhança de H-147 é elementar depois da decomposição.

A barreira de H-148 usa a lei binomial negativa do custo geométrico e a
fatia crítica da WCC. Nenhuma das fontes verificadas calcula a taxa
`I(1+log_4 3)` ou o expoente `1.0109587219...`.

## Classificação

- H-133: prova textual de uma conjectura explicitamente aberta na fonte.
- H-143: síntese exata entre dois formalismos publicados, não localizada
  nas fontes pesquisadas.
- H-145/H-146: aplicação nova para este objeto de um princípio geral
  conhecido.
- H-147: consequência elementar nova da decomposição, com prioridade não
  estabelecida.
- H-148: barreira quantitativa não localizada nas fontes pesquisadas.

## Limite da auditoria

Ausência em busca não prova novidade mundial. A prioridade permanece
inconclusiva até revisão por especialista ou busca de citações mais
exaustiva. O paper deve enunciar os teoremas diretamente, citar as fontes
que fornecem os ingredientes e evitar expressões como "first known".
