# E-049 — Verificação do paper #007 (Kazunobu Hikawa, "Parity Vector Structures")

## Objetivo

Verificar "Finite-Dimensional Combinatorial and Arithmetic Structures
of Parity Vectors for the Accelerated Collatz Map" (Kazunobu Hikawa,
34 páginas). Paper puramente combinatório sobre "vetores de paridade"
(strings binárias que codificam a sequência de passos ímpar/par do
mapa acelerado), classificados por comprimento k e peso de Hamming d.
Repetidamente honesto: "these finite-dimensional results do not by
themselves determine the existence or nonexistence of an infinite
non-convergent trajectory... remain an open problem."

## O que fizemos

1. **Teorema 3.2** (bijeção explícita Φ:U(d)→J(d+1), identidade
   X(d+1)=W(d)): confirmado por força bruta para d=1..7 — geramos
   U(d) e J(d+1) diretamente por peso (via combinações, evitando
   enumerar todos os 2^(k-1) vetores) e confirmamos que a imagem de Φ
   aplicada a TODO U(d) coincide exatamente (como conjunto) com J(d+1).
2. **Teorema 5.2** (rigidez 2-ádica): confirmado em 2000 pares
   aleatórios de vetores de mesmo comprimento e mesmo peso, com
   aritmética exata (`fractions.Fraction`).
3. **Remark 5.3** (contraexemplo do próprio paper para pesos
   desiguais): confirmado que a fórmula realmente NÃO vale nesse caso,
   como o paper honestamente antecipa.
4. **Reimplementação independente do Algoritmo 1** (programação
   dinâmica): reproduz exatamente os valores de W(k) e W(d) das
   Tabelas 1-2 do paper (k=1,10,100; d=1,2,5,10,20 — todos batem
   exatamente, dentro do alcance computável nesta sessão, k até 200).

## Nota de eficiência

A primeira versão do script tentou enumerar TODOS os vetores binários
de comprimento até 40 (2^39 ≈ 5,5×10¹¹) para depois filtrar por peso —
computacionalmente inviável, o processo em background falhou sem
produzir saída. Corrigido gerando vetores diretamente pelo peso exato
via `itertools.combinations` (escolhendo as posições dos 1s), reduzindo
o custo de exponencial para polinomial no comprimento.

## Resultado

**Nenhum erro encontrado** em nenhuma reivindicação testada. Paper de
alta qualidade combinatória, honesto sobre o escopo limitado dos seus
resultados (nada sobre a conjectura em si). Declara uso de IA generativa
apenas para prosa/estrutura, com responsabilidade final do autor.

Ver `hypotheses/H-049-hikawa-parity-vector-structures-review.md`.

## Como rodar

```
/home/rat/.venv/bin/python3 experiment.py
```
