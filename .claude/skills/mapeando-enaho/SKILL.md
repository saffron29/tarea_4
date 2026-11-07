---
name: mapeando-enaho
description: Mapea la pobreza monetaria de la ENAHO del INEI por departamento del Perú, ponderada por facpob07 y unida al GeoJSON por código de ubigeo. Úsala cuando pidan un mapa, un coroplético o la pobreza por departamento o región con la ENAHO.
---
# Mapear la ENAHO
1. Si no existe salidas/personas_2024.parquet, usa primero la skill limpiando-enaho.
2. Si falta datos/peru_departamental_simple.geojson, pide al usuario bajarlo (la URL está en el README) y no sigas.
3. Desde la raíz del repositorio, corre: uv run ${CLAUDE_SKILL_DIR}/scripts/mapear.py
4. Reglas fijas: unir por código (ubigeo[:2] con FIRST_IDDP), nunca por nombre; exigir 25 departamentos y ninguno sin dato; un color de claro a oscuro desde 0, nunca arcoíris; leyenda con la unidad (% de personas); Lima (15) y Callao (07) separados.
5. Si el script falla en un assert, detente y avisa; no unas por nombre ni completes datos a mano.
6. Responde con la ruta mapas/pobreza_departamento.png y los tres departamentos con más y con menos pobreza.
