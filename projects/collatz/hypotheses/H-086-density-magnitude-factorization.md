# H-086 — D(v) fatora quase inteiramente como C/v; a dependência 3-ádica "profunda" de H-024 era majoritariamente efeito de magnitude

Status: confirmada (H-024 recalibrada, não invalidada — a conclusão formal continua correta, mas o mecanismo estava mal atribuído)
Criada em: 2026-07-15
Origem: consulta ao modelo Fable pedindo ângulos criativos para H-013/
H-018/H-024, a pedido do diretor científico. O Fable apontou uma
crítica metodológica direta ao desenho experimental de H-024, em vez
de propor só ideias novas — testada aqui antes de investir em qualquer
uma das 4 ideias mais especulativas que ele também trouxe (expansão de
Mahler, renormalização, complexidade de Kolmogorov, multifractal).

## A crítica do Fable

H-024 mediu D(v) para 5 valores todos ≡85 (mod 3⁶=729), com magnitudes
diferindo por um fator ~860× (85 a 72.985), e concluiu que a variação
de 300× observada mostra que D depende de "estrutura 3-ádica
arbitrariamente profunda". O Fable observou que isso **não separa** o
efeito do resíduo do efeito da magnitude: se D(v) fatora
(aproximadamente) como C(log v)·G(v mod 3^K), a variação de 300× pode
ser majoritariamente o termo de magnitude C, não o termo residual G —
e a atribuição mecanística de H-024 estaria correta na conclusão
formal ("não é função de resíduo finito sozinho") mas errada em
apontar a causa.

## Teste

`experiments/E-086-mahler-magnitude-separation/experiment.py`, usando
`build_tree_count_dfs` já validado (E-018): medimos D(v) para muitos v
com o **mesmo resíduo mod 729** (=85 mod 729, o mesmo de H-024) mas
magnitude variando livremente ao longo de 5+ ordens de grandeza (85 a
~10⁷), e calculamos a regressão de log₁₀(D) contra log₁₀(v).

## Resultado

**Regressão log-log**: inclinação = **−0,9971** (praticamente exatamente
−1), R²=**0,9991** — ou seja, D(v)·v é quase constante. Isso é o
comportamento de **D(v) ≈ C/v** quase exato, com C variando pouco.

**Resíduo depois de remover o termo 1/v** (log₁₀(D·v), medido em 23
amostras adicionais com o mesmo resíduo mod 729, magnitude variando
por ~5 ordens de grandeza): desvio-padrão de **0,0995 dex** (fator
~1,26×) — comparar com o **1,24 dex** (fator ~300×) da variação bruta
original de H-024. Ou seja: **removendo só o termo de magnitude 1/v,
a variação "inexplicada" cai de 300× para ~1,26×** — mais de duas
ordens de magnitude de redução.

## Interpretação

A crítica do Fable estava certa, e de forma mais decisiva do que eu
esperava: quase toda a variação de 300× que H-024 atribuiu a
"profundidade 3-ádica arbitrária" é, na verdade, o termo arquimediano
trivial D(v)~1/v — que é exatamente o que se esperaria de qualquer
densidade normalizada por contagem de nós menores que um limite fixo
(quanto maior v, proporcionalmente menos múltiplos de sua subárvore
cabem abaixo de qualquer n_max fixo). **Isso não invalida a conclusão
formal de H-024** (D(v) genuinamente não é função só do resíduo mod
3^K — o resíduo residual de ~1,26× depois de remover 1/v ainda mostra
alguma dependência que K=6 não capturou completamente, e sabemos por
outros testes desta sessão que não existe K finito que zere esse
resíduo). **Mas muda a magnitude do fenômeno que resta para explicar**:
não é uma variação de 300× indomável, é uma variação residual de
~1,26× depois de contabilizar o efeito trivial de tamanho — uma
obstrução real, porém muito mais modesta do que parecia.

## Por que isso importa para as próximas tentativas

Qualquer tentativa futura de caracterizar a "estrutura 3-ádica" de D(v)
(expansão de Mahler, medida de Syracuse em ℤ₃, espectro multifractal —
ideias trazidas pelo Fable) deveria trabalhar com o **resíduo**
D(v)·v (ou G(v) = D(v)/C(v)), não com D(v) bruto — do contrário,
qualquer análise estaria dominada pelo termo trivial 1/v e não revelaria
a estrutura genuinamente 3-ádica que sobra. Isso é uma correção de
metodologia importante para toda a linha H-013/H-018/H-024, não só uma
nota lateral.

## Atualizações

- 2026-07-15: identificado via consulta ao Fable, testado e confirmado
  imediatamente com regressão log-log (R²=0,9991). Reduz a variância
  "inexplicada" de H-024 de ~300× para ~1,26×, sem invalidar a
  conclusão formal de que D(v) não é função de resíduo mod 3^K
  sozinho. Próximo passo natural (não feito ainda): repetir a análise
  de continuidade 3-ádica (sequência de Cauchy em ℤ₃) sobre o resíduo
  D(v)·v em vez de D(v) bruto, antes de decidir se vale investir em
  expansão de Mahler ou análise multifractal.
