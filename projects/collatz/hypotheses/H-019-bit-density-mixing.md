# H-019 — Tempo de mistura da densidade de bits (popcount)

Status: confirmada qualitativamente (crescimento linear em k, razão estabiliza ~1.3-1.5)
Criada em: 2026-07-13
Origem: ideia do brainstorm do modelo Fable ("H-E").

## Enunciado

A densidade de bits 1 (popcount/comprimento em bits) dos iterados de uma
órbita de Collatz converge para 1/2, mas com memória: partindo de extremos
(2^k−1, densidade 1; 2^k+1, densidade baixa), a relaxação para 1/2 deveria
levar Θ(k) passos acelerados — porque 3n+1 é uma operação local (janela de
poucos bits + carry), não um embaralhamento global instantâneo.

## Por que é interessante

Primeira estatística **global** de bits do projeto (não redutível a
resíduo mod 2^k, que já cobrimos em H-002/H-005 — aqui olhamos a proporção
de 1s no número inteiro, não resíduos de baixa ordem).

## Como testar

Para famílias de números com densidade de bits controlada nos extremos
(popcount fixo alto ou baixo, ex: 2^k−1 com todos os bits 1, ou 2^k+1 com
só 2 bits 1), medir a densidade de bits do iterado a cada passo acelerado e
estimar quantos passos levam até |densidade−0.5|<ε, comparando contra k
(previsão: tempo de mistura cresce linearmente em k, não constante).

## Atualizações

- 2026-07-13: hipótese aberta.
- 2026-07-13: testada em `experiments/E-019-bit-density-mixing/`. Razão
  passos-até-misturar/k estabiliza em ~1.3-1.5 (denso) e ~1.0-1.23 (esparso)
  ao longo de k=8 a 1024 — confirma crescimento linear (não constante),
  consistente com 3n+1 sendo operação local. Achado qualitativo, sem
  constante exata derivada teoricamente.
