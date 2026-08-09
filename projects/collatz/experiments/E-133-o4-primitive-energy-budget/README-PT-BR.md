# E-133: o orçamento l2 disponível para O4 (regime 3)

Hipóteses relacionadas:
[`H-115`](../../hypotheses/H-115-tao-bivariate-extension-three-precision-regimes.md)
(três regimes de precisão, O4),
[`H-155`](../../hypotheses/H-155-multiscale-parseval-o5-o7.md)
(Parseval multiescala),
[`H-154`](../../hypotheses/H-154-primitive-fibre-energy.md)
(identidade de energia por fibras novas),
[`H-162`](../../hypotheses/H-162-emparelhamento-bilinear-irmaos-sem-decaimento.md)
(a rota que esta medição deixa de pé).

## O que mede

O4 pede controle exponencial da cauda de frequência fina em precisão
linear, depois de separados os modos de condutor sublinear. A única
implementação que a rota de segundo momento fornece é uma cota de
Cauchy-Schwarz sobre o emparelhamento das somas de caracteres das duas
irmãs, e o orçamento que essa cota gasta é a energia de Fourier
primitiva da lei de Syracuse acima dos condutores separados. Este script
mede esse orçamento diretamente.

Para a lei de Syracuse `mu_ell` em `Z/3^ell Z`:

    K_ell = 3^ell * sum_x mu_ell(x)^2
    E_ell = soma sobre xi com 3 não dividindo xi de |muhat_ell(xi)|^2
    sup_ell = máximo sobre os mesmos xi de |muhat_ell(xi)|

`mu_ell` vem da recursão exata de E-100, validada lá bin a bin contra
Monte Carlo direto em `ell = 3, 4`.

## Resultados (níveis 1 a 15, exatos até arredondamento em dupla precisão)

**(a) Três expressões para a energia primitiva coincidem.** `K_ell -
K_(ell-1)` (identidade de Parseval multiescala de H-155), a soma direta
por FFT sobre frequências primitivas e a forma de fibras novas de H-154
batem até `2.1e-15` em todos os níveis. H-155 e H-154 ficam assim
verificadas aqui de forma independente de E-124 e E-123, sobre a própria
lei de Syracuse.

**(b) A separação de condutores sublineares remove uma parcela
decrescente do orçamento.** A fração `(K_r - 1) / (K_ell - 1)` da massa
l2 primitiva total que vive em condutores até `3^r`:

| ell | r = 3 | r = ell/2 |
|-----|-------|-----------|
| 8   | 0,408 | 0,526     |
| 10  | 0,330 | 0,521     |
| 12  | 0,276 | 0,517     |
| 14  | 0,238 | 0,514     |

Ao longo de qualquer sequência sublinear a parcela cai; ao longo de
`r = ell/2` fica em torno de um meio. O resíduo `K_ell - K_r` cresce
linearmente em `ell` nas duas colunas.

**(c) O espectro primitivo fica na escala de raiz quadrada, e acima
dela.** `E_ell` permanece perto de `0,47` em toda a faixa: 0,4762 em
`ell = 2`, caindo para 0,4616 em `ell = 3`, depois subindo até 0,4708 em
`ell = 15`, com um recuo pequeno em `ell = 7`. Logo o coeficiente
primitivo em RMS fica entre `0,832` e `0,845` vezes `3^(-ell/2)`, sem
tendência que o tire dessa escala. O máximo é muito maior e cresce
contra a mesma escala:

| ell | sup * 3^(ell/2) | sup / rms | argmax xi |
|-----|-----------------|-----------|-----------|
| 5   | 2,02            | 2,4       | 32        |
| 10  | 9,30            | 11,1      | 54953     |
| 15  | 61,69           | 73,4      | 262144    |

A razão por nível `sup_ell / sup_(ell-1)` sobe ao longo da faixa, de
0,6546 em `ell = 2` para 0,8513 em `ell = 15` (não monotonamente; há
recuos em `ell = 9` e `ell = 12`), contra o `3^(-1/2) = 0,5774` que uma
cota uniforme de raiz quadrada exigiria. O
maximizador fica na órbita multiplicativa de `1` por duplicação em quase
todos os níveis, que é onde vive o suporte de `mu_ell`.

## Status destes números

Medição de nível finito, não prova. `K_ell` é não decrescente (H-138),
então nenhuma faixa finita separa convergência de divergência; H-140
registra essa correção e ela continua valendo aqui. O que a faixa mostra
é o tamanho e o formato do orçamento nos níveis alcançáveis, e ambos
estão longe do que a implementação por Cauchy-Schwarz de O4 precisaria.

## Reproduzir

```
python3 primitive_energy_budget.py
```

Roda até `ell = 15` em 12 s, com pico de 1,0 GB de memória residente. O
custo por nível triplica, então não aumente `lmax` sem necessidade.
