# H-111 — Quinta rodada de consulta externa: avaliação crítica de quatro alegações técnicas (Baker/Rhin, somas exponenciais cruzadas, Lema de Breiman, experimento de controle)

Status: concluído — experimento de controle implementado e rodado; nenhum acoplamento aritmético positivo detectado, cota ρ_eff≲0,06 (IC95)
Criada em: 2026-07-17
Origem: quinto prompt enviado à IA externa (`prompt-followup-5-outra-ia.md`),
pedindo caminhos reais (não analogias) para a decorrelação entre folhas
identificada em H-110, mais retomada das três perguntas de uma rodada
anterior. Avaliado pelo Fable com o mesmo pedido de ceticismo das
consultas anteriores (esta é a quarta correção substantiva à mesma IA
nesta linha, depois de Kesten local, Furstenberg/Martin, e a conspiração
2-ádica).

## Enunciado

A IA externa propôs, desta vez com densidade técnica maior que nas
rodadas anteriores: (1) usar o Teorema de Baker (formas lineares em
logaritmos) para obter a TAXA de equidistribuição da fase arquimediana;
(2) reduzir a decorrelação 3-ádica entre folhas a somas exponenciais
cruzadas em ℤ/3^{m+L}, análogas à Proposição 1.17 de Tao (2022),
citando Bourgain-Garaev-Konyagin como território relacionado; (3)
argumentar, via Lema de Breiman, que α*=2 (e a generalização qx+1) está
"blindado" contra a crise de endogenia de H-110; (4) propor um
experimento de "falsificação de controle" com valuações acopladas para
separar experimentalmente "física de ramificação" de "topologia
aritmética".

## Motivação

Depois de três correções anteriores ao mesmo padrão de erro (empréstimo
de prestígio / nome de área impressionante sem conexão real), era
importante verificar se esta rodada, mais tecnicamente densa, de fato
continha conteúdo sólido ou repetia o padrão com verniz mais convincente.

## Avaliação do Fable (resumo — ver consulta completa no histórico da sessão)

| Item | Veredito |
|---|---|
| 1. Baker / fase arquimediana | Meio-certo: núcleo real, mas o teorema certo para dar taxa polinomial é **Rhin (1987)**, não Baker genérico (que só dá taxa super-polinomial); e ataca a metade do problema que já estava resolvida em H-110 (Choquet-Deny), não o gargalo real |
| 2. Somas exponenciais cruzadas | **A melhor sugestão desta IA em toda a linha** — extensão bivariada correta e verificável da Prop. 1.17 de Tao (2022); mas a citação Bourgain-Garaev-Konyagin é errada de regime (BGK é sobre subgrupos multiplicativos pequenos mod primos; aqui 2 é raiz primitiva mod 3^n, é o grupo inteiro de unidades) |
| 3. Breiman / blindagem de α | Conclusão correta, justificativa errada — Breiman exige Y independente de W, que não temos para um gauge aritmético hipotético; a blindagem real vem de um argumento de sanduíche (c·W ≤ WY ≤ C·W) + a equação de pressão (α é propriedade da recursão, não da solução) |
| 4. Experimento de controle | Núcleo bom, duas implementações propostas quebram em direções opostas; versão corrigida de 3 braços vale rodar |

### Detalhe 1 — Baker vs. Rhin

A não-aritmeticidade qualitativa da distribuição do log-passo (2^A ≠
3^k) só precisa de fatoração única — uma linha, já coberta pela
maquinaria de H-110 (Choquet-Deny). O teorema de Baker–Wüstholz
genérico para dois logaritmos dá só |A·log2 − k·log3| >
exp(−C(log B)²), taxa super-polinomial insuficiente para converter em
taxa útil. A cota que realmente dá taxa polinomial para este par
específico é **Rhin (1987, via aproximantes de Padé)**:
|u₁·log2+u₂·log3| ≫ H^{−7.616} — a mesma cota usada na literatura de
exclusão de m-ciclos de Collatz que já tocamos em H-057
(Simons–de Weger, Hercher). Mesmo corrigido, ataca a fase arquimediana,
que não é o gargalo — o gargalo é a decorrelação entre folhas (item 2).

### Detalhe 2 — somas exponenciais cruzadas (direção viva)

Álgebra confirmada: para uma folha ao fim de um caminho com valuações
a₁,...,a_k e somas parciais A_j, 3^k·w = 2^{A_k}·v − Σ_j 3^{j-1}·2^{A_k−A_j}
— os resíduos das folhas mod 3^{m+L} são combinações ℤ-lineares de
potências de 2. Equidistribuição conjunta de pares de folhas ⟺
decaimento das somas cruzadas é o critério de Weyl padrão, e o caso
univariado é literalmente a Prop. 1.17 de Tao. A citação BGK é
imprecisa (regime errado — aqui não há subgrupo pequeno, 2 é raiz
primitiva mod 3^n), mas a redução em si é sólida e é a primeira
proposta com superfície de ataque real e verificável nesta linha
inteira. **Próxima ação concreta e barata**: checar na demonstração da
Prop. 1.17 de Tao (2022) — já temos o PDF (item Tao 2022, H-076) — se o
decaimento de Fourier é uniforme no resíduo inicial. Se for, o caso
cruzado sai por condicionamento; se não for, aí está o conteúdo novo
duro que a IA não endereçou.

### Detalhe 3 — Breiman

Lema de Breiman (1965) exige Y independente de X — vale no toy de
H-110 (espaço-produto por construção), mas não necessariamente para um
gauge aritmético hipotético fabricado do próprio v. A conclusão (α
blindado) sobrevive por dois argumentos mais robustos: (i) sanduíche
c·W≤WY≤C·W para 0<c≤Y≤C, herda o índice sem hipótese de independência;
(ii) α é o autovalor principal da equação de pressão (raiz de
ρ(M_q(α))=1), propriedade da recursão, não da solução particular —
endogenia decide qual solução é a aritmética, nunca o expoente
(já dito em H-110). **Caveat que a IA omitiu**: só o expoente está
blindado — a CONSTANTE de cauda (e qualquer lei limite exata) depende
de gauge.

### Detalhe 4 — experimento de controle (corrigido, vale rodar)

Ponto fino de teoria de smoothing transforms que a IA não distinguiu:
a equação de ponto fixo exige que as cópias de SUBÁRVORE sejam i.i.d.,
mas a classificação (Alsmeyer-Biggins-Meiners 2012) permite dependência
arbitrária entre os PESOS dentro de uma geração. Isso quebra as duas
implementações propostas:

- **Acoplar valuações entre irmãos** (dentro de uma geração): fica
  100% dentro da teoria ABM — α permanece 2 (trivialmente, não é
  descoberta) E a independência entre subárvores continua intacta ⟹ o
  piso de variância previsto pela IA **não aparece** neste braço.
- **Acoplar tempos de parada ao longo de caminhos** (entre gerações):
  sai do framework i.i.d. para Markov-modulado — o expoente de cauda
  vira raiz de ρ(P_α)=1 para o operador com pesos correlacionados, e
  **α genericamente se move** mesmo com marginais idênticas. A
  previsão central da IA ("Hill intocado em α=2") é falsa neste braço.
- **Restringir v mod p**: ou vácuo (só condiciona o ensemble de
  raízes) ou poda a árvore mudando os pesos e confundindo de novo α
  com acoplamento.

**Desenho corrigido de 3 braços** (o que testaria a tese de verdade —
acoplar CONTEÚDO das subárvores entre irmãos, não pesos):

1. Controle positivo: modelo sintético i.i.d. (pesos 3·2^{-a}, Monte
   Carlo por amostragem de caminhos) — espera-se colapso de variância
   com taxa medível.
2. Controle negativo: mesmo modelo com acoplamento de conteúdo entre
   subárvores irmãs de intensidade ajustável ρ — espera-se piso
   crescente com ρ, dando uma curva de calibração piso(ρ).
3. Árvore aritmética real (enumeração exata + G(v) + gap de Jensen,
   ferramentas já existentes), profundidade/truncamento casados com os
   braços sintéticos.

O produto não é binário (colapsa/não colapsa) — é a curva piso(ρ),
convertendo as cotas decrescentes de H-101/H-107 sobre σ_Y numa cota
quantitativa interpretável para o "acoplamento aritmético efetivo".
Teto de expectativa honesto: mesmo corrigido, o experimento não testa a
aritmética diretamente — dá uma régua para interpretar o piso real, não
prova que a árvore real é independente.

## Como testar

Implementar o desenho de 3 braços acima em
`experiments/E-090-syracuse-measure-vs-density/`; separadamente, ler a
demonstração da Prop. 1.17 de Tao (2022) para checar uniformidade no
resíduo inicial (ação de baixo custo, decide se a rota das somas
exponenciais cruzadas é imediatamente tratável ou requer trabalho novo).

## Atualizações

- 2026-07-17: consulta ao Fable concluída, avaliação registrada acima.
  Próximo passo: checar Prop. 1.17 de Tao contra uniformidade, e
  decidir se implementamos o experimento de 3 braços.
- 2026-07-17: **experimento de controle de 3 braços implementado e
  concluído** (`experiment_synthetic_core.py`, `experiment_control_arms.py`,
  `experiment_synthetic_dp_oracle.py` em `experiments/E-090-syracuse-
  measure-vs-density/`). Resumo do percurso completo:

  **Núcleo sintético**: enumeração truncada por TAMANHO (não pesos, não
  spine) espelhando `build_tree_count_dfs`/`measure_G_headroom`;
  estrutura cíclica de tipos (w_a mod 3 cicla como (ρ,ρ+1,ρ+2,...) por
  fase ρ do pai) derivada pelo Fable e verificada contra 10.000 inteiros
  reais; acoplamento de conteúdo (braço 2) via replicação de família
  inteira por hash endereçado (σ,r,tag), com prova de que as marginais
  ficam intactas para qualquer ρ.

  **Bug de checklist descoberto e resolvido**: a criticidade medida
  (E[G|tipo]) não batia com a previsão original do Fable (1,00/2,00,
  ±poucos%) — ficava sistematicamente ~2,6× mais alta. Diagnóstico:
  **erro na derivação teórica do Fable** (omitiu o fator do teorema de
  renovação de Markov), não bug de implementação — confirmado por um
  oráculo de programação dinâmica exata que ele mesmo escreveu, batendo
  com os valores medidos dentro do erro amostral (2,618/5,240 com o
  truncamento de busca real, não 1,00/2,00). Episódio registrado como
  autocorreção do consultor, não erro de montagem nosso.

  **Braço 1 (i.i.d.) vs. Braço 3 (real, remedido no mesmo mult=2000)**:
  variâncias residuais muito próximas em toda a grade m=8 a 29, excesso
  minúsculo e com sinal alternando — nenhum sinal de acoplamento
  positivo entre subárvores irmãs da árvore real.

  **Rodada de forma do braço 2**: confirmou que o mecanismo de
  acoplamento funciona como desenhado (variância cresce
  monotonicamente com ρ), mas descobriu contaminação por saturação em
  ρ alto + m profundo (até 91% dos pares saturados em ρ=1,0/m=29) —
  exatamente o guard que o Fable havia especificado. Conclusão:
  perseguir ρ alto/m profundo é inviável computacionalmente (exigiria
  mult da ordem de milhões) E desnecessário — só o slope perto de ρ=0
  importa para limitar ρ_eff.

  **Rodada final de slope + bootstrap de excesso** (mult=2000, n=4000,
  ρ∈{0;0,05;0,1;0,2}, m∈{11,14,17,20}): slope dVar/dρ decresce com a
  profundidade (0,062 em m=11 a 0,021 em m=20); excesso (real−sintético)
  converge monotonicamente a zero com a profundidade (−0,0033 em m=14 →
  −0,0015 em m=17 → +0,0001 em m=20). Diagnóstico final do Fable: a
  convergência ordenada a zero é assinatura de descasamento residual do
  null sintético (levemente super-disperso em g raso, mais persistente
  em profundidade do que ele havia estimado — só limpa em m=20, não
  m≈14 como previsto), não sinal aritmético real — e por ter sinal
  oposto ao acoplamento positivo procurado, só reforça a conclusão,
  nunca a contradiz. Dois mecanismos alternativos de descasamento
  (normalização do truncamento, jitter de magnitude na amostragem do
  par real) foram checados e descartados pelo Fable.

  **Conclusão final (citável)**: nenhum acoplamento aritmético positivo
  entre subárvores irmãs foi detectado. Cota quantitativa no braço mais
  profundo e melhor calibrado (m=20): **ρ_eff ≲ 0,06 (IC95%)** — o
  acoplamento aritmético efetivo entre folhas da árvore reversa real é,
  no máximo, ~6% do acoplamento máximo simulável no modelo de controle.
  (m=17 daria uma cota mais apertada, ≲0,012, mas sobre um braço ainda
  não totalmente limpo — não usar como número principal, só como nota
  condicional.) Isto converte a barreira de endogenia de H-110 (que
  apenas apontava a existência teórica do gap) numa medida empírica
  quantitativa do tamanho desse gap — evidência a favor de decorrelação
  entre folhas, com a ressalva permanente de que isto calibra o piso
  sob o modelo de acoplamento testado, não prova independência
  aritmética exata.

- 2026-07-17: **checagem barata feita** — lida a demonstração da Prop.
  1.17 no PDF já arquivado (item 106, `106_Almost-All-Orbits-Almost-
  Bounded-Values-Tao.pdf`). Achado favorável, mas parcial: o próprio
  texto afirma explicitamente que "a constante implícita [no decaimento
  do valor esperado E[e^{-2πiξ·Syrac(ℤ/3ⁿℤ)/3ⁿ}]] é uniforme nos
  parâmetros n≥1 e ξ∈ℤ/3ⁿℤ" (Prop. 1.17, com equivalência estabelecida
  à Prop. 1.14, a versão em termos de oscilação/mistura fina
  condicionada em Syrac≡Y mod 3^m). Isso é exatamente o tipo de
  uniformidade que a rota bivariada precisaria para "sair por
  condicionamento", como o Fable apontou.

  **Ressalva honesta**: isso NÃO é a mesma afirmação que precisamos —
  Tao prova decaimento para UMA variável de Syracuse (entrada
  Geom(2)^n), não para o par (w1,w2) de duas folhas irmãs saindo do
  mesmo vértice de bifurcação da árvore reversa. A técnica de prova
  (processo de renovação bidimensional em ℤ², evitar "triângulos
  pretos") já lida com ξ arbitrário de forma uniforme, o que é sinal
  favorável de que uma extensão bivariada é tecnicamente plausível —
  mas não é uma prova nem redução automática. Fica como candidato para
  eventual verificação mais funda (leitura da Seção 7 completa) se a
  linha for adiante, não uma questão fechada.
