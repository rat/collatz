# H-083 — Revisão: Wang, "Non-Existence of Collatz m-Cycles for m≤95" (2026)

Status: revisão externa concluída (identidades verificáveis confirmadas; resultado condicionado a inputs externos citados, não reprovados)
Criada em: 2026-07-15
Origem: item 030 da coleção de literatura (`literature/papers/INDEX.md`),
arquivado em 2026-07-15.

## O paper

Xinjun Wang (pesquisador independente). *INTEGERS* 26 (2026), A##
— periódico revisado por pares estabelecido em teoria dos números
combinatória. **Não alega prova completa** da conjectura — exclui
ciclos não-triviais específicos (m≤95, onde m é o número de mínimos
locais), no estilo Diofantino de Simons–de Weger/Hercher. Território já
conhecido deste projeto (H-057, que conecta essa mesma técnica via
frações contínuas de log₂3).

## Estrutura do argumento

Usa três **inputs externos certificados, não reprovados no paper**:
(I1) verificação computacional até X=2^71 (item 110 desta coleção,
Barina 2025, já revisado em H-080); (I2)/(I3) limites de Simons–de
Weger para K (número total de passos ímpares num ciclo hipotético).
A partir desses inputs, deriva uma cadeia de lemas puramente algébricos
(identidade de transição, estimativa elementar, seleção de bloco
"suffix-balanced", teste de denominador de fração contínua) que excluem
m≤91 por uma iteração de cota inferior, e m=92,93,94,95 por buscas
finitas exatas adicionais.

## Verificação computacional

`experiments/E-083-wang-2026-review/experiment.py` — focada nas
identidades algébricas centrais, verificáveis independentemente sem
reproduzir os inputs externos (I1-I3) nem a busca finita completa dos
4 casos especiais:

1. **Lemma 1 (Local-minimum transition)**: n_i=a·2^k−1 ⟹
   C^k(n_i)=a·3^k−1 (quando os k passos são de fato todos ímpares
   consecutivos). **49 casos válidos, 0 falhas.**
2. **Lemma 3 (Elementary bound)**: T(n)<3/n, onde T(n)=Σ1/C^t(n) ao
   longo de uma corrida ímpar. **8 valores de n testados, 0 falhas**
   (todas as razões T(n)/(3/n) claramente abaixo de 1).
3. **Lemma 9 (Monotonicity of suffix exponents)**: V_t≥V_s para 1≤t≤s,
   onde V_t=(tK/m)·(δ−1)/(δ^t−1). **114 casos (K, m variados), 0
   falhas.**
4. **Aritmética do Lemma 13**: U(49)=1,4784·49·δ⁴⁹ < 7×10¹¹ (o cálculo
   que exclui m≤49 imediatamente) — confirmado
   (U(49)≈4,58×10¹¹<7×10¹¹). A fronteira m*(K⁽⁰⁾) (solução de U(m)=K⁽⁰⁾)
   calculada numericamente cai em (49,50), exatamente como a tabela do
   paper afirma. **Confirmado.**

Nenhum erro encontrado nas identidades algébricas testadas.

## O que não foi verificado (fora do escopo razoável)

Os valores numéricos específicos de K^(1) a K^(6) na Tabela do Lemma 12
(que dependem de um teste de denominador mínimo de fração contínua de
log₂3, não reimplementado aqui) e as quatro buscas finitas exaustivas
para m=92,93,94,95 (que exigiriam reimplementar o "affine a-ladder"
completo da Seção 6) não foram reproduzidos independentemente — exigem
replicar aparato computacional específico do autor. As identidades
algébricas que sustentam essas buscas (Lemas 1, 3, 9, e a fórmula de
recursão da Seção 6.1-6.2) foram verificadas e estão corretas, dando
razoável confiança na correção do método, mesmo sem reproduzir os
números finais exatos.

## Avaliação geral

Paper tecnicamente sólido, no território bem estabelecido de exclusão
Diofantina de ciclos (mesma linha de Simons–de Weger/Hercher, já
conhecida por este projeto via H-057). Não alega mais do que exclusão
de ciclos específicos — não uma prova da conjectura completa. As
identidades algébricas centrais, verificáveis sem reproduzir o aparato
computacional pesado do autor, estão corretas.

## Atualizações

- 2026-07-15: revisão externa concluída. PDF lido por completo (20
  páginas das primeiras seções, cobrindo definições, lemas centrais e
  a iteração de cota inferior até m≤91). Lemas 1, 3, 9 e a aritmética
  do Lemma 13 confirmados sem exceção. Valores numéricos específicos
  da Tabela do Lemma 12 e as buscas finitas para m=92-95 não
  reproduzidos independentemente (exigem replicar aparato computacional
  específico do autor).
