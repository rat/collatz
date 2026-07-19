# E-099 — Teste certificado da Conjectura 3 de Wirsching (2003) via momentos exatos de φ

Hipótese relacionada: [`H-125-wirsching-2003-functional-equation-fabius-atomic-function.md`](../../hypotheses/H-125-wirsching-2003-functional-equation-fabius-atomic-function.md)

## O que foi feito

Teste numérico com erro CERTIFICADO (não heurístico) da Conjectura 3
de Wirsching (2003) — a peça mais concreta de uma cadeia de 3
conjecturas reduzindo densidade positiva de predecessores 3n+1. O
objeto central, φ (densidade invariante do operador de médias W₃, que
acaba sendo o análogo em base 3 da função de Fabius/"atomic function"
de Rvachev), tem momentos RACIONAIS EXATOS via autossimilaridade
(X=d(2U+X)/3) — permitindo avaliar φ em pontos de cauda extrema
(x~ℓ·3⁻ℓ) sem iterar o operador W₃ e sem perda de precisão, via uma
redução por antiderivadas iteradas.

## Resultado

Executado até ℓ=500 (janela CLT, u∈[−2,2]): a razão decisiva
L_ℓ=3^(1−ℓ)φ(3x_ℓ)/φ(x_ℓ) converge ao valor previsto 2/3 com déficit
(0,580±0,001)/ℓ — coeficiente reproduzido de forma independente pela
própria assintótica φ₀ de Berg-Krüppel (1998). ln(φ/φ₀) converge a um
limite finito L=−0,619±0,001(estatístico)±0,015(forma funcional), i.e.
c=e^L≈0,54 (intervalo honesto 0,53-0,55). Uniformidade forte sobre a
janela CLT (dispersão <10⁻⁴ em ℓ=500, contra variação individual de
~100 unidades em ln φ). Nenhuma modulação log-periódica visível.
**Conjectura 3 SUPORTADA numericamente** — mas é a ponta mais concreta
de uma cadeia de 3 conjecturas; as Conjecturas 1 e 2 (acima dela)
permanecem abertas e não são tocadas por este teste. Ver H-125 para a
análise completa.

## Arquivos

- `experiment_conjecture3.py` — script principal: momentos exatos,
  redução por antiderivadas, φ₀ via assintótica de Berg-Krüppel
  (constantes simbólicas α,β,γ,δ,ε), validação (φ(1/2)=3/2 exato,
  momentos centrais ímpares=0), varredura ℓ até 300.
- Extensão ℓ∈{350,400,450,500} (6+ decimais, teste out-of-sample contra
  os modelos de cauda ajustados em ℓ≤300) rodada inline, não
  persistida como script separado — ver H-125 para os números.

## Reproduzir

```
python3 experiment_conjecture3.py
```

Custo: momentos(310)~18s, momentos(510)~5min (cresce ~N^4-5). Não
subir N_MAX sem necessidade — ℓ~1000+ exigiria dezenas de minutos a
horas.
