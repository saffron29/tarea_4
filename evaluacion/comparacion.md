# Comparación del agente sin y con el MCP del BCRP y las Skills de la ENAHO

## 1. Diseño del experimento

El presente documento compara el desempeño de Claude Code al responder diez preguntas con respuesta verificable bajo dos condiciones equivalentes, siendo que la única diferencia entre ellas consiste en el acceso al servidor MCP del BCRP y a las Skills del proyecto. Las preguntas se distribuyen en cuatro del BCRP (B1 a B4), cuatro de la ENAHO 2024 (E1 a E4) y dos que combinan ambas fuentes (M1 y M2), y se encuentran, junto con sus respuestas esperadas y tolerancias, en `evaluacion/preguntas.csv`. Debe tenerse en cuenta que dichas respuestas no provienen del agente: fueron calculadas por `evaluacion/verdades.py`, que consulta directamente la API del BCRP sin pasar por el MCP y recalcula la ENAHO desde los archivos `.dta` sin reutilizar el código de las Skills, y quedaron congeladas en el commit `d3731a7`, antes de la primera corrida.

Ahora bien, ambos modos se ejecutaron con el mismo modelo (`claude-sonnet-5-5`), la misma instrucción (responder con un solo número en un JSON con valor, unidad, fuente e interpretación, y devolver `null` antes que estimar) y una sesión independiente por pregunta, mediante `evaluacion/evaluar.py`. En el **Modo A** cada pregunta corrió en una carpeta vacía y nueva, con `--tools ""` y `--strict-mcp-config`, de modo que el agente no disponía de ninguna herramienta, no podía leer archivos con respuestas ni cargar memorias del proyecto; la única herramienta presente en el registro es `StructuredOutput`, que corresponde al formato de salida. En el **Modo B** cada pregunta corrió en una copia del repositorio sin las carpetas `evaluacion/`, `informes/` y `evidencias_ia/` ni el `README.md`, y con `salidas/`, `figuras/` y `mapas/` vacías antes de cada pregunta, de forma que ninguna cifra podía leerse ya calculada; el agente disponía del MCP `bcrp`, de las cuatro Skills y de las herramientas de archivos, con permiso para ejecutar únicamente `uv run` (los scripts del proyecto) y algunos comandos de lectura. Los registros completos de las treinta corridas se encuentran en `evidencias_ia/evaluacion/`.

Por otra parte, tras analizar el Modo B se corrigieron las descripciones de dos Skills (commit `3dd5c40`) y se repitió únicamente ese modo como **B2**, sin modificar las preguntas ni las respuestas esperadas. Por ello, el resultado oficial del experimento es el del Modo B, mientras que B2 se reporta como un análisis adicional de cómo cambia la calidad de las respuestas al ajustar la activación de las Skills.

## 2. Resultados por pregunta

| Pregunta | Esperado | Modo A (sin MCP ni Skills) | Modo B (con MCP y Skills) | B2 (descripciones corregidas) |
|---|---:|---|---|---|
| B1 · Inflación de Lima, dic. 2024 (%) | 1.9663 | ✅ 1.97 (memoria) | ✅ 1.9663 (`resumen`) | ✅ 1.9663 (`buscar_series`, `serie`) |
| B2 · Tasa de referencia, dic. 2024 (%) | 5.00 | ✅ 5.00 (memoria) | ✅ 5.00 (`resumen`) | ✅ 5.00 (`resumen`) |
| B3 · Crecimiento del PBI 2024 (%) | 3.5153 | ❌ 3.30 (memoria) | ✅ 3.5153 (`buscar_series`, `serie`) | ✅ 3.50 (`buscar_series`, `serie`) |
| B4 · Gasto regional total 2024 (millones de S/) | 56,575.52 | ⚪ sin respuesta | ✅ 56,575.52 (`departamentos`) | ✅ 56,575.52 (`departamentos`) |
| E1 · Pobreza nacional 2024 (%) | 27.58 | ✅ 27.6 (memoria) | ✅ 27.6 (memoria) | ✅ 27.6 (memoria) |
| E2 · Pobreza rural 2024 (%) | 39.30 | ⚪ sin respuesta | ⚪ sin respuesta | ⚪ sin respuesta |
| E3 · Pobreza de Puno 2024 (%) | 39.94 | ⚪ sin respuesta | ✅ 39.94 (script de limpieza) | ⚪ sin respuesta |
| E4 · Pobreza de 0 a 17 años (%) | 36.47 | ⚪ sin respuesta | ✅ 36.47 (script de limpieza) | ⚪ sin respuesta |
| M1 · Gasto regional por habitante, Cajamarca (S/) | 2,439.82 | ⚪ sin respuesta | ⚪ sin respuesta | ✅ 2,439.82 (`investigando-peru`, `limpiando-enaho`, `departamentos`) |
| M2 · Correlación gasto-pobreza, 26 territorios | −0.1607 | ⚪ sin respuesta | ✅ −0.1607 (`limpiando-enaho`, `departamentos`) | ✅ −0.1607 (`limpiando-enaho`, `departamentos`) |

## 3. Métricas

| Indicador | Modo A | Modo B | B2 |
|---|---:|---:|---:|
| Respuestas correctas | **3** | **8** | **7** |
| Respuestas incorrectas | 1 | 0 | 0 |
| Sin respuesta | 6 | 2 | 3 |
| Correctas del BCRP / ENAHO / mixtas | 2 / 1 / 0 | 4 / 3 / 1 | 4 / 1 / 2 |
| Tiempo promedio por pregunta | 5.6 s | 21.4 s | 23.5 s |
| Turnos promedio | 2.0 | 6.1 | 7.1 |
| Llamadas a herramientas por pregunta | 0 | 4.0 | 4.8 |
| Costo informado de las diez preguntas | 0.14 USD | 0.83 USD | 0.78 USD |

Se observa, en primer lugar, que el acceso a las herramientas elevó las respuestas correctas de tres a ocho y eliminó la única respuesta incorrecta, a cambio de un tiempo cerca de cuatro veces mayor y un costo cerca de seis veces mayor. Las preguntas que mejoraron del Modo A al Modo B fueron B3, B4, E3, E4 y M2; ninguna empeoró. En el caso de las preguntas mixtas, la revisión automática de `evaluar.py` señaló que todas las respuestas mencionan ambas fuentes; asimismo, marcó «lenguaje causal» en la interpretación de M1 del Modo B, si bien la revisión manual del autor determinó que se trata de un falso positivo, pues la palabra «porque» se refiere al bloqueo de permisos y no a una relación entre gasto y pobreza. La interpretación de M2 del Modo B, por su parte, precisa expresamente que se trata de «una asociación descriptiva, no causal».

## 4. Principales errores encontrados

**Respuestas de memoria.** Sin herramientas, el agente acertó únicamente las cifras más difundidas (la inflación de diciembre, la tasa de referencia y el 27.6% de pobreza que publica el INEI) y se equivocó en el crecimiento del PBI de 2024, para el que respondió 3.3% en lugar de 3.5153% (`PM04863AA`). Ahora bien, debe destacarse que en las otras seis preguntas reconoció no poder responder sin estimar, lo que muestra que la instrucción de devolver `null` redujo las cifras inventadas. Por otra parte, en los modos B y B2 la pregunta E1 también se respondió de memoria, aunque el agente declaró en la fuente que no recalculó la cifra; el valor es correcto, pero no proviene de las herramientas.

**Activación irregular de la Skill de limpieza.** Las respuestas faltantes de los modos B y B2 tienen una misma causa: ante preguntas que piden «solo un número» de la ENAHO, el agente no siempre activó `limpiando-enaho` e intentó escribir su propio código en Python para leer los microdatos. Como el modo solo autoriza `uv run`, el sistema de permisos bloqueó esos intentos (9 negaciones en el Modo B y 14 en B2) y el agente, en lugar de completar la cifra, respondió `null` y explicó el bloqueo. Es decir, el diseño de permisos impidió cálculos improvisados no validados, pero también evidenció que la descripción de la Skill no basta para garantizar su uso. Asimismo, en E3 y E4 del Modo B el agente acertó ejecutando el script de la Skill directamente por Bash, sin invocarla como tal.

**Variabilidad entre corridas.** La corrección de las descripciones resolvió M1, que en B2 activó `investigando-peru` y `limpiando-enaho` y obtuvo el valor exacto, pero E3 y E4, que en el Modo B se habían acertado, quedaron sin respuesta en B2. Siguiendo esto, la activación de las Skills ante preguntas breves debe considerarse probabilística, por lo que una sola corrida por pregunta no permite afirmar que una versión sea mejor que otra; por esa misma razón no se siguieron ajustando las descripciones en función de estas diez preguntas, lo que equivaldría a sobreajustar el sistema a la prueba.

## 5. Conclusión

Una primera conclusión de la presente evaluación es que el servidor MCP del BCRP mejora de manera consistente la calidad de las respuestas: en los modos B y B2 las cuatro preguntas del BCRP se respondieron con la cifra oficial, citando el código de la serie, y la herramienta propia `departamentos` resolvió preguntas que sin ella no tenían respuesta (B4). En ese sentido, las cifras dejan de depender de lo que el modelo recuerda y pasan a depender de una llamada que puede repetirse y verificarse. Por otra parte, las Skills de la ENAHO producen resultados exactos cuando se activan, como en E3, E4, M1 y M2, cuyos valores coinciden con el cálculo independiente al redondearlos (39.94 frente a 39.9381 en E3, 2,439.82 frente a 2,439.8152 en M1 y −0.1607 en M2); sin embargo, su activación ante preguntas breves es irregular, lo que constituye la principal limitación del sistema y la principal línea de mejora (por ejemplo, mediante un comando explícito o una instrucción general del proyecto que obligue a usarlas). Debe considerarse, finalmente, que en ninguna corrida con herramientas el agente presentó una cifra incorrecta: cuando no pudo calcularla, lo dijo. De esta forma, el MCP y las Skills no solo aumentan los aciertos, sino que vuelven verificables las respuestas y reducen el riesgo de cifras inventadas, a cambio de más tiempo y costo por pregunta.

## 6. Limitaciones del experimento

Se trata de diez preguntas y una sola corrida por pregunta y modo, por lo que los porcentajes de acierto son sensibles a la variabilidad del modelo, como muestra la comparación entre B y B2. Asimismo, algunas respuestas esperadas son cifras públicas que el modelo puede conocer de antemano (E1, B1, B2), lo que favorece al Modo A en esas preguntas. Por último, la calificación de las preguntas mixtas combina una revisión automática (ambas fuentes y ausencia de lenguaje causal) con la revisión manual del autor, que corrigió el falso positivo señalado.

## 7. Archivos

- `evaluacion/preguntas.csv`: preguntas, respuestas esperadas, tolerancias y procedimiento de verificación.
- `evaluacion/verdades.py`: cálculo independiente de las respuestas esperadas.
- `evaluacion/evaluar.py`: ejecución de ambos modos y calificación.
- `evaluacion/resultados.csv`: resultados oficiales (modos A y B), con respuesta, fuente, herramientas, tiempo, turnos, costo y errores.
- `evaluacion/resultados_b2.csv`: segunda corrida del Modo B tras corregir las descripciones.
- `evidencias_ia/evaluacion/`: registros completos de las treinta corridas (`A_*.jsonl`, `B_*.jsonl`, `B2_*.jsonl`).
