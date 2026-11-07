# Referencia de variables · ENAHO 2024

Códigos tomados del diccionario del INEI (`Diccionario2024.pdf`, dentro de cada zip).

## Variables de la base `salidas/personas_2024.parquet`

| Variable | Viene de | Qué es | Códigos |
|---|---|---|---|
| `conglome`, `vivienda`, `hogar` | ambos | Llaves del hogar (texto, con ceros) | 6, 3 y 2 caracteres |
| `codperso` | miembros | Número de la persona en el hogar (texto) | 2 caracteres |
| `p203` | miembros | Parentesco con el jefe(a) del hogar | 0 panel, 1 jefe/jefa, 2 esposo(a), 3 hijo(a), 4 yerno/nuera, 5 nieto(a), 6 padres/suegros, 7 otros parientes, 8 trabajador del hogar, 9 pensionista, 10 otros no parientes, 11 hermano(a) |
| `p207` | miembros | Sexo | 1 hombre, 2 mujer |
| `p208a` | miembros | Edad en años cumplidos | 0–98 (0 = menor de un año; el diccionario indica 1–98 y los meses van en `p208b`); 99 es valor perdido |
| `facpob07` | miembros | Factor de expansión de población | Peso de cada persona |
| `pobreza` | sumaria | Pobreza monetaria del hogar | 1 pobre extremo, 2 pobre no extremo, 3 no pobre |
| `mieperho` | sumaria | Total de miembros del hogar | Número |
| `factor07` | sumaria | Factor de expansión del hogar | Peso de cada hogar |
| `ubigeo` | sumaria | Ubicación geográfica (texto) | 6 dígitos: departamento, provincia, distrito |
| `estrato` | sumaria | Estrato geográfico | 1–5 urbano (de 500 000 a más hasta 2 000 habitantes); 6 de 500 a 1 999 habitantes, 7 AER compuesto, 8 AER simple (rural) |
| `dominio` | sumaria | Dominio geográfico | 1 Costa Norte, 2 Costa Centro, 3 Costa Sur, 4 Sierra Norte, 5 Sierra Centro, 6 Sierra Sur, 7 Selva, 8 Lima Metropolitana |
| `departamento` | construida | `ubigeo[:2]` | Ver tabla de abajo |
| `territorio` | construida | `ubigeo[:2]`, pero Lima se separa | `15LM` Lima Metropolitana (provincia `1501`), `15LP` Lima Provincias (resto del departamento 15) |
| `area` | construida | `estrato <= 5` | Urbana / Rural |
| `sexo`, `edad` | construidas | `p207` y `p208a` agrupada | Hombre / Mujer; 0-17, 18-29, 30-44, 45-59, 60+ |
| `urbano` | construida | `estrato <= 5` | True / False |
| `pobre` | construida | `pobreza <= 2` | True / False |
| `pobre_extremo` | construida | `pobreza == 1` | True / False |

## Cómo ponderar

- Indicadores territoriales (nacional, área, departamento, territorio): sumaria con peso `factor07 * mieperho`, que es como se obtienen las cifras oficiales (27.58% nacional, 24.81% urbano y 39.30% rural en 2024, y los 25 departamentos iguales a la referencia de la Sesión 16).
- Indicadores individuales (sexo, edad): base de personas con `100 * (pobre * facpob07).sum() / facpob07.sum()` (27.53% nacional). La diferencia con la sumaria se debe a que en 1,846 hogares el número de residentes habituales no coincide con `mieperho`.
- Nunca promedio simple: el promedio simple de hogares daría 20.22%, más de 7 puntos por debajo.

## Tabla `salidas/indicadores.csv`

| Columna | Qué es |
|---|---|
| `anio` | Año de la encuesta |
| `nivel` | `nacional`, `area`, `departamento` (25), `territorio` (26, Lima separada), `sexo`, `edad` |
| `codigo` | Código de la categoría: `01`–`25`, `15LM`, `15LP`, `Urbana`, `Mujer`, `0-17`, etc. |
| `nombre` | Nombre legible |
| `pobreza_pct`, `pobreza_extrema_pct` | % de personas, ponderado, con 4 decimales (se redondea una sola vez al presentar) |
| `poblacion` | Población expandida (suma del peso) |
| `muestra` | Hogares (sumaria) o personas (base de personas) encuestados |
| `base`, `ponderador` | De qué base y con qué peso se calculó |
| `fuente` | INEI, ENAHO, módulos 34 y 02 |

## Códigos de departamento (`ubigeo[:2]`)

Para unir con mapas u otras tablas se usa siempre el código, nunca el nombre.

| Código | Departamento | Código | Departamento |
|---|---|---|---|
| 01 | Amazonas | 14 | Lambayeque |
| 02 | Áncash | 15 | Lima (sin Callao) |
| 03 | Apurímac | 16 | Loreto |
| 04 | Arequipa | 17 | Madre de Dios |
| 05 | Ayacucho | 18 | Moquegua |
| 06 | Cajamarca | 19 | Pasco |
| 07 | Callao | 20 | Piura |
| 08 | Cusco | 21 | Puno |
| 09 | Huancavelica | 22 | San Martín |
| 10 | Huánuco | 23 | Tacna |
| 11 | Ica | 24 | Tumbes |
| 12 | Junín | 25 | Ucayali |
| 13 | La Libertad | | |

Variables que no están en la base (ingresos, gastos, educación, empleo) requieren otros módulos del INEI; antes de agregarlas, se pide confirmación al usuario.
