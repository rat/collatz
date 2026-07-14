# H-046 — Revisão do paper #002 (Adnan & Dar, "Decimal-Parity-Based 3n+1 Mapping") — extensão ad hoc mal definida

Status: revisão externa concluída — não é alegação de prova, mas a
construção central é conceitualmente mal definida
Criada em: 2026-07-14
Origem: paper baixado manualmente pelo diretor científico (item 002 da
coleção, `literature/papers/002_Decimal-Parity-Based-3n1-Mapping.pdf`,
Global Journal of Pure and Applied Mathematics, 9 páginas).

## O paper

"Behavior of a Decimal-Parity-Based 3n+1 Mapping" — J. Adnan (Jammu and
Kashmir Board of School Education) e S.A. Dar (Kashmir University).
**Não alega provar ou refutar** a Conjectura de Collatz original (nos
inteiros positivos) — categoria diferente de H-043/H-045. Propõe uma
"extensão" ad hoc: para um decimal n∈(0,1), define "paridade" olhando
o **último dígito significativo** da representação decimal (ímpar/par)
e aplica a mesma regra 3n+1/n÷2 (em aritmética real) conforme essa
paridade. Conclui que a sequência diverge para infinito para todo
n∈(0,1) ("Mathematical Law" na conclusão).

## O que está correto

A aritmética de **todos** os exemplos do próprio paper confere
(`experiments/E-046-adnan-dar-decimal-parity-check/`): Tables 1-2,
Examples 1-3, e a cadeia de 5 passos partindo de 1231.42. Não há erro
de cálculo em lugar nenhum do paper.

## O problema conceitual (dois níveis)

1. **A regra de "paridade" não é definida na maior parte do domínio
   que o paper alega cobrir.** "Último dígito significativo" só existe
   para decimais com expansão **finita** — um subconjunto contável
   (medida zero) de (0,1). A "Lei Matemática" da conclusão ("∀n∈(0,1):
   lim f_i(n)=∞") é uma afirmação sobre o contínuo, mas a regra que a
   sustenta nem está bem-definida para 1/3 (0,333...), 1/7
   (0,142857142857...), ou qualquer irracional (√2/10, etc.) —
   confirmado computacionalmente que nenhum desses tem "último dígito".

2. **Mesmo restrita aos decimais finitos, a divergência é um artefato
   trivial, não um mecanismo profundo.** Testamos 200 decimais
   aleatórios em (0,1): 200/200 divergem em 30 passos. Isso não reflete
   nenhuma estrutura análoga ao Collatz real — no Collatz original,
   3n+1 é **sempre** par quando n é ímpar (fato algébrico: n ímpar ⟹
   3n+1 par), garantindo que a divisão subsequente por 2 seja uma
   consequência estrutural, não arbitrária, do próprio valor. Aqui, a
   "paridade" do resultado 3n+1 depende do último dígito de sua
   representação decimal — uma propriedade **sem nenhuma relação
   algébrica** com o valor 3n+1 em si. Combinado com a constante "+1"
   nunca normalizada em relação à escala do domínio (0,1) — de modo que
   3×(número pequeno)+1 ≈ 1 quase sempre, um salto de ordens de
   magnitude relativo ao ponto de partida — a divergência é garantida
   por construção, não uma propriedade nova ou informativa sobre a
   conjectura original.

## Por que isto é diferente das "alegações de prova completa"

Diferente de Santos (2018), CTUHSK (H-043) e Mohammed (H-045), este
paper não tenta provar nada sobre o problema original — é uma
exploração tangencial de um sistema dinâmico diferente que reaproveita
a linguagem do Collatz. Não vai para
`literature/unverified-proof-claims.md` (não é alegação de prova/refutação
da conjectura original); fica registrado aqui como parte da crítica
cumulativa da coleção.

## Novas hipóteses?

Nenhuma. O sistema estudado não é uma generalização matematicamente
significativa do Collatz (a "paridade decimal" não tem análogo
algébrico ao v₂(3n+1) real), e o próprio paper não conecta o resultado
de volta ao problema original.

## Atualizações

- 2026-07-14: paper lido por completo (9 páginas), aritmética verificada
  (100% correta), problema conceitual identificado e demonstrado
  computacionalmente em dois níveis independentes
  (`experiments/E-046-adnan-dar-decimal-parity-check/`). Flags
  atualizadas em `literature/papers/INDEX.md` (item 002: Lido=Sim,
  Corrigido=Sim, Implementado=Sim).
