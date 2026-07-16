# H-087 — G(v)=D(v)·v mostra continuidade 3-ádica real (decaimento de variância com mais dígitos fixados)

Status: confirmada (evidência moderada-forte, não uma prova); abre caminho para as ideias 1-2 do Fable (Mahler / medida de Syracuse em ℤ₃)
Criada em: 2026-07-15
Origem: continuação direta de H-086 (recalibração de H-024). Depois de
confirmar que a maior parte da "variação de 300×" de H-024 era o termo
trivial D(v)~C/v, a pergunta natural é se o que sobra — o resíduo
G(v)=D(v)·v — tem estrutura 3-ádica genuína (o pré-requisito que o
próprio Fable sugeriu testar antes de investir em expansão de Mahler
ou na medida de Syracuse em ℤ₃).

## O teste

`experiments/E-087-3adic-continuity-of-residual/experiment.py`: para
cada nível de precisão K (resíduo mod 3^K), construímos uma cadeia
**nested** de dígitos base-3 (cada K refina o anterior, aproximando um
único inteiro 3-ádico) e sorteamos vários v com esse resíduo fixo,
**magnitude livre** ao longo de 5 ordens de grandeza (10² a 10⁷) —
correção metodológica direta do erro que o Fable apontou em H-024
(nunca deixar a magnitude contaminar a leitura). Medimos a variância de
log₁₀(G(v)) para cada K, e repetimos com **5 cadeias de resíduo
independentes** (sementes diferentes) — mesmo cuidado que já derrubou a
falsa hipótese mod9 nesta sessão, para não confiar numa única
coincidência de amostra.

## Resultado

| K | desvio-padrão médio de log₁₀(G) (5 cadeias) |
|---|---|
| 1 | 0,4145 ± 0,0731 |
| 2 | 0,2371 ± 0,0675 |
| 4 | 0,1984 ± 0,0281 |
| 6 | 0,1343 ± 0,0609 |
| 8 | 0,1010 ± 0,0527 |

**A variância cai monotonicamente e de forma consistente nas 5 cadeias**
— redução de mais de 4× no desvio (K=1→K=8), com uma razão de
decaimento por unidade de K aproximadamente geométrica (~0,80-0,87 por
passo, com alguma variação entre trechos — a série não é perfeitamente
exponencial com os tamanhos de amostra testados, mas a direção e a
magnitude do efeito são claras e reprodutíveis entre cadeias
independentes).

## Interpretação

Diferente de H-024 (onde nenhum K finito explicava D(v) — a variância
não caía, ficava presa no mesmo patamar não importava quanto K
crescesse), aqui **G(v)=D(v)·v mostra continuidade 3-ádica real**:
fixar mais dígitos base-3 de v reduz sistematicamente a incerteza sobre
G(v), mesmo com a magnitude de v livre para variar por ordens de
grandeza. Isso é evidência (moderada — 5 cadeias, 15 amostras cada,
não uma prova formal) de que G, ao contrário de D bruto, **é
aproximadamente uma função contínua do inteiro 3-ádico v** — abrindo
de fato a porta, como o Fable sugeriu, para uma expansão de Mahler
(coeficientes a_n cuja taxa de decaimento capturaria essa estrutura) ou
uma conexão com a medida de Syracuse em ℤ₃ (candidata explícita e
computável via programação dinâmica, proposta pelo próprio Fable como
ideia 2).

## O que ainda falta para essas ideias serem viáveis

Este teste só mostra que a variância *diminui* com K — não mede a taxa
de decaimento com precisão suficiente para ajustar uma expansão de
Mahler real, nem verifica se a "continuidade" sobrevive em amostras
muito maiores (o teste usou 15-20 amostras por ponto; um resultado mais
robusto pediria centenas). É um sinal verde qualificado para investir
nas ideias 1-2 do Fable, não uma confirmação definitiva de que elas vão
dar em algo.

## Atualizações

- 2026-07-15: testado com 5 cadeias de resíduo independentes (K=1,2,4,
  6,8; 15 amostras cada). Variância de log₁₀(G) cai monotonicamente e
  de forma consistente entre as 5 cadeias — mais de 4× de redução total.
  Diferente de H-024 (D bruto, nenhuma redução observável com K
  crescente), aqui há evidência real de continuidade 3-ádica. Não
  testado ainda: amostras maiores para caracterizar a taxa de decaimento
  com precisão, nem a expansão de Mahler propriamente dita.
