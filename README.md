# Tarea 4 · Agente de investigación socioeconómica con el MCP del BCRP y Skills de la ENAHO

Frank Pinares Gutiérrez · Python Intermedio para CCSS y Gestión Pública (Q-LAB PUCP) · noviembre de 2026

**Pregunta de investigación:** ¿El gasto de los gobiernos regionales por habitante en 2024 fue mayor en los territorios con más pobreza monetaria, y cómo evolucionó ese gasto entre 2019 y 2024?

**Informe final:** [`informes/informe_final.md`](informes/informe_final.md)

| Resultado | Valor |
|---|---|
| Pruebas del servidor MCP | **12/12 aprobadas** (8 originales de la Sesión 04 sin cambios + 4 propias) |
| Pobreza monetaria nacional 2024 | **27.58%** (referencia INEI: 27.6%) |
| Residentes habituales | **108,664** |
| Unidades territoriales del mapa | **25/25** (iguales a la referencia de la Sesión 16) |
| Evaluación sin MCP ni Skills (Modo A) | **3/10** correctas |
| Evaluación con MCP y Skills (Modo B) | **8/10** correctas |

## 1. Objetivo

El presente proyecto construye un agente de investigación que responde preguntas sobre la realidad socioeconómica peruana con datos oficiales, siendo que las cifras no provienen de la memoria del modelo sino de herramientas que pueden repetirse y verificarse: un servidor MCP que consulta las series estadísticas del Banco Central de Reserva del Perú (BCRP) y cuatro Skills de Claude Code que procesan los microdatos de la ENAHO 2024 del INEI, los grafican, los mapean y los cruzan con el BCRP. El agente se aplica a una pregunta propia sobre el gasto de los gobiernos regionales y la pobreza, y su desempeño se evalúa con diez preguntas de respuesta conocida, con y sin dichas herramientas.

## 2. Arquitectura

```text
                     Pregunta en lenguaje natural
                                 │
                       Claude Code (el agente)
          ┌──────────────────────┼───────────────────────────┐
          ▼                      ▼                           ▼
   MCP «bcrp»              Skills de la ENAHO          Skill investigando-peru
   mcp/server.py           .claude/skills/             (coordina y cruza)
   · buscar_series         · limpiando-enaho  ──► salidas/indicadores.csv
   · serie (guardar)       · graficando-enaho ──► figuras/pobreza_*.png
   · resumen               · mapeando-enaho   ──► mapas/pobreza_departamento.png
   · correlacion
   · departamentos ──► salidas/bcrp_departamentos_*.csv ─┐
   · recursos y prompts                                   ├─► cruzar.py ──► salidas/cruce_*.csv
                                                          │                 figuras/cruce_gasto_pobreza.png
   serie(guardar=True) ──► salidas/bcrp_serie_*.csv ──────┴─► graficar_bcrp.py ──► figuras/bcrp_RD16629DA.png
                                                                        │
                                                         informes/informe_final.md
```

La regla de diseño, tomada de la Sesión 04, es que las cuentas las hace Python y no el modelo: cada cifra sale de una herramienta del MCP o de un archivo de `salidas/`, y el informe la cita con su serie o su archivo. Asimismo, toda unión entre fuentes se hace por código territorial (`ubigeo[:2]` = `FIRST_IDDP`) y nunca por nombre.

## 3. Herramientas del servidor MCP (`mcp/server.py`)

| Elemento | Tipo | Función |
|---|---|---|
| `buscar_series(texto, frecuencia, limite)` | Herramienta | Encuentra series oficiales por palabras clave en el catálogo del BCRP (17,167 series). |
| `serie(codigo, desde, hasta, guardar)` | Herramienta | Descarga los datos de una serie con la URL de la fuente; con `guardar=True` los escribe en `salidas/bcrp_serie_<codigo>.csv`. |
| `resumen(codigo, desde, hasta)` | Herramienta | Primer y último dato, cambio, variación, promedio, máximo y mínimo, calculados en Python. |
| `correlacion(codigo_a, codigo_b, desde, hasta)` | Herramienta propia | Correlación de Pearson entre dos series de la misma frecuencia, alineando periodos. |
| **`departamentos(grupo, anio, medida, guardar)`** | **Herramienta propia** | Valor de un indicador regional del BCRP en cada departamento **con su código de ubigeo**, tomado del GeoJSON oficial del curso, para unirlo con la ENAHO por código. Mantiene separados a la Municipalidad Metropolitana de Lima (`15LM`) y al Gobierno Regional de Lima (`15LP`) y comprueba que la suma coincida con la serie «Total» del BCRP. |
| `bcrp://serie/{codigo}` | Recurso | Ficha descriptiva de cualquier serie (nombre, categoría, frecuencia, cobertura). |
| `bcrp://grupos-departamentales` | Recurso | Los 52 grupos de series anuales con un dato por departamento. |
| `informe(tema)` e `investigacion(pregunta)` | Prompts | Plantillas reutilizables para informes con cifras verificables. |

Las pruebas están en `mcp/test_server.py` (las 8 originales de la Sesión 04, idénticas byte a byte al archivo del curso) y en `mcp/test_propias.py` (2 de `correlacion` y 2 de `departamentos`, que verifican la alineación de periodos, el rechazo de frecuencias distintas, los 26 territorios con Lima separada, el cuadre con el total del BCRP y los mensajes de error).

## 4. Skills (`.claude/skills/`)

| Skill | Qué hace | Salidas |
|---|---|---|
| `limpiando-enaho` | Lee los módulos 34 y 02 con las llaves como texto, filtra residentes habituales (`((p204 == 1) & (p205 == 2)) \| ((p204 == 2) & (p206 == 1))`), une personas y hogares con `validate="m:1"`, construye pobreza, área, departamento y territorio, pondera y escribe 15 verificaciones marcadas como `[APROBADA]` o `[FALLIDA]`; si falla una esencial, se detiene sin guardar. | `salidas/validacion.txt`, `salidas/indicadores.csv`, `salidas/personas_2024.parquet` |
| `graficando-enaho` | Gráficos ponderados por área, sexo, edad y departamento, con títulos analíticos calculados con los datos, período, unidad y fuente. | `figuras/pobreza_{area,sexo,edad,departamento}.png` |
| `mapeando-enaho` | Coroplético de 25 departamentos unido por código, con Lima y Callao separados, cuatro rangos fijos y comparación con la referencia de la Sesión 16. | `mapas/pobreza_departamento.png`, `salidas/comparacion_mapa.csv` |
| `investigando-peru` | Coordina el MCP y las Skills, cruza el gasto del BCRP con la pobreza y la población de la ENAHO por código de territorio, calcula la variación real del gasto y redacta el informe con su plantilla. | `salidas/cruce_*.csv`, `salidas/bcrp_resumen_*.csv`, `figuras/cruce_gasto_pobreza.png`, `figuras/bcrp_RD16629DA.png`, `informes/` |

Debe tenerse en cuenta la regla de ponderación: los indicadores territoriales (nacional, área, departamento, territorio) se calculan con la sumaria y el peso `factor07 × mieperho`, que es como se obtienen las cifras oficiales, mientras que los individuales (sexo y edad) se calculan con la base de personas y `facpob07`. Las Skills de gráficos, mapas e investigación ejecutan primero `limpiando-enaho` cuando no existe la base procesada; las demostraciones están en `evidencias_ia/skills/`. El estilo común de las figuras (tipografías Montserrat e Inter, con licencia SIL Open Font License) está en `recursos/`.

## 5. Fuentes y descarga de los datos

| Fuente | Datos | Enlace |
|---|---|---|
| INEI | ENAHO 2024, módulo 34 (sumaria) | https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo34.zip |
| INEI | ENAHO 2024, módulo 02 (miembros) | https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo02.zip |
| Repositorio del curso | Límites departamentales (incluido en `datos/`) | https://raw.githubusercontent.com/d2cml-ai/Data-Science-Python/main/sessions/06-geoespacial/lab/Data/peru_departamental_simple.geojson |
| Repositorio del curso | Referencia departamental de la Sesión 16 (incluida en `referencias/`) | https://github.com/d2cml-ai/Data-Science-Python/tree/main/sessions/16-skills-enaho/referencias |
| BCRP | Series estadísticas (API y catálogo, se descargan solos) | https://estadisticas.bcrp.gob.pe/estadisticas/series/ |

Las series del BCRP usadas en la investigación son el gasto no financiero de los gobiernos regionales por departamento (`RD16603DA` a `RD16628DA`) y total (`RD16629DA`), el de los gobiernos locales por departamento (`RD16551DA` a `RD16575DA`) y el índice de precios al consumidor de Lima Metropolitana (`PN38705PM`, diciembre de 2021 = 100). Los microdatos, el catálogo del BCRP y la base `personas_2024.parquet` no se suben al repositorio (ver `.gitignore`).

## 6. Instalación con `uv`

```bash
git clone https://github.com/saffron29/tarea_4.git
cd tarea_4
uv sync                                   # Python 3.14 y dependencias (fastmcp, pandas, pyarrow, geopandas, matplotlib, pytest)

# Microdatos de la ENAHO 2024 (unos 21 MB comprimidos y 74 MB descomprimidos)
curl -L -o datos/966-Modulo34.zip https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo34.zip
curl -L -o datos/966-Modulo02.zip https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo02.zip
unzip datos/966-Modulo34.zip -d datos && unzip datos/966-Modulo02.zip -d datos
# En PowerShell: Expand-Archive datos\966-Modulo34.zip datos; Expand-Archive datos\966-Modulo02.zip datos
```

El catálogo del BCRP (`datos/catalogo_bcrp.csv`, unos 7 MB) se descarga automáticamente la primera vez que se usa el servidor.

## 7. Conectar el MCP a Claude Code

El servidor está registrado en `.mcp.json` con alcance de proyecto. Por seguridad, Claude Code no ejecuta los servidores de un repositorio recién clonado sin el consentimiento de quien lo abre, de modo que la primera vez se debe aprobar:

```bash
claude                  # al abrirlo en la raíz, aceptar el servidor «bcrp» que propone .mcp.json (una sola vez)
                        # luego, dentro de la sesión, /mcp debe mostrar «bcrp · connected»
claude mcp list         # antes de aprobarlo muestra «Pending approval»; después, «Connected»
```

Para usarlo sin interfaz, por ejemplo en evaluaciones: `claude -p "..." --strict-mcp-config --mcp-config .mcp.json --allowedTools mcp__bcrp`.

## 8. Reproducir el procesamiento y las pruebas

```bash
uv run pytest -v                                                          # 12 pruebas del MCP
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024      # validación e indicadores
uv run .claude/skills/graficando-enaho/scripts/graficar.py --por area     # también sexo, edad y departamento
uv run .claude/skills/mapeando-enaho/scripts/mapear.py                    # mapa y comparación con la Sesión 16
uv run evaluacion/verdades.py                                             # respuestas esperadas independientes
uv run evaluacion/evaluar.py --modos A B --trabajo <carpeta temporal>     # experimento (requiere Claude Code)
```

El cruce y el gráfico del BCRP requieren que antes el MCP haya guardado sus datos, lo que hace el agente con la Skill `investigando-peru` (ver la sección 11); también puede hacerse desde Python llamando a `departamentos(..., guardar=True)` y `serie(..., guardar=True)` y luego:

```bash
uv run .claude/skills/investigando-peru/scripts/cruzar.py --anio 2024
uv run .claude/skills/investigando-peru/scripts/graficar_bcrp.py --codigo RD16629DA --desde 2019 --hasta 2024 --deflactor PN38705PM
```

## 9. Resultados de la evaluación

Se formularon diez preguntas (cuatro del BCRP, cuatro de la ENAHO y dos que combinan ambas fuentes), cuyas respuestas esperadas calculó `evaluacion/verdades.py` por caminos independientes del agente y que quedaron congeladas antes de la primera corrida (commit `d3731a7`). Cada pregunta se ejecutó en una sesión independiente, con el mismo modelo (`claude-sonnet-5-5`) y la misma instrucción.

| Indicador | Modo A (sin MCP ni Skills) | Modo B (con MCP y Skills) | B2 (tras corregir descripciones) |
|---|---:|---:|---:|
| Correctas | 3 | **8** | 7 |
| Incorrectas | 1 | 0 | 0 |
| Sin respuesta | 6 | 2 | 3 |
| Tiempo promedio | 5.6 s | 21.4 s | 23.5 s |
| Costo informado (10 preguntas) | 0.14 USD | 0.83 USD | 0.78 USD |

El MCP del BCRP respondió correctamente las cuatro preguntas del BCRP en ambos modos con herramientas, mientras que sin él el agente se equivocó en el crecimiento del PBI (3.3% frente a 3.5153%). Las Skills produjeron cifras exactas cuando se activaron, aunque su activación ante preguntas breves fue irregular, y en ningún caso con herramientas el agente presentó una cifra incorrecta: cuando no pudo calcularla, lo dijo. El análisis completo está en [`evaluacion/comparacion.md`](evaluacion/comparacion.md) y los datos en [`evaluacion/resultados.csv`](evaluacion/resultados.csv).

## 10. Limitaciones y problemas encontrados

En cuanto a la investigación, el cruce territorial se limita a 2024 porque se dispone de una sola ENAHO, el gasto se mide en soles corrientes (salvo la variación real, deflactada con el IPC de Lima), la población por habitante es la expandida de la encuesta y no una proyección oficial, y la relación entre gasto y pobreza es una asociación descriptiva entre 26 territorios, no causal. Asimismo, al separar Lima, la Municipalidad Metropolitana de Lima registra un gasto «regional» de apenas 11.2 soles por habitante, por lo que todos los resultados se reportan con y sin ese territorio.

Por otra parte, durante el desarrollo se encontraron y corrigieron varios problemas, todos documentados en las evidencias: un doble redondeo que hacía diferir dos departamentos de la referencia en una décima; un título de gráfico escrito a mano con una cifra incorrecta («once» departamentos en lugar de diez), tras lo cual todos los títulos pasaron a calcularse con los datos; una comparación por grupos en la que Lima Metropolitana, por estar 0.004 puntos sobre el promedio nacional, distorsionaba el resultado; una primera ejecución integrada en la que el agente corrió los scripts de la ENAHO por Bash en lugar de invocar sus Skills; y, finalmente, la activación irregular de las Skills en la evaluación, que se reporta sin ocultarla.

## 11. Ejemplo de una ejecución completa

Con `salidas/`, `figuras/`, `mapas/` e `informes/` vacías, se ejecutó:

```bash
claude -p "Investiga con datos oficiales la siguiente pregunta y deja un informe reproducible en informes/informe_final.md: ¿El gasto de los gobiernos regionales por habitante en 2024 fue mayor en los territorios con más pobreza monetaria, y cómo evolucionó ese gasto entre 2019 y 2024? Usa el servidor MCP del BCRP y las skills de la ENAHO de este proyecto; prepara primero un plan." \
  --model sonnet --strict-mcp-config --mcp-config .mcp.json --output-format stream-json --verbose
```

En una sola sesión de 23 turnos el agente escribió `informes/plan.md`; consultó el MCP con `departamentos` (gasto regional y local de 2024), `serie` (gasto total 2015-2025 e IPC) y `resumen` (2019-2024); invocó las Skills `investigando-peru`, `limpiando-enaho` (15 de 15 verificaciones), `graficando-enaho` y `mapeando-enaho` (25 de 25 departamentos); ejecutó `cruzar.py` y `graficar_bcrp.py`, y redactó `informes/informe_final.md`. El registro completo y su resumen están en [`evidencias_ia/integracion/`](evidencias_ia/integracion/). Los tres hallazgos son que el gasto regional creció 67.6% nominal y 34.9% real entre 2019 y 2024; que la pobreza de 2024 va de 6.0% en Ica a 45.0% en Cajamarca; y que la mayor pobreza no se acompaña de mayor gasto regional por habitante (2,233 frente a 2,433 soles sin Lima Metropolitana; correlaciones entre −0.10 y −0.18). Cuatro de sus cifras fueron verificadas manualmente por el autor (sección 8 del informe).

## 12. Evidencias del uso de inteligencia artificial

El proyecto se desarrolló con Claude Code como asistente. En la carpeta [`evidencias_ia/`](evidencias_ia/) se encuentran las conversaciones completas exportadas a Markdown, con la información sensible oculta, y los registros de todas las ejecuciones del agente; su índice está en [`evidencias_ia/README.md`](evidencias_ia/README.md).

```text
tarea_4/
├── README.md · pyproject.toml · uv.lock · .mcp.json · .gitignore · .python-version
├── mcp/                 server.py · test_server.py (8 originales) · test_propias.py (4 propias)
├── .claude/skills/      limpiando-enaho · graficando-enaho · mapeando-enaho · investigando-peru
├── recursos/            estilo.py · fuentes/ (Inter y Montserrat, OFL)
├── scripts/             resumir_registro.py · exportar_conversaciones.py
├── datos/               GeoJSON (los microdatos se descargan; ver la sección 6)
├── referencias/         pobreza_departamento_2024.csv de la Sesión 16
├── salidas/             validacion.txt · indicadores.csv · comparacion_mapa.csv · bcrp_*.csv · cruce_*.csv · pruebas_mcp.txt
├── figuras/ · mapas/
├── evaluacion/          preguntas.csv · verdades.py · evaluar.py · resultados.csv · resultados_b2.csv · comparacion.md
├── informes/            plan.md · informe_final.md
└── evidencias_ia/       mcp/ · skills/ · integracion/ · evaluacion/ · conversaciones/
```
