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

1. ~~Estender o cálculo do pior cilindro sem executar o DP de custo
   mínimo.~~ Feito (E-127, até `ell=18`).
2. ~~Registrar o resíduo minimizante em coordenadas aditiva e
   logarítmica.~~ Feito: E-127 já reporta `argmin` (aditiva) e
   `log2_argmin` (logarítmica, base 2) a cada nível.
3. ~~Separar a contribuição por faixas do custo microcanônico.~~ Feito
   (E-130): ver "Atualização E-130" abaixo.
4. Procurar uma desigualdade recursiva subexponencial para o mínimo.
   Em aberto; é a questão de pesquisa real por trás desta hipótese, não
   uma auditoria computacional, e não foi tentada nesta sessão.

## Atualização E-127 (estendida a `ell=18`)

O cálculo direto foi estendido até `ell=18`, sem executar o DP de custo.
Os valores completos de `ell=12` a `18` foram

```text
ell   beta_eff    3^ell c_ell
 12   1.222938    0.0529150
 13   1.209617    0.0500995
 14   1.198911    0.0469172
 15   1.189390    0.0441133
 16   1.179102    0.0429289
 17   1.170057    0.0417504
 18   1.162241    0.0404242
```

Um ajuste descritivo nos níveis `6<=ell<=18` dá `3^ell c_ell`
proporcional a `exp(-1.084099)*ell^(-0.744288)` (substitui o ajuste
anterior, `ell^(-0.773)` sobre `6<=ell<=15`; a mudança de expoente ao
incluir três níveis a mais mostra que esse ajuste é sensível ao
intervalo, não um expoente estável). Isso é compatível com perda
subexponencial, mas o intervalo continua curto e não constitui uma
conclusão assintótica. O resíduo minimizante muda de ramo várias vezes
(coluna `same_parent` de E-127); no total de 17 transições testadas
(`ell=1` a `18`), pouco mais da metade são levantamentos do minimizante
anterior.

## Atualização E-130: decomposição por faixa de custo (passo 3)

A recursão sem memória de Tao, desenrolada em série geométrica, dá uma
coordenada de custo gratuita: `mu_ell(y) = soma_s 2^-(s+1) *
nu(2^-(s+1) y mod 3^ell)`, onde `s` conta duplicações extras antes de
recair na lei do nível anterior. Comparado ao resíduo de massa MÁXIMA
(dominado quase inteiramente pelo termo `s=0`, que sozinho excede 99%
do total a partir de `ell=5`) e ao de massa mediana (precisa de poucos
termos, `s` até ~1-6 para 90%), o resíduo de massa MÍNIMA (`c_ell`)
precisa consistentemente de mais bandas: `s` até 5 para 90%, até 9-11
para 99%, em todos os níveis de 2 a 15 testados. Nenhum dos três limiares
mostra tendência com `ell` no intervalo testado.

Achado descritivo, não assintótico: o déficit do pior resíduo não vem
de um único caminho barato dominante (como no resíduo de massa máxima);
ele recebe contribuições comparáveis de várias bandas de custo. Não
identifica uma desigualdade recursiva (passo 4) nem se conecta à
variável de custo do DP de custo mínimo de E-111 (uma coordenada
diferente, mais cara, que este experimento evita computar). Ver
`projects/collatz/experiments/E-130-worst-cylinder-cost-bands/`.
