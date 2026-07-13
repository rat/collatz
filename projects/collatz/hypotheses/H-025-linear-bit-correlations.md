# H-025 — Busca de invariantes lineares entre bits de n e bits de m=(3n+1)/2^a

Status: refutada (resultado negativo, com mecanismo totalmente explicado)
Criada em: 2026-07-13
Origem: item #9 de uma quarta lista de ideias externas ("busca sistemática
de invariantes lineares em representações binárias, sobre GF(2) ou Z"),
avaliada como a mais barata e diretamente testável das 15 sugestões dessa
lista (ver `literature/external-ideas-review.md`).

## Enunciado

Existe uma correlação linear (estilo criptoanálise linear: bias entre
`bit_i(n)` e `bit_j(m)`) entre um bit qualquer de n e um bit qualquer de
m = próximo ímpar da órbita, que não seja explicada pela determinação
2-ádica trivial de baixa ordem — isto é, um invariante estrutural genuíno
e ainda não catalogado nos bits do problema?

## Como foi testado

Amostra de 2-6 milhões de n ímpares aleatórios (50 bits), calculado m e a
via `accel_step_vec` (vetorizado com numpy). Matriz de bias (correlação
±1, estilo Pearson) entre `bit_i(n)` e `bit_j(m)` para uma janela de bits,
SEM condicionar em a (a varia por amostra, como acontece de fato).

Resultado inicial: vários pares `(bit_i(n), bit_{i-4}(m))` mostraram bias
significativo (~0.02, z>28) e aparentemente **não decrescente** com i até
i=23 — candidato a invariante genuíno.

## Diagnóstico do mecanismo (decisivo)

Condicionando a amostra em cada valor fixo de a (1 a 5) separadamente:

| a | bias(bit_i(n), bit_{i-4}(m)), i=8..19 |
|---|---|
| 1 | ~0.000 (ruído) |
| 2 | ~0.000 (ruído) |
| 3 | ~0.001 (ruído) |
| **4** | **~0.33 (constante, forte)** |
| 5 | ~0.000 (ruído) |

O sinal agregado de ~0.02 é **inteiramente explicado** pela fatia a=4
(probabilidade 1/16≈0.0625): 0.0625 × 0.33 ≈ 0.0206 — bate exatamente com
o valor agregado observado. Quando a=k, por definição m=(3n+1)/2^k
**exatamente**, então bits de m na posição j correspondem exatamente a
bits de (3n+1) na posição j+k — um deslocamento algébrico trivial, não
uma descoberta nova. A correlação residual de ~0.33 (não 1.0) é apenas a
assinatura conhecida de propagação de carry em adição binária (3n+1=2n+n).

Confirmação adicional: fixando a=1 e olhando `bit_i(n)` vs `bit_i(m)` (o
alinhamento correto para esse a), a correlação cai a ruído puro (|bias|<
0.002) já a partir de i=1 — nenhum efeito de longo alcance mesmo no caso
mais simples.

## Conclusão

**Não existe invariante linear novo.** Toda correlação bit-a-bit
observada entre n e m se reduz a duas coisas já conhecidas: (1) o valor
exato de a (conhecido desde H-005/H-007), que determina um deslocamento
algébrico exato; e (2) o bias clássico e de curto alcance da propagação
de carry em adição binária, que já não carrega informação nova sobre
Collatz especificamente. Isso **fecha com mecanismo explícito** (mais
forte que a ambiguidade deixada por H-020) a pergunta se há vazamento de
informação linear entre bits: não há, além do já conhecido.

## Atualizações

- 2026-07-13: hipótese testada e refutada com mecanismo totalmente
  identificado. Resultado negativo limpo — encerra a via de "busca de
  invariantes lineares em bits" (item #9 de uma lista externa) com
  explicação, não apenas com busca exaurida.
