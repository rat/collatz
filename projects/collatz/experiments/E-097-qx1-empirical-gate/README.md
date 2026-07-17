# E-097 — Portão estatístico empírico para a generalização qx+1 (H-113)

Hipótese relacionada: [`H-113-statistical-gate-kontorovich-lagarias-vs-volkov.md`](../../hypotheses/H-113-statistical-gate-kontorovich-lagarias-vs-volkov.md)

## O que foi feito

Mede o expoente de contagem empírico da árvore reversa real de 5x+1
para decidir entre duas previsões teóricas concorrentes da literatura:
Kontorovich-Lagarias (2009), 0,650919 (idêntico à nossa segunda raiz da
equação de pressão qx+1, H-109), vs. Volkov, 0,678.

## Arquivos

- `pressure_qx1.py`, `empirical_qx1_tree.py` — scripts originais do
  Fable (verificação da equação de pressão multitipo; primeira
  confirmação empírica ad hoc, citada em H-109 mas nunca antes
  persistida no repositório).
- `pilot_gate_5x1.py`, `pilot2_gate_5x1.py` — pilotos de calibração de
  ruído/viés/custo (regra de admissibilidade q=5, sensibilidade ao
  viés de truncamento).
- `experiment_gate_production.py` — produção n=300, janela fixa
  1e5-1e8, buffer=5 décadas (primeira versão; documentado em H-113
  como o passo que revelou o modo de falha "IC exclui os dois
  candidatos" previsto pelo Fable).
- `experiment_gate_richardson.py` — versão final: DFS com rastreio de
  path-max (uma única passada dá as contagens em todos os buffers
  simultaneamente, validado byte-a-byte contra o método antigo) +
  extrapolação de Aitken Δ² na curva média entre raízes + bootstrap.

## Resultado

Aitken Δ² (buffer→∞): **0,639, IC95%=[0,633, 0,645]** — exclui Volkov
(0,678) com folga ampla (~10+ erros-padrão); o resíduo até
Kontorovich-Lagarias (0,650919) tem assinatura de pré-assintótica de
janela fixa (painel de slope por década ainda sobe na última década
testada), não de viés de truncamento não corrigido. Ver H-113 para a
análise completa, incluindo uma correção necessária a uma alegação
anterior de H-109 (o Hill estimator "1,547 vs 1,5363" citado lá não é
confirmatório — erro padrão real ~0,45).

## Reproduzir

```
python3 experiment_gate_richardson.py
```
