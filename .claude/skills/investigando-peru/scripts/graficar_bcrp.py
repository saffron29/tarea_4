"""Grafica la evolución anual de una serie del BCRP guardada por el MCP y, si se da un índice de precios, calcula
su variación en términos reales.

Se corre desde la raíz del repositorio, después de llamar a la herramienta serie del MCP con guardar=True:
    uv run .claude/skills/investigando-peru/scripts/graficar_bcrp.py --codigo RD16629DA --desde 2019 --hasta 2024 \
        --deflactor PN38705PM

Lee salidas/bcrp_serie_<codigo>.csv (y salidas/bcrp_serie_<deflactor>.csv), de modo que las cifras del gráfico son
exactamente las que entregó el MCP. Escribe figuras/bcrp_<codigo>.png y salidas/bcrp_resumen_<codigo>.csv.
"""
import argparse
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "recursos"))
from estilo import ACENTO, APAGADO, GRIS, TINTA, aplicar, encabezado, pie  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--codigo", default="RD16629DA")
p.add_argument("--desde", default="2019", help="primer año del periodo que se resalta y se resume")
p.add_argument("--hasta", default="2024", help="último año del periodo que se resalta y se resume")
p.add_argument("--deflactor", default=None, help="código del índice de precios mensual (por ejemplo, PN38705PM)")
a = p.parse_args()


def leer(codigo):
    ruta = Path(f"salidas/bcrp_serie_{codigo}.csv")
    if not ruta.exists():
        raise SystemExit(f"Falta {ruta}. Llama primero a la herramienta serie del MCP bcrp con codigo={codigo!r} y "
                         "guardar=True; no copies las cifras a mano.")
    return pd.read_csv(ruta, dtype={"periodo": str})


s = leer(a.codigo)
if s.frecuencia.iloc[0] != "Anual":
    raise SystemExit(f"{a.codigo} es {s.frecuencia.iloc[0].lower()}; este gráfico es para series anuales.")
s["anio"] = s.periodo.str[:4]
ini, fin = s.set_index("anio").loc[[a.desde, a.hasta], "valor"]
var_nominal = 100 * (fin / ini - 1)
filas = [{"indicador": "valor_inicial", "periodo": a.desde, "valor": ini, "unidad": "millones de S/ corrientes"},
         {"indicador": "valor_final", "periodo": a.hasta, "valor": fin, "unidad": "millones de S/ corrientes"},
         {"indicador": "variacion_nominal_pct", "periodo": f"{a.desde}-{a.hasta}", "valor": var_nominal, "unidad": "%"}]
nota_real = ""
if a.deflactor:
    ipc = leer(a.deflactor)
    ipc["anio"] = ipc.periodo.str[:4]
    promedio = ipc.groupby("anio").valor.mean()          # índice promedio de cada año
    if not {a.desde, a.hasta} <= set(promedio.index):
        raise SystemExit(f"El índice {a.deflactor} no cubre {a.desde} y {a.hasta}; pide la serie para esos años.")
    var_precios = 100 * (promedio[a.hasta] / promedio[a.desde] - 1)
    var_real = 100 * ((fin / promedio[a.hasta]) / (ini / promedio[a.desde]) - 1)
    filas += [{"indicador": "variacion_precios_pct", "periodo": f"{a.desde}-{a.hasta}", "valor": var_precios,
               "unidad": f"% (promedio anual de {a.deflactor})"},
              {"indicador": "variacion_real_pct", "periodo": f"{a.desde}-{a.hasta}", "valor": var_real,
               "unidad": f"% (deflactado con el promedio anual de {a.deflactor})"}]
    nota_real = f"; en términos reales, {var_real:+.1f} %"
resumen = pd.DataFrame(filas).assign(codigo=a.codigo, fuente=s.fuente.iloc[0])
resumen["valor"] = resumen.valor.round(4)
resumen.to_csv(f"salidas/bcrp_resumen_{a.codigo}.csv", index=False, encoding="utf-8")

TITULO = aplicar()
nombre = s.nombre.iloc[0]
fig, ax = plt.subplots(figsize=(9, 5.2))
fig.subplots_adjust(left=0.06, right=0.97, top=0.76, bottom=0.19)
verbo = "creció" if var_nominal >= 0 else "cayó"
encabezado(fig, f"El gasto de los gobiernos regionales {verbo} {abs(var_nominal):.0f} % entre {a.desde} y {a.hasta}"
           if "gobiernos regionales" in nombre.lower() else
           f"{nombre.split(' - ')[-1]}: {var_nominal:+.0f} % entre {a.desde} y {a.hasta}",
           f"{nombre}. Soles corrientes{nota_real}.", TITULO)
dentro = s.anio.between(a.desde, a.hasta)
barras = ax.bar(s.anio, s.valor / 1000, color=[ACENTO if d else APAGADO for d in dentro], width=0.65)
for b, v, d in zip(barras, s.valor / 1000, dentro):
    ax.text(b.get_x() + b.get_width() / 2, v + s.valor.max() / 1000 * 0.015, f"{v:.1f}", ha="center",
            fontsize=8.5, color=TINTA, fontweight="bold" if d else "normal")
ax.set_ylabel("Miles de millones de S/")
ax.set_ylim(0, s.valor.max() / 1000 * 1.12)
ax.set_yticks([])
ax.set_ylabel("")
for lado in ("top", "right", "left"):
    ax.spines[lado].set_visible(False)
ax.tick_params(axis="x", length=0)
ax.text(0, 1.02, "Miles de millones de soles", transform=ax.transAxes, color=GRIS, fontsize=8.5)
pie(fig, f"Fuente: BCRP, serie {a.codigo}" + (f"; índice de precios {a.deflactor}" if a.deflactor else "")
    + f". Elaboración propia.\nConsulta: {s.fuente.iloc[0]}")
Path("figuras").mkdir(exist_ok=True)
fig.savefig(f"figuras/bcrp_{a.codigo}.png", dpi=200)
print(f"figuras/bcrp_{a.codigo}.png y salidas/bcrp_resumen_{a.codigo}.csv")
print(resumen[["indicador", "periodo", "valor", "unidad"]].round(2).to_string(index=False))
