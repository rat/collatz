# H-037 — A Conjectura 10.4 de Pratiher (2026) tem um provável erro de rotulagem off-by-one (números corretos, forma errada)

Status: achado de integridade em literatura externa (números de Pratiher
aparentemente corretos; rótulo de qual "forma" carrega cada número,
aparentemente errado — confirmado com correspondência exata, não
aproximada)
Criada em: 2026-07-13
Origem: H-035 estabeleceu que Freq_r(N) de Pratiher (média de conjunto)
é categoricamente diferente de D(v) (densidade por-nó, obstrução de
H-024); o advisor sugeriu, como próxima direção, tentar verificar se
α≈0,9762 (Conjectura 10.4 de Pratiher) é derivável por métodos de
equidistribuição — já que a obstrução de H-024 não deveria se aplicar a
uma média de conjunto.

## Pergunta original

Freq_a(N) (fração de {1,...,N} cuja órbita atinge, pela primeira vez,
uma potência de 2 ≡8 mod9 — "forma 𝔞" na notação de Pratiher) converge
para α≈0,9762 (Conjectura 10.4). Isso é derivável/verificável por
equidistribuição, dado que H-035 já mostrou que este é um tipo de objeto
diferente de D(v)?

## Alarme teórico (antes de rodar qualquer código)

Pratiher define "forma" de n via M = expoente da primeira/maior potência
de 2 atingida pela trajetória de n (Definição 2.2+9.1), com M mod6
mapeado para uma das 6 formas via sua Tabela (Teorema 4.3): 0↔𝔡, 1↔𝔠,
2↔𝔟, 3↔𝔞, 4↔𝔣, 5↔𝔢.

Mas: a primeira potência de 2 atingida por qualquer trajetória
não-trivial (n que não é ele mesmo já uma potência de 2) **tem que**
ser atingida via um passo ímpar (3x+1=2^M) — nenhum passo de divisão por
2 pode produzir uma potência de 2 a partir de um valor que não é ele
próprio uma potência de 2. E 3x+1=2^M só tem solução inteira (e essa
solução é automaticamente ímpar) quando **M é par** — 2^M≡1 mod3 se e
somente se M é par (2≡-1 mod3). **Isto é exatamente o mesmo mecanismo do
nosso H-012** (todo J_t satisfaz 3J_t+1=4^t=2^(2t), expoente sempre
par). Logo, a forma dominante de qualquer trajetória não-trivial **tem
que** ter M par (formas 𝔡, 𝔟 ou 𝔣) — nunca M ímpar. Mas a forma que
Pratiher relata como dominante (97,6%) é 𝔞, que por sua própria Tabela
4.3 tem M≡3 mod6, **ímpar**. Contradição direta, antes de qualquer
computação.

## Verificação computacional

`experiments/E-037-pratiher-ensemble-check/experiment.py`: simulação
direta da trajetória de Collatz (não acelerada) para todo n≤N, extraindo
M (expoente da primeira potência de 2 atingida) e classificando via a
própria Tabela 4.3 de Pratiher.

**Resultado em N=10^7** (comparar com a Tabela na Observação 10.2 dele):

| Minha forma (M mod6) | Minha freq. | Forma de Pratiher | Freq. dele |
|---|---|---|---|
| 𝔣 (M≡4) | 0,9761136 | 𝔞 | 0,97611 |
| 𝔟 (M≡2) | 0,0238808 | 𝔠 | 0,02388 |
| 𝔡 (M≡0) | 0,0000044 | 𝔢 | 0,0000044 |
| 𝔠 (M≡1) | 0,0000004 | 𝔡 | 0,0000004 |
| 𝔞 (M≡3) | 0,0000004 | 𝔟 | 0,0000004 |
| 𝔢 (M≡5) | 0,0000004 | 𝔣 | 0,0000004 |

**Todas as 6 formas conferem exatamente** sob um deslocamento cíclico
fixo: o valor que Pratiher relata para a forma com M≡k (mod6, pela
tabela dele) é idêntico ao que calculo para M≡(k-1) mod6. Ou seja,
`forma_relatada(M) = forma_verdadeira(M-1 mod 6)` — um erro sistemático
de off-by-one na correspondência expoente↔forma, consistente em todas
as 6 classes, incluindo as 3 caudas raras (4, 4, 4 em N=10^7).

## Verificação exata (não só aproximada) das caudas

As 3 formas "raras" com M ímpar só podem vir de n que **já é** uma
potência de 2 de expoente ímpar (nenhuma trajetória não-trivial entra
num M ímpar — ver alarme teórico acima). Até N=10^7, há exatamente 12
expoentes ímpares possíveis (1,3,...,23, já que 2^23≤10^7<2^24), 4 em
cada resíduo mod6 (1,7,13,19 / 3,9,15,21 / 5,11,17,23). **Minhas
contagens computadas são exatamente 4, 4, 4** — não uma aproximação,
uma igualdade exata com a contagem teórica fechada. Isso é uma
confirmação muito forte de que o mecanismo está corretamente entendido,
não só "parece bater".

## Conexão com nosso próprio H-013 (validação cruzada independente)

M par ⟺ M=2t para algum t (nossa notação de H-013, J_t=(4^t-1)/3,
3J_t+1=4^t). De fato, `M mod6 = 2t mod6`, então forma (M par) é
determinada por `t mod3`: t≡0→𝔡, t≡1→𝔟, t≡2→𝔣. **"Forma" de Pratiher,
uma vez corrigida, é exatamente um agrupamento por t mod3 da nossa
própria distribuição p_t de H-013** (p_t = fração de órbitas cuja última
valor ímpar é J_t = D(J_t), já medida por nós independentemente, meses
antes de eu conhecer o paper de Pratiher).

Conferindo com os dados já registrados em H-013 (300.000 amostras Monte
Carlo): p_2≈93,77%, p_4≈2,37%, p_5≈3,78%, p_7≈0,01%, p_8≈0,06%. Agrupando
por t mod3: t≡2 (2,5,8,...) → 93,77+3,78+0,06≈97,61% ≈ minha forma 𝔣
✓. t≡1 (4,7,...) → 2,37+0,01≈2,38% ≈ minha forma 𝔟 ✓. t≡0 (3,6,9,...) →
~0% (explicado por H-005, já sabíamos) ≈ minha forma 𝔡 ✓. **Os três
números batem com o que calculei agora, de forma totalmente
independente** (H-013 foi medido por Monte Carlo simples, sem qualquer
referência ao FSM de Pratiher). Isso reforça a confiança tanto na nossa
medição antiga (H-013) quanto neste achado novo.

## Sobre a pergunta original (derivação por equidistribuição)

Com o rótulo corrigido, a pergunta vira: dá para derivar
Freq_𝔣(N)→~0,976 por métodos de equidistribuição/operador de
transferência? Achado importante: **α não é uma média "genérica"
imune à obstrução de H-024** — é literalmente uma SOMA infinita dos
mesmos D(J_t) por-nó que H-024 já mostrou não terem fórmula fechada
individual (α = Σ_{t≡2 mod3} D(J_t)). A diferença é que essa soma
específica é **dominada por poucos termos pequenos** (p_2=D(5) sozinho
já é 93,77% do total; a "renda" cai rapidamente com t, por causa do
mesmo mecanismo de orçamento de H-018/Galton-Watson) — não porque é uma
média genérica sobre infinitos nós arbitrários, mas porque a soma
converge rápido o suficiente para ser dominada por um punhado de termos
pequenos e computáveis. Isso é uma razão estrutural genuína para
esperar mais tratabilidade que o D(v) genérico de H-024 — mas não é uma
prova de fórmula fechada, e o mesmo obstáculo de H-024 (D(J_t)
individual não fecha para t grande) continua valendo termo a termo. Não
resolvido; fica como reformulação mais precisa do problema, não como
solução.

## O que NÃO estou afirmando

Não tenho o código-fonte de Pratiher, então não posso apontar a linha
exata do bug — só o padrão observado (deslocamento cíclico de 1,
consistente e exato em todas as 6 classes, inclusive nas caudas raras
com contagem exata prevista). Isso é evidência estatística e
teoricamente fundamentada muito forte de um erro de rotulagem, não uma
inspeção de código confirmada. O **conteúdo numérico central do paper
(dois valores com densidade positiva, ~0,976 e ~0,024, quatro formas
com densidade zero) parece estar correto** — só a atribuição de qual
letra (𝔞 vs 𝔣, 𝔠 vs 𝔟, etc.) carrega qual número parece estar errada.

## Atualizações

- 2026-07-13: achado, verificado exaustivamente (correspondência exata
  em todas as 6 classes, incluindo contagem exata das caudas), e
  conectado à nossa própria medição independente de H-013.
