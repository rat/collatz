# H-028 — Consolidação da família de exclusões via CRT (mod 72)

Status: confirmada (consolidação de resultados já provados + validação
exaustiva contra 100% dos dados reais conhecidos)
Criada em: 2026-07-13
Origem: sugestão do advisor de que, entre os 27 resultados do projeto, o
que mais se aproxima de algo publicável não é nenhuma hipótese isolada,
mas a *família* de teoremas de exclusão (H-007, H-014, H-022, H-027)
consolidada numa única caracterização.

## Enunciado

Combinando via Teorema Chinês do Resto os quatro resultados provados de
exclusão de recordistas de stopping time:

- **H-007**: N ≡ 2 (mod 3) — exceto N=2.
- **H-027**: N ≡ 4 (mod 6) — corolário de H-007.
- **H-014**: N ≡ 5 (mod 8) — exclusão por empate.
- **H-008** (H-022+H-027): N ≡ 4 (mod 9).

produz uma caracterização única mod 72 = lcm(8,9) (que também é múltiplo
de 3 e 6): **45 dos 72 resíduos possíveis (62,5%) estão provadamente
excluídos** — nenhum número nessas classes residuais pode jamais ser um
recordista de stopping time, com exceção do caso-base N=2.

## Verificação

Script `E-028-crt-exclusion-family/experiment.py`: gera os 45 resíduos
excluídos mod 72 a partir das quatro regras, e testa contra os 148
recordistas reais conhecidos (OEIS A006877, mesmo dado usado em H-004/
E-004). **Zero violações** — todos os 148 caem nos 27 resíduos
permitidos (ou são o caso-base N=2). Dos 27 resíduos permitidos, 18 já
aparecem de fato na amostra de 148 recordistas conhecidos.

## Honestidade sobre o significado

Isto não é uma prova nova — é a **consolidação aritmética** de quatro
resultados já provados anteriormente (nenhuma matemática nova além do
CRT, que é elementar). O valor está em apresentar, numa única afirmação
curta e verificável, o que o projeto já demonstrou de forma espalhada em
quatro hipóteses separadas: mais de 60% do espaço de resíduos mod 72 é
provavelmente inacessível a recordistas de stopping time, e isso bate
exatamente com 100% dos dados reais conhecidos.

Isso **não aproxima uma prova da Conjectura de Collatz em si** — é uma
afirmação sobre a estrutura dos recordistas de *stopping time*, um objeto
derivado, não sobre a convergência de todas as órbitas. Mas é um pacote de
resultados limpo, completo, com prova e validado, do tipo que o advisor
apontou como o candidato mais realista a nota/paper curto deste projeto,
caso o diretor científico decida formalizar algo.

## Próximos passos naturais (não executados ainda)

- Incorporar H-015 (generalização sistemática mod 2^d, 2374 classes mod
  2^16) à consolidação — deixado de fora aqui por ser uma lista grande,
  não uma fórmula fechada como as quatro usadas.
- Investigar se os 9 resíduos "permitidos mas não ocupados" (27−18) têm
  alguma razão estrutural para não aparecerem ainda, ou se é só falta de
  amostra.

## Atualizações

- 2026-07-13: consolidado e validado. 45/72 resíduos excluídos com prova,
  zero violações contra os 148 recordistas reais conhecidos.
