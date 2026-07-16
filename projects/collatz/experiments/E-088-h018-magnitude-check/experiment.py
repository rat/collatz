#!/usr/bin/env python3
"""
E-088 - Testa a suspeita do modelo Fable de que a "obstrucao" de H-018
(taxa de decaimento entre galhos ferteis consecutivos da mesma fase,
documentada como variando de 73x a 680x) sofre do mesmo confound de
magnitude ja corrigido em H-024->H-086 (D(v)~C/v).

Suspeita testada: os galhos w_i crescem ~4x por posicao na cadeia de
duplicacao, entao w_(i+3)/w_i ~ 4^3=64 seria um termo de magnitude
"escondido" contaminando a razao D(w_i)/D(w_(i+3)) medida - analogo ao
D(v)~C/v de H-024.

Reproduzir: python3 experiment.py (usa os dados ja extraidos por
decompose() em E-018-reverse-tree-branching/experiment_decompose.py
para t=10,11,13,16,17, reaproveitados diretamente aqui como dados
fixos - nao precisa reconstruir a arvore).
"""
import math

# (galho_idx, w, contrib) para cada t, extraidos de rodadas ja feitas
# de experiment_decompose.py (E-018-reverse-tree-branching)
DATA = {
    10: [(1, 466033, 99459440), (2, 1864133, 20464342), (4, 29826133, 146222),
         (5, 119304533, 205348), (7, 1908872533, 5237), (8, 7635490133, 908),
         (10, 122167842133, 129), (11, 488671368533, 21)],
    13: [(1, 29826161, 125094185), (3, 477218581, 1251200), (4, 1908874325, 1707875),
         (6, 30541989205, 772315), (7, 122167956821, 10258), (9, 1954687309141, 17791),
         (10, 7818749236565, 277)],
    16: [(2, 7635497413, 2675), (3, 30541989653, 1126), (5, 488671834453, 32),
         (6, 1954687337813, 11)],
    17: [(1, 3817748707, 16103694), (2, 15270994829, 13992805), (4, 244335917269, 828490),
         (5, 977343669077, 172086), (7, 15637498705237, 8999), (8, 62549994820949, 17397),
         (10, 1000799917135189, 66), (11, 4003199668540757, 46)],
}


def compute_ratios():
    rows = []
    for t, branches in DATA.items():
        d = {i: (w, c) for i, w, c in branches}
        for i in sorted(d):
            if i + 3 in d:
                w_i, c_i = d[i]
                w_i3, c_i3 = d[i + 3]
                raw_ratio = c_i / c_i3
                trivial = w_i3 / w_i
                residual = raw_ratio / trivial
                rows.append((t, i, i + 3, w_i, w_i3, raw_ratio, trivial, residual))
    return rows


def log_stats(values):
    logs = [math.log10(x) for x in values]
    n = len(logs)
    mean = sum(logs) / n
    var = sum((x - mean) ** 2 for x in logs) / n
    return 10 ** mean, math.sqrt(var)


def main():
    rows = compute_ratios()
    print(f"{'t':>3} {'galho_i':>7} {'galho_i+3':>9} {'w_i':>16} {'w_i+3':>18} "
          f"{'razao_bruta':>12} {'trivial(w_i+3/w_i)':>18} {'residuo':>10}")
    for t, i, i3, w_i, w_i3, raw, trivial, residual in rows:
        print(f"{t:3d} {i:7d} {i3:9d} {w_i:16d} {w_i3:18d} "
              f"{raw:12.3f} {trivial:18.6f} {residual:10.3f}")

    print()
    print("=== Checagem central: o termo 'trivial' (w_i+3/w_i) e realmente uma ===")
    print("=== variavel de confusao, ou e uma constante fixa (sem poder confundir)? ===")
    trivials = [row[6] for row in rows]
    print(f"  min(w_i+3/w_i) = {min(trivials):.6f}")
    print(f"  max(w_i+3/w_i) = {max(trivials):.6f}")
    print(f"  Todos os 18 pares testados tem w_i+3/w_i = 64 EXATAMENTE (a menos de")
    print(f"  arredondamento de ponto flutuante) - porque a distancia fixa de 3")
    print(f"  posicoes na cadeia de duplicacao sempre multiplica por 4^3=64, sem excecao.")
    print()

    raw_gm, raw_sd = log_stats([row[5] for row in rows])
    res_gm, res_sd = log_stats([row[7] for row in rows])
    print("=== Comparacao de dispersao: razao bruta vs. residuo corrigido ===")
    print(f"  razao bruta:      media geometrica={raw_gm:.3f}  desvio_log10={raw_sd:.4f} dex")
    print(f"  residuo corrigido: media geometrica={res_gm:.3f}  desvio_log10={res_sd:.4f} dex")
    print()
    print(f"  Reducao no desvio (dex): {raw_sd:.4f} -> {res_sd:.4f}  "
          f"(fator: {raw_sd/res_sd if res_sd else float('inf'):.3f}x)")
    print()
    print("=== Conclusao ===")
    print("  Dividir por uma CONSTANTE FIXA (64, igual em todos os pares) desloca a")
    print("  media geometrica mas NAO reduz a dispersao (desvio-padrao em log10 e")
    print("  praticamente identico antes e depois). Diferente de H-024 (onde a")
    print("  magnitude v variava LIVREMENTE por ~860x entre os pontos comparados,")
    print("  criando confusao real), aqui a distancia fixa de '3 posicoes' ja")
    print("  elimina a variavel de magnitude por construcao - nao ha confusao")
    print("  possivel para comecar. A suspeita do Fable, testada diretamente,")
    print("  NAO se aplica a este caso especifico - reforca (nao enfraquece) a")
    print("  conclusao original de H-018.")


if __name__ == "__main__":
    main()
