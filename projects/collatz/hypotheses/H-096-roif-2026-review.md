# H-096 — Revisão: Roif (2026), "On the Convergence of the Collatz Function" — ALEGAÇÃO DE PROVA REFUTADA

Status: alegação de prova refutada (erro fatal e trivial, contraexemplo
elementar)
Criada em: 2026-07-16
Origem: item 050 do catálogo, baixado manualmente pelo diretor
científico (bloqueado, academia.edu). "V4 — April 2026", 8 páginas, não
peer-reviewed, título completo "...A Structural Proof via Galois
Fields, Topological Duality, and Lyapunov Wave Analysis".

## O que o paper alega

Prova completa em 9 estágios: exclusão de ciclos extras via uma
identidade 2-ádica (Seção 6, mesma família algébrica já vista em
H-092/H-093 nesta rodada e em trabalho próprio deste projeto), uma
"função de Lyapunov de onda" V~ que decresce a cada ciclo de retorno
(Seção 5), e o Teorema de Tao (2022) cobrindo "quase todo" n₀ (Seção
8). A Seção 9 ("Closing the Gap") tenta fechar o conjunto excepcional
de Tao (densidade zero, mas não necessariamente vazio ou finito) via
um argumento chamado "empty container".

## O gap fatal (Seção 9)

O paper constrói um espaço topológico de 3 pontos S={0,2,1} onde
reinterpreta o número 2 como um "container vazio" {} e prova (Lemma
4.3): **se A⊆ℤ⁺ tem densidade assintótica zero, então A=∅**. Essa
afirmação é matematicamente falsa como fato geral — é um erro
elementar, do tipo encontrado em cursos introdutórios de teoria dos
números. A confusão: densidade zero (d̄(A)=0) não implica conjunto
finito, muito menos vazio — só implica que a "fração" do conjunto
dentro de [1,N] tende a zero conforme N cresce, o que é compatível com
A ser infinito.

**Contraexemplo trivial**: o conjunto dos quadrados perfeitos
{1,4,9,16,25,...} tem densidade zero (√N/N → 0) mas é obviamente
infinito e não-vazio. O mesmo vale para as potências de 2. Isso por si
só refuta a "Lemma 4.3" tal como enunciada, e com ela todo o
"Teorema 9.1" (que conclui que o conjunto excepcional de Tao é vazio)
e a "Corolário 9.2" (que seria a conjectura de Collatz completa).

O próprio paper tenta antecipar essa objeção na Seção 9.3 ("Why This
Argument Is Not Circular"), mas a defesa não resolve o problema: a
identificação entre "densidade zero" e "contido em {}" (um ponto
abstrato de um espaço topológico de 3 elementos S, que não é sequer um
subconjunto de ℤ⁺) nunca é justificada como uma relação matemática
real — é puramente metafórica ("boundary present, content empty").
Não existe uma função ou imersão estabelecida de subconjuntos de ℤ⁺
no espaço S que tornaria "E ⊆ {}" uma afirmação com sentido
matemático, muito menos uma que implique E=∅.

## Verificação computacional

`experiments/E-096-roif-2026-review/experiment.py`: demonstra
numericamente que os quadrados perfeitos e as potências de 2 têm
densidade tendendo a zero (10⁻¹ em N=10² até 10⁻¹¹ em N=10¹² para
potências de 2) enquanto são claramente infinitos — refutação direta
e elementar de "Lemma 4.3".

## Avaliação

O restante do andaime matemático (Seções 3-8) contém identidades
algébricas plausíveis na mesma família já vista em outras revisões
desta coleção (fórmula exata de ciclo, cota 2-ádica b/a≥log₂3), mas
tudo isso é irrelevante frente ao erro fatal da Seção 9 — sem ela, o
paper reduz-se ao mesmo resultado já conhecido de Tao (2022, "quase
todo n₀"), sem fechar o conjunto excepcional. O histórico de versões
do próprio paper (V1→V4, cada uma "fechando um gap" da anterior)
sugere um padrão de tentativas sucessivas de remendar o mesmo buraco
lógico, terminando nesta versão com um erro ainda mais básico
(confundir densidade zero com vazio) do que as tentativas anteriores.

## Referências

- Experimento: `experiments/E-096-roif-2026-review/experiment.py`.
- Paper: `literature/papers/050_On-the-Convergence-of-the-Collatz-Function.pdf`.
