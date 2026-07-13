# E-030 — Verificação independente do paper de Chang (2026)

Hipótese relacionada: [`H-030-chang-onebit-mixing-verification.md`](../../hypotheses/H-030-chang-onebit-mixing-verification.md)

Paper: [Edward Y. Chang, "A Structural Reduction of the Collatz Conjecture
to One-Bit Orbit Mixing"](https://arxiv.org/abs/2603.25753) (2026).

## O que foi testado

Verificação computacional independente de três resultados centrais do
paper (Lema 4.1, Teorema 4.2 "Map Balance", mecanismo do bit-4), seguida
de duas extensões: órbitas maiores que o testado no paper, e o conjunto
dos 148 recordistas reais de stopping time (dados já usados em E-004).

## Bugs próprios encontrados e corrigidos

Dois bugs na verificação (não no paper): (1) esqueci de restringir o teste
do bit-4 à condição k=(n−1)/8 ímpar; (2) apliquei o teste mod-8 do Lema
4.1 ao valor errado (n em vez de T(n)). Ambos corrigidos antes de reportar
qualquer resultado — versão final dá zero falhas.

## Resultado

Todos os três resultados verificados sem exceção (Lema 4.1: 50k casos;
Map Balance: K=5..15 exato; bit-4: 12.5k casos). Extensão com os 148
recordistas reais mostrou desvio de ~0,61 (vs. 0,5 esperado) em 9064
observações — mas isso é **pseudo-replicação** (órbitas de recordistas
colidem entre si, confirmado diretamente: 8/45 pares entre os 10 maiores
recordistas compartilham valores de cauda numa janela de 500 passos) e,
mesmo descontando isso, o desvio bate exatamente com o que a própria
Tabela 2 do paper já mostra para órbitas genéricas grandes (desvios de
órbita individual de ±10-25%) — não é achado novo nem contra-evidência.

Reproduzir: `python3 experiment.py`.

## Status de H-030

**Confirmada** (verificação bem-sucedida do paper externo) com extensão
honesta que não superclaimou um desvio aparentemente grande mas
metodologicamente confundido.
