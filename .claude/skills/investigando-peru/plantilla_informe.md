# Plantilla del informe final (informes/informe_final.md)

## Reglas de redacción (obligatorias)

- Voz impersonal con «se» y «el presente informe»; nunca primera persona ni «nosotros».
- Prosa en párrafos completos, con subordinadas y conectores: «Ahora bien», «Siguiendo esto», «Sin embargo», «Asimismo», «Por otra parte», «En ese sentido», «De esta forma», «Es decir», «si bien… también», «debe considerarse que».
- Pocas viñetas: solo en las tablas y en la lista de archivos de reproducibilidad.
- Porcentajes sin espacio (27.6%), punto decimal, miles con coma (56,575.5).
- Cada cifra lleva su origen entre paréntesis la primera vez que aparece: la serie del BCRP con su periodo (RD16629DA, 2024) o el archivo de salidas/ (salidas/cruce_resumen.csv).
- Nada de causalidad: «se asocia», «coincide con», «no se acompaña de»; nunca «causa», «provoca», «explica» ni «se explica por», tampoco para descomponer una variación (se escribe «la variación real equivale a cerca de la mitad de la nominal»).
- Cuidar el sentido de las frases de asociación: lo que se pregunta es si donde hay más pobreza hay más gasto, por lo que se escribe «la mayor pobreza no se acompaña de mayor gasto por habitante», no al revés.

## Estructura

```markdown
# <Título analítico que resuma el hallazgo principal>

<Autor: Frank Pinares Gutiérrez · fecha de elaboración · Tarea 4, Python Intermedio para CCSS y Gestión Pública>

## 1. Pregunta de investigación
Tema, objetivo y delimitación (2024 para el cruce territorial; 2019-2024 para la evolución; 26 territorios con
Lima Metropolitana y Lima Provincias separadas).

## 2. Fuentes y metodología
BCRP (series y herramientas MCP usadas), ENAHO 2024 (módulos 34 y 02, ponderadores, validaciones), cómo se unen
(código de territorio), cómo se calcula el gasto por habitante y la variación real, y qué skills se ejecutaron.

## 3. Resultados
Al menos tres hallazgos, cada uno con su párrafo y sus cifras rastreables:
### 3.1 <Evolución del gasto regional 2019-2024, nominal y real>
### 3.2 <Distribución territorial de la pobreza 2024>
### 3.3 <Relación entre gasto regional por habitante y pobreza, con y sin Lima Metropolitana>

## 4. Visualizaciones
![...](../figuras/bcrp_RD16629DA.png)          — gráfico del BCRP
![...](../figuras/pobreza_departamento.png)    — gráfico de la ENAHO
![...](../mapas/pobreza_departamento.png)      — mapa departamental
![...](../figuras/cruce_gasto_pobreza.png)     — cruce de ambas fuentes
Una o dos líneas de lectura debajo de cada figura.

## 5. Interpretación
Qué patrones se observan y qué no puede concluirse.

## 6. Limitaciones
Cobertura temporal (gasto 2019-2024 frente a una sola ENAHO, 2024), niveles de agregación distintos, soles
corrientes y deflactor de Lima, población expandida de la encuesta, muestra pequeña en algunos departamentos
(columna muestra), caso atípico de Lima Metropolitana, y asociación no causal.

## 7. Reproducibilidad
Comandos, scripts, herramientas MCP y series usadas, y una tabla de trazabilidad:

| Cifra del informe | Valor | Origen (serie y periodo, o archivo y fila) |
|---|---:|---|

## 8. Verificación manual
Tabla para que el autor compruebe al menos tres cifras (dos del BCRP y una de la ENAHO) por un camino distinto:

| Afirmación | Valor del informe | Cómo verificarla | Resultado | Diferencia |
|---|---:|---|---|---|
(las columnas «Resultado» y «Diferencia» quedan como «pendiente de verificación manual»)
```
