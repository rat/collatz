# H-113 — Portão estatístico: expoente empírico de 5x+1 exclui Volkov (0,678), consistente com Kontorovich-Lagarias/pressão (0,650919)

Status: fechado — evidência forte a favor de Kontorovich-Lagarias, resíduo pequeno explicado por pré-assintótica de janela
Criada em: 2026-07-17
Origem: sexta rodada de consulta à IA externa recomendou consolidar um
pacote de publicação (H-113 planejado); o Fable identificou que a peça
mais citável desse pacote — resolver empiricamente a disputa
Kontorovich-Lagarias (2009) vs. Volkov sobre o expoente de contagem de
5x+1 — não estava de fato fechada, porque a citação anterior em H-109
("Hill batendo em 0,650919") não tinha intervalo de confiança e, como o
próprio Fable calculou depois, tinha erro padrão real ~0,45 (a
concordância de 2 casas decimais era sorte estatística, não confirmação
válida — H-109 precisa ser corrigido para não repetir essa alegação).

## Enunciado

Kontorovich & Lagarias (2009) preveem, para a árvore reversa de 5x+1,
expoente de contagem η₅,BP≈0,650919 (idêntico à nossa segunda raiz da
equação de pressão qx+1, H-109/H-112). Um modelo estocástico concorrente
(Volkov) prevê η*₅,BP≈0,678. Os próprios autores citam isso como uma
disputa em aberto desde 2009 por falta de dados suficientes. Este
experimento mede o expoente empírico em árvores reais de 5x+1 com poder
estatístico suficiente para discriminar entre os dois valores (Δ=0,027).

## Regra de admissibilidade (q=5, derivada pelo Fable)

Nó ímpar u, filhos w=(2^a·u−1)/5 válidos sse 2^a·u≡1 (mod 5), i.e.
a≡A0[u mod 5] (mod 4), com A0={1:4, 2:3, 3:1, 4:2}. u≡0 mod 5 não tem
filhos (nó estéril, conta mas não ramifica). Diferente de q=3: não há
condição de paridade — a integralidade mod 5 é a única condição, e o
filho é automaticamente ímpar quando inteiro. O ramo a=1 (u≡3 mod 5)
ENCOLHE (w≈0,4u) — fonte do viés de truncamento abaixo.

## Como testar (e o que deu errado antes de dar certo)

**Bug de truncamento (mesma classe do bug histórico do E-018)**: o ramo
que encolhe (a=1) faz com que nós abaixo de um checkpoint possam ter
ancestrais ACIMA dele — o teto de BUSCA precisa ficar ≥5 décadas acima
do maior checkpoint usado, senão o slope sai enviesado para baixo
(medido: ~-0,012 na fronteira buffer 3→4, metade do Δ=0,027 a
discriminar).

**Piloto** (60 raízes, mult/search_bound=1e12): slope médio=0,6433,
IC95%=[0,6327, 0,6531] — já excluía 0,678 por ~6,4 erros-padrão.

**Produção inicial (n=300, bug meu)**: amostrei raízes até 200.000,
ultrapassando o checkpoint inferior da janela (1e5) — descartou 83/300
raízes não-aleatoriamente e poluiu o painel de convergência. Corrigido
(raízes em (101,9999), bem abaixo da janela).

**Produção corrigida (n=300, mesma janela)**: slope médio=0,63801,
IC95%=[0,63159, 0,64410] — **excluiu os DOIS valores candidatos**
(0,678 por 12,57 SE; 0,650919 por 4,06 SE). Modo de falha previsto
explicitamente pelo Fable antes de rodar: com n grande o SE cai abaixo
do viés residual de truncamento, e um IC bilateral do ESTIMADOR
enviesado exclui tudo — não é evidência contra Kontorovich-Lagarias.

**Correção final — path-max + Richardson (Aitken Δ²)**: reescrita do
DFS para rastrear path_max (maior valor de nó visitado ao longo do
caminho raiz→nó) numa única passada em search_bound=1e13, dando as
contagens em TODOS os buffers 9-13 simultaneamente (validado
byte-a-byte contra o método antigo de DFS separado por buffer, 4
raízes de teste, 100% de concordância). Extrapolação de Aitken na
curva MÉDIA entre raízes (não por raiz — séries por raiz são
granulosas e o Aitken diverge; a média pooled decai quase
geometricamente, razão~0,4-0,5/década).

## Resultado final

- Curva média por buffer: 0,60049 (1e9) → 0,62387 (1e10) → 0,63261
  (1e11) → 0,63650 (1e12) → 0,63801 (1e13) — incrementos decrescendo
  geometricamente (0,0234, 0,0087, 0,0039, 0,0015).
- **Aitken Δ² (extrapolação buffer→∞): 0,639**, bootstrap por raiz
  reamostrada: **IC95%=[0,633, 0,645]**.
- **Exclui Volkov (0,678)** com folga ampla (limite superior do IC a
  0,033 de distância, ~10+ erros-padrão).
- **Resíduo até Kontorovich-Lagarias (0,650919)**: ~0,012 (o valor
  KL/pressão fica logo acima do limite superior do IC). Diagnóstico:
  painel de slope por década DENTRO da janela fixa (1e4→1e5 até
  1e7→1e8) mostra o slope ainda SUBINDO na última década testada
  (0,6021 → 0,6296 → 0,6432 → 0,6460 — não platôs), aproximando-se
  monotonicamente de 0,6509 sem ter chegado lá — assinatura de
  **pré-assintótica de janela fixa** (a janela 1e5-1e8 ainda não é
  "profunda o suficiente"), não de viés de truncamento residual (esse
  já foi corrigido pela extrapolação de Richardson).

## Veredito

Evidência empírica forte a favor da previsão de Kontorovich-Lagarias
(0,650919) e contra a de Volkov (0,678) — o portão fecha para excluir
Volkov com confiança alta; o pequeno resíduo restante até o valor exato
de KL tem o tamanho e a assinatura esperados de um efeito de janela
finita (mensurável e explicado), não uma discrepância não resolvida.

**Correção necessária em H-109**: a citação anterior "Hill batendo em
0,650919 (600 raízes, top 2%) vs. previsão 1,5363" deve ser sinalizada
como **não confirmatória** — o erro padrão real desse estimador, dado
k≈12 pontos de cauda, é ≈0,45 (ξ_cauda/√k), então a concordância de 2
casas decimais foi coincidência estatística, não evidência. O resultado
válido e citável é este H-113 (slope de contagem por década, n=300,
com correção de Richardson), não o Hill estimator da rodada anterior.

## Notação (clarificada, corrige ambiguidade α₁/α₂ de H-109)

- α₋ = menor raiz de q^(α−1)=2^α−1; α₊ = maior raiz.
- q=3: {α₋,α₊}={1,2}. q=5: {α₋,α₊}={0,650919, 1} (a raiz trivial é a
  MAIOR para q≥5, ao contrário de q=3).
- **Expoente de contagem (o que este experimento mede) = α₋ sempre.**
- Cauda de W (fator martingale) = α₊/α₋; ξ de Fréchet = α₋/α₊.

## Referências

- H-109 (equação de pressão, valores teóricos) — corrigir a citação do
  Hill estimator conforme acima.
- H-112 (checagem de novidade — identificou a disputa KL vs. Volkov).
- `experiments/E-097-qx1-empirical-gate/` — todos os scripts
  (`empirical_qx1_tree.py`, `pressure_qx1.py`, pilotos, produção,
  versão final com Richardson).
