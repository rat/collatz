# E-061 — Verificação do paper #029 (Alic, "Collatz Progressions Reframed")

Hipótese relacionada: [`H-061-alic-p2er-review.md`](../../hypotheses/H-061-alic-p2er-review.md)

## Paper

Alic, N. (2026). *Collatz Progressions Reframed: Exponent
Representation, Algorithmic Hierarchies, and Record Computations*.
IEEE Access, vol. 14, peer-reviewed. PDF local:
`literature/papers/029_Collatz-Progressions-Reframed.pdf`. Paper de
algoritmos/engenharia — não faz alegação matemática sobre Collatz.

## O que foi testado

A álgebra central P2ER (representar `n` como vetor de expoentes de
potências de 2; passo ímpar = concatenação+consolidação via carry
binário; passo par = deslocamento em bloco):

1. Passo ímpar vs. `3n+1` direto — 500 trajetórias aleatórias (`n` até
   4000 bits), 20.000 passos testados.
2. Passo par vs. divisão repetida direta — 500 casos.
3. Exemplo numérico do próprio paper (Figura 1, `n=15`, sequência
   completa de 17 passos).
4. Exemplos de "waiting line" e "end-gap" (pág. 5).

## Resultado

**Álgebra confirmada correta em todos os testes**, incluindo reprodução
exata de todos os exemplos numéricos do paper. Dá confiança de que os
benchmarks comparativos (PASA/REN/UPX/ACCEL/POW2BASIC) medem
implementações corretas do mapa de Collatz. A "computação recorde"
(`2^{1.024.001}-1`, 13,8 milhões de passos) não foi reproduzida —
computacionalmente inviável nesta sessão (o próprio paper levou horas
numa máquina de 56 núcleos/512GB RAM).

## Como reproduzir

```
python3 experiment.py
```

Sem dependências além da stdlib. Roda em alguns segundos. **Nota de
implementação**: a primeira versão deste script usava uma função
`consolidate()` ingênua (O(n²), rescaneava o histograma inteiro a cada
carry) que travou com os parâmetros originais (n até 4000 bits, 500
trials) — reescrita para uma varredura linear única (O(faixa de
expoentes)) antes de rodar de verdade.
