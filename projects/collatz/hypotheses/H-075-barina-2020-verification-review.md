# H-075 — Revisão: Barina, "Convergence verification of the Collatz problem" (2020/2021)

Status: revisão externa concluída (sem erros encontrados)
Criada em: 2026-07-15
Origem: item 105 da coleção de literatura (`literature/papers/INDEX.md`),
arquivado via busca EBSCO/ScienceDirect em 2026-07-15. Já citado sem PDF
em `literature/00-index.md` e `literature/overview-and-known-results.md`
como uma das duas verificações computacionais mais fortes conhecidas
(o resultado de 2020, aqui; e o de 2025 até 2^71, item 110).

## O paper

David Barina (Brno University of Technology). *Journal of Supercomputing*
77, 2681-2688 (2021, publicado online 2020), Springer — periódico
revisado por pares estabelecido em ciência da computação/engenharia.
**Não alega nada sobre resolver a conjectura** — apresenta uma técnica
algorítmica para acelerar a *verificação computacional* de convergência,
usada num projeto de computação distribuída que verificou todos os
inteiros até 2^68 (2019-2020).

## A contribuição central

Observa que a etapa aditiva "+1" da função de Collatz pode ser evitada
computacionalmente alternando entre rastrear a órbita em n e em n+1
(Eqs. 3-5), usando só operações multiplicativas (potências de 3 e 2)
mais a operação `ctz` (count trailing zeros). Isso substitui tabelas de
lookup pré-computadas de tamanho O(2^N) (usadas por projetos
concorrentes) por uma tabela pequena de tamanho O(N) — resultado prático
de engenharia, não uma alegação matemática nova sobre a conjectura em
si.

## Verificação computacional

`experiments/E-075-barina-2020-verification-review/experiment.py`:

1. **Identidades Eq.4/Eq.5** (as funções auxiliares T(n) e T1(n) que
   trocam de domínio n↔n+1): confirmadas idênticas à forma acelerada
   padrão T(n)=(3n+1)/2 (ímpar) ou n/2 (par), **200.000 casos, 0
   falhas**.
2. **Algorithm 1** (teste de convergência via ctz/potências de 3):
   reimplementado literalmente do pseudocódigo do paper e confirmado
   convergindo corretamente (parando com resultado <n0) para todo
   n0=2..2000, **999 casos, 0 falhas**.
3. **Algorithm 2** (delay = soma de todos os α's e β's): confirmado
   batendo exatamente com a contagem padrão de passos até atingir 1,
   em 5 sementes representativas (incluindo n=27, órbita clássica
   longa), **5 casos, 0 falhas**.
4. **Eq.6** (forma geral de T^k(n), base dos "sieves" de janela k):
   confirmada em 1000 casos aleatórios (k=1 a 9), **0 falhas**.
5. **Afirmação textual** ("for odd n, the average number of iterates
   computed in a single step... is 4"): confirmado empiricamente, média
   de 4,009 sobre 200 sementes ímpares aleatórias (vs. 4,0 previsto).

Nenhum erro encontrado em nenhuma das construções algorítmicas
verificáveis.

## Nota sobre o resultado empírico citado (Lagarias-Weiss)

O paper reporta (Seção 5) que o maior "path record" abaixo de 2^68
ocorre em n=274133054632352106267 (não publicado antes), e que os
dados até 2^68 confirmam a predição de Lagarias-Weiss (1992, teoria de
grandes desvios) de que limsup log(t(n))/log(n) = 2 para path records.
Esse resultado empírico específico (o valor exato do path record) não é
verificável de forma independente sem reexecutar a verificação
computacional completa até 2^68 — fora do escopo razoável desta
revisão (exigiria recursos computacionais da ordem dos usados pelo
próprio projeto distribuído). Reportado como citação, não verificado
diretamente.

## Avaliação geral

Paper de engenharia/otimização computacional sólido e correto em toda
construção algorítmica verificável. Referência importante para o
projeto — junto com o item 110 (mesmo autor, verificação até 2^71,
2025), representa o estado da arte em verificação computacional da
conjectura, já citado no levantamento inicial da literatura deste
projeto (`literature/00-index.md`) desde 2026-07-13, agora com PDF
arquivado e as construções centrais verificadas independentemente.

## Atualizações

- 2026-07-15: revisão externa concluída. PDF lido por completo (8
  páginas). Todas as identidades e algoritmos centrais (Eqs. 4-6,
  Algorithms 1-2) confirmados sem exceção. Resultado empírico específico
  (path record em 2^68) citado mas não reverificado (exigiria escala
  computacional do próprio projeto original).
