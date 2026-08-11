# Outline — paper 05 (Wirsching 2003)

Status: `main.tex` passou por redação final (Regra 5), 11 páginas,
compila limpo. Split de `01-syracuse-qx1-endogenia/main.tex` §9.2+§9.3,
em 2026-08-10, a pedido do diretor científico.

Repositório de reprodutibilidade: `github.com/faculdade/collatz-wirsching-2003`.

## Escopo

Hipóteses-fonte: H-125 (função de Fabius base-3), H-133 (Conjectura 1
provada), H-134 (Conjectura 2, defeito relativo de mistura, refutada
por H-160 mas pelo motivo errado, corrigido por H-167/H-168), H-142
a H-147 (decomposição microcanônica, pontes de equivalência de
ensembles), H-153 (não equivalência em precisão linear), H-160
(refutação da rota de H-134), H-167 (zeros de custo central,
fechada-inconclusiva), H-168 (fechada-inconclusiva em 2026-08-10,
ínfimo do quociente mínimo em `a` fixo; ver seção própria no arquivo da
hipótese para quantis, composição do bucket inferior, extensão a
`ell=17` e o escalonamento que descarta a rota de H-166), H-171
(fechada-confirmada, sensibilidade ao deslocamento explicada pela
fronteira de suporte), E-135 (medições desta sessão e da anterior).

## Estrutura

1. Introdução — a cadeia de Wirsching (2003), o que já foi resolvido
   (Conjectura 1, H-133) e o que continua aberto (Conjectura 2).
2. A cadeia, direto da fonte primária (§2) — as cinco condições
   (?1)-(?5), com as três descobertas que só ficam visíveis lendo o
   PDF original (achado do O3 desta sessão, corrigindo uma paráfrase
   de segunda mão que a linha usava até então): (?4) é só sobre `W_3`,
   sem informação da coordenada 3-ádica; (?3) e (?2) são a mesma
   desigualdade, só quantificador muda; Teorema 1 só usa `a` inteiro,
   mais fraco que (?2)/(?3) sobre `Z_3^x`.
3. Conjectura 1 (§3) — prova por cancelamento de função geradora
   (H-133).
4. Decomposição microcanônica e equivalência de ensembles (§4) —
   `thm:microcanonical`, `prop:complex-deconditioning`,
   `thm:fixed-precision-ensemble`, `thm:sublinear-precision-ensemble`,
   `thm:linear-block-nonequivalence`, `thm:ensemble-divergence`, mais
   um novo par de resultados sobre a hipótese em aberto de
   `thm:microcanonical` (`thm:quantile-diagnosis`,
   `rem:no-monotone-certificate`, incorporando H-168/H-171, ver abaixo),
   mais os resultados empíricos de nível finito originais.
5. Teste numérico certificado da Conjectura 3 (§5) — `thm:conjecture3`,
   erro certificado ≤1e-8 até ℓ=500.
6. Discussão — por que a Conjectura 2 continua aberta, e o alvo exato
   que falta (um argumento sobre `W_3` em si, não sobre os geradores).

## H-167/H-168/H-171 incorporados (2026-08-10, redação final)

O achado de O3 sobre zeros de custo central (H-167, fechada-inconclusiva)
e a extensão desta sessão (H-168, fechada-inconclusiva; H-171,
fechada-confirmada como subproduto) entraram em §4 como
`thm:quantile-diagnosis` (Empirical Result: separação entre estatística
de extremos e deterioração real via conjunto fixo exaustivo em `d=+5`
e diagnóstico de quantis em `d=6..12`) e `rem:no-monotone-certificate`
(Remark: por que o mecanismo de combinação convexa de um resultado do
paper companion não se transfere para este quociente, com contraexemplo
exato de não-monotonicidade). H-167 em si (zeros de custo central,
`central_zeros.py`) não ganhou seção própria: seu conteúdo
(extrapolação sobre quando o conjunto coerente de zeros pode se
extinguir) é mais especulativo que o que H-168/H-171 assentaram, e não
alimenta diretamente nenhuma hipótese de teorema do paper; mencionado
de passagem no `hypotheses/H-168-...md` mas deixado fora do `main.tex`
por não ter o mesmo grau de assentamento. Uma rodada de crítica
adversarial (subagente Opus, contexto fresco) sobre esse material novo
achou 9 problemas (C-031 a C-039 em `CRITIQUE.md`), 4 de severidade
alta; todos corrigidos ou rejeitados com motivo registrado antes do
commit, incluindo uma correção de mérito matemático (a explicação
original do Remark estava incompleta, e a rederivação corrigiu também
quatro dos seis valores de `S_3(3,a)` que um escalonamento anterior a
Codex tinha citado errado).

## Rótulo dos resultados (Regra 10b)

Teorema (prova completa): `thm:wirsching-conj1` (Conjectura 1),
`thm:microcanonical`, `thm:fixed-precision-ensemble`,
`thm:sublinear-precision-ensemble`, `thm:linear-block-nonequivalence`,
`thm:ensemble-divergence`. Resultado empírico (certificado, não prova):
`thm:conjecture3`, `thm:fixed-precision-finite`,
`thm:microcanonical-finite`, `thm:microcanonical-fourier`,
`thm:quantile-diagnosis`. Observação estrutural exata, não teorema
autocontido: `rem:no-monotone-certificate`.

## Pendências

- `main-pt-br.tex`: não criado, decisão do pesquisador de deixar para
  pedido explícito separado (mesma tensão de política dos papers
  01/04/06; ver C-027 em `CRITIQUE.md`).
