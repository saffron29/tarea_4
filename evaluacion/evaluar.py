"""Experimento: las mismas 10 preguntas a Claude Code sin y con el MCP y las skills del proyecto.

    uv run evaluacion/evaluar.py --modos A B           # escribe evaluacion/resultados.csv
    uv run evaluacion/evaluar.py --modos A --ids B1 E1 # solo algunas preguntas

Modo A (sin MCP ni skills): cada pregunta corre en una carpeta vacía y nueva, con --tools "" (ninguna herramienta)
y --strict-mcp-config sin servidores; así no puede leer archivos con respuestas ni cargar memorias del proyecto.
Modo B (con MCP y skills): cada pregunta corre en una copia del repositorio SIN evaluacion/, informes/,
evidencias_ia/ ni README.md (que contienen respuestas) y con salidas/, figuras/ y mapas/ vacías, de modo que el
agente debe obtener cada cifra con el MCP del BCRP y las skills de la ENAHO.

En ambos: el mismo modelo, la misma instrucción, una sesión independiente por pregunta (--no-session-persistence) y
el registro stream-json completo en evidencias_ia/evaluacion/. Las respuestas esperadas vienen de preguntas.csv,
congeladas antes de correr (commit d3731a7).
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
AQUI = Path(__file__).parent
RAIZ = AQUI.parent
REGISTROS = RAIZ / "evidencias_ia" / "evaluacion"
ESQUEMA = {"type": "object", "required": ["valor", "fuente", "interpretacion"],
           "properties": {"valor": {"type": ["number", "null"]}, "unidad": {"type": "string"},
                          "fuente": {"type": "string"}, "interpretacion": {"type": "string"}}}
INSTRUCCION = ("Responde la pregunta con un solo número en «valor», en la unidad que pide. Si no puedes saberlo con "
               "certeza, pon valor null: no estimes. En «fuente» di de dónde sale la cifra (serie, archivo o "
               "publicación). En «interpretacion» escribe una o dos frases sobre qué significa el resultado.\n\n")
HERRAMIENTAS_B = "Skill,Bash,PowerShell,Read,Write,Edit,Glob,Grep,ListMcpResourcesTool,ReadMcpResourceTool"
PERMITIDAS_B = ("mcp__bcrp,Skill,Bash(uv run:*),Bash(ls:*),Bash(cat:*),Bash(head:*),PowerShell(uv run:*),Read,Write,"
                "Edit,Glob,Grep,ListMcpResourcesTool,ReadMcpResourceTool")
EXCLUIR_B = {".git", ".venv", "evaluacion", "informes", "evidencias_ia", "README.md", "salidas", "figuras", "mapas",
             "__pycache__", ".pytest_cache"}
CAUSALES = re.compile(r"\b(causa|causó|provoca|provocó|genera|generó|explica|debido a|porque)\b", re.I)


def preparar_b(base: Path) -> Path:
    """Copia limpia del repositorio para el modo B (los microdatos se copian; las salidas no)."""
    if base.exists():
        shutil.rmtree(base)
    shutil.copytree(RAIZ, base, ignore=lambda d, nombres: [n for n in nombres if n in EXCLUIR_B])
    for carpeta in ("salidas", "figuras", "mapas", "informes"):
        (base / carpeta).mkdir()
    subprocess.run(["uv", "sync", "-q"], cwd=base, check=True)
    return base


def limpiar_salidas(base: Path):
    for carpeta in ("salidas", "figuras", "mapas", "informes"):
        shutil.rmtree(base / carpeta, ignore_errors=True)
        (base / carpeta).mkdir()


def preguntar(fila, modo, modelo, carpeta_b: Path | None, trabajo: Path):
    if modo == "A":
        cwd = trabajo / f"A_{fila.id}"
        shutil.rmtree(cwd, ignore_errors=True)
        cwd.mkdir(parents=True)
        extra = ["--tools", "", "--strict-mcp-config"]
    else:
        cwd = carpeta_b
        limpiar_salidas(cwd)
        extra = ["--tools", HERRAMIENTAS_B, "--allowedTools", PERMITIDAS_B, "--strict-mcp-config",
                 "--mcp-config", str(cwd / ".mcp.json")]
    cmd = ["claude", "-p", INSTRUCCION + fila.pregunta, "--model", modelo, "--output-format", "stream-json",
           "--verbose", "--json-schema", json.dumps(ESQUEMA), "--no-session-persistence", *extra]
    registro = REGISTROS / f"{modo}_{fila.id}.jsonl"
    t = time.time()
    with open(registro, "w", encoding="utf-8") as salida:
        proc = subprocess.run(cmd, stdout=salida, stderr=subprocess.PIPE, text=True, encoding="utf-8", cwd=cwd,
                              timeout=1800)
    segundos = round(time.time() - t, 1)
    herramientas, final = [], {}
    for linea in registro.read_text(encoding="utf-8").splitlines():
        try:
            e = json.loads(linea)
        except json.JSONDecodeError:
            continue
        if e.get("type") == "assistant":
            for c in e["message"]["content"]:
                if c.get("type") == "tool_use" and c["name"] != "StructuredOutput":   # formato de salida, no herramienta
                    nombre = c["name"]
                    if nombre == "Skill":
                        nombre = f"Skill:{c['input'].get('skill', '?')}"
                    elif nombre.startswith("mcp__"):
                        nombre = "MCP:" + nombre.split("__")[-1]
                    herramientas.append(nombre)
        elif e.get("type") == "result":
            final = e
    r = final.get("structured_output") or {}
    error = None if final and not final.get("is_error") else (final.get("subtype") or proc.stderr[-300:] or "sin resultado")
    return {"valor": r.get("valor"), "unidad_respuesta": r.get("unidad", ""), "fuente_respuesta": r.get("fuente", ""),
            "interpretacion": r.get("interpretacion", ""), "herramientas": ";".join(dict.fromkeys(herramientas)),
            "n_llamadas": len(herramientas), "segundos": segundos, "turnos": final.get("num_turns"),
            "costo_usd": round(final.get("total_cost_usd") or 0, 4), "error": error,
            "registro": registro.relative_to(RAIZ).as_posix()}


def calificar(fila, res):
    v = res["valor"]
    if v is None:
        return "sin respuesta"
    margen = fila.tolerancia * abs(fila.respuesta_esperada) if fila.tipo_tolerancia == "relativa" else fila.tolerancia
    return "correcta" if abs(v - fila.respuesta_esperada) <= margen else "incorrecta"


def criterio_mixto(fila, res):
    """Para las mixtas: ¿cita ambas fuentes y evita lenguaje causal? (revisión automática; el autor la confirma)."""
    if fila.tipo != "Mixta":
        return ""
    texto = f"{res['fuente_respuesta']} {res['interpretacion']}"
    ambas = bool(re.search(r"BCRP|RD166", texto)) and bool(re.search(r"ENAHO|INEI", texto))
    causal = bool(CAUSALES.search(res["interpretacion"]))
    return f"ambas_fuentes={'sí' if ambas else 'no'}; lenguaje_causal={'sí' if causal else 'no'}"


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--modos", nargs="+", default=["A", "B"], choices=["A", "B"])
    p.add_argument("--ids", nargs="*", default=None)
    p.add_argument("--modelo", default="sonnet")
    p.add_argument("--trabajo", required=True, help="carpeta temporal fuera del repositorio")
    p.add_argument("--salida", default=str(AQUI / "resultados.csv"))
    a = p.parse_args()
    trabajo = Path(a.trabajo)
    REGISTROS.mkdir(parents=True, exist_ok=True)
    preguntas = pd.read_csv(AQUI / "preguntas.csv")
    if a.ids:
        preguntas = preguntas[preguntas.id.isin(a.ids)]
    carpeta_b = preparar_b(trabajo / "copia_B") if "B" in a.modos else None
    filas = []
    for modo in a.modos:
        for fila in preguntas.itertuples():
            print(f"[{time.strftime('%H:%M:%S')}] modo {modo} · {fila.id} ...", flush=True)
            res = preguntar(fila, modo, a.modelo, carpeta_b, trabajo)
            filas.append({"id": fila.id, "tipo": fila.tipo, "modo": modo, "modelo": a.modelo,
                          "pregunta": fila.pregunta, "respuesta_esperada": fila.respuesta_esperada,
                          "unidad": fila.unidad, "tolerancia": fila.tolerancia, "tipo_tolerancia": fila.tipo_tolerancia,
                          "respuesta_generada": res["valor"], "resultado": calificar(fila, res),
                          "criterio_mixto": criterio_mixto(fila, res), **res})
            print(f"    -> {res['valor']} ({filas[-1]['resultado']}) en {res['segundos']} s; {res['herramientas']}",
                  flush=True)
    nuevos = pd.DataFrame(filas)
    salida = Path(a.salida)
    if salida.exists():   # se reemplazan solo las filas que se volvieron a correr
        viejos = pd.read_csv(salida)
        viejos = viejos[~viejos.set_index(["id", "modo"]).index.isin(nuevos.set_index(["id", "modo"]).index)]
        nuevos = pd.concat([viejos, nuevos]).sort_values(["modo", "id"])
    nuevos.to_csv(salida, index=False, encoding="utf-8")
    print(nuevos.groupby("modo").resultado.value_counts().to_string())
