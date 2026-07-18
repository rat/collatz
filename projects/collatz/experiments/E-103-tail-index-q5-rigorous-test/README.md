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
acima de 1,6. O transiente conhecido de q=5 (raiz complexa subdominante,
decaimento k^-0,222) cai só ~7% entre k=8 e k=11; reduzi-lo pela metade
exigiria k≈250 — impossível por enumeração exaustiva (custo 5^k).
Tentativas de extrapolação (Aitken/Richardson) deram valores instáveis
e não confiáveis (o transiente real é oscilatório de raiz complexa, não
geométrico simples — quebra a premissa do extrapolador).

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
retomada: controle analítico sobre o espectro subdominante do operador
de transferência, ou uma comparação pré-registrada tipo
Clauset-Shalizi-Newman com orçamento muito maior que enumeração
exaustiva.

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

Mirror público (código idêntico, adaptado para autocontido):
`collatz-endogeny/sec3-pressure-equation/` (`full_battery.py`,
`exact_moment_test.py`).

## Reproduzir

```
python3 experiment_tail_index_q5.py    # ~20 min, Rodada 1
python3 full_battery.py                # ~25 min, Rodada 2 (precisa das amostras brutas — ver rerun_save_raw.py)
python3 stage1_exact_moment_test.py    # ~15 min (k ate 11), usa ~10-15GB RAM no pico
```

## Próximos passos (se a linha for retomada)

1. Controle analítico do espectro subdominante do operador de
   transferência (a raiz complexa causando o transiente k^-0,222) —
   resolveria a ambiguidade da Rodada 3 sem precisar de mais
   profundidade computacional.
2. Bateria estatística completa (CSN+Vuong pré-registrado) com amostra
   muito maior (10^5+ raízes) e headroom maior, se viável
   computacionalmente.
3. Ver H-129 para uma frente teórica paralela (otimização ergódica)
   que pode dar uma caracterização exata do congelamento sem depender
   de estimadores numéricos.
