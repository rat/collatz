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

## Experimento de controle de 3 braços (H-111, 2026-07-17)

Calibra quantitativamente a barreira de endogenia de H-110: braço 1
(`experiment_synthetic_core.py`) simula a árvore sob a hipótese nula de
dígitos 3-ádicos frescos independentes entre subárvores; braço 2
(mesmo arquivo, parâmetro `rho`) adiciona acoplamento de conteúdo
ajustável entre subárvores irmãs; braço 3 (`experiment_control_arms.py`,
reusa `measure_G_headroom`) remede a árvore aritmética real no mesmo
`mult` dos braços sintéticos. `experiment_synthetic_dp_oracle.py` é um
oráculo de programação dinâmica exata para validar a criticidade do
simulador (E[G|tipo]) sem Monte Carlo.

Resultado: nenhum acoplamento aritmético positivo detectado entre
braço 1 e braço 3; cota ρ_eff≲0,06 (IC95%, m=20). Ver H-111 para a
documentação completa, incluindo uma autocorreção do Fable na
derivação teórica de criticidade (descoberta pelo checklist de
validação, não um bug de implementação).

```
python3 experiment_synthetic_core.py          # checklist de validacao
python3 experiment_control_arms.py braco1     # braco 1, grade completa
python3 experiment_control_arms.py braco3     # braco 3, remedido
python3 experiment_control_arms.py slope      # slope + bootstrap de excesso (resultado final)
```
