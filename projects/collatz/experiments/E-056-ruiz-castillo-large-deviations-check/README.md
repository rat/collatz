# E-056 — Verificação do paper #026 (Ruiz Castillo, "Grandes Desviaciones Residuales")

Hipótese relacionada: `H-056`.

## Paper

Ruiz Castillo, J.C. (2026). *Grandes Desviaciones Residuales de Ruiz
Castillo en la dinámica acelerada de la Conjetura de Collatz*. Zenodo,
DOI [10.5281/zenodo.20767811](https://zenodo.org/records/20767811), 44
páginas. Sétimo paper deste autor revisado nesta coleção (após item
001/H-039, 008/H-050, 010/H-052, 013/H-053, 017/H-054, 020/H-055).

PDF local: `literature/papers/026_Grandes-Desviaciones-Residuales-Ruiz-Castillo.pdf`
(md5:f12d30c3d0e052854f6da782f0af7bab, confere com o md5 listado na
página do Zenodo). O link original da coleção (item 026 do
`literature/papers/INDEX.md`) aponta para o ResearchGate, que bloqueia
download automatizado — o mesmo paper está espelhado no Zenodo (aberto,
sem bloqueio) sob o DOI acima; usamos essa via.

## O que foi testado

**Parte 1 — identidades algébricas (Seções 1-2), contra órbitas REAIS
de Collatz** (não o modelo i.i.d. abstrato): Proposición 1.2
(interpretação multiplicativa da deuda residual), Proposición 2.3
(equivalência residual-disipativa), Corolario 2.4 (evento crítico
x=0), Proposición 2.5 (monotonia de eventos, o análogo "para k finito"
da Proposición 3.4 que entra no achado central). 24 valores de n (9
fixos + 15 aleatórios ímpares até 10⁶) × 6 valores de k × (até 8
valores de x ou 5 pares) = 2160 casos totais.

**Parte 2 — modelo probabilístico ideal** (a_j iid Geométrica(1/2),
mesmo modelo de H-001/H-011): Proposición 4.4 (E[a]=2), Teorema 4.7
(drift residual negativo, log₂3−2), Teorema 5.2 (cota de Chernoff
P(L_k≥0)≤e^{-ck}) — todos verificados calculando o MGF/Ψ(t) em forma
fechada e comparando com a demonstração do próprio paper.

**Achado central — inconsistência interna real** (não erro de cálculo
isolado): a Definición 3.1 define I_RC(x) via o evento de cauda
**unilateral** {L_k/k≥x}. A Proposición 3.4 (pág. 19, **já provada**)
mostra corretamente que essa I_RC é monótona não-decrescente — mas essa
conclusão é *condicional* à existência do limite que define I_RC em
cada ponto. A Figura 1 (pág. 33, Seção 6, "conceptual") e a Conjetura
7.3 (pág. 36, propriedade 2: "existe un único punto x* tal que
I_RC(x*)=0") descrevem I_RC como uma função **bilateral** em V/U,
positiva nos dois lados de x*=log₂3−2. A Conjetura 7.5 (pág. 38,
conferida diretamente contra o PDF) formaliza essa mesma leitura
bilateral: I_RC(x)=sup_{t∈ℝ}{tx−Λ(t)}, sup **irrestrito** — ou seja,
Figura 1, Conjetura 7.3 e Conjetura 7.5 são as três mutuamente
consistentes entre si, e é esse trio que contradiz a Proposición 3.4:
uma função monótona não-decrescente com um zero em x* é
obrigatoriamente zero em TODO x≤x*, não só num ponto único.

Confirmamos de três formas independentes que I_RC(x)=0 (não positivo)
para x<x*, e que portanto **o limite que define I_RC de fato existe
nesse regime** (a condição de que depende a Proposición 3.4 — sem essa
checagem, o achado seria "uma conjectura falsa" em vez de "uma
conjectura provadamente incompatível com uma proposição já demonstrada
no mesmo paper"):

1. **Analiticamente**: `I_RC_restricted(x)` = sup_{t≥0}{tx−Λ(t)} — a
   restrição de sinal padrão da teoria de grandes desvios para eventos
   unilaterais (Dembo-Zeitouni, cap. 2), a mesma restrição usada
   implicitamente (só para x=0) na demonstração já provada do Teorema
   5.2. Dá exatamente 0 para x<x*, coincidindo com `J_unrestricted(x)`
   (a Legendre-Fenchel bilateral, sem restrição — Conjetura 7.5 como
   realmente escrita) apenas para x≥x*.
2. **Monte Carlo**: para x=−0.6 (<x*≈−0.415), simulando somas de k
   Geométricas(1/2) iid, P(L_k/k≥x) **sobe** de 0.667 (k=10) para
   0.99996 (k=1000) — o evento fica cada vez MENOS raro, não mais.
3. **Exato para k pequeno**: distribuição Binomial Negativa fechada via
   `Fraction` (sem ponto flutuante perto do limiar), mesmo padrão
   crescente (k=5→40: 0.623→0.804).

## Como reproduzir

```
python3 experiment.py
```

Sem dependências além de `numpy` (usado só na simulação Monte Carlo
vetorizada). Roda em poucos segundos.

## Nota de integridade (ver H-056 para detalhes)

1. **Verificado diretamente contra o PDF original**: um rascunho
   anterior desta mesma análise caracterizava a Conjetura 7.5 como já
   tendo a restrição de sinal correta (t≥0) — tratando-a como "a
   correção que o próprio paper oferece" para a Conjetura 7.3. Isso
   estava **errado**: conferimos a pág. 38 diretamente e a Conjetura
   7.5, como escrita, é irrestrita (sup_{t∈ℝ}). Corrigido no
   `experiment.py` antes de finalizar. O achado central não muda — só
   a atribuição de qual conjectura tem qual fórmula.
2. **Reportado, não re-verificado em detalhe**: também nesta sessão foi
   relatado (por uma etapa anterior do mesmo trabalho) um bug de
   inversão na ordem de unpacking de tupla no código de verificação,
   identificado e corrigido antes de qualquer número ser reportado. Não
   temos histórico de git do arquivo (ainda não commitado) nem a forma
   exata do bug para reconstruir com certeza — relatamos o fato de que
   foi pego e corrigido em sessão, sem inventar o diff específico.

## Resultado

Suporta H-056: Seções 1-5 do paper (identidades concretas, drift
negativo, cota de Chernoff) inteiramente corretas. O erro real está
contido na Seção 7 (inteiramente conjectural, nunca rotulada
"Teorema"/"Proposición"), que entra em contradição com a Proposición
3.4 (Seção 3, já demonstrada). Não é uma alegação de prova de Collatz
— o paper nega isso explicitamente ("El marco desarrollado no
demuestra la Conjetura de Collatz", pág. 41) — nem um erro de cálculo
isolado. É uma conjectura de estrutura global (função de tasa
bilateral em V) inconsistente com uma proposição local já provada no
mesmo texto, por confundir a função de tasa de Cramér clássica
(bilateral) com a função de tasa real do evento de cauda unilateral
que a Definición 3.1 realmente define.
