# E-108 — Soma ponderada por Δ da correlação grosseira (H-126, Prop. 2)

## Hipótese relacionada

H-126 (`Prop. 2`, "endogenia grosseira exata") prova que, para duas
folhas-irmãs com expoentes de ramo admissíveis a1<a2 (gap Δ=a2-a1,
sempre par para q=3), Corr(Z1,Z2) = +1 se Δ≡0 (mod 6), e -1/2 caso
contrário — exato, independente de profundidade. Uma auditoria externa
do paper (2026-07-20) apontou uma tensão aparente entre esse resultado
(correlação grosseira provada, persistente, não-nula) e a calibração
empírica de H-110 (ρ_eff≲0,06, "nenhum acoplamento positivo
detectado"). O Opus, consultado sobre a reconciliação, sugeriu que os
pesos de ramo geométricos (q·2^-a) concentram massa em Δ pequeno,
predominantemente no caso Δ≢0(mod6) (correlação -1/2), prevendo uma
contribuição grosseira líquida NEGATIVA — mas só qualitativamente, e
sugeriu computar a soma fechada para verificar o sinal (e a magnitude)
de verdade.

## O que foi testado

Sob a medida natural de seleção de par "size-biased" pelo produto dos
pesos de ramo (peso do par (a_i,a_j) ∝ 2^-a_i · 2^-a_j — a mesma
ponderação que aparece no segundo momento E[Z_i Z_j] cujos termos
dominam a covariância agregada), qual é a distribuição de Δ=2k
(k=1,2,3,...) e a correlação grosseira média E[Corr]?

Derivação fechada (verificada por soma direta truncada, razão
sucessiva 0,25 confirmada a 10 casas decimais):

- P(Δ=2k) = 3·4^-k (série geométrica normalizada)
- P(Δ≡0 mod 6) = P(k≡0 mod 3) = 1/21 ≈ 0,0476
- P(Δ≢0 mod 6) = 20/21 ≈ 0,9524
- **E[Corr] = (1/21)(+1) + (20/21)(-1/2) = -3/7 ≈ -0,4286**

## Resultado

O sinal previsto pelo Opus está confirmado, agora com valor exato: a
correlação grosseira média, pesada pela distribuição natural de gaps
Δ induzida pelos pesos geométricos de ramo, é **-3/7**, não zero e não
pequena em módulo. Isso é qualitativamente consistente com o excesso
residual negativo observado na calibração de H-110 (Braço 3 − Braço 1
convergindo a zero pelo lado negativo), embora este cálculo **não**
seja uma derivação da magnitude numérica esperada de ρ_eff — só do
sinal e da ordem de grandeza da correlação de par subjacente, antes da
diluição pela variância agregada (ver a Observação
`rem:calibration-consistency` adicionada ao paper nesta mesma auditoria).

## Limitação honesta (não escondida)

A escolha de ponderar pares por 2^-a_i·2^-a_j ("size-biased pelo
segundo momento") é natural — é literalmente o peso que aparece na
soma de Lema 1 de H-126 — mas não é a única medida concebível sobre
pares de ramos. Este cálculo mostra que, **sob essa medida específica**,
o sinal é negativo com magnitude -3/7; não prova que é a única medida
relevante para a calibração empírica de H-110, cujo desenho (Braço 2)
usa uma família de acoplamento funcionalmente diferente (replicação de
família via hash, não correlação de par por Δ). Portanto isto
**fortalece** a plausibilidade da explicação de dilution já registrada
no paper, mas não a torna uma prova formal de que os dois resultados
descrevem exatamente a mesma quantidade.

## Como reproduzir

```
python3 delta_weighted_correlation.py
```

Sem dependências externas além da biblioteca padrão (`fractions`).
Roda em menos de 1 segundo.
