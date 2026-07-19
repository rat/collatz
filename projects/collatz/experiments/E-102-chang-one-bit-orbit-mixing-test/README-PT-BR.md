# E-102 — Teste computacional da conjectura de "one-bit orbit mixing" (Chang, 2026)

Hipótese relacionada: [`H-128-busca-literaria-dirigida-pos-h127.md`](../../hypotheses/H-128-busca-literaria-dirigida-pos-h127.md)

## O que foi feito

Pedido do diretor científico: testar se o achado 2 de H-128 (Chang 2026,
arXiv:2603.25753, "A Structural Reduction of the Collatz Conjecture to
One-Bit Orbit Mixing") pode ajudar a explicar/fechar algo da linha.
Extraídas as definições exatas do paper (mapa comprimido ímpar-a-ímpar
T(n)=(3n+1)/2^v2(3n+1), indicador de burst X_t=1[n_t≡1 mod4], burst-
ending times, Prop. 5.1-5.5 relacionando bit4/mod32 a comprimento de
gap) e implementado um teste direto sobre órbitas reais — sem Fourier,
sem medida, só aritmética de órbita.

A conjectura remanescente do paper (Seção 5.9): na subclasse de
burst-endings com n≡1 mod 8, a fração que cai em n≡9 mod 32 (gap longo)
vs. n≡25 mod 32 (gap unitário) fica **limitada** perto de 1/2 (não
precisa convergir a 1/2 exatamente, só ficar abaixo de algum δ).

Dois experimentos complementares:

1. **`experiment_ensemble.py`** — muitas órbitas moderadas (2×10⁴ a
   5×10⁴, 20-50 bits) rodadas em paralelo (numpy vetorizado), agregando
   todos os burst-endings de todas as órbitas, do início ao fim de cada
   uma.
2. **`experiment_deep_orbit.py`** — poucas órbitas ÚNICAS mas muito
   longas (500 a 16000 bits, inteiros Python de precisão arbitrária),
   acompanhando a evolução cumulativa do desvio DENTRO de uma mesma
   trajetória — mais fiel ao "T→∞ ao longo de uma órbita" que o paper
   de fato enuncia.

## Resultado

**Validação da implementação**: em nenhum dos dois experimentos surgiu
um burst-ending com n≡1 ou 17 (mod 32) na subclasse n≡1 mod 8 — bate
exatamente com a Prop. 5.1-5.5 do paper (só 9 e 25 deveriam ocorrer).

**Ensemble (muitas órbitas curtas agregadas)**: o desvio |B9/(B9+B25) −
1/2| CRESCE de forma consistente ao longo dos primeiros ~100 passos e
depois estabiliza num platô de ~0,012-0,019 (1,2%-1,9%) — não parece
crescer sem limite, mas também não cai a zero. **Isto por si só ainda é
consistente com a conjectura do Chang** (ela só pede limitação, não
convergência a 0).

**Órbita única longa (o teste mais fiel ao enunciado do paper)**: aqui
o quadro é mais limpo. Rodando uma única órbita de 16000 bits (38395
passos comprimidos, 4761 burst-endings na subclasse relevante) e
acompanhando o desvio a cada 100 eventos, ele **acompanha de perto a
curva de ruído estatístico ~1/√i** (comparação direta na tabela de
saída), sem nenhum sinal de viés sistemático persistente, terminando em
|desvio|=0,00053 no evento 4761. As 5 órbitas de 500 a 8000 bits
testadas em `experiment_deep_orbit.py` (main) mostram o mesmo padrão:
desvios pequenos e consistentes com ruído amostral (0,0004 a 0,028),
sem tendência de crescimento com o tamanho da órbita.

**Interpretação**: o platô de ~1-2% visto no ensemble é aparentemente
um artefato de agregar muitas órbitas curtas e finitas (dominadas pela
fase inicial/transiente, correlacionada entre órbitas de magnitude
parecida), não um viés assintótico real. O teste mais rigoroso (órbita
única, T genuinamente grande dentro da mesma trajetória) é consistente
com a conjectura de mixing do Chang — o desvio se comporta como ruído
decrescente, não como um viés persistente. **Suporte empírico
(qualificado) à conjectura remanescente do paper**, na escala testada
(até ~4761 eventos numa única órbita de 16000 bits) — não uma prova,
mesmo padrão epistêmico dos outros testes empíricos desta linha
(H-111, H-114).

## Arquivos

- `experiment_ensemble.py` — teste vetorizado (numpy) em muitas órbitas
  moderadas.
- `experiment_deep_orbit.py` — teste em poucas órbitas únicas muito
  longas (inteiros de precisão arbitrária).

## Reproduzir

```
python3 experiment_ensemble.py
python3 experiment_deep_orbit.py
```

Custo: ambos rodam em segundos a poucos minutos (a órbita de 16000 bits
usada na análise fina do texto acima foi rodada à parte, ~1-2min).
