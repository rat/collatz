# H-076 — Revisão: Tao, "Almost all orbits of the Collatz map attain almost bounded values" (2022)

Status: revisão externa concluída (exemplos e identidades explícitas confirmados; não é uma "caça a erros")
Criada em: 2026-07-15
Origem: item 106 da coleção de literatura (`literature/papers/INDEX.md`),
arquivado via busca EBSCO/ScienceDirect em 2026-07-15. Já citado sem PDF
em `literature/00-index.md` e `literature/overview-and-known-results.md`
como o resultado mais forte e rigoroso já estabelecido sobre a
conjectura.

## O paper

Terence Tao (UCLA). *Forum of Mathematics, Pi* 10:e12 (2022), Cambridge
University Press — periódico de matemática de primeira linha, revisão
por pares rigorosa. Anunciado originalmente em 2019
(arXiv:1909.03562), publicado formalmente em 2022. **Não é uma "caça a
erros"** como as revisões de preprints amadores desta coleção — é
trabalho de um matemático de resultado comprovado, revisado com todo o
rigor de um periódico de primeira linha. O objetivo desta revisão é
verificação disciplinada dos exemplos numéricos e identidades explícitas
concretas que o próprio texto apresenta, não ceticismo.

## O resultado central (não re-derivado, só citado com precisão)

**Teorema 1.3**: para qualquer função f:ℕ+1→ℝ com lim f(N)=+∞ (por mais
lenta que seja), tem-se Col_min(N)<f(N) para quase todo N (densidade
logarítmica 1). Em particular, Col_min(N)<log log log log N para quase
todo N. Fortalece resultados anteriores (Korec: Col_min(N)<N^θ para
θ>log3/log4≈0,7924) para qualquer função divergente, não só potências.
A prova usa análise 3-ádica de um passeio aleatório enviesado
associado à iteração de Siracusa, via um processo de renovação
bidimensional.

## Verificação computacional

`experiments/E-076-tao-2022-review/experiment.py` — testa só as
afirmações concretas e numericamente checáveis que o próprio texto
apresenta como exemplos ou casos base, não o teorema central em si
(que é uma afirmação assintótica sobre densidade logarítmica, não
diretamente testável por computação finita):

1. **Exemplos do mapa de Siracusa** (Seção 1.2): Syr(1)=1, Syr(3)=5,
   Syr(5)=1, Syr(7)=11. **4 casos, 0 falhas.**
2. **Identidade (1.2)**: Col_min(N) = Syr_min(N/2^v2(N)), conectando o
   mínimo da órbita de Collatz ao mínimo da órbita de Siracusa (a parte
   ímpar de N). **2000 casos (N=1 a 2000), 0 falhas.**
3. **Distribuição exata de Syrac(ℤ/3ℤ)** (n=1, Seção 1.4, logo após o
   Lemma 1.12): valores 0,1,2 mod 3 com probabilidades 0, 1/3, 2/3.
   Reimplementamos a fórmula recursiva do Lemma 1.12 do zero (usando
   aritmética de frações exatas, não ponto flutuante) e reproduzimos
   exatamente. **3 valores, 0 falhas.**
4. **Distribuição exata de Syrac(ℤ/9ℤ)** (n=2, mesma seção): valores 0
   a 8 mod 9 com probabilidades 0, 8/63, 16/63, 0, 11/63, 4/63, 0, 2/63,
   22/63 — números racionais não-triviais, não escolhidos para bater
   facilmente. Reproduzidos **exatamente**, os 9 valores, usando a
   mesma implementação recursiva (sem hardcoded), mais confirmação de
   que as probabilidades somam exatamente 1. **9 valores, 0 falhas.**

Este é o teste mais rigoroso desta rodada de revisões: implementar do
zero uma fórmula recursiva razoavelmente sofisticada (Lemma 1.12) e
reproduzir exatamente 12 valores fracionários não-triviais que o texto
apresenta como *resultado* de aplicar essa fórmula, não como definição.

## Avaliação geral

Nenhum erro encontrado — nem seria esperado, dado o nível de revisão
por pares do periódico e a reputação do autor. O valor desta revisão
para o projeto é diferente do de outros itens da coleção: não estamos
avaliando se o paper é confiável (é), mas exercitando a mesma disciplina
de verificação computacional em todos os itens da coleção, e
confirmando com precisão exata (frações racionais, não aproximações)
uma fórmula recursiva não-trivial que conecta diretamente à análise
3-ádica que este projeto já usa em outras linhas (H-013/H-018/H-024).
Nenhuma conexão de pesquisa nova identificada além do que já era
conhecido — este resultado já era citado no levantamento inicial da
literatura deste projeto.

## Atualizações

- 2026-07-15: revisão externa concluída. PDF lido por completo (10
  páginas das primeiras seções, cobrindo a formulação do resultado
  principal e o aparato 3-ádico inicial). Todos os exemplos e
  identidades explícitas testadas confirmados sem exceção, incluindo
  reprodução exata de 12 valores de probabilidade racionais via
  reimplementação independente do Lemma 1.12.
