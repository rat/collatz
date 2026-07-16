# H-084 — Revisão: Ruiz Castillo, "Disipación Promedio... y medidas de equilibrio" (2026)

Status: revisão externa concluída (correto, elementar; oitavo paper da mesma série, mesmo padrão)
Criada em: 2026-07-15
Origem: item 035 da coleção de literatura (`literature/papers/INDEX.md`),
arquivado em 2026-07-15 (DOI 10.5281/zenodo.20636301).

## O paper

Juan Carlos Ruiz Castillo (Universidad de San Carlos de Guatemala) —
**oitavo paper do mesmo autor** já revisado neste projeto (ver
`literature/ruiz-castillo-research-program.md` para a síntese dos 7
anteriores: H-039, H-050, H-052 a H-056). **Mesmo padrão exato**: pega
a mesma quantidade clássica — a "deuda residual"
L_k(n)=k·log₂3−A_k(n), onde A_k(n) é a soma das primeiras k valuações
2-ádicas ao longo da órbita acelerada (já conhecida deste projeto via
H-001/H-011, e idêntica à usada nos 7 papers anteriores da série) — e a
reveste com um vocabulário formal novo: aqui, **dinâmica simbólica e
teoria ergódica** (medidas invariantes sobre um espaço simbólico de
sequências de valuações, semiconjugação com o deslocamento, potencial
dissipativo, Teorema Ergódico de Birkhoff). Explicitamente não alega
provar a conjectura: "El propósito de este trabajo no es afirmar una
demostración definitiva de la Conjetura de Collatz."

## Verificação computacional

`experiments/E-084-ruiz-castillo-dissipation-review/experiment.py`:

1. **Proposición 1.2** (interpretação multiplicativa):
   2^{L_k(n)}=3^k/2^{A_k(n)}. **24 casos, 0 falhas.**
2. **Proposición 2.4** (semiconjugação simbólica): π(U(n))=σ(π(n)),
   onde U é o mapa acelerado e σ o deslocamento simbólico — verificada
   diretamente checando a_j(U(n))=a_{j+1}(n) para muitos j. **105
   casos, 0 falhas.**
3. **Proposición 3.2** (classificação local do potencial): φ(a)<0 sse
   a₀=1; φ(a)>0 sse a₀≥2; φ(a)=0 nunca ocorre (a₀ inteiro, log₂3
   irracional). **19 casos, 0 falhas.**

Nenhum erro encontrado. Todas as identidades são reescritas algébricas
diretas da definição, como nos 7 papers anteriores da série.

## Nota de metodologia própria (erro corrigido antes de reportar)

Minha primeira tentativa de testar uma suposta identidade
"3^k·n=U^k(n)·2^{A_k(n)}" (não uma alegação do paper — uma suposição
minha sobre como A_k deveria se relacionar à órbita) falhou em 100%
dos 120 casos testados. Investigando: a fórmula estava errada porque
ignora os termos "+1" que se acumulam a cada passo do mapa acelerado
(U(n)=(3n+1)/2^{v₂(3n+1)}, não simplesmente 3n/2^{v₂}) — a relação real
entre A_k(n) e a órbita é mais sutil que uma multiplicação direta.
**Isso não é um erro do paper** — é um teste que eu mesmo inventei
incorretamente, fora do que o texto realmente afirma. Removido e
substituído por uma checagem de sanidade mais modesta (crescimento
plausível de A_k(n) em torno de k·log₂3, consistente com o drift já
conhecido deste projeto).

## Avaliação geral

Mesmo veredito dos 7 papers anteriores da série: matematicamente
correto, elementar (todas as identidades concretas são reescritas
diretas), sem verificação numérica própria, sem alegação de prova.
Consistente com o padrão já documentado na síntese do programa —
Collatz como "estudo de caso" para demonstrar aplicabilidade de um
formalismo clássico (aqui, dinâmica simbólica/teoria ergódica) a uma
quantidade já conhecida, não uma tentativa de resolver o problema.

## Atualizações

- 2026-07-15: revisão externa concluída. PDF lido por completo (15
  páginas). Três proposições centrais confirmadas sem exceção. Um erro
  metodológico próprio (não do paper) identificado e corrigido antes
  de reportar. Considerar incluir este item na síntese
  `literature/ruiz-castillo-research-program.md` (oitavo paper da
  série) numa próxima atualização, se pedido.
