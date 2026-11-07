---
name: limpiando-enaho
description: Limpia los módulos 34 (sumaria) y 02 (miembros) de la ENAHO del INEI y arma una base de personas con pobreza y factor de expansión. Úsala cuando pidan limpiar, unir o analizar la ENAHO, o calcular pobreza por región, departamento, área, sexo o edad.
argument-hint: [año]
---
# Limpiar la ENAHO
Año de trabajo: si en «$ARGUMENTS» aparece un año de cuatro dígitos, usa ese; si no, usa 2024. En los pasos de abajo, <año> es ese número.

1. Si faltan los zip en datos/, pide al usuario bajarlos del INEI (código 966 = 2024) y no sigas.
2. Desde la raíz del repositorio, corre exactamente: uv run ${CLAUDE_SKILL_DIR}/scripts/limpiar.py --anio <año>
3. Lee salidas/validacion.txt. Si la pobreza difiere del INEI en más de 0.1 puntos, o el script falla en un assert, detente y avisa; no corrijas los datos a mano.
4. Responde con salidas/personas_<año>.parquet; toda cifra va ponderada con facpob07 y la pobreza es pobre = pobreza <= 2, nunca un promedio del código.
5. Antes de usar una variable que no está en la base, lee reference.md.
