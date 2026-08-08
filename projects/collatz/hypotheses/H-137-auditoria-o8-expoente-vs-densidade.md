# H-137: auditoria de O8, expoente versus densidade

Status: fechada-confirmada; conjectura corrigida

Criada: 2026-08-07

## Erro encontrado

O paper afirmava, para `q=3`,

```text
N_u(x) ~ x.
```

Mas `N_u` conta inteiros ímpares distintos, logo
`N_u(x)<=ceil(x/2)`. A fórmula era impossível. Também não é o enunciado
da Growth Exponent Conjecture.

As fontes primárias de Applegate--Lagarias e
Kontorovich--Lagarias definem

```text
eta_q(u) = lim log N_u(x)/log x
```

e conjecturam `eta_3(u)=1`. Para `5x+1`, a previsão correspondente é
`N_u(x)=x^(eta_5+o(1))`, com `eta_5` próximo de `0.6505`. Nenhuma dessas
afirmações fornece uma constante assintótica ou densidade natural
positiva.

## Formulação corrigida

```text
N_u(x)=x^(alpha_-(q)+o(1)).
```

Para `q=3`, isso coincide com a Growth Exponent Conjecture. Para
`q>=5`, prevê expoente estritamente menor que um. A transição é de
expoente, não de densidade.

## Auditoria do experimento KL--Volkov

O intervalo bootstrap `[0.633,0.645]` condiciona na janela de medição.
As inclinações locais ainda crescem na última janela, portanto existe
viés sistemático não incluído no intervalo. O experimento favorece a
direção da previsão de Kontorovich--Lagarias, mas não exclui um valor
assintótico e não resolve a disputa com Volkov. O manuscrito foi
corrigido nesse sentido.

## Relação com O7

Remover a assíntota `N_u~W_u x^alpha` tornou `W_u` indefinido. O7 agora
é formulado com uma raiz `U` Haar-uniforme em `Z_q` e os fatores
coerentes `Z_k(alpha_-;U mod q^k)`. A existência e não degenerescência
do limite fazem parte da conjectura aritmética.

