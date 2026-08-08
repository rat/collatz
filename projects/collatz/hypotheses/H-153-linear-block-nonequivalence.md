# H-153: não equivalência de ensembles para blocos lineares

Status: fechada-confirmada após auditoria

Criada: 2026-08-07

## Enunciado

Sejam `J_0,...,J_(ell-1)` os custos geométricos dobrados independentes,
`K_ell=sum J_i`, e `B_(ell,r)` o vetor dos últimos `r` custos. Suponha

```text
r/ell -> rho in (0,1),
(k_ell-ell)/sqrt(ell) -> u.
```

Então a distância em variação total entre a lei de `B_(ell,r)`
condicionada por `K_ell=k_ell` e sua lei não condicionada converge para

```text
TV(N(rho*u, 2*rho*(1-rho)), N(0,2*rho)) > 0.
```

A mesma distância é obtida comparando apenas a soma dos custos no bloco.

## Prova

Escreva `S_(ell,r)` para a soma do bloco e
`R_(ell,r)=K_ell-S_(ell,r)`. O derivado de Radon-Nikodym da lei
condicionada do vetor do bloco depende apenas de sua soma:

```text
P(R_(ell,r)=k_ell-S_(ell,r))/P(K_ell=k_ell).
```

Logo a estatística soma é suficiente para distinguir as duas leis, e a
distância dos vetores coincide exatamente com a distância das somas.

Os custos têm momentos exponenciais uniformes. Todos, salvo um número
fixo de coordenadas iniciais, diferem de uma geométrica em `N_0` por uma
truncagem exponencialmente pequena. O teorema local do limite para o par
de somas independentes dá, na escala

```text
x=(S_(ell,r)-r)/sqrt(ell),
```

a densidade limite `N(0,2*rho)` sem condicionamento. Depois de impor
`K_ell=k_ell`, o produto das duas densidades locais é

```text
phi_(0,2*rho)(x) phi_(0,2*(1-rho))(u-x) / phi_(0,2)(u),
```

que é a densidade de `N(rho*u,2*rho*(1-rho))`. Caudas exponenciais
uniformes promovem a convergência local para convergência em variação
total. As variâncias são distintas para `rho in (0,1)`, portanto o
limite é estritamente positivo.

Para `u=0`, o limite tem a forma fechada

```text
2[Phi(sqrt(-log(1-rho)/rho))
  -Phi(sqrt(-(1-rho)log(1-rho)/rho))].
```

## Alcance

H-146 prova equivalência dos vetores para `r=o(ell)`. H-153 mostra que
essa escala é afiada para os vetores latentes de custo. A projeção do
vetor no resíduo módulo `3^r` pode apagar a estatística soma. Portanto o
teorema não prova não equivalência das medidas residuais e não resolve a
estimativa de Fourier em precisão linear de O4.

Verificação independente: E-122.

## Rodada crítica

Foram separados três níveis de informação. A igualdade de distâncias
entre vetor e soma é finita e exata, pois o derivado condicionado é
mensurável em relação à soma. A passagem gaussiana usa um teorema local
do limite, não apenas convergência fraca, e as caudas exponenciais dão a
uniformidade integrável necessária. Finalmente, a projeção residual é
uma aplicação muitos-para-um, portanto nenhuma cota inferior de TV foi
transferida para os resíduos.

E-122 foi comparado com convolução direta variável por variável para
todos os segmentos iniciados nos índices 0, 1, 2 e 3, com comprimentos
de 1 a 8 e somas até 40. O erro máximo ficou abaixo de `2e-14`.
