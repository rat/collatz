# E-134: o programa de somas de Weyl 3-ádicas para a desigualdade de par, e uma cota de cascata incondicional

Dois resultados, um negativo e um positivo, ambos mirando a Questão 2 de
H-161 (a desigualdade de anti-concentração de pares que daria
`beta_eff <= 1 + 1/(2*kappa)`).

O negativo responde à pergunta que foi feita: o programa esboçado de
somas de Weyl 3-ádicas não consegue provar a desigualdade de par, e o
motivo não é falha de equidistribuição. O positivo apareceu ao montar
esse programa, e melhora a melhor cota incondicional sobre `beta_eff`
registrada neste projeto, de `2.306270` para `1.882712`.

## Resultado 1 (positivo, incondicional): o fator de cascata é não decrescente

Escreva `N_ell(u) = 3^ell mu_ell(u)` e, para `u` unidade mod `3^ell`,

```text
R_ell(u) := N_ell(u) / N_(ell-1)(u mod 3^(ell-1)).
```

F4 (pushforward) diz que os três filhos de cada `u` têm média igual ao
pai, logo `R` tem média 1 em cada trio de irmãos e `min_u R <= 1`.

**Alegação.** `min_u R_ell(u) >= min_v R_(ell-1)(v)`.

*Prova.* F1 dá `N_ell(y) = 3*2^-t0(y)*W_ell(k0(y))` com
`W_ell(k) = sum_{j>=0} 4^-j N_(ell-1)(A^j k)` e `A(k) = 4k+1 mod
3^(ell-1)`. Como `t0` depende só de `y mod 3` e
`k0(y mod 3^(ell-1)) = k0(y) mod 3^(ell-2)`, os fatores `3*2^-t0` se
cancelam na razão:

```text
R_ell(y) = W_ell(k) / W_(ell-1)(k mod 3^(ell-2)),    k = k0(y).
```

`A` é dado por uma fórmula inteira, então `A^j k mod 3^(ell-2) =
A^j(k mod 3^(ell-2))` para todo `j`. Numerador e denominador percorrem
portanto o MESMO índice `j` com os MESMOS pesos `4^-j`. Substituindo
`N_(ell-1)(A^j k) = N_(ell-2)(A^j k') * R_(ell-1)(A^j k)` exibe
`R_ell(k)` como média ponderada de `R_(ell-1)(A^j k)` com pesos
`4^-j N_(ell-2)(A^j k') / W_(ell-1)(k') >= 0` somando 1. Uma combinação
convexa fica entre o mínimo e o máximo do que ela promedia. Os pesos se
anulam exatamente nas posições não-unidade, onde `N` é identicamente
zero e `R_(ell-1)` não está definido, então nenhum termo `0/0` entra.
QED

**Consequência.** `N_ell(u) = N_(ell-1)(u mod 3^(ell-1)) * R_ell(u)`
pontualmente, logo `min N_ell >= (min R_ell)(min N_(ell-1))`, e pela
alegação `min R_ell >= min R_L` para todo `ell >= L`. Assim, para um
único nível `L`,

```text
3^ell c_ell = min_u N_ell(u) >= (min R_L)^(ell-L) * min_u N_L(u)
limsup beta_eff <= 1 + log(1 / min R_L) / log 3.
```

Um cálculo finito em um nível limita todos os níveis acima dele.

### Valores certificados (aritmética racional exata, sem ponto flutuante)

```text
 ell   min R_ell (exato)        decimal        cota de beta
   2   2/7                     0.285714285714   2.140314
   3   5240/15257              0.343448908698   1.972788
   4   razão de 49 bits        0.358528086675   1.933676
   5   razão de 153 bits       0.367554035026   1.911045
   6   razão de 479 bits       0.372104367916   1.899845
   7   razão de 1450 bits      0.375368623784   1.891895
   8   razão de 4365 bits      0.376951049877   1.888066
   9   razão de 13112 bits     0.377986076854   1.885570
  10   razão de 39355 bits     0.379174805339   1.882712
```

`min R_2 = 2/7` já dá `beta_eff <= 2.140314` a partir de um cálculo com
nove elementos, batendo o `2.306270` registrado antes em H-158. O nível
10 dá `1.882712`.

### Onde o método satura

float64, níveis 2 a 16 (min N conferido contra os valores que E-127
registrou de forma independente, `match` na última coluna):

```text
 ell    min R        max R      min N      minN/prev   cota beta   E-127
  10  0.37917481  1.51367184  0.060876   0.91318    1.882712
  12  0.37982580  1.51306047  0.052915   0.97170    1.881150  match
  14  0.38016988  1.51271393  0.046917   0.93648    1.880326  match
  16  0.38030266  1.51244385  0.042929   0.97315    1.880008  match
```

`min R_ell` cresce e é limitado por 1, logo converge; os valores medidos
ficam perto de `0.3803` e ainda estão subindo no nível 16. Esta rota
portanto encalha perto de `beta_eff <= 1.880` e **não consegue chegar a
1**. O motivo está visível na tabela: o fator por nível provado é `0.38`
enquanto a razão que a verdade atinge (`minN/prev`) roda entre `0.93` e
`0.97`. Essa folga é exatamente o que a desigualdade de par fecharia, e é
por isso que a Questão 2 de H-161 continua aberta.

Só `min R_L` num `L` calculado está certificado. O limite perto de
`0.3803` é medição, não constante provada.

### Relação com a alegação "nenhuma recursão escalar" de H-158

H-158 registra, como esboço não rederivado linha a linha, que nenhuma
desigualdade usando só o escalar `c_(ell-1)` (ou qualquer lista finita de
estatísticas de ordem de `mu_(ell-1)`, sem informação posicional) pode
fazer melhor que cerca de `beta <= 2.31`. O Resultado 1 é uma recursão
escalar com fator `0.3798 > 5/21`, então as duas afirmações precisam ser
reconciliadas.

Elas são consistentes. `min R_L` não é função de `c_(ell-1)`, nem de
nenhuma estatística de ordem de um único nível: é uma quantidade entre
níveis, comparando `mu_ell` contra `mu_(ell-1)` em resíduos casados. A
construção adversarial por trás do esboço de H-158 (uma medida
hipotética de nível `ell-1` mantendo um bloco de valores no mínimo ao
longo de um arco de `A`) é excluída aqui não por quão pequenos são os
valores, mas pela identidade de combinação convexa, que restringe como
uma lei de Syracuse real em um nível pode se apoiar sobre a própria
projeção. O esboço de H-158 é sobre o que o valor `c_(ell-1)` sozinho
sustenta, e ele sobrevive; só não cobre insumo entre níveis.

## Resultado 2 (negativo): o programa de Weyl não consegue provar a desigualdade de par

### A reformulação é limpa e exata

Na coordenada `z = 1+3k`, o mapa afim `A(k) = 4k+1` é multiplicação por 4
no grupo cíclico `G = {z = 1 mod 3}` dentro de `(Z/3^(n+1))^*`, de ordem
`3^n`. O tempo de órbita é o logaritmo discreto 3-ádico na base 4,
`tau(z) = log(z)/log(4)`, ambos os logaritmos convergentes em `G`. Logo
`A` é o deslocamento `tau -> tau+1` e os caracteres de `G` são
exatamente as fases de Weyl `chi_m(z) = e(m tau(z) / 3^n)`. Nessa base a
recursão `W(k) = N(k) + (1/4) W(A(k))` diagonaliza exatamente:

```text
What(m) = Nhat(m) / (1 - (1/4) e(-m/3^n)),
```

cujo denominador tem módulo entre 3/4 e 5/4, então `W` e `N` têm
coeficientes comparáveis frequência a frequência.

Os dois tipos de par de F2 viram mapas afins de `G` (ambos verificados
abaixo):

```text
Tipo (1,2):  b = 2a+1       <=>  sigma1(z) = 2z+2
Tipo (2,1):  a''' = 32b+17  <=>  sigma2(z) = 32z+20
```

### As somas de Weyl mistas são maximamente não degeneradas

`T(m,n) = sum_{z in G} chi_m(z) chi_n(sigma z)`. Escrevendo `z = 1+3a` e
`lambda = log/3`, a fase é `F(a) = m~ lambda(1+3a) + n~ lambda(sigma z)`
com `m~ = m/lambda(4)`, e

```text
sigma1:  F'(a) = m~/(1+3a) + n~/(2+3a)
sigma2:  F'(a) = m~/(1+3a) + 8 n~/(13+24a)
```

Um ponto crítico mod 3 exige `2m+n = 0 (mod 3)` para `sigma1` e
`m+2n = 0 (mod 3)` para `sigma2` (`lambda(4)` é unidade 3-ádica, então os
critérios se leem igual em `m,n` e em `m~,n~`). Sem ponto crítico a soma
se anula identicamente.

Verificado exaustivamente para `n = 2..7` e os dois mapas:

- fora do critério, `max|T| < 3.3e-14`: o anulamento é exato;
- dentro do critério, `|T(m,n)| = 3^((n+1+v)/2)` com
  `v = v_3(mdc(m,n))`, atingido. Razão `max|T| / 3^((n+1+v)/2) =
  1.000000` em todos os níveis testados.

Ou seja, toda frequência primitiva tem cancelamento de raiz quadrada,
`|T| = 3^((n+1)/2) = sqrt(3|G|)`, e as únicas somas maiores são as
aritmeticamente forçadas em frequências divisíveis por potência de 3
(uma frequência divisível por `3^v` colapsa a soma em `3^v` cópias de uma
soma mod `3^(n-v)`). A fase é tão não degenerada quanto uma fase pode
ser.

### E mesmo assim não dá nada

Sejam `S, S' ⊂ G` com densidades `delta, delta'`, e
`Sigma = #{z : z in S, sigma z in S'}`. Expandindo os dois indicadores,

```text
Sigma = |S||S'|/|G| + |G|^-2 * sum_{(m,n)!=(0,0)} conj(Shat(m)) conj(S'hat(n)) T(m,n).
```

Limitando o erro por valores absolutos, com
`sum_m |Shat(m)| <= |G|^(1/2) (sum_m |Shat(m)|^2)^(1/2) = |G|^(3/2)
delta^(1/2)`:

```text
erro <= max|T| * |G| * (delta*delta')^(1/2) = 3^(1/2) |G|^(3/2) (delta delta')^(1/2),
```

contra um termo principal `|G| delta delta'`. Isso substitui o valor mais
favorável `max|T| = sqrt(3|G|)`, o primitivo; o máximo verdadeiro sobre
todas as frequências não nulas é `|G|`, o que só piora. O erro só bate o
termo principal se `(delta delta')^(1/2) > 3^(1/2) |G|^(1/2)`, impossível
para densidades no máximo 1. **Em nenhuma densidade essa rota diz
alguma coisa**, incluindo o regime denso, quanto mais a cauda profunda
`x ~ 3^(-ell/2kappa)` que o teorema exige.

Isso não é artefato de tomar valores absolutos. `T(m,n)/|G|` é a matriz,
na base de caracteres, da composição com uma bijeção de `G`; composição
com bijeção é isometria de `L^2(G)`, então essa matriz é unitária e a
rota por norma de operador devolve exatamente a cota trivial de
Cauchy-Schwarz `(|S||S'|)^(1/2)`. De forma decisiva: tomando `S' =
sigma(S)` obtém-se `Sigma = |S|`, logo **nenhuma cota que dependa só de
`|S|`, `|S'|` e de dados espectrais de `sigma` pode ser não trivial**,
por melhores que sejam as estimativas de Weyl.

### O que de fato falta

Não é equidistribuição de `sigma`. O que falta é controle harmônico do
próprio conjunto de nível `{V <= x}`, conjuntamente com `sigma`: algum
motivo pelo qual `Shat` não pode se alinhar com as frequências onde `T` é
grande. Como `S` é definido por `V` e `sigma` relaciona `V` consigo
mesmo, qualquer prova tem que usar a descrição autossimilar de `V` em vez
de tratar `S` como caixa preta.

Escopo da alegação negativa: exclui o programa específico (estimar `T`,
inserir na expansão, limitar o erro), não métodos tipo Weyl em geral.
Estimar os coeficientes de Mellin do próprio `V` continua intocado e é a
próxima coisa natural a tentar.

## Arquivos

- `cascade_factor_bound.py`: Resultado 1. `--exact L` roda aritmética
  racional certificada até o nível `L`; `--float L` roda a medição em
  float64, checa F4 e a monotonicidade em todos os níveis, e confere min
  N contra E-127.
- `pair_character_sum.py`: Resultado 2. Reverifica F1 e os dois tipos de
  par de F2 a partir de uma reconstrução do zero das leis, deriva os
  mapas em coordenada `z`, e avalia `T(m,n)` exaustivamente contra a
  previsão de fase estacionária e a lei de tamanho.

## Como rodar

```sh
python3 cascade_factor_bound.py --exact 8 --float 12     # segundos
python3 cascade_factor_bound.py --exact 10 --float 16    # cerca de 100 s
python3 pair_character_sum.py --weyl-levels 2 3 4 5 6 7  # cerca de 3 s
```

O nível 10 exato leva cerca de 74 s e é a parte lenta (a busca do mínimo
compara racionais de 39355 bits). O nível 16 em float64 tem pico de 2,4
GB residentes (medido).
Toda asserção dos dois scripts é uma checagem que falharia alto: massa
total 1 em cada nível, F4 a 1e-10, monotonicidade de `min R`,
`min R <= 1`, `sigma` bijetora em `G`, e 4 gerando `G`.
