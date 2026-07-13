# E-025 — Busca de invariantes lineares entre bits de n e bits de m

Hipótese relacionada: [`H-025-linear-bit-correlations.md`](../../hypotheses/H-025-linear-bit-correlations.md)

Origem: item #9 de uma quarta lista de ideias externas — busca de
invariantes lineares (GF(2)/Z) em representações binárias.

## O que foi testado

Correlação (bias) estilo criptoanálise linear entre `bit_i(n)` e
`bit_j(m)`, onde m é o próximo ímpar da órbita acelerada, para todos os
pares numa janela de bits, sem condicionar no valor de a (que varia por
amostra).

## Dependências

Requer `numpy` (não estava instalado no ambiente do sistema; instalado no
venv `/home/rat/.venv` durante esta sessão). Rodar com:
`/home/rat/.venv/bin/python3 experiment.py [N_SAMPLES] [WINDOW] [BIT_LENGTH]`

## Resultado

Sinal aparente (~0.02, altamente significativo, z>28) em offset fixo
(bit_i(n) vs bit_{i-4}(m)) que parecia não decair com i — candidato a
invariante genuíno. Diagnóstico: condicionando em cada valor fixo de a
separadamente, o sinal só aparece quando a=4 (bias~0.33), e sua
contribuição ponderada pela probabilidade (1/16) reproduz exatamente o
valor agregado (0.0625×0.33≈0.0206). Mecanismo: quando a=k, m=(3n+1)/2^k
exatamente — um deslocamento algébrico trivial, e a correlação residual é
só o bias clássico de propagação de carry em adição binária (3n+1=2n+n),
de curto alcance (confirmado nulo além de i=1 quando a=1 é fixado).

## Conclusão

Nenhum invariante linear novo encontrado. Toda correlação observada é
explicada por (1) o valor exato de a (já conhecido) e (2) bias clássico de
carry em adição binária, sem informação nova sobre a estrutura do
Collatz. Resultado negativo limpo, com mecanismo identificado.
