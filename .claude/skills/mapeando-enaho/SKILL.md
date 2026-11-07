---
name: mapeando-enaho
description: Mapea la pobreza monetaria de la ENAHO del INEI por departamento del Perú (25 unidades, Lima y Callao separados) en un coroplético unido al GeoJSON por código de ubigeo, y lo compara con la referencia de la Sesión 16. Úsala cuando pidan un mapa, un coroplético o la distribución territorial de la pobreza por departamento o región con la ENAHO.
---
# Mapear la ENAHO

1. Si no existe salidas/indicadores.csv, usa primero la skill limpiando-enaho y espera a que sus validaciones se aprueben.
2. Si falta datos/peru_departamental_simple.geojson, pide al usuario bajarlo (la URL está en el README) y no sigas.
3. Desde la raíz del repositorio, corre: `uv run ${CLAUDE_SKILL_DIR}/scripts/mapear.py`
4. Reglas fijas: unir por código (ubigeo[:2] con FIRST_IDDP), nunca por nombre; exigir 25 departamentos y ninguno sin dato; Lima (15) y Callao (07) separados; un solo tono en cuatro rangos fijos (menos de 15, 15 a 25, 25 a 35 y 35 % o más), nunca arcoíris; leyenda con la unidad (% de personas) y cuántos departamentos hay en cada rango; recuadro ampliado de Lima y Callao; comparar cada departamento con referencias/pobreza_departamento_2024.csv y guardar salidas/comparacion_mapa.csv.
5. Si el script falla en un assert o porque un departamento difiere de la referencia en más de 0.1 puntos, detente y avisa; no unas por nombre ni completes ni ajustes datos a mano.
6. Responde con la ruta mapas/pobreza_departamento.png, cuántos departamentos coinciden con la referencia y los tres departamentos con más y con menos pobreza.
