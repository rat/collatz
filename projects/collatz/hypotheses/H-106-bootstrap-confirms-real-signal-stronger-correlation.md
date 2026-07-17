# H-106 — Bootstrap confirma: a heterogeneidade do gap de Jensen é sinal real (não só ruído de cauda pesada), e a correlação com PR(r) fica mais forte ao filtrar classes ruidosas

Status: confirmado — resultado positivo, fortalece H-105
Criada em: 2026-07-16
Origem: alerta explícito do Fable em H-104 ("com α*=2, E[G²] está na
fronteira da divergência — parte do fator 46× de H-099 pode ser ruído
de cauda pesada, não heterogeneidade estrutural. Faça bootstrap/
half-sample por classe antes de tratar o 46× como sinal").

## Teste

`experiments/E-090-syracuse-measure-vs-density/experiment_bootstrap_gap.py`:
150 classes residuais (m=8, headroom=2000, 150 amostras/classe).
Para cada classe, bootstrap (1000 reamostragens com reposição) do
gap de Jensen, medindo a incerteza de estimação PRÓPRIA de cada classe
(desvio-padrão bootstrap), comparada com a dispersão observada ENTRE
classes.

## Resultado

- **Dispersão entre classes** (desvio-padrão do gap pontual entre as
  150 classes): 0,0616.
- **Incerteza de bootstrap dentro de cada classe** (média dos
  desvios-padrão bootstrap individuais): 0,0309 — mas com faixa enorme
  (0,0028 a 0,1895), confirmando que algumas classes específicas têm
  estimativas muito mais ruidosas que outras (exatamente o que se
  esperaria de contaminação por cauda pesada em classes específicas).
- **Razão (dispersão entre classes / incerteza média dentro de
  classe) ≈ 2,0** — a heterogeneidade real é cerca do DOBRO do ruído
  de estimação médio. Ou seja: **há sinal real, mas o ruído não é
  desprezível** — é aproximadamente metade da magnitude do sinal.

**O resultado mais importante**: restringindo a análise às 75 classes
mais confiáveis (bootstrap std ≤ mediana, ou seja, removendo as
classes mais contaminadas por ruído de cauda pesada), a correlação
entre gap(r) e log(PR(r)) **sobe de −0,58 (H-105, todas as 300
classes) para −0,74** (75 classes mais confiáveis). A correlação
ficando MAIS FORTE ao filtrar ruído, não mais fraca, é evidência de
que PR(r) é um preditor mecanístico genuíno — parte da variância
"não explicada" de H-105 (R²≈0,34) era contaminação por ruído de
cauda pesada nas classes mais instáveis, não uma limitação real do
mecanismo de PR(r).

## Interpretação

A linha de investigação aberta pela crítica de uma IA externa (e
corrigida pelo Fable) chega a um resultado coerente e bem
fundamentado: G(v) tem cauda universal α=2 (H-104); a heterogeneidade
de forma da distribuição condicional entre classes residuais é
majoritariamente sinal real (razão ~2 sobre o ruído de bootstrap); e
esse sinal é explicado, em boa parte, pela razão de participação da
árvore-prefixo determinística (correlação reforçada para −0,74 ao
controlar ruído). Isso fecha, com razoável confiança, o "mistério"
levantado em H-099 sobre a origem do gap de Jensen — não totalmente
(ainda sobra variância não explicada mesmo nas classes mais
confiáveis), mas com uma explicação mecanicista sólida e verificada em
múltiplas frentes (identidade algébrica, previsão teórica do expoente,
correlação direta, e agora confirmação de robustez a ruído).

## Referências

- H-104 (previsão do expoente α=2, origem do alerta sobre ruído de
  cauda pesada).
- H-105 (correlação original gap~PR(r), −0,58).
- Experimento: `experiments/E-090-syracuse-measure-vs-density/experiment_bootstrap_gap.py`.
