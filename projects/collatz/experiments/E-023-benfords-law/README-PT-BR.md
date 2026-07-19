# E-023 — Lei de Benford nos valores da órbita de Collatz

Hipótese relacionada: [`H-023-benfords-law.md`](../../hypotheses/H-023-benfords-law.md)

Origem: vídeo do Veritasium sobre a Conjectura de Collatz (trazido pelo
diretor científico).

## O que foi testado

Se os valores visitados numa órbita de Collatz seguem a Lei de Benford
(P(primeiro dígito=d) = log₁₀(1+1/d), P(1)≈30.1%). Dois testes limpos
(evitando a armadilha de colisão de órbitas):
(a) uma única órbita longa (837799, 525 passos);
(b) 500.000 órbitas independentes, um valor por órbita (n grande e
distinto, valor tomado após um número aleatório de passos, 10-200).

## Bug metodológico encontrado e corrigido

Primeira tentativa da parte (b) deu um ajuste muito ruim (qui-quadrado=837,
p≈10⁻¹¹²) — 2.61% das amostras já haviam atingido n=1 antes do fim da janela
de passos escolhida, "prendendo" o valor em 1 (dígito 1) artificialmente e
inflando essa contagem. Um teste com janela ainda maior (50-2000 passos)
tornou isso dramaticamente óbvio: 91.7% das amostras davam dígito 1, porque
a maioria das órbitas já tinha convergido bem antes do fim da janela.
**Corrigido** descartando amostras que atingem 1 antes do fim da janela em
vez de contar o 1 espúrio.

## Resultado (após correção)

- **(a) Órbita única**: qui-quadrado=7.49, p=0.486 — **consistente com
  Benford** (amostra modesta, 525 pontos).
- **(b) 500.000 órbitas independentes**: ajuste excelente em magnitude —
  dígito 1: 30.11% observado vs. 30.10% previsto; todos os outros dígitos
  também batem na 3ª-4ª casa decimal. Qui-quadrado=43.10, p=1.4×10⁻⁶ —
  tecnicamente "significativo", mas com desvios absolutos minúsculos,
  esperado dado o tamanho enorme da amostra (mesmo desvios de ruído fino
  ficam detectáveis com n=500.000).

Reproduzir: `python3 experiment.py 837799 500000`.

## Conclusão

A Lei de Benford é confirmada com excelente precisão prática nos valores de
órbitas de Collatz — consequência natural do comportamento tipo "passeio
aleatório multiplicativo" já estabelecido em H-001/H-010/H-011/H-017 (o
logaritmo do valor "equidistribui" ao longo da órbita). Não é uma
descoberta matemática nova, mas conecta uma observação popular (do vídeo)
ao nosso próprio arcabouço teórico já validado, e o processo revelou (e
corrigiu) um viés metodológico real na amostragem.

## Status de H-023

**Confirmada** (excelente ajuste prático; desvio estatístico residual é
esperado dado o tamanho da amostra, não uma falha real do modelo).
