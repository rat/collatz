# E-135: zeros de custo central e a metade quantitativa de `(?3)` de Wirsching

Hipóteses relacionadas: H-134 (seção de 2026-08-09), H-162, H-163.

Wirsching (2003) reduz densidade positiva uniforme de predecessores a
uma cadeia de cinco condições. A Conjectura 2 é o passo `(?4) => (?3)`,
com

```text
(?3)  g_ell(k_ell, a) >= mu * gbar_ell(k_ell)
      para toda unidade a, todo ell >= ell_0 e toda sequência
      (k_ell) com |ell - k_ell| <= delta*sqrt(ell),
```

e `(?4)` um enunciado sobre o operador de média unidimensional `W_3`
que nunca menciona os geradores. Como `k_ell = ell` é uma sequência
admissível para todo `delta > 0`, um único resíduo unitário com
`g_ell(ell,a) = 0` num nível `ell >= ell_0` falsifica `(?3)`.

Este experimento separa as duas metades independentes de `(?3)`.

## `central_zeros.py`: a metade de suporte

Suporte booleano exato de `g_ell(.,a)` para todo resíduo módulo `3^ell`
e todo custo até um teto, empacotado um bit por custo numa palavra por
resíduo. Reporta o conjunto de zeros no custo exatamente `ell`, o menor
custo cujo suporte cobre todas as unidades, e a subárvore coerente de
resíduos cujas truncagens são zeros centrais em todos os níveis
anteriores.

```sh
python3 central_zeros.py --max-ell 18
```

Até `ell = 18` o conjunto de zeros nunca é vazio e o menor custo que
cobre tudo é `ell + 5` para todo `ell` a partir de 10, estendendo o
padrão que E-115 via até 16. Em `ell = 18` são 11.540.739 zeros entre
258.280.326 unidades, e 734.754 deles coerentes. Uma subárvore coerente
não vazia em todo nível daria, pelo limite inverso de conjuntos finitos
não vazios, um `alpha` 3-ádico que é zero central em todo nível,
refutando `(?3)` e `(?2)` nesse `alpha`. Sua razão de crescimento cai de
2,17 para 1,79 nos últimos quatro níveis, então ela plausivelmente se
extingue perto de `ell = 24` e o argumento de compacidade não estará
disponível. Nos dois sentidos isso é extrapolação.

A tabela empacotada é auditada contra o predicado regressivo
independente de E-121 em todo nível até 7, e as menores testemunhas
coerentes de cada nível são reconferidas com o mesmo predicado em todos
os níveis anteriores.

## `central_ratio.py`: a metade quantitativa

Contagens inteiras exatas da mesma recursão, reportando

```text
min_{a em S} g_ell(ell+d, a) / gbar_ell(ell+d)
```

para vários deslocamentos `d`, e separadamente para um conjunto **fixo**
de inteiros `a` que não cresce com `ell`. O total de cada linha é
confrontado com a contagem independente de composições limitadas de `k`
com capacidades `2, 6, 18, ..., 2*3^(ell-1)`, que é a identidade de
Wirsching `2*3^(ell-1)*gbar_ell(k)`.

```sh
python3 central_ratio.py --max-ell 15
python3 central_ratio.py --max-ell 16 --offsets 0 5 12 --sqrt-multiples 1
python3 central_ratio.py --max-ell 16 --offsets 5 --sqrt-multiples 1 \
    --fixed-offset 5 --random-fixed 1458 --random-bound 2187
```

O mínimo sobre todas as unidades, em deslocamentos onde o suporte já é
completo, decai geometricamente em `ell`: em `d = +12` cai de 0,4805 em
`ell = 6` para 0,2555 em `ell = 16`, fator perto de 0,94 por nível,
igual nas duas metades da faixa. O deslocamento teria de crescer
linearmente em `ell` para compensar, e a janela de Wirsching só permite
`d <= delta*sqrt(ell)`. Logo o ínfimo sobre `Z_3^x` que `(?3)` exige não
estabiliza em ponto nenhum da janela, não apenas em `k = ell` por falta
de suporte.

O mínimo sobre um conjunto fixo de inteiros se comporta de outro jeito.
Em `d = +5`, sobre todas as 486 unidades abaixo de `3^6`, o quociente dá
0,102, 0,147, 0,134, 0,138, 0,131, 0,140 para `ell = 10..15`: plano.
Sobre todas as 1458 unidades abaixo de `3^7` dá 0,102, 0,074, 0,107,
0,079, 0,116, 0,108, 0,096 para `ell = 10..16`, e sobre todas as 4374
unidades abaixo de `3^8` dá 0,051, 0,074, 0,081, 0,079, 0,102, 0,097,
0,088: também plano. Sobre as 54 unidades abaixo de `3^4` fica perto de
0,22.

O mínimo sobre todas as unidades módulo `3^ell` é o mínimo sobre
inteiros `a < 3^ell`, e isso não é evidência sobre `liminf_ell` em
nenhum `a` fixo, porque o resíduo que o realiza tem representante
inteiro da ordem de `3^ell`. O que as tabelas estabelecem é que a `a`
fixo o quociente não se deteriora com `ell`; a queda do mínimo sobre
todas as unidades é o crescimento do conjunto de índices. Separar isso
de uma queda real da cauda esquerda exige quantis em vez do mínimo, que
é o próximo passo registrado em H-163.

## Memória e tempo

A execução de suporte guarda dois arrays `3^ell` de palavras de 32 bits
durante a transição de nível, mais alguns arrays booleanos `3^ell`, então
`ell = 18` precisa de cerca de 5 GB. O último nível levou 117 s. A
execução de contagens exatas guarda dois arrays
`(k_max+1) x 3^ell` int64, então o comando com `ell = 16` acima, cujo
teto é `k_max = 28`, precisa de cerca de 20 GB. Seu último nível levou
96 s. Ambas são numpy de uma thread. Baixar `--offsets` baixa `k_max` e
a memória cai na mesma proporção.
