# Plan de investigación

## Pregunta
¿El gasto de los gobiernos regionales por habitante en 2024 fue mayor en los territorios con más pobreza monetaria, y cómo evolucionó ese gasto entre 2019 y 2024?

## Fuentes
- BCRP (MCP `bcrp`): grupo «gastos gobiernos regionales» 2024 por departamento (millones de soles); «gastos gobiernos locales» 2024 (complemento); serie RD16629DA (gasto regional total, 2015-2025); serie PN38705PM (IPC de Lima, dic. 2021 = 100).
- ENAHO 2024 (INEI), módulos 34 (sumaria) y 02 (miembros): pobreza monetaria y población expandida por territorio (26 territorios, con Lima Metropolitana y Lima Provincias separadas), área, sexo y edad.

## Indicadores
- Gasto regional por habitante 2024 = gasto departamental (BCRP) / población expandida (ENAHO).
- Pobreza monetaria 2024 (%) por territorio.
- Evolución 2019-2024 del gasto regional total: nominal y real (deflactado con el IPC de Lima).
- Asociación descriptiva (correlación) entre gasto por habitante y pobreza, con y sin Lima Metropolitana (15LM).

## Pasos
1. Consultar el BCRP con el MCP y guardar los CSV; verificar `suma` = `total_bcrp` y `faltan` vacío (hecho).
2. Regenerar la ENAHO (limpiando-enaho) con sus validaciones; luego graficando-enaho (departamento, área) y mapeando-enaho.
3. Cruzar con `cruzar.py` y graficar con `graficar_bcrp.py`.
4. Contrastar: pobreza nacional frente a 27.6% del INEI, mapa frente a la Sesión 16, suma departamental frente al total del BCRP.
5. Redactar informes/informe_final.md según la plantilla, con tabla de trazabilidad.

## Limitaciones previstas
Una sola ENAHO (2024) frente a gasto 2019-2024; soles corrientes salvo el cálculo real; población expandida de la encuesta; muestra pequeña en algunos departamentos; Lima Metropolitana atípica; asociación no causal; el gasto regional no incluye el gasto local ni el gasto del gobierno nacional ejecutado en el territorio.
