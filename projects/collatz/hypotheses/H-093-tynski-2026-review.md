# H-093 — Revisão: Tynski (2026), "A Common Proof of the Riemann Hypothesis and the Collatz Conjecture" — ALEGAÇÃO DE PROVA REFUTADA

Status: alegação de prova refutada (gap real localizado e refutado
computacionalmente, mesmo padrão de erro já catalogado neste projeto)
Criada em: 2026-07-16
Origem: item 087 do catálogo, baixado manualmente pelo diretor
científico (bloqueado para download automatizado, academia.edu, 403).
99 páginas, não revisado por pares, repositório companion no GitHub
(`ktynski/apollonian-wave`, 238 testes).

## O que o paper alega

Uma "prova comum" da Hipótese de Riemann e da Conjectura de Collatz via
um framework unificado ("echo dynamics"/"acoustic spacetime") que
constrói, para cada problema, um "sistema de testemunha fechado"
(closed witness system) — uma tupla (X,T,V_W,ι,∇,Λ,δ) com álgebra de
Clifford, involução, traço construtivo e "drift estrutural positivo" —
e um "teorema mestre" (Teorema 8.64) que afirma: todo sistema desse
tipo com drift positivo força toda trajetória a atingir seu "assento
fixo" em tempo finito. RH e Collatz são apresentados como duas
especializações desse teorema mestre (§9.4, Fig. 26).

O vocabulário é extenso e não-padrão em toda a extensão do paper
("Logos section", "witness bundle", "Merkaba root angles", "Fano
nilpotent seed", "acoustic witness module", grade "Merkaba-Fano",
"27 formulações equivalentes"). O paper reconhece explicitamente ter
tido "duas versões anteriores" com um gap ("Witness Trace Axiom")
que esta versão alega ter eliminado construindo o traço explicitamente
em vez de assumi-lo por axioma.

## O que é matematicamente correto (verificado)

- **Teorema 8.3 (fórmula exata da órbita)**: T^m(n₀) = (3^m n₀+W_m)/2^{A_m},
  com W_m a soma telescópica padrão. Identidade algébrica real e
  correta (mesma família de identidades já vista em H-092/item 071
  desta mesma rodada, e em trabalho próprio deste projeto).
- **Teorema 8.4 (obstrução de ciclo)**: dado um "grace-depth word"
  periódico, existe no máximo um n₀ possível — álgebra correta (equação
  linear com solução racional única). Mas a Observação 8.5 do próprio
  paper admite honestamente que a exclusão de TODOS os ciclos não-
  triviais **não está provada em geral** — só verificada "por busca
  empírica" para k≤6 e "por computação externa" até n≤2^68. Ou seja, a
  exclusão de ciclos é o mesmo resultado computacional padrão já
  conhecido na literatura (idêntico em espírito ao que este projeto já
  mapeou em H-057), não uma prova nova.
- Definições de álgebra de Clifford, involução, traço acústico:
  matemática padrão aplicada corretamente (checável independentemente
  de qualquer conexão com Collatz).

## O gap real: o "axioma (W6)" (limite de Lyapunov determinístico)

A exclusão de **órbitas divergentes** (o lado difícil da conjectura,
nunca resolvido na literatura) depende inteiramente da Definição 8.63,
item (W6): existe uma constante **universal** C≥0 tal que, para toda
órbita,

  log₂(n_m) ≤ log₂(n₀) − m·δ + C·√m,   δ = 2 − log₂3 ≈ 0,415

e o texto é explícito: esse limite vale **"deterministicamente (sem
qualificador estocástico)"**. O texto afirma que isso é "forçado" pela
"restrição de resíduo 2-ádico fino" (eq. 8.1) e pelo argumento de
"pigeon-hole" — mas a justificativa (p.81) é circular: conclui que a
densidade de palavras sobreviventes "decai geometricamente em m **uma
vez que A_m/m > log₂3 seja forçado**" — exatamente a propriedade de
decréscimo determinístico que deveria estar sendo provada, usada para
provar a si mesma. A única evidência oferecida é **verificação
numérica para n₀≤3×10⁴** (`test_deterministic_lyapunov.py`, "C≤5").

Esse é exatamente o padrão de erro que este projeto já identificou
repetidamente em outras alegações de prova (H-045/Mohammed: "M≈2P"
confundindo expectativa ergódica com restrição de um ciclo específico;
H-065/Boyle: e=2/3 derivado sob "n aleatório" aplicado depois a uma
trajetória fixa) — tomar uma propriedade **média/esperada** (E[a_i]=2,
logo δ>0 em média, já estabelecido neste projeto como H-001/H-011) e
tratá-la como garantia **determinística por trajetória individual**,
sem prova real da concentração em torno da média.

## Verificação computacional (refutação direta)

`experiments/E-093-tynski-2026-review/experiment.py`: calcula, para
cada semente n₀, o menor C que faz o limite (8.2) valer em **todo**
ponto m da trajetória — se a alegação "C≤5 universal" fosse
verdadeira, esse C_min nunca deveria superar 5, para nenhum n₀.

| teste | pior C_min encontrado |
|---|---|
| 20.000 sementes aleatórias, n₀ < 10⁴ (mesma faixa testada pelo paper) | **3,92** |
| 20.000 sementes aleatórias, 10⁴ ≤ n₀ < 10⁹ | **5,08** (já excede 5) |
| recordistas de atraso conhecidos (27 a 989.345.275.647) | **8,34** |
| sementes adversariais (buscando sequências longas de a_i=1) | **7,81** |

**A alegação "C≤5 universal" já falha só um pouco além da própria faixa
testada pelo paper**, e o C_min necessário cresce sem indício de
estabilizar conforme n₀ e o comprimento da órbita aumentam (recordistas
de atraso — n com excursões conhecidas como anormalmente longas para
seu tamanho — dão os piores casos, como esperado se o limite for
apenas uma tendência média com flutuações crescentes, não um limite
determinístico fixo).

## Avaliação

A "prova" tem um andaime extenso de matemática correta mas decorativa
(álgebra de Clifford, ângulos de Merkaba, plano de Fano, seção de
Logos) que **não faz nenhum trabalho lógico real** para estabelecer o
único fato que decidiria a conjectura — o limite de Lyapunov
determinístico do axioma (W6). Esse fato é afirmado como "forçado" por
um argumento circular e sustentado só por verificação numérica numa
faixa estreita (n₀≤3×10⁴), que este experimento mostra **não se
generalizar** — refutação direta, não apenas ausência de prova. O
padrão de honestidade parcial do próprio paper (admitir abertamente que
a exclusão de ciclos não é geral, Observação 8.5; seção 9.5/9.6
"o que permanece em aberto") não se estende ao ponto mais crítico —
a seção 9.6 classifica o Teorema 8.59 (Collatz) como "Tier 1: fechado,
incondicional", quando na verdade depende inteiramente do axioma (W6)
não comprovado.

## Referências

- Experimento: `experiments/E-093-tynski-2026-review/experiment.py`.
- Paper: `literature/papers/087_Common-Proof-Riemann-Hypothesis-Collatz-Conjecture.pdf`.
- Padrão de erro análogo: H-045 (Mohammed), H-065 (Boyle).
- H-001/H-011 (E[a]=2, base do δ=2−log₂3 usado no axioma W6).
