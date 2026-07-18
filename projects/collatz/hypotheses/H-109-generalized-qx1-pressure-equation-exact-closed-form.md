# H-109 — Generalização para qx+1: equação de pressão em forma fechada exata q^(α−1)=2^α−1; virada estrutural em q≥5; confirmado empiricamente em árvores reais de 5x+1 e 7x+1

Status: confirmado (teoria + verificação numérica independente +
confirmação empírica em árvores reais) — achado mais forte desta linha
de investigação até agora, com ressalva de calibração sobre novidade
Criada em: 2026-07-17
Origem: sugestão #1 da terceira rodada de consulta a uma IA externa
("generalizar para qx+1 como rota de publicação"), desenvolvida a
fundo pelo Fable a partir da derivação já validada em H-104.

## O que o Fable derivou (além do que a sugestão original pedia)

A sugestão original pedia para montar a matriz de pressão M_q(α) para
tipos mod q^k e resolver ρ(M_q(α))=1 numericamente para q=5. O Fable
foi além: mostrou que, na construção exata (todo filho vivo s e todo
a≥1 tem exatamente uma classe-mãe, para qualquer resíduo), **as somas
de coluna de M_q(α) são constantes** — logo a pressão tem **forma
fechada exata**, independente de k:

  ρ(M_q(α)) = q^(α−1) / (2^α − 1)

Isso explica RETROATIVAMENTE por que a "estabilidade em 4 níveis de
refinamento" relatada em H-104 não era convergência assintótica — era
uma **identidade exata** o tempo todo. A equação de pressão vira

  **q^(α−1) = 2^α − 1**

## Verificação independente (feita nesta sessão, não só repassada do Fable)

Resolvida por bisseção, confirmando os números do Fable:

| q | raiz trivial | segunda raiz | expoente de cauda (razão) |
|---|---|---|---|
| 3 | 1 | 2,000000 | 2,000 |
| 5 | 1 | 0,650919 | 1,536 |
| 7 | 1 | 0,373501 | 2,677 |
| 9 | 1 | 0,258108 | 3,874 |

α=1 é sempre raiz (conservação de massa). Para q=3, a segunda raiz é
2 exatamente — nosso α*=2 confirmado em H-104. **Para q≥5, a segunda
raiz cai ABAIXO de 1** (não acima) — uma virada estrutural completa.

## A virada estrutural em q≥5 (o insight mais importante)

O drift médio (log q − 2log2) é negativo só para q=3; para q≥5 é
positivo, ou seja, **as órbitas divergem em média**. Consequência: a
árvore reversa de qx+1 (q≥5) tem **densidade natural zero**
(N_v(x) ~ W_v·x^{α₁} com α₁<1, não ~x como em q=3). Isso significa que
"aplicar Hill em G(v) do mesmo jeito que q=3" não funciona para q≥5 —
os observáveis corretos mudam para: o **expoente de contagem α₁**
(tipo Krasikov–Lagarias) e a **cauda do "martingale" W_v** (o fator de
escala aleatório da contagem). O expoente de cauda unificado é sempre
a razão raiz-maior/raiz-menor (2/1=2 para q=3; 1/α₁ para q≥5).

## Confirmação empírica em árvores reais (feita pelo Fable, DFS igual à técnica de E-018)

- **q=5**: slopes de contagem por década (3 raízes testadas) ≈
  0,62–0,66, contra previsão teórica 0,650919.
- **q=7**: slopes ≈ 0,36–0,39, contra previsão teórica 0,373501.
- **Hill sobre W_v para q=5** (600 raízes, headroom 10⁶): top 2% dá
  1,547, contra previsão teórica 1,5363 — **CORREÇÃO (2026-07-17, ver
  H-113): esta concordância NÃO é confirmatória.** Com k≈12 pontos de
  cauda (topo de 2% de 600), o erro padrão do estimador de Hill é
  ξ_cauda/√k≈0,45 — a concordância de 2 casas decimais foi coincidência
  estatística, não evidência. Não citar este número como confirmação em
  nenhum texto futuro. O resultado válido e citável para a disputa
  Kontorovich-Lagarias vs. Volkov é H-113 (slope de contagem por
  década, n=300, com correção de Richardson: 0,639±IC[0,633,0,645],
  exclui Volkov/0,678 com folga).
- Últimas 1-2 décadas subestimam por artefato de truncamento conhecido
  (mesmo tipo de efeito de headroom já mapeado em H-090/H-091 para
  q=3) — quantificado e corrigido em H-113 (efeito de pré-assintótica
  de janela + viés de truncamento, ambos mensurados).

## Nova previsão falsificável para o teste EVT em andamento (H-108)

O parâmetro de forma de Fréchet generaliza para ξ = α₁/α₂ (a mesma
razão de raízes). Para q=3: ξ=1/2=0,5 — exatamente o que já testamos
em H-108 (obtivemos 0,4836 e 0,5575, ambos próximos de 0,5). Para
q=5, a previsão seria ξ=0,651 — um segundo teste independente possível
se a linha for retomada com q=5.

## Avaliação das outras 3 sugestões da mesma rodada (Fable, resumo)

- **#2 (Fronteira de Martin)**: descartada como direção. A
  "equivalência" alegada pela IA externa não é um teorema — reformula
  a conclusão desejada com vocabulário técnico. Identificar fronteiras
  de Martin só funciona para cadeias com estrutura forte (árvores
  homogêneas, grupos hiperbólicos) que nosso grafo não tem. Único
  conteúdo honesto: "fronteira=ℤ₃" é uma forma elegante de dizer "a
  σ-álgebra caudal é gerada pelos dígitos 3-ádicos" — exatamente o que
  os pares casados (H-100/H-101) já testam empiricamente. Nada novo.
- **#3 (Zeta da árvore + Tauberiano)**: matematicamente correta em
  princípio, mas o teorema Tauberiano consome exatamente a
  regularidade analítica que é o problema em aberto — estabelecer a
  continuação necessária de Φ_v(s) é tão difícil quanto provar a
  existência do limite diretamente. Útil só como linguagem para um
  eventual texto (a função de pressão q^(s−1)/(2^s−1) É a função
  espectral controladora), não como direção de pesquisa.
- **#4 (Furstenberg ×2×3)**: descartada, meu ceticismo confirmado. A
  conjectura de Furstenberg é sobre ação COMUTATIVA de ×2 e ×3; o
  mapa de Syracuse (com "+1" e divisão dependente de paridade) quebra
  comutatividade/estrutura de semigrupo no primeiro passo — não há
  nenhuma redução real em nenhuma direção. Era empréstimo de prestígio
  de um problema famoso, não uma conexão precisa. Valor residual: uma
  frase de calibração que H-091 já tinha concluído por conta própria.

## Checagem de novidade concluída (2026-07-17, ver H-112)

A checagem rigorosa (leitura completa, não busca por palavras-chave) foi
feita: Kontorovich-Lagarias (2009), Wirsching (1998), Applegate-Lagarias
(1995, dois papers) e Gonçalves-Greenfeld-Madrid (2022). Veredito
recalibrado (detalhes completos em **H-112**):

- **α₂=0,650919 (q=5) NÃO é novo** — Kontorovich-Lagarias já tinham essa
  quantidade exata (η5,BP, Teorema 8.10, via grandes desvios sobre um
  branching random walk, não nossa equação de pressão). O "≈0,68" da
  nota anterior está identificado: é η*5,BP≈0,678, previsão de um modelo
  ESTOCÁSTICO CONCORRENTE (Volkov), citada pelos próprios
  Kontorovich-Lagarias como uma disputa em aberto desde 2009. Nossos
  dados (enumeração real + Hill estimator) são evidência nova a favor
  da predição deles sobre a de Volkov.
- **A virada estrutural qualitativa em q≥5 também NÃO é nova** —
  Wirsching (1998, Cap. III) já previu isso heuristicamente ("presumably
  impossível para p≥5"), mesmo limiar exato, nunca provado. Confirmada
  independentemente por Gonçalves-Greenfeld-Madrid (2022, Teorema 1.3
  exclui q≥5 para p=2, via prova forward rigorosa).
- **O que sobrevive como novo**: a forma fechada exata
  ρ(M_q(α))=q^(α−1)/(2^α−1) válida para q arbitrário, com derivação
  rigorosa (ninguém unificou isso numa fórmula de família antes), e a
  confirmação quantitativa+empírica que fecha a lacuna entre a
  heurística de 1998 e um resultado verificável.

## Avaliação geral

Este resultado confirma α*=2 como caso particular de uma família mais
ampla e revela uma identidade exata (não só numericamente estável) — mas
a checagem de novidade mostrou que tanto o valor numérico quanto a
virada estrutural qualitativa já tinham precedente na literatura
(Kontorovich-Lagarias 2009, Wirsching 1998). A contribuição real e
defensável é a forma fechada de família e a confirmação rigorosa+
empírica — não a descoberta do fenômeno em si. Ver H-112 para a análise
completa e honesta desta recalibração.

## Addendum (2026-07-18) — correção real encontrada por revisão externa, mecanismo consertado

Uma revisão externa do paper apontou, com contraexemplo concreto e
correto, que o mecanismo descrito na §3 do paper ("operador de
transferência em resíduos mod q, somas de coluna constantes") está
**errado como enunciado**: o resíduo do filho mod q depende do pai mod
q² (não só mod q), verificado com q=3, a=2, u=1 vs u=7 (filhos caem em
resíduos diferentes mod 3). Generaliza para qualquer módulo finito —
nenhum automato de estado finito em resíduos mod q^k está bem definido
para uma única geração da recursão.

**O conserto (Fable + verificação independente minha, dupla, com
scripts próprios não copiados do Fable)**: existe uma identidade
correta, mas ela é sobre a **média** (pressão anelada) sobre todas as
raízes mod q^k, não sobre uma raiz fixa (quenched). Via um Lema de
bijeção de fibra (para a fixo, v↦(2^av-1)/q é bijeção entre a fibra
admissível mod q^j e Z/q^{j-1}Z), toda sequência (a_1,...,a_k) é
admissível para exatamente uma raiz mod q^k — dá a identidade EXATA
Σ_raízes Z_k(α;raiz) = (q^α/(2^α-1))^k. Verifiquei isso por força
bruta, independentemente do Fable, para q=3,5,7,9, k=1,2,3, várias α —
bate a menos de erro de truncamento.

**A ressalva séria**: existe uma transição de congelamento
quenched/anelado (teoria de polímeros dirigidos / REM de Derrida). Fato
estrutural (provado, não só numérico): a raiz MAIOR da equação está
**sempre** congelada, para todo q (P convexa com duas raízes ⟹
s(raiz menor)>0, s(raiz maior)<0, sempre). Para q≥5, forma fechada
exata: s(1)=log(4/q)<0 para q>4 — mesmo sinal do drift médio já
citado no paper, não coincidência. Verifiquei numericamente com DP
memoizada própria (não copiada do Fable): para q=3,α=2,u=1 (um
self-loop genuíno, w_2(1)=1), a razão quenched fica em ~0,6, não 1;
para q=5,α=1, mesma coisa em várias raízes.

**Consequência para o paper**: a equação de pressão (agora "Identidade
de pressão anelada exata", provada) continua correta e agora tem
demonstração de verdade — mas só garante o expoente de CONTAGEM
α_-(q) (que está sempre não-congelado, Teorema de transição sobrevive
intacto para a parte de densidade). O índice de cauda do martingale
W_u (α_+/α_-, incluindo nosso querido α*=2 para q=3) virou
**Conjectura** separada, não teorema — em q=3 com 3 confirmações
empíricas independentes (Hill, EVT, mais a de H-113), em q≥5 **sem**
apoio sólido (a medição de Hill de H-109/H-113 já tinha sido sinalizada
como não-confirmatória). `main.tex`/`main-pt-br.tex` reescritos com
Lema, Teorema, Proposição (congelamento sempre) e Conjectura (índice
de cauda) — ver §3 e §4 do paper.

## Addendum 2 (2026-07-18) — bateria de 4 testes de acompanhamento (Fable + verificação independente)

Depois do conserto acima, pedido explícito do diretor científico: "faça
todos os testes, se precisar chame Fable. sejam criteriosos". Rodados
4 testes, cada um com consulta ao Fable seguida de verificação
independente minha (scripts próprios, não copiados):

**Teste 1 — índice de cauda q=5, estatística mais robusta.** Ver
`experiments/E-103-tail-index-q5-rigorous-test/README.md`. Amostra 8x
maior (5000 raízes vs. 600), 4 níveis de headroom (10^5–10^8) numa só
passada de DFS por raiz, Hill com bootstrap CI em 4 frações de cauda +
regressão Zipf independente. **Resultado**: estabilidade excelente
entre headrooms (o transiente lento que o Fable temia para q=5, raiz
subdominante complexa, não aparece como problema nesta faixa); na
fração de 5% o Hill bate quase exatamente com o previsto (1,58 vs
1,536 previsto, IC95%=[1,41; 1,80]) — mas instabilidade clássica entre
frações (1%→2,10; 10%→1,39) mostra que não é um teste decisivo.
Veredito: encorajador, não conclusivo — Conjectura permanece Conjectura.

**Teste 2 — mais raízes / mais profundidade para o congelamento em
q=3.** Reteste limpo (`/tmp/verify_freezing_clean.py`, raízes fixas via
seed=777, a_max=40 fixo em todos os k, ao contrário de rodadas
anteriores que variavam esses parâmetros entre k raso e profundo — o
que o Fable apontou como possível fonte de inconsistência). Para q=3
(k=5..22) e q=5 (k=5..17, processo interrompido manualmente em k=20
por segurança de memória — memo crescia ~15x por passo, já em 16GB),
o resíduo C_k = log Z_k − A·k + B·log(k) ficou consistentemente na
faixa 2,6–3,4 (q=3) e 2,0–3,0 (q=5), confirmando C_k=O(1) como previsto
pela fórmula assintótica do Fable (ver Addendum 1 e Teste 4 abaixo).
Não converge monotonicamente em k raso — comportamento pré-assintótico
esperado, não bug (ver Teste 4).

**Teste 3 — teorema tipo Biggins rigoroso.** Fable confirmou que
Biggins (1992) é genuinamente o teorema certo para a região
não-congelada de um branching random walk genuíno (i.i.d.), mas NÃO
cobre nossa recursão aritmética diretamente — a lacuna é a mesma
independência que já nomeávamos no Teorema da barreira, agora em forma
quantitativa de grandes desvios. Sem teorema mais forte disponível na
literatura para o caso arithmetic (confirmado por busca — nenhuma ponte
direta existe). Adicionado como `Remark` (rem:transfer-basis) no paper,
citando Biggins1992 + Applegate-Lagarias1995 I/II.

**Teste 4 — por que os números de congelamento não batiam com a
previsão ingênua.** Resolvido pelo Fable: crescimento na fase congelada
não é puramente exponencial, é log Z_k(α) = A·k − B·log(k) + O(1), com
B=3α/(2α_c) — um termo log(k) não-desprezível em k raso. Cruzamento
estimado k≈139 (q=3) e k≈407 (q=5) antes do termo A·k dominar
visivelmente. Explica por que medições em k raso oscilam em vez de
convergir monotonicamente — não é bug, é o regime pré-assintótico
correto. Confirmado independentemente no Teste 2 (C_k estável dentro
de uma faixa O(1), não divergente).

**Limitação reconhecida e não corrigida**: o estimador de regressão
Zipf no Teste 1 não inclui a correção rank−½ de Gabaix-Ibragimov que o
Fable recomendou como âncora mais confiável; a bateria completa
(GI-correção, MLE de GPD, teste Clauset-Shalizi-Newman+Vuong) fica
como próximo passo caso a linha seja retomada — ver
`E-103/README.md`, seção "Próximos passos".

## Addendum 3 (2026-07-18) — bateria completa + teste exato: inconclusivo, não confirmatório

O diretor científico notou que o Teste 1 do Addendum 2 tinha uma "nota
de limitação" (bateria completa não implementada "por falta de tempo")
inconsistente com a autorização já dada de usar tempo/Fable à vontade.
Implementamos a bateria completa e, depois, um teste ainda mais
rigoroso (momento populacional exato). Resultado honesto, em duas
rodadas:

**Bateria completa de 4 estimadores** (Gabaix-Ibragimov, Huisman,
GPD, Clauset-Shalizi-Newman+Vuong): quadro misto. Huisman estável
perto do previsto (1,536), mas GPD sem platô limpo e Vuong favorecendo
**lognormal** sobre lei de potência em 3 de 4 headrooms (p≈0,03). Fable:
os 4 métodos, lidos pela profundidade de cauda que cada um resume,
concordam entre si que o índice local sobe suavemente de ~1,3 a ~2,2 —
os "acertos" anteriores eram artefato de janela de observação, não
confirmação. Veredito: rebaixar de "encorajador" para "inconclusivo".

**Teste exato via momento populacional** (reusa a DP `Z_k(θ;u)`,
θ=α₋(5), sobre TODOS os resíduos mod 5^k, não amostra): checagem de
sanidade M_k(1,0)=1,0 exato em todo k (bate com a identidade de pressão
anelada, confirma implementação). Rodado exato até k=11 (teto seguro de
memória — k=12 estoura, mesmo problema de explosão de estado da
verificação de congelamento). M_k(p) satura para p≤1,6 e diverge para
p≥1,7 — sugeriria índice real >1,536 se lido ingenuamente. MAS: a razão
entre incrementos sucessivos ainda não estabilizou para p≤1,6 em k=11
(ao contrário de p≥1,7, já estável) — assinatura de "desaceleração
crítica" perto de qualquer criticalidade, não evidência de índice mais
alto. O transiente conhecido de q=5 (raiz complexa subdominante,
k^-0,222) cai só ~7% entre k=8 e k=11; reduzi-lo pela metade exigiria
k≈250, inalcançável por enumeração exaustiva (custo 5^k). Extrapolação
Aitken/Richardson tentada e descartada (transiente é oscilatório de
raiz complexa, não geométrico — quebra a premissa do método). Veredito
final do Fable: **inconclusivo, não desconfirmatório**.

**Consequência para o paper**: §3.3 (Conjectura do índice de cauda)
reescrita em `main.tex`/`main-pt-br.tex` para reportar as duas rodadas
honestamente — nem confirmação, nem refutação, com o motivo específico
identificado (transiente de convergência lenta conhecido) em vez de
deixar a questão vaga. Ambos os scripts (`full_battery.py`,
`exact_moment_test.py`) espelhados em
`collatz-endogeny/sec3-pressure-equation/` para reprodutibilidade.

**Ideia descartada no caminho**: uma calibração via árvore i.i.d. de
fase aleatória foi tentada e abandonada — circular (cai algebricamente
na identidade de pressão anelada já provada, no ponto sempre congelado)
E tecnicamente quebrada (contagem bruta de nós explode
combinatorialmente sob fase i.i.d. — ver
`E-103/stage0_iid_power_check.ABANDONED.py`).

**Frente paralela (H-129)**: inspirada por um paper externo (Jon
Seymour, "Rigidity of the Syracuse Transition Matrix", 2026) que prova
que toda a não-rigidez do mapa Syracuse padrão (q=3, forward) se
concentra no polo 2-ádico −1/3. A transcrição literal para nossa árvore
reversa NÃO funciona (mecanismo diferente — nosso "precisa de mais um
dígito" é universal, o dele é localizado numa sequência rara) — mas
abriu um reframing teórico genuíno do congelamento via otimização
ergódica/formalismo termodinâmico a temperatura zero (Mañé, Bousch,
Contreras-Lopes-Thieullen, Jenkinson), com uma confirmação parcial já
verificada por força bruta (a dinâmica gulosa nos resíduos recupera
exatamente o ciclo real mais simples de q=5 e q=7). Ver
`H-129-q-adic-pole-analog-seymour.md` para os detalhes — não fechada,
não integrada ao paper ainda.

## Referências

- H-104 (achado original α*=2 para q=3, agora explicado como caso
  particular exato, não aproximado — mas ver addendum acima: o índice
  de cauda em si virou conjectura, não teorema).
- H-108 (teste EVT em andamento — nova previsão ξ=α₁/α₂ para
  generalizações futuras).
- Scripts do Fable, agora arquivados em `experiments/E-097-qx1-empirical-gate/`
  (`pressure_qx1.py`, `empirical_qx1_tree.py`) e no repositório de
  verificação `collatz-endogeny/sec3-pressure-equation/`.
- E-103 (`experiments/E-103-tail-index-q5-rigorous-test/`) — teste de
  índice de cauda robusto para q=5, ver Addendum 2 acima.
