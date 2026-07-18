# E-100 — Massa de colisão K_ℓ da medida de Syracuse: teste da hipótese L²

Hipótese relacionada: [`H-126-regime2-decorrelacao-agregados-irmaos-estrutura-exata.md`](../../hypotheses/H-126-regime2-decorrelacao-agregados-irmaos-estrutura-exata.md)

## O que foi feito

Teste computacional decisivo, pedido pelo advisor antes de formalizar o
"lema do regime 2" (H-115/H-126): o Fable propôs um Lema 2' condicional
cuja hipótese é K_∞ := lim_ℓ K_ℓ < ∞, onde

    K_ℓ := 3^ℓ · Σ_y P(Syrac(Z/3^ℓZ) = y)² = 3^ℓ · P(Syrac_ℓ = Syrac'_ℓ)

é a massa de colisão normalizada da medida de Syracuse de Tao (2022)
— equivalentemente, a densidade f = dμ/d(Haar) pertence a L²(Z_3).

Calculamos K_ℓ EXATAMENTE (a menos de arredondamento de ponto
flutuante double, sem truncar a cauda geométrica de forma
significativa) via uma recursão derivada nesta sessão a partir da
identidade F_n(a) = 2^{-a_1}·(1+3·F_{n-1}(a_2,...,a_n)) de Tao (eq.
1.22/1.29) e da propriedade memoryless de Geom(2): a lei μ_n de F_n
satisfaz o ponto fixo

    μ_n(y) = (1/2)·ν(2y mod 3^n) + (1/2)·μ_n(2y mod 3^n)

onde ν = lei de 1+3·F_{n-1}. Como F_n nunca é múltiplo de 3 (Remark
1.15 de Tao) e 2 é raiz primitiva mod 3^n para todo n, o suporte inteiro
de μ_n vive numa única órbita cíclica de tamanho 2·3^{n-1} sob
multiplicação por 2; ao longo dela a equação acima é uma recursão
linear circular, resolvida por série geométrica truncada (o kernel
(1/2)^s decai tão rápido que truncar em s=100 é irrelevante em ponto
flutuante).

## Resultado

K_ℓ NÃO satura — cresce de forma limpa e consistentemente linear até
ℓ=17 (o limite prático testado), com incrementos ΔK_ℓ convergindo
monotonamente para ≈0,47 (de 0,476 em ℓ=2 a 0,472 em ℓ=17, sem sinal
de reversão). **A hipótese L² (K_∞<∞) FALHA** — refutação empírica
direta, não apenas "em aberto". Isso mata o Lema 2' condicional do
Fable pela mesma parede do regime 3: o "lema do regime 2" não é um
degrau mais fácil que o regime 3, é irmão dele, e agora com evidência
computacional de que a condição extra que o salvaria é falsa. Ver
H-126 para a análise completa e o teorema de estrutura que sobrevive
(a componente grosseira exata, Prop. 2 — essa parte é positiva e
demonstrada).

Checagem de sanidade: K_1 = 5/3 exato (calculado à mão a partir de
P(Syrac_1=1)=1/3, P(Syrac_1=2)=2/3 — bate com o script, erro <1e-10).

## Arquivos

- `experiment_k_ell.py` — script único: recursão da lei de F_n via
  DP na órbita cíclica, cálculo de K_ℓ para ℓ=1..17, ajuste log-log
  grosseiro do expoente de crescimento.

## Reproduzir

```
python3 experiment_k_ell.py
```

Custo: ℓ≤14 é instantâneo; ℓ=17 leva ~55s (dominado pelo `np.roll`
sobre um array de tamanho 2·3^16≈86 milhões, ~100 vezes). Não subir
muito além de ℓ=18-19 sem necessidade — o custo por nível escala
~3x (tamanho da órbita triplica).
