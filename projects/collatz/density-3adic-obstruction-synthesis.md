# Síntese — Da "densidade não computável" (H-024) à medida de Syracuse (H-090)

Data: 2026-07-16. Consolida a jornada completa H-024→H-086→H-087→H-088→
H-089→H-090, uma cadeia de descobertas encadeadas sobre um único objeto:
a densidade D(v) da subárvore reversa de Collatz enraizada num nó v.
Este documento não repete os detalhes técnicos de cada hipótese (ver os
arquivos individuais em `hypotheses/`) — organiza a narrativa e explica
como um resultado levou ao seguinte, incluindo dois casos em que a
correção de uma hipótese acabou não se aplicando a outra.

## O objeto em comum

D(v) = fração de inteiros ímpares ≤ n_max que estão na subárvore
reversa de v (a árvore onde todo nó tem filho "duplicação" 2v sempre,
e filho extra "ramo" (v−1)/3 se v≡4 mod6). Essa árvore é o mesmo objeto
usado em H-013 (a família especial J_t) e H-018 (o mecanismo de
ramificação) — D(v) é a quantidade central que a recursão exata
D(v)=D(2v)+D(ramo) tenta calcular.

## Capítulo 1 — H-024 (2026-07-13): "D(v) não é função de resíduo finito"

Testando 5 valores todos ≡85 (mod 3⁶=729), com magnitude variando por
~860×, encontramos variação de **300×** em D(v) — concluímos que D
depende de "estrutura 3-ádica arbitrariamente profunda", sem fórmula
fechada de dimensão finita possível. Esse resultado foi correto na
conclusão formal, mas o desenho tinha um problema que só apareceria
dois dias depois.

## Capítulo 2 — H-086 (2026-07-16): a crítica do Fable

Consultado para ideias criativas sobre esta linha, o modelo Fable
apontou que H-024 não separava o efeito de **magnitude** do efeito de
**resíduo** — os 5 valores comparados tinham magnitudes muito
diferentes, e se D(v) fatora como C(log v)·G(v mod 3^K), a variação de
300× podia ser majoritariamente o termo trivial C, não o termo
residual G. Testado diretamente: **D(v)≈C/v quase exatamente**
(regressão log-log, inclinação=−0,9971, R²=0,9991). Removendo esse
termo, a variância "inexplicada" caiu de ~300× para **~1,26×** — mais
de duas ordens de grandeza de redução. A conclusão formal de H-024
continuou válida (D não é função só de resíduo finito), mas a
*magnitude* do fenômeno restante era muito mais modesta do que parecia.

## Capítulo 3 — H-087 (2026-07-16): o resíduo tem estrutura real

Depois de isolar G(v)=D(v)·v, testamos se ele tem continuidade
3-ádica genuína — diferente de D bruto (onde nenhum K finito reduzia a
incerteza). Resultado: a variância de log(G) cai monotonicamente
conforme mais dígitos base-3 são fixados (0,41 em K=1 para 0,10 em
K=8), confirmado em 5 cadeias de resíduo independentes. **G, ao
contrário de D, é aproximadamente contínuo no 3-ádico v** — abrindo a
porta para as duas ideias mais especulativas do Fable (expansão de
Mahler, medida de Syracuse em ℤ₃).

## Capítulo 4 — Auditoria: o mesmo padrão em outras hipóteses (H-088/H-089)

Perguntamos ao Fable se o mesmo confound de magnitude podia estar
escondido em outras hipóteses da linha. Ele apontou duas candidatas —
com desfechos opostos, o que é o ponto mais importante deste capítulo:

- **H-089 (H-026 estava errada)**: H-026 perguntava se K maior atrasa
  a divergência de memória finita, e concluiu que não. O Fable mostrou,
  por aritmética direta, que os valores relatados batiam quase
  exatamente com o termo trivial de magnitude — a conclusão "K não
  importa" era matematicamente garantida pelo desenho, não uma
  descoberta. Retestado sobre G (não D bruto), com dispersão medida em
  janelas de magnitude controladas: a conclusão **inverteu** — K maior
  reduz a dispersão de forma clara (0,2352→0,0936, K=2 a K=8). H-026
  foi formalmente revertida.
- **H-088 (H-018 estava certa)**: a "taxa de decaimento entre galhos
  férteis" de H-018 (73×–680×) parecia o mesmo padrão de risco. Testado
  com 18 pares de galhos: o termo trivial de magnitude ali é **exatamente
  64** em todos os casos (consequência algébrica de "3 posições" sempre
  multiplicar por 4³), uma constante fixa, não uma variável livre —
  dividir por uma constante não muda a dispersão. A suspeita **não se
  confirmou**; H-018 permanece correta como estava.

**A lição destes dois capítulos**: o mesmo padrão de risco (comparar
casos com magnitude não controlada) só é um problema real quando a
magnitude de fato varia livremente entre os pontos comparados. Testar
isso caso a caso, em vez de aplicar uma correção por analogia, foi
essencial — uma correção "por precedente" teria estado errada em pelo
menos um dos dois casos.

## Capítulo 5 — H-090 (2026-07-16): G(v) tem nome e endereço na literatura

Com G confirmado como tendo estrutura 3-ádica real (H-087), implementamos
a segunda ideia do Fable: testar se G é descrito pela densidade local de
uma medida μ em ℤ₃. Antes de escrever código, consultamos o Fable para
validar a montagem matemática — ele identificou um erro estrutural numa
primeira tentativa de montagem e forneceu a recursão correta, que se
revelou ser **exatamente a mesma equação do Lemma 1.12 de Tao (2022)**
para a variável aleatória Syrac(ℤ/3ⁿℤ) — já implementada e verificada
neste projeto ao revisar o paper de Tao (H-076).

Reaproveitando essa implementação (sem reescrever do zero), testamos a
correlação entre a densidade local dessa medida e G(v) medido
computacionalmente: **correlação log-log de 0,916 (m=2) a 0,980 (m=4)**,
crescendo consistentemente e estável em 5 amostras independentes
(nunca abaixo de 0,947).

## O que essa cadeia deixa como saldo

1. **Um resultado positivo real**: a variância residual de D(v), que
   começou como "ruído genérico sem explicação" (conclusão de sessão
   anterior a esta cadeia), agora tem uma descrição explícita — a
   mesma medida de Syracuse que aparece no trabalho mais rigoroso já
   publicado sobre a conjectura (Tao 2022). Isso não é uma fórmula
   fechada nem uma prova, mas é uma caracterização substancialmente
   mais rica do que "oscila sem padrão".
2. **Uma hipótese revertida com honestidade** (H-026→H-089): registrada
   como erro formal, não apagada — o processo de errar, identificar via
   consulta externa, e corrigir ficou documentado.
3. **Uma suspeita testada e descartada** (H-018 via H-088): prova de que
   nem todo padrão de risco se generaliza — vale testar caso a caso.
4. **Disciplina demonstrada**: em nenhum ponto desta cadeia uma sugestão
   do Fable foi aceita sem verificação computacional direta — inclusive
   quando ele mesmo propôs a montagem de um autômato, ela foi implementada
   e validada contra valores exatos já conhecidos antes de qualquer
   conclusão.

## Referências

- Hipóteses: `hypotheses/H-024-*.md`, `H-026-*.md` (revertida),
  `H-086-*.md` a `H-090-*.md`.
- Experimentos: `experiments/E-086-*` a `E-090-*`.
- H-090 conecta com H-076 (revisão do paper de Tao 2022, item 106 da
  coleção de literatura) e com H-013/H-018 (a árvore reversa e a
  família J_t que motivaram toda esta linha).
