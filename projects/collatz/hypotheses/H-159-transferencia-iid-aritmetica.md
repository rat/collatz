# H-159: transferência da cauda iid para a árvore aritmética

Status: aberta

Criada: 2026-08-08

## Alvo

Transferir o teorema de cauda de H-132 para o funcional enraizado na
árvore reversa aritmética. É necessário controlar a dependência entre
dígitos novos de subárvores irmãs depois da média sobre os índices de
caminho e da remoção dos modos afins grosseiros identificados em H-150.

## Critério de fechamento

Uma prova deve fornecer uma aproximação quantitativa suficiente para
aplicar renovação implícita ou construir diretamente a cauda regular
com índice `alpha_plus(q)/alpha_minus(q)`. Um contraexemplo estrutural
que impeça qualquer transferência desse tipo também fecha a hipótese,
como refutada.

## Relações

Esta é a dívida aritmética compartilhada por O1 e O7. Independência
par a par de caminhos fixos já foi refutada por H-150; o alvo correto é
cancelamento após agregação.

## Atualização E-129 (2026-08-08)

Testada a rota ingênua mais óbvia para a agregação: promediar a lei
conjunta dos dígitos frescos (E-120) sobre a medida de ramificação
natural do gap `Delta` entre irmãos (peso `P(Delta=2k)=3*4^-k`, de
E-108), e medir a distância TV e a informação mútua da lei conjunta
agregada contra o produto de suas próprias marginais.

Resultado: a agregação sobre `Delta` **não** aproxima a lei do produto.
Em `fresh=6`, TV de um par com `delta` fixo é `0.998628`; agregada sobre
`Delta` (com `k_max=16`, cobrindo essencialmente toda a massa da série
geométrica) ainda é `0.992193`. A informação mútua se comporta do mesmo
jeito. Verificado antes de aceitar o número: a lei conjunta de um único
`delta` não depende de qual resíduo unitário `x0 mod 3^coarse` é usado
como referência (checado para vários `coarse` e `delta`), então a
agregação usada é a lei condicional correta, não artefato de uma
escolha arbitrária.

**Isso não fecha H-159 nem a move para refutada.** TV e informação
mútua são as métricas erradas para refutar a transferência: elas ficam
dominadas pela estrutura de suporte determinística (para `delta` fixo,
o bloco de `y` é função determinística do bloco de `x`), então TV
próxima de 1 é esperada independente de qualquer cancelamento no
funcional que a renovação implícita realmente precisa (um momento ou
coeficiente de Fourier/Mellin específico, não a distância em variação
total). O experimento também fixa só um par de irmãos de um mesmo pai;
a árvore real agrega muitos mais pares simultaneamente.

**O que o resultado realmente descarta**: a rota ingênua "promediar
sobre o gap `Delta` isoladamente e invocar renovação implícita direto
sobre a lei quase-produto resultante" não funciona, porque a lei
agregada não fica perto de um produto em nenhuma das duas métricas
testadas. O alvo permanece em aberto, mas mais restrito: precisa ser
cancelamento num funcional específico (momento/Fourier), não
aproximação distribucional, e provavelmente precisa agregar sobre mais
do que um único par de irmãos.

Ver `projects/collatz/experiments/E-129-fresh-digit-aggregate-cancellation/`.

## Atualização E-133 (2026-08-09)

Seguindo o alvo mais restrito que E-129 deixou registrado acima, foi
testado o funcional que o programa de segundo momento realmente
consome. A §9 do `main.tex` ("The correct, non-circular
reformulation") escreve a quantidade relevante como
`Cov ~ sum_{xi != 0} S_1(xi) conj(S_2(xi))`, com a **mesma** frequência
nos dois fatores. Isso é uma fatia diagonal do espectro bivariado do
par, equivalente ao funcional de caractere da diferença,

```text
D(xi) = E[ e_{3^s}( xi (X - Y) ) ],
```

que vale zero para todo `xi != 0` sob a lei produto. É o mesmo tipo de
objeto que `thm:multiscale-parseval` e `prop:primitive-fibre-energy`
consomem: um coeficiente de uma lei numa frequência, nunca uma
distância entre duas leis.

Resultado, agregando sobre exatamente a mesma medida de ramificação que
E-129 usou (`coarse=1`, `k_max=16`, para as linhas serem comparáveis
termo a termo):

```text
fresh   TV agregada     max |D_agg| primitivo
  1       0.651045            9.77e-01
  3       0.885610            1.14e-05
  6       0.992193           1.50e-146
```

A linha `fresh=6` reproduz exatamente o `0.992193` que E-129 relatou,
o que serve de reverificação independente daquele experimento antes de
contrastar com ele.

**O funcional cancela; TV não.** E as duas colunas não são duas
métricas do mesmo objeto: são objetos diferentes, e o programa lê o
segundo.

O mecanismo é exato, não numérico. Com `Y = mX + g mod 3^s` e
`m = 2^Delta`, tem-se `X - Y = (1-m)X - g`, logo

```text
D(xi) = e(-xi g / 3^s) * muhat( xi (1-m) ),
```

para qualquer lei `mu` do parâmetro livre. Como
`v3(1 - 2^(2k)) = 1 + v3(k)`, toda a ressonância diagonal de um par com
gap `2k` mora no condutor `3^(1+v3(k))`, e nada sobrevive acima dele.
Para o gap típico isso é o condutor 3: um único modo grosseiro, que é
exatamente o modo que o enunciado de O1 já manda remover. Um gap
contribui numa frequência primitiva de escala `s` só se `v3(k) >= s-1`,
ou seja `k >= 3^(s-1)`, e esses gaps carregam peso de ramificação total
no máximo `4^(1-3^(s-1))`, limite atingido a menos de fator 1,4 em toda
escala medida.

Consequência quantitativa, ligando o funcional ao resto do programa de
Fourier do paper:

```text
sum_{xi primitivo mod 3^s} |D(xi)|^2 = 3^j * E_(s-j)(mu),
       j = v3(1-2^Delta) = 1 + v3(k),
```

com `E_r` exatamente a energia primitiva de `thm:multiscale-parseval`.
Verificado com erro relativo abaixo de `5e-14`. O funcional de par na
escala `s` é controlado pelo espectro da própria marginal do parâmetro
livre numa escala mais grosseira `s-j`, sem nenhuma hipótese de
independência: o critério `L2` de `thm:multiscale-parseval` transfere
termo a termo.

Rótulos (Regra 10b): o anulamento para gap fixo, a identidade
`D(xi) = fase * muhat(xi(1-m))`, o limite `4^(1-3^(s-1))` e a relação de
energia `3^j E_(s-j)` são **provados** (contas de uma linha,
conferidas numericamente); a verificação sobre inteiros reais na seção
E do experimento é **empírica**, seis raízes e profundidade 5.

Duas descobertas colaterais, ambas registradas no README do
experimento:

1. Nem todo momento cancela. A covariância dos `j`-ésimos dígitos
   base-3 das duas folhas fica em `0,46` (dígito 0) e `0,19`
   (dígito 2) depois de agregada. A escolha do somatório de caractere
   da diferença está fazendo trabalho de verdade.
2. A folha de Syracuse tem que ser coprima com 3, e `w(v0)+2^A t`
   percorre as três classes mod 3 quando `t` varia, então uma classe de
   `t` é inadmissível por folha. O parâmetro livre de um par real de
   folhas é uniforme numa união de classes mod 3, não em todo `Z/3^s`,
   que é hipótese mais fraca que a de `thm:fresh-digit-coupling`. Os
   vértices intermediários não são afetados (deslocam-se por
   `2^(A_i) 3^(D-i) t`, nulo mod 3). O anulamento sobrevive, e a
   identidade acima diz por quê: para uma lei dessas `muhat` some fora
   dos múltiplos de `3^(s-1)`, então `E_r(mu)=0` para `r >= 2` e a
   diagonal primitiva zera em toda escala `s >= j+2`, com todo o
   resíduo em `s = j+1`. Medido em pares reais de folhas, com `j=1`:
   `|D|` máximo é `1,000` em `fresh=2` e cai para `1e-14` em `fresh=3`
   e `fresh=4`.

**Isto não fecha H-159, e o limite é preciso.** A média que mata o
coeficiente diagonal é sobre o **parâmetro aritmético livre**, que é
justamente a aleatoriedade que `thm:fresh-digit-coupling` postula e que
E-129 também usou, de modo que a comparação é legítima. Mas O1 precisa
de cancelamento para um inteiro `v` **fixo**, onde
`S_1(xi) conj(S_2(xi))` de um par de caminhos é uma única fase de
módulo 1 e não há esperança nenhuma sobre `t` a tomar. O cancelamento
que O1 precisa tem que vir da média sobre os dois índices de caminho,
que é outra média e outro teorema. Registrado como H-162 (Regra 8e).

O que a atualização de fato estabelece: o acoplamento máximo de
`thm:fresh-digit-coupling` restringe um funcional que a rota de segundo
momento nunca avalia, e no funcional que ela avalia a ressonância
sobrevivente é exatamente o modo afim grosseiro que O1 já remove. O
número `TV = 1-3^-s` não deve ser lido como obstrução ao programa de
Fourier. A dívida aritmética de H-159 continua aberta, agora com o
alvo deslocado da média sobre o parâmetro livre para a média sobre
índices de caminho a `v` fixo.

Ver `projects/collatz/experiments/E-133-fresh-digit-moment-cancellation/`.
## Nota E-138 (2026-08-09): o lado O7 encontrou o mesmo objeto de O1

Atacando o sub-alvo de O7 (a margem de sinal uniforme de `q=3` em
H-157), o funcional que sobra é uma colisão deslocada afim,
`T_ell(4,1) = 3^ell P[F' = 4F+1 mod 3^ell]`, que é a correlação de
vizinhos `(1/M) sum_j N_j N_(j+1)` ao longo da órbita do mapa afim
`A(k)=4k+1`. É a mesma órbita e o mesmo mapa de H-161, e são os mesmos
pares consecutivos que E-132 mede.

As duas perguntas não são a mesma. E-132 mede a cauda inferior conjunta
(com que frequência os dois membros de um par consecutivo são pequenos
ao mesmo tempo) e acha antiaglomeração; O7 precisa de cota inferior
para a esperança do produto do par. Antiaglomeração empurra na direção
certa para essa cota, mas não a dá.

Isso confirma o diagnóstico de "dívida aritmética compartilhada" desta
hipótese em forma concreta: os dois lados chegam a um funcional de
momento sobre pares na mesma órbita afim, por rotas independentes. Ver
a seção datada de 2026-08-09 em H-157 e
`projects/collatz/experiments/E-138-diagonal-shifted-collision/`.
