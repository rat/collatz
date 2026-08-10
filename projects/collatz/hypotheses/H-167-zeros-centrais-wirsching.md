# H-167: os zeros de custo central de Wirsching persistem?

Status: fechada-inconclusiva

Criada e encerrada: 2026-08-09

Origem: H-134, seção de 2026-08-09. Leitura da fonte primária
(`literature/papers/132_Wirsching-2003-Positive-Predecessor-Density.pdf`)
mostrou que a Conjectura 2 é a implicação `(?4) => (?3)`, e que `(?3)`
é quantificada em todo `ell >= ell_0` e toda unidade `a`. Como
`k_ell = ell` pertence a `A_delta` para todo `delta > 0`, um único
resíduo com `g_ell(ell,a) = 0` num nível `ell >= ell_0` já falsifica
`(?3)`.

## Hipótese

`Z_ell = {a em (Z/3^ell)^x : g_ell(ell,a) = 0}` é não vazio para todo
`ell`. Se for, `(?3)` é falsa, e a Conjectura 2 é falsa sempre que
`(?4)` valer (a seção 7 de Wirsching prova `(?5) => (?4)`, e a
Conjectura 3 tem suporte numérico certificado em §9.3 do paper 01).

## Teste (E-135, `central_zeros.py`)

Suporte booleano exato de `g_ell(.,a)`, empacotado um bit por custo,
para todos os `3^ell` resíduos e todo `ell <= 18`. A recursão progressiva
é a equação (2.1) lida ao contrário: `b` módulo `3^(ell-1)` com custo `c`
alimenta `(3b+1)*2^(-(j+1))` módulo `3^ell` com custo `c+j`. Auditada
contra o predicado regressivo independente de E-121 em todos os níveis
até 7 e em testemunhas de todos os níveis até 18.

```text
ell      unidades       |Z_ell|   fração   1o custo cheio   coerentes
 10         39366         10511   0.2670        ell+5            1465
 12        354294         68228   0.1926        ell+5            8836
 14       3188646        414112   0.1299        ell+5           47188
 16      28697814       2312693   0.0806        ell+5          211664
 18     258280326      11540739   0.0447        ell+5          734754
```

`Z_ell` é não vazio em todos os 18 níveis. O primeiro custo com suporte
completo é `ell+5` em todo `10 <= ell <= 18`, estendendo até 18 o padrão
que E-115 tinha até 16.

## Por que fica inconclusiva

A razão `|Z_(ell+1)|/|Z_ell|` vale 2,39, 2,34, 2,27 e 2,20 nos quatro
últimos passos, contra 3 unidades novas por nível. Ela cai cerca de
0,06 por nível. Extrapolando linearmente ela cruzaria 1 perto de
`ell=35`, e só depois disso `|Z_ell|` começaria a encolher. Nada nos
dados decide se chega a zero.

A coluna `coerentes` conta os resíduos módulo `3^ell` cujas truncagens
são zeros centrais em todos os níveis anteriores. Se essa subárvore
fosse não vazia em todo nível, o limite inverso de conjuntos finitos não
vazios daria um `alpha` 3-ádico com `g_ell(ell,alpha)=0` para todo
`ell`, refutando `(?3)` e também `(?2)` naquele `alpha`. Mas a razão de
crescimento da subárvore cai mais depressa que a de `Z_ell`: 2,17, 2,06,
1,94, 1,79. Extrapolação linear a leva a 1 perto de `ell=24`, ou seja, a
subárvore provavelmente se extingue e o argumento de compacidade não
estará disponível. Isso é extrapolação, não prova, nos dois sentidos.

E-121 já havia mostrado o mesmo fenômeno num caso isolado: `2^(-1)`
módulo `3^ell` é zero central em todo nível até 21 e deixa de ser em 22.

## O que isso muda

Nada da cadeia, por dois motivos.

Primeiro, mesmo que `Z_ell` nunca esvazie, a Proposição da janela
unilateral em H-134 mostra que o Teorema 1 de Wirsching não precisa do
centro: basta a cota em deslocamentos `c_0 <= k-ell <= delta*sqrt(ell)`,
e com `c_0 = 5` o suporte é completo em todo nível testado a partir de
10. Os buracos em `k=ell` são artefato da janela simétrica.

Segundo, o obstáculo real medido em E-135 não é de suporte e sim
quantitativo, e ele está registrado em H-168.

## Auditoria

`central_zeros.py` verifica cada nível até 7 comparando os 32 bits de
custo de resíduos amostrados com o predicado regressivo de E-121, e
recheca as três menores testemunhas coerentes de cada nível contra o
mesmo predicado em todos os níveis anteriores. Nenhuma divergência.
