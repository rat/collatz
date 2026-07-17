# H-119 — Getachew & Assefa, "Efficient Computation of Collatz Sequence Stopping Times" (2025): trabalho honesto, sem prova disfarçada, mas com falhas de rigor na análise de complexidade e metodologia estatística

Status: sem erro de correção/lógica; falhas de rigor técnico documentadas
Criada em: 2026-07-17
Origem: item 119 do INDEX.md (IEEE Access 2025). Mesmo primeiro autor do
item 109/H-079 ("Unfolding the Collatz Tree", ALEGAÇÃO DE PROVA
REFUTADA), mas este é um paper diferente, sem alegação de prova.

## Enunciado

Propõe algoritmo que acelera o cálculo do "stopping time" batchando
várias divisões por 2 consecutivas num único passo (via `n & -n` +
`log2`, isolando de uma vez quantas divisões seguidas ocorrerão).
Validação em massa (1 bilhão de números) contra força bruta; extensão
de verificação para 2^100000 a 2^100000+100000.

## Avaliação

**Sem prova disfarçada** (diferente do item 109 do mesmo autor) — a
alegação é puramente de eficiência computacional (~28% menos
"iterações" que referências), apresentada honestamente como faixa
pequena de verificação adicional.

**Nota de terminologia, não erro**: "stopping time" no paper mede
comprimento da sequência (nº de termos, incluindo n), não nº de
operações — verificado consistente em múltiplos n (48,7,63,20480,27,97).
Convenção não-padrão mas usada uniformemente.

**Falhas de rigor encontradas**:

1. **Complexidade "O(1)" falsa no regime que o paper mais enfatiza**:
   afirma cada operação (log2, AND, divisão) em O(1), mas testa
   explicitamente números até 2^100000 (~100.000 bits), que exigem
   aritmética de precisão arbitrária — nesse regime AND/shift/log2 de
   um número de k bits custam ≥O(k), não O(1). Invalida a análise
   assintótica justamente no regime que o paper destaca como
   diferencial.
2. **Curve-fitting com apenas 2 pontos**: as fórmulas logarítmicas de
   crescimento (caso médio e pior caso) são derivadas resolvendo um
   sistema linear com exatamente 2 pontos de dados — sempre tem solução
   exata, não confirma forma logarítmica nenhuma (sem R², sem
   resíduos, sem mais pontos). A linguagem ("Equation 6 confirms...")
   superestima o que foi demonstrado.
3. **Novidade superestimada**: o algoritmo é, essencialmente, a técnica
   padrão de contagem de zeros à direita (CTZ) para acelerar divisões
   consecutivas por 2 — otimização comum em implementações sérias de
   verificação Collatz. A moldura de "structural patterns"/"branch
   traversal" descreve a mesma operação de forma confusa (ex: "compute
   previous number = 3×current+1" é o passo DIRETO do mapa, não
   travessia reversa, apesar da terminologia sugerir isso).
4. **Ganho de ~28% é previsível estatisticamente**: com E[v₂]≈2 (fato
   conhecido da literatura), o batching deveria reduzir iterações de
   ~3·N_odd (baseline ingênuo) para ~2·N_odd (proposto), razão ~33% —
   mesma ordem do 28% relatado. O ganho é majoritariamente consequência
   esperada de estatística já conhecida, comparado contra baseline
   fraco, não contribuição algorítmica nova.

## Relevância para a investigação atual

Tangencial — a estatística implícita de "run length médio ≈2" é
consistente com o que sustenta nossa medida G(v)/Syracuse, mas nenhuma
fórmula/técnica nova aproveitável. Sem relação com a generalização qx+1.

## Veredito

Algoritmo correto (validado contra força bruta), sem petição de
princípio nem prova disfarçada — diferente do H-079 do mesmo autor. Mas
com falhas reais de rigor técnico (complexidade, metodologia
estatística, moldura de novidade) que comprometem as alegações de
contribuição do paper.
