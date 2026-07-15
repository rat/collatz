"""
E-039 - Calculo explicito da "pressao residual" de Ruiz Castillo (paper #001
da colecao Google Scholar) para o observavel de dissipacao real do Collatz.

O paper (item 001, literature/papers/INDEX.md, PDF em
literature/papers/001_Geometria-Residual-Ruiz-Castillo.pdf) define
phi(a) = a - log2(3) como o
"potencial disipativo" e P_RC(t) = sup_mu {H_RC(mu) - t*D_RC(mu)} como a
"pressao residual", mas NUNCA calcula isso explicitamente - toda a analise
fica em nivel de "SE P_RC for convexa, ENTAO...". Este script faz o calculo
que o paper nao faz, usando o modelo i.i.d. padrao (a ~ Geometrica(1/2),
ja estabelecido em H-001/H-011 deste projeto) para o observavel real.
"""
import sympy as sp

t = sp.symbols('t', real=True)
log2_3 = sp.log(3, 2)


def compute():
    # funcao geradora de cumulantes de phi(a) = a - log2(3), a ~ Geometrica(1/2) i.i.d.
    # E[e^{t a}] = sum_{k=1}^inf e^{tk} 2^{-k} = e^t/(2-e^t), para t < log(2)
    Lambda = t - t * log2_3 - sp.log(2 - sp.exp(t))
    Lambda1 = sp.diff(Lambda, t)
    Lambda2 = sp.diff(Lambda1, t)
    g = sp.simplify(Lambda2)  # "metrica residual" g_RC(t)

    log_g = sp.log(g)
    K = sp.simplify(-sp.diff(log_g, t, 2))  # "curvatura residual" K_RC(t)

    print("=== Pressao residual explicita (modelo i.i.d. Geometrica(1/2)) ===")
    print("Lambda(t) =", sp.simplify(Lambda))
    print("Dominio: t <", float(sp.log(2)), "(= log 2)")
    print()

    print("=== Verificacao cruzada contra constantes ja estabelecidas no projeto ===")
    L0, L1_0, L2_0 = Lambda.subs(t, 0), Lambda1.subs(t, 0), Lambda2.subs(t, 0)
    print(f"Lambda(0)   = {float(L0):.6f}  (esperado 0)")
    print(f"Lambda'(0)  = {float(L1_0):.6f}  (esperado E[a]-log2(3) = 2-log2(3) = {float(2-log2_3):.6f}, ver H-001)")
    print(f"Lambda''(0) = {float(L2_0):.6f}  (esperado Var[a] = 2, ver H-001/H-011)")
    print()

    print("=== Metrica residual g_RC(t) = Lambda''(t) ===")
    print("g_RC(t) =", g)
    for tt in [-2, -1, -0.5, 0, 0.3, 0.5, 0.6, 0.65]:
        print(f"  g_RC({tt:>5}) = {float(g.subs(t, tt)):.6f}")
    lim_g = sp.limit(g, t, sp.log(2), dir='-')
    print(f"  lim_{{t->log(2)^-}} g_RC(t) = {lim_g}  <-- SINGULARIDADE")
    print()

    print("=== Curvatura residual K_RC(t) = -d^2/dt^2 log(g_RC(t)) ===")
    print("K_RC(t) =", K)
    ratio = sp.simplify(K / g)
    print("K_RC(t) / g_RC(t) =", ratio, " <-- relacao exata neste modelo")
    for tt in [-2, -1, -0.5, 0, 0.3, 0.5, 0.6]:
        print(f"  K_RC({tt:>5}) = {float(K.subs(t, tt)):.6f}")
    lim_K = sp.limit(K, t, sp.log(2), dir='-')
    print(f"  lim_{{t->log(2)^-}} K_RC(t) = {lim_K}")

    return Lambda, g, K


if __name__ == "__main__":
    compute()
