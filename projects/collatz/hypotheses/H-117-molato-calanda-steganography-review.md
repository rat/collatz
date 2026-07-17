# H-117 — Molato & Calanda, "A Secured LSB-Based Image Steganography using Modified Collatz Conjecture" (2023): aplicação, sem erros relacionados a Collatz

Status: sem erros (aplicação, sem alegação matemática sobre a conjectura)
Criada em: 2026-07-17
Origem: item 117 do INDEX.md (IEEE ICACCS 2023).

## Enunciado

Usa uma versão "modificada" da função de Collatz como gerador
pseudoaleatório (seed via troca de chaves Diffie-Hellman) para escolher
posições de bits em esteganografia LSB em imagens. Testes: NIST Test
Suite (passou), PSNR (62,94 dB), SSIM (0,999801), Sample Pairs
(0,1084), RS Analysis (0,1078).

## Avaliação

Nenhum erro relacionado a Collatz. A definição do mapa citada está
correta ("if N is even, divided by 2; if N is odd, multiplied by 3 and
1 added... eventually ends at 1", citando Xu & Tamir 2019) e é tratada
apenas como hipótese/citação da literatura, não como algo que os
autores tentam provar. Nenhuma alegação matemática sobre a conjectura
em si em nenhum ponto do artigo. A modificação específica do algoritmo
está só em figura (não extraída em texto).

## Relevância para a investigação atual

Nenhuma — aplicação pura, Collatz usado só como fonte de
pseudoaleatoriedade.
