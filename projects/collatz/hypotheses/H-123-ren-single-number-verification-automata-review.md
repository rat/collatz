# H-123 — Ren et al., verificação de 2^100000-1 e autômato de classes residuais (2018/2019): computação correta, mas alegação central mal enquadrada; um bug de rotulação sem consequência

Status: computação correta; equivocação conceitual na alegação central (não erro matemático); bug de rotulação secundário encontrado
Criada em: 2026-07-17
Origem: itens 118 (IEEE SmartWorld 2018) e 122 (IEEE HPCC/SmartCity/DSS
2019) do INDEX.md — 122 cita e reusa números de 118.

## Enunciado

**Item 118**: algoritmos bit-a-bit (arquivo em disco em vez de memória)
para computar a trajetória de Collatz de UM número específico
extremamente grande (2^100000−1, ~30000 dígitos). Reporta retorno a 1
após 481603 aplicações de 3x+1 e 863323 aplicações de x/2.

**Item 122**: autômato baseado em classes de resíduo mod 2^m para
determinar antecipadamente segmentos de m+2 transformações a partir de
t=(x−3)/4 mod 2^m. Prova formalmente que a "Reduced Collatz
Conjecture" (∃p: CT^p(x)<x) é equivalente à conjectura original;
propõe "Collatz Tree Conjecture".

## Avaliação

**Item 118 — equivocação conceitual na alegação central (não erro
matemático)**: o título ("...Is True") e abstract enquadram o
resultado como extensão do "maior número verificado" (comparando com
verificações exaustivas de ~60 bits, Silva/Barina), mas isso confunde
duas categorias diferentes de afirmação: verificação EXAUSTIVA
(confirmar TODOS os inteiros abaixo de um limite) vs. checar UM único
inteiro específico, por maior que seja. Checar um número não avança a
fronteira exaustiva em nada — computação correta, significância mal
enquadrada.

**Verificação computacional feita nesta revisão**: reproduzida via
Python (arbitrary-precision) a trajetória de 2^k−1 para k=100, 500,
1000, 5000, 10000, 50000, 100000 — todos os valores batem exatamente
com a Tabela I do paper, incluindo o caso principal (U=481603,
D−U=381720, D=863323, razão=0,7926030). **Alegação numérica central
correta**.

Ponto secundário (item 118): a seção sobre "green mining"/PoW usando
Collatz como substituto de hash é especulativa e frágil — não aborda
que uma função de PoW precisa ser "one-way", propriedade que a
dinâmica de Collatz não obviamente possui.

**Item 122**: nenhuma alegação de prova da conjectura original. A
Proposição 2.4 (equivalência Reduced⇔Collatz) é prova válida
(argumento clássico de descida infinita, lógica verificada). A
"Collatz Tree Conjecture" é rotulada explicitamente como conjectura, e
é na prática uma reformulação de dificuldade equivalente à original —
honesto quanto a isso, não alega mais.

**Erro encontrado (item 122, apêndice)**: no código-fonte C, a fórmula
computada é `ratio=(d-u)/d` mas o `printf` rotula como
`"ratio=(d-u)/u=..."`. Confirmado numericamente (x=27: u=37,d=59;
(d−u)/u=0,5946 mas (d−u)/d=0,37288, e o valor impresso 0,3728814 bate
com (d−u)/d, não com o rótulo). Bug de rotulação sem efeito nos
resultados principais.

## Sobreposição

118↔122: item 122 cita 118 (ref. [4]) e reafirma no abstract/intro os
números exatos (481603, 863323 passos) — confirmado fiel aos números
já validados independentemente. Reuso correto, sem duplicação
problemática.

## Relevância para a investigação atual

Item 118: nenhuma. Item 122: adjacente em espírito (análise de
"prefixo de trajetória determinado por (x−3)/4 mod 2^m" é o mesmo
objeto combinatório clássico de Terras/Everett sobre tempos de parada
em classes residuais, próximo ao território do lema 2-ádico de H-110)
mas não avança nenhuma medida de densidade nem desafia nossas
hipóteses — redescoberta de técnica conhecida, não novidade.

## Veredito

Nenhum erro matemático de fundo em nenhum dos dois papers. Item 118
tem uma alegação central mal enquadrada (confunde "um número" com
"verificação exaustiva"), computação correta. Item 122 tem um bug de
rotulação secundário no apêndice, sem consequência nos resultados
principais.
