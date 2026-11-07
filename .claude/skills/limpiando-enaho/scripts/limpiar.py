"""Limpia los módulos 34 (sumaria) y 02 (miembros) de la ENAHO, valida y calcula los indicadores de pobreza.

Se corre desde la raíz del repositorio:
    uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024

Salidas:
    salidas/validacion.txt        cada verificación con [APROBADA] o [FALLIDA]
    salidas/personas_2024.parquet residentes habituales unidos a su hogar (solo si todo lo esencial se aprueba)
    salidas/indicadores.csv       pobreza ponderada por nivel: nacional, área, departamento, territorio, sexo, edad

Ponderación: los indicadores territoriales (nacional, área, departamento, territorio) se calculan con la sumaria y el
peso factor07 x mieperho, que es como se obtienen las cifras oficiales; los individuales (sexo y edad) solo pueden
calcularse con la base de personas y su factor facpob07.
"""
import argparse
import sys
from pathlib import Path

import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")   # la consola de Windows no usa UTF-8 por defecto

LLAVES = ["conglome", "vivienda", "hogar"]
LLAVES_PERSONA = LLAVES + ["codperso"]
ANCHOS = {"conglome": 6, "vivienda": 3, "hogar": 2, "codperso": 2, "ubigeo": 6}
# Valores de referencia del enunciado (issue 201) y de la Sesión 16; nunca se usan para corregir resultados
REFERENCIA = {2024: {"pobreza": 27.6, "extrema": 5.5, "urbana": 24.8, "rural": 39.3, "residentes": 108_664}}
TOLERANCIA = 0.1   # puntos porcentuales
EDADES = ([-1, 17, 29, 44, 59, 200], ["0-17", "18-29", "30-44", "45-59", "60+"])
NOMBRES = {"01": "Amazonas", "02": "Áncash", "03": "Apurímac", "04": "Arequipa", "05": "Ayacucho",
           "06": "Cajamarca", "07": "Callao", "08": "Cusco", "09": "Huancavelica", "10": "Huánuco", "11": "Ica",
           "12": "Junín", "13": "La Libertad", "14": "Lambayeque", "15": "Lima", "16": "Loreto",
           "17": "Madre de Dios", "18": "Moquegua", "19": "Pasco", "20": "Piura", "21": "Puno", "22": "San Martín",
           "23": "Tacna", "24": "Tumbes", "25": "Ucayali", "15LM": "Lima Metropolitana", "15LP": "Lima Provincias"}


def buscar(patron: str) -> Path:
    """Se ubica el .dta dentro de datos/, aunque el zip lo deje en una subcarpeta."""
    rutas = sorted(Path("datos").rglob(patron))
    if not rutas:
        raise SystemExit(f"Falta {patron} en datos/. Descárgalo del portal del INEI (ver README).")
    return rutas[0]


def leer(ruta: Path) -> pd.DataFrame:
    df = pd.read_stata(ruta, convert_categoricals=False)            # 1. Leer
    df.columns = [c.lower().replace("ñ", "ni") for c in df.columns]  # 2. Normalizar nombres: aÑo -> anio
    for col, ancho in ANCHOS.items():                                # llaves como texto, con sus ceros
        if col in df.columns:
            df[col] = (df[col].astype(str).str.strip()
                       .str.replace(r"\.0$", "", regex=True).str.zfill(ancho))
    return df


def territorio(ubigeo: pd.Series) -> pd.Series:
    """ubigeo[:2], salvo Lima, que se separa en Lima Metropolitana (provincia 1501) y Lima Provincias."""
    dep = ubigeo.str[:2]
    return dep.where(dep != "15", ubigeo.str[:4].eq("1501").map({True: "15LM", False: "15LP"}))


def tasas(df: pd.DataFrame, por: str | None, pobre: str, extremo: str, peso: str) -> pd.DataFrame:
    """Pobreza ponderada: se suma el peso de los pobres y se divide entre el peso total; nunca se cuentan encuestas."""
    d = df.assign(_p=df[pobre] * df[peso], _e=df[extremo] * df[peso], _w=df[peso], _n=1)
    g = d.groupby(por, observed=True) if por else d.assign(_k="Perú").groupby("_k")
    g = g[["_p", "_e", "_w", "_n"]].sum().astype("float64")   # factor07 y facpob07 llegan en float32
    return pd.DataFrame({"pobreza_pct": 100 * g._p / g._w, "pobreza_extrema_pct": 100 * g._e / g._w,
                         "poblacion": g._w, "muestra": g._n.astype(int)})


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--anio", type=int, default=2024)
    anio = parser.parse_args().anio
    ref = REFERENCIA.get(anio, {})

    sumaria = leer(buscar(f"sumaria-{anio}.dta"))
    miembros = leer(buscar(f"enaho01-{anio}-200.dta"))

    # 3. Filtrar residentes habituales: miembros no ausentes 30 días o más y no miembros presentes 30 días o más
    residente = (((miembros.p204 == 1) & (miembros.p205 == 2))
                 | ((miembros.p204 == 2) & (miembros.p206 == 1)))
    personas = miembros.loc[residente, LLAVES_PERSONA + ["p203", "p207", "p208a", "facpob07"]].copy()

    # 4. Unir personas (muchas) con su hogar (uno): las variables de hogar vienen solo de la sumaria
    cols_hogar = LLAVES + ["pobreza", "mieperho", "factor07", "ubigeo", "estrato", "dominio"]
    base = personas.merge(sumaria[cols_hogar], on=LLAVES, how="left", validate="m:1", indicator=True)

    # 5. Construir indicadores en ambas bases
    for df in (sumaria, base):
        df["departamento"] = df.ubigeo.str[:2]
        df["territorio"] = territorio(df.ubigeo)
        df["area"] = (df.estrato <= 5).map({True: "Urbana", False: "Rural"})
        df["pobre"] = df.pobreza <= 2
        df["pobre_extremo"] = df.pobreza == 1
    sumaria["peso"] = sumaria.factor07.astype("float64") * sumaria.mieperho   # 6. Factor de expansión
    base["sexo"] = base.p207.map({1: "Hombre", 2: "Mujer"})
    base["edad"] = pd.cut(base.p208a, bins=EDADES[0], labels=EDADES[1])

    # 7. Validar: cada verificación queda escrita; las esenciales detienen el proceso si fallan
    checks = []

    def verificar(nombre, ok, detalle, esencial=True):
        checks.append((nombre, bool(ok), detalle, esencial))

    nac = tasas(sumaria, None, "pobre", "pobre_extremo", "peso").iloc[0]
    nac_p = tasas(base, None, "pobre", "pobre_extremo", "facpob07").iloc[0]
    area = tasas(sumaria, "area", "pobre", "pobre_extremo", "peso")
    simple = 100 * sumaria.pobre.mean()
    verificar("Personas sin duplicados (conglome, vivienda, hogar, codperso)",
              not personas.duplicated(LLAVES_PERSONA).any(), f"{personas.duplicated(LLAVES_PERSONA).sum()} duplicadas")
    verificar("Hogares sin duplicados en la sumaria (conglome, vivienda, hogar)",
              not sumaria.duplicated(LLAVES).any(), f"{sumaria.duplicated(LLAVES).sum()} duplicados")
    verificar("Unión m:1 sin perder ni duplicar filas", len(base) == len(personas),
              f"{len(personas):,} personas antes y {len(base):,} después")
    verificar("Todas las personas encuentran su hogar en la sumaria", (base._merge == "both").all(),
              f"{(base._merge != 'both').sum()} sin hogar")
    if "residentes" in ref:
        verificar("Residentes habituales", len(base) == ref["residentes"],
                  f"{len(base):,} (referencia {ref['residentes']:,})")
    verificar("Llaves con ceros iniciales (conglome de 6 y ubigeo de 6 caracteres)",
              sumaria.conglome.str.len().eq(6).all() and sumaria.ubigeo.str.len().eq(6).all(),
              f"ejemplo de ubigeo: {sumaria.ubigeo.iloc[0]}")
    deps = sorted(sumaria.departamento.unique())
    verificar("25 códigos de departamento (01 a 25)", deps == [f"{i:02d}" for i in range(1, 26)],
              f"{len(deps)} códigos: {deps[0]} a {deps[-1]}")
    verificar("26 territorios al separar Lima Metropolitana (15LM) y Lima Provincias (15LP)",
              sumaria.territorio.nunique() == 26, f"{sumaria.territorio.nunique()} territorios")
    verificar("Factores de expansión completos y positivos (factor07, facpob07)",
              (sumaria.factor07 > 0).all() and (base.facpob07 > 0).all(),
              f"población expandida {sumaria.peso.sum():,.0f}")
    if "pobreza" in ref:
        verificar("Pobreza nacional (sumaria, factor07 x mieperho)", abs(nac.pobreza_pct - ref["pobreza"]) <= TOLERANCIA,
                  f"{nac.pobreza_pct:.2f} % (referencia {ref['pobreza']} %, tolerancia {TOLERANCIA})")
        verificar("Pobreza nacional (personas, facpob07)", abs(nac_p.pobreza_pct - ref["pobreza"]) <= TOLERANCIA,
                  f"{nac_p.pobreza_pct:.2f} % (referencia {ref['pobreza']} %)")
        verificar("La ponderación cambia el resultado frente al promedio simple de hogares",
                  abs(simple - nac.pobreza_pct) > 1,
                  f"promedio simple {simple:.2f} % frente a {nac.pobreza_pct:.2f} % ponderado", esencial=False)
    for clave, etiqueta in (("urbana", "Urbana"), ("rural", "Rural")):
        if clave in ref:
            v = area.loc[etiqueta, "pobreza_pct"]
            verificar(f"Pobreza {clave} (sumaria)", abs(v - ref[clave]) <= TOLERANCIA,
                      f"{v:.2f} % (referencia {ref[clave]} %)", esencial=False)
    if "extrema" in ref:
        verificar("Pobreza extrema nacional (sumaria)", abs(nac.pobreza_extrema_pct - ref["extrema"]) <= TOLERANCIA,
                  f"{nac.pobreza_extrema_pct:.2f} % (referencia {ref['extrema']} %)", esencial=False)

    aprobadas = sum(ok for _, ok, _, _ in checks)
    esenciales_fallidas = [n for n, ok, _, e in checks if e and not ok]
    lineas = [f"Validación ENAHO {anio} · módulos 34 (sumaria) y 02 (miembros)",
              f"Filas del módulo 02: {len(miembros):,} · hogares de la sumaria: {len(sumaria):,}", ""]
    lineas += [f"[{'APROBADA' if ok else 'FALLIDA'}] {'' if e else '(complementaria) '}{n}: {d}"
               for n, ok, d, e in checks]
    lineas += ["", f"Resultado: {aprobadas} de {len(checks)} verificaciones aprobadas; "
               + ("todas las esenciales se aprobaron." if not esenciales_fallidas
                  else f"FALLARON {len(esenciales_fallidas)} esenciales: el proceso se detiene.")]
    Path("salidas").mkdir(exist_ok=True)
    Path("salidas/validacion.txt").write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print("\n".join(lineas))
    if esenciales_fallidas:
        sys.exit(f"ERROR: fallaron verificaciones esenciales ({'; '.join(esenciales_fallidas)}). "
                 "No se guardan la base ni los indicadores; no se deben corregir los datos a mano.")

    # 8. Guardar la base de personas y la tabla de indicadores
    base = base.drop(columns="_merge")
    base.to_parquet(f"salidas/personas_{anio}.parquet", index=False)
    niveles = [("nacional", tasas(sumaria, None, "pobre", "pobre_extremo", "peso"), "sumaria", "factor07*mieperho"),
               ("area", area, "sumaria", "factor07*mieperho"),
               ("departamento", tasas(sumaria, "departamento", "pobre", "pobre_extremo", "peso"), "sumaria",
                "factor07*mieperho"),
               ("territorio", tasas(sumaria, "territorio", "pobre", "pobre_extremo", "peso"), "sumaria",
                "factor07*mieperho"),
               ("sexo", tasas(base, "sexo", "pobre", "pobre_extremo", "facpob07"), "personas", "facpob07"),
               ("edad", tasas(base, "edad", "pobre", "pobre_extremo", "facpob07"), "personas", "facpob07")]
    tabla = pd.concat([t.rename_axis("codigo").reset_index().assign(nivel=n, base=b, ponderador=p)
                       for n, t, b, p in niveles])
    tabla["codigo"] = tabla.codigo.astype(str)
    tabla["nombre"] = tabla.codigo.map(NOMBRES).fillna(tabla.codigo)
    tabla["anio"] = anio
    tabla["fuente"] = f"INEI, ENAHO {anio}, módulos 34 y 02"
    tabla = tabla[["anio", "nivel", "codigo", "nombre", "pobreza_pct", "pobreza_extrema_pct", "poblacion",
                   "muestra", "base", "ponderador", "fuente"]]
    tabla.round({"pobreza_pct": 4, "pobreza_extrema_pct": 4, "poblacion": 0}).to_csv(   # 4 decimales: sin doble redondeo
        "salidas/indicadores.csv", index=False, encoding="utf-8")
    print(f"\nGuardados: salidas/personas_{anio}.parquet ({len(base):,} filas) y salidas/indicadores.csv "
          f"({len(tabla)} filas)")


if __name__ == "__main__":
    main()
