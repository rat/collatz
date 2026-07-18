import numpy as np
rng = np.random.default_rng(42)
N = 2_000_000
G = 60

# Toy anelado do fator local da cascata: Z = sum_{g>=1} w_g e(2 pi i U_g)
# Modelo 1: pesos Geom(1/2), w_g = 2^{-g}  (modelo i.i.d. de Tao, Syrac)
# Modelo 2: pesos Geom tilted, media gamma0 = 1 + log_4 3 (limiar WCC): p = 1/gamma0
log3 = np.log(3.0)

def run(p_geom, label):
    g = np.arange(1, G+1)
    w = p_geom * (1-p_geom)**(g-1)
    w = w / w.sum()
    tot_logs = []
    # E|Z|^2 exato = sum w_g^2
    ez2 = (w**2).sum()
    for chunk in range(4):
        U = rng.random((N//4, G))
        Z = (w * np.exp(2j*np.pi*U)).sum(axis=1)
        tot_logs.append(np.log(1.0/np.abs(Z)))
    L = np.concatenate(tot_logs)
    lam = L.mean(); se = L.std()/np.sqrt(len(L))
    print(f"{label}: p={p_geom:.4f}  E|Z|^2={ez2:.5f}  (1/2)log(1/E|Z|^2)={0.5*np.log(1/ez2):.4f}")
    print(f"   Lambda = E log(1/|Z|) = {lam:.4f} +/- {2*se:.4f}   vs  log 3 = {log3:.4f}")
    print(f"   veredito anelado: {'Lambda > log3 (forca estrutura)' if lam - 2*se > log3 else 'Lambda < log3 (orcamento cabe sem estrutura)' if lam + 2*se < log3 else 'indeterminado'}")
    return lam

run(0.5, "Modelo 1 (Geom(1/2), Syrac de Tao)")
gamma0 = 1 + np.log(3)/np.log(4)
run(1.0/gamma0, f"Modelo 2 (tilted, media {gamma0:.4f}, limiar WCC)")
