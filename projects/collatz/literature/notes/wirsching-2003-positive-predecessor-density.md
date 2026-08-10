# Wirsching (2003), "On positive predecessor density in 3n+1 dynamics"

Arquivo local: `../papers/132_Wirsching-2003-Positive-Predecessor-Density.pdf`
18 páginas, A4, marcado pelo próprio autor como *preliminary version*.
Afiliação impressa: Mathematisch-Geographische Fakultät, Katholische
Universität Eichstätt, D-85071 Eichstätt.

Lido na íntegra em 2026-08-09 (E-135 / H-134). Antes disso esta linha de
pesquisa usava paráfrase de segunda mão para o conteúdo das três
conjecturas, e o enunciado da Conjectura 2 estava sendo atribuído a algo
que o artigo não diz. Esta nota existe para que isso não se repita.

## Alvo

**Positive Density.** Os conjuntos de predecessores de `T` têm densidade
positiva uniforme de predecessores em `A = {a em N : a != 0 mod 3, a não
cíclico}`, no sentido da Definição 1: existe `c > 0` com
`liminf_n |{x em P_f(a) : x <= n}|/n >= c/a` para cada `a` em `A`. A
constante `c` não depende de `a`. O autor observa que a asserção parece
logicamente independente da conjectura 3n+1.

## A cadeia, com o que é provado e o que é conjecturado

```text
Teorema 1   provado      (?1) => Positive Density
Conjectura 1             (?2) => (?1)
Teorema 2   provado      (?3) => (?2)
Conjectura 2             (?4) => (?3)
Conjectura 3             (?5); a implicação (?5) => (?4) é provada na seção 7
```

Objetos. `e_ell(k,a)` (funções Elka) conta caminhos com `ell` ramos `T_1`
e `k` ramos `T_0` terminando em `a`. `g_ell(k,a)` são geradores de
suporte compacto definidos pela recursão (2.1),
`g_(ell+1)(k,a) = soma_{0<=j<2*3^ell} g_ell(k-j, (2^(j+1)a-1)/3)`, com
`g_0(k,a) = [k=0][a em Z_3]`. Ligação: `e_ell = p_ell * g_ell`, com
`p_ell(m)` o número de modos de pagar `m` com moedas `c_0=1`,
`c_j=2*3^(j-1)`. Médias de Haar: `ebar_ell(k) = binom(k+ell,k)/(2*3^(ell-1))`.
`A_delta` são as sequências inteiras com `|ell - k_ell| <= delta*sqrt(ell)`
para todo `ell` (1.5).

Enunciados literais:

```text
(?1)  liminf_ell e_ell(k_ell,a)/ebar_ell(k_ell) >= mu
      uniformemente para (k_ell) em A_delta.

(?2)  liminf_ell g_ell(k_ell,a)/gbar_ell(k_ell) >= mu_1
      uniformemente para (k_ell) em A_delta1.

(?3)  gtilde_ell(x_ell,a) >= mu * integral_{Z_3^x} gtilde_ell(x_ell,a) da
      uniformemente para (x_ell) em Atilde_delta e ell >= ell_0.

(?4)  liminf_ell (W_3^ell chi_1)(x_ell) / (W_3^ell chi_0)(x_ell) >= mu
      uniformemente para (x_ell) em Atilde_delta,
      chi_0 = 1_[0,2/3],  chi_1 = 1_[1/3,1].

(?5)  lim_ell phi(z_ell)/phi_0(z_ell) = c > 0
      uniformemente para (z_ell) em Atilde_delta5.
```

`W_3 f(x) = (3/2) integral_{3x-2}^{3x} f`, com ponto fixo `phi` único em
`L^1([0,1])` (Corolário 7), e `phi_0` é a assintótica de Berg e Krüppel
(7.11).

## Três coisas que só ficam visíveis na fonte

1. **A Conjectura 2 é `(?4) => (?3)`**, e `(?4)` não menciona os
   geradores. É um enunciado só sobre `W_3`. A conjectura pede uma cota
   inferior pontual na coordenada 3-ádica a partir de uma hipótese que
   não carrega informação nenhuma sobre essa coordenada. A única ponte
   oferecida é o Teorema 3 (`S_ell -> S_infty` na topologia forte,
   uniforme em famílias equicontínuas limitadas).

2. **`(?3)` e `(?2)` são a mesma desigualdade.** Como
   `gtilde_ell(x,a) = gamma_ell * g_ell(floor(3^ell x), a)` com
   `gamma_ell` constante em `a`, o fator cancela dos dois lados. O que
   o Teorema 2 acrescenta é troca de quantificador: `(?3)` pede a
   desigualdade em todo `ell >= ell_0` e toda unidade; `(?2)` é um
   `liminf` em `ell` a cada `a`.

3. **O Teorema 1 só consome `a` inteiro.** A Definição 1 e a conclusão
   do Teorema 1 falam de `a` em `N`, não cíclico, `a != 0 mod 3`. As
   condições `(?2)` e `(?3)`, enunciadas sobre `Z_3^x`, são
   estritamente mais fortes do que a cadeia usa.

## Estado nesta linha de pesquisa

- Conjectura 1: provada em H-133, com a identidade de funções geradoras
  e a estimativa de cauda da convolução. Registrada no paper 01 como
  `thm:wirsching-conj1`.
- Conjectura 3: testada numericamente com erro certificado até
  `ell = 500` (paper 01, `thm:conjecture3`).
- Conjectura 2: aberta. Ver H-134 (seção de 2026-08-09), H-167, H-168 e
  E-135.

## Referências que o artigo usa e que ainda não foram lidas aqui

- Berg, L., e Krüppel, M., *On the Solution of an Integral-Functional
  Equation with a Parameter*, J. Anal. Appl. 17 (1998), 159-181.
  Fonte da assintótica `phi_0` de (7.11) e da seção 9 citada como
  sugestão de que a Conjectura 3 é verdadeira.
- Wirsching, G. J., *Balls in constrained urns and Cantor-like sets*,
  J. Anal. Appl. 17 (1998), 979-996. Interpretação combinatória de
  `gbar_ell(k)`.
- Wirsching, G. J., *A functional differential equation and 3n+1
  dynamics*, Fields Institute Communications 29 (2001). O Teorema 3
  aqui é apresentado como variante do teorema 4.1 desse artigo.

O livro Springer LNM 1681 (1998) está em
`../papers/131_Dynamical-System-3n1-Function-Wirsching-Book.pdf` e é a
referência [4] do artigo, usada para os capítulos III e IV.
