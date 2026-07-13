# H-016 — Busca de coalescência mod 9 para atacar H-008

Status: refutada como abordagem para H-008 (achados são todos genéricos mod-2^d, não específicos de mod 9)
Criada em: 2026-07-13

## Contexto

H-015 provou que a técnica de coalescência mod-2^d não pode, por construção,
dizer nada sobre classes mod 9 (coprimalidade). Esta hipótese tenta uma
versão conjunta: fixar N mod (9·2^d) — full informação mod 9 **e** d bits
binários simultaneamente — permitindo rastrear a evolução exata tanto do
resíduo mod 9 quanto da paridade/valuação nos primeiros passos.

## Por que isso pode funcionar

O simulador simbólico de E-015 (V=C·K+D, deterministico enquanto C for par)
generaliza para qualquer C₀ par, não só potências de 2. Usando C₀=9·2^d, o
"9" permanece como fator de C durante toda a simulação (nunca é removido,
já que só as divisões por 2 removem fatores de C, e 9 é ímpar) — o que
significa que ao final do prefixo determinístico, D_final mod 9 é
**exatamente** o resíduo mod 9 do valor alcançado, independente de K. Ou
seja: conseguimos rastrear mod 9 e mod 2^d ao mesmo tempo, o que a busca
pura mod-2^d (H-015) não conseguia.

## Enunciado

Buscar, para N ≡ 4 (mod 9) combinado com d bits binários extras (N mod
9·2^d), algum M=N−k (k pequeno, mesmo "K" livre) cuja órbita simbólica
coalesça com a de N — o que provaria que a classe 4 mod 9 nunca é
recordista, resolvendo H-008.

## Como testar

Generalizar o simulador de E-015 para C₀=9·2^d (d de 1 a 12), r₁ ≡ 4 (mod 9)
dentro de [0, 9·2^d), buscar k pequeno com coalescência. Verificar achados
contra órbitas reais (cuidado com o efeito de borda de K pequeno, já visto
em E-015) e contra os 148 recordistas oficiais.

## Atualizações

- 2026-07-13: hipótese aberta.
- 2026-07-13: testada em `experiments/E-016-mod9-coalescence-search/`.
  Encontrou vários candidatos aparentes (verificados contra órbitas reais,
  10/10 K's confirmados no primeiro caso). Mas ao testar se cada achado é
  **exclusivo** da classe 4 mod 9 (repetindo a busca para os outros 8
  resíduos mod 9, mesmo d e mesmo k) — **todos funcionaram igualmente para
  os 9 resíduos**, ou seja, nenhum depende de fato de mod 9. São fenômenos
  puramente mod-2^d (já cobertos por H-015), coincidindo com mod9=4 por
  acaso. Testado até d=7, k=100, nenhum achado genuinamente mod-9-específico.
  Explicação teórica: T(n) mod 9 depende só de n mod 3 (não do valor
  completo mod 9), então fixar mod 9 não adiciona restrição real além do
  mod-2^d puro. **Não resolve H-008** — precisaria de uma ideia
  estruturalmente diferente (não coalescência por deslocamento pequeno).
