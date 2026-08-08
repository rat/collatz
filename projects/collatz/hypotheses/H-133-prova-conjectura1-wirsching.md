# H-133: prova da Conjectura 1 de Wirsching por cancelamento gerador

Status: fechada-confirmada após rodada crítica

Criada: 2026-08-07

## Enunciado

Na notação de Wirsching (2003), suponha que existam `delta_1, mu_1>0`
tais que

```text
liminf g_ell(k_ell,a)/gbar_ell(k_ell) >= mu_1
```

uniformemente nas sequências
`|k_ell-ell|<=delta_1 sqrt(ell)`. Então a mesma propriedade vale para
as funções de Elka `e_ell`, com a mesma dependência em `a` presente na
hipótese. Esta é a Conjectura 1 do artigo.

## Identidade exata

Ponha `c_0=1` e `c_j=2*3^(j-1)` para `j>=1`. Seja `q_ell(k)` o número
de distribuições de `k` bolas em urnas de capacidades `c_j-1`,
`0<=j<=ell`. Wirsching registra

```text
q_ell(k) = 2*3^(ell-1) gbar_ell(k)
```

para `ell>=1`. Logo

```text
sum q_ell(k) z^k = product_(j=0)^ell (1-z^c_j)/(1-z).
```

Por definição,

```text
sum p_ell(m) z^m = product_(j=0)^ell (1-z^c_j)^(-1).
```

Os fatores se cancelam. Usando `ebar_ell=p_ell*gbar_ell`, obtemos

```text
ebar_ell(k) = [1/(2*3^(ell-1))] binom(k+ell,ell).       (1)
```

## Concentração da convolução

Fixe `0<delta<delta_1` e escolha `eta>0` com
`delta+eta<delta_1`. Para `|k-ell|<=delta sqrt(ell)`, escreva

```text
ebar_ell(k) = sum_(m=0)^k p_ell(m) gbar_ell(k-m).
```

O número de partições `p_ell(m)` é limitado pelo número `p_infty(m)`
de partições nas moedas `1,2,6,18,...`. Se `J` é o maior índice com
`c_J<=m`, então

```text
p_infty(m) <= product_(j=0)^J (1+floor(m/c_j))
             <= (m+1)^(J+1)
             <= exp(C log^2(m+2))                         (2)
```

para uma constante absoluta `C`, pois `J=O(log m)`.

Removendo as restrições de capacidade das urnas,

```text
gbar_ell(r) <= [1/(2*3^(ell-1))] binom(r+ell,ell).       (3)
```

Para `0<=m<=k`,

```text
binom(k-m+ell,ell)/binom(k+ell,ell)
 = product_(s=0)^(m-1) (k-s)/(k+ell-s)
 <= (k/(k+ell))^m.                                      (4)
```

Na janela escolhida, `k/(k+ell)<=r<1` para todo `ell` grande, com
`r` independente de `ell`. De (1)-(4), a fração da convolução com
`m>=eta sqrt(ell)` é no máximo

```text
sum_(m>=eta sqrt(ell)) exp(C log^2(m+2)) r^m = o(1).     (5)
```

O limite é exponencial em `-sqrt(ell)`, salvo um termo
`O(log^2 ell)`.

## Transferência da cota

Pela hipótese uniforme nas sequências, para qualquer `epsilon>0` e todo
`ell` suficientemente grande,

```text
g_ell(j,a) >= (mu_1-epsilon) gbar_ell(j)
```

sempre que `|j-ell|<=delta_1 sqrt(ell)`. De fato, se essa afirmação
falhasse, uma subsequência de pares ruins `(ell,j)` poderia ser estendida
a uma sequência admissível, contradizendo a hipótese. Se
`|k-ell|<=delta sqrt(ell)` e `0<=m<=eta sqrt(ell)`, então
`j=k-m` pertence a essa janela. Como todos os termos são não negativos,

```text
e_ell(k,a)
 >= (mu_1-epsilon) sum_(m<=eta sqrt(ell))
                         p_ell(m) gbar_ell(k-m)
 = (mu_1-epsilon)(1-o(1)) ebar_ell(k),
```

uniformemente em `k`, e preservando a uniformidade em `a` caso ela faça
parte da hipótese. Tomando, por exemplo,
`epsilon=mu_1/2`, obtemos a condição `(?1)` do Teorema 1 com qualquer
`mu<mu_1/2`. Isto prova a Conjectura 1.

## Dependências e alcance

A prova usa apenas as equações (2.2)-(2.4) e a interpretação de
`gbar_ell` registrada por Wirsching, mais estimativas elementares.
Não usa WCC, a conjectura beta=1, independência entre subárvores ou a
Conjectura 3.

O3 fica reduzido à Conjectura 2 de Wirsching. A condição analítica
`(?4)` que aparece como premissa da Conjectura 2 continua fortemente
apoiada por E-099, mas a passagem dos operadores limites para as
densidades aritméticas ainda precisa ser provada.

Verificação finita independente: `experiments/E-113-wirsching-conj1/`.

## Rodada crítica de 2026-08-07

Foram conferidos quatro pontos capazes de invalidar o argumento. A equação
(1) coincide com a fórmula (1.4) de Wirsching. A majorante (2) conta um
superconjunto de todas as partições permitidas. A razão binomial em (4) é
exata e uniforme na janela menor. Por fim, a uniformidade sequencial da
hipótese fornece a cota simultânea usada na prova por um argumento de
subsequência ruim. Também foi removida uma formulação que acrescentava
uniformidade em `a` sem que esse quantificador estivesse explícito no
enunciado impresso. A prova preserva qualquer dependência em `a` presente
na hipótese e não a fortalece.
