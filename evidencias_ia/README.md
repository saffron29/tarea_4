# Evidencias del uso de inteligencia artificial

El proyecto se desarrolló con Claude Code como asistente de programación y como agente de investigación. La presente carpeta reúne, por un lado, las conversaciones completas con el asistente durante el desarrollo (Opción B del enunciado: exportación a Markdown) y, por otro, los registros completos (`stream-json`) de cada ejecución del agente con `claude -p`. Antes de publicarlos se ocultaron correos, teléfonos, DNI, tokens o claves y la ruta del usuario (reemplazada por `~`), y se omitieron el contexto interno del sistema y el contenido de la memoria personal del asistente; el procedimiento está en `scripts/exportar_conversaciones.py`.

## Conversaciones de desarrollo

| Archivo | Qué abarca |
|---|---|
| `mcp/conversacion_2026-10-28_desarrollo_mcp_bcrp.md` | Desarrollo del servidor MCP del BCRP en la tarea de la Sesión 04: herramientas, herramienta propia `correlacion`, recurso, prompt, pruebas y evaluación. Es la base de `mcp/server.py`. |
| `skills/conversacion_2026-10-31_desarrollo_skills_enaho.md` | Desarrollo de las Skills `limpiando-enaho`, `graficando-enaho` y `mapeando-enaho` en la tarea de la Sesión 16, con sus validaciones y su evaluación. |
| `conversaciones/conversacion_2026-11-06_tarea_4.md` | La Tarea 4 completa: diseño, integración del MCP en `mcp/` y herramienta `departamentos` (Parte 1), reescritura de las Skills con validación explícita y rediseño de figuras (Parte 2), Skill `investigando-peru`, ejecución integrada e informe (Parte 3), diseño y ejecución del experimento, verificación manual, README y estas evidencias (Parte 4). Incluye las revisiones y autorizaciones del autor en cada etapa. |

## Registros de ejecución del agente

| Carpeta | Contenido |
|---|---|
| `mcp/demo_mcp_claude_code.jsonl` | Claude Code usando solo el MCP: identifica la serie, pide los datos, calcula con `resumen` y `departamentos`, y cita código, periodo y fuente. |
| `skills/` | Activación de las Skills por encadenamiento (mapa sin base procesada), por lenguaje natural y por invocación directa (`resumen_activacion.md`), y la prueba en que una validación esencial falla y el proceso se detiene (`prueba_falla_validacion.txt`). |
| `integracion/` | La ejecución integrada final (`ejecucion_integrada.jsonl`), con tres herramientas MCP y cuatro Skills en una sola sesión; la primera ejecución corregida (`v1/`); y una corrida en que las herramientas fallan y el agente no inventa cifras (`manejo_errores.jsonl`). Resumen en `resumen_integracion.md`. |
| `evaluacion/` | Las treinta corridas del experimento: `A_*.jsonl` (sin MCP ni Skills), `B_*.jsonl` (con ellos, resultado oficial) y `B2_*.jsonl` (tras corregir las descripciones de las Skills). |

Los resúmenes legibles de cualquier registro pueden regenerarse con `uv run scripts/resumir_registro.py <archivo.jsonl> --markdown`.
