# E-051 — Verificação do paper #009 (Olgac, "Structural Dualism in Integer Architectures")

## Objetivo

Verificar "Technical Note: Structural Dualism in Integer Architectures"
(Enis Olgac, 3 páginas). Nota curta conectando duas alegações
anteriores do mesmo autor (não incluídas nesta coleção, citadas apenas
como referências [3]/[4], ambos preprints Zenodo auto-publicados): uma
sobre Collatz ("Canonical Triple-Graph") e outra alegando **provar a
Conjectura de Goldbach inteira** ("The Proof Beyond Goldbach").

## O que fizemos

O único conteúdo específico de Collatz nesta nota (Definição 2.1,
"Localized Stranger Invariant" — ramos da árvore reversa enraizados em
ímpares distintos não se sobrepõem) é uma **tautologia**: consequência
direta de todo inteiro positivo ter exatamente uma parte ímpar (via
fatoração única de potências de 2), não um resultado novo. Confirmamos
isso computacionalmente para 200.000 inteiros (0 violações, como
esperado por construção).

## Resultado

O restante do paper (Teorema 2.2 "Lattice Inversion", Teorema 3.3 "Hard
Physical Boundary Fact") é inteiramente sobre a Conjectura de
**Goldbach** — fora do escopo deste projeto (Collatz) — e não alcança
rigor matemático suficiente para ser avaliado como prova: usa linguagem
descritiva não-rigorosa ("physical collision", "topologically trapped",
"retaining wall") sem definir precisamente os objetos envolvidos.

**Este não é um paper sobre Collatz com conteúdo específico
verificável** — é uma nota curta conectando duas alegações
extraordinárias do mesmo autor através de analogia vaga, sem rigor
matemático real em nenhuma das duas pontas.

Ver `hypotheses/H-051-olgac-structural-dualism-review.md`.

## Como rodar

```
/home/rat/.venv/bin/python3 experiment.py
```
