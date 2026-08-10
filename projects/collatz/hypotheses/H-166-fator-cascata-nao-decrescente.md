# H-166: o fator de cascata entre níveis é não decrescente, beta_eff <= 1,882712 incondicional

Status: closed-confirmed

Criada: 2026-08-09

Origem: subproduto de uma tentativa (Regra 11b, consulta a modelo mais
forte) de fechar a Questão 2 de H-161 (anti-concentração de pares) via
um programa de somas de Weyl. O programa em si fecha como insuficiente
(ver H-161, "Terceira rodada"); montá-lo produziu este resultado
incondicional separado, registrado aqui por exigência da Regra 8e.

## Enunciado

Com `N_ell(u) := 3^ell mu_ell(u)` e, para `u` unidade mod `3^ell`,

```text
R_ell(u) := N_ell(u) / N_(ell-1)(u mod 3^(ell-1))
```

(F4, a identidade de pushforward, já dava `E[R_ell]=1` sobre cada trinca
de irmãos, logo `min_u R_ell <= 1`). O resultado novo é a outra ponta:

**Teorema.** `min_u R_ell(u)` é não decrescente em `ell`.

**Prova.** F1 dá `N_ell(y) = 3*2^-t0(y)*W_ell(k0(y))`, com
`W_ell(k) = sum_j 4^-j N_(ell-1)(A^j k)`. Como `t0` e `k0` são
compatíveis entre níveis adjacentes (verificado abaixo, é o passo que
sustenta tudo), os fatores `3*2^-t0` cancelam na razão e

```text
R_ell(y) = W_ell(k) / W_(ell-1)(k mod 3^(ell-2)),   k = k0(y).
```

`A` é fórmula inteira, então numerador e denominador percorrem o MESMO
índice `j` com os MESMOS pesos `4^-j`. Substituindo
`N_(ell-1)(A^j k) = N_(ell-2)(A^j k')*R_(ell-1)(A^j k)` exibe `R_ell(k)`
como combinação convexa de valores `R_(ell-1)(A^j k)`, pesos
`4^-j N_(ell-2)(A^j k')/W_(ell-1)(k') >= 0` somando 1. Uma combinação
convexa fica entre o mínimo e o máximo do que ela promedia, logo
`min R_ell >= min R_(ell-1)`. QED.

**Consequência.** `N_ell(u) = N_(ell-1)(u mod 3^(ell-1))*R_ell(u)`
ponto a ponto, logo `min N_ell >= (min R_L)^(ell-L) min N_L` para
qualquer nível `L` fixo e todo `ell>=L`, dando

```text
limsup beta_eff <= 1 + log(1/min R_L)/log 3
```

**Verificação (Regra 8c, feita antes de aceitar o resultado, não depois):**

- A identidade de ponte entre indexações (`k0` calculado no resíduo-pai
  `y mod 3^(ell-1)` via a construção de nível `ell-1` coincide com
  `k0(y) mod 3^(ell-2)` calculado no nível `ell`, e o mesmo para `t0`) é
  o único passo do argumento que não é reindexação trivial. Checada de
  forma EXAUSTIVA (não amostrada) em `ell=3` a `8`, usando a mesma
  construção `t0_and_k0` já verificada em `E-131/fact_a_check.py`: zero
  exceções em 4374 unidades no maior nível testado.
- Monotonicidade de `min R` verificada por asserção em aritmética
  racional exata até `ell=10`, e em ponto flutuante até `ell=16`, sem
  falhar em nenhum nível.
- `min N` cruzado contra os valores já registrados de forma
  independente em E-127: bate em `ell=12,14,16`.

## Valores certificados (aritmética racional exata, `E-134`)

```text
 ell   min R_ell (exato)     beta bound
   2   2/7                    2.140314
   8   4365-bit ratio         1.888066
  10   39355-bit ratio        1.882712
```

`limsup beta_eff <= 1.882712`, melhorando a melhor cota incondicional
registrada no projeto até aqui (`2.306270`, ver H-158).

## Onde o método satura

Em ponto flutuante até `ell=16`, `min R_ell` continua subindo, perto de
`0.3803`, e `N_max/N_(ell-1)` real roda entre 0,93 e 0,97 contra o fator
`0,38` que a prova garante. Essa distância é exatamente o que a
desigualdade de par de H-161 (Questão 2) fecharia, se provada. Esta
rota, sozinha, não passa de `beta_eff ~ 1,88` e não chega a 1.

## Reconciliação com o esboço de H-158

H-158 registra, como esboço não rederivado linha a linha, que nenhuma
desigualdade usando só `c_(ell-1)` (ou qualquer estatística de ordem de
um único nível) melhora `beta <= 2,31`. Este resultado não contradiz
isso: `min R_L` não é uma estatística de um único nível, é uma
quantidade ENTRE níveis (compara `mu_ell` com `mu_(ell-1)` em resíduos
casados pela identidade de órbita afim), fora do escopo do esboço de
H-158.

## Impacto em H-161

Recalibra o limiar de `kappa` que tornaria a Questão 2 (desigualdade de
par) útil: com a referência agora em `1,882712`, só vale a pena atacar
Q2 mirando `kappa > 0,567` (antes, `kappa > 0,383` já bastava para
melhorar a cota então vigente).

## Verificação

`projects/collatz/experiments/E-134-weyl-sum-pair-anticoncentration/cascade_factor_bound.py`.
