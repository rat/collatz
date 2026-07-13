#!/usr/bin/env python3
"""
E-032 - Testa H-032: os pontos onde a anomalia/inversao de H-013 ocorre
(t=4/5, 7/8, 10/11, 13/14) se correlacionam com a qualidade da
aproximacao racional de log2(3) nesses t (via fracao continua)?

Motivacao: convergentes de log2(3) sao a ferramenta classica usada para
limites de comprimento de ciclo (Simons & de Weger), e o mecanismo de
H-018 (orcamento de bits log2(n_max/J_t) encolhendo 2 bits por t) tem
log2(3) como constante aditiva. Pergunta: a proximidade de t*log2(3) a
um inteiro (medida classica de "boa aproximacao", ligada aos
convergentes) explica a direcao da anomalia em cada par flagged?

Reproduzir: python3 experiment.py
"""
from decimal import Decimal, getcontext

getcontext().prec = 30


def main():
    log2_3 = Decimal(3).ln() / Decimal(2).ln()

    flagged_pairs = [(4, 5, "anomalia p5>p4"),
                     (7, 8, "anomalia p8>p7"),
                     (10, 11, "inversao"),
                     (13, 14, "inversao")]

    print("Testando se dist(t*log2(3), inteiro mais proximo) correlaciona")
    print("com a direcao da anomalia/inversao documentada em H-013/H-018:\n")

    for t1, t2, label in flagged_pairs:
        d1 = dist_to_int(t1 * log2_3)
        d2 = dist_to_int(t2 * log2_3)
        closer = t1 if d1 < d2 else t2
        print(f"par ({t1},{t2}) [{label}]: dist({t1})={float(d1):.4f}, "
              f"dist({t2})={float(d2):.4f}  -> mais proximo de inteiro: t={closer}")

    print("\n=> Se houvesse correlacao real, pares do MESMO tipo (anomalia vs")
    print("   inversao) deveriam mostrar o mesmo padrao (sempre 'primeiro mais")
    print("   proximo' ou sempre 'segundo mais proximo'). Checar manualmente:")
    print("   anomalia (4,5): segundo mais proximo. anomalia (7,8): PRIMEIRO mais proximo.")
    print("   => padroes OPOSTOS dentro do mesmo tipo -- SEM correlacao consistente.")


def dist_to_int(x):
    frac = x - int(x)
    return min(frac, 1 - frac)


if __name__ == "__main__":
    main()
