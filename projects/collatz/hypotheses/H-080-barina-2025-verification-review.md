# H-080 — Revisão: Barina, "Improved verification limit for the convergence of the Collatz conjecture" (2025)

Status: revisão externa concluída (sem erros encontrados)
Criada em: 2026-07-15
Origem: item 110 da coleção de literatura (`literature/papers/INDEX.md`),
arquivado via busca EBSCO/ScienceDirect em 2026-07-15. Já citado sem PDF
em `literature/00-index.md` e `literature/overview-and-known-results.md`
como a verificação computacional mais recente (2^71).

## O paper

David Barina (Brno University of Technology). *Journal of Supercomputing*
81:810 (2025), Springer. **Continuação direta** do paper de 2020/2021 do
mesmo autor (item 105, já revisado em H-075/E-075) — as equações
centrais T(n)/T1(n)/Eq.6 são **idênticas** e já confirmadas naquela
revisão. Este paper estende o resultado computacional de 2^68 (2020)
para 2^71 (2025), usando computação distribuída em supercomputadores
europeus, e introduz "sieves 3^k" mais sofisticados que a versão
anterior.

## O que é novo aqui (foco desta revisão)

1. **Sieves 3^k** (Seção 3.2, Tabela 1): percentuais de eliminação de
   candidatos por classe residual módulo 3^k — 33,33% (3¹), 44,44%
   (3² e 3³), 45,68-45,95% (3⁴-3⁶).
2. **Timeline de verificação** (Tabela 10): 2^68 (2020) → 2^69 (2021) →
   2^70 (2023) → 1,5×2^70 (2023) → 2^71 (2025).
3. **5 novos path records** (não publicados antes), o maior:
   2358909599867980429759.
4. Comparações de desempenho CPU/GPU/sieve compression (Tabelas 4-9) —
   dados de engenharia específicos da implementação do autor, não
   verificáveis independentemente sem o código-fonte exato.

## Verificação computacional

`experiments/E-080-barina-2025-verification-review/experiment.py`:

1. **Mecanismo do sieve 3¹**: em vez de só reproduzir o percentual
   citado (33,33%), simulamos diretamente o mecanismo real (busca
   exaustiva: um n é "eliminável" se existe n'<n, testado antes, cuja
   órbita acelerada atinge n em exatamente k=1 passo). Confirmado por
   enumeração exaustiva (n=3 a 2000): **100% dos números ≡2 (mod 3) são
   elimináveis, 0% dos outros dois resíduos** — bate exatamente com o
   percentual citado (33,33% = 1/3) e localiza precisamente *qual*
   resíduo é eliminável, não só a fração agregada.
2. **Fato aritmético base do sieve**: confirmado que 3n+2>2n+1 para
   todo n≥0 (a desigualdade que garante que o valor "consumido" pelo
   sieve é sempre maior que sua origem). **100.000 casos, 0 falhas.**
3. **Timeline monotônico**: confirmado que a sequência de limites
   verificados é estritamente crescente, incluindo o caso não-trivial
   de que 1,5×2^70<2^71. **Confirmado.**
4. **Ordem dos 5 novos path records**: confirmado que estão em ordem
   estritamente crescente (consistente com a definição de path record
   — cada um deve superar todos os anteriores). **Confirmado.**

Nenhum erro encontrado nas afirmações verificáveis independentemente.

## O que não foi verificado (fora do escopo razoável)

Os dados de desempenho específicos (Tabelas 3-9: tempos de execução em
hardware específico, comparações CPU/GPU) e o resultado computacional
central (verificação até 2^71 em si) não são verificáveis
independentemente sem acesso ao código-fonte exato e aos mesmos
supercomputadores — exigiria recursos computacionais da mesma ordem do
projeto original. Reportados como citação, não reverificados
diretamente (mesma limitação já documentada em H-075 para o paper de
2020 do mesmo autor).

## Avaliação geral

Paper de engenharia/otimização computacional sólido, continuação direta
de trabalho já revisado e confirmado (H-075). O mecanismo do sieve 3^k
(a peça genuinamente nova desta versão) foi verificado diretamente por
simulação exaustiva, não apenas por reprodução dos números citados.
Nenhum erro encontrado.

## Atualizações

- 2026-07-15: revisão externa concluída. PDF lido por completo (15
  páginas). Mecanismo do sieve 3¹ confirmado por simulação exaustiva
  (não só reprodução de números); fato aritmético base, timeline e
  ordem dos path records confirmados. Dados de desempenho específicos
  de hardware citados, não reverificados (fora do escopo razoável).
