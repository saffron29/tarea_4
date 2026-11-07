"""Resume un registro stream-json de Claude Code: herramientas disponibles, skills y herramientas MCP usadas,
comandos ejecutados, respuesta final, turnos, tiempo y costo.

    uv run scripts/resumir_registro.py evidencias_ia/skills/activacion_1_encadenamiento.jsonl
    uv run scripts/resumir_registro.py evidencias_ia/skills/*.jsonl --markdown > evidencias_ia/skills/resumen.md
"""
import argparse
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")


def resumir(ruta: Path) -> dict:
    r = {"archivo": ruta.as_posix(), "modelo": None, "mcp": [], "pasos": [], "skills": [], "mcp_usadas": [],
         "resultado": "", "turnos": None, "segundos": None, "costo_usd": None, "error": None}
    for linea in ruta.read_text(encoding="utf-8").splitlines():
        if not linea.strip():
            continue
        e = json.loads(linea)
        if e.get("type") == "system" and e.get("subtype") == "init":
            r["modelo"] = e.get("model")
            r["mcp"] = [f"{s['name']} ({s['status']})" for s in e.get("mcp_servers", [])]
        elif e.get("type") == "assistant":
            for c in e["message"]["content"]:
                if c.get("type") != "tool_use":
                    continue
                nombre, entrada = c["name"], c.get("input", {})
                if nombre == "Skill":
                    r["skills"].append(entrada.get("skill") or entrada.get("command") or "?")
                    detalle = json.dumps(entrada, ensure_ascii=False)
                elif nombre.startswith("mcp__"):
                    r["mcp_usadas"].append(nombre.split("__")[-1])
                    detalle = json.dumps(entrada, ensure_ascii=False)
                elif nombre in ("Bash", "PowerShell"):
                    detalle = entrada.get("command", "")
                else:
                    detalle = json.dumps(entrada, ensure_ascii=False)
                r["pasos"].append(f"{nombre}: {detalle[:220]}")
        elif e.get("type") == "result":
            r["resultado"] = e.get("result", "")
            r["turnos"] = e.get("num_turns")
            r["segundos"] = round(e.get("duration_ms", 0) / 1000, 1)
            r["costo_usd"] = round(e.get("total_cost_usd") or 0, 4)
            r["error"] = e.get("subtype") if e.get("is_error") else None
    return r


def markdown(r: dict) -> str:
    pasos = "\n".join(f"{i}. `{p.replace('`', 'ʼ')}`" for i, p in enumerate(r["pasos"], 1))
    return (f"### {Path(r['archivo']).name}\n\n"
            f"- Modelo: {r['modelo']} · servidores MCP: {', '.join(r['mcp']) or 'ninguno'}\n"
            f"- Skills activadas: {', '.join(r['skills']) or 'ninguna'} · herramientas MCP usadas: "
            f"{', '.join(r['mcp_usadas']) or 'ninguna'}\n"
            f"- Turnos: {r['turnos']} · tiempo: {r['segundos']} s · costo informado: {r['costo_usd']} USD"
            f"{' · ERROR: ' + r['error'] if r['error'] else ''}\n\n"
            f"Pasos:\n\n{pasos}\n\nRespuesta final:\n\n> " + r["resultado"].replace("\n", "\n> ") + "\n")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("registros", nargs="+", type=Path)
    p.add_argument("--markdown", action="store_true")
    a = p.parse_args()
    for ruta in a.registros:
        r = resumir(ruta)
        if a.markdown:
            print(markdown(r))
        else:
            print(f"{ruta.name}: skills={r['skills']} mcp={r['mcp_usadas']} turnos={r['turnos']} "
                  f"s={r['segundos']} usd={r['costo_usd']} error={r['error']}")
