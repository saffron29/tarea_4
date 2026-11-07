# El gasto regional por habitante de 2024 no fue mayor en los territorios más pobres, aunque el gasto regional creció 34.9% real desde 2019

Frank Pinares Gutiérrez · 6 de noviembre de 2026 · Tarea 4, Python Intermedio para CCSS y Gestión Pública

## 1. Pregunta de investigación

El presente informe examina si el gasto de los gobiernos regionales por habitante en 2024 fue mayor en los territorios con más pobreza monetaria y cómo evolucionó ese gasto entre 2019 y 2024. El cruce territorial se limita a 2024, año de la ENAHO utilizada, mientras que la evolución abarca 2019-2024. Se trabaja con 26 territorios, en los que Lima Metropolitana (15LM) y Lima Provincias (15LP) se mantienen separadas.

## 2. Fuentes y metodología

Del Banco Central de Reserva del Perú se emplearon, mediante el servidor MCP `bcrp`, la herramienta `departamentos` (grupos «gastos gobiernos regionales» y «gastos gobiernos locales», 2024, millones de soles) y la herramienta `serie`, con el gasto regional total (RD16629DA, 2015-2025) y el IPC de Lima Metropolitana (PN38705PM, dic. 2021 = 100). Se comprobó que la suma de los 26 territorios coincidiera con el total del BCRP (56,575.5223 millones de soles, ambos valores idénticos, sin territorios faltantes). En el complemento local, la suma fue 39,345.7465 frente a un total de 39,345.7466, una diferencia de redondeo.

De la ENAHO 2024 del INEI se usaron los módulos 34 (sumaria) y 02 (miembros) con la skill limpiando-enaho: la pobreza territorial se calcula con la sumaria y el ponderador factor07 × mieperho, y la población expandida proviene de la propia encuesta. Las 15 verificaciones de salidas/validacion.txt se aprobaron, entre ellas la pobreza nacional de 27.58% frente a la referencia del INEI de 27.6%. Asimismo se ejecutaron graficando-enaho (departamento y área), mapeando-enaho e investigando-peru (scripts `cruzar.py` y `graficar_bcrp.py`).

La unión se realiza por código de territorio. El gasto por habitante resulta de dividir el gasto regional de cada territorio entre su población expandida. La variación real se obtiene deflactando con el promedio anual de PN38705PM. Debe considerarse que se trata de una asociación descriptiva entre territorios y no de un análisis causal.

## 3. Resultados

### 3.1 Evolución del gasto regional 2019-2024, nominal y real

El gasto regional total pasó de 33,755.12 millones de soles en 2019 a 56,575.52 millones en 2024 (RD16629DA, 2019-2024), lo que equivale a un aumento nominal de 67.61% (salidas/bcrp_resumen_RD16629DA.csv). Ahora bien, los precios de Lima Metropolitana subieron 24.23% en el mismo periodo (PN38705PM, promedio anual 2019-2024), de modo que la variación real alcanza 34.92% (salidas/bcrp_resumen_RD16629DA.csv). Es decir, cerca de la mitad del aumento nominal se explica por el nivel de precios, si bien el gasto sigue creciendo de manera sustantiva en términos reales. Cabe señalar que la serie total no permite hacer esta comparación por habitante ni por territorio, pues la ENAHO utilizada corresponde solo a 2024.

### 3.2 Distribución territorial de la pobreza 2024

La pobreza monetaria nacional fue 27.58% (salidas/indicadores.csv, nivel nacional), con 39.30% en el área rural y 24.81% en la urbana (salidas/indicadores.csv, nivel área). Entre los territorios, los mayores niveles corresponden a Cajamarca (45.0%), Loreto (43.0%) y Puno (39.9%), mientras que los menores se observan en Ica (6.0%), Moquegua (11.0%) y Madre de Dios (11.1%) (salidas/cruce_territorios.csv). Los porcentajes de los 25 departamentos coinciden con la referencia de la Sesión 16 (salidas/comparacion_mapa.csv: 25 de 25 con coincide = True).

### 3.3 Relación entre gasto regional por habitante y pobreza, con y sin Lima Metropolitana

El gasto regional por habitante a escala nacional fue S/ 1,640.69 (salidas/cruce_resumen.csv). Al comparar territorios con pobreza superior al promedio nacional y los de pobreza igual o inferior, sin Lima Metropolitana, el primer grupo (10 territorios) registró S/ 2,233.46 por habitante y el segundo (15 territorios) S/ 2,433.20 (salidas/cruce_resumen.csv). Es decir, el gasto por habitante no fue mayor en los territorios más pobres; fue incluso algo menor.

La correlación entre pobreza y gasto regional por habitante fue de -0.161 (Pearson) y -0.128 (Spearman) con los 26 territorios, y de -0.185 y -0.102 sin Lima Metropolitana (salidas/cruce_resumen.csv). Son valores débiles y de signo negativo, es decir, el gasto no se acompaña de mayor pobreza. Con Lima Metropolitana dentro del grupo de pobreza alta, el promedio cae a S/ 1,210.19 (11 territorios), porque este territorio solo registra 115.665 millones de soles de gasto regional (RD16628DA, 2024) para una población muy numerosa, o S/ 11.2 por habitante (salidas/cruce_territorios.csv). Por ello se reportan siempre ambas versiones.

Por otra parte, existen territorios con gasto alto y pobreza alta o baja a la vez. Moquegua tiene el mayor gasto por habitante (S/ 4,315.2) y baja pobreza (11.0%), mientras que Cajamarca (S/ 2,439.8) y Puno (S/ 1,980.9), con pobreza elevada, se ubican en la parte media o baja de la distribución. Como complemento, la correlación con el gasto de los gobiernos locales por habitante en 25 departamentos fue -0.402 (Pearson) y -0.287 (Spearman) (salidas/cruce_resumen.csv).

## 4. Visualizaciones

![Gasto regional total 2019-2024, nominal y real](../figuras/bcrp_RD16629DA.png)

El gráfico del BCRP muestra el crecimiento sostenido del gasto regional entre 2019 y 2024 y la diferencia entre la variación nominal y la real.

![Pobreza monetaria por departamento, ENAHO 2024](../figuras/pobreza_departamento.png)

Se observa una dispersión amplia, desde 45.0% en Cajamarca hasta 6.0% en Ica.

![Mapa de la pobreza monetaria por departamento, ENAHO 2024](../mapas/pobreza_departamento.png)

El mapa permite ubicar territorialmente los departamentos con mayor pobreza (Cajamarca, Loreto, Puno) y los de menor pobreza (Ica, Moquegua, Madre de Dios).

![Gasto regional por habitante y pobreza, 2024](../figuras/cruce_gasto_pobreza.png)

La nube de puntos no muestra una pendiente positiva entre pobreza y gasto por habitante, y destaca el caso atípico de Lima Metropolitana.

## 5. Interpretación

Los datos indican que, en 2024, el gasto regional por habitante no se concentró en los territorios con mayor pobreza monetaria: la asociación es débil y negativa, con y sin Lima Metropolitana. Sin embargo, no puede concluirse que el gasto sea insuficiente o ineficiente, ni que la distribución obedezca a criterio alguno. Siguiendo esto, el gasto regional es solo una parte del gasto público en un territorio, y el gobierno nacional y los gobiernos locales ejecutan también recursos allí. En cuanto a la evolución, el crecimiento real de 34.92% entre 2019 y 2024 se refiere al total nacional y no indica a qué territorios llegó el aumento.

## 6. Limitaciones

Debe considerarse que el gasto abarca 2019-2024 mientras que la pobreza proviene de una sola ENAHO (2024), por lo que la evolución territorial no puede analizarse. Los niveles de agregación difieren: el gasto es administrativo (gobierno regional) y la pobreza es de los hogares residentes. El gasto está en soles corrientes, salvo la variación real calculada con el IPC de Lima Metropolitana, que puede no reflejar los precios de otros territorios. La población es la expandida de la encuesta y no una proyección oficial, y en algunos departamentos la muestra es reducida (columna `muestra` de salidas/cruce_territorios.csv). Lima Metropolitana es un caso atípico, y el resultado es una asociación descriptiva, no causal.

## 7. Reproducibilidad

Desde la raíz del repositorio se ejecutaron, en este orden:

- Herramientas MCP `bcrp`: `departamentos` (regionales y locales, 2024), `serie` (RD16629DA y PN38705PM, con guardar) y `resumen` (RD16629DA, 2019-2024).
- `uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024`
- `uv run .claude/skills/graficando-enaho/scripts/graficar.py --por departamento` y `--por area`
- `uv run .claude/skills/mapeando-enaho/scripts/mapear.py`
- `uv run .claude/skills/investigando-peru/scripts/cruzar.py --anio 2024`
- `uv run .claude/skills/investigando-peru/scripts/graficar_bcrp.py --codigo RD16629DA --desde 2019 --hasta 2024 --deflactor PN38705PM`

| Cifra del informe | Valor | Origen (serie y periodo, o archivo y fila) |
|---|---:|---|
| Gasto regional total 2019 | 33,755.12 | RD16629DA, 2019 |
| Gasto regional total 2024 | 56,575.52 | RD16629DA, 2024 |
| Variación nominal 2019-2024 | 67.61% | salidas/bcrp_resumen_RD16629DA.csv, variacion_nominal_pct |
| Variación de precios 2019-2024 | 24.23% | salidas/bcrp_resumen_RD16629DA.csv, PN38705PM |
| Variación real 2019-2024 | 34.92% | salidas/bcrp_resumen_RD16629DA.csv, variacion_real_pct |
| Pobreza nacional 2024 | 27.58% | salidas/indicadores.csv, nivel nacional; salidas/validacion.txt |
| Pobreza rural / urbana | 39.30% / 24.81% | salidas/indicadores.csv, nivel área |
| Gasto regional por habitante nacional | 1,640.69 | salidas/cruce_resumen.csv, gasto_regional_pc_nacional |
| Pobreza alta / baja (sin 15LM) | 2,233.46 / 2,433.20 | salidas/cruce_resumen.csv |
| Pobreza alta con 15LM | 1,210.19 | salidas/cruce_resumen.csv |
| Pearson / Spearman (26 territorios) | -0.161 / -0.128 | salidas/cruce_resumen.csv |
| Pearson / Spearman (sin 15LM) | -0.185 / -0.102 | salidas/cruce_resumen.csv |
| Pearson / Spearman gasto local (25) | -0.402 / -0.287 | salidas/cruce_resumen.csv |
| Gasto regional 15LM | 115.665 | RD16628DA, 2024 |

## 8. Verificación manual

| Afirmación | Valor del informe | Cómo verificarla | Resultado | Diferencia |
|---|---:|---|---|---|
| Gasto regional total 2024 | 56,575.52 millones | Consultar RD16629DA, 2024, en el portal del BCRP | pendiente de verificación manual | pendiente de verificación manual |
| Variación nominal 2019-2024 | 67.61% | Calcular 56,575.52 / 33,755.12 - 1 con los datos de RD16629DA | pendiente de verificación manual | pendiente de verificación manual |
| Pobreza nacional 2024 | 27.58% | Comparar con la cifra publicada por el INEI (27.6%) | pendiente de verificación manual | pendiente de verificación manual |
