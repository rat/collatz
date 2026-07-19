"""
E-103 Estagio 3 -- checa o transiente k^-0,222 no eixo onde ele foi
originalmente observado (M_k(p) vs. profundidade k), nao na cauda de
W_v em x (isso foi o Estagio 2, que testou log-periodicidade em x e
nao encontrou suporte).

Dados: stage1_moment_results.json (Rodada 3), k=5..11 exato, 7 pontos.

Duas perguntas, ambas condicionadas pela limitacao severa de dados
(so 5-7 pontos em k -- nao e por falta de cuidado, e o teto real da
enumeracao exata 5^k):

1. Ha sinal de OSCILACAO na razao de incrementos sucessivos M_k(p)?
   (Isso testaria diretamente a narrativa antiga "raiz complexa
   subdominante", que preveria oscilacao. A propria observacao direta
   da sequencia, sem ajuste nenhum, ja responde isso -- e o unico
   resultado deste script que sobrevive a revisao, ver abaixo.)

2. O ajuste de |razao(k)-1| ~ k^-chi (tentativa de comparar contra
   "0,222") foi FEITO E DESCARTADO (revisao por advisor, 2026-07-19):
   nao e um teste valido. Motivos: (a) 1 so e o alvo assintotico
   correto EXATAMENTE no p critico -- para p<indice de cauda a razao
   converge a taxa geometrica subcritica, nao a 1, entao o alvo esta
   errado para p=1.5 e p=1.6 (so p=1,53629 fica em cima do previsto);
   (b) com n=5 pontos suaves e correlacionados, o erro-padrao OLS nao
   tem significado (o proprio chi ajustado varia 0,98->1,23->3,60 entre
   os 3 p's -- oscilacao grande demais para ser medida real, e sim
   assinatura de sub-poder + alvo errado); (c) a quantidade "0,222" foi
   inventada por mim para comparar -- a fonte original de 0,222 nunca
   foi localizada no projeto (ver correcao em H-109/E-105), entao um
   descasamento aqui nao informa nada sobre se 0,222 esta certo ou
   errado. O codigo do ajuste fica abaixo POR TRANSPARENCIA (mesma
   norma do projeto: manter tentativas erradas visiveis), mas o
   resultado numerico dele NAO deve ser citado como achado.
"""
import json
import numpy as np

with open("stage1_moment_results.json") as f:
    data = json.load(f)

ks = sorted(int(k) for k in data.keys())

for p_str in ["1.5", "1.53629", "1.6"]:
    vals = np.array([data[str(k)]["moments"][p_str] for k in ks])
    incs = np.diff(vals)
    ratios = incs[1:] / incs[:-1]
    k_ratio = np.array(ks[2:])  # k associado a cada razao (indice superior)

    print(f"=== p={p_str} ===")
    print(f"  razoes de incrementos sucessivos: {np.round(ratios, 6).tolist()}")
    print(f"  (k correspondente: {k_ratio.tolist()})")

    # 1. oscilacao? checagem direta -- a razao e monotonica?
    d = np.diff(ratios)
    monotona = np.all(d > 0) or np.all(d < 0)
    print(f"  monotonica (sem oscilacao visivel)? {monotona}")

    # 2. ajuste de lei de potencia a |1 - razao| -- TENTADO E DESCARTADO,
    # ver docstring. Mantido so por transparencia; NAO citar o numero.
    dev = np.abs(ratios - 1.0)
    if np.all(dev > 0):
        logk = np.log(k_ratio.astype(float))
        logd = np.log(dev)
        slope, intercept = np.polyfit(logk, logd, 1)
        print(f"  [DESCARTADO -- ver docstring] ajuste ingenuo |razao-1|~k^-chi "
              f"deu chi={-slope:.4f} (nao interpretar; alvo=1 so correto no p critico "
              f"exato, e n=5 pontos correlacionados nao da erro-padrao confiavel)")
    print()
