# H-026 — A taxa de divergência da aproximação de memória finita parece independer de K

Status: **REVERTIDA (2026-07-16, ver H-089)** — a conclusão original estava errada, não só fraca: media D(v) bruto, dominado pelo termo trivial de magnitude D~C/v (H-086), o que garantia matematicamente "K não importa" independente da verdade. Testado corretamente sobre G(v)=D(v)·v (a variável certa, H-087), K maior REDUZ a dispersão de forma clara. Ver H-089 para o teste corrigido e a explicação do erro.
Criada em: 2026-07-13
Origem: extensão direta de H-024, item #15 de uma quarta lista de ideias
externas ("operador de transferência com memória 3-ádica finita crescente,
medindo a taxa de divergência"). H-024 provou que não existe aproximação
*exata* de dimensão finita; esta hipótese pergunta pela *taxa* na qual a
aproximação de profundidade K se degrada conforme a magnitude cresce, e se
K maior "aguenta" mais tempo antes de degradar.

## Enunciado

Fixando um resíduo r mod 3^K (derivado de J_4=85) e usando D(v) no menor v
daquele resíduo como "previsão" de memória-K, o erro |log(D(v)/D(v₀))|
cresce sem limite conforme a magnitude de v cresce (mantendo o resíduo
fixo) — já esperado a partir de H-024. A pergunta nova: **K maior atrasa
essa divergência** (erro menor para a mesma magnitude v)?

## Como foi testado

Para K∈{4,6,8}, resíduo r = 85 mod 3^K, medido D(v) para v = r + m·3^K
(m=0,2,4,10,20,50,100,200,400, todos pares para evitar colisão de
paridade), com orçamento de magnitude proporcional (budget_bits=18, como
em H-024). D₀ = D(85) é **idêntico nos três casos** (coincidência
aritmética: 85 = 3^K·1 + r para K=4,6,8 dentro do intervalo testado),
permitindo comparação direta entre K's.

## Resultado

Comparando em magnitudes de v similares (log₂v ≈ 13–14, ≈17–18, ≈20–21)
em vez de no mesmo m (que dá v's de escalas muito diferentes por K):

| log₂(v) aprox. | K=4 | K=6 | K=8 |
|---|---|---|---|
| ~13–14 | −3.66 a −5.05 | −2.63 a −5.45 | −5.09 a −5.59 |
| ~17–18 | — | −7.55 a −7.65 | −7.53 a −7.85 |
| ~20–21 | — | — | −9.98 a −9.21 |

Os valores ficam na **mesma ordem de grandeza entre K's diferentes** na
mesma faixa de magnitude — não há evidência de que K=8 "aguenta" mais que
K=4. A divergência parece ser função principalmente de log₂(v) (magnitude
absoluta, "orçamento de bits" já visto em H-018/H-013), não da
profundidade do resíduo fixado.

## Ressalva importante sobre confiança

Este é um resultado **sugestivo, não uma confirmação estatística
robusta**: cada ponto (K, m) é uma ÚNICA medição de uma quantidade já
demonstrada em H-024 como extremamente errática (variação de centenas de
vezes entre v's vizinhos do mesmo resíduo). Os próprios dados mostram
não-monotonicidade dentro de um mesmo K (ex: K=4, m=50 dá −2.17, menos
divergente que m=20 com −2.81 e m=100 com −3.66) — ruído genuíno, não um
efeito suave. Para uma confirmação robusta seria necessário promediar
sobre múltiplos resíduos r por combinação (K, magnitude), o que não foi
feito aqui por prioridade (ver STATE.md — decisão de seguir o loop de
busca ampla em vez de aprofundar esta medição específica).

## Implicação

Combinado com H-024, isto reforça a ideia de que a densidade do
subárvore reverso não tem uma escala natural de "profundidade de memória
que ajuda" — mais dígitos 3-ádicos conhecidos não parecem comprar previsão
adicional além do que a magnitude bruta já dita. Consistente com (não
prova adicional de) a impossibilidade de um operador de transferência de
dimensão finita útil mesmo como aproximação, não só como fórmula exata.

## Atualizações

- 2026-07-13: testado com budget_bits=18, K∈{4,6,8}. Resultado sugestivo
  mas não estatisticamente robusto (ver ressalva acima). Reportado com
  essa hedge explícita em vez de superclaim, seguindo o padrão já usado em
  H-020.
- 2026-07-16: **REVERTIDA**. O modelo Fable, consultado sobre risco
  metodológico nesta linha, mostrou por aritmética direta que os
  valores da tabela acima batem quase exatamente com o termo trivial
  −ln(v/v₀) que H-086 depois identificou (D(v)≈C/v) — ou seja, esta
  hipótese testou D(v) bruto, e a conclusão "K não importa" era
  matematicamente garantida pelo desenho (comparando três cópias do
  mesmo termo dominante, com o efeito real de K, ~0,1-0,4 dex,
  soterrado embaixo de um termo de 5-10 unidades). Testado
  corretamente sobre G(v)=D(v)·v, com dispersão medida em janelas de
  magnitude controladas e 5 cadeias de resíduo independentes
  (`experiments/E-089-h026-corrected/`): a dispersão CAI
  monotonicamente com K (0,2352→0,0936 dex, K=2 a K=8) — o oposto da
  conclusão aqui. Ver H-089-h026-corrected-K-does-help.md.
