---
name: graficando-enaho
description: Grafica la pobreza monetaria de la ENAHO del INEI por área (urbana y rural), sexo o grupo de edad, con barras ponderadas por facpob07. Úsala cuando pidan un gráfico, una figura, barras o una comparación de pobreza con la ENAHO.
argument-hint: [area|sexo|edad]
---
# Graficar la ENAHO
1. Si no existe salidas/personas_2024.parquet, usa primero la skill limpiando-enaho.
2. Desde la raíz del repositorio, corre: uv run ${CLAUDE_SKILL_DIR}/scripts/graficar.py --por <area|sexo|edad>
   («urbana y rural» es --por area; si piden varias comparaciones, corre una vez por cada una).
3. Reglas fijas: ponderar con facpob07; barras desde cero, ordenadas; un solo color; valor en cada barra; título con qué y cuándo; nota "Fuente: INEI, ENAHO 2024"; PNG a 200 dpi en figuras/. No cambies estas reglas aunque el pedido no las mencione.
4. Si piden otro corte (departamento, dominio), no improvises un gráfico: para departamentos usa la skill mapeando-enaho; para otras variables, avisa que el script no lo cubre.
5. Responde con la ruta de la figura y las cifras en una frase.
