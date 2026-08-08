# H-156: renormalização exata da colisão em ordem logarítmica

Status: fechada-confirmada após auditoria algébrica e computacional

Criada: 2026-08-07

## Enunciado

Seja `mu_ell` a lei de Syracuse módulo `3^ell`, seja
`M=3^(ell-1)` e reordene a lei anterior por

```text
a_j = mu_(ell-1)((4^j-1)/3 mod M),  0 <= j < M.
```

Essa é uma permutação de todos os resíduos módulo `M`. Para a
transformada não normalizada

```text
A_m = sum_j a_j exp(-2*pi*i*m*j/M),
```

vale a identidade exata

```text
K_ell = sum_m 15/(17-8*cos(2*pi*m/M)) |A_m|^2.
```

Como `K_(ell-1)=sum_m |A_m|^2`, H-155 implica

```text
E_ell = sum_m (15/(17-8*cos(2*pi*m/M))-1) |A_m|^2.
```

Logo o crescimento da massa de colisão é equivalente a um balanço
espectral explícito na coordenada de logaritmo discreto. Modos com
`cos(2*pi*m/M)>1/4` têm peso positivo no incremento e os demais têm
peso não positivo.

## Derivação

Escreva `y_k=2^k mod 3^ell`, `x_k=mu_ell(y_k)` e
`n_k=nu_ell(y_k)`, onde `nu_ell` é a lei de
`1+3 F_(ell-1)`. A recursão de Syracuse dá

```text
x_k = (n_(k+1)+x_(k+1))/2.
```

O período de `2` módulo `3^ell` é `2M`. Os valores de `n_k` são zero
para índices ímpares e `n_(2j)=a_j`. Definindo `u_j=x_(2j)`, as duas
etapas consecutivas dão

```text
u_j = (a_(j+1)+u_(j+1))/4,
x_(2j+1)=2u_j.
```

Assim

```text
sum_k x_k^2 = 5 sum_j u_j^2.
```

No caráter `z=exp(2*pi*i*m/M)`, o filtro circular de `a` para `u`
tem multiplicador `z/(4-z)`, cujo módulo ao quadrado é
`1/(17-8 cos(2*pi*m/M))`. Parseval e `3^ell=3M` fornecem o fator 15.

## Auditoria

- O mapa `j -> (4^j-1)/3 mod 3^(ell-1)` é bijetivo porque `4` tem
  ordem `3^(ell-1)` módulo `3^ell`.
- A transformada usa a convenção não normalizada, de modo que
  `M sum_j a_j^2=sum_m |A_m|^2`.
- E-125 calcula `K_ell` pela recursão original de E-100 e pelo
  multiplicador acima. Os dois lados coincidem até o nível 12, com
  erro absoluto máximo abaixo de `3e-15`.
- A busca dirigida encontrou a recursão de Syracuse e o uso de entropia
  de colisão em Tao, mas não encontrou esta diagonalização em ordem
  logarítmica. Isso não constitui uma alegação global de prioridade.

## Alcance

A identidade substitui a pergunta sobre crescimento de `K_ell` por
uma pergunta sobre a distribuição de `|A_m|^2` entre arcos do círculo.
Ela não fornece, por si só, um limite inferior uniforme para `E_ell`.
Portanto não prova divergência de `K_ell` nem singularidade da medida
de Syracuse. O7 continua aberto.
