# Demostraciones de activación y coordinación de las Skills

Corridas con `claude -p` (Sonnet) sobre la versión final del proyecto, en una copia aislada, sin servidores MCP y con salidas/, figuras/ y mapas/ vacías al inicio. Registros completos en los .jsonl de esta carpeta.

### activacion_1_encadenamiento.jsonl

- Modelo: claude-sonnet-5-5 · servidores MCP: ninguno
- Skills activadas: mapeando-enaho, limpiando-enaho · herramientas MCP usadas: ninguna
- Turnos: 8 · tiempo: 29.0 s · costo informado: 0.1232 USD

Pasos:

1. `Skill: {"skill": "mapeando-enaho", "args": "Mapa de la pobreza monetaria por departamento con ENAHO 2024"}`
2. `Bash: cd "~/AppData/Local/Temp/claude/ec29f026d20d029c/e1a1efca-5acd-4d78-af95-978724b4c191/scratchpad/skills_demo2" && ls salidas datos referencias mapas 2>&1 | head -50`
3. `Skill: {"skill": "limpiando-enaho"}`
4. `Bash: cd "~/AppData/Local/Temp/claude/ec29f026d20d029c/e1a1efca-5acd-4d78-af95-978724b4c191/scratchpad/skills_demo2" && find datos -name "*.dta" | head; uv run ~/AppData/Local/Temp/claude/ec29f026d20d02`
5. `Bash: cd "~/AppData/Local/Temp/claude/ec29f026d20d029c/e1a1efca-5acd-4d78-af95-978724b4c191/scratchpad/skills_demo2" && uv run ~/AppData/Local/Temp/claude/ec29f026d20d029c/e1a1efca-5acd-4d78-af95-978724`

Respuesta final:

> Hice el mapa de pobreza monetaria por departamento con la ENAHO 2024 y lo guardé en `mapas/pobreza_departamento.png`.
> 
> Las 15 verificaciones de limpieza se aprobaron. Los 25 departamentos se unieron por código, con Lima y Callao separados, y no quedó ninguno sin dato. Los 25 coinciden con la referencia de la Sesión 16, con diferencia máxima de 0.00 puntos. La comparación está en `salidas/comparacion_mapa.csv`.
> 
> Las cifras salen de `salidas/indicadores.csv`, como % de personas en pobreza monetaria.
> 
> | Posición | Más pobreza | % | Menos pobreza | % |
> |---|---|---|---|---|
> | 1 | Cajamarca | 45.0 | Ica | 6.0 |
> | 2 | Loreto | 43.0 | Moquegua | 11.0 |
> | 3 | Puno | 39.9 | Madre de Dios | 11.1 |
> 
> - **Lima:** el mapa muestra a Lima con 27.1 %. Esa cifra incluye Lima Metropolitana y Lima Provincias.
> - **Pasco y Huánuco:** quedan empatados en 39.0 %, justo debajo de Puno.
> 
> No revisé visualmente el PNG, así que no puedo confirmar cómo se ve el recuadro ampliado de Lima y Callao.

### activacion_2_lenguaje_natural.jsonl

- Modelo: claude-sonnet-5-5 · servidores MCP: ninguno
- Skills activadas: graficando-enaho · herramientas MCP usadas: ninguna
- Turnos: 6 · tiempo: 18.3 s · costo informado: 0.0721 USD

Pasos:

1. `Skill: {"skill": "graficando-enaho", "args": "Pobreza monetaria por sexo, ENAHO 2024"}`
2. `Bash: cd "~/AppData/Local/Temp/claude/ec29f026d20d029c/e1a1efca-5acd-4d78-af95-978724b4c191/scratchpad/skills_demo2" && ls salidas figuras 2>&1 | head -30`
3. `Bash: cd "~/AppData/Local/Temp/claude/ec29f026d20d029c/e1a1efca-5acd-4d78-af95-978724b4c191/scratchpad/skills_demo2" && cat salidas/validacion.txt | head -20; uv run .claude/skills/graficando-enaho/scripts/graficar`
4. `Read: {"file_path": "~\\AppData\\Local\\Temp\\claude\\ec29f026d20d029c\\e1a1efca-5acd-4d78-af95-978724b4c191\\scratchpad\\skills_demo2\\figuras\\pobreza_sexo.png"}`

Respuesta final:

> Según la ENAHO 2024, la pobreza monetaria de hombres y mujeres es casi la misma. La diferencia es de 0.3 puntos porcentuales.
> 
> **Figura:** `figuras/pobreza_sexo.png`
> 
> **Título del gráfico:** «Mujeres y hombres tienen casi la misma pobreza: 0.3 puntos de diferencia»
> 
> | Grupo | Pobreza monetaria (% de personas) | Muestra |
> |---|---|---|
> | Mujeres | 27.7 % | 56,077 |
> | Hombres | 27.4 % | 52,587 |
> | Promedio nacional | 27.6 % | |
> 
> - **Interpretación:** las mujeres están 0.3 puntos por encima de los hombres. Esa brecha es pequeña y no la probé estadísticamente. No hay evidencia de una brecha de pobreza por sexo en este indicador.
> - **Qué mide:** es la pobreza de las personas según su sexo, y se asigna igual a todos los miembros del hogar. Por eso no capta desigualdades dentro del hogar, como el acceso a ingresos propios o la carga de trabajo no remunerado. Las brechas de género suelen aparecer en esos otros indicadores.
> - **Método:** las cifras están ponderadas con `facpob07`. Los datos pasaron las 15 verificaciones de validación, y la pobreza nacional salió 27.6 %, igual a la referencia.

### activacion_3_invocacion_directa.jsonl

- Modelo: claude-sonnet-5-5 · servidores MCP: ninguno
- Skills activadas: graficando-enaho · herramientas MCP usadas: ninguna
- Turnos: 5 · tiempo: 14.7 s · costo informado: 0.0571 USD

Pasos:

1. `Skill: {"skill": "graficando-enaho", "args": "departamento"}`
2. `Bash: cd "~/AppData/Local/Temp/claude/ec29f026d20d029c/e1a1efca-5acd-4d78-af95-978724b4c191/scratchpad/skills_demo2" && ls salidas/indicadores.csv figuras 2>&1 | head`
3. `Bash: cd "~/AppData/Local/Temp/claude/ec29f026d20d029c/e1a1efca-5acd-4d78-af95-978724b4c191/scratchpad/skills_demo2" && uv run ~/AppData/Local/Temp/claude/ec29f026d20d029c/e1a1efca-5acd-4d78-af95-978724`

Respuesta final:

> Generé el gráfico por departamento.
> 
> **Figura:** `figuras/pobreza_departamento.png` (200 dpi)
> 
> **Título que imprimió el script:** «10 de 25 departamentos superan el promedio nacional de pobreza; mayor Cajamarca (45.0 %), menor Ica (6.0 %)».
> 
> **Cifras principales** (% de personas en pobreza monetaria, ponderadas, de `salidas/indicadores.csv`):
> - **Más altos:** Cajamarca 45.0 %, Loreto 43.0 %, Puno 39.9 %, Pasco 39.0 % y Huánuco 39.0 %.
> - **Más bajos:** Ica 6.0 %, Moquegua 11.0 %, Madre de Dios 11.2 % y Lambayeque 14.0 %.
> - **Lima y Callao:** Lima 27.1 % y Callao 33.9 %.
> 
> La forma del gráfico es la distancia de cada departamento al promedio nacional. Los que están por encima van en terracota y los que están por debajo, en gris.

