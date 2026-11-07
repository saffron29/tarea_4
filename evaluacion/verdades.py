"""Calcula las respuestas esperadas de las 10 preguntas de evaluación por caminos independientes del agente.

    uv run evaluacion/verdades.py          # escribe evaluacion/preguntas.csv

- BCRP: llamadas HTTP directas a la API oficial (no usa mcp/server.py).
- ENAHO: un cálculo propio y mínimo desde los .dta (no importa el código de las skills), con la misma definición
  oficial: pobre = pobreza <= 2, peso factor07 x mieperho en la sumaria y facpob07 para personas.
- Cruce: la correspondencia entre las series regionales del BCRP y los códigos de ubigeo se escribe aquí a mano,
  aparte de la que hace la herramienta departamentos, para que un error en una no se copie en la otra.

Las respuestas esperadas y sus tolerancias se fijan antes de correr el experimento y no se cambian después.
"""
import json
import sys
from pathlib import Path

import httpx
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
API = "https://estadisticas.bcrp.gob.pe/estadisticas/series/api"
SALIDA = Path(__file__).parent / "preguntas.csv"

# Gasto no financiero de gobiernos regionales (millones de S/): serie del BCRP -> código de territorio
GASTO_REGIONAL = {"RD16603DA": "01", "RD16604DA": "02", "RD16605DA": "03", "RD16606DA": "04", "RD16607DA": "05",
                  "RD16608DA": "06", "RD16609DA": "08", "RD16610DA": "09", "RD16611DA": "10", "RD16612DA": "11",
                  "RD16613DA": "12", "RD16614DA": "13", "RD16615DA": "14", "RD16616DA": "16", "RD16617DA": "17",
                  "RD16618DA": "18", "RD16619DA": "19", "RD16620DA": "20", "RD16621DA": "21", "RD16622DA": "22",
                  "RD16623DA": "23", "RD16624DA": "24", "RD16625DA": "25",
                  "RD16626DA": "15LP",   # Gobierno Regional de Lima -> Lima Provincias
                  "RD16627DA": "07",     # Callao
                  "RD16628DA": "15LM"}   # Municipalidad Metropolitana de Lima -> Lima Metropolitana


def bcrp(codigos, desde, hasta):
    """Valores de una o varias series del BCRP; devuelve {periodo: [valores]} y la URL consultada."""
    url = f"{API}/{'-'.join(codigos)}/json/{desde}/{hasta}"
    r = httpx.get(url, timeout=60)
    datos = json.loads(r.content.decode("latin-1"))
    return {p["name"]: [float(v) for v in p["values"]] for p in datos["periods"]}, url


def leer(patron, columnas):
    ruta = sorted(Path("datos").rglob(patron))[0]
    df = pd.read_stata(ruta, convert_categoricals=False, columns=columnas)
    for c in ("conglome", "vivienda", "hogar", "ubigeo"):
        if c in df:
            df[c] = df[c].astype(str).str.strip()
    df["ubigeo"] = df["ubigeo"].str.zfill(6) if "ubigeo" in df else None
    return df


def tasa(pobre, peso):
    return float(100 * (pobre * peso).sum() / peso.sum())


preguntas = []


def agregar(id_, tipo, pregunta, esperada, unidad, tolerancia, tipo_tol, fuente, procedimiento, criterio=""):
    preguntas.append({"id": id_, "tipo": tipo, "pregunta": pregunta, "respuesta_esperada": round(esperada, 4),
                      "unidad": unidad, "tolerancia": tolerancia, "tipo_tolerancia": tipo_tol,
                      "fuente_verificacion": fuente, "procedimiento": procedimiento,
                      "criterio_interpretacion": criterio})


# ---------------- BCRP ----------------
v, url = bcrp(["PN01273PM"], "2024-12", "2024-12")
agregar("B1", "BCRP", "¿Cuál fue la inflación interanual (variación porcentual del IPC en 12 meses) de Lima "
        "Metropolitana en diciembre de 2024, según el BCRP? Responde en %.", v["Dic.2024"][0], "%", 0.05, "absoluta",
        url, "Serie PN01273PM, periodo Dic.2024, consulta directa a la API del BCRP.")
v, url = bcrp(["PD04722MM"], "2024-12", "2024-12")
agregar("B2", "BCRP", "¿Cuál era la tasa de referencia de la política monetaria del BCRP en diciembre de 2024? "
        "Responde en %.", v["Dic.2024"][0], "%", 0.01, "absoluta", url,
        "Serie PD04722MM, periodo Dic.2024, consulta directa a la API del BCRP.")
v, url = bcrp(["PM04863AA"], "2024", "2024")
agregar("B3", "BCRP", "¿Cuánto creció el PBI real del Perú en 2024 (variación porcentual anual), según el BCRP? "
        "Responde en %.", v["2024"][0], "%", 0.05, "absoluta", url,
        "Serie PM04863AA, año 2024, consulta directa a la API del BCRP.")
v, url = bcrp(["RD16629DA"], "2024", "2024")
agregar("B4", "BCRP", "¿Cuál fue el gasto no financiero total de los gobiernos regionales del Perú en 2024, "
        "según el BCRP? Responde en millones de soles.", v["2024"][0], "millones de S/", 1.0, "absoluta", url,
        "Serie RD16629DA (Total), año 2024, consulta directa a la API del BCRP.")

# ---------------- ENAHO ----------------
sumaria = leer("sumaria-2024.dta", ["conglome", "vivienda", "hogar", "ubigeo", "estrato", "pobreza", "mieperho",
                                    "factor07"])
sumaria["peso"] = sumaria.factor07.astype("float64") * sumaria.mieperho
sumaria["pobre"] = sumaria.pobreza <= 2
sumaria["dep"] = sumaria.ubigeo.str[:2]
fuente_enaho = "INEI, ENAHO 2024, módulos 34 y 02 (cálculo independiente: evaluacion/verdades.py)"
agregar("E1", "ENAHO", "Según la ENAHO 2024 del INEI, ¿qué porcentaje de la población del Perú estaba en pobreza "
        "monetaria en 2024? Responde en %.", tasa(sumaria.pobre, sumaria.peso), "%", 0.1, "absoluta", fuente_enaho,
        "Sumaria 2024: pobre = pobreza <= 2, ponderado con factor07 x mieperho.")
rural = sumaria.estrato > 5
agregar("E2", "ENAHO", "Según la ENAHO 2024 del INEI, ¿qué porcentaje de la población del área rural del Perú "
        "estaba en pobreza monetaria en 2024? Responde en %.", tasa(sumaria.pobre[rural], sumaria.peso[rural]), "%",
        0.2, "absoluta", fuente_enaho, "Sumaria 2024, estrato 6 a 8 (rural), ponderado con factor07 x mieperho.")
puno = sumaria.dep == "21"
agregar("E3", "ENAHO", "Según la ENAHO 2024 del INEI, ¿qué porcentaje de la población del departamento de Puno "
        "estaba en pobreza monetaria en 2024? Responde en %.", tasa(sumaria.pobre[puno], sumaria.peso[puno]), "%",
        0.2, "absoluta", fuente_enaho, "Sumaria 2024, ubigeo[:2] == '21', ponderado con factor07 x mieperho.")
miembros = leer("enaho01-2024-200.dta", ["conglome", "vivienda", "hogar", "codperso", "p204", "p205", "p206",
                                         "p208a", "facpob07"])
residentes = miembros[((miembros.p204 == 1) & (miembros.p205 == 2)) | ((miembros.p204 == 2) & (miembros.p206 == 1))]
personas = residentes.merge(sumaria[["conglome", "vivienda", "hogar", "pobre"]], on=["conglome", "vivienda", "hogar"],
                            how="inner", validate="m:1")
assert len(personas) == len(residentes) == 108_664
menores = personas.p208a <= 17
agregar("E4", "ENAHO", "Según la ENAHO 2024 del INEI, ¿qué porcentaje de las personas de 0 a 17 años "
        "(residentes habituales) estaba en pobreza monetaria en 2024? Responde en %.",
        tasa(personas.pobre[menores], personas.facpob07[menores].astype("float64")), "%", 0.3, "absoluta",
        fuente_enaho, "Residentes habituales del módulo 02 unidos a la sumaria; p208a <= 17; ponderado con facpob07.")

# ---------------- Cruce BCRP + ENAHO ----------------
sumaria["territorio"] = sumaria.dep.where(sumaria.dep != "15",
                                          sumaria.ubigeo.str[:4].eq("1501").map({True: "15LM", False: "15LP"}))
g = sumaria.assign(pp=sumaria.pobre * sumaria.peso).groupby("territorio")[["pp", "peso"]].sum()
territorios = pd.DataFrame({"pobreza": 100 * g.pp / g.peso, "poblacion": g.peso})
v, url = bcrp(list(GASTO_REGIONAL), "2024", "2024")
gasto = pd.Series(v["2024"], index=[GASTO_REGIONAL[c] for c in GASTO_REGIONAL], name="gasto_millones")
territorios = territorios.join(gasto, how="inner")
assert len(territorios) == 26
territorios["gasto_pc"] = territorios.gasto_millones * 1e6 / territorios.poblacion
fuente_cruce = f"{url} + {fuente_enaho}"
agregar("M1", "Mixta", "Con el gasto no financiero del Gobierno Regional de Cajamarca en 2024 publicado por el BCRP y "
        "la población de Cajamarca estimada con la ENAHO 2024 (población expandida), ¿cuánto gastó ese gobierno "
        "regional por habitante en 2024? Responde en soles por habitante.", territorios.loc["06", "gasto_pc"],
        "S/ por habitante", 0.02, "relativa", fuente_cruce,
        "RD16608DA (2024) x 1,000,000 / suma de factor07 x mieperho de los hogares con ubigeo[:2] == '06'.",
        "Debe usar ambas fuentes y explicar que la población es una estimación de la encuesta.")
r = territorios.pobreza.corr(territorios.gasto_pc)
agregar("M2", "Mixta", "Para 2024, considera 26 territorios: los 24 departamentos distintos de Lima, Lima Metropolitana "
        "(gasto de la Municipalidad Metropolitana de Lima en el grupo de gobiernos regionales del BCRP; población de "
        "la provincia de Lima, ubigeo 1501) y Lima Provincias (gasto del Gobierno Regional de Lima; población del "
        "resto del departamento de Lima). ¿Cuál es la correlación de Pearson entre la tasa de pobreza monetaria "
        "(ENAHO 2024, % de personas) y el gasto no financiero del gobierno regional por habitante (BCRP, 2024) en "
        "esos 26 territorios? Responde con el coeficiente.", r, "coeficiente", 0.05, "absoluta", fuente_cruce,
        "Gasto 2024 de RD16603DA a RD16628DA / población expandida ENAHO por territorio; Pearson entre las 26 "
        "tasas de pobreza y los 26 gastos por habitante.",
        "Debe usar ambas fuentes, no afirmar causalidad y advertir que es una asociación entre 26 unidades.")

tabla = pd.DataFrame(preguntas)
tabla.to_csv(SALIDA, index=False, encoding="utf-8")
territorios.round(4).to_csv(Path(__file__).parent / "verdades_territorios.csv", encoding="utf-8")
print(tabla[["id", "tipo", "respuesta_esperada", "unidad", "tolerancia", "tipo_tolerancia"]].to_string(index=False))
print(f"\nGuardado {SALIDA.as_posix()}")
