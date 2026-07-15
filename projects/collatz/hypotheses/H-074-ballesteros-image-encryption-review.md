# H-074 — Revisão: Ballesteros, Peña & Renza, "A Novel Image Encryption Scheme Based on Collatz Conjecture" (2018)

Status: revisão externa concluída (construção central correta e verificada; não é sobre a conjectura em si)
Criada em: 2026-07-15
Origem: item 104 da coleção de literatura (`literature/papers/INDEX.md`),
arquivado via busca EBSCO/ScienceDirect em 2026-07-15.

## O paper

Dora M. Ballesteros, Jimmy Peña, Diego Renza (Universidad Militar Nueva
Granada, Colômbia). *Entropy* 20(901), 2018, MDPI — periódico revisado
por pares estabelecido. **Não é sobre resolver a Conjectura de
Collatz** — é um esquema de criptografia de imagens aplicado que usa a
órbita de Collatz de cada valor de pixel como uma primitiva de
codificação de comprimento variável.

## A construção central

Para cada valor de pixel x (deslocado para [1,256]), gera-se um "código
de Collatz": simula a órbita acelerada de x até atingir 1, emitindo um
bit por iteração (0 se par/divisão, 1 se ímpar/3x+1), mais um bit de
terminação fixo "0" na última iteração (quando o valor atinge 1), tudo
prefixado por um cabeçalho artificial "11". A alegação central do paper
(Seção 3.1, ponto 4) é que **a subsequência "11" nunca ocorre dentro do
corpo do código** (só como cabeçalho) — "if a number is odd, the
following number is always even, and the code corresponding to the
sequence odd-odd (i.e., '11') thus does not exist" — o que permite ao
receptor reparticionar um fluxo de bits concatenado de volta em códigos
individuais sem ambiguidade.

## Verificação computacional

`experiments/E-074-ballesteros-image-encryption-review/experiment.py`:

1. **Exemplo do próprio paper** (Figura 3, x=3 → código "1100000101",
   10 bits): reproduzido exatamente, bit a bit.
2. **Corpo nunca contém "11"** (a alegação central): testado para x=1 a
   256 (o range completo de pixels+1 usado pelo esquema). **256 casos,
   0 falhas.**
3. **Unicidade dos 256 códigos**: todos distintos entre si (necessário
   para a decodificação encontrar exatamente 1 match na estrutura
   embaralhada). **Confirmado.**
4. **Decodificabilidade única de um fluxo concatenado real**: gerado um
   fluxo de 1000 pixels aleatórios concatenados (48.693 bits) e
   verificado, via programação dinâmica sobre o conjunto completo dos
   256 códigos válidos, que existe **exatamente uma** decomposição
   válida do fluxo inteiro nesses códigos. **Confirmado.**

Nenhum erro encontrado na construção central. A alegação-chave do
esquema (decodificabilidade única via ausência de "11" no corpo) é
matematicamente correta.

## Nota de metodologia própria (dois erros meus, corrigidos antes de reportar)

1. Minha primeira reconstrução do "código de Collatz" esqueceu o bit de
   terminação explícito que o texto descreve ("the value of 1 is
   reached. Its corresponding code is 0") — sem ele, meu código para
   x=3 tinha 9 bits em vez de 10, não batendo com o exemplo do paper.
   Corrigido lendo o texto com mais cuidado, não apenas a Figura 3.
2. Meu primeiro teste de decodificabilidade usava uma heurística
   ingênua (escanear a próxima ocorrência de "11" como delimitador) com
   um limite de comprimento (`max_len=40`) escolhido sem verificar o
   comprimento real dos códigos (que chega a 130 bits para alguns
   pixels) — isso deu falsos negativos de decodificação que pareciam
   apontar para uma falha real no esquema. Substituído por uma busca de
   programação dinâmica correta (conta o número de partições válidas do
   fluxo inteiro), que resolveu a questão sem ambiguidade: exatamente 1
   partição válida, confirmando o esquema.

## Avaliação geral

Paper de engenharia aplicada correto na construção central verificável
(codificação de comprimento variável com decodificabilidade única).
Segurança do esquema (256! permutações possíveis, análises de entropia/
correlação/SSIM) não foi verificada aqui — são alegações estatísticas
sobre a saída do esquema, não sobre a Conjectura de Collatz, fora do
escopo deste projeto (que foca em matemática da conjectura, não em
criptoanálise). Usa a conjectura só como fonte de uma função de
comprimento variável e imprevisível — categoricamente diferente das
alegações de prova/refutação revisadas em outros itens da coleção.

## Atualizações

- 2026-07-15: revisão externa concluída. PDF lido por completo (10
  páginas, Seções 1-5). Construção central (códigos de Collatz +
  decodificabilidade única) verificada sem erros, após corrigir dois
  erros próprios de reconstrução (bit de terminação faltante; limite de
  comprimento insuficiente na primeira tentativa de teste de
  decodificação).
