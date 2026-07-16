# E-090 — Medida de Syracuse μ em ℤ₃ vs. densidade residual G(v)

Hipótese relacionada: [`H-090-syracuse-measure-explains-density-residual.md`](../../hypotheses/H-090-syracuse-measure-explains-density-residual.md)

## O que foi feito

O Fable propôs (e ajudou a validar a montagem matemática antes de
implementar) que G(v)=D(v)·v — o resíduo 3-ádico de D(v) depois de
remover o termo trivial de magnitude (H-086) — é bem aproximado pela
densidade local de uma medida μ em ℤ₃, definida pela mesma recursão
do Lemma 1.12 de Tao (2022) para a variável Syrac(ℤ/3ⁿℤ), já
implementada e verificada neste projeto em E-076.

Reaproveitamos essa implementação, escrevemos uma versão truncada em
ponto flutuante para escalar a m maior (validada contra a versão
exata, erro ~0), e comparamos 3^m·μ_m(r) com a média geométrica de
G(v) medida computacionalmente para v's com resíduo r mod 3^m,
magnitude controlada.

## Resultado

Correlação log-log forte e crescente com m: 0,916 (m=2) → 0,969 (m=3)
→ 0,980 (m=4), estável em 5 sementes independentes (0,947-0,988 para
m=3, 0,968-0,981 para m=4). A conjectura do Fable se confirma com
evidência real. Ver H-090 para a análise completa.

## Reproduzir

```
python3 experiment.py
```
