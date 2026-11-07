"""Grafica la pobreza monetaria de la ENAHO 2024 por área, sexo, grupo de edad o departamento.

Se corre desde la raíz del repositorio:
    uv run .claude/skills/graficando-enaho/scripts/graficar.py --por area
    uv run .claude/skills/graficando-enaho/scripts/graficar.py --por departamento

Lee salidas/indicadores.csv, que produce la skill limpiando-enaho con las estimaciones ya ponderadas: así el
gráfico muestra exactamente las mismas cifras que se validaron. El título se arma con los datos, de modo que
siempre resume la diferencia que se ve.
"""
import argparse
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
INDICADORES = Path("salidas/indicadores.csv")
COLOR = "#B5441B"    # un solo color: es una sola serie
GRIS = "#555555"
ORDEN_EDAD = ["0-17", "18-29", "30-44", "45-59", "60+"]

parser = argparse.ArgumentParser()
parser.add_argument("--por", choices=["area", "sexo", "edad", "departamento"], default="area")
por = parser.parse_args().por

if not INDICADORES.exists():
    raise SystemExit(f"Falta {INDICADORES}. Usa primero la skill limpiando-enaho.")

tabla = pd.read_csv(INDICADORES, dtype={"codigo": str})
datos = tabla[tabla.nivel == por].copy()
nacional = tabla.loc[tabla.nivel == "nacional", "pobreza_pct"].iloc[0]
anio = int(tabla.anio.iloc[0])
ponderador = datos.ponderador.iloc[0]
if datos.empty:
    raise SystemExit(f"indicadores.csv no tiene el nivel {por!r}; vuelve a correr limpiando-enaho.")

# Orden: la edad sigue su orden natural; lo demás, de menor a mayor pobreza
if por == "edad":
    datos = datos.set_index("nombre").loc[ORDEN_EDAD[::-1]].reset_index()
else:
    datos = datos.sort_values("pobreza_pct")
alto, bajo = datos.loc[datos.pobreza_pct.idxmax()], datos.loc[datos.pobreza_pct.idxmin()]
dif = alto.pobreza_pct - bajo.pobreza_pct

# Títulos analíticos calculados con los datos
if por == "area":
    titulo = f"La pobreza rural supera a la urbana en {dif:.1f} puntos"
elif por == "sexo":
    titulo = (f"Mujeres y hombres tienen casi la misma pobreza: {dif:.1f} puntos de diferencia"
              if dif < 1 else f"La pobreza de {alto.nombre.lower()}es supera a la de {bajo.nombre.lower()}es "
                              f"en {dif:.1f} puntos")
elif por == "edad":
    titulo = (f"El grupo de {alto.nombre} años es el más pobre ({alto.pobreza_pct:.1f} %), "
              f"{dif:.1f} puntos sobre el de {bajo.nombre} años")
else:
    titulo = (f"{alto.nombre} ({alto.pobreza_pct:.1f} %) tiene {alto.pobreza_pct / bajo.pobreza_pct:.1f} veces "
              f"la pobreza de {bajo.nombre} ({bajo.pobreza_pct:.1f} %)")
etiqueta = {"area": "área de residencia", "sexo": "sexo", "edad": "grupo de edad",
            "departamento": "departamento"}[por]

alto_fig = 0.6 + 0.32 * len(datos) if por == "departamento" else 3.2
fig, ax = plt.subplots(figsize=(8, max(alto_fig, 3.2)))
ax.axvline(nacional, color=GRIS, linewidth=1, linestyle="--", zorder=0)   # detrás de barras y etiquetas
barras = ax.barh(datos.nombre, datos.pobreza_pct, color=COLOR, height=0.62, zorder=2)
etiquetas = ax.bar_label(barras, labels=[f"{v:.1f} %" for v in datos.pobreza_pct], padding=3, fontsize=9)
for e in etiquetas:
    e.set_bbox({"facecolor": "white", "edgecolor": "none", "pad": 1})
ax.set_xlim(0, datos.pobreza_pct.max() * 1.18)   # empieza en cero
ax.set_xlabel("% de personas en pobreza monetaria")
for lado in ("top", "right"):
    ax.spines[lado].set_visible(False)
ax.tick_params(axis="y", length=0)
fig.suptitle(titulo, x=0.01, ha="left", fontsize=12, fontweight="bold")
ax.set_title(f"Pobreza monetaria por {etiqueta}, Perú {anio} (% de personas). "
             f"Línea discontinua: promedio nacional ({nacional:.1f} %)", loc="left", fontsize=9, color=GRIS)
fig.text(0.01, -0.02, f"Fuente: INEI, ENAHO {anio} (módulos 34 y 02). Estimación ponderada con {ponderador}. "
         "Elaboración propia.", fontsize=8, color=GRIS)
fig.tight_layout()

Path("figuras").mkdir(exist_ok=True)
salida = Path(f"figuras/pobreza_{por}.png")
fig.savefig(salida, dpi=200, bbox_inches="tight")
print(f"{salida} · {titulo}")
print(datos[["codigo", "nombre", "pobreza_pct", "muestra"]].iloc[::-1].to_string(index=False))
