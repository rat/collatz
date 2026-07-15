# H-060 — Revisão do paper #028 (Csikos, "Continuous Multi-Component DAG-ness") — paper de teoria de grafos; conteúdo Collatz-específico correto exceto direção do ciclo

Status: revisão externa concluída (escopo limitado ao conteúdo
Collatz-específico) — correto, exceto um erro de descrição textual sem
consequência numérica
Criada em: 2026-07-15
Origem: item 028 da coleção (`literature/papers/INDEX.md`), já baixado
(`027_Continuous-Multi-Component-Measure-DAG-ness.pdf`).

## O paper

Csikos, E. (2026), *A Continuous Multi-Component Measure of Directed
Acyclicity (DAG-ness)*, arXiv:2606.22205, 22 páginas. Binghamton
University + Moravian University. **Não é um paper sobre Collatz** —
é um paper de teoria de grafos/ciência de redes, propondo uma métrica
contínua de 4 componentes (`A`,`F`,`M`,`S`) para quantificar "o quão
próximo" um grafo dirigido arbitrário está de ser acíclico. Collatz
aparece apenas na Seção 5.2 ("The Collatz Graph"), meia página, como
**um exemplo ilustrativo entre vários** (Kaprekar 6174, Collatz, grafos
sintéticos de diagnóstico) — nenhuma alegação é feita sobre a
conjectura em si.

## Escopo desta revisão

Dado que o aparato geral (Seções 2-4: SCCs, MFAS, raio espectral,
framework de 4 componentes) não é específico de Collatz, esta revisão
cobre **apenas** o conteúdo Collatz-específico (Seção 5.2), não o
framework de teoria de grafos em si (fora do escopo deste projeto —
seria uma revisão de teoria de grafos, não de Collatz).

## O que foi verificado

`experiments/E-060-csikos-dag-ness-check/experiment.py`, três partes:

1. Restringindo `T(n)=n/2` (par) `/3n+1` (ímpar) — o mapa PADRÃO, não
   acelerado, exatamente como definido pelo paper — aos primeiros 2228
   inteiros positivos: confirmado que existe exatamente um SCC cíclico,
   `{1,2,4}` (o ciclo trivial), e que todo `n=1..2228` o atinge. 0 casos
   não resolvidos. Consistente com verificação exaustiva de Collatz
   muito além deste intervalo, já publicada na literatura.
2. Direção do ciclo — ver achado abaixo.
3. Aritmética do `D(G)=0.875` (Tabela 1, linha "Collatz") — confere
   exatamente com os componentes `A=1.000,F=1.000,M=0.999,S=0.500`
   citados. `M(G)=1-2/2227=0.999102` (arredonda para 0.999) também
   confere com a fórmula do próprio paper.

## Achado — direção do ciclo invertida no texto (sem consequência numérica)

O paper escreve (Seção 5.2): *"The only cyclic SCC is the well-known
`1→2→4→1` cycle."* Mas pelas arestas reais do mapa `T(n)` **definido
no próprio paper**: `T(1)=4`, `T(4)=2`, `T(2)=1` — ou seja, as arestas
são `1→4`, `4→2`, `2→1`, e o ciclo percorrido é **`1→4→2→1`**, não
`1→2→4→1` como escrito. Nenhuma das três arestas alegadas (`1→2`,
`2→4`, `4→1`) existe de fato sob `T`.

**Não afeta nenhum resultado do paper**: `A(G)`, `F(G)`, `M(G)`, `S(G)`
e `D(G)` dependem apenas do tamanho do ciclo (3 nós) e de propriedades
espectrais/estruturais — nenhum deles depende da ordem em que o ciclo é
descrito em palavras no texto. É um erro de descrição textual (o autor
escreveu o ciclo na ordem errada), não um erro de cálculo ou de
definição.

## Por que isso não é uma crítica de peso

O paper não faz nenhuma alegação sobre a Conjectura de Collatz — usa o
grafo de Collatz restrito a um intervalo pequeno (`n≤2228`) e já
conhecido apenas como exemplo ilustrativo de sua métrica de teoria de
grafos, junto com o grafo de Kaprekar e grafos sintéticos. O erro
encontrado é cosmético (direção do ciclo trocada na descrição textual),
do tipo que revisão por pares tipicamente pega, e não compromete
nenhuma conclusão do paper.

## Novas hipóteses?

Nenhuma. O framework de "DAG-ness" em si (fora de escopo) não parece
oferecer ferramenta nova para o problema central deste projeto (busca
de ciclos não-triviais, distribuição de stopping times, etc.) — ele
mede uma propriedade diferente (quão "quase acíclico" um grafo dirigido
arbitrário é), não relacionada às perguntas que este projeto investiga.

## Atualizações

- 2026-07-15: conteúdo Collatz-específico (Seção 5.2) lido e verificado
  computacionalmente. `INDEX.md` atualizado (item 028: Lido=Sim,
  Corrigido=Sim, Implementado=Sim — com ressalva de escopo limitado ao
  conteúdo Collatz-específico).
