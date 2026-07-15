# H-057 — Frações contínuas de log₂(3): conectando nosso muro combinatório (H-009/H-034) com o bound atual da literatura (Hercher 2023) e com a "deuda residual" onipresente nos papers de Ruiz Castillo

Status: confirmada (nenhum ciclo novo; síntese/conexão nova para o
projeto, não matemática nova) — inclui uma correção de interpretação
feita pelo advisor() antes de fechar
Criada em: 2026-07-14
Origem: candidato #1 da lista "candidatos ainda não implementados" do
`BACKLOG.md` (seção 6): "Ângulo de estratégia adversarial de máxima
subida, conectando com a literatura de limites inferiores em ciclos
(Simons & de Weger, Eliahou) — potencial nova via para H-009 (ciclos
não-triviais)". Testada a pedido do diretor científico ("faça o teste
das hipóteses promissoras de nosso backlog").

## Enunciado

Um ciclo não-trivial hipotético de comprimento `a` (número de termos
ímpares) e dissipação total `S` (soma das valuações 2-ádicas ao longo
do ciclo) só pode ter `n₀` positivo se `2^S > 3^a`, ou seja, se
`S > a·log₂(3)`. Definindo o excesso da PAR abstrata `(a,S)` —

```
L(a,S) = S − a·log₂(3)          [queremos L(a,S) > 0, o menor possível]
```

— esta é exatamente a mesma quantidade `L_k(n) = k·log₂(3) − A_k(n)`
("deuda residual") usada em todos os ~7 papers de Ruiz Castillo
revisados nesta coleção (H-052 a H-056), só que aqui aplicada a um par
abstrato `(a,S)`, não à trajetória real de um `n` específico.

A teoria clássica de frações contínuas diz exatamente quais valores de
`a` dão o menor excesso possível para aquele tamanho: os denominadores
dos convergentes (e semiconvergentes, necessários porque este é um
problema de aproximação **unilateral** — precisamos de `S/a > log₂(3)`,
não só `|S/a − log₂(3)|` pequeno) da fração contínua de `log₂(3)`. Essa
é a técnica real usada por Steiner (1977), Simons (2005), Simons & de
Weger (2005) e Hercher (2023) para excluir ciclos — a hipótese testada
aqui era se essa conexão, aplicada ao nosso próprio "muro combinatório"
(H-009/H-034), revelaria algo útil para o projeto.

## Verificação da literatura (antes de escrever qualquer código)

Via `WebSearch` + `WebFetch` (arXiv:2201.00406, Wikipedia — não de
memória): nossas notas próprias citavam "Simons & de Weger (2005), sem
ciclo até 68 subidas" — **correto historicamente**, mas **desatualizado
como bound atual**: Hercher (2023, arXiv:2201.00406) estendeu a exclusão
para `a≤91` (qualquer ciclo não-trivial precisaria de `a≥92`). Técnica
confirmada em ambas as fontes: frações contínuas de `log₂(3)` conectadas
a cotas de Baker sobre formas lineares em logaritmos. **Esta atualização
(68→91) deve ser propagada a `STATE.md`/`BACKLOG.md` onde citado.**

## Como testado

`experiments/E-057-continued-fraction-cycle-exclusion/experiment.py`,
reaproveitando (sem reimplementar) `compositions`/`candidate_n0`/
`check_self_consistency` já validados em E-034:

1. Fração contínua de `log₂(3)` (45 termos) + convergentes plenos +
   semiconvergentes (as "melhores aproximações de um lado só") →
   107 candidatos `(a,S)`, 12 com `a≤2000` (95 descartados por já terem
   `a` com 20+ dígitos, onde `C(S-1,a-1)` deixa de ser computável ou
   informativo).
2. Checagem REAL de autoconsistência (não hipotética) nos candidatos
   dentro do nosso alcance (`a=3,5,17`), no `S` exato do convergente.
3. Cálculo fechado de `n0_min` (composição que minimiza `n0` entre
   todas as composições de `S` em `a` partes — confirmada por
   enumeração exaustiva) para todos os 12 candidatos.
4. Quantificação do custo combinatório `C(S-1,a-1)` além do nosso
   alcance, até e além de `a=91`.

## Resultado

Nenhum ciclo novo (esperado, consistente com H-009/H-034 e com toda a
literatura). Para `a=3,5,17` (nosso alcance), resultado mais forte que
"nenhum autoconsistente": **nenhuma composição sequer produz um `n₀`
inteiro positivo** (a condição de divisibilidade `num % denom == 0` já
falha para todas as 6 / 35 / 5.311.735 composições testadas,
respectivamente) — a autoconsistência nem chega a ser testada porque não
há candidato para testar. Isto é um **subconjunto** da janela
`S_min..S_min+20` que H-034 já cobria (o `S` do convergente cai dentro
dela), não uma verificação adicionalmente mais precisa.

Para `a=29,41`: já excluídos por Simons & de Weger (2005, `a≤68`) — fora
do nosso alcance computacional (`C(S-1,a-1)` de ~1,1×10¹² e ~2,5×10¹⁷
composições), mas cobertos pela literatura via Baker, não por enumeração.

Para `a=94,147,200,253,306,971,1636` (e além): território aberto — além
do bound atual de Hercher (2023, `a≤91`). São os candidatos de menor
excesso `L(a,S)` entre os semiconvergentes até `a≤2000`.

## Correção de interpretação (achado do advisor(), antes de finalizar)

A primeira versão deste experimento afirmava, no docstring e na "Parte
4", que **menor excesso `L(a,S)` implica menor `n₀` possível** — e por
isso rotulava `a=29,41` como os candidatos mais "perigosos" a atacar
primeiro. **Isso está invertido.** Para a composição que minimiza `n₀`
(forma fechada `(1,1,...,1,S-a+1)`, confirmada por enumeração exaustiva
em `a=3,5,17` como o mínimo global):

```
n0_min = (3^a − 2^a) / (2^S − 3^a)  ≈  1 / (L·ln2)     [L pequeno]
```

ou seja, **menor excesso ⟹ `n0_min` MAIOR**, não menor — exatamente o
oposto do que a primeira versão afirmava. Verificado numericamente
(`experiment.py`, Parte 2b): `n0_min` cresce de 3,8 (`a=3`) até ~1069
(`a=1636`) conforme `L` encolhe de 0,245 para 0,00135.

Mas isso é só o **mínimo sobre composições** — não um limite superior
sobre o `n₀` de um ciclo real, cuja composição (se existisse) é
desconhecida e pode estar longe do mínimo. Verificado concretamente: com
uma composição diferente (valuações grandes no início, não no fim), o
mesmo par `(a=306, S=485)` produz `n₀ ≈ 4,5×10²⁵` em vez de
`n0_min≈978` — uma diferença de ~22 ordens de grandeza para o mesmo
`(a,S)`. A ordem da composição afeta `n₀` muito mais do que o valor de
`L` isoladamente.

**Conclusão correta**: `L(a,S)` pequeno mede **dificuldade analítica de
exclusão** (cotas de Baker precisam de constantes efetivas maiores
quanto mais perto `2^S` está de `3^a` — por isso o bound da literatura
para exatamente em `a=91`, não em algum lugar arbitrário), **não** o
tamanho de um eventual ciclo. São perguntas diferentes. A "Parte 4"
(candidatos entre nosso muro e a literatura, ordenados por excesso)
permanece útil como leitura de "qual `a` seria o próximo alvo natural
para quem for estender o bound analítico" — não como previsão de
tamanho de `n₀`.

## Contribuição para o projeto

Não é matemática nova (reproduz a técnica clássica de
Steiner/Simons/de Weger/Hercher), mas é uma síntese nova e útil para
ESTE projeto:

1. Confirma que nosso próprio muro combinatório (H-034, `a≤16` limpo)
   é explicado precisamente pela mesma ferramenta (frações contínuas)
   que a literatura profissional usa — não uma coincidência.
2. Corrige nossa citação desatualizada "Simons & de Weger, `a≤68`" para
   o bound atual "Hercher 2023, `a≤91`" (arXiv:2201.00406).
3. Conecta explicitamente `L(a,S)` (par abstrato) com `L_k(n)` (deuda
   residual, trajetória real) — a mesma fórmula, aplicada a duas
   perguntas diferentes: "existe algum par que admite excesso zero
   exatamente" (nunca, `log₂(3)` é irracional) vs. "qual o comportamento
   assintótico do excesso ao longo de uma trajetória real" (H-052/H-053).
4. Identifica e corrige, via `advisor()`, uma inversão de raciocínio
   própria antes de ela entrar permanentemente na memória do projeto —
   mesmo tipo de disciplina de verificação aplicada nas revisões dos
   papers externos (H-053, H-056), desta vez ao nosso próprio trabalho.

## Novas hipóteses?

Nenhuma nova. Fecha o item do backlog; não abre uma via computacional
realista para estender H-009/H-034 além de `a≈25` sem implementar as
cotas de Baker/redução de reticulado da literatura profissional (fora
de escopo — projeto separado, não uma tarde de continuação, como já
observado em H-034).

## Atualizações

- 2026-07-14: experimento criado e corrigido em duas rodadas de bugs
  (convergentes plenos sozinhos eram esparsos demais → adicionados
  semiconvergentes; alguns `a` gerados tinham 22+ dígitos → cutoff
  `A_MAX_ANALISE=2000`). Rodado com sucesso, resultado inicial
  interpretado de forma invertida (menor excesso → menor n₀). Corrigido
  após `advisor()` apontar a inversão; verificado empiricamente antes de
  reescrever (n0_min fechado, checagem de composição "ruim" para
  `a=306`). Versão final do `experiment.py` e desta hipótese refletem a
  interpretação corrigida.
