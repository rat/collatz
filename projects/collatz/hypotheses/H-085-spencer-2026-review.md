# H-085 — Revisão: Spencer, "Rooted Surjectivity from the Invariant E/O Refinement System" (2026)

Status: revisão externa concluída — ALEGAÇÃO DE PROVA COMPLETA, veredito: **não fecha logicamente** (lacuna de rigor identificada), mas **sem contraexemplo computacional encontrado** (diferente do item 022 do mesmo autor)
Criada em: 2026-07-15
Origem: item 037 da coleção de literatura (`literature/papers/INDEX.md`),
arquivado em 2026-07-15 (academia.edu).

## O paper

Michael E. Spencer — **mesmo autor do item 022** (já refutado com
contraexemplo direto em H-081). **Alega prova completa** da Conjectura
de Collatz, sem revisão por pares (academia.edu).

Usa o mapa acelerado T(m)=(3m+1)/2^{v₂(3m+1)} e seu inverso
R(n;k)=(2^k·n−1)/3. Estrutura importante e **diferente** da árvore de
H-018/item 022: como T "acelera" removendo todos os fatores de 2 de uma
vez, um mesmo n pode ter **infinitos predecessores diferentes** sob T
(um para cada k admissível da paridade correta — k=1,3,5,... ou
k=2,4,6,...), não apenas 2 como na árvore de duplicação padrão.
Confirmado algebricamente e computacionalmente: por exemplo, T(3)=T(13)=
T(53)=5 (via k=1,3,5 respectivamente).

## Investigação e mudança de avaliação inicial

Dado que é o mesmo autor do item 022 (H-081, onde encontrei um furo
claro: "classe residual ocupada" ≠ "inteiro específico atingido",
confirmado com contraexemplo concreto em n=27), a suspeita inicial era
a mesma anatomia de erro. **A investigação computacional não confirmou
essa suspeita da mesma forma.**

Construí a árvore reversa real a partir de n=1 (usando R(n;k) com k
variando em toda a paridade admissível) e testei cobertura de inteiros
ímpares pequenos, aumentando o orçamento computacional progressivamente:

| magnitude_max | orçamento (nós) | cobertura até 1000 | cobertura até 10.000 | cobertura até 50.000 |
|---|---|---|---|---|
| 1e6 | 2M | 500/500 | 4986/5000 | — |
| 1e7 | 8M | 500/500 | 5000/5000 | — |
| 3e7 | 10M | — | 5000/5000 | 24994/25000 |

**Diferente do item 022**: os "faltantes" em cada rodada **não são um
gap persistente** — verifiquei individualmente vários deles (9663,
26623) e confirmei que **cada um converge exatamente à raiz 1** quando
sigo a cadeia de predecessores únicos até profundidade suficiente (66 a
113 passos, com picos de magnitude de ~9 a ~35 milhões) — exatamente o
comportamento esperado se a árvore real cobre cada valor exato, e o
"faltante" era só limitação de orçamento computacional daquela rodada
específica, não uma lacuna estrutural. Isso é o oposto do que encontrei
no item 022, onde aumentar a profundidade **nunca** trazia o valor
exato, só representantes cada vez maiores da mesma classe residual.

## A lacuna de rigor que permanece (não confirmada nem refutada computacionalmente)

Apesar da evidência empírica favorável, uma leitura cuidadosa da
demonstração revela uma passagem não justificada: o **Lemma 11.1**
(propagação de gap) e o **Teorema 14.1** ("No invariant scaling gap")
argumentam sobre a ocupação de **classes residuais** D_k (definidas por
v₂(3m+1)=k — conjuntos infinitos, cada um uma progressão aritmética
única, pelo Lemma 6.2). Mas o **Teorema 14.2** conclui algo mais forte:
que **cada elemento individual** abaixo de 2^L está no componente
enraizado R_1 — não apenas que a classe/rail correspondente está
"ocupada" (o que só exigiria que *algum* elemento da classe estivesse
em R_1). A passagem de "a classe D_k está ocupada" para "todo elemento
de D_k pertence a R_1" nunca é justificada explicitamente — o Lemma
11.1 fala em termos de "classe" e "classe filha", não de elementos
individuais, então a conclusão do Teorema 14.2 é mais forte do que o
que os lemas anteriores demonstram.

**Isto é uma lacuna de rigor genuína** — mas, diferente do item 022,
não encontrei um contraexemplo computacional que a explore. É possível
que a lacuna seja preenchível (talvez a estrutura específica das
classes D_k, sendo progressões aritméticas de passo fixo 2^{k+1}, force
de fato "tudo ou nada" — todos os elementos ocupados ou nenhum), mas o
paper não demonstra isso, e eu não tentei provar ou refutar essa
propriedade adicional (estaria além do escopo de uma revisão).

## Avaliação geral

**Veredito honesto e diferenciado do item 022 do mesmo autor**: a
demonstração, como escrita, tem uma lacuna de rigor real na passagem
entre nível de classe residual e nível de elemento individual (Teorema
14.1→14.2) — não é uma prova completa e válida como está. Mas,
diferente do item 022 (onde um contraexemplo concreto e persistente
refuta a alegação central diretamente), aqui a evidência computacional
disponível é **consistente** com a conclusão final do paper (cobertura
completa observada em todas as escalas testadas, com os aparentes
contraexemplos se resolvendo como limitações de orçamento, não
estruturais). Não afirmo que o resultado esteja correto (a lacuna de
rigor é real e não foi fechada), nem que esteja refutado (não encontrei
um contraexemplo). Isso é diferente de simplesmente repetir "não é uma
prova válida" — é reportar com precisão o que a investigação mostrou:
uma lacuna lógica identificada, sem evidência computacional que a
explore.

## Atualizações

- 2026-07-15: revisão externa concluída. PDF lido por completo (12
  páginas). Suspeita inicial (mesma anatomia de erro do item 022, mesmo
  autor) foi testada e **não confirmada** — a evidência computacional é
  distinta e favorável à alegação do paper (cobertura completa, sem
  gap persistente). Identificada uma lacuna de rigor diferente (Teorema
  14.1→14.2, passagem classe→elemento não justificada), reportada com
  honestidade como não resolvida, nem confirmada nem refutada
  computacionalmente. Este é um caso onde a primeira suspeita (baseada
  em precedente do mesmo autor) foi corrigida pela investigação real —
  documentado para reforçar a disciplina de nunca aplicar um veredito
  por analogia sem verificar.
