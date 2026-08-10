# H-162: cancelamento bilinear entre irmãs sem decaimento pontual nem l2

Status: backlog

Criada: 2026-08-09

Origem: passe dirigido a O4 de 2026-08-09, registrado em H-115. É a única
rota que aquela análise deixa de pé, e é registrada aqui por Regra 8e,
não porque haja indício de que funcione.

## Pergunta

A rota de segundo momento precisa que

```text
Cov ~ sum_{xi != 0} S_1(xi) * conj(S_2(xi))
```

seja pequena depois de removidos os modos afins grosseiros exatos
(H-126, Prop. 2), onde `S_1` e `S_2` são as somas de caracteres tipo
Syracuse condicionadas no primeiro passo, uma por irmã.

Toda tentativa registrada até hoje ataca isso por uma cota em cada fator
separadamente: cota pontual uniforme, ou Cauchy-Schwarz sobre o
somatório. H-115 (passe de 2026-08-09) mostra que as duas estão barradas
pelo mesmo lado. A cota pontual uniforme com power-saving implicaria
`K_infinity < infinity`, e é contrariada em nível finito pela medição de
E-133 (`sup * 3^(ell/2)` cresce de 1,13 para 61,7 entre `ell=2` e
`ell=15`). Cauchy-Schwarz gasta exatamente `K_ell - K_(r_ell)`, que
cresce linearmente sob o platô medido `E_r ~ 0,47`.

A pergunta que sobra: existe cancelamento na FASE RELATIVA entre
`S_1(xi)` e `S_2(xi)`, uniforme o bastante sobre `xi`, que torne o
pareamento pequeno sem que nenhum dos dois fatores decaia?

## Por que não é obviamente vazia

As duas irmãs não são independentes nem iguais. Elas diferem apenas pelo
primeiro passo. Pela recursão de Tao (eq. 1.22), condicionar no primeiro
passo `a_1 = j` multiplica o argumento por `2^(-j)` e translada por
`2^(-j)`, isto é, atua em `xi` por dilatação `xi -> 2^j xi` mais uma fase
linear. Logo `S_1(xi)` e `S_2(xi)` são, a menos dessas fases, valores da
MESMA função em frequências relacionadas por potências de 2 módulo
`3^ell`. O pareamento não é um produto de dois objetos arbitrários, é uma
correlação da função consigo mesma ao longo da órbita de duplicação.

Isso é exatamente onde E-133 vê estrutura: o maximizador do coeficiente
primitivo fica na órbita de `1` sob duplicação em quase todo nível. Ou
seja, o mesmo lugar onde a energia se concentra é o lugar onde os dois
fatores estão relacionados. Pode ser que a concentração ajude o
cancelamento em vez de atrapalhar, e pode ser que ela seja justamente a
ressonância que impede o cancelamento. Nenhuma das duas foi testada.

## Primeiro teste barato, antes de qualquer teoria

Calcular, para `ell` pequeno e um par de irmãs explícito, a soma
`sum_xi S_1(xi) conj(S_2(xi))` e compará-la com:

1. o orçamento trivial de Cauchy-Schwarz `sqrt(E_1) * sqrt(E_2)`;
2. o valor que sairia se as fases relativas fossem aleatórias
   (aproximadamente `sqrt(sum_xi |S_1|^2 |S_2|^2)`).

Se o valor medido ficar perto de (1), não há cancelamento e a rota morre
com um número. Se ficar perto de (2) ou abaixo, há cancelamento de fase e
a pergunta seguinte é se a taxa é suficiente e uniforme em `ell`. Custo
esperado: o mesmo da recursão de E-133, poucos minutos até `ell=12`.

E-129 já mede algo vizinho (agregação sobre o intervalo entre irmãs
contra o acoplamento de dígitos novos) e deve ser lido antes, para não
repetir a mesma medida com outro nome.

## Precedentes verificados antes de abrir

Grep em `hypotheses/` por rotas já fechadas sobre o mesmo objeto: H-126
(componente grosseira exata, sobrevive; lema condicional caiu por
`K_infinity`), H-127 (dicotomia espectral; ramo difuso inacessível a
métodos l¹ por uma parede exata de constantes), H-149 (buraco de suporte
não força espectro primitivo), H-153 (não equivalência dos vetores de
custo latentes, que não transfere para resíduos). Nenhuma delas ataca o
pareamento bilinear diretamente. Esta hipótese não repete nenhuma.

## Expectativa honesta

Baixa. Cancelamento bilinear sem decaimento em nenhum fator é raro e,
quando ocorre, costuma vir de uma estrutura algébrica que aqui seria
justamente a rigidez `x2, x3` que H-115 já identificou como território
sem ferramenta. O motivo para registrar mesmo assim é que é a última
formulação não refutada do alvo de O4, e o primeiro teste custa poucos
minutos.
