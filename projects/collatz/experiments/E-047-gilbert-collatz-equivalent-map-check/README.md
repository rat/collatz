# E-047 — Verificação do paper #003 (Jonathan S. Gilbert, "A Collatz-Equivalent Map on the Nonzero Integers")

## Objetivo

Verificar "A Collatz-Equivalent Map on the Nonzero Integers" (Jonathan
S. Gilbert, preprints.org, 14 páginas). Paper **não** alega provar a
conjectura ("No proof of the conjecture is claimed; the aim is a
coordinate system in which its dynamics are easier to see").

## O que fizemos

Reimplementamos o mapa acelerado T, a bijeção J entre as classes
residuais relevantes [1]₃∪[2]₃ e os inteiros não-nulos Z*, o mapa
conjugado K, e o mapa acelerado K̂ (que contrai corridas por inteiros
negativos pares). Testamos independentemente:

1. **Conjugação K=J∘T∘J⁻¹** (Teorema 5): confirmada em 1000 casos.
2. **Pruning dos múltiplos de 3** (Lemma 2/Teorema 4): confirmado até
   n=20000 — nenhum n fora de [0]₃ mapeia para dentro, e toda órbita
   que começa em [0]₃ sai em ≤v₂(n)+1 passos e nunca retorna.
3. **"Conjectura equivalente"** (Teorema 6): confirmada em 4999 casos
   (a tradução J/K preserva corretamente qual órbita converge — não é
   um teste da conjectura em si, só da correção da tradução).
4. **Mapa acelerado K̂** (Lemma 4) e o exemplo do próprio paper
   (n=-160 → K̂(n)=608, Remark 5): confirmado exatamente.
5. **Fórmula dos pais** (Proposição 3): confirmada via busca por força
   bruta no grafo, para vários k.
6. **Proposição 4** (identidade algébrica entre duas expressões via
   lifting-the-exponent, e conexão com OEIS A254046): confirmada — as
   duas fórmulas coincidem entre si, com a contagem direta de pais, **e
   com a sequência real A254046** (ver nota abaixo).

## Nota sobre acesso ao OEIS

A primeira tentativa de confirmar a sequência OEIS A254046 usou
`WebFetch` em `oeis.org` — o site bloqueou o acesso automatizado (403),
mesmo padrão de outros hosts do projeto. Por indicação do diretor
científico, refizemos via `curl` com um User-Agent de navegador
(`curl -s -A "Mozilla/5.0 ..." https://oeis.org/A254046/b254046.txt`),
que funciona sem bloqueio nesse site (ver memória
`feedback_oeis_access_method.md`). **A sequência real confirma
exatamente** a fórmula do paper — Proposição 4 correta em todos os
aspectos testados.

## Resultado

**Nenhum erro encontrado** em nenhuma reivindicação testada. Paper de
alta qualidade — mesmo padrão de honestidade e rigor de H-042 (Williams)
e H-044 (Fu/Liu/Wang): distingue com cuidado o que é teorema provado do
que é conjectura equivalente (mais fraca) e do que é analogia/heurística
(Seção 7, explicitamente rotulada como tal, "by itself it proves
nothing").

Ver `hypotheses/H-047-gilbert-collatz-equivalent-map-review.md`.

## Como rodar

```
/home/rat/.venv/bin/python3 experiment.py
```
