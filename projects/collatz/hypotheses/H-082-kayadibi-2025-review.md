# H-082 — Revisão: Kayadibi, "Exact and Delayed Descent in Accelerated Odd Collatz Spines" (2026)

Status: revisão externa concluída (sem erros encontrados; não alega prova, honesto sobre o escopo)
Criada em: 2026-07-15
Origem: item 025 da coleção de literatura (`literature/papers/INDEX.md`),
arquivado em 2026-07-15.

## O paper

Seyma Yaman Kayadibi (Victoria University). Preprint, 2026 (via
ResearchGate/Zenodo v1). **Não alega prova completa** — o texto afirma
explicitamente: "The results do not prove the Collatz conjecture" e
inclui uma "Remark 4.5 (Local Scope)" dedicada a deixar claro que o
resultado é local a uma família específica de resíduos, não uma
afirmação de convergência global.

Estuda "spines de resistência modular" S_m={n∈ℤ⁺: n≡−1 (mod 2^m)}
(equivalentemente n=2^m·q−1) sob o mapa acelerado T(n)=(3n+1)/2^{v₂(3n+1)},
e o "tempo de primeiro descenso" τ(n)=min{r≥1: T^r(n)<n}. Prova uma
identidade de persistência exata (nenhum descenso pode ocorrer antes do
passo m dentro de um spine), isola um limiar de valuação κ_m que
certifica descenso exato no primeiro passo possível para uma subclasse
residual infinita, e analisa a estrutura do complemento não-certificado
via um "lema de valuação de deslocamento".

## Verificação computacional

`experiments/E-082-kayadibi-2025-review/experiment.py`:

1. **Lemma 3.1 (Spine Persistence Identity)**: T^j(n)=3^j·2^{m−j}·q−1
   para n=2^m·q−1, 0≤j≤m−1. **3016 casos (m=2 a 14, q=1 a 29), 0
   falhas.**
2. **Lemma 3.2 (Spine Exit Formula)**: T^m(n)=(3^m·q−1)/2^s,
   s=v₂(3^m·q−1). **377 casos, 0 falhas.**
3. **Theorem 4.1 (Valuation Threshold)**: v₂(3^m·q−1)≥κ_m ⟹ τ(n)=m
   (calculado exatamente via τ(n), não só inferido). **184 casos
   certificados testados, 0 falhas.**
4. **Lemma 5.4 (Shift Valuation Lemma)**: para q≡q*_m+a (mod 2^{κ_m}),
   1≤a<2^{κ_m}, tem-se v₂(3^m·q−1)=v₂(a). **244 casos, 0 falhas.**
5. **Estatísticas empíricas** (E_bar, mediana, máximo do excesso de
   descenso E(n)=τ(n)−m): reproduzido em escala menor (N até 200.000,
   m=2 a 15, vs. N=10⁷, m=2 a 23 do paper) — valores qualitativamente
   consistentes e na direção esperada (E_bar=5,28 vs. 6,74 do paper,
   crescendo com escala maior; todos E(n)≥0, consistente com o
   Corollary 3.3 já confirmado).

Nenhum erro encontrado em nenhuma das quatro identidades algébricas
centrais, testadas exaustivamente sem exceção.

## Avaliação geral

Paper tecnicamente correto e com honestidade epistêmica exemplar sobre
seu próprio alcance — nunca alega mais do que prova, é explícito sobre
o escopo local (uma família específica de resíduos módulo potências de
2), e distingue claramente entre a subclasse "certificada" (onde
τ(n)=m é provado exatamente) e o complemento "não-certificado" (onde
apenas uma estrutura algébrica de por que o certificado falha é
estabelecida, sem alegar nada sobre convergência). Resultado modesto
mas limpo — nenhuma conexão nova com as linhas de pesquisa deste
projeto identificada além do território já conhecido (H-005/H-007 e
outras análises de classes residuais mod 2^k).

## Atualizações

- 2026-07-15: revisão externa concluída. PDF lido por completo (15
  páginas). Quatro identidades algébricas centrais confirmadas sem
  exceção; estatísticas empíricas reproduzidas em escala menor com
  consistência qualitativa. Nenhum erro encontrado.
