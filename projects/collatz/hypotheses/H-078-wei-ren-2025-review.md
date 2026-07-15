# H-078 — Revisão: Wei Ren, "Reduced Collatz dynamics is periodical..." (2025)

Status: revisão externa concluída (teorema central correto e verificado; condicional, não fecha a conjectura, honestamente reconhecido pelo autor)
Criada em: 2026-07-15
Origem: item 108 da coleção de literatura (`literature/papers/INDEX.md`),
arquivado via busca EBSCO/ScienceDirect em 2026-07-15.

## O paper

Wei Ren (China University of Geosciences, Wuhan). *Research in
Mathematics* 12(1), 2025 — Taylor & Francis, "Pure Mathematics",
revisado por pares. Trabalha com a dinâmica acelerada
T(x)=(3x+1)/2 (ímpar) ou x/2 (par) — o mesmo mapa acelerado já usado
por este projeto (H-001 etc.), aqui chamado "dinâmica reduzida".

## O resultado central

**Definição 2.6**: d_r(x) é a sequência de operações I ((3x+1)/2) e O
(x/2) desde x até o primeiro iterado estritamente menor que x
(equivalente ao "stopping time"/glide já usado neste projeto). **Teorema
3.22 (Period Theorem)**: se d_r(x) existe, então d_r(x+2^L) existe **e é
idêntica** a d_r(x), onde L=|d_r(x)| é o comprimento da sequência.
**Corollary 3.24**: estende para d_r(x+k·2^L)=d_r(x) para todo k≥1
inteiro.

**Apêndice — Form Corollary (Corollary 4.2)**: para qualquer sequência
válida s=d_r(x), CntO(s)=⌈log₂(1,5)·CntI(s)⌉ (contagem de operações O em
função da contagem de I), com desigualdade estrita para todo prefixo
próprio de s — uma caracterização necessária e suficiente da forma que
qualquer dinâmica reduzida válida deve ter.

## Verificação computacional

`experiments/E-078-wei-ren-2025-review/experiment.py`:

1. **Exemplos do próprio paper** (Remark 2.8): d_r(3)=IIOO, d_r(5)=IO,
   d_r(7)=IIIOIOO, d_r(9)=IO, d_r(11)=IIOIO. **5 casos, 0 falhas.**
2. **Period Theorem** (Teorema 3.22): testado exaustivamente para
   x=2 a 500. **499 casos, 0 falhas.**
3. **Corollary 3.24** (extensão a k·2^L): testado para x=2 a 50, k=1 a
   5. **245 casos, 0 falhas.**
4. **Form Corollary** (Corollary 4.2, apêndice): testada tanto a
   igualdade para a sequência completa quanto a desigualdade estrita
   para todo prefixo próprio, para x=2 a 2000. **999 casos, 0 falhas em
   ambas as partes.**

Nenhum erro encontrado em nenhum resultado verificável.

## Sobre o alcance real do teorema (não é uma prova da conjectura)

O próprio Teorema 3.22 é **condicional**: só afirma algo sobre x para os
quais d_r(x) *já existe* (ou seja, x cuja órbita eventualmente cai
abaixo do próprio valor inicial — precisamente o que já sabemos ser
verdade para todo x testado computacionalmente, mas não provado para
todo x). O teorema não diz nada sobre a possibilidade de existir algum
x para o qual d_r(x) nunca exista (órbita que nunca cai abaixo de si
mesma) — que é exatamente o conteúdo não resolvido da própria
Conjectura de Collatz.

**Isso é honestamente reconhecido pelo próprio autor** na Seção 4
(Conclusão): "what is left for future work is to verify that reduced
dynamics of partial integers exists (partial can be understood as
residue class basis)... If all residue classes can cover all positive
integers, then Reduced Collatz Conjecture will be true, and Collatz
conjecture will be true too." Ou seja, o autor está explícito que o
teorema **não fecha** a conjectura — resta exatamente o problema
original, apenas reformulado em termos de cobertura de classes residuais
por "dinâmicas reduzidas" existentes. Nenhuma alegação de prova
completa é feita; o título do paper é sobre a periodicidade da dinâmica
reduzida, não sobre a conjectura em si.

## Avaliação geral

Paper tecnicamente correto e honesto: prova rigorosamente um resultado
estrutural real (periodicidade condicional, com aplicação prática
potencial de reduzir a verificação computacional a classes de resíduos
em vez de inteiros individuais — semelhante em espírito, mas não
idêntico, à estratégia de exclusão residual já explorada por este
projeto em H-005/H-007/H-014/H-015), sem alegar ter resolvido a
conjectura. A "Reduced Collatz Conjecture" que o autor propõe como
equivalente (Definição 2.6/Teorema 2.7) permanece tão em aberto quanto
a original — o teorema do período é uma ferramenta computacional
potencialmente útil para organizar a verificação por classes residuais,
não um passo de prova rumo à conjectura completa.

## Atualizações

- 2026-07-15: revisão externa concluída. PDF lido por completo (10
  páginas incluindo apêndice). Teorema central, corolário de extensão e
  Form Corollary do apêndice confirmados sem exceção. Confirmado que o
  teorema é condicional e não fecha a conjectura, honestamente
  reconhecido pelo próprio autor na conclusão.
