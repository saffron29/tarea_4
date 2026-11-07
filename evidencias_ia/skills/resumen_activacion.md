# Demostraciones de activación y coordinación de las Skills

Corridas con `claude -p` (Sonnet) en una copia aislada del proyecto, sin servidores MCP, con salidas/ vacía al inicio. Registros completos en los .jsonl de esta carpeta.

### activacion_1_encadenamiento.jsonl

- Modelo: claude-sonnet-5-5 · servidores MCP: ninguno
- Skills activadas: mapeando-enaho, limpiando-enaho · herramientas MCP usadas: ninguna
- Turnos: 10 · tiempo: 29.8 s · costo informado: 0.1327 USD

Pasos:

1. `Skill: {"skill": "mapeando-enaho"}`
2. `Bash: cd "C:/Users/USER/AppData/Local/Temp/claude/ec29f026d20d029c/e1a1efca-5acd-4d78-af95-978724b4c191/scratchpad/skills_demo" && ls salidas datos referencias mapas 2>&1 | head -50`
3. `Skill: {"skill": "limpiando-enaho"}`
4. `Bash: cd "C:/Users/USER/AppData/Local/Temp/claude/ec29f026d20d029c/e1a1efca-5acd-4d78-af95-978724b4c191/scratchpad/skills_demo" && ls datos/966-Modulo02 datos/966-Modulo34 | head; ls datos/*.dta 2>&1`
5. `Bash: cd "C:/Users/USER/AppData/Local/Temp/claude/ec29f026d20d029c/e1a1efca-5acd-4d78-af95-978724b4c191/scratchpad/skills_demo" && ls datos/966-Modulo34; grep -n "dta\|datos" .claude/skills/limpiando-enaho/scripts/limpiar.py |`
6. `Bash: cd "C:/Users/USER/AppData/Local/Temp/claude/ec29f026d20d029c/e1a1efca-5acd-4d78-af95-978724b4c191/scratchpad/skills_demo" && uv run C:/Users/USER/AppData/Local/Temp/claude/ec29f026d20d029c/e1a1efca-5acd-4d78-af95-978724b`
7. `Bash: cd "C:/Users/USER/AppData/Local/Temp/claude/ec29f026d20d029c/e1a1efca-5acd-4d78-af95-978724b4c191/scratchpad/skills_demo" && uv run C:/Users/USER/AppData/Local/Temp/claude/ec29f026d20d029c/e1a1efca-5acd-4d78-af95-978724b`

Respuesta final:

> Hice el mapa de pobreza monetaria por departamento con la ENAHO 2024. Está en `mapas/pobreza_departamento.png`.
> 
> - **Datos:** `salidas/indicadores.csv` no existía, así que primero corrí la limpieza. Las 15 validaciones se aprobaron. La pobreza nacional es 27.58 %.
> - **Unión del mapa:** se unieron los 25 departamentos por código con el GeoJSON, sin ninguno sin dato. Lima y Callao están separados.
> - **Comparación con la referencia (Sesión 16):** coinciden los 25 de 25 departamentos, con diferencia máxima de 0.00 puntos. El detalle está en `salidas/comparacion_mapa.csv`.
> 
> | Más pobreza | % de personas | Menos pobreza | % de personas |
> |---|---|---|---|
> | Cajamarca | 45.0 | Ica | 6.0 |
> | Loreto | 43.0 | Moquegua | 11.0 |
> | Puno | 39.9 | Madre de Dios | 11.1 |
> 
> Pasco y Huánuco quedan empatados en 39.0 %, justo debajo de Puno.

### activacion_2_lenguaje_natural.jsonl

- Modelo: claude-sonnet-5-5 · servidores MCP: ninguno
- Skills activadas: graficando-enaho · herramientas MCP usadas: ninguna
- Turnos: 6 · tiempo: 17.3 s · costo informado: 0.0687 USD

Pasos:

1. `Skill: {"skill": "graficando-enaho"}`
2. `Bash: cd "C:/Users/USER/AppData/Local/Temp/claude/ec29f026d20d029c/e1a1efca-5acd-4d78-af95-978724b4c191/scratchpad/skills_demo" && ls && ls salidas figuras 2>&1 | head -30`
3. `Bash: cd "C:/Users/USER/AppData/Local/Temp/claude/ec29f026d20d029c/e1a1efca-5acd-4d78-af95-978724b4c191/scratchpad/skills_demo" && cat salidas/validacion.txt | head -30; uv run .claude/skills/graficando-enaho/scripts/graficar.`
4. `Read: {"file_path": "C:\\Users\\USER\\AppData\\Local\\Temp\\claude\\ec29f026d20d029c\\e1a1efca-5acd-4d78-af95-978724b4c191\\scratchpad\\skills_demo\\figuras\\pobreza_sexo.png"}`

Respuesta final:

> Prácticamente no hay diferencia de pobreza entre hombres y mujeres en la ENAHO 2024.
> 
> **Figura:** `figuras/pobreza_sexo.png`
> 
> **Título del gráfico:** «Mujeres y hombres tienen casi la misma pobreza: 0.3 puntos de diferencia»
> 
> | Sexo | Pobreza monetaria | Muestra (personas) |
> |---|---|---|
> | Mujer | 27.7 % | 56,077 |
> | Hombre | 27.4 % | 52,587 |
> | Promedio nacional | 27.6 % | |
> 
> - **Diferencia:** las mujeres tienen 0.3 puntos porcentuales más de pobreza. La brecha es muy pequeña y queda alrededor del promedio nacional.
> - **Significancia:** no calculé errores estándar ni intervalos de confianza, así que no puedo decir si 0.3 puntos es estadísticamente distinguible de cero. Con esta diferencia, lo más prudente es hablar de brecha mínima.
> - **Qué mide:** es la pobreza monetaria de personas, ponderada con `facpob07`. Las 15 validaciones de la limpieza se aprobaron.
> - **Alcance:** esta medida no capta desigualdades dentro del hogar, porque la pobreza monetaria se define a nivel de hogar. Todos sus miembros se clasifican igual.
> 
> Si quieres, puedo cruzar el sexo con área o con departamento. El script actual solo cubre cortes simples.

### activacion_3_invocacion_directa.jsonl

- Modelo: claude-sonnet-5-5 · servidores MCP: ninguno
- Skills activadas: graficando-enaho · herramientas MCP usadas: ninguna
- Turnos: 5 · tiempo: 14.3 s · costo informado: 0.0624 USD

Pasos:

1. `Skill: {"skill": "graficando-enaho", "args": "departamento"}`
2. `Bash: cd "C:/Users/USER/AppData/Local/Temp/claude/ec29f026d20d029c/e1a1efca-5acd-4d78-af95-978724b4c191/scratchpad/skills_demo" && ls salidas figuras 2>&1 | head -30`
3. `Bash: cd "C:/Users/USER/AppData/Local/Temp/claude/ec29f026d20d029c/e1a1efca-5acd-4d78-af95-978724b4c191/scratchpad/skills_demo" && cat salidas/validacion.txt | head -20; uv run C:/Users/USER/AppData/Local/Temp/claude/ec29f026d`

Respuesta final:

> Generé el gráfico de pobreza monetaria por departamento (ENAHO 2024). Las validaciones de `limpiando-enaho` ya estaban aprobadas (15 de 15).
> 
> **Figura:** `figuras/pobreza_departamento.png` (barras horizontales ordenadas desde cero, un solo color, valor en cada barra, línea del promedio nacional, 200 dpi).
> 
> **Título:** «Cajamarca (45.0 %) tiene 7.5 veces la pobreza de Ica (6.0 %)»
> 
> **Cifras principales** (% de personas, ponderadas):
> - **Más altas:** Cajamarca 45.0 %, Loreto 43.0 %, Puno 39.9 %, Pasco 39.0 % y Huánuco 39.0 %.
> - **Más bajas:** Ica 6.0 %, Moquegua 11.0 %, Madre de Dios 11.1 %, Lambayeque 14.0 % y Arequipa 15.8 %.
> - **Promedio nacional:** 27.6 %, que es la línea de referencia del gráfico. Lima (27.1 %), Tumbes (26.9 %) y Ucayali (27.1 %) quedan cerca de ese promedio.
> 
> Las 25 unidades (Callao separado de Lima) tienen entre 603 y 4,544 observaciones muestrales. Madre de Dios es la más pequeña, con 603, así que su cifra es menos precisa.

