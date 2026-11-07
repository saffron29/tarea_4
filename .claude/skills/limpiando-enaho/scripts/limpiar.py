"""Limpia los módulos 34 y 02 de la ENAHO y arma una base de personas.

Se corre desde la raíz del repositorio:
    uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024
"""
import argparse
from pathlib import Path

import pandas as pd

LLAVES = ["conglome", "vivienda", "hogar"]
LLAVES_PERSONA = LLAVES + ["codperso"]
ANCHOS = {"conglome": 6, "vivienda": 3, "hogar": 2, "codperso": 2, "ubigeo": 6}
POBREZA_INEI = {2024: 27.6}  # % de personas, cifra oficial
EXTREMA_INEI = {2024: 5.5}  # % de personas en pobreza extrema
RESIDENTES = {2024: 108_664}  # residentes habituales esperados en la clase


def buscar(patron: str) -> Path:
    """Se ubica el .dta dentro de datos/, aunque el zip lo deje en una subcarpeta."""
    rutas = sorted(Path("datos").rglob(patron))
    if not rutas:
        raise SystemExit(f"Falta {patron} en datos/. Descárgalo del portal del INEI.")
    return rutas[0]


def leer(ruta: Path) -> pd.DataFrame:
    df = pd.read_stata(ruta, convert_categoricals=False)            # 1. Leer
    df.columns = [c.lower().replace("ñ", "ni") for c in df.columns]  # 2. aÑo -> anio
    for col, ancho in ANCHOS.items():                                # llaves como texto
        if col in df.columns:
            df[col] = (df[col].astype(str).str.strip()
                       .str.replace(r"\.0$", "", regex=True).str.zfill(ancho))
    return df


def tasa(pobre: pd.Series, peso: pd.Series) -> float:
    """Se pondera cada caso por su factor; nunca se cuentan encuestas."""
    return 100 * (pobre * peso).sum() / peso.sum()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--anio", type=int, default=2024)
    anio = parser.parse_args().anio

    sumaria = leer(buscar(f"sumaria-{anio}.dta"))
    miembros = leer(buscar(f"enaho01-{anio}-200.dta"))

    # 3. Filtrar residentes habituales: miembros no ausentes 30 días o más
    # y no miembros presentes 30 días o más
    residente = (((miembros.p204 == 1) & (miembros.p205 == 2))
                 | ((miembros.p204 == 2) & (miembros.p206 == 1)))
    personas = miembros.loc[residente, LLAVES_PERSONA
                            + ["p203", "p207", "p208a", "facpob07"]].copy()

    # 4. Unir (las variables de hogar vienen solo de la sumaria)
    cols_hogar = LLAVES + ["pobreza", "mieperho", "factor07",
                           "ubigeo", "estrato", "dominio"]
    base = personas.merge(sumaria[cols_hogar], on=LLAVES, how="left",
                          validate="m:1", indicator=True)

    # 5. Construir
    base["departamento"] = base.ubigeo.str[:2]
    base["urbano"] = base.estrato <= 5
    base["pobre"] = base.pobreza <= 2
    base["pobre_extremo"] = base.pobreza == 1

    # 6. Validar
    assert not personas.duplicated(LLAVES_PERSONA).any(), "personas duplicadas"
    assert not sumaria.duplicated(LLAVES).any(), "hogares duplicados"
    assert len(base) == len(personas), "la unión perdió o duplicó filas"
    assert (base._merge == "both").all(), "personas sin hogar en la sumaria"
    base = base.drop(columns="_merge")

    peso_hogar = sumaria.factor07 * sumaria.mieperho
    pob_sumaria = tasa(sumaria.pobreza <= 2, peso_hogar)
    ext_sumaria = tasa(sumaria.pobreza == 1, peso_hogar)
    pob_personas = tasa(base.pobre, base.facpob07)

    oficial = POBREZA_INEI.get(anio)
    if oficial is not None:
        assert abs(pob_sumaria - oficial) < 0.1, f"sumaria: {pob_sumaria:.2f}"
        assert abs(pob_personas - oficial) < 0.1, f"personas: {pob_personas:.2f}"
    if anio in EXTREMA_INEI:
        assert abs(ext_sumaria - EXTREMA_INEI[anio]) < 0.1, f"extrema: {ext_sumaria:.2f}"
    if anio in RESIDENTES:
        assert len(base) == RESIDENTES[anio], f"residentes: {len(base):,}"

    # 7. Guardar
    Path("salidas").mkdir(exist_ok=True)
    base.to_parquet(f"salidas/personas_{anio}.parquet", index=False)
    reporte = (
        f"ENAHO {anio}\n"
        f"Filas módulo 200: {len(miembros):,}\n"
        f"Residentes habituales: {len(base):,}\n"
        f"Hogares (sumaria): {len(sumaria):,}\n"
        f"Población expandida: {peso_hogar.sum():,.0f}\n"
        f"Pobreza (sumaria, factor07 x mieperho): {pob_sumaria:.2f} %\n"
        f"Pobreza extrema (sumaria): {ext_sumaria:.2f} %\n"
        f"Pobreza (personas, facpob07): {pob_personas:.2f} %\n"
        f"Cifra oficial INEI: {oficial} %\n"
    )
    Path("salidas/validacion.txt").write_text(reporte, encoding="utf-8")
    print(reporte)


if __name__ == "__main__":
    main()
