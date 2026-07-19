"""
E-107 -- checa se a Definicao 2 de H-127 (configuracao diagonal
(gamma,delta,eta) de profundidade s) e satisfeita por xi GENERICO
(incluindo xi=1), ou se e' de fato uma condicao restritiva.

Contexto: H-127/Lema B usa a Definicao 2 (configuracao diagonal) como
o objeto que uma falha da WCC + concentracao espectral SC(eps) forcaria
a existir. Ao tentar escrever a Etapa 6 do esboco da prova (upgrade
"configuracao diagonal" -> "segmento continuo", consulta ao Fable,
2026-07-19), surgiu a suspeita de que a Definicao 2 como escrita (janela
[gamma*t - t^(2/3), gamma*t + t^(2/3)], sem exigir COERENCIA entre os
expoentes a_t escolhidos em escalas consecutivas) e' satisfeita por
quase qualquer xi, nao so por xi estruturado -- o que tornaria o Lema B
vazio de conteudo com essa definicao.

Este script (gerado pelo Fable durante a consulta, promovido a
experimento formal) testa isso diretamente: para xi=1, alguns xi
pequenos, e varios xi aleatorios de ~200 bits, mede:

  (a) fracao de escalas t=1..S com pelo menos um "hit" na janela
      (definicao literal da Def. 2, sem exigir cadeia coerente);
  (b) o maior "segmento continuo encadeavel" -- um run de escalas
      consecutivas com escolha de expoente a_t monotona e incrementos
      limitados (o objeto que de fato carregaria conteudo de rigidez,
      analogo ao "encadeamento" mencionado na propria heuristica de
      abundancia de H-127).

Resultado esperado se a Def. 2 for vazia: fracao de hits proxima de 1
para TODO xi testado (incluindo xi=1), enquanto o maior segmento
encadeavel fica limitado a O(log S) para todo xi -- sem diferenca entre
xi "aleatorio" e xi=1.

Ver hypotheses/H-127-reducao-z-number-dicotomia-espectral-wcc.md,
secao "Lema B", Etapa 6 (upgrade diagonal -> segmento continuo).
"""
import math
import random

random.seed(2026)

GAMMA = 1 + math.log(3) / math.log(4)  # ~1.7925 (limiar WCC, c=0)


def hits_at_scale(xi, t, gamma, delta):
    """Expoentes a na janela [gamma*t - t^(2/3), gamma*t + t^(2/3)]
    com ||xi*2^a/3^t|| < delta."""
    w = t ** (2.0 / 3.0)
    lo = max(0, math.ceil(gamma * t - w))
    hi = math.floor(gamma * t + w)
    m = 3 ** t
    out = []
    r = (xi * pow(2, lo, m)) % m
    for a in range(lo, hi + 1):
        d = min(r, m - r) / m
        if d < delta:
            out.append(a)
        r = (2 * r) % m
    return out


def diag_profile(xi, s, gamma, delta):
    """Fracao de escalas t=1..s com hit (definicao literal da Def. 2)."""
    misses = []
    hitsets = []
    for t in range(1, s + 1):
        h = hits_at_scale(xi, t, gamma, delta)
        hitsets.append(h)
        if not h:
            misses.append(t)
    return misses, hitsets


def longest_chain(hitsets, B):
    """Maior run de escalas consecutivas t..t+L-1 com escolha a_t em
    hitsets[t], monotono com incrementos em [0,B] (DP sobre conjuntos
    alcancaveis) -- o objeto com conteudo de rigidez real."""
    best = 0
    n = len(hitsets)
    t0 = 0
    while t0 < n:
        if not hitsets[t0]:
            t0 += 1
            continue
        reach = set(hitsets[t0])
        L = 1
        t = t0 + 1
        while t < n and hitsets[t]:
            nxt = set()
            hs = set(hitsets[t])
            for a in reach:
                for g in range(0, B + 1):
                    if a + g in hs:
                        nxt.add(a + g)
            if not nxt:
                break
            reach = nxt
            L += 1
            t += 1
        best = max(best, L)
        t0 += 1
    return best


if __name__ == "__main__":
    S = 300
    for delta in (1 / 6, 1 / 10, 1 / 30):
        B = math.floor(math.log2(1 / (2 * delta)))
        print(f"\n=== delta = {delta:.4f}  (B = incremento max encadeavel = {B}) ===")
        xis = [1, 5, 7]
        for _ in range(5):
            x = random.getrandbits(200)
            while x % 3 == 0:
                x += 1
            xis.append(x)
        for xi in xis:
            misses, hitsets = diag_profile(xi, S, GAMMA, delta)
            frac = 1 - len(misses) / S
            chain = longest_chain(hitsets, B)
            tail_miss = [t for t in misses if t > 50]
            label = str(xi) if xi < 10**6 else f"random~2^200 ({str(xi)[:8]}...)"
            print(f"xi = {label:28s} fracao de escalas com hit: {frac:6.3f}  "
                  f"misses t>50: {len(tail_miss):3d}  maior run encadeavel: {chain}")
        print(f"log(S) = {math.log(S):.1f}  -- comparar com 'maior run encadeavel'")
