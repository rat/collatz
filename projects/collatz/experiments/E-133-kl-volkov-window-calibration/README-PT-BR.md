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

A pergunta que este experimento responde não é "qual é o expoente". É
"quanto viés esse estimador carrega", coisa que ninguém tinha medido, e
que decide se a medição consegue resolver alguma coisa.

## O que tem aqui

| arquivo | o que faz |
|---------|-----------|
| `tree_counts.c` | o enumerador: árvore aritmética e dois controles estocásticos casados, um só caminho de código |
| `validate_vs_python.py` | conferência byte a byte do C contra o enumerador Python de E-097 |
| `annealed_exact.py` | forma fechada da função de contagem anelada exata do modelo |
| `check_mean_vs_annealed.py` | o simulador reproduz essa forma fechada |
| `compare_modes.py` | distribuições de contagem dos três modos lado a lado |
| `within_root_spread.py` | separa flutuação entre raízes de flutuação dentro de uma raiz |
| `analyze.py` | o estimador de E-097, slopes por década, déficit contra `alpha_-` |
| `run_deep.sh` | as rodadas profundas, checkpoints até `1e12`, buffers até `1e17` |

Compilar e reproduzir:

```
gcc -O3 -march=native -fopenmp -o tree_counts tree_counts.c -lm
python3 validate_vs_python.py          # tem que imprimir VALIDATION PASSED
python3 annealed_exact.py 5
./tree_counts --q 5       --roots 300 --cp 4 8 --buf 9 13 --out data/q5_arith_b13.txt
./tree_counts --q 5 --cyc --roots 300 --cp 4 8 --buf 9 13 --out data/q5_cyc_b13.txt
./tree_counts --q 5 --iid --roots 300 --cp 4 8 --buf 9 13 --out data/q5_iid_b13.txt
python3 compare_modes.py data/q5_arith_b13.txt data/q5_cyc_b13.txt data/q5_iid_b13.txt
./run_deep.sh                          # cerca de 45 minutos em 16 núcleos
```

## Os três modos

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

As raízes nos três modos são férteis por construção. Errar isso foi um
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

## Resultado

Janela padrão de E-097, `1e5..1e8`, 300 raízes, truncamento extrapolado
a buffer infinito por Aitken, estimador idêntico nos três modos:

| modo | estimador | sd de log10 N(1e8) | verdade |
|------|-----------|--------------------|---------|
| iid | 0.6119 | 0.8014 | 0.650919 |
| cyc | 0.6283 | 0.6657 | 0.650919 |
| arith | 0.6364 | 0.5942 | em disputa |

**O estimador subestima em 0.039 num processo cujo expoente é
conhecido.** Isso é maior que a separação `Delta = 0.027` que ele foi
construído para resolver. A medição de E-097 é portanto silenciosa sobre
Kontorovich-Lagarias versus Volkov, nas duas direções.

O passo óbvio seguinte, somar 0.039 de volta à leitura aritmética para
obter `0.675`, não é lícito. O viés foi medido num processo cuja
flutuação é visivelmente maior que a da árvore aritmética (sd 0.80
contra 0.59), então não é o mesmo regime de viés, e viés medido num
regime não transfere para outro.

Slopes por década, cada um extrapolado no buffer de truncamento
separadamente, se comportam muito melhor que o estimador de janela de
três décadas. Na década mais profunda da rodada padrão, `1e7 -> 1e8`, o
viés do controle já cai a `0.0102`, abaixo de `Delta/2`. A rodada
profunda leva isso até a década `1e11 -> 1e12`; ver `data/` e a tabela
abaixo.

## Rodada profunda

Checkpoints `1e4..1e12`, buffers `1e9..1e17`, 300 raízes, três modos.
Preenchido a partir da saída de `analyze.py`.

Em execução; os resultados vão para `data/q5_{arith,cyc,iid}_b17.txt`.

## Notas

- `q = 7` tem `d = ord_7(2) = 3 < 6`, então só os resíduos em `<2> =
  {1,2,4}` são férteis: quatro classes entre sete são estéreis, não uma.
  A equação de pressão não muda, porque o número esperado de filhos por
  expoente continua `1/q`.
- O enumerador não precisa de conjunto de visitados. O mapa direto é uma
  função, então na árvore reversa todo nó tem no máximo um pai, e um
  membro de ciclo só é alcançável de dentro do próprio ciclo; as raízes
  são sorteadas fora de todo ciclo.
