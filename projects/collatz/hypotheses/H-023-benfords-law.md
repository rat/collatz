# H-023 — Lei de Benford nos valores da órbita de Collatz

Status: confirmada (excelente ajuste prático após corrigir viés metodológico)
Criada em: 2026-07-13
Origem: vídeo do Veritasium sobre a Conjectura de Collatz, trazido pelo
diretor científico ("para o primeiro bilhão de sequências, 1 é de longe o
primeiro dígito mais comum, ~30%").

## Enunciado

Os valores visitados ao longo de órbitas de Collatz deveriam seguir a Lei
de Benford: P(primeiro dígito = d) = log₁₀(1+1/d), com P(1)≈30.1%. Isso é
uma consequência natural do comportamento tipo "passeio aleatório
multiplicativo" já estabelecido em H-001/H-010/H-011/H-017 — se log₁₀(valor)
"equidistribui" (mod 1) ao longo da órbita, o primeiro dígito segue Benford
automaticamente (teoria clássica de equidistribuição).

## Cuidado metodológico

Agregar valores de MÚLTIPLAS órbitas (todos os n de 1 a N, todos os valores
visitados) cai na armadilha de colisão de órbitas já documentada em
`protocols/new-experiment.md` — órbitas se fundem, contando o mesmo trecho
várias vezes. Testamos de duas formas limpas:
1. **Uma única órbita longa** (sem problema de colisão, é uma trajetória só)
   — verificar Benford nos valores internos.
2. **Muitas órbitas independentes, um valor por órbita** (amostra grande de
   n distintos e distantes, pegando um "retrato" de cada — sem colisão por
   construção, como em E-001).

## Como testar

(1) Pegar um recordista de órbita longa (ex: 837799), computar toda a
trajetória padrão, tabular o primeiro dígito de cada valor, comparar com
Benford. (2) Amostrar n grandes aleatórios distintos, pegar o valor da
órbita após um número fixo de passos (ou o pico), tabular primeiro dígito.

## Atualizações

- 2026-07-13: hipótese aberta e testada em `experiments/E-023-benfords-law/`.
  Órbita única (837799): qui-quadrado=7.49, p=0.486 (consistente com
  Benford). Achei e corrigi um viés metodológico real na parte de múltiplas
  órbitas (amostras que já haviam atingido n=1 inflavam artificialmente o
  dígito 1 — 2.61% das 500k amostras originais). Após correção: ajuste
  excelente (dígito 1: 30.11% vs 30.10% previsto). Confirma Benford como
  consequência natural do passeio aleatório multiplicativo já estabelecido
  (H-001/H-010/H-011/H-017).
