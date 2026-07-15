# H-081 — Revisão: Spencer, "Finite Block Exhaustion and Rooted Occupancy in the Inverse Collatz System" (2025)

Status: revisão externa concluída — **ALEGAÇÃO DE PROVA COMPLETA REFUTADA** (mesma anatomia de erro do item 109/H-079, confirmada computacionalmente com um exemplo concreto)
Criada em: 2026-07-15
Origem: item 022 da coleção de literatura (`literature/papers/INDEX.md`),
arquivado em 2026-07-15 (academia.edu).

## O paper

Michael E. Spencer. "Finite Block Exhaustion and Rooted Occupancy in the
Inverse Collatz System: A No-Alternative Proof via Ternary Counters,
Primitive Carry, and Forced Thread Displacement", academia.edu, 2025 —
**sem revisão por pares**. **Alega prova completa** da Conjectura de
Collatz. Constrói a mesma árvore reversa de Collatz usada por este
projeto (H-018) e pelo item 109 (Getachew, já refutado em H-079):
T(m)=(3m+1)/2^{v₂(3m+1)} direto, R(n;k)=(2^k n−1)/3 reverso.

Aparato mais sofisticado que o item 109: um "contador ternário
enraizado" que conta, por escala finita J, quantas classes residuais
mod 2·3^J são "ocupadas" por algum ponto da árvore reversa, com
identidades de cardinalidade exatas (|W_J|=3^J, |C_J|=2^J,
|O_J|=3^J−2^J) apoiadas por uma formalização parcial em Lean (lista de
lemas verificados na Seção 17 — mas essas verificações cobrem só as
identidades de cardinalidade combinatória, não a alegação final do
Teorema 15.3).

## O furo lógico central (mesma anatomia do item 109, mecanismo diferente)

O "Teorema 14.2" (Rooted occupancy) e o "Corollary 12.3" (Finite scale
primitive surjectivity) provam que, em cada escala finita J, toda
**classe residual** primitiva mod 2·3^J é ocupada por algum ponto da
árvore — uma afirmação sobre **resíduos** (objetos abstratos, cada um
representando uma progressão aritmética infinita de inteiros), não
sobre inteiros específicos. O "Teorema 15.3" (Odd convergence) então
conclui, sem justificar a passagem, que **todo inteiro ímpar específico
m** tem um "endereço reverso enraizado" finito — ou seja, salta de
"o resíduo de m está ocupado em toda escala J" para "m em si é
alcançado pela construção real da árvore".

**Esses dois enunciados não são equivalentes**: "a classe residual de m
mod 2·3^J está ocupada" só diz que *algum* inteiro naquela progressão
aritmética infinita foi alcançado — pode ser um representante
completamente diferente de m, arbitrariamente maior. O paper nunca
mostra a conexão (nenhuma proposição trata da relação entre "resíduo
ocupado" e "valor exato atingido").

## Verificação computacional

`experiments/E-081-spencer-2025-review/experiment.py`:

1. **Identidade de cardinalidade** (Teorema 6.3, |O_J|=3^J−2^J): pura
   combinatória de contagem de palavras num alfabeto ternário —
   confirmada correta (é definicional, não depende de nada sobre
   Collatz). **8 casos (J=1 a 8), 0 falhas.**
2. **Demonstração direta do gap com um exemplo concreto**: construímos
   a árvore reversa **real** a partir da raiz 1 (usando R(n;k) do
   próprio paper) até profundidade J=6 e J=8, e verificamos se o valor
   27 (escolha arbitrária, qualquer ímpar pequeno serviria) é
   alcançado **exatamente**.
   - Em **ambas** as profundidades, 27 **não** é atingido exatamente.
   - Mas a **classe residual** de 27 (mod 2·3^J) **está** representada
     por outros elementos da árvore construída — por exemplo, em J=6,
     os representantes encontrados foram 1267029, 1372005, 2760021,
     23379057, 43910613 (todos ≡27 mod 1458), **nenhum igual a 27**.
   - Isso confirma exatamente o gap suspeitado: "ocupação de classe
     residual" é uma alegação muito mais fraca que "alcançabilidade do
     valor exato", e o paper nunca fecha essa distância.

## Avaliação geral

**Não é uma prova válida** — mesma anatomia de erro do item 109
(Getachew, H-079), aplicada por um caminho combinatório diferente
(contagem de classes residuais em vez de "pai = mapa direto"). O
aparato técnico (contador ternário de seis casos, threads de deslocamento
diádico, formalização parcial em Lean) é genuíno e as identidades de
cardinalidade que ele estabelece estão corretas — mas nenhuma delas
implica a conclusão final (Teorema 15.3/16.2), que continua sendo
exatamente a Conjectura de Collatz, agora disfarçada em linguagem de
"exaustão de alternativas" sobre classes residuais. É um caso
particularmente elaborado de petição de princípio: o aparato é
complexo o suficiente para parecer substantivo, mas a lacuna lógica
central (resíduo ocupado ⇏ valor específico atingido) nunca é
endereçada nem mencionada.

## Atualizações

- 2026-07-15: revisão externa concluída. PDF lido por completo (13
  páginas). Identidade de cardinalidade confirmada correta (é
  definicional). Furo lógico central identificado e confirmado
  computacionalmente com um exemplo concreto (n=27): a classe residual
  de 27 está ocupada na árvore real construída até profundidade 6 e 8,
  mas 27 em si nunca é atingido — os representantes reais são muito
  maiores (ordem de 10⁶ a 10⁸). Adicionar entrada em
  `literature/unverified-proof-claims.md`.
