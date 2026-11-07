"""Grafica la pobreza monetaria de la ENAHO 2024 por área, sexo o grupo de edad.

Se corre desde la raíz del repositorio:
    uv run .claude/skills/graficando-enaho/scripts/graficar.py --por area
"""
import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

BASE = Path("salidas/personas_2024.parquet")
COLOR = "#B5441B"  # un solo color para todas las barras
ETIQUETAS = {"area": "área", "sexo": "sexo", "edad": "grupo de edad"}

parser = argparse.ArgumentParser()
parser.add_argument("--por", choices=["area", "sexo", "edad"], default="area")
por = parser.parse_args().por

if not BASE.exists():
    raise SystemExit(f"Falta {BASE}. Usa primero la skill limpiando-enaho.")

base = pd.read_parquet(BASE)
base["area"] = base.urbano.map({True: "Urbana", False: "Rural"})
base["sexo"] = base.p207.map({1: "Hombre", 2: "Mujer"})
# Grupos de edad fijos, para que el gráfico salga siempre igual
base["edad"] = pd.cut(base.p208a, [-1, 17, 29, 44, 59, 200],
                      labels=["0-17", "18-29", "30-44", "45-59", "60+"])

# Se pondera con facpob07: nunca se cuentan encuestas
base["pobre_w"] = base.pobre * base.facpob07
g = base.groupby(por, observed=True)[["pobre_w", "facpob07"]].sum()
tasa = (100 * g.pobre_w / g.facpob07).astype("float64").sort_values()  # facpob07 llega en float32

fig, ax = plt.subplots(figsize=(7, 4))
barras = ax.barh(tasa.index.astype(str), tasa.values, color=COLOR)
ax.bar_label(barras, fmt="%.1f %%", padding=3)
ax.set_xlim(0, tasa.max() * 1.15)  # empieza en cero
ax.set_xlabel("% de personas en pobreza monetaria")
ax.set_title(f"Pobreza monetaria por {ETIQUETAS[por]}, 2024")
fig.text(0.01, 0.01, "Fuente: INEI, ENAHO 2024", fontsize=8)

Path("figuras").mkdir(exist_ok=True)
fig.savefig(f"figuras/pobreza_{por}.png", dpi=200, bbox_inches="tight")
print(tasa.round(1).to_string())
