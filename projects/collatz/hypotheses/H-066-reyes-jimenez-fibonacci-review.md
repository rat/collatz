# H-066 — Revisão do paper #057/089 (Reyes Jiménez, "A Fibonacci theorem for Collatz trajectories via modular graph structure") — resultado exato confirmado, sem erros

Status: revisão externa concluída — 11 partes verificadas
computacionalmente (incluindo o resultado central, Teorema 4.7), 0
falhas
Criada em: 2026-07-15
Origem: item 057 da coleção (`literature/papers/INDEX.md`), já baixado
(`056_Fibonacci-theorem-Collatz-modular-graph.pdf`). Item 089 é
duplicata confirmada do mesmo paper.

## O paper

Reyes Jiménez, M-A. (2026), *A Fibonacci theorem for Collatz
trajectories via modular graph structure*, arXiv:2606.02621
[math.NT], 24 páginas. Doutorando na Universitat Politècnica de
Catalunya (UPC Barcelona), orientador Jaume Franch Bullich (agradecido
nominalmente).

Diferente da maioria dos papers processados nesta sessão, este é
**pesquisa matemática genuína e tecnicamente sofisticada** (não uma
tentativa amadora de resolver a conjectura clássica, nem uma alegação
de prova): prova um resultado **combinatório exato e incondicional**
sobre um objeto **finito** bem definido — o grafo de transição módulo
6 do mapa acelerado de Collatz `T(n)=n/2` (par) `(3n+1)/2` (ímpar).

**Resultado central (Teorema 4.7)**: exatamente `F(m+1)` dos `2^m`
inteiros ímpares em `{1,...,2^m}` têm órbita que evita o resíduo 4
mod 6 nos passos `2,...,m`, onde `F` é a sequência de Fibonacci
(`F(1)=F(2)=1`). A prova é via um argumento espectral: o subgrafo que
evita o vértice 4 tem raio espectral `φ=(1+√5)/2` (razão áurea),
contra raio espectral `2` do grafo efetivo completo — essa "lacuna
espectral" `φ/2 < 1` é o que força a contagem a ser **exatamente**
Fibonacci, não apenas aproximadamente.

O paper é explícito sobre o escopo: **não resolve nem se aproxima de
resolver** a conjectura clássica — a conclusão lista três perguntas em
aberto sobre generalizações do próprio resultado combinatório.

**Conexão com trabalho anterior deste projeto**: antes mesmo de
conhecermos este paper, [[H-027-mod6-corollary-closes-h008-even-half]]
(2026-07-13) já havia verificado independentemente a Proposição 2.8
(tabela de transição mod 6, resíduo 4→{2,5}) como o mesmo mecanismo
algébrico usado numa prova própria deste projeto — uma coincidência
estrutural entre duas investigações independentes, já documentada.

## O que foi verificado

`experiments/E-066-reyes-jimenez-fibonacci-check/experiment.py`, onze
partes, **0 falhas**:

1. **Lemma 2.1** (fórmula fechada + lei recursiva do resíduo
   corretivo `R`) e **Exemplo 2.2** (`n=11,m=4`: trajetória
   `11→17→26→13→20`, `R=23`) — reproduzidos exatamente; fórmula
   fechada vs. definição direta testada em 3.289 casos.
2. **Proposição 2.3** (bijetividade e periodicidade de `Φ_m`) —
   confirmada para `m=1..14`.
3. **Lemma 2.4** (antissimetria) e **Lemma 2.5** (translação
   generalizada) — 6.608+ casos, confirmados.
4. **Proposição 2.8** (tabela de transição mod 6) — reverificação
   independente (já feita antes em H-027).
5. **Proposição 3.1** (decomposição em componentes fortemente conexas:
   `{0},{3},{1,2,4,5}`) e **Proposição 3.3** (enumeração COMPLETA dos
   6 ciclos simples do grafo, nenhum de comprimento ≥4) — confirmadas
   via algoritmo de grafos.
6. **Cinco raios espectrais** (Proposições 3.4, 4.10, 4.11, 4.13,
   Teorema 4.15): `ρ(G')=2`, `ρ(H₄)=ρ(H₁)=φ≈1,618`, `ρ(H₅)=√2≈1,414`,
   `ρ(H₂)=1`, hierarquia `1<√2<φ<2` — confirmados via autovalores
   (numpy), incluindo a fórmula explícita de potência de matriz de
   Fibonacci (Proposição 4.10) para `n=1..14`.
7. **Corolário 4.5** (órbitas ímpares confinadas a `{1,2,4,5}` a
   partir do nível 2) — 200.000 inteiros ímpares testados, 0 exceções.
8. **Teorema 4.7 (RESULTADO PRINCIPAL)** — contagem de Fibonacci
   reproduzida por **força bruta exata** para `m=1` a `22`
   (`F(2)=1` até `F(23)=28.657`) — bate exatamente em todos os 22
   valores.
9. **Exemplo 4.8** (`m=4`: os 5 inteiros que evitam o vértice 4 e
   seus sufixos `(h₂,h₃,h₄)` exatos) — reproduzido literalmente.
10. **Teorema 4.1** (teorema do caminho modular, ação do deslocamento
    `+2^m`) e **Corolário 4.4** (rigidez de níveis `≥r+2`) —
    confirmados em milhares de casos.
11. **Proposição 4.18/Corolário 4.19** (distribuição de vértices em
    ciclos positivos) — verificados contra o único ciclo positivo
    conhecido de `T` (`n=1,m=2`, o ciclo trivial `1↔2`); busca
    computacional confirma que nenhum outro ciclo existe para
    `n₀=1..99.999`.

## Correções ao longo da verificação (erros próprios, não do paper)

Duas "falhas" apareceram inicialmente e foram corrigidas antes de
finalizar — ambas bugs do meu script, não do paper:

1. **Parte 5** (ciclos simples): meu algoritmo normaliza cada ciclo
   rotacionando para começar no vértice mínimo, mas eu havia
   hard-codado o conjunto esperado usando a notação literal do paper
   (que começa em vértices arbitrários, ex. "`2→1→2`") sem aplicar a
   mesma normalização. Corrigido normalizando ambos os lados antes de
   comparar — as sequências de vértices são idênticas, só descritas a
   partir de pontos de partida diferentes no mesmo ciclo.
2. **Parte 9** (Exemplo 4.8): erro de indexação off-by-one
   (`h[1:4]` em vez de `h[0:3]`) ao extrair `(h₂,h₃,h₄)` de uma lista
   que já começava em `h₂`. Corrigido; todos os 5 valores do exemplo
   batem exatamente após a correção.

## Resultado

**Nenhum erro matemático ou numérico encontrado.** Este é o paper de
maior rigor técnico revisado nesta sessão entre os itens desta fila —
consistente com ser pesquisa de doutorado genuína, não uma tentativa
amadora. Todas as definições, lemas, proposições, corolários e o
teorema central foram verificados exatamente, incluindo o exemplo
numérico explícito e a contagem de Fibonacci por força bruta até
`m=22`.

## Novas hipóteses?

Nenhuma concreta — mas vale registrar para a síntese final que este
projeto já tinha, de forma independente, tocado exatamente a mesma
estrutura de grafo mod 6 (via H-027), o que reforça que esse objeto
(a tabela de transição mod 6 do mapa acelerado) é um ponto de
convergência natural entre investigações distintas na literatura
Collatz.

## Atualizações

- 2026-07-15: paper lido por completo (24 páginas), 11 partes
  verificadas computacionalmente, incluindo reprodução exata do
  Teorema 4.7 (contagem de Fibonacci) para m=1 a 22. Dois bugs
  próprios de indexação/normalização corrigidos antes de finalizar.
  `INDEX.md` atualizado (itens 057 e 089 [duplicata]: Lido=Sim,
  Corrigido=Sim [nada a corrigir], Implementado=Sim).
