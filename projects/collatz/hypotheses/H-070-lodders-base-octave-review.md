# H-070 — Revisão do paper #099 (Lodders, "Selection Rules and Channel Structure in a Base–Octave Model of Collatz Dynamics") — ALEGAÇÃO DE PROVA refutada, Corollary 9.6.7 falso no próprio exemplo do paper

Status: revisão externa concluída — gap fatal localizado e falsificado
computacionalmente (Corollary 9.6.7 falha, inclusive no próprio exemplo
citado pelo paper); NÃO é uma prova válida
Criada em: 2026-07-15
Origem: item 099 da coleção (`literature/papers/INDEX.md`), já baixado
(`098_Selection-Rules-Channel-Structure-Base-Octave.pdf` — nome de
arquivo com numeração trocada no download, mas o conteúdo é do item 099;
o item 098 não tem PDF livre). **Alegação de prova completa** — requer
maior rigor de escrutínio (arXiv, não peer-reviewed).

## O paper

Lodders, K. (2026), *Selection Rules and Channel Structure in a
Base–Octave Model of Collatz Dynamics*, arXiv:2604.20181, 60 páginas.
Saint Louis, Missouri, EUA. Disclosure explícito de uso de IA (Claude)
como "collaborative tool" para estruturar argumentos e redigir o texto,
com o autor retendo "full responsibility for all mathematical claims and
proofs".

Este é o paper tecnicamente mais sofisticado entre as três alegações de
prova completa já revisadas neste projeto (comparar com
[[H-065-boyle-collatz-proof-review]] e [[H-068-yun-structural-proof-review]]):
não é um argumento informal com um gap isolado, mas um aparato
combinatório elaborado (decomposição base-octava, 16 regras de seleção,
sistema estendido de 128 estados, enumeração exaustiva de caminhos).

## Estrutura do argumento do paper

1. **Reformulação parity-controlled** (Seções 2-4): todo h=B+8(A-1),
   B∈{1,...,8} ("base"), A∈N ("índice de octava"); regra única
   h_{i+1}=((2s_i+1)(2k_i+s_i)+s_i)/2 unifica os casos par/ímpar.
2. **16 regras de seleção** (Seção 5): a transição de base B_i→B_{i+1}
   é determinada por (B_i, paridade de A_i) — 8 bases × 2 paridades = 16
   casos, exaustivamente derivados (Proposition 5.3).
3. **Canal de persistência B=7** (Seção 8): único capaz de sustentar
   crescimento (self-loop 7→7, ativo enquanto A permanece par).
   Proposition 8.4: o comprimento de qualquer tal "episódio" é
   ≤ v2(A_entrada) (valuação 2-ádica do índice de octava na entrada).
4. **Enumeração de "caminhos de retorno"** (Seção 9.6, Apêndice A2): um
   sistema estendido de 128 estados (B mais 4 bits de paridade
   adicionais de A) é construído; uma busca exaustiva enumera "22
   caminhos simples de retorno" entre a saída forçada 7→3 e a reentrada
   6→7, e afirma (Proposition 9.6.6) que todos têm "orçamento 2-ádico"
   ≤0.
5. **Corollary 9.6.7**: do item anterior, conclui que v2(A) na entrada
   de episódios *sucessivos* de persistência base-7 deve **decrescer
   estritamente** ao longo de qualquer trajetória.
6. **Theorem 9.6.8**: como v2(A) é um inteiro não-negativo que não pode
   decrescer indefinidamente, conclui que só finitos episódios de
   persistência podem ocorrer, e portanto toda trajetória está
   eventualmente confinada à bacia terminal {1,2} — **a conjectura de
   Collatz, provada**.

## O que está correto no paper

`experiments/E-070-lodders-base-octave-check/experiment.py`, 4 partes:

- **Parte 1**: a codificação base-octava e o mapa acelerado foram
  validados byte-a-byte contra o próprio exemplo do paper (trajetória
  completa de h1=7, página 22, 12 valores) e a Tabela 2 (h1=1..16) — 0
  falhas. Isto garante que as Partes 2-4 testam fielmente as definições
  do paper, não uma reconstrução própria divergente.
- **Parte 2**: as 16 regras de seleção (Casos 1-4, Seção 5) — 31.992
  pares (B,A) testados, 0 falhas. Máquina combinatória genuinamente
  correta.
- **Parte 3**: Proposition 8.4 (comprimento do episódio ≤ v2(A_entrada))
  — 515.342 episódios testados (N até 200.000), 0 falhas. Resultado
  correto: cada passo 7→7 exige A par e multiplica A por 3/2,
  consumindo exatamente um fator de 2 por passo — mecanismo aritmético
  simples e correto.

## Gap fatal — Corollary 9.6.7 é falso, no próprio exemplo do paper

**Parte 4** (resultado principal): testei diretamente, com inteiros
reais (sem depender de uma reconstrução manual do sistema de 128
estados do Apêndice A1 — uma tabela densa extraída de imagem/PDF,
propensa a erro de transcrição), se v2(A_entrada) de fato decresce
estritamente entre episódios sucessivos de persistência base-7, para
N até 500.000 (até 200.000 passos por trajetória).

**O próprio exemplo citado pelo paper na Introdução já é um
contraexemplo**: *"Well-known examples include sequences initiated at
n=27 and 31, which require substantially more steps to reach 1 than
neighboring initial values"* (página 2). Para n=27, os episódios de
persistência base-7 têm:

```
(A_entrada, comprimento) = [(4, 2), (22, 1), (40, 3), (114, 1)]
v2(A_entrada)             =  [2,      1,      3,      1]
```

O salto de v2=1 (episódio 2, A=22) para v2=3 (episódio 3, A=40)
**contradiz diretamente** "deve decrescer estritamente" — é um AUMENTO,
não uma diminuição. n=31 tem exatamente a mesma sequência de episódios
(mesma órbita a partir de um ponto comum) e portanto a mesma violação.

Isto não é um caso raro de borda: em escala, de 988.476 pares de
episódios sucessivos testados (312.547 trajetórias com ≥2 episódios,
até 18 episódios numa única trajetória), **560.682 (56,7%) violam a
alegação de decréscimo estrito**.

## Onde a cadeia lógica quebra

Rastreei manualmente a trajetória completa de n=27 e identifiquei que,
entre o fim do episódio 2 (saída forçada 7→3, A=33) e o início do
episódio 3 (reentrada 6→7, A=40), o "caminho de retorno" real passa por
uma visita intermediária à base B=7 com A **ímpar** (A=21, um mero
"pass-through" que a própria Seção A2.2(iii) do paper permite como
estado intermediário admissível, já que só exclui estados no "conjunto
de persistência" B=7∧A-par — não qualquer visita a B=7). Isto está em
tensão com o procedimento de enumeração descrito em A2.3 ("Paths are
terminated upon first re-entry into base 7"), que sugere que QUALQUER
toque em B=7 deveria encerrar o caminho — uma inconsistência interna
entre duas partes do próprio Apêndice A2. Não tentei reconstruir o
sistema de 128 estados completo para determinar se isso significa que a
enumeração dos "22 caminhos" não é exaustiva (existe um 23º caminho não
listado) ou se a fórmula de "orçamento 2-ádico" (Definição 9.6.2) não é
uma proxy fiel da mudança real de v2(A) através de atualizações afins
compostas — qualquer uma das duas quebra a cadeia Proposition
9.6.6→Corollary 9.6.7→Theorem 9.6.8, e a violação direta e concreta
(n=27) já demonstra isso sem precisar decidir qual.

**Nota de metodologia**: uma tentativa inicial de recalcular o
"Net_Budget" do paper (Definição 9.6.2) manualmente sobre o caminho real
de n=27 produziu um valor aparentemente "compatível" (≤0), mas essa
reconstrução não foi validada contra a Tabela A2 do próprio paper (uma
checagem rápida mostrou que minha contagem de "passos ímpar-base com A
ímpar" não reproduz a coluna `v2_Max_Gain` tabulada — ex. o Path 1 do
paper tem Odd_Steps=2 mas v2_Max_Gain=1) — por isso essa reconstrução
foi **descartada** desta revisão. A refutação acima depende apenas da
definição explícita de "episódio de persistência base-7" e da
desigualdade explícita do próprio Corollary 9.6.7, ambas testadas por
computação direta com inteiros reais — não da minha reconstrução do
Apêndice A2.

## Por que isso é notável

O paper é irônico neste ponto: o monovariante proposto (v2(A) decrescer
estritamente entre episódios) falha exatamente no par de números (n=27,
31) que o próprio paper invoca na Introdução para motivar a necessidade
de uma análise estrutural mais cuidadosa.

## Novas hipóteses?

Nenhuma. Item descartado como alegação de prova inválida, com o gap
localizado e demonstrado computacionalmente usando o próprio exemplo do
autor.

## Atualizações

- 2026-07-15: paper lido por completo (60 páginas + 2 apêndices), gap
  fatal localizado (Corollary 9.6.7 falso) e demonstrado com o próprio
  exemplo do paper (n=27); confirmado em escala (56,7% de violação entre
  pares de episódios, N até 500.000). Partes 1-3 do aparato do paper
  (codificação, 16 regras de seleção, Proposition 8.4) confirmadas
  corretas. `INDEX.md` atualizado (item 099: Lido=Sim, Corrigido=Não
  [alegação de prova refutada], Implementado=Sim).
