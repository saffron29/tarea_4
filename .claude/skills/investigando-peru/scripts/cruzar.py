"""Cruza el gasto de los gobiernos subnacionales (BCRP, vía MCP) con la pobreza monetaria (ENAHO, vía skills) por
código de territorio, calcula el gasto por habitante y su asociación con la pobreza, y grafica el resultado.

Se corre desde la raíz del repositorio, después de limpiando-enaho y de la herramienta departamentos del MCP con
guardar=True (gobiernos regionales y, si se quiere el complemento, gobiernos locales):
    uv run .claude/skills/investigando-peru/scripts/cruzar.py --anio 2024

Entradas: salidas/indicadores.csv y salidas/bcrp_departamentos_*_<anio>.csv. Salidas: salidas/cruce_territorios.csv,
salidas/cruce_resumen.csv y figuras/cruce_gasto_pobreza.png. Es una asociación descriptiva, no causal.
"""
import argparse
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "recursos"))
from estilo import ACENTO, APAGADO, GRIS, LINEA, TINTA, aplicar, encabezado, pie  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--anio", default="2024")
anio = p.parse_args().anio

INDICADORES = Path("salidas/indicadores.csv")
if not INDICADORES.exists():
    raise SystemExit("Falta salidas/indicadores.csv. Usa primero la skill limpiando-enaho.")
regional = sorted(Path("salidas").glob(f"bcrp_departamentos_*regionales*_{anio}.csv"))
local = sorted(Path("salidas").glob(f"bcrp_departamentos_*locales*_{anio}.csv"))
if not regional:
    raise SystemExit(f"Falta el gasto regional {anio}. Llama a la herramienta departamentos del MCP bcrp con "
                     f"grupo='gastos gobiernos regionales', anio='{anio}', medida='millones de soles', guardar=True.")

ind = pd.read_csv(INDICADORES, dtype={"codigo": str})
if str(int(ind.anio.iloc[0])) != anio:
    print(f"Aviso: la ENAHO procesada es de {int(ind.anio.iloc[0])} y el gasto es de {anio}.")


def cruzar(archivo, nivel, esperados):
    """Une el gasto del BCRP con la pobreza y la población de la ENAHO por código; exige que no falte ninguno."""
    gasto = pd.read_csv(archivo, dtype={"codigo_territorio": str})
    enaho = ind[ind.nivel == nivel][["codigo", "nombre", "pobreza_pct", "poblacion", "muestra"]]
    t = enaho.merge(gasto[["codigo_territorio", "codigo_serie", "valor", "fuente"]], left_on="codigo",
                    right_on="codigo_territorio", how="outer", validate="1:1", indicator=True)
    sin_par = t[t._merge != "both"]
    if len(sin_par) or len(t) != esperados:
        raise SystemExit(f"La unión por código de {archivo.name} no cuadra: {len(t)} filas (se esperaban "
                         f"{esperados}); sin pareja: {sin_par[['codigo', 'codigo_territorio']].values.tolist()}")
    t["gasto_pc"] = t.valor * 1e6 / t.poblacion
    return t.drop(columns=["_merge", "codigo_territorio"]).rename(columns={"valor": "gasto_millones"})


def pearson(t):
    return float(t.pobreza_pct.corr(t.gasto_pc))


def spearman(t):   # correlación de los rangos (sin depender de scipy)
    return float(t.pobreza_pct.rank().corr(t.gasto_pc.rank()))


reg = cruzar(regional[-1], "territorio", 26)
nacional = ind.loc[ind.nivel == "nacional", "pobreza_pct"].iloc[0]
alta = reg.pobreza_pct > nacional


def por_habitante(t):
    return t.gasto_millones.sum() * 1e6 / t.poblacion.sum()


# Lima Metropolitana (15LM) casi no tiene gasto «regional» y pesa 10 millones de habitantes: dentro de un grupo
# arrastra el promedio. Por eso la comparación por grupos se hace sin 15LM y la versión con 15LM queda como
# sensibilidad.
sin_lm = reg.codigo != "15LM"
filas = [("gasto_regional_pc_nacional", por_habitante(reg), 26,
          "S/ por habitante: gasto regional total / población expandida total (26 territorios)"),
         ("gasto_regional_pc_pobreza_alta", por_habitante(reg[alta & sin_lm]), int((alta & sin_lm).sum()),
          "S/ por habitante en los territorios con pobreza mayor al promedio nacional, sin Lima Metropolitana"),
         ("gasto_regional_pc_pobreza_baja", por_habitante(reg[~alta & sin_lm]), int((~alta & sin_lm).sum()),
          "S/ por habitante en los territorios con pobreza menor o igual al promedio nacional, sin Lima "
          "Metropolitana"),
         ("gasto_regional_pc_pobreza_alta_con_15LM", por_habitante(reg[alta]), int(alta.sum()),
          "sensibilidad: el mismo grupo incluyendo Lima Metropolitana (27.58 %, justo sobre el promedio)"),
         ("pearson_regional_26", pearson(reg), 26, "pobreza % vs gasto regional por habitante, 26 territorios"),
         ("spearman_regional_26", spearman(reg), 26, "correlación de rangos, 26 territorios"),
         ("pearson_regional_sin_15LM", pearson(reg[reg.codigo != "15LM"]), 25,
          "sensibilidad: sin Lima Metropolitana, cuyo gasto regional por habitante es atípico"),
         ("spearman_regional_sin_15LM", spearman(reg[reg.codigo != "15LM"]), 25, "sensibilidad, rangos")]
tabla = reg.rename(columns={"gasto_millones": "gasto_regional_millones", "gasto_pc": "gasto_regional_pc",
                            "codigo_serie": "serie_regional", "fuente": "fuente_regional"})
if local:
    loc = cruzar(local[-1], "departamento", 25)
    filas += [("pearson_local_25", pearson(loc), 25, "pobreza % vs gasto local por habitante, 25 departamentos"),
              ("spearman_local_25", spearman(loc), 25, "correlación de rangos, 25 departamentos")]
    tabla = tabla.merge(loc[["codigo", "gasto_millones", "gasto_pc", "codigo_serie"]].rename(columns={
        "gasto_millones": "gasto_local_millones", "gasto_pc": "gasto_local_pc", "codigo_serie": "serie_local"}),
        on="codigo", how="left")
resumen = pd.DataFrame(filas, columns=["indicador", "valor", "n", "descripcion"]).assign(anio=anio)
resumen["valor"] = resumen.valor.round(4)
tabla.sort_values("pobreza_pct", ascending=False).round(4).to_csv("salidas/cruce_territorios.csv", index=False,
                                                                  encoding="utf-8")
resumen.to_csv("salidas/cruce_resumen.csv", index=False, encoding="utf-8")

# Gráfico de dispersión: pobreza (x) y gasto regional por habitante (y); una etiqueta por territorio destacado
TITULO = aplicar()
r = pearson(reg)
fuerza = "casi no se asocian" if abs(r) < 0.3 else ("se asocian negativamente" if r < 0 else
                                                   "se asocian positivamente")
fig, ax = plt.subplots(figsize=(9, 6.6))
fig.subplots_adjust(left=0.1, right=0.97, top=0.8, bottom=0.14)
encabezado(fig, f"La pobreza y el gasto regional por habitante {fuerza} (r = {r:.2f})",
           f"26 territorios, {anio}. Cada punto es un departamento; Lima Metropolitana y Lima Provincias van "
           "separadas. Tamaño: población.", TITULO)
colores = [ACENTO if a else APAGADO for a in alta]
ax.scatter(reg.pobreza_pct, reg.gasto_pc, s=reg.poblacion / reg.poblacion.max() * 600 + 30, color=colores,
           alpha=0.85, edgecolor="white", linewidth=1, zorder=3)
ax.axvline(nacional, color=TINTA, linewidth=1, linestyle=(0, (4, 3)))
ax.text(nacional + 0.4, reg.gasto_pc.max() * 1.04, f"Pobreza nacional {nacional:.1f} %", fontsize=8.5, color=TINTA)
destacar = set(reg.nlargest(3, "pobreza_pct").codigo) | set(reg.nlargest(2, "gasto_pc").codigo) | \
    set(reg.nsmallest(2, "pobreza_pct").codigo) | {"15LM", "15LP", "07"}
for f in reg[reg.codigo.isin(destacar)].itertuples():
    ax.annotate(f"{f.nombre} ({f.gasto_pc:,.0f})", (f.pobreza_pct, f.gasto_pc), xytext=(6, 4),
                textcoords="offset points", fontsize=8, color=TINTA)
ax.set_xlabel("Pobreza monetaria (% de personas, ENAHO)")
ax.set_ylabel("Gasto no financiero del gobierno regional\n(S/ por habitante, BCRP / ENAHO)")
ax.set_xlim(0, reg.pobreza_pct.max() * 1.15)
ax.set_ylim(0, reg.gasto_pc.max() * 1.12)
ax.grid(color=LINEA)
ax.set_axisbelow(True)
for lado in ("top", "right"):
    ax.spines[lado].set_visible(False)
sin_lm = pearson(reg[reg.codigo != "15LM"])
pie(fig, f"Fuente: BCRP, gasto no financiero de gobiernos regionales {anio} (RD16603DA a RD16628DA); INEI, ENAHO "
    f"{int(ind.anio.iloc[0])}, pobreza y población expandida (factor07 × mieperho).\nSin Lima Metropolitana, "
    f"r = {sin_lm:.2f}. Asociación descriptiva entre territorios: no implica causalidad. Elaboración propia.")
fig.savefig("figuras/cruce_gasto_pobreza.png", dpi=200)

print("salidas/cruce_territorios.csv, salidas/cruce_resumen.csv y figuras/cruce_gasto_pobreza.png")
print(resumen[["indicador", "valor", "n"]].round(3).to_string(index=False))
print(tabla[["codigo", "nombre", "pobreza_pct", "gasto_regional_pc"]].sort_values("gasto_regional_pc")
      .round(1).to_string(index=False))
