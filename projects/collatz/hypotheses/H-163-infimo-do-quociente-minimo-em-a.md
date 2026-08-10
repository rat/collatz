# H-163: o quociente mínimo de Wirsching estabiliza em `ell`; o ínfimo em `a` é positivo?

Status: aberta (open-unexplored), com medição parcial em E-135

Criada: 2026-08-09

Origem: H-134, seção de 2026-08-09, e H-162. Ao medir a metade
quantitativa de `(?3)` apareceu uma separação que nenhuma nota anterior
desta linha registra.

## Observação

Defina

```text
R_ell(k, S) = min_{a em S} g_ell(k,a) / gbar_ell(k),
gbar_ell(k) = (soma sobre unidades de g_ell(k,a)) / (2*3^(ell-1)).
```

Com `S` = todas as unidades módulo `3^ell`, `R` decai geometricamente em
`ell`. Com `S` = um conjunto **fixo** de inteiros, `R` fica plano em
`ell`. Medidas de E-135 (`central_ratio.py`) em `k = ell + 5`, o menor
custo com suporte completo:

```text
S                     ell=10   ell=11   ell=12   ell=13   ell=14   ell=15   ell=16
todas as unidades     0.0509   0.0368   0.0536   0.0197   0.0435   0.0215   0.0240
a < 3^4  (54)         0.3056   0.2576   0.1877   0.2361   0.1742      .        .
a < 3^6  (486)        0.1019   0.1472   0.1341   0.1377   0.1306   0.1397      .
a < 3^7  (1458)       0.1019   0.0736   0.1073   0.0787   0.1161   0.1075   0.0958
a < 3^8  (4374)       0.0509   0.0736   0.0805   0.0787   0.1016   0.0967   0.0878
```

Todos os conjuntos fixos acima são completos, não amostrados. Em
`ell=10` a linha de `3^8` coincide com a linha de todas as unidades
porque 4374 dos 39366 resíduos já contêm o minimizador global; a partir
de `ell=11` o conjunto fixo é uma fração que encolhe e as duas linhas
se separam.

A linha das unidades decai a cerca de 0,88 por nível em `d=+5`. Em
`d=+12`, onde o suporte é completo desde `ell=4` e a série tem menos
ruído, o mínimo sobre todas as unidades cai de 0,4805 em `ell=6` para
0,2555 em `ell=16`, razão 0,94 por nível, estável entre as metades
`6..10` e `11..16`. As linhas de conjunto fixo não têm tendência ao
longo de seis ou sete níveis.

## Interpretação, e o confundidor que precisa ser separado

`min` sobre todas as unidades módulo `3^ell` é o mesmo que `min` sobre
inteiros `a < 3^ell`. Isso não é evidência sobre `liminf_ell` em nenhum
`a` fixo: o resíduo que realiza o mínimo no nível `ell` tem
representante inteiro da ordem de `3^ell`, e o `liminf` que `(?2)` pede
para esse inteiro só começa em níveis bem acima de `ell`. As duas
estatísticas medem coisas diferentes.

Mas o mínimo sobre `a < 3^m` também depende de `m` só por ser mínimo
sobre um conjunto maior. Em `ell=14`, onde as quatro linhas existem,
passar de `a < 3^4` para `a < 3^8` multiplica o conjunto por 81 e o
mínimo cai de 0,1742 para 0,1016, fator 1,71; passar daí para todas as
3.188.646 unidades multiplica por mais 729 e o mínimo cai para 0,0435,
fator 2,34. O mínimo cai muito devagar com o tamanho do conjunto,
compatível
tanto com uma cauda esquerda de ínfimo positivo quanto com decaimento
lento até zero. Os dados não separam as duas coisas, e qualquer leitura
que atribua a queda ao tamanho 3-ádico de `a`, e não ao tamanho do
conjunto, estaria confundindo os dois efeitos.

O que está estabelecido: **a `ell` fixo o quociente não se deteriora**.
O decaimento em `ell` do mínimo sobre todas as unidades é o crescimento
do conjunto de índices, `2*3^(ell-1)`, não a piora de nenhum resíduo.

## A pergunta

`(?3)` pede `inf` sobre `Z_3^x` inteiro, e esse ínfimo continua caindo
enquanto o grupo cresce. `(?1)`, que é o que o Teorema 1 consome, pede
só, para cada inteiro `a` não cíclico com `a != 0 mod 3`, um `liminf` em
`ell`, com constante uniforme em `a`. A pergunta é se

```text
inf_{a inteiro unitário} liminf_ell g_ell(k_ell,a)/gbar_ell(k_ell)
```

é positivo. Equivalentemente, se a cauda esquerda da distribuição do
quociente tem ínfimo positivo.

Se for positivo, `(?3)` como enunciada é forte demais sem prejuízo para
a cadeia, e a Conjectura 2 é o alvo errado. Se for zero com decaimento
`rho^m` em `m = log_3 a`, então `mu_1` na prova do Teorema 1 vira
`a^(-log(1/rho)/log 3)` e a conclusão enfraquece de `densidade >= c/a`
para `densidade >= c*a^(-1-eps)`: ainda densidade positiva de
predecessores para cada `a`, mas não a taxa uniforme da Definição 1 de
Wirsching.

## Próximo passo

Trocar o mínimo por quantis fixos da distribuição de
`g_ell(k,a)/gbar_ell(k)` sobre as unidades. Um quantil não sofre do
confundidor de tamanho de conjunto. Se o quantil de `10^(-3)` for plano
em `ell` enquanto o mínimo cai, a queda do mínimo é estatística de
extremos; se o quantil também cair, é deterioração real da cauda.
E-116 e E-128 já computam estatísticas de colisão sobre as mesmas
tabelas e podem ser reaproveitados. A tabela exata vai a `ell=16` em
cerca de 96 s.

## Ligação com H-143

H-143 prova que uma cota uniforme `g_ell(k,a) >= eta*gbar_ell(k)` na
janela implica `mu_ell(a) >= C*3^(-ell)`. Com `eta` substituído pelo
valor medido para o mínimo sobre todas as unidades, a mesma implicação
só entrega `mu_ell(a) >~ 3^(-1.06*ell)`. Com `eta` fixo em `a`, ela
entrega a forma original `C_a*3^(-ell)`, com `C_a` dependendo de `a`.
Qual das duas é a verdadeira é exatamente o conteúdo desta hipótese.
