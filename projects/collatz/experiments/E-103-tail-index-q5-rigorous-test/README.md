# E-103 — Índice de cauda de W_v para q=5 (Conjectura do índice de cauda, §3.3 do paper)

Hipótese relacionada: [`H-109-generalized-qx1-pressure-equation-exact-closed-form.md`](../../hypotheses/H-109-generalized-qx1-pressure-equation-exact-closed-form.md)
Ver também: [`H-129-q-adic-pole-analog-seymour.md`](../../hypotheses/H-129-q-adic-pole-analog-seymour.md) (frente paralela, framing teórico diferente)

## O que foi feito

Depois de corrigir a §3 do paper (equação de pressão anelada + transição
de congelamento) e rebaixar o índice de cauda do martingale para q≥5 a
uma Conjectura sem apoio empírico sólido (a medição original de
H-109/H-113, Hill com 600 raízes, já tinha sido sinalizada como
estatisticamente não-confirmatória), o diretor científico pediu
sucessivamente testes mais robustos, com autorização explícita de usar
o tempo de computação e o Fable à vontade. A investigação passou por
três rodadas, cada uma mais rigorosa que a anterior:

**Rodada 1** — Hill/Zipf mais cuidadoso (`experiment_tail_index_q5.py`):
amostra 8x maior (5000 vs 600 raízes), 4 headrooms, bootstrap. Resultado
inicial parecia "encorajador" (perto do previsto na fração de 5%).

**Rodada 2** — bateria completa de 4 estimadores (`full_battery.py`):
regressão Gabaix-Ibragimov, Hill com correção de viés (Huisman et al.),
MLE de GPD com varredura de estabilidade de limiar, e
Clauset-Shalizi-Newman + teste de Vuong contra lognormal. Revelou que a
Rodada 1 tinha sido otimista demais — ver "Resultado" abaixo.

**Rodada 3** — teste EXATO via momento populacional (`exact_moment_test.py`):
em vez de estimador estatístico sobre amostra de raízes, usa a DP exata
`Z_k(θ;u)` (já validada nos testes de congelamento) sobre a POPULAÇÃO
COMPLETA de resíduos mod 5^k. Decisivo em princípio (sem ruído de
amostragem), mas limitado por profundidade alcançável (k≤11 por
memória).

**Descartado antes da Rodada 3** — uma ideia de calibração via árvore
i.i.d. de fase aleatória (`stage0_iid_power_check.ABANDONED.py`) foi
abandonada por dois motivos: (1) circular (o índice dela cai
algebricamente na identidade de pressão anelada já provada, no ponto
que já sabemos estar sempre congelado — não pode falhar por
construção); (2) contagem bruta de nós explode combinatorialmente sob
fase i.i.d. (headroom=100: árvore real=42 nós, sintética>200000 nós) —
ver o arquivo para os detalhes.

## Resultado da Rodada 2 (bateria completa) — quadro misto

**Estabilidade entre headrooms**: excelente para o Huisman (bias-corrected
Hill), que fica em ~1,61 em todos os 4 níveis de headroom, IC bootstrap
≈[1,48; 1,77] — cobre o previsto 1,536 com folga.

**Mas**: a varredura de estabilidade de limiar (GPD) não mostra platô
limpo perto do ξ previsto (0,651) — ξ̂(u) decresce de ~0,58 para ~0,45
conforme o limiar sobe, sem estabilizar. E o teste de Vuong favorece a
alternativa **lognormal** sobre a lei de potência, com significância
(p≈0,03), em 3 dos 4 níveis de headroom testados.

Consultado o Fable para interpretar: os 4 estimadores, quando lidos
pela profundidade de cauda que cada um resume, concordam entre si sobre
a FORMA da curva — o índice local aparente sobe suavemente de ~1,3
(janela larga) a ~2,2 (janela estreita), cruzando o valor previsto perto
da janela de 10%. Ou seja, os "acertos" anteriores eram artefato de
janela, não confirmação — uma curva côncava assim "confirmaria" quase
qualquer valor entre 1,3 e 2,2 em alguma profundidade. Veredito do
Fable: rebaixar de "encorajador" para "inconclusivo".

## Resultado da Rodada 3 (momento exato) — inconclusivo, motivo identificado

Checagem de sanidade: M_k(1,0)=1,0 exatamente em todo k (forçado pela
identidade de pressão anelada já provada — confirma a implementação).

Para o índice de cauda: M_k(p) satura (incrementos decrescentes) para
p≤1,6 e diverge (incrementos crescentes) para p≥1,7 — o que colocaria
o índice real ACIMA do previsto 1,536 se tomado ao pé da letra.

Mas, analisando a RAZÃO entre incrementos sucessivos (não só o sinal):
para p≥1,7 essa razão já relaxou para o regime geométrico assintótico
em k=8-11; para p≤1,6, incluindo o valor previsto, a razão **ainda está
se movendo** — a assinatura clássica de "desaceleração crítica" perto
de qualquer ponto crítico, não evidência de que a criticalidade esteja
acima de 1,6. O transiente conhecido de q=5 (decaimento k^-0,222) cai só
~7% entre k=8 e k=11; reduzi-lo pela metade exigiria k≈250 — impossível
por enumeração exaustiva (custo 5^k). Tentativas de extrapolação
(Aitken/Richardson) deram valores instáveis e não confiáveis (o
transiente parece oscilatório, não geométrico simples — quebra a
premissa do extrapolador).

**Veredito final (Fable + verificação própria)**: inconclusivo, não
desconfirmatório. Não dá para distinguir, com este método, entre o
valor previsto estar logo abaixo do índice real (consistente com a
teoria) ou bem abaixo dele (evidência contra). Ir mais fundo por
enumeração exaustiva não resolve — o custo cresce exponencialmente
(5^k) enquanto o transiente decai em lei de potência lenta.

## Veredito consolidado (as duas rodadas juntas)

Nenhuma das duas rotas confirma a Conjectura para q≥5, nenhuma a
refuta. Ambas são muito mais informativas que a medição original
subdimensionada. O texto do paper (main.tex/main-pt-br.tex, §3.3) foi
reescrito para refletir isso honestamente — ver commit correspondente.
Caminhos mais promissores para resolver isso de vez, se a linha for
retomada: uma comparação pré-registrada tipo Clauset-Shalizi-Newman com
orçamento muito maior que enumeração exaustiva, testando explicitamente
contra um ajuste log-periódico (ver correção abaixo — a via do "espectro
subdominante" foi fechada por E-105: não existe subdominante isolado a
controlar).

**Correção de terminologia (2026-07-19, ver H-129/E-105)**: a frase
"raiz complexa subdominante do operador de transferência" que aparecia
aqui e no restante do projeto estava errada. Uma consulta ao Fable
resolveu a formalização correta do operador (par dual L_α/M_α agindo
sobre Z_q) e mostrou, com verificação numérica exata em E-105, que M_α
tem espectro EXATAMENTE {Λ,0} em qualquer nível de truncamento — gap
espectral perfeito, sem nenhum autovalor subdominante isolado. O
transiente k^-0,222 não é um fenômeno espectral linear — pertence a
uma camada não-linear diferente (ver Estágio 2 abaixo para o que essa
camada acabou não sendo).

## Estágio 2 (2026-07-19) — hipótese log-periódica testada e NÃO suportada

Levantamos a hipótese de que o transiente k^-0,222 fosse um efeito de
reticulado log-periódico (pesos dos ramos são potências de 2). Antes
de testar, consultamos o Fable para DERIVAR o período previsto (não
ajustar aos dados — a mesma armadilha que já pegou o a* em H-129).

**Derivação (Fable)**: os multiplicadores A_a=(5·2^-a)^θ formam um
reticulado deslocado por tipo (u0 mod 5), com deslocamento
b_i/s=(log₂5−a₀(i))/4 — **irracional**, pois log₂5 é irracional (5 não
é potência de 2). Pela dicotomia aritmético/não-aritmético da teoria de
renovação implícita (Goldie 1991), este é o caso **não-aritmético**:
não deve haver correção log-periódica assintótica (a fase gira log₂5
por nível, irracional, e "lava" com k crescente — teorema de
Blackwell). Dois períodos candidatos seriam visíveis só como artefato
de profundidade finita, com amplitude esperada DECRESCENTE em k:
θ·log2=0,4512 ("união", todos os a) e 4θ·log2=1,8047 ("por-tipo",
espaçamento d=ord₅(2)=4), em log natural de x.

**Teste** (`stage2_periodogram.py`): ajuste de lei de potência pura via
CSN nas 4 amostras de W_v (headroom 10⁵-10⁸, n=5000 raízes cada, já
existentes de E-103 Rodadas 1-2), resíduo log(S_emp/S_pred) em
t=log(x/xmin), potência de Lomb-Scargle medida EXATAMENTE nos dois
períodos pré-registrados (não escolhidos a posteriori), comparada
contra o nível de ruído de fundo (grade ampla de períodos).

**Resultado**: em nenhum dos 4 headrooms a potência nos períodos
previstos passa do percentil 95 do ruído de fundo. No período "união"
(bem cotado — 6,7 a 9,7 ciclos cabem no alcance dos dados), a potência
é praticamente nula (0,003-0,010, ruído de fundo médio ~0,11-0,14). No
período "por-tipo", 3 dos 4 headrooms também dão potência próxima de
zero; o único valor não-trivial (H=10⁸, potência=0,1985) ainda fica
abaixo do p95 (0,263), tem só 1,7 ciclos no alcance dos dados (abaixo
do mínimo recomendável), e aparece no headroom MAIS profundo — o
oposto do que a previsão teórica diria (amplitude deveria decrescer
com k, não aparecer só no k mais profundo). Os três fatos triangulam
para ruído, não sinal.

**Veredito**: hipótese log-periódica **testada e não suportada** —
consistente com a própria previsão teórica do Fable (caso
não-aritmético, sem log-periodicidade assintótica esperada). Isso é
uma confirmação mútua teoria+dado, não uma coincidência favorável.
Checagem de coerência de fase entre headrooms (planejada como guarda
estrutural) ficou sem objeto — não há amplitude para checar fase.

**O que isso NÃO fecha**: a origem do transiente k^-0,222 continua em
aberto. Já refutamos dois mecanismos candidatos (raiz espectral
isolada — E-105; log-periodicidade — aqui). Isso não "explica" o
transiente, só elimina duas explicações específicas. A própria origem
numérica do valor "0,222" permanece sem localização no projeto (ver
correção em H-109/E-105).

**Checagem complementar no eixo k** (`stage3_k_axis_check.py`, dados
da Rodada 3, k=5..11): a razão de incrementos sucessivos de M_k(p) é
MONOTÔNICA em k, sem nenhum sinal de oscilação, para os 3 valores de p
próximos do índice previsto — corrobora (não prova de novo) a ausência
de oscilação já estabelecida em E-105/Estágio 2. Uma tentativa de
ajustar |razão(k)−1|~k^-χ para comparar contra "0,222" foi feita e
DESCARTADA (revisão do advisor): o alvo "1" só é assintoticamente
correto exatamente no p crítico, e n=5 pontos suaves/correlacionados
não sustenta um erro-padrão confiável (o χ ajustado varia 0,98 a 3,60
entre os 3 p's testados — sinal de sub-poder, não medida real). O
código fica no repositório por transparência, mas o número não deve ser
citado. Resolver a origem de "0,222" continua exigindo ou localizar a
derivação original, ou estender k além do teto de memória de 5^k (uma
formulação nova, não um ajuste de script) — nenhum dos dois é uma ação
imediata.

## Estágio 4 (2026-07-19) — família de escala por tipo de resíduo: CONFIRMADA (mas não testa κ)

A previsão colateral do Fable (pesos relativos por tipo C_i ∝
2^(−a₀(i)θκ), i.e. (2⁻⁴,2⁻³,2⁻¹,2⁻²) para tipos u0 mod 5 = 1,2,3,4)
foi testada, não deixada para depois. Reconstruí a lista de raízes
(mesma seed, sem refazer o DFS) para recuperar o tipo de cada amostra
de W_v já coletada, e comparei razões de quantis condicionais x_i/x_1
(top30%/20%/10%) contra a previsão (C_i/C_1)^(1/κ), κ=α₊/α₋=1,536290.

**Resultado**: bate muito bem (2-9% de desvio) em TODOS os 4 headrooms
independentes e 3 níveis de cauda, com notável estabilidade cruzada
(ex. x₃/x₁≈4,06-4,12 ao longo de 4 ordens de grandeza de headroom —
não parece ruído). Consultei o Fable para confirmar a tradução, e ele
revelou um ponto crucial que eu não tinha visto: **κ se cancela
algebricamente** nessa razão — (C_i/C_j)^(1/κ) = 2^((a₀(j)−a₀(i))θ),
independente de κ. Ou seja, este teste confirma a **família de escala
exata W_i =_d 2^(−a₀(i)θ)·W\*** (mesma distribuição para todo tipo de
resíduo, só reescalada por θ e a₀) e rejeita a alternativa "C_i entra
linearmente" (previria x₃/x₁=8; medido 4,06-4,12) — mas **não testa o
índice de cauda κ em si**. Escopo exato: confirma θ e a decomposição
multi-tipo, não κ; e é exato só no modelo idealizado (resíduos
sistemáticos de 2-9% medem onde a árvore real diverge da hipótese de
resíduo-filho uniforme i.i.d.).

## Estágio 5 (2026-07-19) — pool reescalado por tipo: não melhora o teste de κ

Tentativa de usar a família de escala do Estágio 4 para um teste mais
limpo de κ: reescalei as 5000 amostras pelo fator previsto 2^(a₀(tipo)θ)
e rodei a mesma bateria de 4 estimadores (Estágio/Rodada 2) no pool
reescalado. **Não melhorou**: Huisman ficou em ~1,50 (IC95%
[1,38;1,63], cobre 1,536, estável nos 4 headrooms) e Gabaix-Ibragimov
em ~1,57 — consistente com κ=1,536, não confirmatório (mesmo padrão de
sempre); GPD continua sem platô de limiar limpo. O CSN+Vuong pareceu
piorar (lognormal favorecida com p<0,001 em 3 dos 4 headrooms), mas
isso é ARTEFATO: nesses 3 casos o x_min ótimo por KS caiu para dentro
do CORPO da distribuição (n_tail~2000, ~40% da amostra, não é teste de
cauda). O único headroom com cauda genuína por CSN (H=10⁵, x_min=95,
n_tail=112) deu "indistinguível" (p=0,93), não lognormal — evidência de
que o sinal "lognormal" nos outros 3 é artefato de corpo, não de cauda.
Lognormal global já está descartada de outra forma: M_k(p) diverge
para p≥1,7 (Rodada 3) — lognormal tem todos os momentos finitos,
incompatível com um momento exato divergente.

**Veredito consolidado dos Estágios 4-5**: um achado estrutural novo e
real (família de escala por tipo), mas de escopo limitado — não
resolve nem aproxima a resolução da Conjectura do índice de cauda. κ
continua **consistente com 1,536290, não confirmado**: mesmo obstáculo
de sempre (5000 amostras não alcançam profundidade de cauda suficiente
para decidir), agora com a razão precisa por que o teste de razão de
quantis não pode ajudar (é κ-invariante por construção).

## Arquivos

- `experiment_tail_index_q5.py` — Rodada 1 (Hill/Zipf simples).
- `results.json` — resultados da Rodada 1.
- `full_battery.py` — Rodada 2 (bateria de 4 estimadores).
- `stage0_iid_power_check.ABANDONED.py` — ideia descartada, documentada.
- `stage1_exact_moment_test.py` — Rodada 3 (momento populacional exato).
- `stage1_moment_results.json` — resultados da Rodada 3 (k=5..11).
- `rerun_save_raw.py` — script auxiliar que reroda a Rodada 1 salvando
  amostras brutas de W_v (usado para alimentar a Rodada 2 sem refazer
  o DFS).
- `stage2_periodogram.py` — Estágio 2 (teste log-periódico pré-registrado).
- `stage2_periodogram_results.json` — resultados do Estágio 2 (4 headrooms).
- `stage3_k_axis_check.py` — checagem de monotonicidade no eixo k (sem
  ajuste citável — ver seção "Checagem complementar no eixo k" acima).
- `stage4_type_constants_check.py` / `stage4_type_constants_results.json`
  — Estágio 4 (família de escala por tipo, confirmada).
- `stage5_rescaled_pool_battery.py` / `stage5_rescaled_pool_results.json`
  — Estágio 5 (pool reescalado, não melhora o teste de κ).

Mirror público (código idêntico, adaptado para autocontido):
`collatz-endogeny/sec3-pressure-equation/` (`full_battery.py`,
`exact_moment_test.py`).

## Reproduzir

```
python3 experiment_tail_index_q5.py    # ~20 min, Rodada 1
python3 full_battery.py                # ~25 min, Rodada 2 (precisa das amostras brutas — ver rerun_save_raw.py)
python3 stage1_exact_moment_test.py    # ~15 min (k ate 11), usa ~10-15GB RAM no pico
python3 stage2_periodogram.py          # segundos, precisa das amostras brutas (rerun_save_raw.py)
python3 stage3_k_axis_check.py         # segundos, usa stage1_moment_results.json
python3 stage4_type_constants_check.py # ~1 min, reconstroi raizes + amostras brutas
python3 stage5_rescaled_pool_battery.py # ~2 min, idem
```

## Próximos passos (se a linha for retomada)

1. ~~Controle analítico do espectro subdominante do operador de
   transferência~~ — **fechado por E-105**: não há autovalor
   subdominante isolado a controlar, o gap espectral da camada linear é
   perfeito e comprovado.
2. ~~Testar o ajuste log-periódico contra a lei de potência pura~~ —
   **fechado pelo Estágio 2 (2026-07-19)**: testado e não suportado,
   consistente com a derivação teórica do Fable (caso não-aritmético).
   Ver seção acima.
3. Bateria estatística completa (CSN+Vuong pré-registrado) com amostra
   muito maior (10^5+ raízes) e headroom maior, se viável
   computacionalmente — ainda não feito, e nenhum dos achados desta
   sessão (Estágios 2-5) o torna menos necessário. Este continua sendo
   o único caminho concreto identificado para de fato pressionar o
   índice de cauda κ, dado que o teste de razão de quantis (Estágio 4)
   é κ-invariante por construção e o pool reescalado (Estágio 5) não
   melhorou o poder do teste.
4. Ver H-129 para uma frente teórica paralela (otimização ergódica)
   que pode dar uma caracterização exata do congelamento sem depender
   de estimadores numéricos.
5. ~~Testar o transiente k^-0,222 no eixo em que ele foi observado~~ —
   checagem leve feita (`stage3_k_axis_check.py`): sem oscilação visível
   na razão de incrementos de M_k(p), k=5..11. Só 5-7 pontos existem por
   causa do teto real de memória de 5^k — não dá para medir decaimento
   de amplitude com k nem localizar "0,222" com esses dados. **Item real
   que resta, não executado**: localizar a derivação original de
   "0,222" (busca, não cálculo novo) ou estender k além do teto atual
   (formulação nova, custo alto).
6. ~~Previsão colateral falsificável (pesos por tipo de resíduo)~~ —
   **feita, Estágio 4 (2026-07-19)**: CONFIRMADA (família de escala
   exata por tipo), mas mostrou não testar κ (cancela algebricamente).
   Tentativa de usar isso para melhorar o teste de κ (Estágio 5) também
   feita — não ajudou. Ver seções acima.
