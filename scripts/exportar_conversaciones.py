"""Exporta conversaciones de Claude Code (.jsonl) a Markdown legible y oculta la información sensible.

    uv run scripts/exportar_conversaciones.py SESION.jsonl SALIDA.md --titulo "..."
    uv run scripts/exportar_conversaciones.py --sanear evidencias_ia/**/*.jsonl   # oculta datos en los registros

Qué se oculta o se omite:
- Los bloques <system-reminder> (contexto interno: correo de la cuenta e índice de memorias personales).
- Lo leído o escrito en la carpeta de memoria personal del asistente (~/.claude/projects/.../memory) y en
  carpetas de documentos personales del autor ajenas a la tarea (por ejemplo, la de su sustentación de tesis).
- Correos, teléfonos de 9 dígitos, DNI, tokens o claves, y la ruta del usuario (C:\\Users\\USER -> ~).
- Los términos personales de scripts/ocultar_local.txt (código de alumno, proyectos o servicios ajenos a la tarea),
  un archivo local que no se sube al repositorio para no publicar esos términos dentro de este script.
Las imágenes se marcan como [imagen] y las salidas de más de 4,000 caracteres se recortan indicándolo.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
LIMITE = 4000
OMITIDO = "[contenido personal omitido: memoria del asistente o documentos personales ajenos a la tarea]"
PATRONES = [
    (re.compile(r"<system-reminder>.*?</system-reminder>", re.S), ""),
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"), "[correo oculto]"),
    (re.compile(r"(?i)(DNI\D{0,12})\d{8}"), r"\1[DNI oculto]"),
    (re.compile(r"\b9\d{2}[ -]?\d{3}[ -]?\d{3}\b"), "[teléfono oculto]"),
    (re.compile(r"\b(sk-[A-Za-z0-9_-]{16,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AIza[0-9A-Za-z_-]{30,})"),
     "[token oculto]"),
    (re.compile(r"(?i)c:(\\\\|\\|/)users(\\\\|\\|/)user"), "~"),
    (re.compile(r"(?i)/c/users/user"), "~"),
]


# Términos personales adicionales (código de alumno, proyectos o servicios ajenos a la tarea): se leen de un archivo
# local que no se sube al repositorio, una expresión regular por línea, para no publicarlos dentro de este script.
LOCAL = Path(__file__).with_name("ocultar_local.txt")
if LOCAL.exists():
    PATRONES += [(re.compile(l.strip(), re.I), "[dato personal oculto]")
                 for l in LOCAL.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]


def ocultar(texto: str) -> str:
    for patron, reemplazo in PATRONES:
        texto = patron.sub(reemplazo, texto)
    return texto


def es_memoria(texto: str) -> bool:
    """Llamadas cuyo contenido se omite: la memoria personal del asistente y los documentos personales del autor."""
    t = texto.replace("\\\\", "/").replace("\\", "/").lower()
    personales = ("sustentación de tesis", "sustentacion de tesis")
    return ("/memory/" in t and ".claude/projects" in t) or "memory.md" in t or any(p in t for p in personales)


def recortar(texto: str) -> str:
    return texto if len(texto) <= LIMITE else texto[:LIMITE] + f"\n[... salida recortada: {len(texto):,} caracteres]"


def texto_resultado(contenido) -> str:
    if isinstance(contenido, str):
        return contenido
    partes = []
    for c in contenido or []:
        partes.append(c.get("text", "") if c.get("type") == "text" else "[imagen]")
    return "\n".join(partes)


def exportar(ruta: Path, salida: Path, titulo: str):
    lineas = [f"# {titulo}", "", f"Exportación de la sesión `{ruta.stem}` de Claude Code. Se ocultaron correos, "
              "teléfonos, DNI, tokens, rutas personales, el contexto interno del sistema y el contenido de la memoria "
              "personal del asistente.", ""]
    memoria = set()   # ids de llamadas que tocan la memoria personal
    for linea in ruta.read_text(encoding="utf-8").splitlines():
        try:
            e = json.loads(linea)
        except json.JSONDecodeError:
            continue
        hora = e.get("timestamp", "")[:16].replace("T", " ")
        msg = e.get("message") or {}
        contenido = msg.get("content")
        if e.get("type") == "user":
            if isinstance(contenido, str):
                t = ocultar(contenido).strip()
                if t:
                    lineas += [f"## Usuario · {hora}", "", t, ""]
                continue
            for c in contenido or []:
                if c.get("type") == "text":
                    t = ocultar(c["text"]).strip()
                    if t:
                        lineas += [f"## Usuario · {hora}", "", t, ""]
                elif c.get("type") == "image":
                    lineas += ["[imagen]", ""]
                elif c.get("type") == "tool_result":
                    if c.get("tool_use_id") in memoria:
                        t = OMITIDO
                    else:
                        t = ocultar(recortar(texto_resultado(c.get("content"))))
                    marca = " (error)" if c.get("is_error") else ""
                    lineas += [f"<details><summary>Resultado{marca}</summary>", "", "```text", t.replace("```", "ʼʼʼ"),
                               "```", "", "</details>", ""]
        elif e.get("type") == "assistant":
            for c in contenido or []:
                if c.get("type") == "text" and c["text"].strip():
                    lineas += [f"## Asistente · {hora}", "", ocultar(c["text"]).strip(), ""]
                elif c.get("type") == "tool_use":
                    entrada = json.dumps(c.get("input", {}), ensure_ascii=False, indent=1)
                    if es_memoria(entrada):
                        memoria.add(c["id"])
                        entrada = OMITIDO
                    lineas += [f"**Herramienta `{c['name']}`**", "", "```json", ocultar(recortar(entrada)).replace(
                        "```", "ʼʼʼ"), "```", ""]
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text("\n".join(lineas), encoding="utf-8")
    print(f"{salida.as_posix()}: {len(lineas):,} líneas; {len(memoria)} llamadas a la memoria omitidas")


def sanear(rutas):
    """Oculta datos sensibles dentro de registros stream-json (claude -p) sin cambiar su estructura."""
    for ruta in rutas:
        original = ruta.read_text(encoding="utf-8")
        limpio = "\n".join(ocultar(l) if l.strip() else l for l in original.splitlines())
        if limpio != original:
            ruta.write_text(limpio + "\n", encoding="utf-8")
            print(f"saneado: {ruta.as_posix()}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("rutas", nargs="+", type=Path)
    p.add_argument("--titulo", default="Conversación con Claude Code")
    p.add_argument("--sanear", action="store_true")
    a = p.parse_args()
    if a.sanear:
        sanear(a.rutas)
    else:
        exportar(a.rutas[0], a.rutas[1], a.titulo)
