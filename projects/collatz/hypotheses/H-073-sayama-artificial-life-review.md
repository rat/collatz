# H-073 — Revisão: Sayama, "An Artificial Life View of the Collatz Problem" (2011)

Status: revisão externa concluída (cálculos corretos; um ponto interessante identificado e explicado, não é erro)
Criada em: 2026-07-15
Origem: item 103 da coleção de literatura (`literature/papers/INDEX.md`),
arquivado via busca EBSCO/ScienceDirect em 2026-07-15.

## O paper

Hiroki Sayama (Binghamton University). *Artificial Life* 17, 137-140
(2011), MIT Press — periódico revisado por pares estabelecido. Curto
("letter"), conceitual, explicitamente honesto: a última frase do corpo
diz claramente que o argumento "is still not a rigorous proof of the
Collatz conjecture, because it assumed stochasticity in bit patterns."

## O que o paper propõe

Reinterpreta a dinâmica **acelerada e sem a divisão par** (o autor
descarta a condição par de propósito, "porque só desloca a string sem
influenciar seu padrão"), definindo x_{t+1}=3x_t+LSNB(x_t) (Eq.2), onde
LSNB(x) é o bit não-nulo menos significativo. Interpreta 3x_t como
"replicação" (crescimento à esquerda) e LSNB(x_t) como "extinção" (perda
à direita), calculando duas taxas médias:

- **Crescimento**: L_app = log₂3 ≈ 1,585 bits/passo (aproximação válida
  quando LSNB(x)≪x).
- **Extinção**: R_app = Σ_{l=1}^∞ l·(1/2)^l = 2 bits/passo (assumindo
  bits 0/1 equiprováveis).

Como 2 > log₂3, conclui que "extinção é sempre mais rápida que
crescimento", dando uma explicação ecológica informal (não uma prova)
de por que a série colapsa a um ciclo de bit único.

## Verificação computacional

`experiments/E-073-sayama-artificial-life-review/experiment.py`:

1. **Identidade telescópica exata para L** (Eq.4, antes da aproximação
   de Eq.5) — log₂(x_final)−log₂(x_inicial) = Σ log₂(3+LSNB(x_t)/x_t) é
   exata por telescopagem, verificada sem falhas em 4 sementes.
2. **R_app=2**: soma fechada l·x^l em x=1/2 e soma parcial truncada
   confirmadas iguais a 2,0 (identidade de série geométrica padrão,
   trivial de verificar).

## Achado interessante (não é erro — confirma uma ressalva que o próprio paper já faz)

Ao medir a taxa média de crescimento L sobre uma trajetória longa (2000
passos), o valor medido inicialmente ficou perto de **2,0**, não de
log₂3≈1,585 como o paper prevê — um resultado que parecia contradizer a
Eq.5. Investigando: a dinâmica x→3x+LSNB(x), sem a divisão par, tem
**potências de 2 como estado absorvente exato** — se x=2^k, então
LSNB(x)=x, e 3·2^k+2^k=4·2^k=2^(k+2), então a órbita fica presa
multiplicando por 4 (L=2 exato) para sempre, uma vez atingida uma
potência de 2. Confirmamos que isso é **genérico, não uma coincidência
das sementes testadas**: 200/200 amostras aleatórias atingiram uma
potência de 2 dentro de 500 passos.

Isso **não é um erro do paper** — é exatamente o caso extremo que o
próprio texto já reconhece explicitamente logo após a Eq.5: "the maximal
value of L is log₂4=2 bits/step, which is sustainable **if and only if**
LSNB(xt)=xt always, that is, if the population consists of a single
nonzero bit." O que fizemos foi medir a média sobre toda a trajetória
(incluindo essa fase final absorvente), diluindo a leitura para perto
de 2; medindo separadamente **só a fase ativa** (antes de atingir uma
potência de 2), a taxa bate com log₂3 dentro de <0,5% em todas as 4
sementes testadas (1,590 a 1,591 vs 1,585 teórico).

**Nota de interesse, não uma refutação**: como a dinâmica acelerada sem
divisão SEMPRE atinge uma potência de 2 rapidamente (dezenas de passos
nas sementes testadas), e a partir daí cresce para sempre sem nunca mais
"extinguir" — a "explicação ecológica" do paper (extinção vence
crescimento) só é uma boa descrição da fase transitória inicial, não do
comportamento assintótico da própria dinâmica simplificada que o paper
define. O paper é honesto sobre isso (reconhece o caso extremo
explicitamente), mas não chama atenção para o fato de que esse caso
extremo é o destino *garantido* e *rápido* de toda trajetória na
dinâmica sem divisão — um ponto que teria fortalecido (ou complicado) a
narrativa do artigo, dependendo de como fosse discutido.

## Avaliação geral

Paper honesto e matematicamente correto nas duas fórmulas centrais
(L_app e R_app), com uma limitação de escopo real mas já reconhecida
pelo próprio autor (não uma falha escondida): a simplificação de
remover a divisão par transforma a dinâmica original — que de fato
converge a {1,2,4} — numa dinâmica diferente que colapsa rapidamente
para crescimento explosivo sem limite. A "explicação ecológica" é uma
metáfora pedagógica interessante para a fase transitória, não uma
redução válida do problema original à luz do próprio comportamento
assintótico da dinâmica simplificada.

## Atualizações

- 2026-07-15: revisão externa concluída. PDF lido por completo (5
  páginas). Ambas as fórmulas centrais (L_app=log₂3, R_app=2)
  confirmadas. Identificado e explicado (não é erro do paper) um
  comportamento de estado absorvente (potências de 2) que dilui a
  leitura da taxa de crescimento se medida sobre trajetórias longas —
  resolvido medindo só a fase ativa, que bate com a previsão do paper.
