# E-133 -- calibração do portão Kontorovich-Lagarias versus Volkov (H-113, O8)

Hipóteses relacionadas:
[`H-113`](../../hypotheses/H-113-statistical-gate-kontorovich-lagarias-vs-volkov.md),
[`H-162`](../../hypotheses/H-162-congruencia-de-irmaos-qx1.md).
Experimento predecessor: [`E-097`](../E-097-qx1-empirical-gate/).

## A pergunta

Kontorovich e Lagarias (arXiv:0910.1944, Teorema 8.10) preveem expoente
de contagem `eta_5,BP ~ 0.650919` para a árvore reversa de `5x+1`. Um
modelo de ramificação concorrente, de Volkov, discutido no mesmo artigo,
prevê `~0.678`. Os dois diferem por `Delta = 0.027081`, e os próprios
autores escrevem que os dados de Volkov "seems insufficient to
discriminate between these two predicted exponents. It would be
interesting for this problem to be investigated further." E-097 mediu
`0.639` com intervalo bootstrap `[0.633, 0.645]`.

Ninguém tinha medido o que esse estimador faz com um processo de
expoente já conhecido. Fazer isso acaba respondendo também a pergunta
original, porque o viés do estimador é maior que `Delta`, e a saída é
rodar o mesmo estimador em processos construídos para ter cada um dos
dois expoentes em disputa e ver qual leitura a árvore aritmética casa.

## O que tem aqui

| arquivo | o que faz |
|---------|-----------|
| `tree_counts.c` | o enumerador: árvore aritmética e três controles estocásticos casados, um só caminho de código |
| `validate_vs_python.py` | conferência byte a byte do C contra o enumerador Python de E-097 |
| `annealed_exact.py` | forma fechada da função de contagem anelada exata do modelo |
| `check_mean_vs_annealed.py` | o simulador reproduz essa forma fechada |
| `compare_modes.py` | distribuições de contagem dos modos lado a lado |
| `within_root_spread.py` | separa flutuação entre raízes de flutuação dentro de uma raiz |
| `cyc_vs_cycq.py` | confere que a recursão inteira e a real concordam |
| `buffer_squeeze.py` | limita o erro da própria extrapolação de truncamento |
| `analyze.py` | o estimador de E-097, slopes por década, déficit contra `alpha_-` |
| `summary.py` | a tabela de comparação: todos os processos, um estimador |
| `run_deep.sh`, `run_deep_cycq.sh` | as rodadas profundas, checkpoints até `1e12`, buffers até `1e17` |

Compilar e reproduzir:

```
gcc -O3 -march=native -fopenmp -o tree_counts tree_counts.c -lm
python3 validate_vs_python.py          # tem que imprimir VALIDATION PASSED
python3 annealed_exact.py 5
./tree_counts --q 5       --roots 300 --cp 4 8 --buf 9 13 --out data/q5_arith_b13.txt
./tree_counts --q 5 --cyc --roots 300 --cp 4 8 --buf 9 13 --out data/q5_cyc_b13.txt
./tree_counts --q 5 --iid --roots 300 --cp 4 8 --buf 9 13 --out data/q5_iid_b13.txt
./tree_counts --q 5 --cycq 5.00000 --roots 300 --cp 4 8 --buf 9 13 --out data/q5_cycq500_b13.txt
./tree_counts --q 5 --cycq 5.05398 --roots 300 --cp 4 8 --buf 9 13 --out data/q5_cycq505_b13.txt
python3 summary.py                     # a tabela de comparação
./run_deep.sh ; ./run_deep_cycq.sh     # horas, não minutos, em 16 núcleos
```

## Os quatro modos

Compartilham um único caminho de código. A classe de ramo de um nó ou é
o resíduo verdadeiro ou é um sorteio, e nada mais difere:

- `arith`: `r = u mod q`, a árvore real.
- `iid`: `r` sorteado uniformemente em cada nó. É o passeio aleatório
  ramificado cuja pressão anelada é `q^(alpha-1)/(2^alpha-1)`, então seu
  expoente de contagem é comprovadamente `alpha_-(q) = 0.650919` em
  `q = 5`.
- `cyc`: a classe do primeiro irmão é sorteada, e irmãos sucessivos
  avançam de `c = ((2^d-1)/q) mod q`, que é exatamente o que a árvore
  aritmética faz (H-162).
- `cycq qval`: a estrutura de `cyc` com o denominador de valor trocado
  por um real `qval`, o que torna o expoente ajustável. Ele resolve
  `qval^alpha = q(2^alpha - 1)`: `qval = 5.00000` dá 0.650919 e
  `qval = 5.05398` dá 0.678.

As raízes são férteis por construção em todos os modos. Errar isso foi um
erro real na primeira passada aqui: as raízes aritméticas são sorteadas
com `u mod q != 0` e portanto são sempre férteis, então um controle que
sorteasse o resíduo da raiz em `{0..q-1}` matava uma árvore em `q` de
saída e lia `0.484` em vez de `0.612`.

## A contagem anelada exata

Para cada inteiro `n >= 1`, o número esperado de filhos de um nó no
expoente exatamente `n` é `1/q`: o filho existe sse `2^n r == 1 (mod q)`,
isto é `r == 2^(-n)`, uma única classe de resíduo entre `q`. Logo a
intensidade de prole é `(1/q) sum_{n>=1} delta_n`, um nó de nível `k`
alcançado pelos expoentes `a_1..a_k` fica na razão de valor `2^A/q^k`
com `A = sum a_i`, e

```text
E[# nós de nível k com sum a_i = A] = q^(-k) C(A-1, k-1).
```

Contar os que têm `2^A/q^k <= 10^t` significa `A <= N_k(t)` com
`N_k(t) = floor((t + k log10 q)/log10 2)`, e a identidade do taco de
hóquei `sum_{A=k}^{N} C(A-1,k-1) = C(N,k)` colapsa a soma interna:

```text
M(t) := E[N(u0 * 10^t)] = sum_{k>=1} C(N_k(t), k) / q^k .
```

Conferida contra a soma dupla bruta para `q = 3, 5, 7` e `t = 1..4`, e
contra a contagem média do simulador.

Isso importa porque resolve uma questão que as extrapolações ajustadas
não resolviam. O slope local anelado chega a `0.6517` em `t = 3` e
`0.65079` em `t = 4`, contra `alpha_-(5) = 0.650919`. O lado anelado do
modelo praticamente não tem viés de janela finita nas escalas em que
E-097 trabalhou. Todo viés que o estimador tem é, portanto, atraso
quenched contra anelado, o log-slope de uma realização ficando para trás
do log-slope da média, e não um expoente de correção que se pudesse
ajustar.

## Resultado, parte 1: o viés do estimador é maior que aquilo que ele mede

Janela padrão de E-097, `1e5..1e8`, 300 raízes, truncamento extrapolado
a buffer infinito por Aitken, estimador idêntico em todos os modos:

| modo | estimador | sd de log10 N(1e8) | expoente verdadeiro |
|------|-----------|--------------------|---------------------|
| iid | 0.6131 | 0.8014 | 0.650919 |
| cyc | 0.6294 | 0.6657 | 0.650919 |
| arith | 0.6382 | 0.5942 | em disputa |

O estimador subestima em 0.038 num processo de expoente conhecido. Isso
é maior que `Delta = 0.027`. Logo a leitura crua não pode ser comparada
contra uma previsão teórica, que é o que E-097 e H-113 fizeram, e é
também por isso que somar o viés de volta na mão não é lícito: o viés
depende de quanto o processo flutua, e as três linhas acima flutuam de
formas visivelmente diferentes.

## Resultado, parte 2: comparar leituras, não leitura contra previsão

A saída é parar de comparar leitura enviesada com previsão não
enviesada. Rodar o mesmo estimador num processo construído para ter
expoente 0.650919 e noutro construído para ter 0.678, e ver qual leitura
a árvore aritmética casa. O modo `cycq` fornece os dois: mesma
ramificação, mesma congruência de irmãos, mesmas raízes, mesma janela,
mesmos buffers, mudando só o denominador de valor,
`qval^alpha = q(2^alpha - 1)`.

Saída de `summary.py`:

```
       process  true exponent             window estimator              decade 1e7->1e8
  cycq 5.00000       0.650919   0.63950 [0.63357,0.64647]   0.64796 [0.64426,0.65204]
  cycq 5.05398       0.678000   0.65943 [0.65290,0.66630]   0.67079 [0.66649,0.67585]
           cyc       0.650919   0.62943 [0.62213,0.63650]   0.64437 [0.64067,0.64819]
           iid       0.650919   0.61308 [0.60233,0.62415]   0.64068 [0.63276,0.64962]
         arith       disputed   0.63824 [0.63183,0.64474]   0.64791 [0.64391,0.65241]
```

A árvore aritmética lê 0.64791 na década comum mais profunda. Um
processo de expoente 0.650919 lê 0.64796 ali. Um processo de expoente
0.678 lê 0.67079, e o intervalo dele não encosta no da aritmética. A
mesma conclusão vale no estimador de janela.

Então o `0.639` de E-097 nunca foi evidência contra Kontorovich-Lagarias.
É, com três casas, o que um processo de expoente deles devolve nesse
estimador.

Isto é uma medição com controles calibrados, não uma prova, e testa o
expoente 0.678, não o modelo de Volkov. Aquele modelo é uma árvore
binária completa com outra codificação dos iterados, e não está
implementado aqui.

Dois sistemáticos foram checados em vez de supostos. `cyc` e
`cycq(5.0)` são o mesmo processo por construção e diferem de 0.0035 em
seis sementes, 1.5 erro-padrão, então nenhum sistemático de
implementação acima de cerca de 0.004 separa a recursão inteira da real
(`cyc_vs_cycq.py`). Pôr um piso em valor 1 no passeio real, onde a
recursão inteira encosta, muda as contagens mas deixa o slope idêntico a
cinco casas.

## Rodada profunda

Checkpoints `1e4..1e12`, buffers `1e9..1e17`, 300 raízes. O slope
aritmético por década, cada década extrapolada no buffer separadamente:

| década | slope | bootstrap | distância a 0.650919 |
|--------|-------|-----------|----------------------|
| 1e7 -> 1e8 | 0.6465 | [0.6425,0.6506] | 0.0044 |
| 1e8 -> 1e9 | 0.6487 | [0.6467,0.6506] | 0.0022 |
| 1e9 -> 1e10 | 0.6490 | [0.6479,0.6499] | 0.0020 |
| 1e10 -> 1e11 | 0.6506 | [0.6502,0.6510] | 0.0003 |
| 1e11 -> 1e12 | 0.6505 | [0.6503,0.6508] | 0.0004 |

Essas bandas de bootstrap cobrem só a reamostragem de raízes.
`buffer_squeeze.py` limita o outro termo: refazer uma década bem
bufferizada usando só os três buffers que as décadas mais profundas têm
disponíveis a move em no máximo 0.002, e em 0.0003 a 0.0004 da década
`1e8 -> 1e9` em diante. Leia as décadas profundas como `0.6505 +/-
0.002`, contra `alpha_-(5) = 0.650919` e `0.678`.

O estimador de janela satura em 0.63778 no buffer `1e17`, então o valor
de Aitken 0.639 de E-097 para o limite de buffer infinito estava certo,
e toda a diferença restante até 0.6509 era viés de janela, não
truncamento.

## Notas

- `q = 7` tem `d = ord_7(2) = 3 < 6`, então só os resíduos em `<2> =
  {1,2,4}` são férteis: quatro classes entre sete são estéreis, não uma.
  A equação de pressão não muda, porque o número esperado de filhos por
  expoente continua `1/q`.
- O enumerador não precisa de conjunto de visitados. O mapa direto é uma
  função, então na árvore reversa todo nó tem no máximo um pai, e um
  membro de ciclo só é alcançável de dentro do próprio ciclo; as raízes
  são sorteadas fora de todo ciclo.
