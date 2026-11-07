# Plan de investigación

## Pregunta
¿El gasto de los gobiernos regionales por habitante en 2024 fue mayor en los territorios con más pobreza monetaria, y cómo evolucionó ese gasto entre 2019 y 2024?

## Fuentes
- BCRP (MCP `bcrp`): grupo «gastos gobiernos regionales» y «gastos gobiernos locales» por departamento (2024, millones de soles); serie RD16629DA (gasto regional total, anual); serie PN38705PM (IPC de Lima, dic. 2021 = 100) como deflactor.
- ENAHO 2024 (INEI), módulos 34 (sumaria) y 02 (miembros): pobreza monetaria ponderada y población expandida por territorio (26 unidades, con Lima Metropolitana y Lima Provincias separadas).

## Indicadores
- Gasto regional por habitante 2024 = gasto departamental (BCRP) / población expandida (ENAHO).
- Pobreza monetaria 2024 por territorio (ENAHO).
- Evolución 2019-2024 del gasto regional total: variación nominal y real (deflactada con el IPC de Lima).
- Asociación entre gasto por habitante y pobreza (correlación y comparación por terciles), con y sin Lima Metropolitana (15LM).

## Pasos
1. Confirmar códigos y descargar con el MCP (departamentos 2024, series RD16629DA y PN38705PM, resumen 2019-2024), guardando los CSV en salidas/.
2. Ejecutar las skills `limpiando-enaho` (2024), `graficando-enaho` (departamento y área) y `mapeando-enaho`.
3. Cruzar ambas fuentes con `cruzar.py` y graficar la serie con `graficar_bcrp.py`.
4. Contrastar: pobreza nacional frente a 27.6% (INEI), mapa frente a la Sesión 16, suma departamental frente al total BCRP.
5. Redactar informes/informe_final.md según la plantilla.

## Limitaciones previstas
- Una sola ENAHO (2024) frente a una serie de gasto 2019-2024.
- Gasto en soles corrientes; la variación real depende del IPC de Lima.
- Población de la encuesta (expandida), no proyecciones oficiales; muestra pequeña en algunos departamentos.
- Lima Metropolitana es atípica: se reportan resultados con y sin ella.
- Asociación descriptiva entre territorios, no causal.
