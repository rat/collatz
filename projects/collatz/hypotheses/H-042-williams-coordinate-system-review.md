# H-042 — Revisão do paper #014 (Williams, "A Coordinate System for Collatz Dynamics") — sem erros matemáticos; dois erros de citação OEIS

Status: revisão externa concluída (estendida em 2026-07-15) — todos os
teoremas confirmados; dois erros de citação bibliográfica na Seção 5.2
(não afetam nenhuma prova)
Criada em: 2026-07-14; estendida em 2026-07-15
Origem: quarto paper priorizado da coleção (item 014, local,
arXiv:2607.01718). Reaberta por engano em 2026-07-15 dentro da tarefa
"revisar todos os papers já baixados até esgotar": ao escanear
rapidamente as ~100 linhas de `literature/papers/INDEX.md` para montar
a lista de itens baixados-mas-não-processados, o item 014 foi incluído
por erro de leitura — a linha já estava (e sempre esteve) marcada
Lido=Sim/Corrigido=Sim/Implementado=Sim desde 2026-07-14, sem nenhuma
inconsistência real no `INDEX.md`. Só percebido ao consultar
`BACKLOG.md` e achar H-042 já existente. Consolidado aqui em vez de
manter um H-058 duplicado (que chegou a ser criado e depois removido,
nunca commitado).

## O paper

"A Coordinate System for Collatz Dynamics" — Jennifer Williams,
School of Electronics and Computer Science, University of
Southampton, Reino Unido. Qualidade acadêmica claramente superior aos
itens anteriores: afiliação institucional real e verificável,
literatura extensa e genuína (Applegate-Lagarias, Barina — já
catalogado por nós —, Bateman-Horn, Blecksmith-McCallum-Selfridge,
Flatto, Guy, Kannan-Ganesa Moorthy, Knight 2026, Lagarias ×3, Mahler,
OEIS, Ren), código público no GitHub
(`github.com/rhoposit/collatz-coordinate-system`), e uma **declaração
explícita de uso de IA generativa** (Claude Opus 4.8, usado para
rascunhar/formatar, com verificação humana integral declarada) —
prática exemplar de transparência. O paper ainda agradece a um colega
(Ian Leary) por ter identificado um erro menor durante a revisão,
mostrando que passou por escrutínio real antes da publicação.

## O que foi verificado (ambos confirmados corretos)

- **Teorema 3.6** (dinâmica diagonal): para n=λ·2^a·3^b−1 com a≥2, o
  próximo ímpar na trajetória de Collatz é λ·2^(a−1)·3^(b+1)−1 —
  confirmado em 20.000 casos aleatórios
  (`experiments/E-042-williams-coordinate-system-check/`).
- **Teorema 4.1** (Zero-Prime Rows): linhas k≡2 mod4 com k≥6 do
  "esqueleto principal" L₁ (números da forma 2^a·3^b−1) não contêm
  primos — confirmado exaustivamente para 14 linhas (k=6 a 58, até 58
  elementos por linha). A exceção k=2 (contém os primos 3 e 5,
  explicitamente notada pelo próprio paper) foi confirmada. Controles
  (linhas fora desse padrão) contêm primos, como esperado.

**Nenhum erro encontrado.** Diferente dos itens 001 (H-039) e 004
(H-040), este paper passou em todas as verificações que fizemos.

## Extensão (2026-07-15) — mais 6 partes verificadas, dois erros de citação OEIS

Ao retomar este item (achando, por engano, que ainda não tinha sido
revisto), verificamos computacionalmente tudo que H-042 original **não**
cobria: Teorema 2.13 (partição bijetora `Z≥0`→crown triangles, n=0..200.000,
0 falhas), Proposição 3.10 (transição de fronteira `a=1`, 81 casos, 0
falhas), Teorema 4.2 (contagem exata de posições "prime-admissible",
k=2..300, 0 discrepâncias), Proposição 6.2 (fórmula assintótica de
contagem de cadeias — ver "erro próprio" abaixo), Observação 6.3
(linhas "acidentalmente" sem primos — listas exatas reproduzidas sem
diferença), e as referências cruzadas da Seção 5.2 (OEIS).

**Dois erros de citação OEIS encontrados** (conferidos via `curl` direto
em oeis.org, não de memória):
1. **A017557 citado para "crowns ≡ 8 (mod 12)" está errado.** `A017557`
   é `12n+3` (≡3 mod 12), não ≡8 mod 12. A sequência correta é
   **A017617** (`12n+8`). As outras três citações da mesma tabela
   (A007494, A016777, A008594) conferem exatamente.
2. **"Primos em `L_1` = A005105" é impreciso por um elemento.** A005105
   (`2^i·3^j-1`, `i,j≥0`) inclui o primo 2 (via `i=0,j=1`), mas `L_1`
   exige `a≥1` e nunca alcança 2. Correto seria "A005105 sem o elemento 2".

Nenhum dos dois afeta qualquer prova do corpo do texto — ambos isolados
na tabela expositiva da Seção 5.2.

### Erro próprio encontrado e corrigido (via `advisor()`) — não é erro do paper

Uma primeira tentativa de verificar a Proposição 6.2 concluiu
(incorretamente) que havia um erro de fator 2, usando `T_c(k,0)` como
"elemento mínimo da linha k". **Isso era um bug na verificação, não no
paper**: `T_c(k,0)` é o elemento na posição PAR `j=0` (multiplicador de
paridade `g=2`, Definição 2.7) — não o mínimo da linha. O mínimo real
está em `j=1` (posição ímpar, `g=1`), `T_c(k,1)=λ·2^k-1`, exatamente a
fórmula que a demonstração do paper usa. Confirmado diretamente contra
o Exemplo 2.9 do próprio paper: linha k=2 de `L_1` é `[6,3,10,5,16]` —
mínimo real **3** (em j=1), não 6 (em j=0). `advisor()` apontou a
inconsistência antes de essa conclusão errada entrar neste arquivo.

**Lição registrada**: a essa altura da sessão já tinham sido
encontrados 3 erros reais em papers diferentes (H-053, H-056), e o
padrão "prova contradiz [o que parece ser] um lema já provado no mesmo
texto" pareceu familiar demais — convidando a atribuir a discrepância
ao autor antes de checar a própria verificação contra o exemplo
numérico que o paper já fornecia. Ordem de suspeita correta ao
investigar uma discrepância: checar a própria verificação primeiro, os
exemplos numéricos do paper depois, só então considerar erro do autor.

## Conteúdo matemático (resumo)

O paper organiza os inteiros não-negativos via a fatoração 3-suave
única n+1 = λ·2^a·3^b (gcd(λ,6)=1), definindo "triângulos coroa" cujas
linhas são cadeias de Collatz de paridade alternada. Dentro de cada
"esqueleto" (conjunto de elementos ímpares com λ fixo), a dinâmica de
Collatz é um fluxo diagonal determinístico (a,b)→(a−1,b+1) — sem
nenhum insumo teórico-numérico — até atingir a fronteira a=1, onde a
dificuldade aritmética real da conjectura se concentra (a escolha de
qual esqueleto seguinte é alcançada depende da fatoração de
λ·3^(b+1)−1). O resultado de aplicação concreta (Teorema 4.1) usa essa
organização para provar que uma classe residual específica é
algebricamente livre de primos, e o Teorema 4.2 caracteriza essa
classe como a única (mod 4) com essa propriedade.

## Seções honestamente marcadas como não-provadas

O próprio paper separa claramente "Computational Observations" (Seção
6 — observações verificadas computacionalmente mas não provadas, ex:
"linhas acidentalmente livres de primos") de resultados provados, e
lista explicitamente "Open Problems" (Seção 7): dinâmica de saída de
linha (sem forma fechada conhecida), por que p=3 é especial entre
mapas pn+1 genéricos, se toda trajetória alcança λ=1 ("λ-recorrência"),
conexão com o resultado de Tao, e conexão com vetores de paridade de
Knight (2026).

## Novas hipóteses?

Nenhuma testada concretamente ainda, mas esta é a primeira linha de
organização genuinamente **diferente** da família mod-8/Steiner-word
(itens 004/005) que vimos até agora — baseada em fatoração 3-suave
(λ,a,b) em vez de resíduos mod8. Vale reconsiderar em sessão futura se
essa organização por peso (a+b) oferece algo novo para nossa própria
família de exclusão (H-007/H-014/H-022/H-028), mas isso é especulativo
por enquanto, não uma hipótese concreta.

## Atualizações

- 2026-07-14: paper lido por completo, ambos os teoremas centrais
  confirmados corretos, sem erros encontrados. Flags atualizadas em
  `literature/papers/INDEX.md` (item 014: Lido=Sim, Corrigido=Sim
  [nada a corrigir], Implementado=Sim).
- 2026-07-15: item reaberto por engano (erro de leitura ao escanear
  `INDEX.md` rapidamente, não uma falha real de tracking — ver
  "Origem" acima). Aproveitado para estender de verdade: mais 6 partes
  verificadas (`experiments/E-042-williams-coordinate-system-check/experiment.py`),
  dois erros de citação OEIS encontrados e confirmados via fonte
  primária, um erro de verificação próprio (não do paper) encontrado e
  corrigido via `advisor()`. Flags de `INDEX.md` conferidas — já
  estavam corretas desde 2026-07-14, sem mudança necessária.
