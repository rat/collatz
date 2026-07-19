# E-104 — Teste de otimização ergódica para o congelamento (H-129)

Hipótese relacionada: [`H-129-q-adic-pole-analog-seymour.md`](../../hypotheses/H-129-q-adic-pole-analog-seymour.md)

## O que foi testado

Depois de reframear o congelamento quenched-vs-anelado (já provado em
geral no paper, Proposição~prop:always-frozen) como um fenômeno de
otimização ergódica/formalismo termodinâmico a temperatura zero
(reframing sugerido pelo Fable numa consulta anterior sobre um paper
externo do Seymour), testamos diretamente se a medida de Gibbs quenched
se concentra na trajetória "gulosa" (sempre o menor `a` admissível a
cada passo) conforme a profundidade cresce, na fase congelada vs.
não-congelada.

## Resultado 1 — sem concentração genuína (revisado)

`experiment_greedy_concentration.py` calcula p_greedy(k) = probabilidade
quenched de seguir sempre o ramo guloso nos k primeiros passos, via a
mesma DP exata `Z_k` já validada em E-103. Observação inicial: em q=5
congelada, p_greedy parecia desacelerar para quase-platô — mas um
argumento EXATO (Z_k ≥ peso_guloso, válido para todo k, pois todos os
pesos são positivos) mostra que a taxa própria do caminho guloso é
muito mais negativa que a taxa real de crescimento de Z_k, em ambas as
fases. O platô observado é artefato pré-assintótico (mesmo crossover
k≈407 já conhecido de H-109) — não há concentração genuína.

## Resultado 2 — achado colateral real, mas previsão numérica não confirmada

No caminho, surgiu que A(α)/α = P(α_c)/α_c é constante (fato exato já
estabelecido), e que o expoente B(α_c)=3/2 é literalmente a constante
de Bramson de máximos de branching random walk — conexão real e
citável com a literatura de extremos de BRW, independente do resto.

Isso levou a testar se a*=(log q − P(α_c)/α_c)/log 2 prevê o ⟨a⟩ médio
real dos ciclos conhecidos do mapa. Confirmação inicial parecia forte
para q=5 (ciclos secundários batendo com a* a 1,3%), mas um teste
direto (calcular A(α)/α via DP, sem atalho anelado, para 3 raízes reais
de q=5) **não reproduziu** a* em nenhum caso, e mostrou oscilação
instável em k. Um terceiro ponto de dados (q=7) refutou a hipótese
alternativa testada (razão α₊/α_c prever a qualidade do ajuste).

**Veredito**: a concordância numérica de a* com ciclos catalogados
deve ser tratada como evidência anedótica fraca, não confirmação. A
fórmula usada é, na melhor hipótese, um limite superior não verificado
(a_min≤a*), não uma igualdade testada — a igualdade exigiria uma
fórmula de congelamento tipo REM que nunca foi demonstrada nem testada
para este subshift determinístico específico.

## O que sobrevive como sólido

- A constante de Bramson B(α_c)=3/2 (fato exato, citável por si só).
- O framing de otimização ergódica/formalismo termodinâmico como lente
  teórica mais correta que REM/vidro de spin para este congelamento
  (mas sem a previsão quantitativa de a*, que não se sustentou).

## Arquivos

- `experiment_greedy_concentration.py` — Resultado 1 (concentração da
  medida gulosa).
- `output.txt`, `greedy_concentration_results.json` — dados brutos.

Os scripts do Resultado 2 (teste de A(α)/α via DP direta, sem atalho
anelado) foram executados em scratchpad de sessão, não persistidos
neste repositório (eram exploratórios, refutaram a própria hipótese
que testavam).

## Próximos passos (se a linha for retomada)

~~Análise espectral genuína do operador de transferência (Perron-
Frobenius em Z/q^kZ) ou formalismo de Manneville-Pomeau/Sarig-Iommi
para cadeias de Markov de alfabeto infinito~~ — **executado e fechado
em [E-105](../E-105-transfer-operator-spectral-gap/README.md)
(2026-07-19)**: o operador dual M_α tem gap espectral perfeito e
comprovado (espectro exato {Λ,0}), Manneville-Pomeau/Sarig-Iommi não
se aplica. O transiente k^-0,222 pertence a uma camada não-linear
separada. Resta como via real: teste log-periódico da cauda (ver
E-105/E-103). Nada disso foi integrado ao paper.
