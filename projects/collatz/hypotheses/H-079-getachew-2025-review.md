# H-079 — Revisão: Getachew, "Unfolding the Collatz Tree: An Indirect Structural Proof" (2025)

Status: revisão externa concluída — **ALEGAÇÃO DE PROVA COMPLETA REFUTADA** (furo lógico central identificado e confirmado computacionalmente)
Criada em: 2026-07-15
Origem: item 109 da coleção de literatura (`literature/papers/INDEX.md`),
arquivado via busca EBSCO/ScienceDirect em 2026-07-15.

## O paper

Eyob Solomon Getachew (Addis Ababa University). *Research in Mathematics*
12(1), 2025, Taylor & Francis — periódico de escopo genérico (não
especializado em matemática pura), revisado por pares. **Alega prova
completa** da Conjectura de Collatz. Já catalogado em
`literature/unverified-proof-claims.md` desde o levantamento inicial de
2026-07-13 (sem PDF na época); agora com PDF arquivado (item 109) e
revisado por completo.

Constrói a árvore reversa de Collatz g(n) — **exatamente a mesma
construção usada por este projeto em H-018/E-018**: todo nó v tem filho
2v sempre, e filho extra (v−1)/3 se v≡4 (mod 6). Alega provar três
propriedades (Teorema 9.1): (1) Cobertura — todo n∈ℕ aparece na árvore;
(2) Aciclicidade — o único ciclo é o trivial {1,2,4}; (3) Terminação —
todo caminho de volta (parent-chain) de qualquer nó até a raiz 1 é
finito. Conclui que (1)+(2)+(3) juntas provam a conjectura.

## O furo lógico central

**A relação "pai" definida no paper é literalmente idêntica ao próprio
mapa de Collatz direto**: parent(m)=m/2 se m par, 3m+1 se m ímpar
(Remark 1 do paper, fórmula explícita). Isso significa que **"o
caminho de volta de n até a raiz 1" É, por definição, a órbita direta de
Collatz de n**. Portanto, o "Lemma 4.3" (Terminação: todo caminho de
volta é finito) **não é uma consequência de "árvore acíclica + pai
único"** — ele é **literalmente equivalente** à própria Conjectura de
Collatz ("toda órbita direta atinge 1"), e a prova apresentada
(Lemma 4.3: "porque a árvore é acíclica e cada nó tem um único pai,
qualquer caminho de volta é uma cadeia simples que termina em 1 após
finitos passos") comete uma petição de princípio: aciclicidade e
unicidade de pai garantem que o caminho **não repete nós** e **não
bifurca**, mas nunca garantem que o caminho seja **finito** — uma cadeia
de pais únicos numa árvore acíclica infinita pode perfeitamente ser
infinita (é exatamente o que aconteceria se existisse um contraexemplo:
a órbita de um contra-exemplo n₀ nunca atinge 1, logo nunca "chega" à
raiz — n₀ simplesmente não pertenceria à componente conexa da raiz,
sem violar nem aciclicidade nem unicidade de pai da árvore como um
todo).

O **Teorema 5.1** (cobertura), que o paper trata como a peça central que
"prova" que todo n aparece na árvore, sofre do mesmo problema por um
caminho diferente: a fórmula de indexação a_{n,m}=(2n+1)·2^m, cuja soma
sobre um range apropriado de (n,m) é provada igual a N(N+1)/2 (Teorema
5.1), **é apenas a decomposição única de qualquer inteiro positivo em
parte ímpar × potência de 2** — um fato aritmético universal, válido
para *qualquer* N, que **não usa nem menciona a regra de ramificação
g(n) em nenhum lugar da prova**. Confirmamos isso diretamente
(`experiments/E-079-getachew-2025-review/experiment.py`): o "conjunto
indexado" pela fórmula do Teorema 5.1 é sempre exatamente {1,...,N} para
qualquer N, **mesmo que a árvore real (construída via g(n) a partir da
raiz 1) não tivesse ramificação nenhuma** — a identidade prova uma
tautologia aritmética, não a propriedade de que os nós são de fato
alcançáveis a partir da raiz pela construção recursiva real da árvore.

## Verificação computacional

`experiments/E-079-getachew-2025-review/experiment.py`:

1. **Teorema 5.1 em si**: confirmado correto — a soma da fórmula de
   indexação bate exatamente com N(N+1)/2 para N=5,10,15,20,100,1000.
   **6 casos, 0 falhas.** (O teorema está matematicamente correto; o
   problema é que ele não prova o que o paper alega que prova.)
2. **A fórmula de indexação é um fato aritmético genérico**: confirmado
   que o conjunto {a_{n,m} : a_{n,m}≤N} é sempre {1,...,N}, para
   N=1000, **sem qualquer referência à regra g(n)**.
3. **parent(x) = f(x) (mapa direto)**: confirmado algebricamente e
   verificado em 1000 casos aleatórios (x até 10⁶) — 0 discrepâncias.
4. **Construção real da árvore via BFS/DFS a partir da raiz 1** (usando
   a regra de ramificação verdadeira, não a fórmula de indexação):
   tentamos verificar se o número 27 (cuja órbita direta atinge 1 em
   111 passos, subindo até 9232 antes de descer — fato bem
   estabelecido) é de fato alcançável a partir da raiz 1 pela
   construção recursiva real. Confirmamos que:
   - O caminho reverso completo de 1 até 27 (a órbita direta de 27,
     invertida) **satisfaz corretamente a regra de ramificação** em
     todos os 111 passos — ou seja, 27 *é* alcançável em princípio.
   - Mas alcançá-lo por **busca direta a partir da raiz** (sem usar o
     atalho de já saber a órbita de 27) requer profundidade 112 e
     passa por um valor intermediário de 9232 — e mesmo com buscas de
     até 5 milhões de nós processados, uma implementação BFS ingênua
     não encontrou 27 dentro do orçamento computacional testado.
     Isso **não é uma falha da árvore em si** (sabemos por outra via
     que 27 está lá), mas ilustra concretamente por que a "cobertura"
     não pode ser estabelecida por um argumento puramente combinatório
     como o do Teorema 5.1: a árvore real cresce de forma tão
     desigual/lenta em certas direções (fenômeno já documentado por
     este projeto em H-018, "orçamento de bits") que **verificar
     cobertura por construção direta da árvore, para todo N, é
     computacionalmente equivalente a verificar Collatz diretamente**
     — não há atalho estrutural que o Teorema 5.1 forneça.

## Sobre a validação empírica do paper (Seções 5.1, 7.1, Tabelas 1-3)

O paper apresenta "validação empírica" (Algoritmo 2/3, Tabela 1/2) que
na verdade só executa a mesma fórmula de indexação tautológica (soma de
a_{n,m}) e a compara com N(N+1)/2 — não verifica em nenhum momento que
os nós foram gerados pela recursão real g(n) a partir da raiz 1. A
Tabela 3 (verificação de que caminhos de volta batem com sequências de
Collatz diretas, incluindo n até 10²¹) é a única verificação
genuinamente relacionada à árvore real — mas, como demonstrado acima,
essa verificação **é exatamente uma verificação computacional padrão de
Collatz** (calcular a órbita direta e conferir que ela é finita), não
uma consequência da estrutura de árvore. Ou seja, a Tabela 3 confirma
Collatz nos casos testados **da mesma forma que qualquer verificação
computacional direta já confirmaria** — não adiciona evidência
estrutural nova além do que já sabíamos (verificação computacional até
2^68-2^71, itens 105/110 desta mesma coleção).

## Avaliação geral

**Não é uma prova válida.** O erro é sutil e tem uma anatomia
específica: o paper reformula corretamente a árvore reversa de Collatz
(mesma construção de H-018), prova corretamente dois fatos verdadeiros
mas triviais em separado (a soma de uma decomposição aritmética
universal; que "parent" definido é acíclico e de pai único, o que é
trivialmente verdade para qualquer árvore genuína), e então monta esses
dois fatos triviais para "provar" uma conclusão que na verdade só é
verdadeira se a Conjectura de Collatz já for verdadeira — um caso claro
de petição de princípio disfarçada por reformulação em linguagem de
teoria dos grafos ("cobertura", "aciclicidade", "terminação"), que soa
mais forte do que "toda órbita de Collatz atinge 1" mas é logicamente
equivalente a isso, não uma via independente para prová-la.

## Atualizações

- 2026-07-15: revisão externa concluída. PDF lido por completo (17
  páginas). Identificado e confirmado computacionalmente o furo lógico
  central: (a) o Teorema 5.1 (cobertura) prova uma tautologia
  aritmética independente da regra de ramificação real; (b) o Lemma 4.3
  (terminação finita do caminho de volta) é logicamente equivalente à
  própria conjectura, não uma consequência de aciclicidade+pai único,
  porque a relação "parent" definida é idêntica ao mapa de Collatz
  direto. Adicionar entrada correspondente em
  `literature/unverified-proof-claims.md`.
