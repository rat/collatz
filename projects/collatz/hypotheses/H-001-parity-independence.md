# H-001 — Independência das valuações 2-ádicas na órbita acelerada

Status: refutada (na forma testada — ver experimento E-001)
Criada em: 2026-07-13

## Enunciado

O modelo heurístico padrão de passeio aleatório para Collatz (Kontorovich–Lagarias e
variantes) trata a sequência de valuações 2-ádicas a_1, a_2, a_3, ... ao longo de uma
órbita acelerada (T(n) = (3n+1)/2^{a}, a = maior potência de 2 que divide 3n+1) como
i.i.d., cada uma com distribuição geométrica P(a=k) = 2^-k. Propomos investigar se
essa suposição de **independência entre passos consecutivos** se sustenta
empiricamente, ou se existe correlação mensurável entre a_i e a_{i+1} — o que seria
esperado a priori, já que a aritmética de carry do 3n+1 acopla dígitos binários de
forma não trivial entre passos sucessivos.

Isso não é uma tentativa de provar a conjectura — é uma checagem empírica de uma
premissa usada por todos os modelos estocásticos da literatura (ver
`literature/approaches-stochastic-heuristic.md`).

## Motivação

- A distribuição marginal de cada a_i (geométrica 1/2) é fato estabelecido. O que os
  modelos assumem, mas raramente testam diretamente numa órbita real, é a
  **independência entre passos consecutivos**.
- Se houver correlação real, isso é candidato a explicar parte do "obstáculo
  estrutural" citado em `literature/overview-and-known-results.md` — o modelo i.i.d.
  simplesmente não capturaria uma dependência real presente na dinâmica
  determinística.

## Como testar

1. Gerar órbitas aceleradas para um conjunto grande de n ímpares iniciais.
2. Coletar a sequência de valuações (a_1, ..., a_k) de cada órbita até atingir 1.
3. Comparar a distribuição conjunta empírica de (a_i, a_{i+1}) com o produto das
   marginais (teste de independência / qui-quadrado) e computar a correlação de
   Pearson entre a_i e a_{i+1}.
4. Se a correlação for estatisticamente distinguível de zero e o qui-quadrado
   rejeitar independência, a hipótese é suportada (existe correlação real). Caso
   contrário, é refutada/inconclusiva para essa faixa.

Ver experimento associado em `experiments/E-001-parity-independence/`.

## Atualizações

- 2026-07-13: hipótese aberta.
- 2026-07-13: testada em `experiments/E-001-parity-independence/`. Primeira
  tentativa (agregando por posição em órbita) mostrou dependência aparente forte,
  mas foi identificada como artefato de colisão de órbitas (pseudo-replicação).
  Desenho corrigido (amostras independentes de n grandes e distintos, 300k e 1M
  observações, duas seeds) **não rejeitou independência** entre a_1 e a_2 — dados
  consistentes com o modelo i.i.d. padrão. Resultado é consistente com o teorema
  clássico de equidistribuição de Terras (1976)/Everett (1977). Hipótese refutada
  na forma simples testada; efeitos de dependência de longo alcance ficam como
  possível extensão futura, não prioridade imediata.
