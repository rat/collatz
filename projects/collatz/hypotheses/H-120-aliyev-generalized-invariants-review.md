# H-120 — Aliyev, "Existence of Invariants in Periods of Generalized Collatz Sequences" (2023): teorema correto, confirmado por teste de estresse independente; um erro de copy-paste sem consequência

Status: sem erro matemático (teorema verificado); erro de digitação encontrado e citável
Criada em: 2026-07-17
Origem: item 121 do INDEX.md (IEEE PCI 2023).

## Enunciado

Generaliza 3x+1 para S_k(x)=(px+k)/q e T(x)=x/q, p,q coprimos
quaisquer. Para uma composição cíclica de n T's e m S's formando órbita
periódica RACIONAL x_0,...,x_{n+m-1}, prova existência de inteiros
(a,b) tais que combinações p^a·x_i ± p^σ·x_{i+b} são sempre inteiras,
independente da rotação escolhida como início.

## Avaliação

Não é alegação sobre a conjectura clássica em inteiros positivos — é
estrutural/algébrico sobre órbitas racionais periódicas de um mapa
afim generalizado (muda multiplicador E divisor, trabalha com
racionais). Não faz nem insinua alegação sobre Collatz clássico.

**Reprodução computacional** (Python, `Fraction`): Exemplo 1 do paper
(p=5,q=2) — todos os x_i (223/3, 88/3, 176/3, 352/3, 139/3, 278/3,
556/3) e as 7 verificações do invariante (665,264,525,1050,417,835,
1660) batem exatamente. Exemplo 2 (p=11,q=5) — x_i (9/4,45/4,19/4) e as
3 verificações finais (36,176,77) batem exatamente.

**Erro de copy-paste encontrado** (Exemplo 2): o texto diz
"U_i=2^i/3" e "11¹·U_0+U_1=3 é inteiro", mas pela definição do paper
(U_i=q^i/(q^{n+m}−p^m)), para este exemplo (q=5,n=1,m=2) deveria ser
U_i=5^i/4 (não 2^i/3, reciclado do Exemplo 1 onde q=2,n=4,m=3). Com
valores corretos: 11¹·(1/4)+5/4=4 (ainda inteiro, só "4" não "3" como
escrito). Erro de digitação que não compromete o teorema.

**Teste de estresse independente**: 200 composições aleatórias
(p,q coprimos 2-9, comprimento 2-6, operações/k's aleatórios),
resolvido ponto fixo racional, testado se o par (a,b) produz
invariância para TODO i. Resultado: **0 violações em 200 testes** —
confirmação computacional forte de que o Teorema 1 (e por simetria o
Teorema 2) está matematicamente correto.

## Relevância para a investigação atual

Baixa — generalização diferente da nossa (muda p E q, foca em
estrutura algébrica de ciclos racionais, não densidade/tempo de parada
de trajetórias inteiras). Útil só para não confundir com a
generalização qx+1 do projeto.

## Veredito

Teorema central correto, verificado independentemente com 200 casos
aleatórios sem violação. Um erro de digitação sem consequência no
Exemplo 2, citável numa revisão formal.
