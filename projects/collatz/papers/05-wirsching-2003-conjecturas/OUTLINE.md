# Outline — paper 05 (Wirsching 2003)

Status: `main.tex` é um rascunho completo (9 páginas, compila limpo).
Split de `01-syracuse-qx1-endogenia/main.tex` §9.2+§9.3, em 2026-08-10,
a pedido do diretor científico.

Repositório de reprodutibilidade: `github.com/faculdade/collatz-wirsching-2003`.

## Escopo

Hipóteses-fonte: H-125 (função de Fabius base-3), H-133 (Conjectura 1
provada), H-134 (Conjectura 2, defeito relativo de mistura, refutada
por H-160 mas pelo motivo errado, corrigido por H-167/H-168), H-142
a H-147 (decomposição microcanônica, pontes de equivalência de
ensembles), H-153 (não equivalência em precisão linear), H-160
(refutação da rota de H-134), H-167 (zeros de custo central,
fechada-inconclusiva), H-168 (aberta, ínfimo do quociente mínimo em
conjuntos fixos), E-135 (medição nova desta sessão).

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
   3 resultados empíricos de nível finito.
5. Teste numérico certificado da Conjectura 3 (§5) — `thm:conjecture3`,
   erro certificado ≤1e-8 até ℓ=500.
6. Discussão — por que a Conjectura 2 continua aberta, e o alvo exato
   que falta (um argumento sobre `W_3` em si, não sobre os geradores).

## O que NÃO entrou nesta versão (pendência)

O achado de O3 desta sessão sobre zeros de custo central (H-167,
fechada-inconclusiva, e H-168, aberta) está mirado no repositório
(`sec4-central-zeros-conjecture2/`) mas ainda não foi incorporado ao
`main.tex` como seção própria — é um resultado real (leitura da fonte
primária corrigindo o enquadramento de H-134/H-160) que merece uma
seção quando houver tempo de escrever com o cuidado da Regra 4b.
Registrar como pendência explícita, não esquecer.

## Rótulo dos resultados (Regra 10b)

Teorema (prova completa): `thm:wirsching-conj1` (Conjectura 1),
`thm:microcanonical`, `thm:fixed-precision-ensemble`,
`thm:sublinear-precision-ensemble`, `thm:linear-block-nonequivalence`,
`thm:ensemble-divergence`. Resultado empírico (certificado, não prova):
`thm:conjecture3`, `thm:fixed-precision-finite`,
`thm:microcanonical-finite`, `thm:microcanonical-fourier`.

## Pendências

- Abstract marcado como rascunho, precisa de reescrita à mão.
- Seção sobre H-167/H-168 (zeros de custo central) ainda não escrita
  no `main.tex`, ver acima.
- `main-pt-br.tex`: não criado, só sob pedido explícito.
- `CRITIQUE.md`: não existe ainda.
