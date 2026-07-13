# E-028 — Consolidação da família de exclusões via CRT

Hipótese relacionada: [`H-028-crt-exclusion-family-consolidated.md`](../../hypotheses/H-028-crt-exclusion-family-consolidated.md)

Origem: sugestão do advisor — a família de teoremas de exclusão (H-007,
H-014, H-022, H-027) consolidada é o candidato mais realista a resultado
"publicável" do projeto até agora, mais do que qualquer hipótese isolada
ou as direções espectrais/especulativas.

## O que foi testado

Combinar via CRT as quatro regras de exclusão provadas (mod3, mod6, mod8,
mod9) numa única caracterização mod 72, e validar contra os 148
recordistas reais conhecidos (OEIS A006877).

## Resultado

45 de 72 resíduos mod 72 (62.5%) provavelmente excluídos. Zero violações
contra os 148 recordistas reais. 18 dos 27 resíduos permitidos aparecem de
fato na amostra.

Reproduzir: `python3 experiment.py` (usa o arquivo de dados de E-004).

## Status de H-028

**Confirmada** — consolidação aritmética (CRT é elementar), sem
matemática nova além da combinação, mas resultado limpo e validado a
100% contra os dados reais.
