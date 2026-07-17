#!/usr/bin/env python3
"""
H-125 - teste computacional certificado da Conjectura 3 de Wirsching
(2003, "On positive predecessor density in 3n+1 dynamics", DCDS 9(3)).

Objeto: a densidade invariante phi (ponto fixo unico do operador de
medias W_3 f(x) = (3/2)*integral_{3x-2}^{3x} f(t)dt sobre [0,1]) e' o
analogo base-3 da funcao de Fabius (densidade de X = soma_j 2*U_j*3^-j,
U_j uniformes iid em [0,1] - identidade derivada pelo Fable, verificada:
X =d (2U+X)/3 reproduz exatamente a equacao de W_3).

Conjectura 3 (a mais concreta da cadeia de 3 conjecturas do Wirsching,
reduzindo densidade positiva de predecessores 3n+1): existe c>0 tal que

    liminf_{l->inf} phi(z_l)/phi_0(z_l) = c > 0

uniformemente para sequencias (z_l) na classe A_delta (janela CLT
|l - k_l| <= delta*sqrt(l)), com phi_0 a assintotica fechada de
Berg-Kruppel (1998, Proposicao 9.1, pp.178-179, item 133 do INDEX):

    phi_0(t) ~ (2*beta)^eps/sqrt(2*pi) * t^gamma * (-ln t)^delta
               * exp(-beta*ln^2(t/(-ln t)))

com (a=3, lambda=2/3, nossos parametros):
    alpha = 1/2 - ln(2)/ln(3)
    beta  = 1/(2*ln(3))
    delta = 1/2 + alpha - 2*beta*ln(2*beta)
    gamma = -2*beta - delta - 1/2
    eps   = 1/2 + alpha - beta*ln(2*beta)

Metodo (upgrade do Fable - SEM iterar W_3): os momentos M_i = E[X^i] de
phi sao RACIONAIS EXATOS via a autossimilaridade acima. Para calcular
phi(x) numa cauda extrema x~l*3^-l, reduz-se via primitivas iteradas:

    phi(x) = (3/2)^(m+1) * 3^(-m(m+1)/2) * F_{m+1}(3^(m+1)*x)

com m = maior inteiro tal que 3^m*x<=2/3, e F_j(y) = integral_0^min(y,1)
((y-t)^(j-1)/(j-1)!)*phi(t)dt. Para y em [1,2] (caso A), F_j(y) e' uma
soma binomial exata dos momentos - erro ZERO. Para y em (2/3,1) (caso
B), usa a simetria phi(t)=phi(1-t) (Berg-Kruppel Prop. 4.1) + reescala
recursiva, com cota certificada no truncamento.

Trabalha SEMPRE em log (phi decai como 3^(-l^2/2), exponenciar
destroi a precisao) - usa mpmath com dps alto.

Reproduzir: python3 experiment_conjecture3.py
"""
import math
import sys
import time
from fractions import Fraction as Fr

from mpmath import mp, mpf, log as mlog, pi as mpi

sys.set_int_max_str_digits(0)  # denominadores crescem ~N^2 digitos (N~300 -> ~10k digitos)
mp.dps = 100

LOG3 = mlog(3)
LOG2 = mlog(2)

ALPHA = mpf('0.5') - LOG2 / LOG3
BETA = 1 / (2 * LOG3)
DELTA = mpf('0.5') + ALPHA - 2 * BETA * mlog(2 * BETA)
GAMMA = -2 * BETA - DELTA - mpf('0.5')
EPS = mpf('0.5') + ALPHA - BETA * mlog(2 * BETA)


def log_phi0(x_frac):
    """ln phi_0(t) - assintotica de Berg-Kruppel (9.6), t=x_frac (Fraction) pequeno."""
    t = mpf(x_frac.numerator) / mpf(x_frac.denominator)
    lnt = mlog(t)
    ln_neglnt = mlog(-lnt)
    ln_inner = lnt - ln_neglnt  # ln(t/(-ln t))
    return (EPS * mlog(2 * BETA) - mpf('0.5') * mlog(2 * mpi)
            + GAMMA * lnt + DELTA * ln_neglnt - BETA * ln_inner ** 2)


def moments(N):
    """Momentos racionais exatos M_i=E[X^i], X=d(2U+X)/3, U~Unif[0,1] iid."""
    M = [Fr(1)]
    for i in range(1, N + 1):
        s = sum(Fr(math.comb(i, k)) * Fr(2 ** k, k + 1) * M[i - k] for k in range(1, i + 1))
        M.append(s / (3 ** i - 1))
    return M


def E_pow(M, y, n):
    """E[(y-X)^n], y racional, exato."""
    return sum(Fr(math.comb(n, i)) * (-1) ** i * y ** (n - i) * M[i] for i in range(n + 1))


def F(M, j, y, depth=80):
    """F_j(y) = int_0^min(y,1) (y-t)^(j-1)/(j-1)! phi(t) dt.
    Retorna (valor_racional, cota_de_erro_racional). y em (2/3, 2]."""
    assert Fr(2, 3) < y <= 2, f"y fora do range: {y}"
    main_num = E_pow(M, y, j - 1) / math.factorial(j - 1)
    if y >= 1:
        return main_num, Fr(0)
    if depth == 0:
        w = 1 - y
        bound = w ** (j - 1) / math.factorial(j - 1)
        return main_num, bound
    w = 1 - y
    pref = Fr(1)
    jj, ww = j, w
    while ww <= Fr(2, 3):
        pref *= Fr(3, 2) * Fr(1, 3 ** jj)
        jj += 1
        ww *= 3
    sub, suberr = F(M, jj, ww, depth - 1)
    val = main_num + (-1) ** j * pref * sub
    return val, pref * suberr


def log_phi_reduced(M, x):
    """ln phi(x) exato (mpmath), + cota de erro relativo, + (m,y) usados."""
    m = 0
    while 3 ** (m + 1) * x <= Fr(2, 3):
        m += 1
    y = 3 ** (m + 1) * x
    val, err = F(M, m + 1, y)
    logval = mlog(mpf(val.numerator) / mpf(val.denominator))
    logphi = (m + 1) * mlog(mpf(3) / 2) - mpf(m * (m + 1)) / 2 * LOG3 + logval
    rel = float(err / val) if val != 0 else float('inf')
    return logphi, rel, m, y, val


def sample_points(ell, us=(-2, -1, -0.5, 0, 0.5, 1, 2)):
    """pontos k_l = l + round(u*sqrt(l)) variando u (janela CLT, classe A_delta~2)."""
    pts = []
    for u in us:
        k = ell + round(u * math.sqrt(ell))
        if k < 1:
            continue
        x = Fr(k, 3 ** ell)
        if not (0 < x <= Fr(2, 3)):
            continue
        pts.append((u, k, x))
    return pts


def decisive_ratio(M, m, y):
    """L_l = 3^(1-l) * phi(3x+)/phi(x+) = 2*3^(m-l)*F_m(y)/F_{m+1}(y), mesmo y.
    Aqui como funcao auxiliar generica: retorna F_m(y) e F_{m+1}(y) exatos."""
    val_m, _ = F(M, m, y) if m >= 1 else (Fr(1), Fr(0))
    val_m1, _ = F(M, m + 1, y)
    return val_m, val_m1


def validate(M):
    print("=== Validacao ===")
    assert M[1] == Fr(1, 2) and M[2] == Fr(7, 24), "M1/M2 errados"
    for n in (3, 5, 7, 9):
        c = sum(Fr(math.comb(n, k)) * (Fr(-1, 2)) ** (n - k) * M[k] for k in range(n + 1))
        assert c == 0, f"momento central {n} != 0: {c}"
    print("  M1=1/2, M2=7/24 OK; momentos centrais impares (3,5,7,9) = 0 OK")
    # phi(1/2) deve ser exatamente 3/2 (Wirsching/BK)
    logphi_half, rel, m, y, val = log_phi_reduced(M, Fr(1, 2))
    phi_half = float(mp.e ** logphi_half) if logphi_half < 700 else float('inf')
    print(f"  phi(1/2) calculado = {phi_half:.10f} (esperado 1.5), rel_err_cota={rel:.1e}")
    assert abs(phi_half - 1.5) < 1e-8, "phi(1/2) deveria ser exatamente 3/2"
    print("  Validacao OK\n")


def main():
    ELL_LIST = [5, 10, 20, 30, 50, 75, 100, 150, 200, 250, 300]
    N_MAX = max(ELL_LIST) + 10

    t0 = time.time()
    print(f"Calculando momentos exatos ate M_{N_MAX}...")
    M = moments(N_MAX)
    print(f"  Momentos prontos em {time.time()-t0:.1f}s\n")

    validate(M)

    print("=== Teste da Conjectura 3: ln(phi/phi0) e razao decisiva L_l ===")
    print(f"{'ell':>5} {'u':>6} {'k_l':>8} {'m':>5} {'ln phi':>12} {'ln phi0':>12} "
          f"{'ln r':>10} {'L_l=phi(3x)/phi(x)*3^(1-l)':>28} {'rel_err':>10} {'tempo':>8}")

    for ell in ELL_LIST:
        for u, k, x in sample_points(ell):
            t1 = time.time()
            logphi, rel, m, y, val = log_phi_reduced(M, x)
            lp0 = log_phi0(x)
            lnr = float(logphi - lp0)

            # razao decisiva L_l: phi(3x)/phi(x) usa o MESMO y, so muda m->m-1
            # phi(x) = (3/2)^(m+1) 3^(-m(m+1)/2) F_{m+1}(y)
            # phi(3x)=(3/2)^m 3^(-(m-1)m/2) F_m(y)  [profundidade m-1 para 3x]
            if m >= 1:
                val_m, _ = F(M, m, y)
                # phi(3x)/phi(x) = [ (3/2)^m 3^{-m(m-1)/2} F_m(y) ] / [ (3/2)^{m+1} 3^{-m(m+1)/2} F_{m+1}(y) ]
                #               = (2/3) * 3^{m} * F_m(y)/F_{m+1}(y)
                log_ratio_33 = mlog(mpf(2) / 3) + m * LOG3 + mlog(mpf(val_m.numerator) / mpf(val_m.denominator)) \
                               - mlog(mpf(val.numerator) / mpf(val.denominator))
                log_Ll = log_ratio_33 + (1 - ell) * LOG3
                Ll = float(mp.e ** log_Ll) if abs(log_Ll) < 700 else float('inf') * (1 if log_Ll > 0 else -1)
            else:
                Ll = float('nan')

            dt = time.time() - t1
            print(f"{ell:5d} {u:6.1f} {k:8d} {m:5d} {float(logphi):12.3f} {float(lp0):12.3f} "
                  f"{lnr:10.4f} {Ll:28.6f} {rel:10.2e} {dt:8.2f}s", flush=True)

    print(f"\n=== Concluido em {time.time()-t0:.1f}s ===")
    print("Conjectura 3: ln r deve convergir (ou oscilar limitado) - nao divergir a -inf/+inf")
    print("Teste decisivo (⋆5): L_l deve ter limsup < 1 (previsao via phi_0: L_l -> 2/3)")


if __name__ == "__main__":
    main()
