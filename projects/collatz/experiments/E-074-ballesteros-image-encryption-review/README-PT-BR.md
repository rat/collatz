# E-074 — Revisão de Ballesteros et al., "A Novel Image Encryption Scheme Based on Collatz Conjecture" (2018)

Hipótese relacionada: [`H-074-ballesteros-image-encryption-review.md`](../../hypotheses/H-074-ballesteros-image-encryption-review.md)

## O que foi feito

Verificamos a construção central do esquema de criptografia (item 104):
os "códigos de Collatz" — codificação de comprimento variável derivada
da órbita acelerada de cada valor de pixel — e a alegação de que a
subsequência "11" nunca aparece dentro do corpo de um código (só como
cabeçalho artificial), o que permite decodificação única de um fluxo
concatenado.

## Resultado

Confirmado sem erros: exemplo do próprio paper reproduzido exatamente;
corpo nunca contém "11" em nenhum dos 256 valores possíveis; os 256
códigos completos são todos distintos; um fluxo de 1000 pixels
concatenados (48.693 bits) tem exatamente uma decomposição válida
(verificado via programação dinâmica). Ver H-074 para o veredito
completo e duas correções de metodologia própria feitas antes de
reportar qualquer conclusão.

## Reproduzir

```
python3 experiment.py
```
