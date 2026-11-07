---
name: limpiando-enaho
description: Limpia y valida los módulos 34 (sumaria) y 02 (miembros) de la ENAHO del INEI y calcula la pobreza monetaria ponderada por nivel (nacional, área urbana/rural, departamento, territorio con Lima separada, sexo y edad). Úsala cuando pidan limpiar, unir, validar o analizar la ENAHO, o calcular pobreza, población o indicadores de hogares con la ENAHO; las skills graficando-enaho, mapeando-enaho e investigando-peru la necesitan primero.
argument-hint: [año]
---
# Limpiar y validar la ENAHO

Año de trabajo: si en «$ARGUMENTS» aparece un año de cuatro dígitos, usa ese; si no, usa 2024. En los pasos de abajo, <año> es ese número.

1. Si faltan los .dta en datos/ (sumaria-<año>.dta y enaho01-<año>-200.dta), pide al usuario bajar los zip del INEI (código 966 = 2024, enlaces en el README) y no sigas.
2. Desde la raíz del repositorio, corre exactamente: `uv run ${CLAUDE_SKILL_DIR}/scripts/limpiar.py --anio <año>`
3. Lee salidas/validacion.txt. Cada verificación dice [APROBADA] o [FALLIDA]. Si el script termina con error porque falló una verificación esencial, detente y muestra cuál falló; no corrijas los datos a mano ni cambies las referencias para que «pase».
4. Si todo se aprobó, las salidas son:
   - salidas/indicadores.csv: una fila por nivel y categoría con pobreza_pct, pobreza_extrema_pct, poblacion (expandida) y muestra. Es la fuente única de cifras para gráficos, mapas e informes.
   - salidas/personas_<año>.parquet: residentes habituales unidos a su hogar, para cortes nuevos.
5. Reglas fijas: llaves como texto con sus ceros; residentes = ((p204 == 1) & (p205 == 2)) | ((p204 == 2) & (p206 == 1)); unión con validate="m:1"; pobre = pobreza <= 2, nunca un promedio del código; indicadores territoriales con la sumaria y peso factor07 × mieperho; sexo y edad con personas y facpob07. Nunca promedios simples.
6. Antes de usar una variable que no está en la base, lee reference.md.
7. Responde citando la cifra y el archivo del que sale (por ejemplo, «27.58 %, salidas/indicadores.csv, nivel nacional»).
