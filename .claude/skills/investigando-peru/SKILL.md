---
name: investigando-peru
description: Investiga preguntas socioeconómicas del Perú que combinan series del BCRP (vía el MCP bcrp) con la ENAHO (vía las skills limpiando-enaho, graficando-enaho y mapeando-enaho), cruza ambas fuentes por código de departamento y redacta un informe reproducible en informes/. Úsala cuando pidan investigar o escribir un informe que relacione gasto público, inflación, actividad económica u otro indicador del BCRP con la pobreza o las desigualdades territoriales, y también para cualquier cifra que combine ambas fuentes, como el gasto por habitante de un departamento (BCRP entre la población expandida de la ENAHO) o la correlación entre gasto y pobreza: su script cruzar.py ya calcula esos valores para los 26 territorios.
argument-hint: [pregunta de investigación]
---
# Investigar con el BCRP y la ENAHO

Si solo piden una cifra que combine ambas fuentes (por ejemplo, el gasto regional por habitante de un departamento o una correlación), haz los pasos 2 (departamentos con guardar=True), 3 (solo limpiando-enaho) y 4 (cruzar.py) y responde con la fila o el indicador de salidas/cruce_territorios.csv o salidas/cruce_resumen.csv, sin informe.

Pregunta: «$ARGUMENTS». Si está vacía, usa: ¿El gasto de los gobiernos regionales por habitante en 2024 fue mayor en los territorios con más pobreza monetaria, y cómo evolucionó ese gasto entre 2019 y 2024?

Regla de oro: ninguna cifra la escribes tú. Cada número sale de una herramienta del MCP o de un archivo de salidas/ y se cita con su serie o archivo. Si algo falla o no hay datos, lo dices y no lo completas.

1. **Plan.** Escribe informes/plan.md: pregunta, fuentes (series del BCRP y módulos de la ENAHO), indicadores, pasos y limitaciones previstas.
2. **BCRP con el MCP bcrp** (desde la raíz del repositorio):
   - Confirma los códigos con buscar_series o el recurso bcrp://grupos-departamentales.
   - `departamentos(grupo="gastos gobiernos regionales", anio="2024", medida="millones de soles", guardar=True)` y lo mismo con `grupo="gastos gobiernos locales"` (complemento con 25 departamentos). Comprueba que `suma` coincida con `total_bcrp` y que `faltan` esté vacío.
   - `serie("RD16629DA", "2015", "2025", guardar=True)` (gasto regional total) y `serie("PN38705PM", "2015-01", "2025-12", guardar=True)` (IPC de Lima, índice dic. 2021 = 100).
   - `resumen("RD16629DA", "2019", "2024")` para la evolución nominal.
3. **ENAHO con las skills, invocadas con la herramienta Skill** (no corras sus scripts por tu cuenta: cada skill trae sus reglas y validaciones):
   - Skill `limpiando-enaho` con argumento 2024 (si no existe salidas/indicadores.csv o le falta el nivel territorio).
   - Skill `graficando-enaho` con argumento `departamento` y otra vez con `area`.
   - Skill `mapeando-enaho`.
4. **Cruce y gráfico del BCRP**, desde la raíz:
   - `uv run ${CLAUDE_SKILL_DIR}/scripts/cruzar.py --anio 2024` → salidas/cruce_territorios.csv, salidas/cruce_resumen.csv y figuras/cruce_gasto_pobreza.png.
   - `uv run ${CLAUDE_SKILL_DIR}/scripts/graficar_bcrp.py --codigo RD16629DA --desde 2019 --hasta 2024 --deflactor PN38705PM` → figuras/bcrp_RD16629DA.png y salidas/bcrp_resumen_RD16629DA.csv.
5. **Contraste con fuentes oficiales:** pobreza nacional de salidas/validacion.txt frente a la cifra del INEI (27.6 %); comparación del mapa con la referencia de la Sesión 16 (salidas/comparacion_mapa.csv); suma departamental frente a la serie Total del BCRP.
6. **Informe:** escribe informes/informe_final.md siguiendo ${CLAUDE_SKILL_DIR}/plantilla_informe.md (estructura, reglas de redacción y tabla de trazabilidad). Incluye las cuatro figuras con rutas relativas (../figuras/..., ../mapas/...).
7. Reglas de interpretación: es una asociación descriptiva entre territorios, nunca causal; el gasto está en soles corrientes salvo la variación real calculada por graficar_bcrp.py; Lima Metropolitana (15LM) tiene un gasto regional por habitante atípico, por lo que se reportan siempre los resultados con y sin 15LM; la población viene de la ENAHO (población expandida), no de proyecciones oficiales.
8. Responde con la ruta del informe, las herramientas MCP y skills que usaste y los tres hallazgos en una línea cada uno.
