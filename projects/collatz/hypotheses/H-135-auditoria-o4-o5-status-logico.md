# H-135: auditoria do status lógico de O4 e O5

Status: fechada-confirmada; problemas corrigidos no manuscrito

Criada: 2026-08-07

## Achados

1. O antigo Teorema `thm:regime3` afirmava que O4 era caso especial e
   ao menos tão difícil quanto três teorias abertas, sem apresentar uma
   redução formal. O conteúdo demonstrado é apenas a necessidade, dentro
   da rota de segundo momento, de decaimento exponencial uniforme dos
   somatórios condicionados. O item foi convertido em observação de
   contexto, sem alegação de equivalência.

2. O antigo Lema `lem:B` era seguido pela declaração de que seu último
   passo estava aberto. Ele não era um lema provado. Foi convertido em
   conjectura e o passo faltante foi isolado como estabilidade da mesma
   frequência quando a escala muda.

3. O déficit de Jensen prova que um orçamento annealed específico tem
   folga aproximada `1.88`. Ele não prova que toda técnica
   Littlewood-Offord ou todo argumento `l1` falha. A Proposição
   `thm:propC` e O5 foram restringidos ao cálculo realmente feito.

## Consequência

O4 e O5 continuam abertos. O manuscrito agora distingue o alvo de
Fourier, a conjectura condicional de estabilidade e o resultado exato de
Jensen. Nenhuma dessas três categorias é apresentada como prova das
outras.

Atualização H-149: a definição original de `SC(epsilon)` ainda continha
um erro de condutor. Modos grosseiros tornavam a condição automática,
mas a conclusão exigia frequência primitiva. O5 agora usa
`SC_prim(epsilon)`. Uma lei uniforme nos unitários com um ponto removido
prova que falha de suporte, sozinha, não força essa condição para
`epsilon<1`.
