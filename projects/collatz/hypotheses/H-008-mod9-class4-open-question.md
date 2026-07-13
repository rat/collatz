# H-008 — Classe 4 mod 9 nunca aparece em recordistas: tentativa de generalizar H-007

Status: inconclusiva (investigada, sem prova nem refutação — registrada como questão em aberto)
Criada em: 2026-07-13

## Contexto

H-004 mostrou que, entre os 148 recordistas oficiais, a classe residual 4 mod 9
(que é ≡1 mod 3, portanto **não** excluída pela prova de H-007) nunca ocorre
(0 de 148). H-007 provou uma exclusão limpa para ≡2 mod 3 via um M=(2N-1)/3
construído algebricamente. Esta hipótese tentou generalizar essa técnica para
explicar a ausência da classe 4 mod 9.

## O que foi tentado

Para uma amostra de N ≡ 4 (mod 9) até 300, busquei computacionalmente o menor
M < N com total_stopping_time(M) ≥ total_stopping_time(N) (o que provaria que
N não pode ser recordista, do mesmo jeito que em H-007). Resultado: **não há
relação algébrica curta e fixa entre M e N** — o M encontrado varia sem
padrão claro (razão M/N de 0.02 a 0.87 na amostra), e frequentemente é só um
recordista "genérico" já forte (como 27, que domina 13 dos 33 N testados só
por já ter stopping time alto) em vez de um M construído especificamente a
partir de N via uma fórmula curta como em H-007.

## Interpretação

Isso sugere que, se a exclusão da classe 4 mod 9 for de fato permanente (nunca
vai aparecer um recordista nessa classe, para nenhum N por maior que seja),
a prova precisaria de uma técnica mais sofisticada que a de H-007 — talvez
uma cadeia de mais de 2 passos, ou um argumento não-construtivo. Também é
possível que essa exclusão **não seja permanente** — apenas um fato empírico
válido até onde a sequência oficial foi calculada (~1.47×10^19), sem garantia
de continuar para sempre. Sem uma prova, não sabemos qual dos dois casos é
verdadeiro.

## Status

Deixado como questão em aberto — não encontrei prova nem contraexemplo.
Registrar para retomar se surgir uma ideia melhor, em vez de forçar uma
explicação sem sustentação.

## Atualizações

- 2026-07-13: investigado, sem conclusão. Marcado como aberto/inconclusivo.
