# E-110 — a correlação grosseira (Prop.2/H-126) e o ρ da calibração (H-111) medem eixos ortogonais

## Hipótese relacionada

Item 1 da auditoria externa do paper (2026-07-20, 4ª rodada): por que
o experimento de calibração (H-111, ρ_eff≲0,06, "nenhum acoplamento
positivo detectado") não entra em tensão com a correlação grosseira
exata e persistente de H-126/Prop.2 (Corr=+1 se Δ≡0 mod6, -1/2 caso
contrário)? O paper já tinha uma resposta por "diluição" (a correlação
grosseira contribui fração evanescente da variância agregada,
conforme a árvore cresce). Este experimento mostra uma resolução mais
forte e exata: as duas coisas não competem porque **não medem a mesma
variável**.

## O que foi verificado

No simulador de H-111
(`E-090-syracuse-measure-vs-density/experiment_synthetic_core.py`), o
tipo do filho k é `child_type = (rho_phase+k) % 3` — literalmente o
resíduo do filho mod 3, exatamente o que a Prop.2 mede em precisão
ℓ=1. Essa fórmula usa só `rho_phase` (a fase da raiz) e `k` (índice do
ramo) — **nunca o parâmetro `rho`** (a intensidade de acoplamento que
o Braço 2 varia). Ou seja: a correlação de tipo entre irmãos é uma
função determinística da estrutura cíclica real (já validada contra
inteiros verdadeiros por `assert_cyclic_structure`, existente no
arquivo original), idêntica em todos os braços — i.i.d. (ρ=0),
acoplado (ρ>0), e árvore real.

**Parte 1**: testei 2000 seeds, comparando a sequência de tipos dos
filhos da raiz com ρ∈{0,0.3,0.7,1.0} — **0 divergências**. O tipo não
depende de ρ.

**Parte 2**: computei a correlação de tipo entre irmãos com gap de
índice δ=k₂-k₁ (gap de expoente Δ=2δ, já que aₖ=a₀+2k para q=3), usando
a mesma ponderação g(0)=0,g(1)=g(2)=c da derivação original de Prop.2.
Resultado: **corr=+1,0000 exatamente quando δ≡0 mod3 (Δ≡0 mod6), e
corr=-0,5001/-0,5005 caso contrário** — reproduz Prop.2 até a 4ª casa
decimal (erro de amostragem Monte Carlo).

## Conclusão

O parâmetro ρ do Braço 2 varia se o **conteúdo/magnitude** de
subárvores irmãs (os fluxos aleatórios frescos que determinam o
*tamanho* de G) é compartilhado ou independente — um eixo
completamente diferente do que a Prop.2 descreve (o *resíduo mod 3*
do filho, que é sempre determinístico dado o índice do ramo). A cota
ρ_eff≲0,06 não podia ter detectado nem deixado de detectar a
correlação de Prop.2, porque essa correlação nunca foi uma forma de
acoplamento que ρ=0 remove — ela é uma propriedade estrutural presente
em qualquer modelo (real ou sintético) que respeite a regra de
admissibilidade correta, com ou sem acoplamento de conteúdo. Isso é
uma resolução mais forte do que a diluição (E-108): não é que a
correlação seja pequena o bastante para não aparecer — é que ela nunca
poderia ter aparecido no experimento de calibração, pois pertence a um
eixo que o experimento não varia em nenhum de seus braços.

## Como reproduzir

```
python3 verify_orthogonality.py
```

Sem dependências externas (cópia local de `node_randoms`, idêntica à
de `E-090/experiment_synthetic_core.py`, para rodar isolado). Roda em
poucos segundos.
