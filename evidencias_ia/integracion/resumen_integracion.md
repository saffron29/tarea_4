# Evidencias de integración: MCP + Skills en una misma ejecución

Corridas con `claude -p` (Sonnet), MCP `bcrp` por `.mcp.json` y las skills de `.claude/skills/`. Antes de cada ejecución integrada se vaciaron salidas/, figuras/, mapas/ e informes/, de modo que todo se regeneró en la sesión. Registros completos en los .jsonl.

## Ejecución integrada final (v2)

### ejecucion_integrada.jsonl

- Modelo: claude-sonnet-5-5 · servidores MCP: bcrp (connected)
- Skills activadas: investigando-peru, limpiando-enaho, graficando-enaho, mapeando-enaho · herramientas MCP usadas: departamentos, departamentos, serie, serie, resumen
- Turnos: 23 · tiempo: 86.8 s · costo informado: 0.2892 USD

Pasos:

1. `Skill: {"skill": "investigando-peru"}`
2. `Bash: ls; ls informes salidas figuras mapas datos 2>&1 | head -50; cat .claude/skills/investigando-peru/plantilla_informe.md`
3. `Write: {"file_path": "~/Documents/GitHub/tarea_4/informes/plan.md", "content": "# Plan de investigación\n\n## Pregunta\n¿El gasto de los gobiernos regionales por habitante en 2024 fue mayor en los territorios con má`
4. `mcp__bcrp__departamentos: {"grupo": "gastos gobiernos regionales", "anio": "2024", "medida": "millones de soles", "guardar": true}`
5. `mcp__bcrp__departamentos: {"grupo": "gastos gobiernos locales", "anio": "2024", "medida": "millones de soles", "guardar": true}`
6. `mcp__bcrp__serie: {"codigo": "RD16629DA", "desde": "2015", "hasta": "2025", "guardar": true}`
7. `mcp__bcrp__serie: {"codigo": "PN38705PM", "desde": "2015-01", "hasta": "2025-12", "guardar": true}`
8. `mcp__bcrp__resumen: {"codigo": "RD16629DA", "desde": "2019", "hasta": "2024"}`
9. `Skill: {"skill": "limpiando-enaho", "args": "2024"}`
10. `Bash: ls datos/966-Modulo34 datos/966-Modulo02 | head; uv run ~/Documents/GitHub/tarea_4/.claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024 2>&1 | tail -30; cat salidas/validacion.txt`
11. `Skill: {"skill": "graficando-enaho", "args": "departamento"}`
12. `Bash: for c in departamento area; do uv run ~/Documents/GitHub/tarea_4/.claude/skills/graficando-enaho/scripts/graficar.py --por $c 2>&1 | tail -8; done`
13. `Skill: {"skill": "mapeando-enaho"}`
14. `Bash: uv run ~/Documents/GitHub/tarea_4/.claude/skills/graficando-enaho/scripts/graficar.py --por departamento 2>&1 | tail -8; uv run ~/Documents/GitHub/tarea_4/.claude/skills/graficando-enaho/scripts/g`
15. `Bash: ls figuras mapas salidas; head -5 salidas/comparacion_mapa.csv; uv run ~/Documents/GitHub/tarea_4/.claude/skills/investigando-peru/scripts/cruzar.py --anio 2024 2>&1 | tail -40; uv run ~/Documents`
16. `Bash: cat salidas/cruce_resumen.csv; head -3 salidas/cruce_territorios.csv; grep -c True salidas/comparacion_mapa.csv; cat salidas/bcrp_resumen_RD16629DA.csv; grep -E "nacional|Nacional" salidas/indicadores.csv | head -3; sed `
17. `Read: {"file_path": "~/Documents/GitHub/tarea_4/figuras/cruce_gasto_pobreza.png"}`
18. `Write: {"file_path": "~/Documents/GitHub/tarea_4/informes/informe_final.md", "content": "# El gasto regional por habitante de 2024 no fue mayor donde hay más pobreza, aunque el gasto total creció cerca de 35% real d`

Respuesta final:

> Terminé el informe y reviso que todo quedó escrito. Lo que dice, y lo que no verifiqué, está abajo.
> 
> **Informe:** `informes/informe_final.md`. El plan está en `informes/plan.md` y se escribió antes de pedir cualquier dato.
> 
> **Herramientas usadas**
> - **MCP del BCRP:** `departamentos` (gasto regional y local 2024), `serie` (RD16629DA y PN38705PM) y `resumen` (RD16629DA, 2019-2024).
> - **Skills:** `investigando-peru`, `limpiando-enaho` (15 de 15 verificaciones aprobadas), `graficando-enaho` (departamento y área) y `mapeando-enaho` (25 de 25 departamentos coinciden con la referencia).
> - **Scripts de cruce:** `cruzar.py` y `graficar_bcrp.py`.
> 
> **Hallazgos**
> 1. **Evolución:** el gasto regional pasó de 33,755.1 a 56,575.5 millones de soles entre 2019 y 2024. Eso es +67.61% nominal y +34.92% real (IPC de Lima: +24.23%).
> 2. **Pobreza 2024:** la nacional fue 27.58%, y Cajamarca (45.0%), Loreto (43.0%) y Puno (39.9%) fueron los territorios más pobres.
> 3. **Respuesta a la pregunta:** no, el gasto regional por habitante no fue mayor donde hay más pobreza. Los territorios más pobres gastaron 2,233.5 soles por habitante y los demás 2,433.2, ambos grupos sin Lima Metropolitana. La correlación es -0.16 con los 26 territorios y -0.18 sin Lima Metropolitana. Es una asociación descriptiva, no causal.
> 
> **Puntos a tener en cuenta**
> - Lima Metropolitana tiene un gasto regional atípico, de 11.2 soles por habitante. Por eso el informe da los resultados con y sin ella.
> - La evolución 2019-2024 es solo del total nacional, porque hay una única ENAHO (2024).
> - En la sección 8 del informe, las columnas «Resultado» y «Diferencia» quedan como «pendiente de verificación manual», como pide la plantilla. Esa verificación la debe hacer usted.
> - No abrí las figuras `bcrp_RD16629DA.png`, `pobreza_departamento.png` ni el mapa. Solo vi `cruce_gasto_pobreza.png`, y los scripts reportaron haber generado las demás.

## Primera ejecución (v1), corregida

En v1 el agente invocó solo la skill investigando-peru y corrió los scripts de la ENAHO por Bash; además invirtió el sentido de una frase («el gasto no se acompaña de mayor pobreza»). Se ajustaron SKILL.md y la plantilla (commit 1a18344) y se repitió. Informe y plan de v1 en v1/.

### ejecucion_integrada_v1.jsonl

- Modelo: claude-sonnet-5-5 · servidores MCP: bcrp (connected)
- Skills activadas: investigando-peru · herramientas MCP usadas: departamentos, departamentos, serie, serie, resumen
- Turnos: 20 · tiempo: 90.1 s · costo informado: 0.3436 USD


## Manejo de errores

### manejo_errores.jsonl

- Modelo: claude-sonnet-5-5 · servidores MCP: bcrp (connected)
- Skills activadas: ninguna · herramientas MCP usadas: departamentos, serie, departamentos, buscar_series
- Turnos: 8 · tiempo: 16.7 s · costo informado: 0.1385 USD

Pasos:

1. `mcp__bcrp__departamentos: {"grupo": "gastos gobiernos regionales", "anio": "2027", "guardar": false}`
2. `mcp__bcrp__serie: {"codigo": "XX999", "desde": "2024", "hasta": "2024"}`
3. `Glob: {"pattern": "**/*.{dta,sav,csv,parquet}"}`
4. `mcp__bcrp__departamentos: {"grupo": "gastos gobiernos regionales", "anio": "2027", "medida": "millones de soles", "guardar": false}`
5. `mcp__bcrp__buscar_series: {"texto": "XX999"}`
6. `Bash: ls -la; find . -path ./.venv -prune -o \( -iname '*enaho*' -o -iname '*sumaria*' -o -iname '*.dta' -o -iname '*.sav' \) -print | head -30`
7. `Bash: ls datos datos/*; ls salidas`

Respuesta final:

> No pude obtener ninguna de las tres cifras, porque ninguna de las fuentes tiene ese dato.
> 
> 1. **Gasto del Gobierno Regional de Puno en 2027:** no hay dato. Consulté el grupo «Gastos no financiero de gobiernos regionales» (en millones de soles) y el BCRP respondió que no tiene datos para 2027. Ese año todavía no ocurre, porque hoy es 2026-11-06. En `salidas/` solo hay datos de 2024.
> 
> 2. **Pobreza monetaria de Puno en 2025 (ENAHO):** no se puede calcular. Los archivos del proyecto son solo de 2024: `datos/966-Modulo34/sumaria-2024.dta` y `datos/966-Modulo02/enaho01-2024-200.dta`. No hay módulos de 2025, así que no inventé la cifra. Si descargan los módulos 34 y 02 de 2025 del INEI, puedo calcularla con la skill `limpiando-enaho`. También puedo darles la cifra de Puno para 2024 con los datos que ya están.
> 
> 3. **Serie `XX999` en 2024:** esa serie no existe. La consulta directa devolvió «No existe el código de serie» y `buscar_series` no encontró nada. Si me dan el nombre del indicador, busco el código correcto.
> 
> Dígame si quiere que haga alguna de estas dos cosas:
> - Consultar el gasto de Puno en 2024, el último año que tiene datos.
> - Calcular la pobreza de Puno en 2024.

