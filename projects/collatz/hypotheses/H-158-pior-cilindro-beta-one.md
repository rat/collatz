# H-158: massa do pior cilindro na lei de Syracuse

Status: em andamento

Criada: 2026-08-08

## Alvo

Para a lei de Syracuse `mu_ell` módulo `3^ell`, defina

```text
c_ell=min_(3 does not divide a) mu_ell(a).
```

Decidir se

```text
3^ell c_ell = exp(-o(ell)),
```

equivalentemente `beta_eff(ell)->1`. Esta é a forma de pior cilindro
da estimativa ponderada `beta=1`.

## Estado conhecido

H-131 prova que a Weak Covering Conjecture, por si só, não fornece essa
estimativa. H-148 prova que até uma distribuição ideal das representações
na fatia de custo da WCC deixa massa exponencialmente insuficiente.
E-111 calculou `c_ell` até `ell=12`, com `beta_eff` decrescendo até
`1.222938`; isso é evidência finita e não decide o limite.

## Próximos testes

1. Estender o cálculo do pior cilindro sem executar o DP de custo mínimo.
2. Registrar o resíduo minimizante em coordenadas aditiva e logarítmica.
3. Separar a contribuição por faixas do custo microcanônico.
4. Procurar uma desigualdade recursiva subexponencial para o mínimo.

## Atualização E-127

O cálculo direto foi estendido até `ell=15`, sem executar o DP de custo.
Os últimos valores foram

```text
ell   beta_eff    3^ell c_ell
 12   1.222938    0.0529150
 13   1.209617    0.0500995
 14   1.198911    0.0469172
 15   1.189390    0.0441133
```

Um ajuste descritivo nos níveis `6<=ell<=15` dá
`3^ell c_ell` proporcional a `ell^(-0.773)`. Esse ajuste é compatível
com perda subexponencial, mas o intervalo é curto e não constitui uma
conclusão assintótica. O resíduo minimizante muda de ramo várias vezes;
em seis das quatorze transições testadas, ele é um levantamento do
minimizante anterior.
