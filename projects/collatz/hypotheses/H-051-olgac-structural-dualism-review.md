# H-051 — Revisão do paper #009 (Olgac, "Structural Dualism in Integer Architectures") — sem conteúdo específico de Collatz verificável

Status: revisão externa concluída — nota curta sem conteúdo matemático
substantivo específico de Collatz; alegação de prova de Goldbach fora
do escopo deste projeto
Criada em: 2026-07-14
Origem: paper baixado manualmente pelo diretor científico (item 009 da
coleção, `literature/papers/009_Structural-Dualism-Integer-Architectures.pdf`,
Enis Olgac, Böblingen, Alemanha, 3 páginas).

## O paper

"Technical Note: Structural Dualism in Integer Architectures" — nota
curta (3 páginas) que conecta, via analogia vaga, duas alegações
**anteriores do mesmo autor**, não incluídas nesta coleção e citadas
apenas como referências [3] e [4] (ambos preprints Zenodo
auto-publicados, sem revisão por pares): "The Canonical Triple-Graph"
(sobre Collatz) e **"The Proof Beyond Goldbach"** (alegando provar a
Conjectura de Goldbach inteira — um problema aberto há quase 300 anos).

## O que foi verificado

O único conteúdo específico de Collatz nesta nota (Definição 2.1,
"Localized Stranger Invariant" — a afirmação de que "ramos" da árvore
reversa do Collatz enraizados em ímpares distintos não se sobrepõem) é
uma **tautologia**: consequência direta e trivial de todo inteiro
positivo ter exatamente uma parte ímpar (fatoração única de potências
de 2) — não é um resultado novo, apenas uma reformulação vistosa de um
fato imediato. Confirmado computacionalmente para 200.000 inteiros
(`experiments/E-051-olgac-structural-dualism-check/`): zero violações,
como esperado por construção.

## Por que não avaliamos o resto do paper como "correto" ou "incorreto"

O Teorema 2.2 ("Lattice Inversion") e o Teorema 3.3 ("Hard Physical
Boundary Fact") são inteiramente sobre a Conjectura de **Goldbach**,
não Collatz — fora do escopo deste projeto/laboratório. Além disso, a
"prova" do Teorema 3.3 não alcança o padrão mínimo de rigor matemático
para ser sequer avaliável formalmente: usa linguagem descritiva/física
("physical collision", "topologically trapped", "retaining wall",
"monotone path tracing the lower sublevel envelope") sem definir
precisamente os objetos matemáticos envolvidos (que caminho exatamente?
sobre qual conjunto? por que a interseção é garantida e não apenas
plausível?). Não é uma questão de "encontramos um erro" — é que não há
argumento matemático suficientemente preciso para testar.

## Sinal de alerta

A referência [4] ("The Proof Beyond Goldbach: Deterministic Navigation,
Bounded Active Zones, and Boundary Anchors over a Complete Lattice")
alega ter provado inteiramente a Conjectura de Goldbach — uma alegação
extraordinária, publicada apenas como preprint Zenodo auto-publicado,
sem qualquer verificação externa conhecida. Combinado com a linguagem
não-rigorosa do Teorema 3.3 desta nota (que se apoia diretamente nessa
alegação), isso é consistente com um padrão de escrita prolífica de
"technical notes" curtas conectando alegações cada vez mais grandiosas
entre si, citando majoritariamente o próprio trabalho anterior — sinal
de alerta similar (embora sobre problema diferente) ao já observado
noutros papers desta coleção.

## Novas hipóteses?

Nenhuma. Não há conteúdo matemático específico de Collatz nesta nota
além da tautologia já discutida.

## Atualizações

- 2026-07-14: paper lido por completo (3 páginas), único conteúdo
  específico de Collatz confirmado como tautológico
  (`experiments/E-051-olgac-structural-dualism-check/`). Flags
  atualizadas em `literature/papers/INDEX.md` (item 009: Lido=Sim,
  Corrigido=Sim [nada específico de Collatz a corrigir],
  Implementado=Sim).
