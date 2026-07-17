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

## Referências

- H-104 (achado original α*=2 para q=3, agora explicado como caso
  particular exato, não aproximado).
- H-108 (teste EVT em andamento — nova previsão ξ=α₁/α₂ para
  generalizações futuras).
- Scripts do Fable (não reproduzidos nesta sessão, exceto a verificação
  algébrica independente acima): `.../scratchpad/pressure_qx1.py` e
  `.../scratchpad/empirical_qx1_tree.py` — copiar para `experiments/`
  se esta linha for formalizada.
