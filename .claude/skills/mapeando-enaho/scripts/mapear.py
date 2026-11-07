"""Mapea la pobreza monetaria de la ENAHO 2024 por departamento y la compara con la referencia de la Sesión 16.

Se corre desde la raíz del repositorio:
    uv run .claude/skills/mapeando-enaho/scripts/mapear.py

Lee el nivel «departamento» de salidas/indicadores.csv (producido por limpiando-enaho, ya ponderado) y lo une con
el GeoJSON del curso por código: ubigeo[:2] con FIRST_IDDP, nunca por nombre.
"""
import sys
from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
INDICADORES = Path("salidas/indicadores.csv")
GEOJSON = Path("datos/peru_departamental_simple.geojson")
REFERENCIA = Path("referencias/pobreza_departamento_2024.csv")   # Sesión 16 del repositorio del curso
TOLERANCIA = 0.1   # puntos porcentuales frente a la referencia, que viene redondeada a un decimal

if not INDICADORES.exists():
    raise SystemExit(f"Falta {INDICADORES}. Usa primero la skill limpiando-enaho.")
if not GEOJSON.exists():
    raise SystemExit(f"Falta {GEOJSON}. Descárgalo del repositorio del curso (ver README).")

tabla = pd.read_csv(INDICADORES, dtype={"codigo": str})
anio = int(tabla.anio.iloc[0])
pobreza = (tabla[tabla.nivel == "departamento"][["codigo", "nombre", "pobreza_pct", "muestra"]]
           .rename(columns={"codigo": "departamento"}))
assert len(pobreza) == 25, f"indicadores.csv trae {len(pobreza)} departamentos; deben ser 25"

# Unión por código: «APURIMAC» en el mapa no es «Apurímac» en la tabla
mapa = gpd.read_file(GEOJSON)
mapa["departamento"] = mapa.FIRST_IDDP.astype(str).str.zfill(2)
mapa = mapa.merge(pobreza, on="departamento", how="left", validate="1:1")
assert len(mapa) == 25, f"el mapa tiene {len(mapa)} unidades; deben ser 25"
assert mapa.pobreza_pct.notna().all(), "hay departamentos sin dato: revisa la unión por código"
assert {"07", "15"} <= set(mapa.departamento), "Lima (15) y Callao (07) deben estar separados"

# Comparación con la referencia de la Sesión 16, también por código
comparacion = pd.DataFrame()
if REFERENCIA.exists():
    ref = pd.read_csv(REFERENCIA, dtype={"ccdd": str}).rename(columns={
        "departamento": "nombre_referencia", "ccdd": "departamento", "pobreza_pct": "referencia_pct"})
    comparacion = pobreza.merge(ref[["departamento", "referencia_pct"]], on="departamento", how="outer",
                                validate="1:1", indicator=True)
    comparacion["calculado_pct"] = comparacion.pobreza_pct.round(1)
    comparacion["diferencia"] = (comparacion.calculado_pct - comparacion.referencia_pct).round(2)
    comparacion["coincide"] = comparacion.diferencia.abs() <= TOLERANCIA
    comparacion = comparacion[["departamento", "nombre", "calculado_pct", "referencia_pct", "diferencia",
                               "coincide", "muestra"]]
    Path("salidas").mkdir(exist_ok=True)
    comparacion.to_csv("salidas/comparacion_mapa.csv", index=False, encoding="utf-8")
    assert len(comparacion) == 25, "la referencia y el cálculo no tienen los mismos 25 códigos"
    if not comparacion.coincide.all():
        print(comparacion[~comparacion.coincide].to_string(index=False))
        raise SystemExit("ERROR: hay departamentos que difieren de la referencia de la Sesión 16 en más de "
                         f"{TOLERANCIA} puntos; se debe revisar la ponderación antes de usar el mapa.")
else:
    print(f"Aviso: no está {REFERENCIA}; el mapa se genera sin comparar con la referencia.")

# Título analítico con los datos; un solo tono de claro a oscuro desde 0, nunca arcoíris
orden = mapa.sort_values("pobreza_pct", ascending=False)
mayores = ", ".join(f"{f.nombre} ({f.pobreza_pct:.1f} %)" for f in orden.head(3).itertuples())
menor = orden.iloc[-1]
fig, ax = plt.subplots(figsize=(7, 9.2))
mapa.plot(column="pobreza_pct", cmap="Oranges", vmin=0, legend=True, edgecolor="white", linewidth=0.6, ax=ax,
          legend_kwds={"label": "Pobreza monetaria (% de personas)", "shrink": 0.6})
for f in mapa.itertuples():   # valor en cada departamento, legible sobre claro u oscuro
    punto = f.geometry.representative_point()
    color = "white" if f.pobreza_pct >= 33 else "#333333"
    if f.departamento == "07":   # Callao es muy pequeño: su etiqueta va al mar, con una línea guía
        ax.annotate(f"Callao {f.pobreza_pct:.0f}", (punto.x, punto.y), xytext=(punto.x - 2.2, punto.y - 0.4),
                    fontsize=7, color="#333333", ha="center",
                    arrowprops={"arrowstyle": "-", "color": "#555555", "linewidth": 0.6})
    else:
        ax.annotate(f"{f.pobreza_pct:.0f}", (punto.x, punto.y), ha="center", va="center", fontsize=7, color=color)
ax.set_axis_off()
ax.text(0, 1.06, f"La pobreza se concentra en {mayores.rsplit(', ', 1)[0]} y {mayores.rsplit(', ', 1)[1]}",
        transform=ax.transAxes, fontsize=11, fontweight="bold")
ax.text(0, 1.025, f"Pobreza monetaria por departamento, Perú {anio} (% de personas). Menor: {menor.nombre} "
        f"({menor.pobreza_pct:.1f} %). Lima y Callao por separado.", transform=ax.transAxes, fontsize=8.5,
        color="#555555")
ax.text(0, -0.03, f"Fuente: INEI, ENAHO {anio} (módulos 34 y 02), estimación ponderada con factor07*mieperho. "
        "Límites: repositorio del curso.\nUnión por código (ubigeo[:2] = FIRST_IDDP). Elaboración propia.",
        transform=ax.transAxes, fontsize=7, color="#555555", va="top")

Path("mapas").mkdir(exist_ok=True)
fig.savefig("mapas/pobreza_departamento.png", dpi=200, bbox_inches="tight")
print(f"mapas/pobreza_departamento.png · 25 de 25 departamentos unidos por código")
if not comparacion.empty:
    print(f"Comparación con la Sesión 16: {comparacion.coincide.sum()} de 25 coinciden "
          f"(diferencia máxima {comparacion.diferencia.abs().max():.2f} puntos) -> salidas/comparacion_mapa.csv")
print(orden[["departamento", "nombre", "pobreza_pct"]].round(1).to_string(index=False))
