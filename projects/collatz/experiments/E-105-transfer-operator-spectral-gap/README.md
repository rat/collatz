# E-105 — Gap espectral do operador de transferência dual (H-129)

Hipótese relacionada: [`H-129-q-adic-pole-analog-seymour.md`](../../hypotheses/H-129-q-adic-pole-analog-seymour.md)
Ver também: [`H-109-...md`](../../hypotheses/H-109-generalized-qx1-pressure-equation-exact-closed-form.md),
[`E-103-tail-index-q5-rigorous-test`](../E-103-tail-index-q5-rigorous-test/README.md)
(corrigidos por este experimento).

## O que motivou

As notas do projeto (H-109, E-103, H-129) atribuíam o transiente lento
de convergência k^-0,222 observado no teste de índice de cauda de q=5
a "uma raiz complexa subdominante do operador de transferência". Ao
retomar H-129 ("análise espectral de Perron-Frobenius" era o próximo
passo listado em H-129/E-104), percebi uma tensão real antes de
programar qualquer coisa: decaimento **geométrico oscilatório**
(assinatura de autovalor subdominante isolado) e decaimento em **lei de
potência** k^-0,222 (assinatura clássica de AUSÊNCIA de gap espectral)
são categorias matematicamente incompatíveis na mesma camada.

## Consulta ao Fable

Consultei o Fable (contexto completo: Lema da bijeção de fibra, a
impossibilidade de estado finito já provada — Exemplo ex:naive-fails —,
a identidade de pressão anelada, a dicotomia quenched/anelado). Resposta
resumida (ver H-129 para o texto completo):

1. O operador certo é o **dual** M_α (pai→filho, via φ_a(w)=(qw+1)·2^-a),
   não o Koopman L_α (filho→pai, esse é o que o Fato 2/Exemplo
   ex:naive-fails proíbe como estado finito). M_α PRESERVA funções
   localmente constantes mod q^K exatamente.
2. M_α tem **gap espectral perfeito e estrutural**: expansão q-ádica
   uniforme por fator exato q, distorção zero — espectro de M_α
   restrito a qualquer nível K é EXATAMENTE {Λ,0} (Λ=q^α/(2^α−1)), sem
   nenhum autovalor subdominante isolado. Manneville-Pomeau/Sarig-Iommi
   (que precisaria de ausência de gap) não se aplica.
3. O k^-0,222 pertence a uma camada NÃO-LINEAR diferente: o teste de
   momento em α perto do índice de cauda está sentado no caso de
   fronteira de branching random walk (α_+ é sempre congelado, já
   provado) — correções polinomiais em k (Bramson, Aïdékon) são
   esperadas aí, sem contradizer o gap da camada linear. Suspeita:
   efeito de reticulado log-periódico (pesos são potências de 2).
4. Armadilha identificada preventivamente: um teste tipo Ulam ingênuo
   (ver espectro de L_α truncado, ou esperar "autovalor subdominante
   convergindo" conforme K cresce) produziria um artefato numérico
   garantido, por não-normalidade do bloco nilpotente — não um sinal
   real de "gap fechando".

## Verificação numérica (`experiment_gap_check.py`)

Construção exata (aritmética modular exata para os índices; ponto
flutuante só nos pesos/autovalores) da matriz q^K×q^K de M_α, para
q=5, α_+=1 (congelada) e α_-=0,650919 (não-congelada), K=2,3,4.

**Resultado — confirma a previsão do Fable em todos os pontos**:

- Soma de linhas de M_α = Λ teórico exatamente (casa 8+ dígitos), em
  toda linha e todo K — confirma M_α·1=Λ·1.
- Autovalor dominante = Λ, em todos os casos.
- Todos os demais autovalores ≈0: 2,3e-8 (K=2) → 9,3e-6 (K=3) → 2,0e-4
  (K=4). O crescimento com K é exatamente o ruído de não-normalidade
  previsto pelo Fable (bloco nilpotente crescente) — **não** um
  autovalor real se aproximando de Λ. Não interpretei isso como "gap
  fechando" porque fui avisado do artefato antes de rodar.

## Conclusão

Espectro {Λ,0} confirmado estrutural e numericamente — gap espectral
perfeito na camada linear. A via "análise espectral de Perron-Frobenius"
listada em H-129/E-104 como próximo passo está **fechada**: a resposta
é definitiva, e não resolve a Conjectura do índice de cauda (que vive
na camada não-linear crítica, não na linear). Corrigimos a terminologia
"raiz complexa subdominante" em H-109 e E-103/README.md — ela não se
sustenta com a formalização correta do operador.

## Próximos passos (se a linha for retomada)

~~Testar a hipótese log-periódica da cauda diretamente~~ — **feito e
não suportado, E-103 Estágio 2 (2026-07-19)**: consulta ao Fable
derivou que o sistema é não-aritmético (log₂5 irracional destrói a
periodicidade, dicotomia de Goldie) — sem log-periodicidade assintótica
esperada. Teste pré-registrado nos dois períodos derivados confirmou:
potência do periodograma no nível de ruído em todos os 4 headrooms
testados. Ver `experiments/E-103-tail-index-q5-rigorous-test/README.md`,
seção "Estágio 2".

Isso NÃO fecha a origem do k^-0,222 — só refuta mais uma explicação
candidata (a primeira foi o gap espectral, aqui mesmo). O item real que
resta é testar o transiente no eixo em que ele foi observado (M_k(p)
vs. k, não a cauda de W_v em x) — ver E-103 item 5 dos próximos passos.

## Arquivos

- `experiment_gap_check.py` — construção e verificação numérica de M_α.

## Reproduzir

```
python3 experiment_gap_check.py    # segundos, sem dependências além de numpy
```
