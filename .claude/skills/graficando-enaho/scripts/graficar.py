"""Grafica la pobreza monetaria de la ENAHO 2024 por área, sexo, grupo de edad o departamento.

Se corre desde la raíz del repositorio:
    uv run .claude/skills/graficando-enaho/scripts/graficar.py --por area
    uv run .claude/skills/graficando-enaho/scripts/graficar.py --por departamento

Lee salidas/indicadores.csv, que produce la skill limpiando-enaho con las estimaciones ya ponderadas: así el
gráfico muestra exactamente las mismas cifras que se validaron. Los títulos se calculan con los datos.
Formas: área = cuadrícula «de cada 100 personas»; sexo y edad = columnas; departamento = distancia de cada uno al
promedio nacional.
"""
import argparse
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Rectangle

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "recursos"))
from estilo import ACENTO, APAGADO, GRIS, LINEA, TINTA, aplicar, encabezado, fraccion, pie  # noqa: E402

INDICADORES = Path("salidas/indicadores.csv")
ORDEN_EDAD = ["0-17", "18-29", "30-44", "45-59", "60+"]

parser = argparse.ArgumentParser()
parser.add_argument("--por", choices=["area", "sexo", "edad", "departamento"], default="area")
por = parser.parse_args().por

if not INDICADORES.exists():
    raise SystemExit(f"Falta {INDICADORES}. Usa primero la skill limpiando-enaho.")

tabla = pd.read_csv(INDICADORES, dtype={"codigo": str})
datos = tabla[tabla.nivel == por].copy()
if datos.empty:
    raise SystemExit(f"indicadores.csv no tiene el nivel {por!r}; vuelve a correr limpiando-enaho.")
nacional = tabla.loc[tabla.nivel == "nacional", "pobreza_pct"].iloc[0]
anio = int(tabla.anio.iloc[0])
ponderador = datos.ponderador.iloc[0].replace("*", " × ")
fuente = (f"Fuente: INEI, ENAHO {anio} (módulos 34 y 02). Estimación ponderada con {ponderador}. "
          "Elaboración propia.")
TITULO = aplicar()


def sin_bordes(ax, *lados):
    for lado in lados:
        ax.spines[lado].set_visible(False)


def area():
    """Cuadrícula de 10 x 10 por área: cada cuadro es 1 % de la población del área."""
    a = datos.set_index("codigo")
    pobres = a.pobreza_pct / 100 * a.poblacion
    urbano = 100 * pobres["Urbana"] / pobres.sum()
    fig = plt.figure(figsize=(9, 5.2))
    encabezado(fig, f"En el área rural, {fraccion(a.loc['Rural', 'pobreza_pct'])} personas son pobres; "
                    f"en la urbana, {fraccion(a.loc['Urbana', 'pobreza_pct'])}",
               f"Pobreza monetaria por área de residencia, Perú {anio}. Cada cuadro = 1 % de la población del área.",
               TITULO)
    for i, nombre in enumerate(["Rural", "Urbana"]):
        x = 0.08 + i * 0.47
        ax = fig.add_axes([x, 0.2, 0.36, 0.47])
        pct = a.loc[nombre, "pobreza_pct"]
        for k in range(100):
            fila, col = divmod(k, 10)
            ax.add_patch(Rectangle((col, 9 - fila), 0.84, 0.84, color=ACENTO if k < round(pct) else LINEA))
        ax.set_xlim(-0.1, 10)
        ax.set_ylim(-0.1, 10)
        ax.set_aspect("equal")
        ax.axis("off")
        fig.text(x, 0.70, f"{pct:.1f} %", fontproperties=TITULO, color=ACENTO, fontsize=22)
        fig.text(x + 0.15, 0.71, f"Área {nombre.lower()}", color=TINTA, fontsize=12, fontweight="bold")
        fig.text(x, 0.155, f"{pobres[nombre] / 1e6:.1f} millones de personas pobres · "
                 f"{a.loc[nombre, 'muestra']:,} hogares encuestados", color=GRIS, fontsize=8.5)
    mayor = "rural" if a.loc["Rural", "pobreza_pct"] > a.loc["Urbana", "pobreza_pct"] else "urbana"
    fig.text(0.04, 0.085, f"Aunque la tasa {mayor} es mayor, {urbano:.0f} % de las personas pobres vive en zonas "
             f"urbanas. Promedio nacional: {nacional:.1f} %.", color=TINTA, fontsize=9.5)
    pie(fig, fuente)
    return fig, (f"Rural {a.loc['Rural', 'pobreza_pct']:.1f} %, urbana {a.loc['Urbana', 'pobreza_pct']:.1f} %; "
                 f"{urbano:.0f} % de las personas pobres vive en zonas urbanas")


def columnas():
    """Columnas en su orden natural; en edad se resalta el grupo con más pobreza."""
    d = datos.set_index("codigo").loc[ORDEN_EDAD] if por == "edad" else datos.set_index("codigo").sort_index()
    alto = d.pobreza_pct.idxmax()
    dif = d.pobreza_pct.max() - d.pobreza_pct.min()
    if por == "sexo":
        titulo = (f"Mujeres y hombres tienen casi la misma pobreza: {dif:.1f} puntos de diferencia" if dif < 1
                  else f"La pobreza de {d.nombre[alto].lower()}es supera en {dif:.1f} puntos a la del otro sexo")
        colores = [APAGADO] * len(d)
        etiquetas = [{"Hombre": "Hombres", "Mujer": "Mujeres"}.get(c, c) for c in d.index]
    else:
        grupo = "Niñas, niños y adolescentes (0-17 años)" if alto == "0-17" else f"Las personas de {alto} años"
        titulo = f"{grupo}: el grupo con más pobreza, {d.pobreza_pct.max():.1f} %"
        colores = [ACENTO if c == alto else APAGADO for c in d.index]
        etiquetas = [f"{c} años" for c in d.index]
    fig, ax = plt.subplots(figsize=(9, 5))
    fig.subplots_adjust(left=0.08, right=0.97, top=0.76, bottom=0.17)
    encabezado(fig, titulo, f"Pobreza monetaria por {'sexo' if por == 'sexo' else 'grupo de edad'}, Perú {anio} "
               "(% de personas). Línea: promedio nacional.", TITULO)
    barras = ax.bar(etiquetas, d.pobreza_pct, color=colores, width=0.62 if por == "edad" else 0.5)
    for b, v in zip(barras, d.pobreza_pct):
        cerca = abs(v - nacional) < 2   # si el valor está pegado a la línea, va dentro de la barra
        ax.text(b.get_x() + b.get_width() / 2, v - 2.6 if cerca else v + 0.8, f"{v:.1f} %", ha="center",
                color="white" if cerca else TINTA, fontsize=11 if cerca else 10, fontweight="bold")
    ax.axhline(nacional, color=TINTA, linewidth=1, linestyle=(0, (4, 3)))
    ax.set_xlim(-0.5, len(d) - 0.5)
    ax.text(len(d) - 0.52, nacional + 0.6, f"Perú {nacional:.1f} %", ha="right", color=TINTA, fontsize=8.5)
    ax.set_ylim(0, max(d.pobreza_pct.max(), nacional) * 1.15)
    ax.set_yticks([])
    sin_bordes(ax, "top", "right", "left")
    ax.tick_params(axis="x", length=0, labelsize=10)
    pie(fig, fuente)
    return fig, titulo


def departamento():
    """Distancia de cada departamento al promedio nacional: encima en acento, debajo en gris."""
    d = datos.sort_values("pobreza_pct")
    n_sobre = int((d.pobreza_pct > nacional).sum())
    titulo = f"{n_sobre} de {len(d)} departamentos superan el promedio nacional de pobreza"
    fig, ax = plt.subplots(figsize=(9, 9.5))
    fig.subplots_adjust(left=0.2, right=0.93, top=0.9, bottom=0.1)
    encabezado(fig, titulo, f"Pobreza monetaria por departamento, Perú {anio} (% de personas). "
               f"Línea: promedio nacional ({nacional:.1f} %).", TITULO)
    colores = [ACENTO if v > nacional else APAGADO for v in d.pobreza_pct]
    ax.hlines(d.nombre, nacional, d.pobreza_pct, color=colores, linewidth=2.2)
    ax.scatter(d.pobreza_pct, d.nombre, color=colores, s=70, zorder=3)
    for y, v in enumerate(d.pobreza_pct):
        encima = v > nacional
        ax.text(v + (0.9 if encima else -0.9), y, f"{v:.1f}", va="center", ha="left" if encima else "right",
                fontsize=9, color=TINTA, fontweight="bold" if encima else "normal")
    ax.axvline(nacional, color=TINTA, linewidth=1)
    ax.set_xlim(0, max(50, d.pobreza_pct.max() + 5))
    ax.set_xlabel("% de personas en pobreza monetaria")
    ax.grid(axis="x", color=LINEA)
    ax.set_axisbelow(True)
    sin_bordes(ax, "top", "right", "left")
    ax.tick_params(axis="y", length=0, labelsize=10)
    ax.text(nacional + 0.6, len(d) - 0.3, "Sobre el promedio", color=ACENTO, fontsize=9, fontweight="bold")
    ax.text(nacional - 0.6, len(d) - 0.3, "Debajo del promedio", color=GRIS, fontsize=9, ha="right")
    pie(fig, fuente)
    alto, bajo = d.iloc[-1], d.iloc[0]
    return fig, (f"{titulo}; mayor {alto.nombre} ({alto.pobreza_pct:.1f} %), menor {bajo.nombre} "
                 f"({bajo.pobreza_pct:.1f} %)")


fig, resumen = {"area": area, "sexo": columnas, "edad": columnas, "departamento": departamento}[por]()
Path("figuras").mkdir(exist_ok=True)
salida = Path(f"figuras/pobreza_{por}.png")
fig.savefig(salida, dpi=200)
print(f"{salida.as_posix()} · {resumen}")
print(datos[["codigo", "nombre", "pobreza_pct", "muestra"]].sort_values("pobreza_pct", ascending=False)
      .round(2).to_string(index=False))
