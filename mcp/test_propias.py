"""Pruebas de las herramientas propias (correlacion y departamentos); las 8 originales siguen en test_server.py sin
cambios.

    uv run pytest -q          # 12 pruebas: 8 originales + 4 propias

Igual que las originales, llaman al servidor en memoria y piden datos reales al BCRP.
"""
import pytest
from fastmcp.exceptions import ToolError

from test_server import llamar


def test_correlacion_alinea_periodos_y_cita_fuentes():
    # Inflación de Lima (PN01273PM) y tasa de referencia (PD04722MM), 36 meses de 2022 a 2024
    r = llamar("correlacion", codigo_a="PN01273PM", codigo_b="PD04722MM", desde="2022-01", hasta="2024-12")
    assert r["periodos"] == 36
    assert (r["desde"], r["hasta"]) == ("2022-01", "2024-12")
    assert -1 <= r["correlacion"] <= 1
    assert r["correlacion"] == pytest.approx(0.303, abs=0.01)
    assert len(r["fuentes"]) == 2


def test_correlacion_rechaza_frecuencias_distintas():
    # La inflación es mensual y el gasto regional total (RD16629DA) es anual: no se pueden alinear
    with pytest.raises(ToolError, match="misma frecuencia"):
        llamar("correlacion", codigo_a="PN01273PM", codigo_b="RD16629DA", desde="2020-01", hasta="2024-12")


def test_departamentos_gasto_regional_separa_lima_y_cuadra_con_el_total():
    r = llamar("departamentos", grupo="gastos gobiernos regionales", anio="2024", medida="millones de soles",
               guardar=False)
    codigos = [t["codigo_territorio"] for t in r["territorios"]]
    assert r["n"] == 26 and r["faltan"] == [] and r["sin_dato"] == []
    assert {"15LM", "15LP", "07"} <= set(codigos) and "15" not in codigos   # Lima separada; Callao aparte
    cusco = next(t for t in r["territorios"] if t["codigo_territorio"] == "08")
    assert cusco["valor"] == pytest.approx(3552.70, abs=0.01)
    assert r["suma"] == pytest.approx(r["total_bcrp"], abs=0.01)           # no se perdió ningún departamento


def test_departamentos_gasto_local_25_y_errores_claros():
    r = llamar("departamentos", grupo="gastos gobiernos locales", anio="2024", medida="millones de soles",
               guardar=False)
    assert r["n"] == 25 and r["faltan"] == []
    assert sorted(t["codigo_territorio"] for t in r["territorios"]) == [f"{i:02d}" for i in range(1, 26)]
    with pytest.raises(ToolError, match="varias medidas"):                 # crédito trae tres medidas
        llamar("departamentos", grupo="credito directo departamentos", anio="2024")
    with pytest.raises(ToolError, match="No hay un grupo"):
        llamar("departamentos", grupo="ipc lima", anio="2024")
