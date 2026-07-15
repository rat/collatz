# H-077 — Revisão: Clay, "The Long Search for Collatz Counterexamples" (2023)

Status: revisão externa concluída (afirmações numéricas concretas confirmadas; paper expositivo, sem alegação de prova)
Criada em: 2026-07-15
Origem: item 107 da coleção de literatura (`literature/papers/INDEX.md`),
arquivado via busca EBSCO/ScienceDirect em 2026-07-15.

## O paper

Oliver Keatinge Clay (Universidad del Rosario, Bogotá — formação em
física teórica e genética humana). *Journal of Humanistic Mathematics*
13(2), 2023 — periódico voltado a exposição acessível de matemática,
não um veículo de pesquisa técnica primária. **Não alega prova nem
refutação** — é um ensaio expositivo sobre a "estratégia de exclusão de
classes residuais mod 2^k" (território já bem coberto por este projeto:
H-005, H-007, H-014, H-015), situando-a no contexto histórico (Terras
1976/1979, Crandall 1978, Lagarias) e à luz do resultado de Tao (2022).

## Verificação computacional

`experiments/E-077-clay-2023-review/experiment.py`:

1. **Três fórmulas algébricas explícitas** (notas de rodapé, Seção 3),
   dando o "stopping length" (número de termos da sequência, incluindo
   início e fim) para três classes residuais:
   - 2k (par) → sequência de 2 termos [2k, k].
   - 4k+1 (≡1 mod4) → sequência de 4 termos [4k+1, 12k+4, 6k+2, 3k+1].
   - 16k+3 (≡3 mod16) → sequência de 7 termos até 9k+2.

   Todas as três confirmadas **identicamente para k=1 a 199** (a
   igualdade é algébrica/simbólica, então testar 199 valores concretos
   de k é uma confirmação forte, embora não uma prova formal). **0
   falhas em todas.**
2. **Classes "domadas" da Figura 2** (livres de contraexemplo até
   mod 128): 0 mod2, 1 mod4, 3 e 11 mod16, 23 mod32, 7/15/59 mod128 —
   confirmado que instâncias dessas classes sempre "mergulham" abaixo
   do valor inicial. **158 casos, 0 falhas.**
3. **Alegação "7,4% restante"** (Seção 3, parágrafo final): após
   excluir as classes citadas, resta uma fração "não domada" de 7,4%
   dos inteiros. Confirmado exatamente: partindo de 3/16 (fração
   restante após excluir 0 mod2, 1 mod4, 3 mod16 — valor que o próprio
   texto também cita explicitamente), subtraindo as exclusões
   adicionais da nota de rodapé 4 (11 e 23 mod32; 7, 15, 59 mod128;
   39, 79, 95, 123, 175, 199, 219 mod256), obtém-se exatamente
   **19/256 ≈ 7,42%** — bate com o "7,4%" citado.

## Nota de metodologia própria (erro real, corrigido antes de reportar)

Minha primeira tentativa de verificar a alegação dos 7,4% deu **4,30%**,
não 7,4% — um desvio que pareceria um erro do paper. Investigando:
confundi as classes "3 mod16 e 11 mod16" (que aparecem juntas na Figura
2, como o par de sub-classes resultante de refinar "3 mod16" antes da
etapa seguinte) com "11 mod32" (a classe que a nota de rodapé 4
realmente lista, um refinamento posterior e distinto, aplicado
*depois* de já se ter chegado a 3/16 restante). Ao reler a nota de
rodapé 4 com mais cuidado — que lista explicitamente "11 and 23 mod 32"
(não mod16) — e recalcular a partir da fração 3/16 já confirmada no
texto principal, o resultado bateu exatamente com "7,4%". O erro era
meu (confusão entre dois estágios diferentes do refinamento
apresentados em partes diferentes do texto), não do paper.

## Avaliação geral

Paper expositivo correto em todas as afirmações numéricas concretas
verificáveis. Não introduz técnica ou resultado novo sobre a
conjectura — é uma síntese histórica e pedagógica da estratégia de
exclusão por classes residuais (já explorada por Terras 1976, Dunn
1973, e por este próprio projeto em H-005/H-007/H-014/H-015) e uma
discussão contextual sobre o resultado de Tao. Menciona explicitamente
(Seção 7) o ângulo p-ádico como possível caminho futuro, citando um
lema de projeção de sistemas de Serre — não desenvolvido
tecnicamente, apenas apontado como direção. Nenhuma conexão de pesquisa
nova para este projeto identificada além da própria confirmação de que
o padrão de exclusão residual (já sabido pelo projeto como
"substancialmente esgotado como fonte de resultado novo", ver
`STATE.md`) é território bem estabelecido na literatura de divulgação
também.

## Atualizações

- 2026-07-15: revisão externa concluída. PDF lido por completo (15
  páginas, Seções 1-7). Três fórmulas algébricas e a alegação dos 7,4%
  confirmadas exatamente, após corrigir um erro próprio de
  interpretação (confundir classes mod16 com mod32 de estágios
  diferentes do refinamento).
