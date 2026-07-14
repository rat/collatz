# E-040 — Verificação do Teorema 5.1 do paper #004 (Seymour, Steiner Sentence Length)

Hipótese relacionada: [`H-040-seymour-steiner-sentence-length-error.md`](../../hypotheses/H-040-seymour-steiner-sentence-length-error.md)

## O que foi testado

O paper #004 (`literature/papers/004_First-Principles-Derivation...pdf`)
prova, com verificação formal alegada em Lean 4/Mathlib, que
P(comprimento da sentença Steiner = k) = 3^(k-1)/4^k, e argumenta
explicitamente contra o modelo "ingênuo" P(k)=(1/2)^k. Reimplementamos
as definições exatas do paper (Def 1.2, 1.3, Teorema 2.1) do zero para
verificar independentemente.

## Resultado

- **Teorema 2.1 (matriz de transição mod 8) — CONFIRMADO** exatamente,
  por amostragem direta de 200.000 inteiros ímpares aleatórios.
- **Teorema 5.1 (distribuição 3^(k-1)/4^k) — REFUTADO**. A simulação
  direta (300.000 amostras, seguindo o protocolo exato do Apêndice B do
  próprio paper) bate com **(1/2)^k** — exatamente o modelo "ingênuo"
  que o paper argumenta ser incorreto — e **não** com 3^(k-1)/4^k.
- **Contraexemplo concreto, aritmética exata** (sem aleatoriedade):
  n=68567 (≡7 mod8) → S(n)=102851 (≡3) → S(S(n))=154277 (≡5). A
  sequência de resíduos [7,3,5] casa com o regex `(7*3)?(1|5)` como
  **uma única palavra Steiner**, terminando em 5 — ou seja, uma
  sentença de comprimento 1 com b₀≡7, **não** b₀≡5. Isso contradiz
  diretamente a prova do Teorema 5.1 do paper, que conta **apenas**
  b₀≡5 como fonte de sentenças de comprimento 1.

## Diagnóstico do erro (ver H-040 para detalhes completos)

A recursão das Seções 3–5 do paper aplica a matriz de transição de UM
PASSO de Syracuse (Teorema 2.1) como se fosse a transição
entrada-a-entrada entre PALAVRAS consecutivas. Isso é válido para
entradas 1 e 5 (que são sempre palavras de exatamente 1 passo), mas
**não** para entradas 3 e 7 (que abrangem 2+ passos): `P[3][5]=1/2` e
`P[7][3]` (seguido do passo 3→5) descrevem o **próprio terminal da
palavra atual**, não a entrada de uma "próxima palavra". Ao tratar como
se fosse sempre uma transição para a próxima palavra, o paper nunca
"gasta" a massa de probabilidade que deveria fechar a sentença ali
mesmo, subestimando a taxa real de fechamento (1/2 por palavra, não a
taxa 1/4 implícita na fórmula 3^(k-1)/4^k).

## Reproduzir

`python3 experiment.py` (~1s, sem dependências externas)

## Status

Achado importante: o teorema central do paper parece estar incorreto,
apesar da alegação de verificação formal em Lean 4/Mathlib. Não temos
acesso ao código Lean para apontar a linha exata, mas a evidência
(matriz de transição confirmada + contraexemplo de aritmética exata +
simulação em larga escala) é forte e reproduzível.
