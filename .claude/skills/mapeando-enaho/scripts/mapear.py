"""Mapea la pobreza monetaria de la ENAHO 2024 por departamento y la compara con la referencia de la Sesión 16.

Se corre desde la raíz del repositorio:
    uv run .claude/skills/mapeando-enaho/scripts/mapear.py

Lee el nivel «departamento» de salidas/indicadores.csv (producido por limpiando-enaho, ya ponderado) y lo une con
el GeoJSON del curso por código: ubigeo[:2] con FIRST_IDDP, nunca por nombre. El mapa usa cuatro rangos fijos
(menos de 15 %, 15 a 25 %, 25 a 35 % y 35 % o más), un recuadro ampliado de Lima y Callao y un panel con los
departamentos de mayor y menor pobreza.
"""
import sys
from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Rectangle

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "recursos"))
from estilo import ACENTO, CLASES, GRIS, TINTA, aplicar, clase, encabezado, pie  # noqa: E402

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

# 1. Unión por código: «APURIMAC» en el mapa no es «Apurímac» en la tabla
mapa = gpd.read_file(GEOJSON)
mapa["departamento"] = mapa.FIRST_IDDP.astype(str).str.zfill(2)
mapa = mapa.merge(pobreza, on="departamento", how="left", validate="1:1")
assert len(mapa) == 25, f"el mapa tiene {len(mapa)} unidades; deben ser 25"
assert mapa.pobreza_pct.notna().all(), "hay departamentos sin dato: revisa la unión por código"
assert {"07", "15"} <= set(mapa.departamento), "Lima (15) y Callao (07) deben estar separados"

# 2. Comparación con la referencia de la Sesión 16, también por código
comparacion = pd.DataFrame()
if REFERENCIA.exists():
    ref = pd.read_csv(REFERENCIA, dtype={"ccdd": str}).rename(columns={
        "departamento": "nombre_referencia", "ccdd": "departamento", "pobreza_pct": "referencia_pct"})
    comparacion = pobreza.merge(ref[["departamento", "referencia_pct"]], on="departamento", how="outer",
                                validate="1:1")
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

# 3. Mapa por rangos fijos; título calculado con los tres departamentos de mayor pobreza
TITULO = aplicar()
mapa["color"] = mapa.pobreza_pct.map(clase)
orden = mapa.sort_values("pobreza_pct", ascending=False)
top = orden.nombre.head(3).tolist()
fig = plt.figure(figsize=(10, 10.5))
encabezado(fig, f"{top[0]}, {top[1]} y {top[2]} tienen la mayor pobreza monetaria del país",
           f"Pobreza monetaria por departamento, Perú {anio} (% de personas). 25 departamentos; Lima y Callao "
           "separados.", TITULO)
ax = fig.add_axes([0.02, 0.06, 0.62, 0.82])
mapa.plot(color=mapa.color, edgecolor="white", linewidth=0.7, ax=ax)
for f in mapa.itertuples():
    if f.departamento in ("07", "15"):   # van en el recuadro ampliado
        continue
    p = f.geometry.representative_point()
    ax.text(p.x, p.y, f"{f.pobreza_pct:.0f}", ha="center", va="center", fontsize=8, fontweight="bold",
            color="white" if f.pobreza_pct >= 25 else TINTA)
ax.set_axis_off()

# Recuadro: Lima y Callao ampliados, con su valor exacto
ins = fig.add_axes([0.03, 0.08, 0.2, 0.2])
mapa.plot(color=mapa.color, edgecolor="white", linewidth=0.8, ax=ins)
x0, y0, x1, y1 = mapa[mapa.departamento == "07"].total_bounds
ins.set_xlim(x0 - 0.9, x1 + 0.9)
ins.set_ylim(y0 - 0.7, y1 + 0.7)
ins.set_xticks([])
ins.set_yticks([])
ins.set_xlabel("")
ins.set_ylabel("")
for s in ins.spines.values():
    s.set_edgecolor(GRIS)
for f in mapa[mapa.departamento.isin(["07", "15"])].itertuples():
    if f.departamento == "07":
        p = f.geometry.representative_point()
        ins.annotate(f"Callao {f.pobreza_pct:.1f}", (p.x, p.y), xytext=(p.x - 0.75, p.y + 0.35), fontsize=7.5,
                     color=TINTA, fontweight="bold", arrowprops={"arrowstyle": "-", "color": GRIS, "linewidth": 0.6})
    else:
        ins.text(x1 + 0.1, y0 - 0.1, f"Lima {f.pobreza_pct:.1f}", fontsize=7.5, color="white", fontweight="bold")
ins.set_title("Lima y Callao", fontsize=8, color=GRIS, loc="left")

# Leyenda de rangos con cuántos departamentos hay en cada uno
lx = fig.add_axes([0.66, 0.58, 0.3, 0.27])
lx.axis("off")
lx.text(0, 1.0, "% de personas en pobreza", fontsize=10, color=TINTA, fontweight="bold", va="top")
for i, (lo, hi, c) in enumerate(reversed(CLASES)):
    n = int(((mapa.pobreza_pct >= lo) & (mapa.pobreza_pct < hi)).sum())
    y = 0.78 - i * 0.2
    lx.add_patch(Rectangle((0, y), 0.12, 0.13, color=c, transform=lx.transAxes))
    rango = f"{lo} % o más" if hi == 100 else f"{lo} a menos de {hi} %"
    lx.text(0.17, y + 0.065, f"{rango}  ·  {n} dptos.", va="center", fontsize=9.5, color=TINTA)

# Panel con los tres de mayor y menor pobreza
rx = fig.add_axes([0.66, 0.2, 0.3, 0.33])
rx.axis("off")
for titulo, color_titulo, filas, y0_panel in (("Mayor pobreza", ACENTO, orden.head(3), 1.0),
                                              ("Menor pobreza", GRIS, orden.tail(3).iloc[::-1], 0.45)):
    rx.text(0, y0_panel, titulo, color=color_titulo, fontweight="bold", fontsize=10, va="top")
    for i, f in enumerate(filas.itertuples()):
        y = y0_panel - 0.12 - i * 0.1
        rx.text(0, y, f.nombre, fontsize=9.5, color=TINTA, va="top")
        rx.text(0.75, y, f"{f.pobreza_pct:.1f} %", fontsize=9.5, color=TINTA, va="top", ha="right")
pie(fig, f"Fuente: INEI, ENAHO {anio} (módulos 34 y 02). Estimación ponderada con factor07 × mieperho. "
    "Elaboración propia.\nUnión por código (ubigeo[:2] = FIRST_IDDP). Límites departamentales: repositorio del "
    "curso.")

Path("mapas").mkdir(exist_ok=True)
fig.savefig("mapas/pobreza_departamento.png", dpi=200)
print("mapas/pobreza_departamento.png · 25 de 25 departamentos unidos por código")
if not comparacion.empty:
    print(f"Comparación con la Sesión 16: {comparacion.coincide.sum()} de 25 coinciden "
          f"(diferencia máxima {comparacion.diferencia.abs().max():.2f} puntos) -> salidas/comparacion_mapa.csv")
print(orden[["departamento", "nombre", "pobreza_pct"]].round(1).to_string(index=False))
