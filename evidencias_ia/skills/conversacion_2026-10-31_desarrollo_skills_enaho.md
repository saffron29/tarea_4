# Desarrollo de las Skills de la ENAHO (repositorio enaho-skills, 31 de octubre de 2026)

Exportación de la sesión `50afee40-1161-4293-b4a9-85c2739871ed` de Claude Code. Se ocultaron correos, teléfonos, DNI, tokens, rutas personales, el contexto interno del sistema y el contenido de la memoria personal del asistente.

## Usuario · 2026-10-31 13:46

Por favor, ayúdame a responder la siguiente pregunta basándote en el contenido de las clases de Python Intermedio para CCSS y Gestión Pública disponible en el contenido de las carpetas y documentos de las siguientes rutas:

"~\Desktop\Documentos Frank\2026-1\Diplomatura de Especialización en Ciencia de Datos\Curso de Capacitación en Fundamentos de Python para CCSS y Gestión Pública"
"~\Desktop\Documentos Frank\2026-1\Diplomatura de Especialización en Ciencia de Datos\Curso de Capacitación en Fundamentos de Python para CCSS y Gestión Pública\Clases"
"~\Desktop\Documentos Frank\2026-1\Diplomatura de Especialización en Ciencia de Datos\Curso de Capacitación en Fundamentos de Python para CCSS y Gestión Pública\Chats"
"~\Desktop\Documentos Frank\2026-1\Diplomatura de Especialización en Ciencia de Datos\Curso de Capacitación en Python Intermedio para CCSS y Gestión Pública"
"~\Desktop\Documentos Frank\2026-1\Diplomatura de Especialización en Ciencia de Datos\Curso de Capacitación en Python Intermedio para CCSS y Gestión Pública\Chats"
"~\Desktop\Documentos Frank\2026-1\Diplomatura de Especialización en Ciencia de Datos\Curso de Capacitación en Python Intermedio para CCSS y Gestión Pública\Clases"

Asimismo, de ser necesario puedes revisar el código de otros ejercicios que he realizado y subido a GitHub, en la siguiente ruta:
"~\Documents\GitHub"
"~\Documents\GitHub\Data-Science-Python"

Responde de forma didáctica, precisa y suficientemente desarrollada, respetando los conceptos, métodos y notación utilizados en clases. Cuando corresponda, incluye el procedimiento de cada parte paso a paso.

No inventes información que no pueda justificarse a partir del material de las clases; si necesitas complementar alguna explicación para hacerla comprensible, distínguela claramente del contenido directamente trabajado en el curso colocándolo entre paréntesis para poder distinguirlo.

Así, debes revisar detalladamente las instrucciones completas de este ejercicio en las siguientes rutas, y seguirlas:
"~\Desktop\Documentos Frank\2026-1\Diplomatura de Especialización en Ciencia de Datos\Curso de Capacitación en Python Intermedio para CCSS y Gestión Pública\Clases\Clase 8\Ejercicio\Skills Claude limpia la ENAHO.pdf"
"~\Desktop\Documentos Frank\2026-1\Diplomatura de Especialización en Ciencia de Datos\Curso de Capacitación en Python Intermedio para CCSS y Gestión Pública\Clases\Clase 8\Ejercicio\Tres skills para limpiar, graficar y mapear la ENAHO 2024.pdf"

También es muy importante que en cada paso en el que se señale que se debe hacer una revisión manual, o consideres que se debe hacer una revisión manual, me lo señales para que yo de una autorización o feedback para que continúe la ejecución de la tarea.

**Herramienta `Bash`**

```json
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

**Herramienta `Bash`**

```json
{
 "command": "cd \"~/Desktop/Documentos Frank/2026-1/Diplomatura de Especialización en Ciencia de Datos/Curso de Capacitación en Python Intermedio para CCSS y Gestión Pública\" && ls -R Clases | head -200; ls Chats",
 "description": "Listar contenido del curso intermedio"
}
```

<details><summary>Resultado</summary>

```text
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

</details>

<details><summary>Resultado</summary>

```text
Clases:
Clase 1
Clase 2
Clase 3
Clase 4
Clase 5
Clase 6
Clase 7
Clase 8

Clases/Clase 1:
(Audio) Clase 1 - Grabación.m4a
(Audio) Clase 1 - Grabación.txt
Clase 1 - Grabación.mp4
Intro_LLMs_Slides.pdf
llms_a_prueba.ipynb

Clases/Clase 2:
(Audio) Clase 2 - Grabación.m4a
(Audio) Clase 2 - Grabación.txt
Clase 2 - Grabación.mp4
lecture-modernbert.ipynb

Clases/Clase 3:
(Audio) Clase 3 - Grabación.m4a
(Audio) Clase 3 - Grabación.txt
Clase 3 - Grabación.mp4
PDF_OCR_and_Complaint_Extraction_with_Claude_AI_.pdf
paddleocr_documentos_peruanos.ipynb
tutorial_ocr_ia (1).pdf

Clases/Clase 4:
(Audio) Clase 4 - Grabación.m4a
(Audio) Clase 4 - Grabación.txt
Clase 4 - Grabación.mp4
audio_a_texto.pdf
tutorial_corto_audio_a_texto.ipynb

Clases/Clase 5:
(Audio) Clase 5 - Grabación.m4a
(Audio) Clase 5 - Grabación.txt
Clase 5 - Grabación.mp4
Ejercicio
raster_aplicado.ipynb

Clases/Clase 5/Ejercicio:
Incendios en el Perú tarea de hoy.pdf
Respuesta_Pregunta_E_Anio_Record.txt

Clases/Clase 6:
Ejercicio

Clases/Clase 6/Ejercicio:
Del texto a tu voz reels con modelos abiertos.pdf

Clases/Clase 7:
Ejercicio

Clases/Clase 7/Ejercicio:
MCP Claude conectado a tus datos.pdf
Tarea Sesión 07 - Su propio MCP del BCRP.pdf

Clases/Clase 8:
Ejercicio

Clases/Clase 8/Ejercicio:
Skills Claude limpia la ENAHO.pdf
Tres skills para limpiar, graficar y mapear la ENAHO 2024.pdf
Clase 1 - Python Intermedio para Ciencia de Datos.pdf
Clase 2 - Python Intermedio para Ciencia de Datos.pdf
Clase 3 - Python Intermedio para Ciencia de Datos.pdf
Clase 4 - Python Intermedio para Ciencia de Datos.pdf
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "cd \"~/Desktop/Documentos Frank/2026-1/Diplomatura de Especialización en Ciencia de Datos/Curso de Capacitación en Python Intermedio para CCSS y Gestión Pública/Clases/Clase 8/Ejercicio\" && uv run --with pypdf python -c \"\nimport pypdf,sys\nfor f in ['Skills Claude limpia la ENAHO.pdf','Tres skills para limpiar, graficar y mapear la ENAHO 2024.pdf']:\n    r=pypdf.PdfReader(f); print('=====',f,len(r.pages))\n    for i,p in enumerate(r.pages): print('--- p',i+1); print(p.extract_text())\n\" 2>&1",
 "description": "Extraer texto de los dos PDFs del ejercicio"
}
```

<details><summary>Resultado (error)</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    for i,p in enumerate(r.pages): print('--- p',i+1); print(p.extract_text())
                                                       ~~~~~^^^^^^^^^^^^^^^^^^
  File "~\AppData\Roaming\uv\python\cpython-3.14-windows-x86_64-none\Lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeEncodeError: 'charmap' codec can't encode characters in position 106-108: character maps to <undefined>
===== Skills Claude limpia la ENAHO.pdf 24
--- p 1
Ciencia de datos con Claude Code
Skills: ens��ale a Claude a limpiar  
la ENAHO
Una carpeta con instrucciones y un script que convierte los m�dulos del INEI en una  
base lista para analizar, siempre de la misma forma
30 min de clase � 45 min de proyecto � 15 min de presentaciones
--- p 2
La sesi�n
Noventa minutos, tres bloques
30
minutos de clase
Qu� es una skill, por qu� en  
Claude Code y el pipeline de  
la ENAHO
45
minutos de proyecto
Tres skills que limpian, grafican y mapean la  
ENAHO, validadas contra la pobreza oficial y  
probadas con y sin ellas
15
minutos de  
presentaciones
Cuatro repositorios al azar,  
tres minutos cada uno
--- p 3
El problema
P�dele dos veces que limpie la ENAHO y te dar� dos  
bases distintas
Otro filtro
Una vez deja a todos los  
miembros; otra, solo a los  
residentes habituales
Otro peso
Una vez pondera con el factor de  
expansi�n; otra, cuenta encuestas
Otra llave
Una vez lee el ubigeo como texto;  
otra, como n�mero, y pierde  
los ceros
Cada respuesta parece razonable. Juntas dan cifras de pobreza que no cuadran. Una skill fija las  
decisiones una vez.
--- p 4
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "cd \"~/Desktop/Documentos Frank/2026-1/Diplomatura de Especialización en Ciencia de Datos/Curso de Capacitación en Python Intermedio para CCSS y Gestión Pública/Clases/Clase 8/Ejercicio\" && PYTHONIOENCODING=utf-8 uv run --with pypdf python -c \"\nimport pypdf,sys\nfor f in ['Skills Claude limpia la ENAHO.pdf','Tres skills para limpiar, graficar y mapear la ENAHO 2024.pdf']:\n    r=pypdf.PdfReader(f); print('=====',f,len(r.pages))\n    for i,p in enumerate(r.pages): print('--- p',i+1); print(p.extract_text())\n\" 2>&1",
 "description": "Extraer texto de los PDFs con UTF-8"
}
```

<details><summary>Resultado</summary>

```text
<persisted-output>
Output too large (39.9KB). Full output saved to: ~\.claude\projects\C--Users-USER\50afee40-1161-4293-b4a9-85c2739871ed\tool-results\b08g20a8x.txt

Preview (first 2KB):
===== Skills Claude limpia la ENAHO.pdf 24
--- p 1
Ciencia de datos con Claude Code
Skills: enséñale a Claude a limpiar  
la ENAHO
Una carpeta con instrucciones y un script que convierte los módulos del INEI en una  
base lista para analizar, siempre de la misma forma
30 min de clase · 45 min de proyecto · 15 min de presentaciones
--- p 2
La sesión
Noventa minutos, tres bloques
30
minutos de clase
Qué es una skill, por qué en  
Claude Code y el pipeline de  
la ENAHO
45
minutos de proyecto
Tres skills que limpian, grafican y mapean la  
ENAHO, validadas contra la pobreza oficial y  
probadas con y sin ellas
15
minutos de  
presentaciones
Cuatro repositorios al azar,  
tres minutos cada uno
--- p 3
El problema
Pídele dos veces que limpie la ENAHO y te dará dos  
bases distintas
Otro filtro
Una vez deja a todos los  
miembros; otra, solo a los  
residentes habituales
Otro peso
Una vez pondera con el factor de  
expansión; otra, cuenta encuestas
Otra llave
Una vez lee el ubigeo como texto;  
otra, como número, y pierde  
los ceros
Cada respuesta parece razonable. Juntas dan cifras de pobreza que no cuadran. Una skill fija las  
decisiones una vez.
--- p 4
Qué es una skill
Una carpeta que Claude abre solo cuando la necesita
.claude/skills/limpiando-enaho/  
├── SKILL.md     qué hace y cuándo  
├── reference.md se lee si hace falta  
└── scripts/
    └── limpiar.py se ejecuta
Proyecto
.claude/skills/
Va en el repo: todo el equipo la usa
Personal
~/.claude/skills/
Solo tú, en todos tus proyectos
Plugin
/plugin:skill
Empaquetada para instalar
--- p 5
Anatomía de SKILL.md
Dos campos arriba, las instrucciones abajo
---  
name:  limpiando-enaho  
description:  Limpia módulos de la ENAHO del INEI y arma una  
base de personas. Úsala cuando pidan limpiar, unir o  
calcular pobreza con la ENAHO.  
---  
# Limpiar la ENAHO  
1. Corre scripts/limpiar.py  
2. Revisa validacion.txt  
...
</persisted-output>
```

</details>

**Herramienta `Read`**

```json
{
 "file_path": "~\\.claude\\projects\\C--Users-USER\\50afee40-1161-4293-b4a9-85c2739871ed\\tool-results\\b08g20a8x.txt"
}
```

<details><summary>Resultado</summary>

```text
1	===== Skills Claude limpia la ENAHO.pdf 24
2	--- p 1
3	Ciencia de datos con Claude Code
4	Skills: enséñale a Claude a limpiar  
5	la ENAHO
6	Una carpeta con instrucciones y un script que convierte los módulos del INEI en una  
7	base lista para analizar, siempre de la misma forma
8	30 min de clase · 45 min de proyecto · 15 min de presentaciones
9	--- p 2
10	La sesión
11	Noventa minutos, tres bloques
12	30
13	minutos de clase
14	Qué es una skill, por qué en  
15	Claude Code y el pipeline de  
16	la ENAHO
17	45
18	minutos de proyecto
19	Tres skills que limpian, grafican y mapean la  
20	ENAHO, validadas contra la pobreza oficial y  
21	probadas con y sin ellas
22	15
23	minutos de  
24	presentaciones
25	Cuatro repositorios al azar,  
26	tres minutos cada uno
27	--- p 3
28	El problema
29	Pídele dos veces que limpie la ENAHO y te dará dos  
30	bases distintas
31	Otro filtro
32	Una vez deja a todos los  
33	miembros; otra, solo a los  
34	residentes habituales
35	Otro peso
36	Una vez pondera con el factor de  
37	expansión; otra, cuenta encuestas
38	Otra llave
39	Una vez lee el ubigeo como texto;  
40	otra, como número, y pierde  
41	los ceros
42	Cada respuesta parece razonable. Juntas dan cifras de pobreza que no cuadran. Una skill fija las  
43	decisiones una vez.
44	--- p 4
45	Qué es una skill
46	Una carpeta que Claude abre solo cuando la necesita
47	.claude/skills/limpiando-enaho/  
48	├── SKILL.md     qué hace y cuándo  
49	├── reference.md se lee si hace falta  
50	└── scripts/
51	    └── limpiar.py se ejecuta
52	Proyecto
53	.claude/skills/
54	Va en el repo: todo el equipo la usa
55	Personal
56	~/.claude/skills/
57	Solo tú, en todos tus proyectos
58	Plugin
59	/plugin:skill
60	Empaquetada para instalar
61	--- p 5
62	Anatomía de SKILL.md
63	Dos campos arriba, las instrucciones abajo
64	---  
65	name:  limpiando-enaho  
66	description:  Limpia módulos de la ENAHO del INEI y arma una  
67	base de personas. Úsala cuando pidan limpiar, unir o  
68	calcular pobreza con la ENAHO.  
69	---  
70	# Limpiar la ENAHO  
71	1. Corre scripts/limpiar.py  
72	2. Revisa validacion.txt  
73	3. Para otras variables, lee reference.md
74	name
75	Minúsculas, números y guiones; hasta 64 caracteres.  
76	Será el comando /limpiando-enaho
77	description
78	Qué hace y cuándo usarla. Es lo único que Claude lee  
79	para decidir si la activa
80	El cuerpo
81	Pasos en Markdown; menos de 500 líneas
82	--- p 6
83	Carga progresiva
84	Claude lee la skill en tres niveles, no toda de golpe
85	1 · Siempre
86	name y description
87	Unos 100 tokens por skill, desde  
88	que abres Claude Code
89	2 · Al activarse
90	El cuerpo de SKILL.md
91	Menos de 5 mil tokens, solo cuando  
92	la tarea lo pide
93	3 · Si hace falta
94	Referencias y scripts
95	Nada hasta que se usan. Del script  
96	solo entra lo que imprime
97	Por eso pueden tener decenas de skills instaladas sin llenar el contexto.
98	Fuente: documentación de Agent Skills, platform.claude.com y code.claude.com
99	--- p 7
100	Cómo se usa
101	Claude la activa solo, o tú la llamas con /
102	Sola
103	¿Cuál fue la pobreza en Cusco en 2024?
104	El pedido coincide con la description y Claude carga la skill
105	A mano, con argumentos
106	/limpiando-enaho 2024
107	En el cuerpo, $ARGUMENTS o $0  se reemplaza por 2024
108	Campo Para qué
109	disable-model-invocation: true Solo tú la llamas; útil para lo que borra o publica
110	user-invocable: false Solo Claude la usa; no aparece en el menú /
111	allowed-tools Herramientas que no piden permiso mientras corre
112	--- p 8
113	La description
114	Decide si la skill se usa o se queda dormida
115	Vaga · no se activa
116	Ayuda con datos.
117	Puedo limpiar tu base.
118	Específica · se activa cuando debe
119	Limpia los módulos 34 y 02 de la ENAHO del INEI y arma una base  
120	de personas con pobreza y factor de expansión. Úsala cuando pidan  
121	limpiar, unir o analizar la ENAHO, o calcular pobreza por región.
122	En tercera persona.  «Limpia…»,  
123	no «Puedo…»
124	Qué y cuándo.  La 
[... salida recortada: 43,064 caracteres]
```

</details>

**Herramienta `Bash`**

```json
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

<details><summary>Resultado</summary>

```text
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

</details>

## Asistente · 2026-10-31 13:46

Ya leí los dos PDFs del ejercicio; ahora reviso qué materiales y herramientas hay disponibles en tu equipo.

**Herramienta `Bash`**

```json
{
 "command": "cd \"~/Documents/GitHub/Data-Science-Python\" && git log --oneline -3; git fetch -q 2>&1 | tail -2; git log --oneline HEAD..origin/main 2>&1 | head; ls sessions/*/ | head -80; grep -ril \"skill\" --include=*.md sessions | head; uv --version; git --version; which claude; find ~ -maxdepth 4 \\( -iname \"*966*\" -o -iname \"sumaria*\" -o -iname \"enaho01*\" \\) 2>/dev/null | head",
 "description": "Revisar repo del curso, herramientas y si existen datos ENAHO"
}
```

<details><summary>Resultado</summary>

```text
42960838 Sesión 16: skills de Claude Code para limpiar, graficar y mapear la ENAHO
d13359d8 Sesión 04: MCP en Claude Code, con el proyecto de un MCP del BCRP
bcec07e0 Sesión 15: notebook de la clase, del texto al reel con tu voz
sessions/01-datos-git-agentes/:
README.md
assets

sessions/02-fundamentos-python/:
README.md
lab.ipynb

sessions/03-scraping-apis/:
README.md
lab
lecture

sessions/04-mcp-claude-code/:
README.md
mcps_mas_usados.md
proyecto

sessions/05-visualizacion-dashboards/:
README.md
lab3
lab4
lecture

sessions/06-geoespacial/:
README.md
lab
lecture-folium
lecture-geopandas

sessions/07-raster/:
README.md
lab
lecture

sessions/08-llms-rag/:
README.md
assets
lab
lab9.ipynb
lecture

sessions/09-huggingface-finetuning/:
README.md
assets
lab-finetune
lab-hf
lecture-finetuning.ipynb
lecture-modernbert.ipynb
lecture-os-models.ipynb

sessions/10-document-ai-voz/:
README.md
lab
lab-vision-models.ipynb
lab-voz
lecture

sessions/11-agentes/:
README.md
lab
lecture-crewai.ipynb
lecture-openclaw

sessions/12-despliegue-evaluacion/:
README.md

sessions/13-audio-a-texto/:
README.md
app
datos.py
lecture
slides
voz.py

sessions/15-texto-a-reel/:
README.md
ejemplo
figuras
guion.py
sessions/04-mcp-claude-code/README.md
sessions/11-agentes/lab/DatosAbiertos/.cursor/skills/datosabiertos-dashboard/SKILL.md
sessions/11-agentes/lab/DatosAbiertos/handoff.md
sessions/11-agentes/lab/DatosAbiertos/README.md
sessions/11-agentes/lab/Skills_Claude/README.md
sessions/11-agentes/lecture-openclaw/LECTURE_PLAN_OpenClaw.md
sessions/16-skills-enaho/README.md
uv 0.12.23 (46b84fd0b 2026-10-03 x86_64-pc-windows-msvc)
git version 2.55.0.windows.5
~/.local/bin/claude
~/.copilot/logs/process-1793147809663-2592.log
~/AppData/Local/Temp/lastChanceDst17931293230516421991966539552357.jar
~/AppData/Local/Temp/pip-unpack-_20q_966
~/Downloads/Funny internet images/287909728_340340101434375_4704053966395062095_n.jpg
~/Downloads/Funny internet images/307112125_172319662009741_3041956966974873538_n.jpg
~/Downloads/Funny internet images/314359049_5696681793710787_1758718173242044632_n.jpg
~/Downloads/Funny internet images/315410237_5167477636688967_8796659677764438474_n.jpg
~/Downloads/Funny internet images/316107391_644262677174451_5056699665520315187_n.jpg
~/Downloads/Funny internet images/324886966_650644160148638_8431997652236433162_n.jpg
~/Downloads/Funny internet images/352306166_815030996636318_5198661263908123002_n.jpg
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "cd \"~/Documents/GitHub/Data-Science-Python/sessions/16-skills-enaho\" && ls -laR | head -60; cat README.md",
 "description": "Leer la sesión 16 del repo del curso"
}
```

<details><summary>Resultado</summary>

```text
.:
total 16
drwxr-xr-x 1 USER 197121     0 Oct 31 08:13 .
drwxr-xr-x 1 USER 197121     0 Oct 31 08:13 ..
-rw-r--r-- 1 USER 197121 11814 Oct 31 08:13 README.md
drwxr-xr-x 1 USER 197121     0 Oct 31 08:13 referencias

./referencias:
total 153
drwxr-xr-x 1 USER 197121      0 Oct 31 08:13 .
drwxr-xr-x 1 USER 197121      0 Oct 31 08:13 ..
-rw-r--r-- 1 USER 197121 154081 Oct 31 08:13 mapa_pobreza_2024.png
-rw-r--r-- 1 USER 197121    459 Oct 31 08:13 pobreza_departamento_2024.csv
# Sesión 16 · Skills de Claude Code: limpiar, graficar y mapear la ENAHO

Qué es una skill de Claude Code, por qué conviene crearla dentro del repositorio y cómo se arma una que limpie la ENAHO
siempre de la misma forma. El proyecto son tres skills que trabajan juntas: una limpia los módulos del INEI, otra
hace gráficos y otra hace un mapa por departamento.

**Slides de la clase:** https://claude.ai/artifact/X7H6PUvaWKde1epsYCJNze

| Bloque | Duración | Qué se hace |
|---|---|---|
| Clase | 30 min | Qué es una skill, cómo se carga y se activa, por qué en Claude Code, el pipeline de la ENAHO y sus trampas |
| Proyecto | 45 min | Tres skills: `limpiando-enaho`, `graficando-enaho` y `mapeando-enaho`, validadas y probadas con y sin ellas |
| Presentaciones | 15 min | Cuatro repositorios al azar, tres minutos cada uno |

## Contenido

| Archivo | Qué hay |
|---|---|
| [`referencias/pobreza_departamento_2024.csv`](referencias/pobreza_departamento_2024.csv) | La pobreza 2024 de los 25 departamentos, para validar el mapa |
| [`referencias/mapa_pobreza_2024.png`](referencias/mapa_pobreza_2024.png) | Cómo debe verse el mapa |

## Lo esencial de una skill

- **Es una carpeta** con un `SKILL.md` obligatorio y, si hace falta, archivos de referencia y scripts. En un proyecto
  va en `.claude/skills/<nombre>/`. Así viaja con git y todo el equipo usa la misma.
- **`SKILL.md`** empieza con un bloque YAML con `name` (minúsculas, números y guiones; hasta 64 caracteres) y
  `description`. Debajo van las instrucciones, en menos de 500 líneas.
- **Carga progresiva.** Al inicio Claude solo ve `name` y `description` de cada skill, unos 100 tokens. El cuerpo se
  carga cuando la tarea lo pide, y los demás archivos solo si se usan. De un script solo entra al contexto lo que
  imprime.
- **Se activa sola** cuando un pedido coincide con la `description`, o a mano con `/nombre argumentos`. Dentro del
  archivo, `$ARGUMENTS` o `$0` toman los argumentos, y `${CLAUDE_SKILL_DIR}` es la carpeta de la skill.
- **La `description`** se escribe en tercera persona y dice qué hace y cuándo usarla, con las palabras que usaría
  quien la pide: ENAHO, INEI, pobreza, mapa.
- **Script o instrucción.** Lo que no se discute (llaves, filtros, uniones, validación) va en un script que la skill
  corre tal cual. Lo que requiere criterio va en el texto.

### Por qué crearla en Claude Code

1. Se versiona con git y los cambios se revisan en un pull request.
2. Corre en su máquina, con su entorno de `uv`, sus archivos e internet. En la API de Claude las skills corren en un
   contenedor sin red y sin poder instalar paquetes.
3. El script hace que el resultado sea el mismo cada vez y para cualquiera.
4. Se puede evaluar con `claude -p`, con y sin skills.
5. Se combina con MCP, hooks y subagentes en el mismo proyecto.
6. Sigue el estándar abierto Agent Skills: la misma carpeta se puede subir a claude.ai como zip.

## Los datos

| Archivo | Una fila por | Filas | Llaves | Factor |
|---|---|---|---|---|
| [Módulo 34, sumaria](https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo34.zip) (16 MB) | hogar | 33,691 | `conglome`, `vivienda`, `hogar` | `factor07` |
| [Módulo 02, miembros](https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo02.zip) (6 MB) | persona | 117,721 | las tres + `codperso` | `facpob07` |
| [Límites departamentales](https://raw.githubusercontent.com/d2cml-ai/Data-Science-Python/main/sessions/06-geoespacial/lab/D
[... salida recortada: 12,183 caracteres]
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "cat referencias/pobreza_departamento_2024.csv; ls \"~/Desktop/Documentos Frank/2026-1/Diplomatura de Especialización en Ciencia de Datos/Curso de Capacitación en Python Intermedio para CCSS y Gestión Pública/Chats\"; ls ../11-agentes/lab/Skills_Claude/; ls ~/Documents/GitHub/enaho-skills 2>&1",
 "description": "Ver CSV de referencia, chats y skills de la sesión 11"
}
```

<details><summary>Resultado (error)</summary>

```text
Exit code 2
ccdd,departamento,pobreza_pct
01,AMAZONAS,25.7
02,ANCASH,22.8
03,APURIMAC,24.0
04,AREQUIPA,15.8
05,AYACUCHO,32.8
06,CAJAMARCA,45.0
07,CALLAO,33.9
08,CUSCO,18.5
09,HUANCAVELICA,33.4
10,HUANUCO,39.0
11,ICA,6.0
12,JUNIN,18.5
13,LA LIBERTAD,30.2
14,LAMBAYEQUE,14.0
15,LIMA,27.1
16,LORETO,43.0
17,MADRE DE DIOS,11.1
18,MOQUEGUA,11.0
19,PASCO,39.0
20,PIURA,31.9
21,PUNO,39.9
22,SAN MARTIN,22.0
23,TACNA,24.0
24,TUMBES,26.9
25,UCAYALI,27.1
Clase 1 - Python Intermedio para Ciencia de Datos.pdf
Clase 2 - Python Intermedio para Ciencia de Datos.pdf
Clase 3 - Python Intermedio para Ciencia de Datos.pdf
Clase 4 - Python Intermedio para Ciencia de Datos.pdf
README.md
dashboard.py
fetch_bcrp.py
mcp_bcrp_server.py
setup.ps1
start_mcp_bcrp.cmd
ls: cannot access '~/Documents/GitHub/enaho-skills': No such file or directory
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "cd ~/Documents/GitHub && mkdir enaho-skills && cd enaho-skills && git init -b main && uv init 2>&1 && uv add pandas pyarrow geopandas matplotlib 2>&1 | tail -15 && mkdir -p datos salidas figuras mapas .claude/skills && ls -la && cat pyproject.toml",
 "description": "Crear repositorio, entorno uv y carpetas del proyecto",
 "timeout": 300000
}
```

<details><summary>Resultado</summary>

```text
Initialized empty Git repository in ~/Documents/GitHub/enaho-skills/.git/
Initialized project `enaho-skills`
 + geopandas==1.2.0
 + kiwisolver==1.5.1
 + matplotlib==3.11.2
 + numpy==2.5.4
 + packaging==26.3
 + pandas==3.1.0
 + pillow==13.0.0
 + pyarrow==26.0.0
 + pyogrio==0.13.0
 + pyparsing==3.3.3
 + pyproj==3.8.0
 + python-dateutil==3.0.0
 + shapely==2.2.0
 + six==1.17.0
 + tzdata==2026.6
total 158
drwxr-xr-x 1 USER 197121      0 Oct 31 08:47 .
drwxr-xr-x 1 USER 197121      0 Oct 31 08:47 ..
drwxr-xr-x 1 USER 197121      0 Oct 31 08:47 .claude
drwxr-xr-x 1 USER 197121      0 Oct 31 08:47 .git
-rw-r--r-- 1 USER 197121      5 Oct 31 08:47 .python-version
drwxr-xr-x 1 USER 197121      0 Oct 31 08:47 .venv
-rw-r--r-- 1 USER 197121      0 Oct 31 08:47 README.md
drwxr-xr-x 1 USER 197121      0 Oct 31 08:47 datos
drwxr-xr-x 1 USER 197121      0 Oct 31 08:47 figuras
drwxr-xr-x 1 USER 197121      0 Oct 31 08:47 mapas
-rw-r--r-- 1 USER 197121    492 Oct 31 08:47 pyproject.toml
drwxr-xr-x 1 USER 197121      0 Oct 31 08:47 salidas
drwxr-xr-x 1 USER 197121      0 Oct 31 08:47 src
-rw-r--r-- 1 USER 197121 140853 Oct 31 08:47 uv.lock
[project]
name = "enaho-skills"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
authors = [
    { name = "Frank Pinares", email = "[correo oculto]" }
]
requires-python = ">=3.14"
dependencies = [
    "geopandas>=1.2.0",
    "matplotlib>=3.11.2",
    "pandas>=3.1.0",
    "pyarrow>=26.0.0",
]

[project.scripts]
enaho-skills = "enaho_skills:main"

[build-system]
requires = ["uv_build>=0.12.23,<0.13.0"]
build-backend = "uv_build"
```

</details>

## Asistente · 2026-10-31 13:47

`uv init` generó un proyecto empaquetado (carpeta `src/` y `[build-system]`) que la tarea no necesita; lo simplifico a un proyecto plano y agrego el `.gitignore`.

**Herramienta `Bash`**

```json
{
 "command": "ls -R src && rm -rf src && python - <<'EOF' 2>/dev/null || ~/anaconda3/python.exe - <<'EOF'\nimport re,pathlib\np=pathlib.Path(\"pyproject.toml\"); t=p.read_text(encoding=\"utf-8\")\nt=t.replace('description = \"Add your description here\"','description = \"Tres skills de Claude Code para limpiar, graficar y mapear la ENAHO 2024\"')\nt=re.sub(r'\\n\\[project.scripts\\].*', '\\n', t, flags=re.S)\np.write_text(t.rstrip()+\"\\n\",encoding=\"utf-8\")\nEOF\ncat > .gitignore <<'EOF'\n# Entorno\n.venv/\n__pycache__/\n\n# Microdatos del INEI: pesan bastante y se descargan del portal\ndatos/*.zip\ndatos/**/*.dta\ndatos/**/*.pdf\nEOF\ncat pyproject.toml; uv sync 2>&1 | tail -3",
 "description": "Quitar paquete src, limpiar pyproject y crear .gitignore"
}
```

<details><summary>Resultado</summary>

```text
src:
enaho_skills

src/enaho_skills:
__init__.py
  File "<stdin>", line 1
    cat > .gitignore <<'EOF'
          ^
SyntaxError: invalid syntax
[project]
name = "enaho-skills"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
authors = [
    { name = "Frank Pinares", email = "[correo oculto]" }
]
requires-python = ">=3.14"
dependencies = [
    "geopandas>=1.2.0",
    "matplotlib>=3.11.2",
    "pandas>=3.1.0",
    "pyarrow>=26.0.0",
]

[project.scripts]
enaho-skills = "enaho_skills:main"

[build-system]
requires = ["uv_build>=0.12.23,<0.13.0"]
build-backend = "uv_build"
   Building enaho-skills @ file:///~/Documents/GitHub/enaho-skills
error: Failed to build `enaho-skills @ file:///~/Documents/GitHub/enaho-skills`
  cause: Expected a Python module at: src\enaho_skills\__init__.py
```

</details>

## Asistente · 2026-10-31 13:47

My heredoc chain was malformed; I'll write the files directly instead.

**Herramienta `Write`**

```json
{
 "file_path": "~\\Documents\\GitHub\\enaho-skills\\pyproject.toml",
 "content": "[project]\nname = \"enaho-skills\"\nversion = \"0.1.0\"\ndescription = \"Tres skills de Claude Code para limpiar, graficar y mapear la ENAHO 2024\"\nreadme = \"README.md\"\nauthors = [\n    { name = \"Frank Pinares\", email = \"[correo oculto]\" }\n]\nrequires-python = \">=3.14\"\ndependencies = [\n    \"geopandas>=1.2.0\",\n    \"matplotlib>=3.11.2\",\n    \"pandas>=3.1.0\",\n    \"pyarrow>=26.0.0\",\n]\n"
}
```

**Herramienta `Write`**

```json
{
 "file_path": "~\\Documents\\GitHub\\enaho-skills\\.gitignore",
 "content": "# Entorno\n.venv/\n__pycache__/\n\n# Microdatos del INEI: pesan bastante y se descargan del portal\ndatos/*.zip\ndatos/**/*.dta\ndatos/**/*.pdf\n"
}
```

**Herramienta `Bash`**

```json
{
 "command": "uv sync 2>&1 | tail -3 && cd datos && curl -sSLO https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo34.zip ; curl -sSLO https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo02.zip ; cp ~/Documents/GitHub/Data-Science-Python/sessions/06-geoespacial/lab/Data/peru_departamental_simple.geojson . ; ls -la; file *.zip",
 "description": "Sincronizar entorno y descargar módulos ENAHO y GeoJSON",
 "timeout": 300000
}
```

<details><summary>Resultado</summary>

```text
The file ~\Documents\GitHub\enaho-skills\pyproject.toml has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>Resultado</summary>

```text
File created successfully at: ~\Documents\GitHub\enaho-skills\.gitignore (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>Resultado</summary>

```text
Resolved 20 packages in 23ms
Uninstalled 1 package in 3ms
 - enaho-skills==0.1.0 (from file:///~/Documents/GitHub/enaho-skills)
total 21372
drwxr-xr-x 1 USER 197121        0 Oct 31 08:48 .
drwxr-xr-x 1 USER 197121        0 Oct 31 08:47 ..
-rw-r--r-- 1 USER 197121  5793097 Oct 31 08:48 966-Modulo02.zip
-rw-r--r-- 1 USER 197121 15935617 Oct 31 08:48 966-Modulo34.zip
-rw-r--r-- 1 USER 197121   139705 Oct 31 08:48 peru_departamental_simple.geojson
966-Modulo02.zip: Zip archive data, made by v3.1, extract using at least v1.0, last modified May 07 2025 14:43:16, uncompressed size 0, method=store
966-Modulo34.zip: Zip archive data, at least v1.0 to extract, compression method=store
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "curl -sSL -o geo_remoto.geojson https://raw.githubusercontent.com/d2cml-ai/Data-Science-Python/main/sessions/06-geoespacial/lab/Data/peru_departamental_simple.geojson && cmp geo_remoto.geojson peru_departamental_simple.geojson && echo IGUALES && rm geo_remoto.geojson; (unzip -oq 966-Modulo34.zip && unzip -oq 966-Modulo02.zip) 2>&1 || ../.venv/Scripts/python.exe -c \"import zipfile;[zipfile.ZipFile(z).extractall('.') for z in ['966-Modulo34.zip','966-Modulo02.zip']]\"; find . -type f | sort",
 "description": "Verificar GeoJSON contra la URL oficial y descomprimir zips"
}
```

<details><summary>Resultado</summary>

```text
geo_remoto.geojson peru_departamental_simple.geojson differ: char 5365, line 1
./966-Modulo02.zip
./966-Modulo02/CED-01-200-2024.pdf
./966-Modulo02/Criterios para codificar Ocupaciones Peligrosas.pdf
./966-Modulo02/Diccionario2024.pdf
./966-Modulo02/FichaTecnica.pdf
./966-Modulo02/enaho01-2024-200.dta
./966-Modulo02/enaho_tabla_ciuo_88.dta
./966-Modulo02/enaho_tabla_cno_2015.dta
./966-Modulo34.zip
./966-Modulo34/ConstVarGasto-Metodologia actualizada.zip
./966-Modulo34/DefinicionValoresMonetariosBasedeDatos.pdf
./966-Modulo34/Diccionario2024.pdf
./966-Modulo34/Estratificacion del Marco.pdf
./966-Modulo34/FichaTecnica.pdf
./966-Modulo34/Sumaria-2024-12g.pdf
./966-Modulo34/Sumaria-2024.pdf
./966-Modulo34/sumaria-2024-12g.dta
./966-Modulo34/sumaria-2024.dta
./geo_remoto.geojson
./peru_departamental_simple.geojson
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "mv -f geo_remoto.geojson peru_departamental_simple.geojson && cd .. && uv run python -c \"\nimport pandas as pd, geopandas as gpd\ns=pd.read_stata('datos/966-Modulo34/sumaria-2024.dta',convert_categoricals=False)\nm=pd.read_stata('datos/966-Modulo02/enaho01-2024-200.dta',convert_categoricals=False)\nprint('sumaria',s.shape); print('miembros',m.shape)\nprint([c for c in s.columns if c.lower() in ('conglome','vivienda','hogar','ubigeo','pobreza','mieperho','factor07','estrato','dominio') or 'o' == c[-1:] and c.lower().startswith('a')][:12])\nprint([c for c in m.columns if c.lower() in ('conglome','vivienda','hogar','codperso','p203','p204','p205','p206','p207','p208a','facpob07')])\nprint(s[['conglome','vivienda','hogar','ubigeo']].dtypes.to_dict()); print(s[['conglome','ubigeo']].head(3))\ng=gpd.read_file('datos/peru_departamental_simple.geojson'); print(len(g), list(g.columns)); print(g[['FIRST_IDDP']].head(3), g.FIRST_IDDP.dtype)\n\"",
 "description": "Verificar filas, llaves y variables de los módulos",
 "timeout": 180000
}
```

<details><summary>Resultado</summary>

```text
sumaria (33691, 163)
miembros (117721, 40)
['a�o', 'conglome', 'vivienda', 'hogar', 'ubigeo', 'dominio', 'estrato', 'mieperho', 'pobreza', 'factor07']
['conglome', 'vivienda', 'hogar', 'codperso', 'p203', 'p204', 'p205', 'p206', 'p207', 'p208a', 'facpob07']
{'conglome': <StringDtype(na_value=nan)>, 'vivienda': <StringDtype(na_value=nan)>, 'hogar': <StringDtype(na_value=nan)>, 'ubigeo': <StringDtype(na_value=nan)>}
  conglome  ubigeo
0   015009  010101
1   015009  010101
2   015009  010101
25 ['NOMBDEP', 'COUNT', 'FIRST_IDDP', 'HECTARES', 'geometry']
  FIRST_IDDP
0         01
1         02
2         03 str
```

</details>

## Asistente · 2026-10-31 13:48

Antes de detenerme, guardo el estado de la tarea en memoria para poder retomarla.

**Herramienta `Write`**

```json
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

<details><summary>Resultado</summary>

```text
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

</details>

**Herramienta `Bash`**

```json
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

<details><summary>Resultado</summary>

```text
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

</details>

## Asistente · 2026-10-31 13:49

## 🔶 Revisión manual 1: fin del Paso 1 (Preparar). Necesito tu autorización para seguir.

Leí las instrucciones de los dos PDFs de la Clase 8. También encontré en tu clon de `Data-Science-Python` la carpeta `sessions/16-skills-enaho`, que tiene el mismo enunciado y un archivo de referencia, `pobreza_departamento_2024.csv`, con los 25 departamentos. Con ese archivo podré validar el mapa en el Paso 3.

### Qué se hizo en el Paso 1

| Sub-paso del PDF | Qué se hizo | Resultado |
|---|---|---|
| **1.1** Repo y entorno | Se creó `~\Documents\GitHub\enaho-skills` con `git init -b main`, `uv init` y `uv add pandas pyarrow geopandas matplotlib`, más las carpetas `datos/ salidas/ figuras/ mapas/ .claude/skills/` | ✅ `pyproject.toml` con las 4 librerías |
| **1.2** Descarga | `curl` bajó los dos zip del INEI (966 = ENAHO 2024) sin problemas de certificado, y se descomprimieron | ✅ Están los dos `.dta` y el `.geojson` en `datos/` |
| **1.3** Verificación | Se leyeron los módulos con `read_stata(convert_categoricals=False)` | ✅ Coincide con la tabla del PDF (ver abajo) |
| **1.4** `.gitignore` | Se agregaron `datos/*.zip`, `datos/**/*.dta` y `datos/**/*.pdf`, más `.venv/` | ✅ |

**Lo que mostró la verificación (1.3):**
- La sumaria tiene **33,691** hogares y los miembros **117,721** filas, igual que en la tabla de la clase.
- Están todas las variables que se usarán: `pobreza`, `mieperho`, `factor07`, `ubigeo`, `estrato`, `dominio` en la sumaria, y `codperso`, `p203`–`p208a`, `facpob07` en miembros.
- La columna del año aparece como `aÑo`. Es la trampa de los «nombres rotos» que el script tendrá que normalizar a `anio`.
- En esta versión de pandas, `conglome` y `ubigeo` ya llegan como texto con el cero inicial (`"015009"`, `"010101"`). Aun así, el script mantendrá el relleno con `zfill`, como manda el pipeline. (Es la regla del «puente angosto»: una decisión que no se discute va fija en el script y no depende de la versión de la librería.)
- El GeoJSON tiene 25 departamentos y `FIRST_IDDP` como texto con dos dígitos (`"01"`). Eso permitirá unir por código.

### Decisiones que tomé y que debes validar

1. **Ubicación y nombre:** `Documents\GitHub\enaho-skills`, junto a `mcp-bcrp` y tus otras tareas.
2. **`uv init` creó un proyecto empaquetado** (carpeta `src/` y `[build-system]`). Lo dejé como proyecto plano, porque la tarea solo usa scripts dentro de las skills.
3. **GeoJSON:** el de tu clon local **es distinto** del que está en la URL del curso. Usé el de la URL, que es la ruta que indica el PDF.
4. **Python 3.14**, la versión que eligió `uv`. Todas las librerías se instalaron sin problemas.

### Lo que viene (Paso 2 · Limpiar)

Escribiré `.claude/skills/limpiando-enaho/scripts/limpiar.py` sobre el esqueleto del PDF (págs. 6-8), con los 7 pasos en orden. Después escribiré su `SKILL.md`, con la línea «Si no se indica año, usa 2024» que recomienda la pág. 9, y un `reference.md` con los códigos. Luego correré el script. La siguiente revisión manual será sobre `validacion.txt`, que debe mostrar 27.6%, 5.5% y 108,664.

**Aviso anticipado** de dos puntos que también requerirán tu autorización:
- **Paso 4:** las 6 corridas con `claude -p` consumen uso de tu cuenta. Es posible que tengas que lanzarlas tú con `!`, como pasó con `claude mcp add` en la tarea del BCRP.
- **Entrega:** crear el repositorio en GitHub (`saffron29/enaho-skills`) y hacer el push.

**¿Apruebas el Paso 1 y continúo con el Paso 2?** Si quieres cambiar algo (el nombre del repo, trabajar en pareja o el registro de los comentarios del código), dímelo ahora. Por defecto, los comentarios del código irán en frases breves e impersonales, como en tu tarea del BCRP.

## Usuario · 2026-10-31 13:52

Sí, apruebo el Paso 1, continúa con el Paso 2.

## Asistente · 2026-10-31 13:52

Empiezo el Paso 2. Primero reviso en el diccionario del INEI los códigos de `dominio`, `estrato` y las preguntas p204–p206, para que `reference.md` y el filtro se apoyen en la fuente y no en suposiciones.

**Herramienta `Bash`**

```json
{
 "command": "cd ~/Documents/GitHub/enaho-skills && PYTHONIOENCODING=utf-8 uv run --with pypdf python -c \"\nimport pypdf,re\nfor f in ['datos/966-Modulo34/Diccionario2024.pdf','datos/966-Modulo02/Diccionario2024.pdf']:\n    t='\\n'.join(p.extract_text() for p in pypdf.PdfReader(f).pages)\n    print('=====',f,len(t))\n    for v in ['DOMINIO','ESTRATO','POBREZA','MIEPERHO','FACTOR07','P204','P205','P206','P207','P208A','FACPOB07','P203']:\n        for m in re.finditer(r'\\n'+v+r'\\b',t):\n            print('##',v); print(t[m.start():m.start()+700]); break\n\"",
 "description": "Extraer códigos de variables de los diccionarios INEI",
 "timeout": 180000
}
```

<details><summary>Resultado</summary>

```text
===== datos/966-Modulo34/Diccionario2024.pdf 813556
## DOMINIO

DOMINIO 1 0 N Dominio Geográfico
1.Costa Norte
2.Costa Centro
3.Costa Sur
4.Sierra Norte
5.Sierra Centro
6.Sierra Sur
7.Selva
8.Lima Metropolitana
Rango : 1 – 8
ESTRATO 1 0 N Estrato Geográfico
1. De 500 000 a más habitantes
2. De 100 000 a 499 999 habitantes
3. De 50 000 a 99 999 habitantes
4. De 20 000 a 49 999 habitantes
5.De 2 000 a 19 999 habitantes
6. De 500 a 1 999 habitantes
7. Área de Empadronamiento Rural (AER) Compuesto
8. Área de Empadronamiento Rural (AER) Simple
Rango : 1 – 8
PERIODO 1 0 N Periodo de ejecución de la Encuesta
1.Primer Período
2.Segundo Período
3.Tercer Período
4.Cuarto Período
5.Quinto Período
Rango : 1- 5
TIPENC 1 0 N Tipo de Selección del Conglomerado
1.Selec
## ESTRATO

ESTRATO 1 0 N Estrato Geográfico
1. De 500 000 a más habitantes
2. De 100 000 a 499 999 habitantes
3. De 50 000 a 99 999 habitantes
4. De 20 000 a 49 999 habitantes
5.De 2 000 a 19 999 habitantes
6. De 500 a 1 999 habitantes
7. Área de Empadronamiento Rural (AER) Compuesto
8. Área de Empadronamiento Rural (AER) Simple
Rango : 1 – 8
PERIODO 1 0 N Periodo de ejecución de la Encuesta
1.Primer Período
2.Segundo Período
3.Tercer Período
4.Cuarto Período
5.Quinto Período
Rango : 1- 5
TIPENC 1 0 N Tipo de Selección del Conglomerado
1.Selección Automática por Computadora - Área Urbana
3.Selección por Muestra Panel
3. ARCHIVOS DEL CUESTIONARIO ENAHO.01.
3.1. ENAHO01-2024-100: Características de la V
## POBREZA

POBREZA 1 0 N Pobreza
1.Pobre Extremo
2.Pobre No Extremo
3.No Pobre
Rango : 1 – 3
LINEAV 9 2 N Linea corriente de vulnerabilidad
POBREZAV 19 0 N Pobreza y vulnerabilidad
1.Pobre Extremo
2.Pobre No Extremo
3.Vulnerable No pobre
4.No Vulnerable
Rango : 1 – 4
TICUEST01B 1 0 Origen de cuestionario
1.  Cuestionario en hojas
2.  Cuestionario en Tablet
Rango 1-2
FACTOR07 7 2 N Factor de Expansión Anual Proyecciones CPV-2007
Diccionario de Datos
485
Encuesta Nacional de Hogares INEI
9. SUMARIA POR 12 GRUPOS DE GASTOS
Variable Tamaño Decimal Formato Etiqueta
AÑO 4 0 C Año de la Encuesta
MES 2 0 C Mes de Ejecución de la Encuesta
NCONGLOME 6 0 C Número de Conglomerado (proveniente del marco)
SUB_CONGL
## MIEPERHO

MIEPERHO 2 0 N Total de miembros del hogar
TOTMIEHO 2 0 N Total de personas en el hogar
PERCEPHO 2 0 N Total de perceptores de Ingresos
IA01HD 9 0 N Ingreso alquiler imputado de la vivienda
PERCEPHO 2 0 N Total de perceptores de Ingresos
IA01HD 9 2 N Ingreso alquiler imputado de la vivienda
8.1. SUMARIA-2024.SAV- Sumaria Por 8 Grupo De Gastos
Archivo: Sumaria-2024-8g
Diccionario de Datos
480
Encuesta Nacional de Hogares INEI
Variable Tamaño Decimal Formato Etiqueta
Archivo: Sumaria-2024-8g
IA02HD 5 0 N Ingreso por transferencia de alquiler
IG03HD1 6 0 N Credito, compra casa, departamento
IG03HD2 6 0 N Credito, comprar terreno para vivienda
IG03HD3 6 0 N Credito mejoramiento y/o ampliacion d
## FACTOR07

FACTOR07 7 2 N Factor de expansión anual. Proyecciones CPV-2007
CODCCPP 4 0 C Codigo del Centro poblado
NOMCCPP 80 0 C Nombre del centro poblado
LONGITUD 8 2 N Longitud
LATITUD 8 2 N Latitud
Diccionario de Datos
30
Encuesta Nacional de Hogares INEI
ARCHIVO DEL CUESTIONARIO  ENAHO.01.
3.2.ENAHO01-2024-200: Características de la Vivienda y del Hogar( Módulo 200)
Archivo: ENAHO01-2024-200
Variable Tamaño Decimal Formato Etiqueta
AÑO 4 0 C Año de la encuesta
MES 2 0 C Mes de ejecución de la encuesta
NCONGLOME 6 0 C Número de Conglomerado (proveniente del marco)
SUB_CONGLOME 2 0 C Número de Subconglomerado (proveniente del marco)
CONGLOME 6 0 C Número de conglomerado
VIVIENDA 3 0 C Número de sel
## P204

P204 1 0 N ¿Es miembro del hogar?
1.Si
2.No
Rango : 1 – 2
P205 1 0 N ¿Se encuentra ausente del hogar 30 días o más?
1.Si
2.No
Rango : 1 – 2
P206 1 0 N ¿Está presente en el hogar 30 días o más?
1.Si
2.No
Rango : 1 – 2
P207 1 0 N Sexo
1.Homb
[... salida recortada: 17,842 caracteres]
```

</details>

**Herramienta `Write`**

```json
{
 "file_path": "~\\Documents\\GitHub\\enaho-skills\\.claude\\skills\\limpiando-enaho\\scripts\\limpiar.py",
 "content": "\"\"\"Limpia los módulos 34 y 02 de la ENAHO y arma una base de personas.\n\nSe corre desde la raíz del repositorio:\n    uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024\n\"\"\"\nimport argparse\nfrom pathlib import Path\n\nimport pandas as pd\n\nLLAVES = [\"conglome\", \"vivienda\", \"hogar\"]\nLLAVES_PERSONA = LLAVES + [\"codperso\"]\nANCHOS = {\"conglome\": 6, \"vivienda\": 3, \"hogar\": 2, \"codperso\": 2, \"ubigeo\": 6}\nPOBREZA_INEI = {2024: 27.6}  # % de personas, cifra oficial\nEXTREMA_INEI = {2024: 5.5}  # % de personas en pobreza extrema\nRESIDENTES = {2024: 108_664}  # residentes habituales esperados en la clase\n\n\ndef buscar(patron: str) -> Path:\n    \"\"\"Se ubica el .dta dentro de datos/, aunque el zip lo deje en una subcarpeta.\"\"\"\n    rutas = sorted(Path(\"datos\").rglob(patron))\n    if not rutas:\n        raise SystemExit(f\"Falta {patron} en datos/. Descárgalo del portal del INEI.\")\n    return rutas[0]\n\n\ndef leer(ruta: Path) -> pd.DataFrame:\n    df = pd.read_stata(ruta, convert_categoricals=False)            # 1. Leer\n    df.columns = [c.lower().replace(\"ñ\", \"ni\") for c in df.columns]  # 2. aÑo -> anio\n    for col, ancho in ANCHOS.items():                                # llaves como texto\n        if col in df.columns:\n            df[col] = (df[col].astype(str).str.strip()\n                       .str.replace(r\"\\.0$\", \"\", regex=True).str.zfill(ancho))\n    return df\n\n\ndef tasa(pobre: pd.Series, peso: pd.Series) -> float:\n    \"\"\"Se pondera cada caso por su factor; nunca se cuentan encuestas.\"\"\"\n    return 100 * (pobre * peso).sum() / peso.sum()\n\n\ndef main() -> None:\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\"--anio\", type=int, default=2024)\n    anio = parser.parse_args().anio\n\n    sumaria = leer(buscar(f\"sumaria-{anio}.dta\"))\n    miembros = leer(buscar(f\"enaho01-{anio}-200.dta\"))\n\n    # 3. Filtrar residentes habituales: miembros no ausentes 30 días o más\n    # y no miembros presentes 30 días o más\n    residente = (((miembros.p204 == 1) & (miembros.p205 == 2))\n                 | ((miembros.p204 == 2) & (miembros.p206 == 1)))\n    personas = miembros.loc[residente, LLAVES_PERSONA\n                            + [\"p203\", \"p207\", \"p208a\", \"facpob07\"]].copy()\n\n    # 4. Unir (las variables de hogar vienen solo de la sumaria)\n    cols_hogar = LLAVES + [\"pobreza\", \"mieperho\", \"factor07\",\n                           \"ubigeo\", \"estrato\", \"dominio\"]\n    base = personas.merge(sumaria[cols_hogar], on=LLAVES, how=\"left\",\n                          validate=\"m:1\", indicator=True)\n\n    # 5. Construir\n    base[\"departamento\"] = base.ubigeo.str[:2]\n    base[\"urbano\"] = base.estrato <= 5\n    base[\"pobre\"] = base.pobreza <= 2\n    base[\"pobre_extremo\"] = base.pobreza == 1\n\n    # 6. Validar\n    assert not personas.duplicated(LLAVES_PERSONA).any(), \"personas duplicadas\"\n    assert not sumaria.duplicated(LLAVES).any(), \"hogares duplicados\"\n    assert len(base) == len(personas), \"la unión perdió o duplicó filas\"\n    assert (base._merge == \"both\").all(), \"personas sin hogar en la sumaria\"\n    base = base.drop(columns=\"_merge\")\n\n    peso_hogar = sumaria.factor07 * sumaria.mieperho\n    pob_sumaria = tasa(sumaria.pobreza <= 2, peso_hogar)\n    ext_sumaria = tasa(sumaria.pobreza == 1, peso_hogar)\n    pob_personas = tasa(base.pobre, base.facpob07)\n\n    oficial = POBREZA_INEI.get(anio)\n    if oficial is not None:\n        assert abs(pob_sumaria - oficial) < 0.1, f\"sumaria: {pob_sumaria:.2f}\"\n        assert abs(pob_personas - oficial) < 0.1, f\"personas: {pob_personas:.2f}\"\n    if anio in EXTREMA_INEI:\n        assert abs(ext_sumaria - EXTREMA_INEI[anio]) < 0.1, f\"extrema: {ext_sumaria:.2f}\"\n    if anio in RESIDENTES:\n        assert len(
[... salida recortada: 4,876 caracteres]
```

**Herramienta `Bash`**

```json
{
 "command": "PYTHONIOENCODING=utf-8 uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024 && uv run python -c \"\nimport pandas as pd\nb=pd.read_parquet('salidas/personas_2024.parquet'); print(b.shape); print(b.dtypes.to_string()); print(b.head(3).to_string())\nt=lambda d:100*(d.pobre*d.facpob07).sum()/d.facpob07.sum()\nprint('Cusco',round(t(b[b.departamento=='08']),1),'urbano',round(t(b[b.urbano]),1),'rural',round(t(b[~b.urbano]),1),'LimaMet',round(t(b[b.dominio==8]),1))\nprint('p208a 99:', (b.p208a==99).sum(), 'p208a na:', b.p208a.isna().sum(), 'deptos', b.departamento.nunique())\n\"",
 "description": "Ejecutar limpiar.py y revisar la base resultante",
 "timeout": 300000
}
```

<details><summary>Resultado</summary>

```text
File created successfully at: ~\Documents\GitHub\enaho-skills\.claude\skills\limpiando-enaho\scripts\limpiar.py (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>Resultado</summary>

```text
ENAHO 2024
Filas módulo 200: 117,721
Residentes habituales: 108,664
Hogares (sumaria): 33,691
Población expandida: 34,482,700
Pobreza (sumaria, factor07 x mieperho): 27.58 %
Pobreza extrema (sumaria): 5.50 %
Pobreza (personas, facpob07): 27.53 %
Cifra oficial INEI: 27.6 %

(108664, 18)
conglome             str
vivienda             str
hogar                str
codperso             str
p203                int8
p207             float64
p208a            float64
facpob07         float32
pobreza             int8
mieperho            int8
factor07         float32
ubigeo               str
estrato             int8
dominio             int8
departamento         str
urbano              bool
pobre               bool
pobre_extremo       bool
  conglome vivienda hogar codperso  p203  p207  p208a    facpob07  pobreza  mieperho    factor07  ubigeo  estrato  dominio departamento  urbano  pobre  pobre_extremo
0   010651      013    11       01     1   1.0   74.0  115.814941        3         4  115.814941  150509        4        2           15    True  False          False
1   010651      013    11       02     2   2.0   70.0  115.814941        3         4  115.814941  150509        4        2           15    True  False          False
2   010651      013    11       03     5   2.0   22.0  115.814941        3         4  115.814941  150509        4        2           15    True  False          False
Cusco 18.5 urbano 24.7 rural 39.4 LimaMet 28.0
p208a 99: 0 p208a na: 0 deptos 25
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "uv run python -c \"\nimport pandas as pd\ns=pd.read_stata('datos/966-Modulo34/sumaria-2024.dta',convert_categoricals=False)\nw=s.factor07*s.mieperho; p=(s.pobreza<=2)\nt=lambda m:round(100*(p[m]*w[m]).sum()/w[m].sum(),1)\nprint('sumaria -> urbano',t(s.estrato<=5),'rural',t(s.estrato>5),'LimaMet',t(s.dominio==8),'Cusco',t(s.ubigeo.str[:2]=='08'))\n\"",
 "description": "Recalcular urbano/rural con la sumaria",
 "timeout": 180000
}
```

<details><summary>Resultado</summary>

```text
sumaria -> urbano 24.8 rural 39.3 LimaMet 28.2 Cusco 18.5
```

</details>

**Herramienta `Write`**

```json
{
 "file_path": "~\\Documents\\GitHub\\enaho-skills\\.claude\\skills\\limpiando-enaho\\SKILL.md",
 "content": "---\nname: limpiando-enaho\ndescription: Limpia los módulos 34 (sumaria) y 02 (miembros) de la ENAHO del INEI y arma una base de personas con pobreza y factor de expansión. Úsala cuando pidan limpiar, unir o analizar la ENAHO, o calcular pobreza por región, departamento, área, sexo o edad.\nargument-hint: [año]\n---\n# Limpiar la ENAHO\nSi no se indica año, usa 2024.\n\n1. Si faltan los zip en datos/, pide al usuario bajarlos del INEI (código 966 = 2024) y no sigas.\n2. Desde la raíz del repositorio, corre exactamente: uv run ${CLAUDE_SKILL_DIR}/scripts/limpiar.py --anio $0\n3. Lee salidas/validacion.txt. Si la pobreza difiere del INEI en más de 0.1 puntos, o el script falla en un assert, detente y avisa; no corrijas los datos a mano.\n4. Responde con salidas/personas_$0.parquet; toda cifra va ponderada con facpob07 y la pobreza es pobre = pobreza <= 2, nunca un promedio del código.\n5. Antes de usar una variable que no está en la base, lee reference.md.\n"
}
```

**Herramienta `Write`**

```json
{
 "file_path": "~\\Documents\\GitHub\\enaho-skills\\.claude\\skills\\limpiando-enaho\\reference.md",
 "content": "# Referencia de variables · ENAHO 2024\n\nCódigos tomados del diccionario del INEI (`Diccionario2024.pdf`, dentro de cada zip).\n\n## Variables de la base `salidas/personas_2024.parquet`\n\n| Variable | Viene de | Qué es | Códigos |\n|---|---|---|---|\n| `conglome`, `vivienda`, `hogar` | ambos | Llaves del hogar (texto, con ceros) | 6, 3 y 2 caracteres |\n| `codperso` | miembros | Número de la persona en el hogar (texto) | 2 caracteres |\n| `p203` | miembros | Parentesco con el jefe(a) del hogar | 0 panel, 1 jefe/jefa, 2 esposo(a), 3 hijo(a), 4 yerno/nuera, 5 nieto(a), 6 padres/suegros, 7 otros parientes, 8 trabajador del hogar, 9 pensionista, 10 otros no parientes, 11 hermano(a) |\n| `p207` | miembros | Sexo | 1 hombre, 2 mujer |\n| `p208a` | miembros | Edad en años cumplidos | 0–98; 99 es valor perdido |\n| `facpob07` | miembros | Factor de expansión de población | Peso de cada persona |\n| `pobreza` | sumaria | Pobreza monetaria del hogar | 1 pobre extremo, 2 pobre no extremo, 3 no pobre |\n| `mieperho` | sumaria | Total de miembros del hogar | Número |\n| `factor07` | sumaria | Factor de expansión del hogar | Peso de cada hogar |\n| `ubigeo` | sumaria | Ubicación geográfica (texto) | 6 dígitos: departamento, provincia, distrito |\n| `estrato` | sumaria | Estrato geográfico | 1–5 urbano (de 500 000 a más hasta 2 000 habitantes); 6 de 500 a 1 999 habitantes, 7 AER compuesto, 8 AER simple (rural) |\n| `dominio` | sumaria | Dominio geográfico | 1 Costa Norte, 2 Costa Centro, 3 Costa Sur, 4 Sierra Norte, 5 Sierra Centro, 6 Sierra Sur, 7 Selva, 8 Lima Metropolitana |\n| `departamento` | construida | `ubigeo[:2]` | Ver tabla de abajo |\n| `urbano` | construida | `estrato <= 5` | True / False |\n| `pobre` | construida | `pobreza <= 2` | True / False |\n| `pobre_extremo` | construida | `pobreza == 1` | True / False |\n\n## Cómo ponderar\n\n- Con la base de personas: `100 * (pobre * facpob07).sum() / facpob07.sum()`.\n- Con la sumaria (hogares): peso `factor07 * mieperho`. Así se calculan las cifras oficiales; puede diferir en una décima de la de personas (27.58 % frente a 27.53 % en 2024).\n\n## Códigos de departamento (`ubigeo[:2]`)\n\nPara unir con mapas u otras tablas se usa siempre el código, nunca el nombre.\n\n| Código | Departamento | Código | Departamento |\n|---|---|---|---|\n| 01 | Amazonas | 14 | Lambayeque |\n| 02 | Áncash | 15 | Lima (sin Callao) |\n| 03 | Apurímac | 16 | Loreto |\n| 04 | Arequipa | 17 | Madre de Dios |\n| 05 | Ayacucho | 18 | Moquegua |\n| 06 | Cajamarca | 19 | Pasco |\n| 07 | Callao | 20 | Piura |\n| 08 | Cusco | 21 | Puno |\n| 09 | Huancavelica | 22 | San Martín |\n| 10 | Huánuco | 23 | Tacna |\n| 11 | Ica | 24 | Tumbes |\n| 12 | Junín | 25 | Ucayali |\n| 13 | La Libertad | | |\n\nVariables que no están en la base (ingresos, gastos, educación, empleo) requieren otros módulos del INEI; antes de agregarlas, se pide confirmación al usuario.\n"
}
```

<details><summary>Resultado</summary>

```text
File created successfully at: ~\Documents\GitHub\enaho-skills\.claude\skills\limpiando-enaho\SKILL.md (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>Resultado</summary>

```text
File created successfully at: ~\Documents\GitHub\enaho-skills\.claude\skills\limpiando-enaho\reference.md (file state is current in your context — no need to Read it back)
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "uv run python -c \"\nimport pandas as pd; b=pd.read_parquet('salidas/personas_2024.parquet'); print(b.p208a.min(), b.p208a.max(), (b.p208a==0).sum(), b.p207.value_counts().to_dict(), b.estrato.value_counts().sort_index().to_dict())\"; cat salidas/validacion.txt; git status --short",
 "description": "Comprobar rangos de edad, sexo y estrato"
}
```

<details><summary>Resultado</summary>

```text
0.0 98.0 1150 {2.0: 56077, 1.0: 52587} {1: 19655, 2: 21482, 3: 8753, 4: 8567, 5: 14136, 6: 5596, 7: 21441, 8: 9034}
ENAHO 2024
Filas módulo 200: 117,721
Residentes habituales: 108,664
Hogares (sumaria): 33,691
Población expandida: 34,482,700
Pobreza (sumaria, factor07 x mieperho): 27.58 %
Pobreza extrema (sumaria): 5.50 %
Pobreza (personas, facpob07): 27.53 %
Cifra oficial INEI: 27.6 %
?? .claude/
?? .gitignore
?? .python-version
?? README.md
?? datos/
?? pyproject.toml
?? salidas/
?? uv.lock
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "sed -i 's|^datos/\\*\\.zip$|datos/**/*.zip|' .gitignore && sed -i 's/| 0–98; 99 es valor perdido |/| 0–98 (0 = menor de un año; el diccionario indica 1–98 y los meses van en `p208b`); 99 es valor perdido |/' .claude/skills/limpiando-enaho/reference.md && grep -n \"p208a\\` \" .claude/skills/limpiando-enaho/reference.md && cat .gitignore && git add -n . | grep -v \"^add '.venv\"",
 "description": "Corregir .gitignore y la nota de edad; simular git add"
}
```

<details><summary>Resultado</summary>

```text
13:| `p208a` | miembros | Edad en años cumplidos | 0–98 (0 = menor de un año; el diccionario indica 1–98 y los meses van en `p208b`); 99 es valor perdido |
# Entorno
.venv/
__pycache__/

# Microdatos del INEI: pesan bastante y se descargan del portal
datos/**/*.zip
datos/**/*.dta
datos/**/*.pdf
add '.claude/skills/limpiando-enaho/SKILL.md'
add '.claude/skills/limpiando-enaho/reference.md'
add '.claude/skills/limpiando-enaho/scripts/limpiar.py'
add '.gitignore'
add '.python-version'
add 'README.md'
add 'datos/peru_departamental_simple.geojson'
add 'pyproject.toml'
add 'salidas/personas_2024.parquet'
add 'salidas/validacion.txt'
add 'uv.lock'
[This command modified 2 files you've previously read: .gitignore, .claude\skills\limpiando-enaho\reference.md. Call Read before editing.]
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "ls -la salidas/ && find .claude -type f",
 "description": "Ver tamaño del parquet y archivos de la skill"
}
```

**Herramienta `Edit`**

```json
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

**Herramienta `Bash`**

```json
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

<details><summary>Resultado</summary>

```text
total 477
drwxr-xr-x 1 USER 197121      0 Oct 31 08:53 .
drwxr-xr-x 1 USER 197121      0 Oct 31 08:54 ..
-rw-r--r-- 1 USER 197121 480478 Oct 31 08:53 personas_2024.parquet
-rw-r--r-- 1 USER 197121    284 Oct 31 08:53 validacion.txt
.claude/skills/limpiando-enaho/reference.md
.claude/skills/limpiando-enaho/scripts/limpiar.py
.claude/skills/limpiando-enaho/SKILL.md
```

</details>

<details><summary>Resultado</summary>

```text
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

</details>

<details><summary>Resultado</summary>

```text
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

</details>

## Asistente · 2026-10-31 13:55

## 🔶 Revisión manual 2: fin del Paso 2 (Limpiar). Necesito que revises `validacion.txt`.

### El resultado: `salidas/validacion.txt`

```
ENAHO 2024
Filas módulo 200: 117,721
Residentes habituales: 108,664
Hogares (sumaria): 33,691
Población expandida: 34,482,700
Pobreza (sumaria, factor07 x mieperho): 27.58 %
Pobreza extrema (sumaria): 5.50 %
Pobreza (personas, facpob07): 27.53 %
Cifra oficial INEI: 27.6 %
```

Comparado con la tabla del punto 2.4 del PDF:

| Indicador | Esperado | Obtenido | |
|---|---|---|---|
| Filas en el módulo 200 | 117,721 | 117,721 | ✅ |
| Residentes habituales | 108,664 | 108,664 | ✅ |
| Hogares en la sumaria | 33,691 | 33,691 | ✅ |
| Población representada | ≈34.5 millones | 34,482,700 | ✅ |
| Pobreza con la sumaria (`factor07 × mieperho`) | 27.58% | 27.58% | ✅ |
| Pobreza con personas (`facpob07`) | 27.53% | 27.53% | ✅ |
| Pobreza extrema (`pobreza == 1`) | 5.5% | 5.50% | ✅ |

También comprobé el primer pedido de evaluación del Paso 4: **Cusco = 18.5%**, igual que la referencia.

### Cómo funciona el pipeline, paso a paso (`scripts/limpiar.py`)

1. **Leer:** `pd.read_stata(..., convert_categoricals=False)` deja los códigos como números (1, 2, 3) en lugar de etiquetas. Las llaves se pasan a texto con `zfill`, así `"015009"` conserva su cero.
2. **Normalizar:** las columnas se pasan a minúscula y la «ñ» se reemplaza, de modo que `aÑo` → `anio`.
3. **Filtrar residentes:** según el diccionario del INEI, se conservan dos grupos. El primero son los miembros (`p204 == 1`) que **no** estuvieron ausentes 30 días o más (`p205 == 2`). El segundo son los no miembros (`p204 == 2`) que **sí** estuvieron presentes 30 días o más (`p206 == 1`). El filtro baja de 117,721 a 108,664 filas.
4. **Unir:** `merge(..., validate="m:1")` exige que cada hogar aparezca una sola vez en la sumaria. Si algún hogar estuviera repetido, pandas lanza un error en vez de multiplicar personas sin avisar.
5. **Construir:** `departamento = ubigeo[:2]`, `urbano = estrato <= 5`, `pobre = pobreza <= 2` y `pobre_extremo = pobreza == 1`. Así la pobreza se trata como categoría y nunca como promedio del código.
6. **Validar:** los `assert` detienen el script si algo no cuadra.
7. **Guardar:** el `.parquet` y el `validacion.txt`.

### Decisiones que debes validar

1. **Dos `assert` adicionales al esqueleto:** uno exige 5.5% de pobreza extrema y otro 108,664 residentes. Ambas cifras son las que la clase pide validar, pero el esqueleto no las comprobaba.
2. **`SKILL.md`:** es la versión de la clase con cuatro agregados:
   - «Si no se indica año, usa 2024», que el PDF recomienda en la pág. 9.
   - «Desde la raíz del repositorio».
   - «no corrijas los datos a mano».
   - Las palabras «departamento, área» en la `description`, para que también se active con pedidos como el de Cusco (criterio del punto 4.3).
3. **`reference.md`:** los códigos se tomaron del diccionario PDF del INEI. Encontré una discrepancia: el diccionario dice que `p208a` va de 1 a 98, pero en los datos hay **1,150 personas con edad 0** (menores de un año). Lo dejé anotado en el archivo.
4. **`.gitignore`:** cambié `datos/*.zip` por `datos/**/*.zip`, porque dentro de `966-Modulo34/` hay otro zip que se habría subido.

### Una pregunta y un aviso para el Paso 3

- **❓ ¿Subo `salidas/personas_2024.parquet` a GitHub?** Pesa 480 KB. **Recomiendo no subirlo** y agregarlo al `.gitignore`. La entrega solo pide `validacion.txt`, quien clone el repo lo regenera con la skill, y la prueba de encadenamiento del Paso 4 exige borrarlo de todas formas.
- **⚠️ Urbano/rural:** con la base de personas y `facpob07` salen **24.7% / 39.4%**, mientras que la clase reporta 24.8% / 39.3%. Verifiqué que con la sumaria salen exactamente 24.8% / 39.3%, así que la diferencia es de método y no un error, como advierte el PDF en la pág. 13. Como la regla de `graficando-enaho` es «pondera siempre con `facpob07`», el gráfico mostrará **24.7% / 39.4%**, y lo dejaré explicado en `evaluacion.md`.

Puedes abrir los archivos en `~\Documents\GitHub\enaho-skills\.claude\skills\limpiando-enaho\`. **¿Apruebas el Paso 2 y continúo con el Paso 3 (graficar y mapear)?** Dime también qué decides sobre el `.parquet`.

## Usuario · 2026-10-31 14:03

Apruebo tus decisiones. No subas salidas/personas_2024.parque, según las indicaciones del ejercicio. Continúa con el Paso 3.

## Asistente · 2026-10-31 14:03

Agrego primero el `.parquet` al `.gitignore` y luego escribo la skill `graficando-enaho`.

**Herramienta `Bash`**

```json
{
 "command": "cd ~/Documents/GitHub/enaho-skills && printf '\\n# Base limpia: se regenera con la skill limpiando-enaho\\nsalidas/*.parquet\\n' >> .gitignore && cat .gitignore",
 "description": "Ignorar el parquet en git"
}
```

**Herramienta `Write`**

```json
{
 "file_path": "~\\Documents\\GitHub\\enaho-skills\\.claude\\skills\\graficando-enaho\\scripts\\graficar.py",
 "content": "\"\"\"Grafica la pobreza monetaria de la ENAHO 2024 por área, sexo o grupo de edad.\n\nSe corre desde la raíz del repositorio:\n    uv run .claude/skills/graficando-enaho/scripts/graficar.py --por area\n\"\"\"\nimport argparse\nfrom pathlib import Path\n\nimport matplotlib.pyplot as plt\nimport pandas as pd\n\nBASE = Path(\"salidas/personas_2024.parquet\")\nCOLOR = \"#B5441B\"  # un solo color para todas las barras\nETIQUETAS = {\"area\": \"área\", \"sexo\": \"sexo\", \"edad\": \"grupo de edad\"}\n\nparser = argparse.ArgumentParser()\nparser.add_argument(\"--por\", choices=[\"area\", \"sexo\", \"edad\"], default=\"area\")\npor = parser.parse_args().por\n\nif not BASE.exists():\n    raise SystemExit(f\"Falta {BASE}. Usa primero la skill limpiando-enaho.\")\n\nbase = pd.read_parquet(BASE)\nbase[\"area\"] = base.urbano.map({True: \"Urbana\", False: \"Rural\"})\nbase[\"sexo\"] = base.p207.map({1: \"Hombre\", 2: \"Mujer\"})\n# Grupos de edad fijos, para que el gráfico salga siempre igual\nbase[\"edad\"] = pd.cut(base.p208a, [-1, 17, 29, 44, 59, 200],\n                      labels=[\"0-17\", \"18-29\", \"30-44\", \"45-59\", \"60+\"])\n\n# Se pondera con facpob07: nunca se cuentan encuestas\nbase[\"pobre_w\"] = base.pobre * base.facpob07\ng = base.groupby(por, observed=True)[[\"pobre_w\", \"facpob07\"]].sum()\ntasa = (100 * g.pobre_w / g.facpob07).sort_values()\n\nfig, ax = plt.subplots(figsize=(7, 4))\nbarras = ax.barh(tasa.index.astype(str), tasa.values, color=COLOR)\nax.bar_label(barras, fmt=\"%.1f %%\", padding=3)\nax.set_xlim(0, tasa.max() * 1.15)  # empieza en cero\nax.set_xlabel(\"% de personas en pobreza monetaria\")\nax.set_title(f\"Pobreza monetaria por {ETIQUETAS[por]}, 2024\")\nfig.text(0.01, 0.01, \"Fuente: INEI, ENAHO 2024\", fontsize=8)\n\nPath(\"figuras\").mkdir(exist_ok=True)\nfig.savefig(f\"figuras/pobreza_{por}.png\", dpi=200, bbox_inches=\"tight\")\nprint(tasa.round(1).to_string())\n"
}
```

**Herramienta `Write`**

```json
{
 "file_path": "~\\Documents\\GitHub\\enaho-skills\\.claude\\skills\\graficando-enaho\\SKILL.md",
 "content": "---\nname: graficando-enaho\ndescription: Grafica la pobreza monetaria de la ENAHO del INEI por área (urbana y rural), sexo o grupo de edad, con barras ponderadas por facpob07. Úsala cuando pidan un gráfico, una figura, barras o una comparación de pobreza con la ENAHO.\nargument-hint: [area|sexo|edad]\n---\n# Graficar la ENAHO\n1. Si no existe salidas/personas_2024.parquet, usa primero la skill limpiando-enaho.\n2. Desde la raíz del repositorio, corre: uv run ${CLAUDE_SKILL_DIR}/scripts/graficar.py --por <area|sexo|edad>\n   («urbana y rural» es --por area; si piden varias comparaciones, corre una vez por cada una).\n3. Reglas fijas: ponderar con facpob07; barras desde cero, ordenadas; un solo color; valor en cada barra; título con qué y cuándo; nota \"Fuente: INEI, ENAHO 2024\"; PNG a 200 dpi en figuras/. No cambies estas reglas aunque el pedido no las mencione.\n4. Si piden otro corte (departamento, dominio), no improvises un gráfico: para departamentos usa la skill mapeando-enaho; para otras variables, avisa que el script no lo cubre.\n5. Responde con la ruta de la figura y las cifras en una frase.\n"
}
```

**Herramienta `Bash`**

```json
{
 "command": "cd ~/Documents/GitHub/enaho-skills && for p in area sexo edad; do PYTHONIOENCODING=utf-8 uv run .claude/skills/graficando-enaho/scripts/graficar.py --por $p; done; ls -la figuras",
 "description": "Generar los tres gráficos de pobreza",
 "timeout": 300000
}
```

<details><summary>Resultado</summary>

```text
# Entorno
.venv/
__pycache__/

# Microdatos del INEI: pesan bastante y se descargan del portal
datos/**/*.zip
datos/**/*.dta
datos/**/*.pdf

# Base limpia: se regenera con la skill limpiando-enaho
salidas/*.parquet
```

</details>

<details><summary>Resultado</summary>

```text
File created successfully at: ~\Documents\GitHub\enaho-skills\.claude\skills\graficando-enaho\scripts\graficar.py (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>Resultado</summary>

```text
File created successfully at: ~\Documents\GitHub\enaho-skills\.claude\skills\graficando-enaho\SKILL.md (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>Resultado</summary>

```text
area
Urbana    24.700001
Rural     39.400002
sexo
Hombre    27.400000
Mujer     27.700001
edad
45-59    21.4
60+      22.0
18-29    23.9
30-44    27.9
0-17     36.5
total 128
drwxr-xr-x 1 USER 197121     0 Oct 31 09:03 .
drwxr-xr-x 1 USER 197121     0 Oct 31 08:54 ..
-rw-r--r-- 1 USER 197121 34966 Oct 31 09:03 pobreza_area.png
-rw-r--r-- 1 USER 197121 49027 Oct 31 09:03 pobreza_edad.png
-rw-r--r-- 1 USER 197121 35763 Oct 31 09:03 pobreza_sexo.png
```

</details>

## Asistente · 2026-10-31 14:04

Las cifras se imprimen como `24.700001` porque `facpob07` viene en `float32`. Lo corrijo convirtiendo a `float64` antes de redondear, y reviso visualmente las figuras.

**Herramienta `Edit`**

```json
{
 "replace_all": false,
 "file_path": "~\\Documents\\GitHub\\enaho-skills\\.claude\\skills\\graficando-enaho\\scripts\\graficar.py",
 "old_string": "tasa = (100 * g.pobre_w / g.facpob07).sort_values()",
 "new_string": "tasa = (100 * g.pobre_w / g.facpob07).astype(\"float64\").sort_values()  # facpob07 llega en float32"
}
```

**Herramienta `Bash`**

```json
{
 "command": "for p in area sexo edad; do PYTHONIOENCODING=utf-8 uv run .claude/skills/graficando-enaho/scripts/graficar.py --por $p; done",
 "description": "Regenerar los gráficos con cifras limpias",
 "timeout": 300000
}
```

**Herramienta `Read`**

```json
{
 "file_path": "~\\Documents\\GitHub\\enaho-skills\\figuras\\pobreza_area.png"
}
```

**Herramienta `Read`**

```json
{
 "file_path": "~\\Documents\\GitHub\\enaho-skills\\figuras\\pobreza_edad.png"
}
```

<details><summary>Resultado</summary>

```text
The file ~\Documents\GitHub\enaho-skills\.claude\skills\graficando-enaho\scripts\graficar.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>Resultado</summary>

```text
area
Urbana    24.7
Rural     39.4
sexo
Hombre    27.4
Mujer     27.7
edad
45-59    21.4
60+      22.0
18-29    23.9
30-44    27.9
0-17     36.5
```

</details>

<details><summary>Resultado</summary>

```text
[imagen]
```

</details>

<details><summary>Resultado</summary>

```text
[imagen]
```

</details>

## Asistente · 2026-10-31 14:04

Los gráficos cumplen las seis reglas. Ahora la skill `mapeando-enaho`.

**Herramienta `Write`**

```json
{
 "file_path": "~\\Documents\\GitHub\\enaho-skills\\.claude\\skills\\mapeando-enaho\\scripts\\mapear.py",
 "content": "\"\"\"Mapea la pobreza monetaria de la ENAHO 2024 por departamento.\n\nSe corre desde la raíz del repositorio:\n    uv run .claude/skills/mapeando-enaho/scripts/mapear.py\n\"\"\"\nfrom pathlib import Path\n\nimport geopandas as gpd\nimport matplotlib.pyplot as plt\nimport pandas as pd\n\nBASE = Path(\"salidas/personas_2024.parquet\")\nGEOJSON = Path(\"datos/peru_departamental_simple.geojson\")\n\nif not BASE.exists():\n    raise SystemExit(f\"Falta {BASE}. Usa primero la skill limpiando-enaho.\")\nif not GEOJSON.exists():\n    raise SystemExit(f\"Falta {GEOJSON}. Descárgalo del repositorio del curso (ver README).\")\n\n# Pobreza ponderada con facpob07 por código de departamento (ubigeo[:2])\nbase = pd.read_parquet(BASE)\nbase[\"pobre_w\"] = base.pobre * base.facpob07\ng = base.groupby(\"departamento\")[[\"pobre_w\", \"facpob07\"]].sum()\npobreza = ((100 * g.pobre_w / g.facpob07).astype(\"float64\")  # facpob07 llega en float32\n           .rename(\"pobreza\").reset_index())\nassert len(pobreza) == 25, f\"la base tiene {len(pobreza)} departamentos, deben ser 25\"\n\n# Se une por código, nunca por nombre: «APURIMAC» no es «Apurímac»\nmapa = gpd.read_file(GEOJSON)\nmapa[\"departamento\"] = mapa.FIRST_IDDP.astype(str).str.zfill(2)\nmapa = mapa.merge(pobreza, on=\"departamento\", how=\"left\", validate=\"1:1\")\nassert len(mapa) == 25, f\"hay {len(mapa)} departamentos, deben ser 25\"\nassert mapa.pobreza.notna().all(), \"hay departamentos sin dato: revisa la unión\"\nassert {\"07\", \"15\"} <= set(mapa.departamento), \"Lima (15) y Callao (07) van separados\"\n\n# Un solo color de claro a oscuro, desde 0; nunca arcoíris\nfig, ax = plt.subplots(figsize=(7, 9))\nmapa.plot(column=\"pobreza\", cmap=\"Oranges\", vmin=0, legend=True,\n          edgecolor=\"white\", linewidth=0.5, ax=ax,\n          legend_kwds={\"label\": \"Pobreza monetaria (% de personas)\"})\nax.set_axis_off()\nax.set_title(\"Pobreza monetaria por departamento, 2024\")\nfig.text(0.01, 0.01, \"Fuente: INEI, ENAHO 2024\", fontsize=8)\n\nPath(\"mapas\").mkdir(exist_ok=True)\nfig.savefig(\"mapas/pobreza_departamento.png\", dpi=200, bbox_inches=\"tight\")\nsalida = mapa[[\"departamento\", \"NOMBDEP\", \"pobreza\"]].sort_values(\"pobreza\", ascending=False)\nprint(salida.round(1).to_string(index=False))\n"
}
```

**Herramienta `Write`**

```json
{
 "file_path": "~\\Documents\\GitHub\\enaho-skills\\.claude\\skills\\mapeando-enaho\\SKILL.md",
 "content": "---\nname: mapeando-enaho\ndescription: Mapea la pobreza monetaria de la ENAHO del INEI por departamento del Perú, ponderada por facpob07 y unida al GeoJSON por código de ubigeo. Úsala cuando pidan un mapa, un coroplético o la pobreza por departamento o región con la ENAHO.\n---\n# Mapear la ENAHO\n1. Si no existe salidas/personas_2024.parquet, usa primero la skill limpiando-enaho.\n2. Si falta datos/peru_departamental_simple.geojson, pide al usuario bajarlo (la URL está en el README) y no sigas.\n3. Desde la raíz del repositorio, corre: uv run ${CLAUDE_SKILL_DIR}/scripts/mapear.py\n4. Reglas fijas: unir por código (ubigeo[:2] con FIRST_IDDP), nunca por nombre; exigir 25 departamentos y ninguno sin dato; un color de claro a oscuro desde 0, nunca arcoíris; leyenda con la unidad (% de personas); Lima (15) y Callao (07) separados.\n5. Si el script falla en un assert, detente y avisa; no unas por nombre ni completes datos a mano.\n6. Responde con la ruta mapas/pobreza_departamento.png y los tres departamentos con más y con menos pobreza.\n"
}
```

**Herramienta `Bash`**

```json
{
 "command": "PYTHONIOENCODING=utf-8 uv run .claude/skills/mapeando-enaho/scripts/mapear.py > salidas/_mapa.txt && cat salidas/_mapa.txt && uv run python -c \"\nimport pandas as pd\nref=pd.read_csv('~/Documents/GitHub/Data-Science-Python/sessions/16-skills-enaho/referencias/pobreza_departamento_2024.csv',dtype={'ccdd':str})\nb=pd.read_parquet('salidas/personas_2024.parquet'); b['w']=b.pobre*b.facpob07\ng=b.groupby('departamento')[['w','facpob07']].sum(); mio=(100*g.w/g.facpob07).astype(float).round(1)\nref['mio']=ref.ccdd.map(mio); ref['dif']=(ref.mio-ref.pobreza_pct).round(1)\nprint(ref[ref.dif!=0].to_string(index=False)); print('max |dif|', ref.dif.abs().max())\n\" && rm salidas/_mapa.txt",
 "description": "Generar el mapa y compararlo con la referencia del curso",
 "timeout": 300000
}
```

**Herramienta `Read`**

```json
{
 "file_path": "~\\Documents\\GitHub\\enaho-skills\\mapas\\pobreza_departamento.png"
}
```

<details><summary>Resultado</summary>

```text
File created successfully at: ~\Documents\GitHub\enaho-skills\.claude\skills\mapeando-enaho\scripts\mapear.py (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>Resultado</summary>

```text
File created successfully at: ~\Documents\GitHub\enaho-skills\.claude\skills\mapeando-enaho\SKILL.md (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>Resultado</summary>

```text
departamento       NOMBDEP  pobreza
          06     CAJAMARCA     45.0
          16        LORETO     42.6
          21          PUNO     40.4
          10       HUANUCO     39.5
          19         PASCO     39.3
          07        CALLAO     33.8
          09  HUANCAVELICA     33.6
          05      AYACUCHO     33.0
          20         PIURA     31.8
          13   LA LIBERTAD     30.1
          25       UCAYALI     27.1
          15          LIMA     26.9
          24        TUMBES     26.6
          01      AMAZONAS     26.1
          03      APURIMAC     24.1
          23         TACNA     23.9
          02        ANCASH     22.9
          22    SAN MARTIN     22.0
          12         JUNIN     18.6
          08         CUSCO     18.5
          04      AREQUIPA     15.8
          14    LAMBAYEQUE     14.1
          17 MADRE DE DIOS     11.1
          18      MOQUEGUA     10.9
          11           ICA      5.9
ccdd departamento  pobreza_pct  mio  dif
  01     AMAZONAS         25.7 26.1  0.4
  02       ANCASH         22.8 22.9  0.1
  03     APURIMAC         24.0 24.1  0.1
  05     AYACUCHO         32.8 33.0  0.2
  07       CALLAO         33.9 33.8 -0.1
  09 HUANCAVELICA         33.4 33.6  0.2
  10      HUANUCO         39.0 39.5  0.5
  11          ICA          6.0  5.9 -0.1
  12        JUNIN         18.5 18.6  0.1
  13  LA LIBERTAD         30.2 30.1 -0.1
  14   LAMBAYEQUE         14.0 14.1  0.1
  15         LIMA         27.1 26.9 -0.2
  16       LORETO         43.0 42.6 -0.4
  18     MOQUEGUA         11.0 10.9 -0.1
  19        PASCO         39.0 39.3  0.3
  20        PIURA         31.9 31.8 -0.1
  21         PUNO         39.9 40.4  0.5
  23        TACNA         24.0 23.9 -0.1
  24       TUMBES         26.9 26.6 -0.3
max |dif| 0.5
```

</details>

<details><summary>Resultado</summary>

```text
[imagen]
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "uv run python -c \"\nimport pandas as pd\nref=pd.read_csv('~/Documents/GitHub/Data-Science-Python/sessions/16-skills-enaho/referencias/pobreza_departamento_2024.csv',dtype={'ccdd':str})\ns=pd.read_stata('datos/966-Modulo34/sumaria-2024.dta',convert_categoricals=False)\ns['w']=s.factor07*s.mieperho; s['pw']=(s.pobreza<=2)*s.w; s['d']=s.ubigeo.str[:2]\ng=s.groupby('d')[['pw','w']].sum(); su=(100*g.pw/g.w).astype(float).round(1)\nref['sumaria']=ref.ccdd.map(su); print('dif max sumaria vs ref:', (ref.sumaria-ref.pobreza_pct).abs().max())\n# hogares de la sumaria sin residentes en la base de personas\nb=pd.read_parquet('salidas/personas_2024.parquet')\nn=b.groupby(['conglome','vivienda','hogar']).size().rename('n').reset_index()\nm=s.merge(n,on=['conglome','vivienda','hogar'],how='left'); print('hogares sin personas:', m.n.isna().sum(), ' n != mieperho:', (m.n!=m.mieperho).sum())\n\"",
 "description": "Comparar método sumaria contra la referencia por departamento",
 "timeout": 180000
}
```

<details><summary>Resultado</summary>

```text
dif max sumaria vs ref: 0.0
hogares sin personas: 0  n != mieperho: 1846
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "uv run python -c \"\nimport pandas as pd\ns=pd.read_stata('datos/966-Modulo34/sumaria-2024.dta',convert_categoricals=False)\nb=pd.read_parquet('salidas/personas_2024.parquet')\nfor nombre,f in [('todos',b),('sin p203 8 y 9',b[~b.p203.isin([8,9])])]:\n    n=f.groupby(['conglome','vivienda','hogar']).size().rename('n').reset_index()\n    m=s.merge(n,on=['conglome','vivienda','hogar'],how='left'); print(nombre,'hogares con n != mieperho:',(m.n!=m.mieperho).sum())\nprint('facpob07 == factor07 en filas:', round(100*(b.facpob07==b.factor07).mean(),1),'%')\n\"",
 "description": "Explorar por qué difieren ambos métodos",
 "timeout": 180000
}
```

<details><summary>Resultado</summary>

```text
todos hogares con n != mieperho: 1846
sin p203 8 y 9 hogares con n != mieperho: 1804
facpob07 == factor07 en filas: 100.0 %
```

</details>

**Herramienta `Edit`**

```json
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

<details><summary>Resultado</summary>

```text
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

</details>

## Asistente · 2026-10-31 14:05

## 🔶 Revisión manual 3: fin del Paso 3 (Graficar y mapear). Necesito tu revisión y una decisión.

Ya agregué `salidas/*.parquet` al `.gitignore`, según tu indicación.

### 1. La skill `graficando-enaho`

**Archivos:** `SKILL.md` y `scripts/graficar.py`, sobre el núcleo del PDF (pág. 11). Generé las tres figuras en `figuras/`:

| Figura | Cifras (ponderadas con `facpob07`) |
|---|---|
| `pobreza_area.png` | Urbana 24.7% · Rural 39.4% |
| `pobreza_sexo.png` | Hombre 27.4% · Mujer 27.7% |
| `pobreza_edad.png` | 0-17: 36.5% · 30-44: 27.9% · 18-29: 23.9% · 60+: 22.0% · 45-59: 21.4% |

Revisé las imágenes y cumplen las seis reglas del punto 3.2:
- pondera con `facpob07`;
- las barras empiezan en cero y están ordenadas;
- usa un solo color y escribe el valor en cada barra;
- el título dice qué y cuándo («Pobreza monetaria por área, 2024»);
- lleva la nota «Fuente: INEI, ENAHO 2024»;
- es un PNG a 200 dpi.

**Cambios respecto al núcleo del PDF:**
- **Título con tilde:** el script del PDF habría escrito «por area». Añadí un diccionario `ETIQUETAS` para que diga «por área» y «por grupo de edad».
- **Cifras sin decimales sobrantes:** `facpob07` llega como `float32` y por eso las cifras se imprimían como `24.700001`. Se convierten a `float64`.
- **Mensaje si falta la base:** si no existe el `.parquet`, el script se detiene con «usa primero la skill limpiando-enaho». Así el encadenamiento funciona aunque Claude no lea el `SKILL.md` con cuidado.
- **Paso 4 en el `SKILL.md`:** si piden un corte que el script no cubre, como departamentos, la skill deriva el pedido a `mapeando-enaho` en vez de improvisar.

### 2. La skill `mapeando-enaho`

**Archivos:** `SKILL.md` y `scripts/mapear.py`, que genera `mapas/pobreza_departamento.png`. Cumple las reglas del punto 3.3:
- une `ubigeo[:2]` con `FIRST_IDDP` por código;
- exige 25 departamentos y ninguno sin dato;
- usa la escala `Oranges` desde 0;
- la leyenda dice «% de personas»;
- Lima (15) y Callao (07) salen separados.

Al esqueleto le agregué dos `assert` más. El primero verifica que la base tenga 25 departamentos **antes** de la unión. El segundo, que estén Lima y Callao.

### ❓ La decisión: las cifras del mapa no coinciden exactamente con la referencia

Comparé el mapa con `referencias/pobreza_departamento_2024.csv` del repositorio del curso:

| Departamento | Referencia (clase) | Mi mapa (`facpob07`) | Diferencia |
|---|---|---|---|
| Cajamarca | 45.0 | 45.0 | 0.0 |
| Loreto | 43.0 | 42.6 | −0.4 |
| Puno | 39.9 | **40.4** | +0.5 |
| Huánuco | 39.0 | 39.5 | +0.5 |
| Ica | 6.0 | 5.9 | −0.1 |
| Moquegua | 11.0 | 10.9 | −0.1 |
| Madre de Dios | 11.1 | 11.1 | 0.0 |

**Diagnóstico:** la unión está bien. Los 25 departamentos tienen dato y el orden general coincide. Si se calcula con la sumaria (`factor07 × mieperho`), los 25 departamentos coinciden **exactamente** con la referencia (diferencia máxima 0.0).

La causa no es el factor de expansión: `facpob07` es idéntico a `factor07` en todas las filas. Lo que cambia es **a quién se cuenta**. En 1,846 hogares, el número de residentes habituales de la base no coincide con `mieperho`, el total de miembros que registra el INEI. A nivel nacional esa diferencia es mínima (27.53% frente a 27.58%), pero en departamentos con menos encuestas llega a medio punto. (El PDF anticipa esto en la pág. 13, aunque habla de variaciones de «algún decimal».)

**Opciones:**
- **A (recomendada):** mantener `facpob07` con la base de personas, como en el esqueleto de la clase y la regla «toda cifra va ponderada con `facpob07`», y documentar la diferencia en `evaluacion.md` y en el README. Sigue el diseño del curso al pie de la letra: las tres skills comparten una sola base.
- **B:** que `limpiar.py` también guarde una base de hogares y que el mapa se calcule con la sumaria (`factor07 × mieperho`). Así las cifras coinciden exactamente con la referencia (Puno 39.9, Ica 6.0), pero se aparta del esqueleto y de la regla de `facpob07`.

### Lo que viene (Paso 4 · Evaluar y subir)

Las 6 corridas con `claude -p` (3 pedidos × con y sin skills), antes borrando el `.parquet`, seguidas de `evaluacion.md`, el `README.md` y la entrega. **Ese paso necesita tu autorización explícita**, por dos razones:
- las corridas consumen uso de tu cuenta;
- quizá tengas que lanzarlas tú con `!` si el sistema me bloquea.

Puedes ver las figuras en `~\Documents\GitHub\enaho-skills\figuras\` y el mapa en `~\Documents\GitHub\enaho-skills\mapas\pobreza_departamento.png`. **¿Apruebas el Paso 3? ¿Opción A o B? ¿Autorizas las corridas con `claude -p` del Paso 4?**

## Usuario · 2026-10-31 14:11

Apruebo el Paso 3, opción A; autorizo las corridas del Paso 4.

## Asistente · 2026-10-31 14:11

Empiezo el Paso 4. Antes de lanzar las 6 corridas, preparo cada una en una **copia aislada** del repositorio dentro del scratchpad. Así, las corridas «sin skills», que pueden escribir sus propios scripts, no sobrescribirán tus figuras ni tu mapa. En cada copia borro `salidas/`, `figuras/` y `mapas/`, tal como pide el punto 4.1.

**Herramienta `Bash`**

```json
{
 "command": "claude --version; claude --help 2>&1 | grep -E \"output-format|allowedTools|disallowedTools|permission-mode|verbose|max-turns\" | head",
 "description": "Revisar versión y opciones de claude CLI"
}
```

<details><summary>Resultado</summary>

```text
2.1.316 (Claude Code)
  --allowedTools, --allowed-tools <tools...>
  --disallowedTools, --disallowed-tools <tools...>
                                        --print and --output-format=stream-json)
                                        --output-format=stream-json)
                                        --output-format=stream-json)
  --output-format <format>              Output format (only works with --print):
  --permission-mode <mode>              Permission mode to use for the session
                                        --output-format=stream-json)
  --verbose                             Override verbose mode setting from
```

</details>

**Herramienta `Write`**

```json
{
 "file_path": "~\\AppData\\Local\\Temp\\claude\\C--Users-USER\\50afee40-1161-4293-b4a9-85c2739871ed\\scratchpad\\eval\\correr.sh",
 "content": "#!/usr/bin/env bash\n# Corre un pedido de evaluación en una copia aislada del repo.\n# Uso: correr.sh <id> <con|sin> \"<pedido>\"\nset -u\nID=\"$1\"; MODO=\"$2\"; PEDIDO=\"$3\"\nREPO=~/Documents/GitHub/enaho-skills\nEVAL=\"$(cd \"$(dirname \"$0\")\" && pwd)\"\nDIR=\"$EVAL/runs/$ID-$MODO\"\nrm -rf \"$DIR\"; mkdir -p \"$DIR\"\n# Copia sin .venv ni salidas: cada corrida parte de los datos crudos\n(cd \"$REPO\" && tar --exclude=.venv --exclude=.git -cf - .) | (cd \"$DIR\" && tar -xf -)\nrm -rf \"$DIR/salidas\" \"$DIR/figuras\" \"$DIR/mapas\"\nmkdir -p \"$DIR/salidas\" \"$DIR/figuras\" \"$DIR/mapas\"\n\nPERMISOS=(--allowedTools \"Bash(uv:*)\" \"Bash(python:*)\" \"Bash(ls:*)\" \"Bash(find:*)\" Read Write Edit Glob Grep Skill)\nEXTRA=()\n[ \"$MODO\" = \"sin\" ] && EXTRA=(--disallowedTools Skill)\n\ncd \"$DIR\"\nstart=$(date +%s)\nclaude -p \"$PEDIDO\" --output-format stream-json --verbose \"${PERMISOS[@]}\" \"${EXTRA[@]}\" \\\n  > \"$EVAL/runs/$ID-$MODO.jsonl\" 2> \"$EVAL/runs/$ID-$MODO.err\"\necho \"exit=$? segundos=$(( $(date +%s) - start ))\" >> \"$EVAL/runs/$ID-$MODO.err\"\n"
}
```

<details><summary>Resultado</summary>

```text
File created successfully at: ~\AppData\Local\Temp\claude\C--Users-USER\50afee40-1161-4293-b4a9-85c2739871ed\scratchpad\eval\correr.sh (file state is current in your context — no need to Read it back)
```

</details>

## Asistente · 2026-10-31 14:11

Pruebo primero una corrida (Cusco con skills) para verificar que el mecanismo funciona antes de lanzar las demás.

**Herramienta `Bash`**

```json
{
 "command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval\" && bash correr.sh 1 con \"¿Cuál fue la pobreza en Cusco en 2024?\"; cat runs/1-con.err; tail -c 1500 runs/1-con.jsonl",
 "description": "Correr el pedido de Cusco con skills",
 "timeout": 600000
}
```

<details><summary>Resultado</summary>

```text
exit=0 segundos=43
filtré el departamento con código `08`. Toda cifra está ponderada con `facpob07`, y una persona cuenta como pobre si `pobreza <= 2`. Para comprobar la limpieza, comparé la cifra nacional del script (27,53 %) con la oficial del INEI (27,6 %): la diferencia es menor a 0,1 puntos.\n\n**A tener en cuenta:**\n- **Margen de error:** con un solo departamento la muestra es más chica. Para las regiones, el INEI publica intervalos de confianza y a veces agrupa departamentos con niveles de pobreza parecidos. No comparé esta cifra con la publicación departamental del INEI, así que tómala como una estimación puntual.\n- **Error en el skill:** `limpiando-enaho` le pasa la primera palabra de tu pregunta como año al script (`--anio Calcular`). Lo corrí a mano con `--anio 2024`. Conviene corregir el skill para que lea bien el año de los argumentos.","ttft_ms":5489,"type":"result","duration_ms":39333,"uuid":"d5b29f38-b360-4c34-b4fe-aa9374ced732","ttft_stream_ms":3582,"time_to_request_ms":196,"first_content_frame_ms":3582,"queued_turn_count":0,"result_index":0,"model_usage_since_last_result":{"claude-opus-5-5":{"inputTokens":10,"outputTokens":1984,"cacheReadInputTokens":148932,"cacheCreationInputTokens":22192,"webSearchRequests":0,"costUSD":0.2470424,"contextWindow":1000000,"maxOutputTokens":128000,"thinkingTokens":317,"cacheCreationEphemeral5mInputTokens":0,"cacheCreationEphemeral1hInputTokens":22192,"canonicalModel":"claude-opus-5-5","provider":"firstParty","costBasis":"list"}}}
Shell cwd was reset to ~\Documents\GitHub\enaho-skills
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval\" && ~/anaconda3/python.exe - <<'EOF'\nimport json\nfor l in open(\"runs/1-con.jsonl\",encoding=\"utf-8\"):\n    e=json.loads(l)\n    if e.get(\"type\")==\"assistant\":\n        for c in e[\"message\"][\"content\"]:\n            if c[\"type\"]==\"tool_use\": print(\"TOOL\",c[\"name\"],json.dumps(c[\"input\"],ensure_ascii=False)[:300])\n    if e.get(\"type\")==\"user\":\n        for c in e[\"message\"][\"content\"] if isinstance(e[\"message\"][\"content\"],list) else []:\n            if c.get(\"type\")==\"tool_result\":\n                t=c[\"content\"] if isinstance(c[\"content\"],str) else \" \".join(x.get(\"text\",\"\") for x in c[\"content\"])\n                print(\"  ->\",t[:250].replace(\"\\n\",\" | \"))\nEOF",
 "description": "Listar herramientas usadas en la corrida de Cusco"
}
```

<details><summary>Resultado (error)</summary>

```text
Exit code 1
TOOL Skill {"skill": "limpiando-enaho", "args": "Calcular la pobreza monetaria en Cusco en 2024"}
  -> Launching skill: limpiando-enaho
TOOL Glob {"pattern": "**/*"}
  -> datos\966-Modulo02\enaho_tabla_ciuo_88.dta | datos\966-Modulo02\enaho_tabla_cno_2015.dta | datos\966-Modulo02\Criterios para codificar Ocupaciones Peligrosas.pdf | datos\966-Modulo02\FichaTecnica.pdf | datos\966-Modulo34\FichaTecnica.pdf | datos\966-Modulo02\C
TOOL Bash {"command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval/runs/1-con\" && uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024 2>&1 | tail -30", "description": "Run ENAHO cleaning script for 2024", "timeout": 600000}
  -> Traceback (most recent call last):
  File "<stdin>", line 11, in <module>
  File "~\anaconda3\Lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeEncodeError: 'charmap' codec can't encode character '\ufffd' in position 118: character maps to <undefined>
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval\" && cat > resumir.py <<'EOF'\n\"\"\"Resume una corrida: herramientas usadas, resultados breves, respuesta final y costo.\"\"\"\nimport json, sys\nsys.stdout.reconfigure(encoding=\"utf-8\")\nfor l in open(sys.argv[1], encoding=\"utf-8\"):\n    e = json.loads(l)\n    if e.get(\"type\") == \"assistant\":\n        for c in e[\"message\"][\"content\"]:\n            if c[\"type\"] == \"tool_use\":\n                print(\"TOOL\", c[\"name\"], json.dumps(c[\"input\"], ensure_ascii=False)[:400])\n    elif e.get(\"type\") == \"user\" and isinstance(e[\"message\"][\"content\"], list):\n        for c in e[\"message\"][\"content\"]:\n            if c.get(\"type\") == \"tool_result\":\n                t = c[\"content\"] if isinstance(c[\"content\"], str) else \" \".join(x.get(\"text\", \"\") for x in c[\"content\"])\n                print(\"   ->\", t[:300].replace(\"\\n\", \" | \"))\n    elif e.get(\"type\") == \"result\":\n        print(\"\\n=== RESPUESTA ===\\n\" + e.get(\"result\", \"\"))\n        print(f\"\\ncosto USD: {e.get('total_cost_usd')}, turnos: {e.get('num_turns')}\")\nEOF\n~/anaconda3/python.exe resumir.py runs/1-con.jsonl | head -c 6000; ls runs/1-con/salidas runs/1-con/figuras",
 "description": "Crear resumidor de corridas y ver la de Cusco"
}
```

<details><summary>Resultado</summary>

```text
TOOL Skill {"skill": "limpiando-enaho", "args": "Calcular la pobreza monetaria en Cusco en 2024"}
   -> Launching skill: limpiando-enaho
TOOL Glob {"pattern": "**/*"}
   -> datos\966-Modulo02\enaho_tabla_ciuo_88.dta | datos\966-Modulo02\enaho_tabla_cno_2015.dta | datos\966-Modulo02\Criterios para codificar Ocupaciones Peligrosas.pdf | datos\966-Modulo02\FichaTecnica.pdf | datos\966-Modulo34\FichaTecnica.pdf | datos\966-Modulo02\CED-01-200-2024.pdf | datos\966-Modulo34\Sumaria-2024
TOOL Bash {"command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval/runs/1-con\" && uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024 2>&1 | tail -30", "description": "Run ENAHO cleaning script for 2024", "timeout": 600000}
   -> Using CPython 3.14.8 | Creating virtual environment at: .venv | Installed 19 packages in 1.79s | ENAHO 2024 | Filas m�dulo 200: 117,721 | Residentes habituales: 108,664 | Hogares (sumaria): 33,691 | Poblaci�n expandida: 34,482,700 | Pobreza (sumaria, factor07 x mieperho): 27.58 % | Pobreza extrema (sumaria): 5.
TOOL Bash {"command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval/runs/1-con\" && cat salidas/validacion.txt; ls salidas; cat .claude/skills/limpiando-enaho/reference.md", "description": "Read validation output and reference notes"}
   -> ENAHO 2024 | Filas módulo 200: 117,721 | Residentes habituales: 108,664 | Hogares (sumaria): 33,691 | Población expandida: 34,482,700 | Pobreza (sumaria, factor07 x mieperho): 27.58 % | Pobreza extrema (sumaria): 5.50 % | Pobreza (personas, facpob07): 27.53 % | Cifra oficial INEI: 27.6 % | personas_2024.parq
TOOL Bash {"command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval/runs/1-con\" && uv run python -c \"\nimport pandas as pd\nd=pd.read_parquet('salidas/personas_2024.parquet')\nc=d[d.departamento=='08']\nw=c.facpob07\nf=lambda m:100*(m*w).sum()/w.sum()\nprint('n',len(c),'pob',round(w.sum()))\nprint('pobreza',round(f(c.pobre),2))\nprint('ext
   -> n 3777 pob 1380357 | pobreza 18.54 | extrema 2.15 | rural 25.0 1872 | urbano 14.72 1905 | Shell cwd was reset to ~\AppData\Local\Temp\claude\C--Users-USER\50afee40-1161-4293-b4a9-85c2739871ed\scratchpad\eval\runs\1-con

=== RESPUESTA ===
Según la ENAHO 2024, el **18,5 %** de la población de Cusco era pobre en términos monetarios en 2024.

| Indicador (Cusco, 2024) | Valor |
|---|---|
| Pobreza monetaria | **18,54 %** |
| Pobreza extrema | 2,15 % |
| Pobreza urbana | 14,72 % |
| Pobreza rural | 25,00 % |
| Población expandida | 1 380 357 personas |
| Muestra | 3777 personas |

En el promedio nacional la pobreza fue de 27,53 %, así que Cusco quedó unos 9 puntos por debajo.

**Cómo lo calculé:** usé la base de personas `salidas/personas_2024.parquet` y filtré el departamento con código `08`. Toda cifra está ponderada con `facpob07`, y una persona cuenta como pobre si `pobreza <= 2`. Para comprobar la limpieza, comparé la cifra nacional del script (27,53 %) con la oficial del INEI (27,6 %): la diferencia es menor a 0,1 puntos.

**A tener en cuenta:**
- **Margen de error:** con un solo departamento la muestra es más chica. Para las regiones, el INEI publica intervalos de confianza y a veces agrupa departamentos con niveles de pobreza parecidos. No comparé esta cifra con la publicación departamental del INEI, así que tómala como una estimación puntual.
- **Error en el skill:** `limpiando-enaho` le pasa la primera palabra de tu pregunta como año al script (`--anio Calcular`). Lo corrí a mano con `--anio 2024`. Conviene corregir el skill para que lea bien el año de los argumentos.

costo USD: 0.2470424, turnos: 7
runs/1-con/figuras:

runs/1-con/salidas:
personas_2024.parquet
validacion.txt
Shell cwd was reset to ~\Documents\GitHub\enaho-skills
```

</details>

**Herramienta `Write`**

```json
{
 "file_path": "~\\Documents\\GitHub\\enaho-skills\\.claude\\skills\\limpiando-enaho\\SKILL.md",
 "content": "---\nname: limpiando-enaho\ndescription: Limpia los módulos 34 (sumaria) y 02 (miembros) de la ENAHO del INEI y arma una base de personas con pobreza y factor de expansión. Úsala cuando pidan limpiar, unir o analizar la ENAHO, o calcular pobreza por región, departamento, área, sexo o edad.\nargument-hint: [año]\n---\n# Limpiar la ENAHO\nAño de trabajo: si en «$ARGUMENTS» aparece un año de cuatro dígitos, usa ese; si no, usa 2024. En los pasos de abajo, <año> es ese número.\n\n1. Si faltan los zip en datos/, pide al usuario bajarlos del INEI (código 966 = 2024) y no sigas.\n2. Desde la raíz del repositorio, corre exactamente: uv run ${CLAUDE_SKILL_DIR}/scripts/limpiar.py --anio <año>\n3. Lee salidas/validacion.txt. Si la pobreza difiere del INEI en más de 0.1 puntos, o el script falla en un assert, detente y avisa; no corrijas los datos a mano.\n4. Responde con salidas/personas_<año>.parquet; toda cifra va ponderada con facpob07 y la pobreza es pobre = pobreza <= 2, nunca un promedio del código.\n5. Antes de usar una variable que no está en la base, lee reference.md.\n"
}
```

**Herramienta `Bash`**

```json
{
 "command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval\" && mv runs/1-con.jsonl runs/v1-1-con.jsonl && mv runs/1-con.err runs/v1-1-con.err && rm -rf runs/1-con && \\\n( bash correr.sh 1 con \"¿Cuál fue la pobreza en Cusco en 2024?\" & \\\n  bash correr.sh 1 sin \"¿Cuál fue la pobreza en Cusco en 2024?\" & \\\n  bash correr.sh 2 con \"Grafica la pobreza urbana y rural\" & \\\n  bash correr.sh 2 sin \"Grafica la pobreza urbana y rural\" & \\\n  bash correr.sh 3 con \"Haz un mapa de la pobreza por departamento con la ENAHO 2024\" & \\\n  bash correr.sh 3 sin \"Haz un mapa de la pobreza por departamento con la ENAHO 2024\" & \\\n  wait ); for f in runs/*.err; do echo \"$f: $(tail -1 $f)\"; done",
 "description": "Lanzar las seis corridas de evaluación en paralelo",
 "run_in_background": true
}
```

<details><summary>Resultado</summary>

```text
The file ~\Documents\GitHub\enaho-skills\.claude\skills\limpiando-enaho\SKILL.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>Resultado</summary>

```text
Command running in background with ID: b98gspe7n. Output is being written to: ~\AppData\Local\Temp\claude\C--Users-USER\50afee40-1161-4293-b4a9-85c2739871ed\tasks\b98gspe7n.output. You will be notified when it completes — do not poll that file or sleep while waiting. Read the file only if the user asks for progress, or if you need a line it prints before you can go on, such as a server's ready line or port.
Session cwd remains ~\Documents\GitHub\enaho-skills; directory changes made by the backgrounded command do not apply to subsequent commands.
```

</details>

## Asistente · 2026-10-31 14:13

Mientras corren las seis evaluaciones, redacto el `README.md`.

**Herramienta `Write`**

```json
{
 "file_path": "~\\Documents\\GitHub\\enaho-skills\\README.md",
 "content": "# Skills de Claude Code para limpiar, graficar y mapear la ENAHO 2024\n\nEl presente repositorio contiene tres *skills* de Claude Code que convierten los microdatos de la Encuesta Nacional de Hogares (ENAHO) 2024 del INEI en una base de personas lista para analizar, y que a partir de ella grafican y mapean la pobreza monetaria. Se trata de la tarea de la Clase 8 del curso Python Intermedio para CCSS y Gestión Pública (Diplomatura de Ciencia de Datos, Q-LAB PUCP).\n\nY es que, si se le pide dos veces a Claude que limpie la ENAHO sin reglas fijas, puede devolver dos bases distintas: una vez deja a todos los miembros y otra solo a los residentes habituales, una vez pondera con el factor de expansión y otra cuenta encuestas, una vez lee el `ubigeo` como texto y otra como número, perdiendo los ceros. Las skills fijan esas decisiones una sola vez, en scripts versionados, de modo que quien clone el repositorio obtenga siempre la misma base, los mismos gráficos y el mismo mapa.\n\n## Las tres skills\n\n| Skill | Entra | Sale |\n|---|---|---|\n| [`limpiando-enaho`](.claude/skills/limpiando-enaho/SKILL.md) | Los módulos 34 (sumaria) y 02 (miembros) del INEI | `salidas/personas_2024.parquet` y `salidas/validacion.txt` |\n| [`graficando-enaho`](.claude/skills/graficando-enaho/SKILL.md) | La base limpia y un corte: área, sexo o edad | `figuras/pobreza_<corte>.png` |\n| [`mapeando-enaho`](.claude/skills/mapeando-enaho/SKILL.md) | La base limpia y los límites de los 25 departamentos | `mapas/pobreza_departamento.png` |\n\nLas skills de gráficos y mapas indican que, si no existe `salidas/personas_2024.parquet`, se use primero `limpiando-enaho`; así, un solo pedido activa dos skills seguidas.\n\nʼʼʼtext\n.claude/skills/\n  limpiando-enaho/   SKILL.md · reference.md · scripts/limpiar.py\n  graficando-enaho/  SKILL.md · scripts/graficar.py\n  mapeando-enaho/    SKILL.md · scripts/mapear.py\nsalidas/validacion.txt\nfiguras/  mapas/\nevaluacion.md  README.md  pyproject.toml\nʼʼʼ\n\n## Requisitos e instalación\n\nSe requieren [uv](https://docs.astral.sh/uv/) y [Claude Code](https://code.claude.com/docs). Luego de clonar el repositorio:\n\nʼʼʼbash\nuv sync\nʼʼʼ\n\n## Descarga de datos\n\nLos microdatos no se suben al repositorio (ver `.gitignore`), por lo que deben descargarse a la carpeta `datos/`. El código `966` corresponde a la ENAHO 2024 en el portal de microdatos del INEI.\n\nʼʼʼbash\ncd datos\ncurl -LO https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo34.zip\ncurl -LO https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo02.zip\nunzip -o 966-Modulo34.zip && unzip -o 966-Modulo02.zip\ncd ..\nʼʼʼ\n\nSi `curl` falla por el certificado del INEI, los zip pueden bajarse desde el navegador y moverse a `datos/`. El GeoJSON departamental (`datos/peru_departamental_simple.geojson`) sí está incluido en el repositorio; su fuente es el [repositorio del curso](https://raw.githubusercontent.com/d2cml-ai/Data-Science-Python/main/sessions/06-geoespacial/lab/Data/peru_departamental_simple.geojson).\n\n## Cómo usarlo\n\nDentro de Claude Code, desde la raíz del repositorio, basta con pedirlo en lenguaje natural:\n\n- «¿Cuál fue la pobreza en Cusco en 2024?» → activa `limpiando-enaho`.\n- «Grafica la pobreza urbana y rural» → activa `graficando-enaho` (y antes `limpiando-enaho`, si falta la base).\n- «Haz un mapa de la pobreza por departamento» → activa `mapeando-enaho` (y antes `limpiando-enaho`, si falta la base).\n\nTambién pueden llamarse a mano: `/limpiando-enaho 2024`, `/graficando-enaho sexo` o `/mapeando-enaho`. Los scripts, a su vez, pueden correrse sin Claude:\n\nʼʼʼbash\nuv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024\nuv run .claude/skills/graficando-enaho/scripts/graficar.py --por area   # area | sexo | edad\nuv run .claude/skills/mapeando-enaho/scripts/mapear.py\nʼʼʼ\n\n## Cómo se limpia la ENAHO\n\n`li
[... salida recortada: 6,450 caracteres]
```

<details><summary>Resultado</summary>

```text
File created successfully at: ~\Documents\GitHub\enaho-skills\README.md (file state is current in your context — no need to Read it back)
```

</details>

## Asistente · 2026-10-31 14:13

Las seis corridas siguen en segundo plano. Cuando terminen, las analizo y redacto `evaluacion.md`.

## Usuario · 2026-10-31 14:14

<task-notification>
<task-id>b98gspe7n</task-id>
<tool-use-id>toolu_01KNUSjizMje2Lj1zq8Bf8bb</tool-use-id>
<output-file>~\AppData\Local\Temp\claude\C--Users-USER\50afee40-1161-4293-b4a9-85c2739871ed\tasks\b98gspe7n.output</output-file>
<status>completed</status>
<summary>Background command "Lanzar las seis corridas de evaluación en paralelo" completed (exit code 0)</summary>
</task-notification>

**Herramienta `Bash`**

```json
{
 "command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval\" && cat ~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/tasks/b98gspe7n.output; for r in 1-con 1-sin; do echo \"################ $r\"; ~/anaconda3/python.exe resumir.py runs/$r.jsonl | cut -c1-600; echo \"archivos:\"; (cd runs/$r && find salidas figuras mapas -type f; ls *.py 2>/dev/null); done",
 "description": "Resumir corridas del pedido de Cusco"
}
```

<details><summary>Resultado (error)</summary>

```text
Exit code 2
runs/1-con.err: exit=0 segundos=47
runs/1-sin.err: exit=0 segundos=22
runs/2-con.err: exit=0 segundos=20
runs/2-sin.err: exit=0 segundos=58
runs/3-con.err: exit=0 segundos=58
runs/3-sin.err: exit=0 segundos=55
runs/v1-1-con.err: exit=0 segundos=43

[exited with code 0]
################ 1-con
TOOL Skill {"skill": "limpiando-enaho", "args": "Calcular la pobreza monetaria en Cusco en 2024"}
   -> Launching skill: limpiando-enaho
TOOL Glob {"pattern": "**/*"}
   -> datos\966-Modulo02\enaho_tabla_ciuo_88.dta | datos\966-Modulo02\enaho_tabla_cno_2015.dta | datos\966-Modulo02\Criterios para codificar Ocupaciones Peligrosas.pdf | datos\966-Modulo02\FichaTecnica.pdf | datos\966-Modulo34\FichaTecnica.pdf | datos\966-Modulo02\CED-01-200-2024.pdf | datos\966-Modulo34\Sumaria-2024
TOOL Bash {"command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval/runs/1-con\" && uv run ~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval/runs/1-con/.claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024", "description": "Run ENAHO cleaning script for 2024", "timeout": 600000
   -> Using CPython 3.14.8 | Creating virtual environment at: .venv | Installed 19 packages in 1.60s | ENAHO 2024 | Filas m�dulo 200: 117,721 | Residentes habituales: 108,664 | Hogares (sumaria): 33,691 | Poblaci�n expandida: 34,482,700 | Pobreza (sumaria, factor07 x mieperho): 27.58 % | Pobreza extrema (sumaria): 5.
TOOL Read {"file_path": "~\\AppData\\Local\\Temp\\claude\\C--Users-USER\\50afee40-1161-4293-b4a9-85c2739871ed\\scratchpad\\eval\\runs\\1-con\\salidas\\validacion.txt"}
   -> 1	ENAHO 2024 | 2	Filas módulo 200: 117,721 | 3	Residentes habituales: 108,664 | 4	Hogares (sumaria): 33,691 | 5	Población expandida: 34,482,700 | 6	Pobreza (sumaria, factor07 x mieperho): 27.58 % | 7	Pobreza extrema (sumaria): 5.50 % | 8	Pobreza (personas, facpob07): 27.53 % | 9	Cifra oficial INEI: 27.6 % | 10	
TOOL Read {"file_path": "~\\AppData\\Local\\Temp\\claude\\C--Users-USER\\50afee40-1161-4293-b4a9-85c2739871ed\\scratchpad\\eval\\runs\\1-con\\.claude\\skills\\limpiando-enaho\\reference.md"}
   -> 1	# Referencia de variables · ENAHO 2024 | 2	 | 3	Códigos tomados del diccionario del INEI (`Diccionario2024.pdf`, dentro de cada zip). | 4	 | 5	## Variables de la base `salidas/personas_2024.parquet` | 6	 | 7	| Variable | Viene de | Qué es | Códigos | | 8	|---|---|---|---| | 9	| `conglome`, `vivienda`, `hogar` | a
TOOL Bash {"command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval/runs/1-con\" && uv run python -c \"\nimport pandas as pd\nd=pd.read_parquet('salidas/personas_2024.parquet')\nc=d[d.departamento=='08']\nw=c.facpob07\nprint('n',len(c),'hogares',c[['conglome','vivienda','hogar']].drop_duplicates().shape[0])\nprint('pob exp',round(w.sum()))\n
   -> n 3777 hogares 1230 | pob exp 1380357 | pobreza 18.539291 | extrema 2.1484504 | urbano False 25.00237 | urbano True 14.719553 | Shell cwd was reset to ~\AppData\Local\Temp\claude\C--Users-USER\50afee40-1161-4293-b4a9-85c2739871ed\scratchpad\eval\runs\1-con

=== RESPUESTA ===
Según la ENAHO 2024 del INEI, **la pobreza monetaria en Cusco fue de 18,5 %** de la población.

| Indicador (Cusco, 2024) | Valor |
|---|---|
| Pobreza monetaria total | **18,5 %** |
| Pobreza extrema | 2,1 % |
| Pobreza en el área urbana | 14,7 % |
| Pobreza en el área rural | 25,0 % |
| Población representada | ≈ 1,38 millones |

Cusco queda unos 9 puntos por debajo del promedio nacional, que fue 27,5 %.

**Cómo se calculó:** limpié los módulos 34 (sumaria) y 02 (miembros) de la ENAHO 2024 con el script del proyecto. Cuento como pobres a quienes tienen `pobreza <= 2` (pobres extremos más pobres no extremos) y pondero a cada persona con `facpob07`. Me quedé con los residentes de Cusco (código de ub
[... salida recortada: 6,227 caracteres]
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval\" && for r in 2-con 2-sin; do echo \"################ $r\"; ~/anaconda3/python.exe resumir.py runs/$r.jsonl | cut -c1-700; echo \"archivos:\"; (cd runs/$r && find . -path ./.venv -prune -o -newer ../../correr.sh -type f -print | grep -v \"^./.venv\"); done",
 "description": "Resumir corridas del pedido urbano/rural"
}
```

<details><summary>Resultado</summary>

```text
################ 2-con
TOOL Skill {"skill": "graficando-enaho", "args": "pobreza urbana y rural"}
   -> Launching skill: graficando-enaho
TOOL Glob {"pattern": "salidas/personas_2024.parquet"}
   -> No files found
TOOL Skill {"skill": "limpiando-enaho"}
   -> Launching skill: limpiando-enaho
TOOL Glob {"pattern": "datos/*"}
   -> datos\966-Modulo34.zip | datos\966-Modulo02.zip | datos\peru_departamental_simple.geojson
TOOL PowerShell {"command": "uv run ~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval/runs/2-con/.claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024", "description": "Limpiar módulos ENAHO 2024", "timeout": 600000}
   -> This PowerShell command contains multiple operations. The following part requires approval: uv run ~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval/runs/2-con/.claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024

=== RESPUESTA ===
Necesito tu aprobación para seguir. Para graficar la pobreza urbana y rural hace falta primero la base limpia `salidas/personas_2024.parquet`, que todavía no existe. Para crearla tengo que correr el script de limpieza de la ENAHO, y ese comando quedó sin ejecutar porque pide permiso:

ʼʼʼ
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024
ʼʼʼ

Los zip del INEI (`966-Modulo34.zip` y `966-Modulo02.zip`) ya están en `datos/`, así que no falta nada más.

Si lo apruebas, hago esto:
1. Corro la limpieza y reviso `salidas/validacion.txt`. Si la pobreza se aleja más de 0.1 puntos de la cifra oficial del INEI, me detengo y te aviso.
2. Corro `graficar.py --por area` para hacer el gráfico de barras urbana/rural, ponderado con `facpob07`, y lo guardo como PNG en `figuras/`.

¿Lo ejecuto?

costo USD: 0.20965820000000002, turnos: 8
archivos:
./.claude/skills/limpiando-enaho/SKILL.md
################ 2-sin
TOOL PowerShell {"command": "Get-ChildItem -Recurse -Force | Select-Object FullName, Length | Format-Table -AutoSize", "description": "Listar archivos del directorio de trabajo"}
   -> FullName                                                                                                                | --------                                                                                                                | ~\AppData\Local\Temp\claude\C--Users-USER\50af
TOOL Bash {"command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval/runs/2-sin\" && find . -type f | head -100", "description": "Listar archivos con rutas relativas"}
   -> ./.claude/skills/graficando-enaho/scripts/graficar.py | ./.claude/skills/graficando-enaho/SKILL.md | ./.claude/skills/limpiando-enaho/reference.md | ./.claude/skills/limpiando-enaho/scripts/limpiar.py | ./.claude/skills/limpiando-enaho/SKILL.md | ./.claude/skills/mapeando-enaho/scripts/mapear.py | ./.claude/ski
TOOL Read {"file_path": "~\\AppData\\Local\\Temp\\claude\\C--Users-USER\\50afee40-1161-4293-b4a9-85c2739871ed\\scratchpad\\eval\\runs\\2-sin\\.claude\\skills\\graficando-enaho\\SKILL.md"}
   -> 1	--- | 2	name: graficando-enaho | 3	description: Grafica la pobreza monetaria de la ENAHO del INEI por área (urbana y rural), sexo o grupo de edad, con barras ponderadas por facpob07. Úsala cuando pidan un gráfico, una figura, barras o una comparación de pobreza con la ENAHO. | 4	argument-hint: [area|sex
TOOL Read {"file_path": "~\\AppData\\Local\\Temp\\claude\\C--Users-USER\\50afee40-1161-4293-b4a9-85c2739871ed\\scratchpad\\eval\\runs\\2-sin\\.claude\\skills\\graficando-enaho\\scripts\\graficar.py"}
   -> 1	"""Grafica la pobreza monetaria de la ENAHO 2024 por área, sexo o grupo de edad. | 2	 | 3	Se corre desde la raíz del repositorio: | 4	    uv run .claude/skills/graficando-enaho/scripts/graficar.py --por area | 5	""" | 6	import argparse | 7	from pathlib i
[... salida recortada: 8,308 caracteres]
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval\" && for r in 3-con 3-sin; do echo \"################ $r\"; ~/anaconda3/python.exe resumir.py runs/$r.jsonl | cut -c1-500; echo \"archivos:\"; (cd runs/$r && find . -path ./.venv -prune -o -newer ../../correr.sh -type f -print); done",
 "description": "Resumir corridas del pedido del mapa"
}
```

<details><summary>Resultado</summary>

```text
################ 3-con
TOOL Skill {"skill": "mapeando-enaho", "args": "pobreza por departamento ENAHO 2024"}
   -> Launching skill: mapeando-enaho
TOOL Glob {"pattern": "{salidas/*,datos/*,README*,mapas/*}"}
   -> README.md | datos\966-Modulo34.zip | datos\966-Modulo02.zip | datos\peru_departamental_simple.geojson
TOOL Read {"file_path": "~\\AppData\\Local\\Temp\\claude\\C--Users-USER\\50afee40-1161-4293-b4a9-85c2739871ed\\scratchpad\\eval\\runs\\3-con\\.claude\\skills\\mapeando-enaho\\scripts\\mapear.py"}
   -> 1	"""Mapea la pobreza monetaria de la ENAHO 2024 por departamento. | 2	 | 3	Se corre desde la raíz del repositorio: | 4	    uv run .claude/skills/mapeando-enaho/scripts/mapear.py | 5	""" | 6	from pathlib import Path | 7	 | 8	import geopandas as gpd | 9	import matplotlib.pyplot as plt | 10	import pandas as pd | 11	 | 12	B
TOOL Skill {"skill": "limpiando-enaho", "args": "ENAHO 2024, módulos 34 y 02, para luego mapear pobreza por departamento"}
   -> Launching skill: limpiando-enaho
TOOL Bash {"command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval/runs/3-con\" && uv run ~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval/runs/3-con/.claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024 && cat salidas/validacion.txt", "description": "Limpia la ENAHO 2024 y m
   -> Using CPython 3.14.8 | Creating virtual environment at: .venv | Installed 19 packages in 2.43s | ENAHO 2024 | Filas m�dulo 200: 117,721 | Residentes habituales: 108,664 | Hogares (sumaria): 33,691 | Poblaci�n expandida: 34,482,700 | Pobreza (sumaria, factor07 x mieperho): 27.58 % | Pobreza extrema (sumaria): 5.
TOOL Bash {"command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval/runs/3-con\" && uv run ~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval/runs/3-con/.claude/skills/mapeando-enaho/scripts/mapear.py", "description": "Genera el mapa de pobreza por departamento", "timeout": 600000}
   -> departamento       NOMBDEP  pobreza |           06     CAJAMARCA     45.0 |           16        LORETO     42.6 |           21          PUNO     40.4 |           10       HUANUCO     39.5 |           19         PASCO     39.3 |           07        CALLAO     33.8 |           09  HUANCAVELICA     33.6 |     
TOOL Read {"file_path": "~\\AppData\\Local\\Temp\\claude\\C--Users-USER\\50afee40-1161-4293-b4a9-85c2739871ed\\scratchpad\\eval\\runs\\3-con\\mapas\\pobreza_departamento.png"}
   -> 

=== RESPUESTA ===
Hice el mapa: **`mapas/pobreza_departamento.png`**

Primero armé la base de personas de la ENAHO 2024 (módulos 34 y 02), porque todavía no existía. La pobreza nacional me salió en 27,53 %, frente al 27,6 % que publica el INEI. La diferencia es de 0,07 puntos y está dentro de la tolerancia de 0,1. Las cifras están ponderadas con `facpob07` y cuento como pobre a quien tiene `pobreza <= 2`.

El mapa tiene los 25 departamentos, todos con dato, y Lima y Callao aparecen por separado. Los departamentos se unieron por código de ubigeo, no por nombre. La escala va de un naranja claro a uno oscuro, empezando en 0, y la leyenda dice "% de personas".

**Más pobreza:**
1. Cajamarca: 45,0 %
2. Loreto: 42,6 %
3. Puno: 40,4 %

**Menos pobreza:**
1. Ica: 5,9 %
2. Moquegua: 10,9 %
3. Madre de Dios: 11,1 %

Las cifras por departamento son menos precisas que la nacional, porque cada una se calcula con menos encuestas. Diferencias de 1 o 2 puntos entre departamentos cercanos, como Huánuco (39,5 %) y Pasco (39,3 %), no son significativas. Por eso el INEI publica estos resultados en grupos de departamentos con niveles de pobreza parecidos, y no como un ranking.

costo USD: 0.28443039999999997, turnos: 10
archivos:
./.claude/skills/limpiando-enaho/SKILL.md
./mapas/pobrez
[... salida recortada: 11,627 caracteres]
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval\" && sed -i 's/\"Bash(find:\\*)\" Read/\"Bash(find:*)\" \"PowerShell(uv:*)\" Read/' correr.sh && grep PERMISOS= correr.sh && mv runs/2-con.jsonl runs/v1-2-con.jsonl && mv runs/2-con.err runs/v1-2-con.err && bash correr.sh 2 con \"Grafica la pobreza urbana y rural\"; tail -1 runs/2-con.err; ~/anaconda3/python.exe resumir.py runs/2-con.jsonl | cut -c1-400; (cd runs/2-con && find salidas figuras mapas -type f)",
 "description": "Repetir la corrida urbano/rural con PowerShell permitido",
 "timeout": 600000
}
```

<details><summary>Resultado</summary>

```text
PERMISOS=(--allowedTools "Bash(uv:*)" "Bash(python:*)" "Bash(ls:*)" "Bash(find:*)" "PowerShell(uv:*)" Read Write Edit Glob Grep Skill)
exit=0 segundos=44
TOOL Skill {"skill": "graficando-enaho", "args": "pobreza por área (urbana y rural)"}
   -> Launching skill: graficando-enaho
TOOL Glob {"pattern": "salidas/personas_2024.parquet"}
   -> No files found
TOOL Skill {"skill": "limpiando-enaho"}
   -> Launching skill: limpiando-enaho
TOOL Glob {"pattern": "datos/*"}
   -> datos\966-Modulo34.zip | datos\966-Modulo02.zip | datos\peru_departamental_simple.geojson
TOOL PowerShell {"command": "uv run ~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval/runs/2-con/.claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024", "description": "Limpiar módulos ENAHO 2024", "timeout": 600000}
   -> Using CPython 3.14.8 | Creating virtual environment at: .venv | Installed 19 packages in 1.51s | ENAHO 2024 | Filas módulo 200: 117,721 | Residentes habituales: 108,664 | Hogares (sumaria): 33,691 | Población expandida: 34,482,700 | Pobreza (sumaria, factor07 x mieperho): 27.58 % | Pobreza extrema (sumaria): 5.
TOOL Read {"file_path": "~\\AppData\\Local\\Temp\\claude\\C--Users-USER\\50afee40-1161-4293-b4a9-85c2739871ed\\scratchpad\\eval\\runs\\2-con\\salidas\\validacion.txt"}
   -> 1	ENAHO 2024 | 2	Filas módulo 200: 117,721 | 3	Residentes habituales: 108,664 | 4	Hogares (sumaria): 33,691 | 5	Población expandida: 34,482,700 | 6	Pobreza (sumaria, factor07 x mieperho): 27.58 % | 7	Pobreza extrema (sumaria): 5.50 % | 8	Pobreza (personas, facpob07): 27.53 % | 9	Cifra oficial INEI: 27.6 % | 10	
TOOL PowerShell {"command": "uv run ~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval/runs/2-con/.claude/skills/graficando-enaho/scripts/graficar.py --por area", "description": "Graficar pobreza por área urbana y rural", "timeout": 300000}
   -> area | Urbana    24.7 | Rural     39.4
TOOL Glob {"pattern": "figuras/*.png"}
   -> figuras\pobreza_area.png
TOOL Read {"file_path": "~\\AppData\\Local\\Temp\\claude\\C--Users-USER\\50afee40-1161-4293-b4a9-85c2739871ed\\scratchpad\\eval\\runs\\2-con\\figuras\\pobreza_area.png"}
   -> 

=== RESPUESTA ===
El gráfico está en `figuras/pobreza_area.png`. Según la ENAHO 2024, el 39.4 % de la población rural es pobre, frente al 24.7 % de la urbana, una diferencia de casi 15 puntos.

Antes de graficar tuve que generar la base `salidas/personas_2024.parquet` a partir de los zip de `datos/`. La pobreza nacional que resulta de esa base es 27.53 %, y la cifra oficial del INEI es 27.6 %. La diferencia es menor que la tolerancia de 0.1 puntos, así que la base es válida.

Las cifras están ponderadas por `facpob07`, el factor de expansión de personas.

costo USD: 0.23749159999999997, turnos: 12
salidas/personas_2024.parquet
salidas/validacion.txt
figuras/pobreza_area.png
Shell cwd was reset to ~\Documents\GitHub\enaho-skills
[This command modified 1 file you've previously read: ..\..\..\AppData\Local\Temp\claude\C--Users-USER\50afee40-1161-4293-b4a9-85c2739871ed\scratchpad\eval\correr.sh. Call Read before editing.]
```

</details>

**Herramienta `Edit`**

```json
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

<details><summary>Resultado</summary>

```text
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "which gh && gh auth status 2>&1 | head -5",
 "description": "Verificar si gh está instalado y autenticado"
}
```

<details><summary>Resultado (error)</summary>

```text
Exit code 1
which: no gh in (~/bin:/mingw64/bin:/usr/local/bin:/usr/bin:/bin:/mingw64/bin:/usr/bin:~/bin:/c/Program Files (x86)/Common Files/Oracle/Java/java8path:/c/Program Files (x86)/Common Files/Oracle/Java/javapath:/c/Windows/system32:/c/Windows:/c/Windows/System32/Wbem:/c/Windows/System32/WindowsPowerShell/v1.0:/c/Windows/System32/OpenSSH:/c/Program Files (x86)/NVIDIA Corporation/PhysX/Common:/cmd:/c/Program Files/Go/bin:~/.local/bin:~/AppData/Local/Programs/Python/Launcher:~/AppData/Local/Microsoft/WindowsApps:~/AppData/Local/Programs/Microsoft VS Code/bin:~/AppData/Local/GitHubDesktop/bin:/cmd:/usr/bin:/mingw64/bin:~/.opencode/bin:~/AppData/Local/Programs/Microsoft VS Code/bin/copilot-shim:~/go/bin:~/AppData/Local/Microsoft/WinGet/Packages/BrechtSanders.WinLibs.POSIX.UCRT_Microsoft.Winget.Source_8wekyb3d8bbwe/mingw64/bin:~/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-9.0.2-full_build/bin:/usr/bin/vendor_perl:/usr/bin/core_perl)
```

</details>

## Asistente · 2026-10-31 14:16

## 🔶 Revisión manual 4: corridas del Paso 4. Necesito dos decisiones antes de cerrar la tarea.

### Cómo se corrieron

Cada pedido se corrió con `claude -p` en una **copia aislada** del repositorio, sin `salidas/`, `figuras/` ni `mapas/`. Para la versión «sin skills» se usó `--disallowedTools Skill`, como indica el punto 4.1. Tu repositorio no se tocó. El costo total fue de ≈ **1.8 USD**.

### Resultados

| Pedido | Modo | Skills activadas | Cifra | ¿Ponderó? | Figura |
|---|---|---|---|---|---|
| Pobreza en Cusco 2024 | con skills | `limpiando-enaho` | **18.5%** ✅ | sí, `facpob07` | — |
| Pobreza en Cusco 2024 | sin skills | ninguna | ninguna | — | — |
| Urbana y rural | con skills | `graficando-enaho` → `limpiando-enaho` | **24.7% / 39.4%** ✅ | sí | barras ordenadas, un color |
| Urbana y rural | sin skills | ninguna (corrió los scripts a mano) | 24.7% / 39.4% | sí | la misma figura |
| Mapa por departamento | con skills | `mapeando-enaho` → `limpiando-enaho` | **Cajamarca 45.0%, Ica 5.9%** ✅ | sí | 25 departamentos, `Oranges` |
| Mapa por departamento | sin skills | ninguna (corrió los scripts a mano) | Cajamarca 45.0%, Ica 5.9% | sí | el mismo mapa |

**Lo que funcionó:** las tres corridas con skills activaron la skill correcta. Los pedidos de gráfico y mapa **encadenaron dos skills seguidas**, que es justo lo que pide mostrar la presentación.

**Tres hallazgos que debes conocer:**

1. **🐞 Se encontró y corrigió un error en `limpiando-enaho`.** En la primera corrida de Cusco, Claude activó la skill sola y le pasó como argumento «Calcular la pobreza monetaria en Cusco en 2024». En consecuencia, `$0` se reemplazó por «Calcular» y no por un año. Corregí el `SKILL.md`: ahora el año se toma de `$ARGUMENTS` si aparece un número de cuatro dígitos y, si no, se usa 2024. Repetí la corrida y salió bien. Es exactamente el ciclo del punto 4.3 («mejora y repite»), así que lo registraré en `evaluacion.md`.
2. **⚠️ El modo «sin skills» del PDF tiene una fuga.** `--disallowedTools Skill` impide *activar* las skills, pero no *leer* sus archivos. En los pedidos de gráfico y mapa, Claude encontró `.claude/skills/*/scripts/` explorando la carpeta y los corrió a mano, así que obtuvo lo mismo. En el pedido de Cusco, en cambio, intentó buscar en la web y, sin permiso, no dio cifra.
3. La primera corrida de urbano/rural se detuvo porque yo no había permitido PowerShell. Era un fallo de mi configuración de prueba, no de la skill. La repetí y salió bien.

### ❓ Decisión 1: ¿corro 3 pruebas complementarias?

Con la fuga, la comparación «con y sin» no muestra lo que la tarea quiere evidenciar: si Claude, por su cuenta, filtra residentes, pondera y une por código. **Propongo correr los 3 pedidos «sin skills» en una copia sin la carpeta `.claude/`** (≈ 1 USD más) y reportarlos en `evaluacion.md` como prueba complementaria, junto a las 6 corridas oficiales. **Recomiendo hacerlo**, porque es lo que daría contenido real a las «dos o tres frases sobre las diferencias» que pide el punto 4.2.

### ❓ Decisión 2: ¿cómo se hace la entrega en GitHub?

No tienes `gh` instalado, y la tarea del BCRP la subiste con **GitHub Desktop**. Hay dos caminos:
- **(a) recomendado:** dejo hecho el commit local, con el mensaje del PDF. Tú publicas el repositorio `enaho-skills` desde GitHub Desktop («Publish repository») y pegas el link en el issue.
- **(b)** creas el repositorio vacío en github.com y me das la URL para que yo haga `git remote add` y `git push`.

Ya escribí el `README.md` en `~\Documents\GitHub\enaho-skills\README.md`, con tu estilo de redacción, por si quieres revisarlo. `evaluacion.md` lo escribiré cuando decidas lo de las pruebas complementarias.

## Usuario · 2026-10-31 14:18

Sí, corre las 3 pruebas complementarias; opción (a) para GitHub.

## Asistente · 2026-10-31 14:18

Agrego a `correr.sh` un modo «solo», que borra `.claude/` y `README.md` de la copia: el README también describe el método y filtraría las reglas. Luego lanzo las 3 pruebas.

**Herramienta `Bash`**

```json
{
 "command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval\" && sed -i 's|^\\[ \"\\$MODO\" = \"sin\" \\] && EXTRA=(--disallowedTools Skill)|[ \"$MODO\" != \"con\" ] \\&\\& EXTRA=(--disallowedTools Skill)\\n# Modo solo: sin la carpeta de skills ni el README, que describen el método\\n[ \"$MODO\" = \"solo\" ] \\&\\& rm -rf \"$DIR/.claude\" \"$DIR/README.md\"|' correr.sh && sed -n 15,20p correr.sh && ( bash correr.sh 1 solo \"¿Cuál fue la pobreza en Cusco en 2024?\" & bash correr.sh 2 solo \"Grafica la pobreza urbana y rural\" & bash correr.sh 3 solo \"Haz un mapa de la pobreza por departamento con la ENAHO 2024\" & wait ); for r in 1 2 3; do tail -1 runs/$r-solo.err; ls runs/$r-solo -a | head -20; done",
 "description": "Correr las 3 pruebas complementarias sin carpeta de skills",
 "timeout": 600000
}
```

<details><summary>Resultado</summary>

```text
PERMISOS=(--allowedTools "Bash(uv:*)" "Bash(python:*)" "Bash(ls:*)" "Bash(find:*)" "PowerShell(uv:*)" Read Write Edit Glob Grep Skill)
EXTRA=()
[ "$MODO" != "con" ] && EXTRA=(--disallowedTools Skill)
# Modo solo: sin la carpeta de skills ni el README, que describen el método
[ "$MODO" = "solo" ] && rm -rf "$DIR/.claude" "$DIR/README.md"

exit=0 segundos=18
.
..
.gitignore
.python-version
datos
figuras
mapas
pyproject.toml
salidas
uv.lock
exit=0 segundos=85
.
..
.gitignore
.python-version
.venv
datos
figuras
mapas
pyproject.toml
salidas
scripts
uv.lock
exit=0 segundos=151
.
..
.gitignore
.python-version
.venv
datos
figuras
mapas
pyproject.toml
salidas
scripts
uv.lock
Shell cwd was reset to ~\Documents\GitHub\enaho-skills
[This command modified 1 file you've previously read: ..\..\..\AppData\Local\Temp\claude\C--Users-USER\50afee40-1161-4293-b4a9-85c2739871ed\scratchpad\eval\correr.sh. Call Read before editing.]
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval\" && for r in 1-solo 2-solo; do echo \"################ $r\"; ~/anaconda3/python.exe resumir.py runs/$r.jsonl | cut -c1-900; (cd runs/$r && find scripts salidas figuras mapas -type f 2>/dev/null); done",
 "description": "Resumir pruebas complementarias de Cusco y urbano/rural"
}
```

<details><summary>Resultado</summary>

```text
################ 1-solo
TOOL ToolSearch {"query": "select:WebSearch", "max_results": 1}
   -> 
TOOL WebSearch {"query": "pobreza monetaria Cusco 2024 INEI porcentaje", "mode": "standard"}
   -> Claude requested permissions to use WebSearch, but you haven't granted it yet.

=== RESPUESTA ===
No pude buscar en internet porque el permiso para WebSearch fue denegado, así que no tengo verificada la cifra exacta de Cusco y prefiero no darte un porcentaje que podría ser incorrecto.

Lo que recuerdo con razonable seguridad:

- **Fuente oficial:** el INEI, en su informe técnico *"Perú: Evolución de la Pobreza Monetaria 2015-2024"*, publicado en mayo de 2025 con datos de la ENAHO.
- **Contexto nacional:** la pobreza monetaria en el Perú fue de alrededor de **27,6 % en 2024**, frente a 29,0 % en 2023.
- **Cómo aparece Cusco:** el INEI suele presentar los departamentos en **grupos** con niveles de pobreza estadísticamente parecidos, según intervalos de confianza. Por eso el dato de Cusco puede aparecer como un rango y no como un único porcentaje.

**Para obtener la cifra exacta:**
1. Si me das permiso para usar WebSearch, la busco y te paso el dato con su fuente.
2. También puedes consultarla en www.inei.gob.pe, en Publicaciones → Informes Técnicos → "Evolución de la Pobreza Monetaria 2015-2024", sección de resultados por departamento.

costo USD: 0.12133680000000001, turnos: 3
################ 2-solo
TOOL Glob {"pattern": "**/*"}
   -> datos\966-Modulo02\enaho_tabla_ciuo_88.dta | datos\966-Modulo02\enaho_tabla_cno_2015.dta | datos\966-Modulo02\Criterios para codificar Ocupaciones Peligrosas.pdf | datos\966-Modulo02\FichaTecnica.pdf | datos\966-Modulo34\FichaTecnica.pdf | datos\966-Modulo02\CED-01-200-2024.pdf | datos\966-Modulo34\Sumaria-2024
TOOL Read {"file_path": "~\\AppData\\Local\\Temp\\claude\\C--Users-USER\\50afee40-1161-4293-b4a9-85c2739871ed\\scratchpad\\eval\\runs\\2-solo\\pyproject.toml"}
   -> 1	[project] | 2	name = "enaho-skills" | 3	version = "0.1.0" | 4	description = "Tres skills de Claude Code para limpiar, graficar y mapear la ENAHO 2024" | 5	readme = "README.md" | 6	authors = [ | 7	    { name = "Frank Pinares", email = "[correo oculto]" } | 8	] | 9	requires-python = ">=
TOOL Read {"file_path": "~\\AppData\\Local\\Temp\\claude\\C--Users-USER\\50afee40-1161-4293-b4a9-85c2739871ed\\scratchpad\\eval\\runs\\2-solo\\.gitignore"}
   -> 1	# Entorno | 2	.venv/ | 3	__pycache__/ | 4	 | 5	# Microdatos del INEI: pesan bastante y se descargan del portal | 6	datos/**/*.zip | 7	datos/**/*.dta | 8	datos/**/*.pdf | 9	 | 10	# Base limpia: se regenera con la skill limpiando-enaho | 11	salidas/*.parquet | 12	
TOOL PowerShell {"command": "Get-ChildItem -Force -Recurse -Depth 3 -Exclude .venv | Where-Object { $_.FullName -notmatch '\\\\.venv\\\\' -and $_.FullName -notmatch '\\\\datos\\\\' } | Select-Object FullName; uv --version", "description": "List hidden files and check uv"}
   -> Command contains a UNC path that could trigger network requests
TOOL Bash {"command": "ls -la; ls -la .claude 2>/dev/null; ls salidas 2>/dev/null; uv --version", "description": "List hidden files and check uv"}
   -> total 159 | drwxr-xr-x 1 USER 197121      0 Oct 31 09:18 . | drwxr-xr-x 1 USER 197121      0 Oct 31 09:18 .. | -rw-r--r-- 1 USER 197121    215 Oct 31 09:03 .gitignore | -rw-r--r-- 1 USER 197121      5 Oct 31 08:47 .python-version | drwxr-xr-x 1 USER 197121      0 Oct 31 08:48 datos | drwxr-xr-x 1 USER 197121   
TOOL Bash {"command": "mkdir -p scripts && cat > scripts/inspeccionar.py <<'EOF'\nimport sys, pandas as pd\nruta = sys.argv[1]\nit = pd.read_stata(ruta, iterator=True)\nlab = it.variable_labels()\nfor v in [\"conglome\",\"vivienda\",\"hogar\",\"ubigeo\",\"dominio\",\"estrato\",\"pobreza\",\"factor07\",\"mieperho\",\"linea\",\"linpe\",\"gashog2d\"]:\n    print(v, \"->\", lab.get(v))\ndf = pd.read_stata(ruta,
   -> Parser skipped input between top-level state
[... salida recortada: 8,796 caracteres]
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval\" && ~/anaconda3/python.exe resumir.py runs/3-solo.jsonl | cut -c1-700; (cd runs/3-solo && find scripts salidas figuras mapas -type f); grep -n -iE \"merge|cmap|NOMBDEP|FIRST_IDDP|zfill|weights|factor|mieperho|facpob\" runs/3-solo/scripts/*.py | head -30",
 "description": "Resumir la prueba complementaria del mapa"
}
```

<details><summary>Resultado</summary>

```text
TOOL Bash {"command": "ls -la; which python py R Rscript 2>/dev/null; python --version 2>&1; python -c \"import pandas, geopandas, matplotlib, pyreadstat; print('ok')\" 2>&1", "description": "Revisar directorio y herramientas"}
   -> Exit code 49 | total 159 | drwxr-xr-x 1 USER 197121      0 Oct 31 09:18 . | drwxr-xr-x 1 USER 197121      0 Oct 31 09:18 .. | -rw-r--r-- 1 USER 197121    215 Oct 31 09:03 .gitignore | -rw-r--r-- 1 USER 197121      5 Oct 31 08:47 .python-version | drwxr-xr-x 1 USER 197121      0 Oct 31 08:48 datos | drwxr-xr-x 1 U
TOOL Bash {"command": "cat pyproject.toml .python-version .gitignore; echo ---; find datos figuras mapas salidas -maxdepth 3 | head -100; which uv; uv --version", "description": "Ver configuración del proyecto y datos"}
   -> [project] | name = "enaho-skills" | version = "0.1.0" | description = "Tres skills de Claude Code para limpiar, graficar y mapear la ENAHO 2024" | readme = "README.md" | authors = [ |     { name = "Frank Pinares", email = "[correo oculto]" } | ] | requires-python = ">=3.14" | dependencies
TOOL Bash {"command": "ls -a ~/.claude/skills 2>/dev/null; ls -a .claude 2>/dev/null; cat > /tmp/explora.py <<'EOF'\nimport sys, pandas as pd, geopandas as gpd\nd = sys.argv[1]\ns = pd.read_stata(f\"{d}/966-Modulo34/sumaria-2024.dta\", convert_categoricals=False)\nprint(s.shape); print([c for c in s.columns][:40])\nfor c in [\"pobreza\",\"ubigeo\",\"factor07\",\"mieperho\",\"dominio\",\"estrato\"]:\n    pri
   -> This Bash command contains multiple operations. The following parts require approval: ls -a ~/.claude/skills, cat
TOOL Glob {"pattern": "**/SKILL.md", "path": "~\\.claude\\skills"}
   -> ~\.claude\skills\synced\029ba692-2ed6-41d3-baab-8ce264390007_0312b454-ab84-40ef-a025-72b7e0b403cb\import-memory\SKILL.md | ~\.claude\skills\synced\029ba692-2ed6-41d3-baab-8ce264390007_0312b454-ab84-40ef-a025-72b7e0b403cb\morning\SKILL.md | ~\.claude\skills\synced\029b
TOOL Bash {"command": "mkdir -p \"$TEMP/enaho_scripts\"; echo \"$TEMP/enaho_scripts\"", "description": "Crear carpeta para scripts"}
   -> A variable in this command can't be checked before it runs
TOOL Write {"file_path": "~\\AppData\\Local\\Temp\\claude\\C--Users-USER\\50afee40-1161-4293-b4a9-85c2739871ed\\scratchpad\\eval\\runs\\3-solo\\scripts\\explora.py", "content": "import sys\n\nimport geopandas as gpd\nimport pandas as pd\n\nd = sys.argv[1]\ns = pd.read_stata(f\"{d}/966-Modulo34/sumaria-2024.dta\", convert_categoricals=False)\nprint(s.shape)\nprint(list(s.columns))\nfor c in [\"p
   -> File created successfully at: ~\AppData\Local\Temp\claude\C--Users-USER\50afee40-1161-4293-b4a9-85c2739871ed\scratchpad\eval\runs\3-solo\scripts\explora.py (file state is current in your context — no need to Read it back)
TOOL Bash {"command": "uv run python -I scripts/explora.py datos", "description": "Explorar Sumaria 2024 y GeoJSON", "timeout": 600000}
   -> Using CPython 3.14.8 | Creating virtual environment at: .venv | Installed 19 packages in 1.64s | (33691, 163) | ['a�o', 'mes', 'conglome', 'vivienda', 'hogar', 'ubigeo', 'dominio', 'estrato', 'mieperho', 'totmieho', 'percepho', 'ia01hd', 'ia02hd', 'ig03hd1', 'ig03hd2', 'ig03hd3', 'ig03hd4', 'ga03hd', 'ga04
TOOL Write {"file_path": "~\\AppData\\Local\\Temp\\claude\\C--Users-USER\\50afee40-1161-4293-b4a9-85c2739871ed\\scratchpad\\eval\\runs\\3-solo\\scripts\\mapa_pobreza.py", "content": "\"\"\"Mapa de pobreza monetaria por departamento - ENAHO 2024 (Sumaria, módulo 34).\n\nUso:\n    uv run python -I scripts/mapa_pobreza.py datos\n\n- Pobreza total = pobre extremo (1) + pobre no extremo (2) de la va
   -> File created successfully at: ~\AppData\Local\Temp\claude\C--Users-USER\50afee40-1161-4293-b4a9-85c2739871ed\scratchpad\eval\runs\3-solo\scripts\mapa_pobreza.py (file state is current in your context — no need to Read it back)
TOOL Bash
[... salida recortada: 14,259 caracteres]
```

</details>

**Herramienta `Read`**

```json
{
 "file_path": "~\\AppData\\Local\\Temp\\claude\\C--Users-USER\\50afee40-1161-4293-b4a9-85c2739871ed\\scratchpad\\eval\\runs\\2-solo\\figuras\\pobreza_urbana_rural.png"
}
```

<details><summary>Resultado</summary>

```text
[imagen]
```

</details>

**Herramienta `Read`**

```json
{
 "file_path": "~\\AppData\\Local\\Temp\\claude\\C--Users-USER\\50afee40-1161-4293-b4a9-85c2739871ed\\scratchpad\\eval\\runs\\3-solo\\mapas\\mapa_pobreza_departamental_2024.png"
}
```

<details><summary>Resultado</summary>

```text
[imagen]
```

</details>

## Usuario · 2026-10-31 14:21

[Image: original 1386x2102, displayed at 1319x2000. Multiply coordinates by 1.05 to map to original image.]

**Herramienta `Write`**

```json
{
 "file_path": "~\\Documents\\GitHub\\enaho-skills\\evaluacion.md",
 "content": "# Evaluación de las skills: tres pedidos con y sin skills\n\n## Cómo se corrió\n\nCada pedido se corrió en modo no interactivo (`claude -p`, Claude Code 2.1.316, 31 de octubre de 2026) dentro de una copia del repositorio en la que se borraron `salidas/`, `figuras/` y `mapas/`, de modo que la base limpia no existía al empezar y debía verse si las skills de gráficos y mapas llamaban primero a `limpiando-enaho`. Para la versión sin skills se bloqueó la herramienta Skill, tal como indica la tarea:\n\nʼʼʼbash\nclaude -p \"Haz un mapa de la pobreza por departamento con la ENAHO 2024\"                          # con skills\nclaude -p --disallowedTools Skill \"Haz un mapa de la pobreza por departamento con la ENAHO 2024\"  # sin skills\nʼʼʼ\n\nEn todas las corridas se permitieron las mismas herramientas (`uv`, `python`, lectura y escritura de archivos); la búsqueda web no se permitió.\n\n## Resultados: seis corridas\n\n| Pedido | Modo | Skills activadas | Cifra | ¿Ponderó? | Figura |\n| --- | --- | --- | --- | --- | --- |\n| ¿Cuál fue la pobreza en Cusco en 2024? | con skills | `limpiando-enaho` | 18.5 % | sí, `facpob07` | — |\n| ¿Cuál fue la pobreza en Cusco en 2024? | sin skills | ninguna | sin cifra | — | — |\n| Grafica la pobreza urbana y rural | con skills | `graficando-enaho` → `limpiando-enaho` | 24.7 / 39.4 % | sí, `facpob07` | barras horizontales desde cero, ordenadas, un color, valor en cada barra, nota de fuente |\n| Grafica la pobreza urbana y rural | sin skills | ninguna (corrió los scripts de `.claude/skills/` a mano) | 24.7 / 39.4 % | sí, `facpob07` | la misma figura |\n| Haz un mapa de la pobreza por departamento | con skills | `mapeando-enaho` → `limpiando-enaho` | Cajamarca 45.0 %, Ica 5.9 % | sí, `facpob07` | 25 departamentos con dato, `Oranges` desde 0, leyenda en % de personas |\n| Haz un mapa de la pobreza por departamento | sin skills | ninguna (corrió los scripts de `.claude/skills/` a mano) | Cajamarca 45.0 %, Ica 5.9 % | sí, `facpob07` | el mismo mapa |\n\nLas tres corridas con skills activaron la skill correcta, y los pedidos de gráfico y de mapa encadenaron dos skills seguidas: al no encontrar `salidas/personas_2024.parquet`, Claude activó `limpiando-enaho`, verificó `validacion.txt` (27.53 % frente al 27.6 % oficial) y recién después graficó o mapeó.\n\nLas cifras de los gráficos y del mapa se calculan sobre la base de personas con `facpob07`, por lo que difieren en una décima de las referencias de la clase, calculadas con la sumaria y `factor07 × mieperho` (24.8 / 39.3 % en el área; Ica 6.0 %). Ambos factores coinciden fila por fila; la diferencia proviene de que en 1,846 hogares el número de residentes habituales no coincide con `mieperho`.\n\n## Correcciones hechas durante la evaluación\n\nEn la primera corrida del pedido de Cusco, Claude activó `limpiando-enaho` por su cuenta y le pasó como argumento la frase «Calcular la pobreza monetaria en Cusco en 2024», de modo que `$0` se reemplazó por «Calcular» y no por un año; Claude lo advirtió y corrió el script con `--anio 2024`, pero la instrucción era frágil. Siguiendo el punto 4.3 de la tarea, se corrigió el `SKILL.md` para que el año se tome de `$ARGUMENTS` solo si aparece un número de cuatro dígitos y, en otro caso, se use 2024; la corrida repetida, que es la que figura en la tabla, ya no presentó el problema. Asimismo, la primera corrida del gráfico se detuvo porque Claude usó PowerShell, que no estaba entre las herramientas permitidas de la prueba; se trató de un problema de configuración de la prueba y no de la skill, por lo que se repitió con ese permiso.\n\n## Prueba complementaria: sin skills y sin la carpeta `.claude/`\n\nLa comparación anterior tiene una fuga: `--disallowedTools Skill` impide activar las skills, pero no leer sus archivos, y en los pedidos de gráfico y de mapa Claude encontró los scripts en `.claude/skills/` y los ejecutó a mano. Por 
[... salida recortada: 6,363 caracteres]
```

<details><summary>Resultado</summary>

```text
File created successfully at: ~\Documents\GitHub\enaho-skills\evaluacion.md (file state is current in your context — no need to Read it back)
```

</details>

## Asistente · 2026-10-31 14:22

Antes del commit, regenero todas las salidas con las versiones finales de los scripts para asegurar que el repositorio sea coherente.

**Herramienta `Bash`**

```json
{
 "command": "export PYTHONIOENCODING=utf-8 && uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024 >/dev/null && for p in area sexo edad; do uv run .claude/skills/graficando-enaho/scripts/graficar.py --por $p >/dev/null; done && uv run .claude/skills/mapeando-enaho/scripts/mapear.py | head -4 && cat salidas/validacion.txt && git config user.name; git config user.email; git add -A && git status --short",
 "description": "Regenerar salidas y preparar el commit",
 "timeout": 300000
}
```

<details><summary>Resultado</summary>

```text
departamento       NOMBDEP  pobreza
          06     CAJAMARCA     45.0
          16        LORETO     42.6
          21          PUNO     40.4
ENAHO 2024
Filas módulo 200: 117,721
Residentes habituales: 108,664
Hogares (sumaria): 33,691
Población expandida: 34,482,700
Pobreza (sumaria, factor07 x mieperho): 27.58 %
Pobreza extrema (sumaria): 5.50 %
Pobreza (personas, facpob07): 27.53 %
Cifra oficial INEI: 27.6 %
Frank Pinares
[correo oculto]
warning: in the working copy of '.claude/skills/graficando-enaho/SKILL.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.claude/skills/graficando-enaho/scripts/graficar.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.claude/skills/limpiando-enaho/SKILL.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.claude/skills/limpiando-enaho/reference.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.claude/skills/limpiando-enaho/scripts/limpiar.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.claude/skills/mapeando-enaho/SKILL.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.claude/skills/mapeando-enaho/scripts/mapear.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.gitignore', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.python-version', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'datos/peru_departamental_simple.geojson', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'evaluacion.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'pyproject.toml', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'uv.lock', LF will be replaced by CRLF the next time Git touches it
A  .claude/skills/graficando-enaho/SKILL.md
A  .claude/skills/graficando-enaho/scripts/graficar.py
A  .claude/skills/limpiando-enaho/SKILL.md
A  .claude/skills/limpiando-enaho/reference.md
A  .claude/skills/limpiando-enaho/scripts/limpiar.py
A  .claude/skills/mapeando-enaho/SKILL.md
A  .claude/skills/mapeando-enaho/scripts/mapear.py
A  .gitignore
A  .python-version
A  README.md
A  datos/peru_departamental_simple.geojson
A  evaluacion.md
A  figuras/pobreza_area.png
A  figuras/pobreza_edad.png
A  figuras/pobreza_sexo.png
A  mapas/pobreza_departamento.png
A  pyproject.toml
A  salidas/validacion.txt
A  uv.lock
```

</details>

## Asistente · 2026-10-31 14:22

Solo quedan en el área de preparación los archivos de la entrega: ni microdatos ni `.parquet`. Hago el commit local.

**Herramienta `Bash`**

```json
{
 "command": "git commit -q -F - <<'EOF'\nSkills para limpiar, graficar y mapear la ENAHO 2024\n\nCo-Authored-By: Claude Opus 5.5 <[correo oculto]>\nEOF\ngit log --stat --oneline | head -25; git status --short | head",
 "description": "Crear el commit local de la entrega"
}
```

<details><summary>Resultado</summary>

```text
88b674a Skills para limpiar, graficar y mapear la ENAHO 2024
 .claude/skills/graficando-enaho/SKILL.md           |  12 +
 .../skills/graficando-enaho/scripts/graficar.py    |  45 ++
 .claude/skills/limpiando-enaho/SKILL.md            |  13 +
 .claude/skills/limpiando-enaho/reference.md        |  51 ++
 .claude/skills/limpiando-enaho/scripts/limpiar.py  | 109 ++++
 .claude/skills/mapeando-enaho/SKILL.md             |  11 +
 .claude/skills/mapeando-enaho/scripts/mapear.py    |  48 ++
 .gitignore                                         |  11 +
 .python-version                                    |   1 +
 README.md                                          |  98 ++++
 datos/peru_departamental_simple.geojson            |  25 +
 evaluacion.md                                      |  49 ++
 figuras/pobreza_area.png                           | Bin 0 -> 34966 bytes
 figuras/pobreza_edad.png                           | Bin 0 -> 49027 bytes
 figuras/pobreza_sexo.png                           | Bin 0 -> 35763 bytes
 mapas/pobreza_departamento.png                     | Bin 0 -> 163288 bytes
 pyproject.toml                                     |  15 +
 salidas/validacion.txt                             |   9 +
 uv.lock                                            | 635 +++++++++++++++++++++
 19 files changed, 1132 insertions(+)
```

</details>

**Herramienta `Edit`**

```json
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

<details><summary>Resultado</summary>

```text
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

</details>

**Herramienta `Bash`**

```json
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

<details><summary>Resultado</summary>

```text
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

</details>

## Asistente · 2026-10-31 14:23

## 🔶 Revisión manual 5 (final): la tarea está lista para que la revises y la publiques.

### Resultado de las 3 pruebas complementarias (sin skills y sin carpeta `.claude/`)

| Pedido | Cifra | Método | Figura | Turnos / costo |
|---|---|---|---|---|
| Cusco 2024 | **sin cifra**: intentó buscar en la web y no miró los datos | — | — | 3 / 0.12 USD |
| Urbana y rural | 24.8% / 39.3% | sumaria, `factor07 × mieperho` | barras **apiladas en dos colores, sin ordenar** | 13 / 0.33 USD |
| Mapa | Cajamarca 45.0%, Ica 6.0% | sumaria, unió **por código** | **clases de 10 puntos** en rojos, nombre de archivo propio | 26 / 0.65 USD |

Hubo un hallazgo inesperado que conviene comentar en la presentación: **Claude solo no cometió los errores clásicos**. Ponderó bien y unió por código. Lo que no hizo fue construir ni validar la base de personas, y tampoco respetó ninguna regla fija: cada corrida inventó sus scripts, nombres y estilos, y el mapa le costó más del doble. Además, ante la pregunta más simple (Cusco) no dio respuesta. Así lo concluye `evaluacion.md`: el valor de las skills está en la **reproducibilidad**, más que en evitar un error de cálculo. El costo total de todas las corridas fue de ≈ **2.9 USD**.

### Estado de la entrega (checklist de la pág. 15)

| Criterio | Puntos | Estado |
|---|---|---|
| Limpieza: valida 27.6% y 108,664 personas | 6 | ✅ `validacion.txt` con 27.58% / 5.50% / 108,664 |
| `graficando-enaho` con sus reglas | 4 | ✅ 3 figuras (área, sexo, edad) |
| `mapeando-enaho`: une por código, 25 con dato | 4 | ✅ con `assert` de 25 departamentos, Lima y Callao |
| Tres pedidos con y sin skills | 4 | ✅ 6 corridas, más 3 complementarias y la corrección del error del año |
| README | 2 | ✅ instalación, descarga, uso, validación y mapa embebido |

Ya está hecho el **commit local** `88b674a` («Skills para limpiar, graficar y mapear la ENAHO 2024», 19 archivos). No incluye microdatos ni el `.parquet`. El mensaje termina con la línea `Co-Authored-By: Claude`, que es la atribución estándar de los commits que hago; si prefieres quitarla, puedo rehacer el commit antes de que publiques.

### Lo que te toca hacer (opción a)

1. **Revisa** `README.md` y `evaluacion.md` en `~\Documents\GitHub\enaho-skills\`. Ambos están redactados con tu estilo.
2. En **GitHub Desktop**: *File → Add local repository…* → elige esa carpeta → **Publish repository**. Desmarca «Keep this code private» si el issue requiere que el repositorio sea público.
3. **Pega el link** del repositorio en el issue de la sesión antes del sorteo.

**Para la presentación (3 minutos):**
- muestra `mapas/pobreza_departamento.png` y `figuras/pobreza_area.png`;
- muestra `salidas/validacion.txt`;
- como pedido que activó dos skills seguidas, usa «Haz un mapa de la pobreza por departamento»: activó `mapeando-enaho` y luego `limpiando-enaho`.

¿Quieres que ajuste algo del README o de la evaluación antes de que publiques, o que rehaga el commit sin la línea de coautoría?

## Usuario · 2026-10-31 14:29

Sí, prefiero que quites la línea de "Co-Authored-By: Claude", así como otras referencias a Claude. Asimismo, recuerda que el estilo de redacción de las partes de texto debe ser lo más similar posible a mi estilo personal.

**Herramienta `Bash`**

```json
{
 "command": "cd ~/Documents/GitHub/enaho-skills && grep -rn -i \"claude\\|anthropic\" --exclude-dir=.venv --exclude-dir=.git --exclude-dir=datos . | grep -v \"^./uv.lock\" | cut -c1-220; git log -1 --format=%B",
 "description": "Buscar referencias a Claude en el repositorio"
}
```

<details><summary>Resultado</summary>

```text
./.claude/skills/graficando-enaho/scripts/graficar.py:4:    uv run .claude/skills/graficando-enaho/scripts/graficar.py --por area
./.claude/skills/graficando-enaho/SKILL.md:8:2. Desde la raíz del repositorio, corre: uv run ${CLAUDE_SKILL_DIR}/scripts/graficar.py --por <area|sexo|edad>
./.claude/skills/limpiando-enaho/scripts/limpiar.py:4:    uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024
./.claude/skills/limpiando-enaho/SKILL.md:10:2. Desde la raíz del repositorio, corre exactamente: uv run ${CLAUDE_SKILL_DIR}/scripts/limpiar.py --anio <año>
./.claude/skills/mapeando-enaho/scripts/mapear.py:4:    uv run .claude/skills/mapeando-enaho/scripts/mapear.py
./.claude/skills/mapeando-enaho/SKILL.md:8:3. Desde la raíz del repositorio, corre: uv run ${CLAUDE_SKILL_DIR}/scripts/mapear.py
./evaluacion.md:5:Cada pedido se corrió en modo no interactivo (`claude -p`, Claude Code 2.1.316, 31 de octubre de 2026) dentro de una copia del repositorio en la que se borraron `salidas/`, `figuras/` y `mapas/`, de mo
./evaluacion.md:8:claude -p "Haz un mapa de la pobreza por departamento con la ENAHO 2024"                          # con skills
./evaluacion.md:9:claude -p --disallowedTools Skill "Haz un mapa de la pobreza por departamento con la ENAHO 2024"  # sin skills
./evaluacion.md:21:| Grafica la pobreza urbana y rural | sin skills | ninguna (corrió los scripts de `.claude/skills/` a mano) | 24.7 / 39.4 % | sí, `facpob07` | la misma figura |
./evaluacion.md:23:| Haz un mapa de la pobreza por departamento | sin skills | ninguna (corrió los scripts de `.claude/skills/` a mano) | Cajamarca 45.0 %, Ica 5.9 % | sí, `facpob07` | el mismo mapa |
./evaluacion.md:25:Las tres corridas con skills activaron la skill correcta, y los pedidos de gráfico y de mapa encadenaron dos skills seguidas: al no encontrar `salidas/personas_2024.parquet`, Claude activó `limpiando
./evaluacion.md:31:En la primera corrida del pedido de Cusco, Claude activó `limpiando-enaho` por su cuenta y le pasó como argumento la frase «Calcular la pobreza monetaria en Cusco en 2024», de modo que `$0` se reem
./evaluacion.md:33:## Prueba complementaria: sin skills y sin la carpeta `.claude/`
./evaluacion.md:35:La comparación anterior tiene una fuga: `--disallowedTools Skill` impide activar las skills, pero no leer sus archivos, y en los pedidos de gráfico y de mapa Claude encontró los scripts en `.claude/
./evaluacion.md:47:Una primera conclusión es que, contra lo que se esperaba, Claude sin skills no cometió los errores típicos que motivan la tarea: en los pedidos de gráfico y de mapa ponderó a las personas con `fac
./evaluacion.md:49:Ahora bien, la diferencia más clara se dio en la pregunta más simple: sin skills, Claude ni siquiera revisó los datos disponibles y, al no poder buscar en la web, se negó a dar la pobreza de Cusco,
./pyproject.toml:4:description = "Tres skills de Claude Code para limpiar, graficar y mapear la ENAHO 2024"
./README.md:1:# Skills de Claude Code para limpiar, graficar y mapear la ENAHO 2024
./README.md:3:El presente repositorio contiene tres *skills* de Claude Code que convierten los microdatos de la Encuesta Nacional de Hogares (ENAHO) 2024 del INEI en una base de personas lista para analizar, y que a part
./README.md:5:Y es que, si se le pide dos veces a Claude que limpie la ENAHO sin reglas fijas, puede devolver dos bases distintas: una vez deja a todos los miembros y otra solo a los residentes habituales, una vez ponder
./README.md:11:| [`limpiando-enaho`](.claude/skills/limpiando-enaho/SKILL.md) | Los módulos 34 (sumaria) y 02 (miembros) del INEI | `salidas/personas_2024.parquet` y `salidas/validacion.txt` |
./README.md:12:| [`graficando-enaho`](.claude/skills/graficando-enaho/SKILL.md) | La base limpia y un corte: área, sexo o edad | `figuras/pobreza_<corte>.png` |
./README.md:13:| [`mapeando-enaho`](.claude/skills/mapeando-enaho/SKILL.md) | La base limpia y los límites de los 25 departamentos | `mapas/pobreza_departamento.png` |
./RE
[... salida recortada: 4,939 caracteres]
```

</details>

**Herramienta `Write`**

```json
{
 "file_path": "~\\Documents\\GitHub\\enaho-skills\\README.md",
 "content": "# Skills para limpiar, graficar y mapear la ENAHO 2024\n\nEl presente repositorio reúne tres *skills* de Claude Code que convierten los microdatos de la Encuesta Nacional de Hogares (ENAHO) 2024 del INEI en una base de personas lista para analizar y que, a partir de ella, grafican y mapean la pobreza monetaria. Se trata de la tarea de la Clase 8 del curso Python Intermedio para CCSS y Gestión Pública, de la Diplomatura de Especialización en Ciencia de Datos (Q-LAB PUCP).\n\nAhora bien, debe tenerse en cuenta el problema que motiva la tarea. Y es que, si se le pide dos veces a un agente que limpie la ENAHO sin reglas fijas, este puede devolver dos bases distintas: una vez conserva a todos los miembros del hogar y otra solo a los residentes habituales, una vez pondera con el factor de expansión y otra cuenta encuestas, una vez lee el `ubigeo` como texto y otra como número, perdiendo así los ceros a la izquierda. Cada una de dichas respuestas parece razonable por separado; sin embargo, juntas producen cifras de pobreza que no cuadran. En ese sentido, las skills fijan esas decisiones una sola vez, en scripts versionados, de modo que quien clone el repositorio obtenga siempre la misma base, los mismos gráficos y el mismo mapa.\n\n## Las tres skills\n\n| Skill | Entra | Sale |\n|---|---|---|\n| [`limpiando-enaho`](.claude/skills/limpiando-enaho/SKILL.md) | Los módulos 34 (sumaria) y 02 (miembros) del INEI | `salidas/personas_2024.parquet` y `salidas/validacion.txt` |\n| [`graficando-enaho`](.claude/skills/graficando-enaho/SKILL.md) | La base limpia y un corte: área, sexo o edad | `figuras/pobreza_<corte>.png` |\n| [`mapeando-enaho`](.claude/skills/mapeando-enaho/SKILL.md) | La base limpia y los límites de los 25 departamentos | `mapas/pobreza_departamento.png` |\n\nLas skills de gráficos y de mapas indican que, si no existe `salidas/personas_2024.parquet`, se use primero `limpiando-enaho`, de modo que un solo pedido activa dos skills seguidas. La estructura del repositorio es la siguiente:\n\nʼʼʼtext\n.claude/skills/\n  limpiando-enaho/   SKILL.md · reference.md · scripts/limpiar.py\n  graficando-enaho/  SKILL.md · scripts/graficar.py\n  mapeando-enaho/    SKILL.md · scripts/mapear.py\nsalidas/validacion.txt\nfiguras/  mapas/\nevaluacion.md  README.md  pyproject.toml\nʼʼʼ\n\n## Requisitos e instalación\n\nPara usar el repositorio se requieren [uv](https://docs.astral.sh/uv/) y [Claude Code](https://code.claude.com/docs). Luego de clonarlo, basta con instalar las dependencias desde su raíz:\n\nʼʼʼbash\nuv sync\nʼʼʼ\n\n## Descarga de datos\n\nDebe considerarse que los microdatos no se suben al repositorio (ver `.gitignore`), por lo que deben descargarse en la carpeta `datos/`. El código `966` corresponde a la ENAHO 2024 en el portal de microdatos del INEI, y cada zip trae, además, el diccionario de variables en PDF.\n\nʼʼʼbash\ncd datos\ncurl -LO https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo34.zip\ncurl -LO https://proyectos.inei.gob.pe/iinei/srienaho/descarga/STATA/966-Modulo02.zip\nunzip -o 966-Modulo34.zip && unzip -o 966-Modulo02.zip\ncd ..\nʼʼʼ\n\nSi `curl` falla por el certificado del INEI, los zip pueden descargarse desde el navegador y moverse luego a `datos/`. Por otra parte, el GeoJSON departamental (`datos/peru_departamental_simple.geojson`) sí se incluye en el repositorio, siendo su fuente el [repositorio del curso](https://raw.githubusercontent.com/d2cml-ai/Data-Science-Python/main/sessions/06-geoespacial/lab/Data/peru_departamental_simple.geojson).\n\n## Cómo usarlo\n\nDentro de Claude Code, y desde la raíz del repositorio, basta con formular el pedido en lenguaje natural. Así, la pregunta «¿Cuál fue la pobreza en Cusco en 2024?» activa `limpiando-enaho`; el pedido «Grafica la pobreza urbana y rural» activa `graficando-enaho` (y antes `limpiando-enaho`, si falta la base); y el pedido «Haz un mapa de la pob
[... salida recortada: 7,361 caracteres]
```

**Herramienta `Write`**

```json
{
 "file_path": "~\\Documents\\GitHub\\enaho-skills\\evaluacion.md",
 "content": "# Evaluación de las skills: tres pedidos con y sin skills\n\n## Procedimiento\n\nCada pedido se corrió en modo no interactivo (`claude -p`, versión 2.1.316, el 31 de octubre de 2026) dentro de una copia del repositorio en la que se borraron previamente `salidas/`, `figuras/` y `mapas/`. De esta forma, la base limpia no existía al iniciar cada corrida, lo que permitió observar si las skills de gráficos y de mapas llamaban primero a `limpiando-enaho`. Para la versión sin skills se bloqueó la herramienta Skill, siguiendo lo indicado en la tarea:\n\nʼʼʼbash\nclaude -p \"Haz un mapa de la pobreza por departamento con la ENAHO 2024\"                          # con skills\nclaude -p --disallowedTools Skill \"Haz un mapa de la pobreza por departamento con la ENAHO 2024\"  # sin skills\nʼʼʼ\n\nDebe precisarse, asimismo, que en todas las corridas se permitieron las mismas herramientas (`uv`, `python`, lectura y escritura de archivos), mientras que la búsqueda web no se permitió en ninguna.\n\n## Resultados de las seis corridas\n\n| Pedido | Modo | Skills activadas | Cifra | ¿Ponderó? | Figura |\n| --- | --- | --- | --- | --- | --- |\n| ¿Cuál fue la pobreza en Cusco en 2024? | con skills | `limpiando-enaho` | 18.5% | sí, `facpob07` | — |\n| ¿Cuál fue la pobreza en Cusco en 2024? | sin skills | ninguna | sin cifra | — | — |\n| Grafica la pobreza urbana y rural | con skills | `graficando-enaho` → `limpiando-enaho` | 24.7% / 39.4% | sí, `facpob07` | barras horizontales desde cero, ordenadas, de un solo color, con el valor en cada barra y la nota de fuente |\n| Grafica la pobreza urbana y rural | sin skills | ninguna (ejecutó a mano los scripts de `.claude/skills/`) | 24.7% / 39.4% | sí, `facpob07` | la misma figura |\n| Haz un mapa de la pobreza por departamento | con skills | `mapeando-enaho` → `limpiando-enaho` | Cajamarca 45.0%, Ica 5.9% | sí, `facpob07` | 25 departamentos con dato, escala `Oranges` desde 0 y leyenda en % de personas |\n| Haz un mapa de la pobreza por departamento | sin skills | ninguna (ejecutó a mano los scripts de `.claude/skills/`) | Cajamarca 45.0%, Ica 5.9% | sí, `facpob07` | el mismo mapa |\n\nLas tres corridas con skills activaron la skill correspondiente y, además, los pedidos de gráfico y de mapa encadenaron dos skills seguidas. Es decir, al no encontrar `salidas/personas_2024.parquet`, el agente activó `limpiando-enaho`, verificó `validacion.txt` (27.53% frente al 27.6% oficial) y, solo después, graficó o mapeó.\n\nAhora bien, las cifras de los gráficos y del mapa se calculan sobre la base de personas con `facpob07`, por lo que difieren en una décima de las referencias de la clase, calculadas con la sumaria y `factor07 × mieperho` (24.8% y 39.3% por área; 6.0% en Ica). Si bien ambos factores coinciden fila por fila, la diferencia se explica porque en 1,846 hogares el número de residentes habituales no coincide con `mieperho`.\n\n## Correcciones realizadas durante la evaluación\n\nEn la primera corrida del pedido de Cusco, el agente activó `limpiando-enaho` por su cuenta y le pasó como argumento la frase «Calcular la pobreza monetaria en Cusco en 2024», de modo que `$0` se reemplazó por «Calcular» y no por un año. Si bien el agente advirtió el problema y corrió el script con `--anio 2024`, la instrucción resultaba frágil. Siguiendo el punto 4.3 de la tarea, se corrigió el `SKILL.md` para que el año se tome de `$ARGUMENTS` solo cuando aparece un número de cuatro dígitos y, en caso contrario, se use 2024; así, la corrida repetida, que es la que figura en la tabla, ya no presentó el problema. Por otra parte, la primera corrida del gráfico se detuvo porque el agente recurrió a PowerShell, que no figuraba entre las herramientas permitidas de la prueba; al tratarse de un problema de configuración de la prueba y no de la skill, dicha corrida se repitió con ese permiso.\n\n## Prueba complementaria: sin skills y sin la carpet
[... salida recortada: 6,809 caracteres]
```

<details><summary>Resultado</summary>

```text
The file ~\Documents\GitHub\enaho-skills\README.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>Resultado</summary>

```text
The file ~\Documents\GitHub\enaho-skills\evaluacion.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## Asistente · 2026-10-31 14:30

Ajusto también el formato de porcentajes en `reference.md`. Después rehago el commit local sin la línea de coautoría; como el commit aún no se ha publicado, enmendarlo no afecta a nadie.

**Herramienta `Bash`**

```json
{
 "command": "sed -i 's/(27.58 % frente a 27.53 % en 2024)/(27.58% frente a 27.53% en 2024)/' .claude/skills/limpiando-enaho/reference.md && grep -n \"27.58\" .claude/skills/limpiando-enaho/reference.md && git add -A && git commit -q --amend -m \"Skills para limpiar, graficar y mapear la ENAHO 2024\" && git log -1 --format=\"%h %an <%ae>%n%B\" && git show --stat --format= HEAD | tail -3 && git status --short && grep -rn -i \"co-authored\\|anthropic\" --exclude-dir=.venv --exclude-dir=.git --exclude-dir=datos . | grep -v uv.lock",
 "description": "Corregir formato y rehacer el commit sin coautoría"
}
```

<details><summary>Resultado</summary>

```text
29:- Con la sumaria (hogares): peso `factor07 * mieperho`. Así se calculan las cifras oficiales; puede diferir en una décima de la de personas (27.58% frente a 27.53% en 2024).
warning: in the working copy of '.claude/skills/limpiando-enaho/reference.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'evaluacion.md', LF will be replaced by CRLF the next time Git touches it
d227754 Frank Pinares <[correo oculto]>
Skills para limpiar, graficar y mapear la ENAHO 2024

 salidas/validacion.txt                             |   9 +
 uv.lock                                            | 635 +++++++++++++++++++++
 19 files changed, 1126 insertions(+)
[This command modified 1 file you've previously read: .claude\skills\limpiando-enaho\reference.md. Call Read before editing.]
```

</details>

## Asistente · 2026-10-31 14:31

El commit quedó limpio. Guardo en memoria tu preferencia para no repetirlo en futuras tareas.

**Herramienta `Write`**

```json
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

<details><summary>Resultado</summary>

```text
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

</details>

**Herramienta `Bash`**

```json
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

<details><summary>Resultado</summary>

```text
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

</details>

**Herramienta `Bash`**

```json
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

<details><summary>Resultado</summary>

```text
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

</details>

## Asistente · 2026-10-31 14:31

## 🔶 Revisión manual 6: listo para que lo publiques desde GitHub Desktop

Quité la línea de coautoría y reescribí los textos con tu estilo. El commit local ahora es `d227754` («Skills para limpiar, graficar y mapear la ENAHO 2024»), figura solo a tu nombre y sigue incluyendo los mismos 19 archivos.

### Referencias a Claude

| Tipo | Qué hice |
|---|---|
| Línea `Co-Authored-By: Claude…` del commit | **Eliminada.** Rehíce el commit, que todavía no estaba publicado. |
| «Claude» como sujeto en la prosa («Claude activó…», «Claude encontró…») | **Reemplazado por «el agente»** en `README.md` y `evaluacion.md`. |
| Referencias técnicas: carpeta `.claude/skills/`, variable `${CLAUDE_SKILL_DIR}`, comando `claude -p`, «Claude Code» como requisito y como título del tipo de skill | **Se mantienen.** Sin ellas las skills no funcionan: Claude Code solo las busca en `.claude/skills/`. Además, el PDF exige indicar «Requisitos: uv y Claude Code» en el README y usar `claude -p` en la evaluación. |

### Cambios de redacción

`README.md` y `evaluacion.md` siguen ahora los rasgos de tu tesis:
- voz impersonal con «se» y la fórmula «el presente repositorio»;
- conectores como «Ahora bien», «Y es que», «En ese sentido», «Si bien… », «siendo que», «Asimismo», «Por otra parte» y «Debe tenerse en cuenta que»;
- anáforas como «dicho» y «este último»;
- una conclusión que abre con «Una primera conclusión… es que»;
- porcentajes sin espacio (27.6%).

Las listas de viñetas pasaron a prosa: por ejemplo, el pipeline ahora se describe con «En primer lugar…, en segundo lugar…, y finalmente…». Mantuve las tablas y los bloques de código, porque son necesarios en un README.

Hay dos textos que no reescribí, y la razón es la misma regla de «no reescribir textos originales del profesor»:
- Los **`SKILL.md`** son instrucciones dirigidas al agente y siguen el formato imperativo de la versión de la clase.
- El texto de **`validacion.txt`** lo genera el código del esqueleto del profesor.

Los comentarios del código ya estaban en frases breves e impersonales.

### Pasos para publicar

1. Revisa `README.md` y `evaluacion.md` en `~\Documents\GitHub\enaho-skills\`.
2. En **GitHub Desktop**: *File → Add local repository…* → elige esa carpeta → **Publish repository**. Desmarca «Keep this code private» si el issue requiere que el repositorio sea público.
3. Pega el link en el issue de la sesión.

También guardé en memoria que tus commits y entregas van sin atribución a Claude, para no repetirlo en próximas tareas. Si quieres ajustar alguna frase de los textos, dímelo antes de publicar y rehago el commit.

## Usuario · 2026-10-31 14:39

Ya lo publiqué, este es el link: https://github.com/saffron29/enaho-skills

**Herramienta `Bash`**

```json
{
 "command": "cd ~/Documents/GitHub/enaho-skills && git remote -v && git fetch -q origin 2>&1; git status -sb | head -3; git ls-remote origin 2>&1 | head; git log --oneline -2",
 "description": "Verificar que el repo remoto coincide con el local"
}
```

<details><summary>Resultado</summary>

```text
origin	https://github.com/saffron29/enaho-skills.git (fetch)
origin	https://github.com/saffron29/enaho-skills.git (push)
## main...origin/main
d22775438d219bc704500289136bfb4808593f82	HEAD
d22775438d219bc704500289136bfb4808593f82	refs/heads/main
d227754 Skills para limpiar, graficar y mapear la ENAHO 2024
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "curl -s -o /dev/null -w \"%{http_code}\\n\" https://raw.githubusercontent.com/saffron29/enaho-skills/main/README.md; curl -s -o /dev/null -w \"%{http_code}\\n\" https://raw.githubusercontent.com/saffron29/enaho-skills/main/mapas/pobreza_departamento.png; curl -s -o /dev/null -w \"%{http_code}\\n\" https://raw.githubusercontent.com/saffron29/enaho-skills/main/.claude/skills/limpiando-enaho/SKILL.md",
 "description": "Comprobar que el repositorio es público y accesible"
}
```

<details><summary>Resultado</summary>

```text
200
200
200
```

</details>

**Herramienta `Bash`**

```json
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

<details><summary>Resultado</summary>

```text
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

</details>

## Asistente · 2026-10-31 14:39

La publicación salió bien: **https://github.com/saffron29/enaho-skills**

Lo comprobé de dos formas:
- **El remoto coincide con tu copia local.** `origin/main` apunta al mismo commit `d227754`, solo a tu nombre y sin nada pendiente de subir.
- **El repositorio es público.** El `README.md`, el mapa y los `SKILL.md` se pueden abrir sin iniciar sesión, así que tus evaluadores y compañeros podrán clonarlo.

### Lo único que falta

**Pega el link en el issue de la sesión** antes del sorteo de presentaciones.

### Si te toca presentar (3 minutos)

1. **El mapa y un gráfico:** `mapas/pobreza_departamento.png` (aparece en el README) y `figuras/pobreza_area.png`, con urbana 24.7% y rural 39.4%.
2. **`salidas/validacion.txt`:** 27.58% con la sumaria y 27.53% con personas, frente al 27.6% oficial, más el 5.50% de pobreza extrema y los 108,664 residentes habituales.
3. **Un pedido que activó dos skills seguidas:** «Haz un mapa de la pobreza por departamento», que activó `mapeando-enaho` y luego `limpiando-enaho` porque no existía la base limpia.
4. **El hallazgo de `evaluacion.md`, si te sobra tiempo:** sin skills, el agente acertó las cifras, pero cada corrida produjo archivos y estilos distintos, y no respondió la pregunta de Cusco. La ventaja de las skills está en la **reproducibilidad**, más que en evitar errores de cálculo.

Ya registré en memoria que la tarea quedó entregada.

## Usuario · 2026-10-31 14:50

Solo faltaría pegar el link del repo en el issue, con la siguiente estructura:

Nombre(s):
Link de tu repo:
Pobreza nacional que dio tu validación:
Pedido que activó dos skills seguidas:

## Asistente · 2026-10-31 14:50

Este es el texto para pegar en el issue:

```markdown
Nombre(s): Frank Pinares Gutiérrez
Link de tu repo: https://github.com/saffron29/enaho-skills
Pobreza nacional que dio tu validación: 27.58% con la sumaria (factor07 × mieperho) y 27.53% con la base de personas (facpob07), frente al 27.6% oficial del INEI; pobreza extrema de 5.50% y 108,664 residentes habituales.
Pedido que activó dos skills seguidas: «Haz un mapa de la pobreza por departamento con la ENAHO 2024», que activó mapeando-enaho y luego limpiando-enaho, pues no existía la base limpia (salidas/personas_2024.parquet).
```

- **Nombre:** solo va el tuyo, porque hiciste la tarea de forma individual. Si te piden un formato distinto, por ejemplo solo apellidos, ajústalo.
- **Pobreza nacional:** si el issue espera una sola cifra, puedes dejar solo «27.58% (oficial INEI: 27.6%)». Es la que el script compara con la cifra oficial.
- **El pedido:** es la corrida `3-con` de `evaluacion.md`, donde quedó registrado el encadenamiento de las dos skills.

## Usuario · 2026-10-31 14:51

Ya lo pegué en el issue

**Herramienta `Bash`**

```json
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

<details><summary>Resultado</summary>

```text
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

</details>

## Asistente · 2026-10-31 14:51

Con el link en el issue, la tarea de la Clase 8 queda entregada. Ya la marqué como cerrada en la memoria.

| Paso | Estado |
|---|---|
| 1 · Preparar | ✅ Repositorio con uv, las cuatro librerías y los datos del INEI |
| 2 · Limpiar | ✅ Validación con 27.58%, 5.50% y 108,664 residentes habituales |
| 3 · Graficar y mapear | ✅ 3 gráficos y el mapa, con los 25 departamentos unidos por código |
| 4 · Evaluar y subir | ✅ 6 corridas, 3 pruebas complementarias, README y repositorio público |
| Entrega | ✅ Link en el issue |

Si sales sorteado, los cuatro puntos de la presentación están en mi mensaje anterior.

Tienes la carpeta de pruebas en `~\AppData\Local\Temp\claude\C--Users-USER\50afee40-1161-4293-b4a9-85c2739871ed\scratchpad\eval\`, con las copias del repositorio y los registros de las corridas. Es temporal y puedes borrarla cuando quieras: lo importante ya está resumido en `evaluacion.md`.

## Usuario · 2026-10-31 14:52

Borra la carpeta de pruebas del scratchpad.

**Herramienta `Bash`**

```json
{
 "command": "cd \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad\" && ls eval eval/runs | head -40 && du -sh eval",
 "description": "Revisar contenido de la carpeta de pruebas antes de borrar"
}
```

<details><summary>Resultado</summary>

```text
eval:
correr.sh
resumir.py
runs

eval/runs:
1-con
1-con.err
1-con.jsonl
1-sin
1-sin.err
1-sin.jsonl
1-solo
1-solo.err
1-solo.jsonl
2-con
2-con.err
2-con.jsonl
2-sin
2-sin.err
2-sin.jsonl
2-solo
2-solo.err
2-solo.jsonl
3-con
3-con.err
3-con.jsonl
3-sin
3-sin.err
3-sin.jsonl
3-solo
3-solo.err
3-solo.jsonl
v1-1-con.err
v1-1-con.jsonl
v1-2-con.err
v1-2-con.jsonl
1.4G	eval
Shell cwd was reset to ~\.claude\projects\C--Users-USER\memory
```

</details>

**Herramienta `Bash`**

```json
{
 "command": "rm -rf \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad/eval\" && ls -la \"~/AppData/Local/Temp/claude/C--Users-USER/50afee40-1161-4293-b4a9-85c2739871ed/scratchpad\"; ls ~/Documents/GitHub/enaho-skills",
 "description": "Borrar la carpeta de pruebas y verificar"
}
```

<details><summary>Resultado</summary>

```text
total 0
drwxr-xr-x 1 USER 197121 0 Oct 31 09:53 .
drwxr-xr-x 1 USER 197121 0 Oct 31 08:46 ..
README.md
datos
evaluacion.md
figuras
mapas
pyproject.toml
salidas
uv.lock
```

</details>

**Herramienta `Bash`**

```json
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

<details><summary>Resultado</summary>

```text
[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]
```

</details>

## Asistente · 2026-10-31 14:54

Borré la carpeta de pruebas del scratchpad (1.4 GB). Contenía los dos scripts de prueba, las 11 copias del repositorio y los registros de cada corrida. El scratchpad quedó vacío.

Tu repositorio `~\Documents\GitHub\enaho-skills` sigue completo, y lo que se obtuvo de las pruebas está resumido en `evaluacion.md`. También actualicé la memoria para que no siga indicando esa carpeta como si existiera.
