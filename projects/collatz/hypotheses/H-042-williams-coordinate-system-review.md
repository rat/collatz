# H-042 — Revisão do paper #014 (Williams, "A Coordinate System for Collatz Dynamics") — sem erros encontrados

Status: revisão externa concluída — paper de boa qualidade, ambos os
teoremas centrais confirmados corretos
Criada em: 2026-07-14
Origem: quarto paper priorizado da coleção (item 014, local,
arXiv:2607.01718).

## O paper

"A Coordinate System for Collatz Dynamics" — Jennifer Williams,
School of Electronics and Computer Science, University of
Southampton, Reino Unido. Qualidade acadêmica claramente superior aos
itens anteriores: afiliação institucional real e verificável,
literatura extensa e genuína (Applegate-Lagarias, Barina — já
catalogado por nós —, Bateman-Horn, Blecksmith-McCallum-Selfridge,
Flatto, Guy, Kannan-Ganesa Moorthy, Knight 2026, Lagarias ×3, Mahler,
OEIS, Ren), código público no GitHub
(`github.com/rhoposit/collatz-coordinate-system`), e uma **declaração
explícita de uso de IA generativa** (Claude Opus 4.8, usado para
rascunhar/formatar, com verificação humana integral declarada) —
prática exemplar de transparência. O paper ainda agradece a um colega
(Ian Leary) por ter identificado um erro menor durante a revisão,
mostrando que passou por escrutínio real antes da publicação.

## O que foi verificado (ambos confirmados corretos)

- **Teorema 3.6** (dinâmica diagonal): para n=λ·2^a·3^b−1 com a≥2, o
  próximo ímpar na trajetória de Collatz é λ·2^(a−1)·3^(b+1)−1 —
  confirmado em 20.000 casos aleatórios
  (`experiments/E-042-williams-coordinate-system-check/`).
- **Teorema 4.1** (Zero-Prime Rows): linhas k≡2 mod4 com k≥6 do
  "esqueleto principal" L₁ (números da forma 2^a·3^b−1) não contêm
  primos — confirmado exaustivamente para 14 linhas (k=6 a 58, até 58
  elementos por linha). A exceção k=2 (contém os primos 3 e 5,
  explicitamente notada pelo próprio paper) foi confirmada. Controles
  (linhas fora desse padrão) contêm primos, como esperado.

**Nenhum erro encontrado.** Diferente dos itens 001 (H-039) e 004
(H-040), este paper passou em todas as verificações que fizemos.

## Conteúdo matemático (resumo)

O paper organiza os inteiros não-negativos via a fatoração 3-suave
única n+1 = λ·2^a·3^b (gcd(λ,6)=1), definindo "triângulos coroa" cujas
linhas são cadeias de Collatz de paridade alternada. Dentro de cada
"esqueleto" (conjunto de elementos ímpares com λ fixo), a dinâmica de
Collatz é um fluxo diagonal determinístico (a,b)→(a−1,b+1) — sem
nenhum insumo teórico-numérico — até atingir a fronteira a=1, onde a
dificuldade aritmética real da conjectura se concentra (a escolha de
qual esqueleto seguinte é alcançada depende da fatoração de
λ·3^(b+1)−1). O resultado de aplicação concreta (Teorema 4.1) usa essa
organização para provar que uma classe residual específica é
algebricamente livre de primos, e o Teorema 4.2 caracteriza essa
classe como a única (mod 4) com essa propriedade.

## Seções honestamente marcadas como não-provadas

O próprio paper separa claramente "Computational Observations" (Seção
6 — observações verificadas computacionalmente mas não provadas, ex:
"linhas acidentalmente livres de primos") de resultados provados, e
lista explicitamente "Open Problems" (Seção 7): dinâmica de saída de
linha (sem forma fechada conhecida), por que p=3 é especial entre
mapas pn+1 genéricos, se toda trajetória alcança λ=1 ("λ-recorrência"),
conexão com o resultado de Tao, e conexão com vetores de paridade de
Knight (2026).

## Novas hipóteses?

Nenhuma testada concretamente ainda, mas esta é a primeira linha de
organização genuinamente **diferente** da família mod-8/Steiner-word
(itens 004/005) que vimos até agora — baseada em fatoração 3-suave
(λ,a,b) em vez de resíduos mod8. Vale reconsiderar em sessão futura se
essa organização por peso (a+b) oferece algo novo para nossa própria
família de exclusão (H-007/H-014/H-022/H-028), mas isso é especulativo
por enquanto, não uma hipótese concreta.

## Atualizações

- 2026-07-14: paper lido por completo, ambos os teoremas centrais
  confirmados corretos, sem erros encontrados. Flags atualizadas em
  `literature/papers/INDEX.md` (item 014: Lido=Sim, Corrigido=Sim
  [nada a corrigir], Implementado=Sim).
