"""
E-103 Estagio 6 (parte 2) -- roda a mesma bateria de 4 estimadores
(full_battery.py) na amostra grande de 100.000 raizes gerada por
stage6_large_sample_generation.py (20x a Rodada 1/2, que usava 5000).
"""
import json
import sys
sys.path.insert(0, ".")
from full_battery import run_all

with open("/tmp/tail_index_q5_large_sample.json") as f:
    data = json.load(f)

all_results = {}
for H_str, W in data["W_by_level"].items():
    all_results[H_str] = run_all(W, f"H={float(H_str):.0e} (AMOSTRA GRANDE, n=100000)")

with open("stage6_large_sample_battery_results.json", "w") as f:
    json.dump(all_results, f, indent=2, default=str)
print("\nResultados salvos em stage6_large_sample_battery_results.json")
