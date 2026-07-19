# E-107 — A Definição 2 de H-127 (configuração diagonal) é vazia como está escrita

Hipótese relacionada: [`H-127-reducao-z-number-dicotomia-espectral-wcc.md`](../../hypotheses/H-127-reducao-z-number-dicotomia-espectral-wcc.md)

## Origem

Ao tentar avançar H-127 (fechar a Etapa 6 do Lema B: "upgrade de
configuração diagonal para segmento contínuo", marcada como "plausível
mas não escrita"), consultei o Fable. A resposta revelou um problema
anterior e mais sério que a lacuna declarada: a Definição 2
(configuração diagonal), como está escrita, **não distingue ξ
estruturado de ξ genérico** — é satisfeita por quase qualquer ξ,
incluindo ξ=1.

## O que testa

Definição 2 (H-127): ξ tem configuração diagonal (γ,δ,η) de
profundidade s se em ≥(1-η)s das escalas t=1..s existe algum expoente a
na janela [γt−t^(2/3), γt+t^(2/3)] com ‖ξ·2^a/3^t‖ < δ — **sem exigir
coerência entre os a_t escolhidos em escalas consecutivas**.

Este script mede, para ξ=1, ξ pequenos (5,7) e ξ aleatórios de ~200
bits: (a) a fração literal de escalas com "hit" (a definição como
escrita); (b) o maior "segmento contínuo encadeável" — um run de
escalas consecutivas com expoentes a_t monótonos e incrementos
limitados (B = ⌊log₂(1/2δ)⌋) — o objeto que de fato carregaria
conteúdo de rigidez (análogo à "heurística de abundância" já presente
em H-127).

## Resultado

Em δ=1/6 e δ=1/10: fração de hits **0,97-0,997 para TODOS os ξ
testados, incluindo ξ=1** — sem diferença entre ξ estruturado e
aleatório. Em contraste, o maior segmento encadeável fica em 5-9 para
todo ξ, consistente com Θ(log s) previsto para ξ genérico (log 300 ≈
5,7) — não maior para ξ=1 do que para ξ aleatório.

## Interpretação

A Definição 2, sem o upgrade da Etapa 6 (encadeamento), conclui algo
que vale para quase todo ξ — o Lema B, usando essa definição, não
exclui nada: uma "configuração diagonal" não é evidência de estrutura,
é o comportamento típico. O objeto com conteúdo real é o **segmento
encadeado de comprimento ≫ log ℓ** — e é exatamente esse upgrade que a
Etapa 6 precisa fornecer e que, por dois argumentos independentes (ver
H-127), não fecha com as ferramentas em jogo (produto de Riesz, Halász,
modelo de gaps tilted). Ver H-127 para a análise completa de por que as
duas rotas possíveis (estabilidade em j; encadeamento intra-j) falham.

## Arquivos

- `experiment_def2_vacuity.py` — script (gerado pelo Fable em consulta,
  documentado e promovido a experimento formal).
- `output.txt` — saída completa da execução.

## Reproduzir

```
python3 experiment_def2_vacuity.py    # segundos
```
