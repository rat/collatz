# H-061 — Revisão do paper #029 (Alic, "Collatz Progressions Reframed") — paper de algoritmos peer-reviewed, álgebra P2ER confirmada correta

Status: revisão externa concluída — álgebra central verificada correta;
paper não faz alegação matemática sobre a conjectura
Criada em: 2026-07-15
Origem: item 029 da coleção (`literature/papers/INDEX.md`), já baixado
(`029_Collatz-Progressions-Reframed.pdf`).

## O paper

Alic, N. (2026), *Collatz Progressions Reframed: Exponent
Representation, Algorithmic Hierarchies, and Record Computations*,
IEEE Access, vol. 14, **peer-reviewed** (recebido, aceito, publicado
com DOI). Autor: Diretor do Photonics Laboratory, Qualcomm Institute,
UCSD — PhD em fotônica, membro IEEE, sem relação prévia aparente com
teoria dos números, mas credenciais acadêmicas reais e verificáveis.

**Diferente de todos os papers revisados até aqui nesta coleção**: não
faz nenhuma alegação matemática sobre a conjectura (o texto é explícito
— *"The Collatz conjecture remains unproven"*, na conclusão). É um
paper de **engenharia/algoritmos**: propõe representar inteiros como
vetores de expoentes de potências de 2 (P2ER — Power-of-2 Exponent
Representation: `n = Σ2^{k_i}`, `k` estritamente decrescente —
literalmente as posições dos bits 1 na representação binária de `n`),
mostra que a etapa ímpar (`3n+1`) vira uma operação algébrica simples
sobre o vetor de expoentes (concatenação de multiset + consolidação via
carry binário), e que a etapa par (`/2`) fica "grátis" (desloca todos
os expoentes de uma vez, sem iterar bit a bit). Compara 5 algoritmos
construídos sobre essa representação (PASA, REN, UPX, ACCEL,
POW2BASIC) e reivindica um recorde computacional: a progressão de
Collatz mais longa já computada, a partir de `2^{1.024.001}-1`
(13,8 milhões de passos, 7,3–9,44h).

## Escopo desta revisão

Como não há teorema matemático sobre Collatz para verificar (o único
"teorema" é sobre a álgebra da representação, não sobre a conjectura),
o que importa verificar é: **a álgebra central (Eq. 2/3 do paper)
realmente reproduz o mapa de Collatz de verdade?** Se estiver certa,
os benchmarks de performance comparam implementações corretas; se
estiver errada, tudo mais no paper mede outra coisa.

## O que foi verificado

`experiments/E-061-alic-p2er-check/experiment.py`, quatro partes:

1. **Álgebra do passo ímpar** (Eq. 2/3: `k_novo = consolidate([k+1 |
   k | k(end)])`) contra `3n+1` direto — 20.000 passos ímpares via 500
   trajetórias aleatórias (`n` de até 4000 bits). 0 falhas.
2. **Álgebra do passo par** (deslocamento em bloco por `min(k)`) contra
   divisão repetida por 2 direta — 500 casos. 0 falhas.
3. **Exemplo numérico do próprio paper** (Figura 1, `n=15`): `k=[3,2,1,0]`
   → passo ímpar → `[5,3,2,1]=46` → passo par → `[4,2,1,0]=23` — reproduzido
   exatamente. Sequência decimal completa (`15→46→23→...→1`, 17 passos,
   5 "UP") também reproduzida exatamente.
4. **Exemplos de "waiting line" e "end-gap"** (pág. 5): `k=[8,5,3,2,1,0]`
   (waiting-line de comprimento 3, `Δ=[1,1,1]` no final) e
   `k=[15,8,4,0]` (end-gap de tamanho 4) — ambos conferem.

## Resultado

**Álgebra central confirmada correta em todos os testes.** A
representação P2ER (vetor de expoentes de potências de 2, com o passo
ímpar como concatenação+consolidação e o passo par como deslocamento em
bloco) reproduz exatamente o mapa de Collatz padrão — dá confiança de
que os benchmarks de performance comparados no paper (PASA/REN/UPX/
ACCEL/POW2BASIC) estão de fato medindo implementações corretas do mapa,
não um mapa diferente por erro de representação.

**Não verificado (fora de escopo, computacionalmente inviável nesta
sessão)**: a "computação recorde" em si (`2^{1.024.001}-1`, 13,8
milhões de passos) — o próprio paper levou horas numa máquina dedicada
(56 núcleos, 512GB RAM) para essa única computação; não reproduzida,
tratada como não verificada, não como confirmada. Dado que a álgebra
subjacente foi verificada correta em escala menor, não há razão
específica para suspeitar do resultado, mas também não foi checado
diretamente.

## Por que isso é diferente dos outros papers da coleção

Não há "erro real" nem "conjectura vs. proposição" para avaliar aqui —
é puramente uma questão de "a implementação/representação está
correta?", que se confirma que sim. O paper é honesto sobre a natureza
de sua contribuição (recorde de computação e framework de benchmarking,
não avanço matemático) e não faz alegações que extrapolem isso.

## Novas hipóteses?

Nenhuma concreta para este projeto (foco em resultados matemáticos
sobre Collatz, não em otimização de algoritmos de verificação
computacional) — mas nota para referência futura: se este projeto algum
dia precisar de verificação computacional em escala muito maior que a
atual, a representação P2ER (e o código-fonte, disponível mediante
solicitação ao autor) seria um ponto de partida razoável.

## Atualizações

- 2026-07-15: paper lido por completo, álgebra central verificada
  computacionalmente em 4 frentes (incluindo reprodução exata de todos
  os exemplos numéricos do próprio paper). `INDEX.md` atualizado (item
  029: Lido=Sim, Corrigido=Sim [nada a corrigir], Implementado=Sim).
