# H-047 — Revisão do paper #003 (Gilbert, "A Collatz-Equivalent Map on the Nonzero Integers") — sem erros encontrados

Status: revisão externa concluída — paper de alta qualidade, teoremas
centrais confirmados corretos, uma identificação externa (OEIS) fica
não verificada por bloqueio de acesso (não é erro do paper)
Criada em: 2026-07-14
Origem: paper baixado manualmente pelo diretor científico (item 003 da
coleção, `literature/papers/003_Collatz-Equivalent-Map-Nonzero-Integers.pdf`,
preprints.org, doi:10.20944/preprints202607.0575.v1, 14 páginas).

## O paper

"A Collatz-Equivalent Map on the Nonzero Integers" — Jonathan S.
Gilbert, pesquisador independente. **Não alega provar a conjectura**
("No proof of the conjecture is claimed; the aim is a coordinate system
in which its dynamics are easier to see" — declarado explicitamente no
resumo). Constrói uma bijeção explícita J entre as classes residuais
onde a dinâmica de Collatz "acontece" ([1]₃∪[2]₃, já que múltiplos de 3
são inertes — nunca alcançados de fora, saem em finitos passos se
começarem dentro) e o conjunto dos inteiros não-nulos Z*, conjugando o
mapa acelerado T por J para obter K:Z*→Z* cujo grafo é isomorfo ao
grafo podado de Collatz. O sinal do iterado codifica a classe residual
mod 3 que seria descartada. Também constrói um mapa acelerado K̂ que
contrai as "corridas" por inteiros negativos pares.

## O que foi verificado (todos confirmados)

- **Conjugação K=J∘T∘J⁻¹** (Teorema 5): confirmada em 1000 casos
  (`experiments/E-047-gilbert-collatz-equivalent-map-check/`).
- **Pruning dos múltiplos de 3** (Lemma 2/Teorema 4): confirmado até
  n=20000.
- **"Conjectura equivalente"** (Teorema 6): confirmada em 4999 casos —
  a tradução J/K preserva corretamente qual órbita converge (teste de
  correção da tradução, não da conjectura em si).
- **Mapa acelerado K̂** (Lemma 4) e o exemplo do próprio paper (n=-160
  → K̂(n)=608, Remark 5): confirmado exatamente.
- **Fórmula dos pais** (Proposição 3): confirmada via busca por força
  bruta no grafo para vários k (5, 7, 14, 20, 122).
- **Identidade algébrica interna da Proposição 4**: as duas expressões
  que o paper afirma serem iguais (1+ν₃(2y-1) e ν₃(2^(2y-1)+1)) de fato
  coincidem entre si e com a contagem direta de pais — confirmado.

**Nenhum erro encontrado** em nenhuma reivindicação testável.

## Limitação honesta na verificação

A Proposição 4 também identifica a sequência resultante com OEIS
A254046. Tentamos confirmar isso via `WebFetch` em `oeis.org/A254046`
e `/b254046.txt` — o site **bloqueou o acesso automatizado (403)**,
mesmo padrão de bloqueio de outros hosts já catalogado neste projeto
(ResearchGate, SSRN, preprints.org, IEEE). Não fabricamos um valor de
referência para comparar — essa identificação específica com a
sequência externa fica **não verificada** (nem confirmada nem
refutada), diferente da matemática interna da proposição (que
verificamos ser correta de forma independente). Isso não é reportado
como erro do paper — é uma limitação da nossa verificação.

## Por que este paper se destaca

Mesmo padrão de honestidade epistêmica de H-042 (Williams) e H-044
(Fu/Liu/Wang): distingue com precisão o que é teorema provado (Teoremas
4-6, 9, 11, Proposições 1-5, todos sobre a reformulação em si) do que é
conjectura equivalente mas mais fraca (Conjectura 10: "G_K bipartido" —
o próprio paper explica por que bipartição sozinha NÃO provaria a
conjectura, já que grafos bipartidos admitem ciclos pares) e do que é
analogia/heurística (Seção 7, "leitura sísmica" — explicitamente
rotulada "this is an analogy, not a mechanism; nothing physical
underlies it, and by itself it proves nothing"). O próprio Teorema 9
("G_K^{1,2} não tem órbitas divergentes nem ciclos não-triviais") é
sobre um grafo deliberadamente **podado** (removendo a aresta E₃) —
verdade quase por construção, e o paper não disfarça isso como
progresso sobre a conjectura real.

## Novas hipóteses?

Nenhuma diretamente aplicável à nossa linha principal (o pruning de
múltiplos de 3 e a distribuição geométrica de v₂ já são nossos
H-001/H-011/H-024 etc.). A técnica de "codificar classe residual via
sinal" é uma reformulação notacional elegante, mas não introduz
mecanismo matemático novo para o obstáculo estrutural que já
identificamos.

## Atualizações

- 2026-07-14: paper lido por completo (14 páginas), teoremas centrais
  verificados computacionalmente
  (`experiments/E-047-gilbert-collatz-equivalent-map-check/`), nenhum
  erro encontrado. Flags atualizadas em `literature/papers/INDEX.md`
  (item 003: Lido=Sim, Corrigido=Sim [nada a corrigir], Implementado=Sim).
