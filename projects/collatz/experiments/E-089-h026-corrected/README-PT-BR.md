# E-089 — Reteste corrigido de H-026 (K maior ajuda a prever G(v)?)

Hipótese relacionada: [`H-089-h026-corrected-K-does-help.md`](../../hypotheses/H-089-h026-corrected-K-does-help.md)

## O que foi feito

H-026 original concluiu que fixar mais dígitos base-3 (K maior) não
reduz a divergência da aproximação de memória finita. O modelo Fable
mostrou por aritmética direta que essa conclusão estava contaminada
pelo mesmo termo trivial de magnitude D(v)≈C/v identificado em H-086 —
H-026 nunca testou a variável certa (G(v)=D(v)·v). Reimplementamos o
teste medindo a **dispersão** de log₁₀(G) dentro de janelas de
magnitude fixas e controladas, com múltiplas cadeias de resíduo
independentes.

## Bug encontrado e corrigido no caminho

Uma primeira tentativa usou janelas de magnitude estreitas demais para
K grande — o espaçamento mod 3^K excedia a largura da janela, forçando
a amostragem a repetir o mesmo v (variância zero espúria). Corrigido
verificando que a janela contém valores distintos suficientes antes de
amostrar, e usando janelas mais largas.

## Resultado

Dispersão de log₁₀(G) cai monotonicamente com K: 0,2352 (K=2) → 0,1748
(K=4) → 0,1444 (K=6) → 0,0936 (K=8) — consistente nas 3 janelas de
magnitude testadas. **K maior reduz a incerteza sobre G(v)** — o
oposto da conclusão original de H-026. Ver H-089 para a análise
completa.

## Reproduzir

```
python3 experiment.py
```
