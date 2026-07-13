# H-035 — A obstrução de H-024 NÃO se aplica à Conjectura 10.4 de Pratiher (objetos categoricamente diferentes)

Status: refutada (checagem negativa, mas esclarece o alcance exato de H-024)
Criada em: 2026-07-13
Origem: pergunta natural depois de H-024 — Pratiher (2026) tem uma
constante empírica não-resolvida (α≈0,9762, fração de órbitas cuja forma
recorrente dominante é 'a') que também "cheira" a precisão 3-ádica.
Será que H-024 (densidade do subárvore reverso exige precisão 3-ádica
ilimitada) resolve ou informa a Conjectura 10.4 dele (fórmula fechada
para α)?

## Enunciado testado

H-024 mostra que D(v) — a densidade do subárvore reverso enraizado num
nó ESPECÍFICO v — não é função de nenhum resíduo finito de v. Pergunta:
isso se transfere para Freq_a(N) de Pratiher, a fração assintótica de
TODOS os n≤N cuja órbita atinge uma potência de 2 na "forma recorrente"
a (uma de 6 classes mod 9)? Se sim, H-024 explicaria por que a
Conjectura 10.4 dele resiste a fórmula fechada — um resultado interno
nosso ajudando a resolver o problema em aberto de outro paper.

## Por que a resposta é não (checagem categorial)

Reli a definição exata de Pratiher (`literature/resources-and-tools.md`,
seção Pratiher): Freq_r(N) = |{n≤N : n∈N_r}| / N, onde N_r é o conjunto
de inteiros cuja órbita eventualmente atinge uma potência de 2 cuja
"forma" (resíduo mod9, um de 6 valores possíveis já que potências de 2
mod9 ciclam com período 6: 2,4,8,7,5,1,...) é r. Isto é uma **média de
conjunto**: para cada N, particiona-se o conjunto FIXO {1,...,N} (que
cresce) em 6 classes, e mede-se a fração em cada uma.

D(v), em contraste, é a densidade da subárvore reversa enraizada num
**único nó fixo v** — quantos inteiros até um orçamento fluem
especificamente para aquele v via divisões reversas.

A ligação exata com H-013 confirma que esses dois tipos de objeto não
são intercambiáveis: releitura de H-013/H-018 mostra que p_t (fração de
órbitas terminando em J_t) É literalmente D(J_t) — a mesma quantidade de
H-024, avaliada num nó específico da família {J_t}. H-013 herda a
obstrução de H-024 porque **é** o mesmo objeto matemático (per-nó).
Freq_a(N) de Pratiher não tem essa forma: é a fração de {1,...,N} (um
conjunto que cresce, com N elementos DIFERENTES) que cai em cada uma de
6 classes — matematicamente mais parecido com "qual fração da
população tem o traço X" do que com "qual a densidade da subárvore
enraizada neste nó único". Médias de conjunto sobre populações inteiras
costumam ter comportamento assintótico estável e computável mesmo
quando o objeto por-nó subjacente é arbitrariamente irregular (é o
fenômeno padrão de lei-dos-grandes-números/equidistribuição suavizando
idiossincrasias individuais) — não há nenhuma razão a priori para herdar
a obstrução de precisão ilimitada de H-024.

## Conclusão

**H-024 não resolve nem informa diretamente a Conjectura 10.4 de
Pratiher.** São obstruções de tipos diferentes (se é que a de Pratiher é
sequer uma obstrução real — pode muito bem ter fórmula fechada via
ferramentas de equidistribuição 2-ádica/3-ádica clássicas, um território
que não exploramos). Reportar o contrário seria exatamente o tipo de
"conexão por aparência" que este projeto já rejeitou antes (ver H-032,
frações contínuas vs H-013 — mesma disciplina aplicada aqui).

**Valor da checagem, apesar do resultado negativo**: esclarece com
precisão o alcance de H-024 — a obstrução é sobre **densidades
por-nó** (subárvore de um v específico), não sobre **médias de
conjunto** (fração de uma população crescente). Essa distinção evita um
erro de categoria futuro e ajuda a decidir rapidamente, para qualquer
nova constante "estranha" que apareça na literatura, se H-024
potencialmente se aplica (pergunta: é uma quantidade por-nó ou uma média
de conjunto?).

## Atualizações

- 2026-07-13: checagem feita e documentada. Resultado negativo esperado
  (a distinção categorial já era visível ao reler as definições com
  cuidado), mas vale o registro para não reabrir essa confusão depois.
- 2026-07-13: **ressalva importante (H-037)** — a distinção "D(v) é
  por-nó, Freq_r(N) é média de conjunto" acima é menos limpa do que
  parece. H-037 mostrou que α de Pratiher é, na verdade, `Σ_{t≡2 mod3}
  D(J_t)` — uma soma infinita dos MESMOS objetos por-nó que H-024
  obstrui, não um tipo de objeto genuinamente diferente. A razão pela
  qual ainda pode ser mais tratável que um D(v) genérico não é
  "equidistribuição lava a irregularidade" (o que eu disse acima), mas
  algo mais específico: a soma é dominada por poucos termos pequenos
  (p_2=D(5) sozinho é 93,77% do total), não por ser uma média sobre
  infinitos nós arbitrários. Não invalida a conclusão principal (H-024
  não resolve Pratiher diretamente), mas troca o motivo — ver H-037 para
  os detalhes.
