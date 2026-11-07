---
name: graficando-enaho
description: Grafica la pobreza monetaria de la ENAHO del INEI con barras ponderadas por área (urbana y rural), sexo, grupo de edad o departamento, con título analítico, unidades y fuente. Úsala cuando pidan un gráfico, una figura, barras o una comparación visual de la pobreza con la ENAHO, incluida la comparación entre departamentos.
argument-hint: [area|sexo|edad|departamento]
---
# Graficar la ENAHO

1. Si no existe salidas/indicadores.csv, usa primero la skill limpiando-enaho y espera a que sus validaciones se aprueben.
2. Elige el corte según el pedido: «urbana y rural» o «área» = area; «hombres y mujeres» o «sexo» = sexo; «edad», «niños», «adultos mayores» = edad; «departamentos», «regiones» o «comparar departamentos» = departamento. Si piden varios, corre una vez por cada uno.
3. Desde la raíz del repositorio, corre: `uv run ${CLAUDE_SKILL_DIR}/scripts/graficar.py --por <area|sexo|edad|departamento>`
4. Reglas fijas (no las cambies aunque el pedido no las mencione): cifras tomadas de salidas/indicadores.csv, ya ponderadas; barras horizontales desde cero y ordenadas; un solo color; valor en cada barra; línea del promedio nacional; título analítico calculado con los datos; subtítulo con período y unidad (% de personas); nota de fuente con el ponderador; PNG a 200 dpi en figuras/.
5. Si piden otro corte que indicadores.csv no trae (por ejemplo, dominio o nivel educativo), no improvises cifras: avisa que el script no lo cubre. Para un mapa, usa la skill mapeando-enaho.
6. Responde con la ruta de la figura (figuras/pobreza_<corte>.png), el título que imprimió el script y las cifras principales.
