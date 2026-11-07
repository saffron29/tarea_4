"""Estilo común de los gráficos y mapas del proyecto (ENAHO, BCRP y cruce de ambas fuentes).

Tipografías Montserrat (títulos) e Inter (texto), con licencia SIL Open Font License, en recursos/fuentes/. Si no
están, se usa la fuente por defecto de Matplotlib y los gráficos se generan igual.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

FUENTES = Path(__file__).parent / "fuentes"
TINTA, GRIS, LINEA = "#1B2A41", "#6B7280", "#E5E7EB"   # texto, texto secundario, grilla
ACENTO, APAGADO = "#C2410C", "#A8B3C2"                  # lo que se resalta / el resto
CLASES = [(0, 15, "#FDE7D3"), (15, 25, "#F7B488"), (25, 35, "#E4733A"), (35, 100, "#A93A0B")]  # % de personas


def _titulo():
    ruta = FUENTES / "montserrat-latin-700-normal.ttf"
    if ruta.exists():
        return fm.FontProperties(fname=str(ruta), size=15)
    return fm.FontProperties(size=15, weight="bold")


def aplicar():
    """Registra las fuentes y fija los parámetros comunes; devuelve la fuente de los títulos."""
    for ruta in FUENTES.glob("*.ttf"):
        fm.fontManager.addfont(str(ruta))
    hay_inter = any(f.name == "Inter" for f in fm.fontManager.ttflist)
    plt.rcParams.update({"font.family": "Inter" if hay_inter else "sans-serif", "font.size": 10,
                         "axes.edgecolor": "#D1D5DB", "axes.labelcolor": "#4B5563", "xtick.color": "#4B5563",
                         "ytick.color": TINTA, "figure.facecolor": "white"})
    return _titulo()


def encabezado(fig, titulo, subtitulo, fuente_titulo):
    """Título analítico y subtítulo arriba a la izquierda, a distancias fijas en pulgadas."""
    alto = fig.get_figheight()
    y = 1 - 0.3 / alto
    fig.text(0.04, y, titulo, fontproperties=fuente_titulo, color=TINTA, va="top")
    fig.text(0.04, y - 0.42 / alto, subtitulo, color=GRIS, fontsize=10, va="top")


def pie(fig, texto):
    fig.text(0.04, 0.02, texto, color=GRIS, fontsize=7.5)


def clase(valor):
    """Color de la clase del mapa a la que pertenece un porcentaje."""
    return next(c for lo, hi, c in CLASES if lo <= valor < hi)


def fraccion(pct):
    """Expresa un porcentaje como «n de cada d» con el denominador más simple que lo aproxima mejor."""
    p = pct / 100
    n, d = min(((round(p * d), d) for d in (2, 3, 4, 5, 10)), key=lambda x: (abs(x[0] / x[1] - p), x[1]))
    return f"{n} de cada {d}"
