"""Mapea la pobreza monetaria de la ENAHO 2024 por departamento.

Se corre desde la raíz del repositorio:
    uv run .claude/skills/mapeando-enaho/scripts/mapear.py
"""
from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

BASE = Path("salidas/personas_2024.parquet")
GEOJSON = Path("datos/peru_departamental_simple.geojson")

if not BASE.exists():
    raise SystemExit(f"Falta {BASE}. Usa primero la skill limpiando-enaho.")
if not GEOJSON.exists():
    raise SystemExit(f"Falta {GEOJSON}. Descárgalo del repositorio del curso (ver README).")

# Pobreza ponderada con facpob07 por código de departamento (ubigeo[:2])
base = pd.read_parquet(BASE)
base["pobre_w"] = base.pobre * base.facpob07
g = base.groupby("departamento")[["pobre_w", "facpob07"]].sum()
pobreza = ((100 * g.pobre_w / g.facpob07).astype("float64")  # facpob07 llega en float32
           .rename("pobreza").reset_index())
assert len(pobreza) == 25, f"la base tiene {len(pobreza)} departamentos, deben ser 25"

# Se une por código, nunca por nombre: «APURIMAC» no es «Apurímac»
mapa = gpd.read_file(GEOJSON)
mapa["departamento"] = mapa.FIRST_IDDP.astype(str).str.zfill(2)
mapa = mapa.merge(pobreza, on="departamento", how="left", validate="1:1")
assert len(mapa) == 25, f"hay {len(mapa)} departamentos, deben ser 25"
assert mapa.pobreza.notna().all(), "hay departamentos sin dato: revisa la unión"
assert {"07", "15"} <= set(mapa.departamento), "Lima (15) y Callao (07) van separados"

# Un solo color de claro a oscuro, desde 0; nunca arcoíris
fig, ax = plt.subplots(figsize=(7, 9))
mapa.plot(column="pobreza", cmap="Oranges", vmin=0, legend=True,
          edgecolor="white", linewidth=0.5, ax=ax,
          legend_kwds={"label": "Pobreza monetaria (% de personas)"})
ax.set_axis_off()
ax.set_title("Pobreza monetaria por departamento, 2024")
fig.text(0.01, 0.01, "Fuente: INEI, ENAHO 2024", fontsize=8)

Path("mapas").mkdir(exist_ok=True)
fig.savefig("mapas/pobreza_departamento.png", dpi=200, bbox_inches="tight")
salida = mapa[["departamento", "NOMBDEP", "pobreza"]].sort_values("pobreza", ascending=False)
print(salida.round(1).to_string(index=False))
