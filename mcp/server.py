"""Servidor MCP del BCRP. Empiecen aquí: buscar_series ya funciona; completen los TODO hasta que pasen las pruebas.

    uv run pytest                                           # el contrato: las 8 pruebas deben pasar
    uv run server.py                                        # el servidor, por stdio
    claude mcp add --scope project bcrp -- uv run server.py # conectarlo a Claude Code

Las cuentas las hace Python, no el modelo: así cada cifra sale de una llamada que se puede repetir.
"""
import json
import re
import time
import unicodedata
from functools import cache
from pathlib import Path

import httpx
import pandas as pd
from fastmcp import FastMCP
from fastmcp.exceptions import ToolError

AQUI = Path(__file__).parent          # carpeta mcp/
RAIZ = AQUI.parent                     # raíz del proyecto
CATALOGO = RAIZ / "datos" / "catalogo_bcrp.csv"
URL_CATALOGO = "https://estadisticas.bcrp.gob.pe/estadisticas/series/metadata"
API = "https://estadisticas.bcrp.gob.pe/estadisticas/series/api"
SOLO_LECTURA = {"readOnlyHint": True, "openWorldHint": True}

mcp = FastMCP("bcrp", instructions=(
    "Series oficiales del Banco Central de Reserva del Perú (BCRP). Primero busca el código con buscar_series; "
    "luego usa resumen para variaciones, promedios y extremos, y serie para los datos. No calcules a mano: "
    "cita siempre el código de la serie y el periodo."))


def _sin_tildes(s):
    return unicodedata.normalize("NFD", str(s).lower()).encode("ascii", "ignore").decode()


@cache
def catalogo():
    """El catálogo oficial: 17 mil series en unos 7 MB. Se baja una vez y queda en datos/."""
    if not CATALOGO.exists():
        CATALOGO.parent.mkdir(exist_ok=True)
        r = httpx.get(URL_CATALOGO, timeout=120)
        r.raise_for_status()
        CATALOGO.write_text(r.content.decode("latin-1"), encoding="utf-8")
    df = pd.read_csv(CATALOGO, sep=";", dtype=str).fillna("")
    df = df.rename(columns={"Código de serie": "codigo", "Categoría de serie": "categoria", "Grupo de serie": "grupo",
                            "Nombre de serie": "nombre", "Frecuencia": "frecuencia",
                            "Fecha de actualización": "actualizada", "Fecha de inicio": "inicio"})
    df["texto"] = (df.categoria + " " + df.grupo + " " + df.nombre).map(_sin_tildes)
    return df


def _ficha(codigo):
    fila = catalogo().query("codigo == @codigo")
    if fila.empty:
        raise ToolError(f"No existe el código de serie {codigo!r}. Búsquenlo con buscar_series.")
    f = fila.iloc[0]
    return {"codigo": f.codigo, "nombre": f"{f.grupo} - {f.nombre}", "categoria": f.categoria,
            "frecuencia": f.frecuencia, "inicio": f.inicio, "actualizada": f.actualizada}


@mcp.tool(annotations=SOLO_LECTURA)
def buscar_series(texto: str, frecuencia: str | None = None, limite: int = 10) -> list[dict]:
    """Busca series del BCRP por palabras: todas deben aparecer en la categoría, el grupo o el nombre.

    Ejemplos: "ipc 12 meses", "tipo de cambio interbancario venta", "reservas internacionales netas",
    "tasa de referencia", "cobre precio". frecuencia: "Diaria", "Mensual", "Trimestral" o "Anual".
    Devuelve el código, el nombre completo, la frecuencia y desde cuándo hay datos. Si no hay resultados,
    prueben con menos palabras.
    """
    df = catalogo()
    m = pd.Series(True, index=df.index)
    for palabra in _sin_tildes(texto).split():
        m &= df.texto.str.contains(re.escape(palabra))
    if frecuencia:
        m &= df.frecuencia.str.lower() == frecuencia.lower()
    # primero las series vigentes y, entre ellas, las de nombre más corto (las más generales)
    sel = df[m]
    orden = sel.assign(vieja=sel.actualizada < "2025", largo=(sel.grupo + sel.nombre).str.len())
    return [_ficha(c) for c in orden.sort_values(["vieja", "largo"]).head(limite).codigo]


# TODO 1 · serie: debe considerarse que la API pide "2025-1" (mensual y trimestral), "2025-01-15" (diaria) o "2025"
# (anual), pero responde "Ene.2025", "01.Oct.26", "T1.25" o "2025". Por ello, las dos funciones siguientes realizan
# la traducción en cada sentido.
MESES = {"ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5, "jun": 6,
         "jul": 7, "ago": 8, "set": 9, "sep": 9, "oct": 10, "nov": 11, "dic": 12}


def _fecha_api(fecha, frecuencia, final=False):
    """Convierte "2025-01", "2025-T1" o "2025-01-15" al formato que pide la API, según la frecuencia de la serie."""
    partes = str(fecha).strip().upper().replace("T", "").split("-")
    anio = partes[0]
    if frecuencia == "Anual" or len(partes) == 1:
        if frecuencia == "Diaria":       # si se pide "2025" en una serie diaria, se toma todo el año
            return f"{anio}-12-31" if final else f"{anio}-01-01"
        if frecuencia in ("Mensual", "Trimestral"):
            return f"{anio}-{(4 if frecuencia == 'Trimestral' else 12) if final else 1}"
        return anio
    if frecuencia == "Diaria":
        if len(partes) == 2:             # si se pide "2026-10" en una serie diaria, se toma todo el mes
            dia = pd.Period(f"{anio}-{partes[1]}", "M").days_in_month if final else 1
            return f"{anio}-{int(partes[1]):02d}-{dia:02d}"
        return f"{anio}-{int(partes[1]):02d}-{int(partes[2]):02d}"
    return f"{anio}-{int(partes[1])}"   # en mensual y trimestral, la API pide el número sin cero adelante


def _periodo(nombre, frecuencia):
    """Convierte el nombre que devuelve la API ("Ene.2025", "01.Oct.26", "T1.25", "2025") al formato "2025-01",
    "2026-10-01", "2025-T1" o "2025"."""
    if frecuencia == "Mensual":
        mes, anio = nombre.split(".")
        return f"{anio}-{MESES[mes[:3].lower()]:02d}"
    if frecuencia == "Diaria":
        dia, mes, anio = nombre.split(".")
        return f"20{anio}-{MESES[mes[:3].lower()]:02d}-{int(dia):02d}"
    if frecuencia == "Trimestral":
        trimestre, anio = nombre.split(".")
        return f"20{anio}-{trimestre}"
    return nombre


@cache
def _pedir(url):
    """Descarga el JSON de la API. Ahora bien, si la API responde con la página HTML que envía cuando recibe
    demasiados pedidos seguidos, se espera unos segundos y se vuelve a intentar."""
    for intento in range(4):
        try:
            r = httpx.get(url, timeout=60)
            return json.loads(r.content.decode("latin-1"))
        except (httpx.HTTPError, json.JSONDecodeError):
            time.sleep(2 * (intento + 1))
    raise ToolError(f"El BCRP no respondió con datos para {url}. Se recomienda esperar unos segundos y volver a "
                    "intentarlo.")


@mcp.tool(annotations={"readOnlyHint": False, "openWorldHint": True})
def serie(codigo: str, desde: str, hasta: str, guardar: bool = False) -> dict:
    """Datos de una serie del BCRP entre dos fechas, ambas incluidas, con la URL de la fuente.

    Las fechas dependen de la frecuencia de la serie: "2025-01" (mensual), "2025-01-15" (diaria), "2025-T1"
    (trimestral) o "2025" (anual). Por ejemplo: serie("PN01273PM", "2025-01", "2025-12"). En caso de no conocer el
    código, se debe usar antes buscar_series. Asimismo, para variaciones, promedios o valores extremos se debe usar
    resumen en lugar de calcularlos a mano. Con guardar=True escribe además salidas/bcrp_serie_<codigo>.csv, para que
    los gráficos usen exactamente estos datos sin copiarlos a mano.
    """
    ficha = _ficha(codigo)               # lanza un ToolError si el código no existe
    frecuencia = ficha["frecuencia"]
    url = f"{API}/{codigo}/json/{_fecha_api(desde, frecuencia)}/{_fecha_api(hasta, frecuencia, final=True)}"
    datos = [{"periodo": _periodo(p["name"], frecuencia), "valor": round(float(p["values"][0]), 4)}
             for p in _pedir(url).get("periods", []) if p["values"][0] != "n.d."]
    if not datos:
        raise ToolError(f"La serie {codigo} no tiene datos entre {desde} y {hasta}; "
                        f"hay datos desde {ficha['inicio']}.")
    resultado = {"codigo": codigo, "nombre": ficha["nombre"], "frecuencia": frecuencia, "datos": datos, "fuente": url}
    if guardar:
        archivo = RAIZ / "salidas" / f"bcrp_serie_{codigo}.csv"
        archivo.parent.mkdir(exist_ok=True)
        pd.DataFrame(datos).assign(codigo=codigo, nombre=ficha["nombre"], frecuencia=frecuencia, fuente=url).to_csv(
            archivo, index=False, encoding="utf-8")
        resultado["archivo"] = archivo.relative_to(RAIZ).as_posix()
    return resultado


# TODO 2 · resumen: reutiliza serie, de modo que las operaciones las realiza Python y no el modelo.
@mcp.tool(annotations=SOLO_LECTURA)
def resumen(codigo: str, desde: str, hasta: str) -> dict:
    """Resume una serie del BCRP en un periodo: primer y último dato, cambio, variación %, promedio, máximo y mínimo.

    Se debe usar para preguntas como «cuánto subió», «cuál fue el promedio» o «cuándo fue el máximo», así como para
    leer un solo dato (desde = hasta). Las fechas siguen el formato de serie: "2025-01", "2025-01-15", "2025-T1" o
    "2025". Debe tenerse en cuenta que, si la serie ya es una tasa en % (por ejemplo, la inflación), el cambio está
    expresado en puntos porcentuales, mientras que variacion_pct es la variación relativa de dicha tasa, que casi
    nunca es lo que se pregunta.
    """
    s = serie(codigo, desde, hasta)
    df = pd.DataFrame(s["datos"])
    primero, ultimo = df.iloc[0], df.iloc[-1]
    maximo, minimo = df.loc[df.valor.idxmax()], df.loc[df.valor.idxmin()]
    dato = lambda fila: {"periodo": fila.periodo, "valor": float(fila.valor)}
    return {"codigo": codigo, "nombre": s["nombre"], "frecuencia": s["frecuencia"], "n": len(df),
            "primero": dato(primero), "ultimo": dato(ultimo),
            "cambio": round(ultimo.valor - primero.valor, 4),
            "variacion_pct": round((ultimo.valor / primero.valor - 1) * 100, 2) if primero.valor else None,
            "promedio": round(df.valor.mean(), 4), "maximo": dato(maximo), "minimo": dato(minimo),
            "fuente": s["fuente"]}


# TODO 3 · Herramienta propia: calcula la correlación entre dos series en los periodos que tienen en común.
@mcp.tool(annotations=SOLO_LECTURA)
def correlacion(codigo_a: str, codigo_b: str, desde: str, hasta: str) -> dict:
    """Correlación de Pearson entre dos series del BCRP de la misma frecuencia, en los periodos que tienen en común.

    Se debe usar cuando se pregunte si dos indicadores se mueven juntos o en sentido contrario, como por ejemplo la
    inflación (PN01273PM) y la tasa de referencia (PD04722MM) entre "2022-01" y "2026-09". El resultado va de -1 a
    1: un valor cercano a 1 indica que ambas series suben juntas, uno cercano a -1 indica que una sube cuando la
    otra baja, y uno cercano a 0 indica que no hay relación lineal. Sin embargo, debe considerarse que correlación
    no implica causalidad. Las fechas siguen el formato de serie, y la respuesta incluye las URL de ambas fuentes.
    """
    a, b = serie(codigo_a, desde, hasta), serie(codigo_b, desde, hasta)
    if a["frecuencia"] != b["frecuencia"]:
        raise ToolError(f"{codigo_a} es {a['frecuencia'].lower()} y {codigo_b} es {b['frecuencia'].lower()}: "
                        "se deben elegir dos series de la misma frecuencia (buscar_series permite filtrar por "
                        "frecuencia).")
    df = pd.DataFrame(a["datos"]).merge(pd.DataFrame(b["datos"]), on="periodo", suffixes=("_a", "_b"))
    if len(df) < 3:
        raise ToolError(f"{codigo_a} y {codigo_b} solo comparten {len(df)} periodos entre {desde} y {hasta}; "
                        "se requieren 3 o más.")
    r = round(df.valor_a.corr(df.valor_b), 3)
    fuerza = "fuerte" if abs(r) >= 0.7 else "moderada" if abs(r) >= 0.4 else "débil"
    return {"serie_a": {"codigo": codigo_a, "nombre": a["nombre"]},
            "serie_b": {"codigo": codigo_b, "nombre": b["nombre"]},
            "periodos": len(df), "desde": df.periodo.iloc[0], "hasta": df.periodo.iloc[-1],
            "correlacion": r, "lectura": f"correlación {fuerza} {'positiva' if r >= 0 else 'negativa'}",
            "fuentes": [a["fuente"], b["fuente"]]}


# Herramienta propia de la Tarea 4 · departamentos: las series regionales del BCRP solo traen el nombre del
# departamento, por lo que se les asigna el código de ubigeo (FIRST_IDDP del GeoJSON del curso) para poder unirlas
# con la ENAHO por código y no por nombre. El Gobierno Regional de Lima y la Municipalidad Metropolitana de Lima se
# mantienen separados: Lima Provincias (15LP) y Lima Metropolitana (15LM).
GEOJSON = RAIZ / "datos" / "peru_departamental_simple.geojson"
LIMA_METROPOLITANA = {"municip. metrop. de lima", "municipalidad metropolitana de lima", "lima metropolitana"}
ALIAS = {"cuzco": "cusco"}
NO_TERRITORIALES = {"total", "lima y callao", "no registrado", "por asignar", "extranjero", "otros", "ajustes"}


@cache
def _codigos_departamento():
    """Nombre sin tildes -> código de 2 dígitos, leído del GeoJSON departamental (25 unidades)."""
    geo = json.loads(GEOJSON.read_text(encoding="utf-8"))
    return {_sin_tildes(f["properties"]["NOMBDEP"]): str(f["properties"]["FIRST_IDDP"]).zfill(2)
            for f in geo["features"]}


def _grupos_departamentales():
    """Series anuales con geografía regional, con el lugar y la medida separados del nombre."""
    df = catalogo()
    r = df[(df.frecuencia == "Anual") & (df["Geografía (País, Región de Perú)"] == "RE")].copy()
    r["lugar"] = r.nombre.str.replace(r"\s*\(.*\)\s*$", "", regex=True).str.strip()
    r["medida"] = r.nombre.str.extract(r"\(([^()]*)\)\s*$", expand=False).fillna("")
    return r


def _territorio(lugar, hay_lima_metropolitana):
    """Devuelve (código, nombre) del territorio, o None si la serie no corresponde a un departamento."""
    clave = ALIAS.get(_sin_tildes(lugar), _sin_tildes(lugar))
    if clave in LIMA_METROPOLITANA:
        return "15LM", "Lima Metropolitana"
    if clave == "lima provincias" or (clave == "lima" and hay_lima_metropolitana):
        return "15LP", "Lima Provincias"
    codigo = _codigos_departamento().get(clave)
    return (codigo, lugar) if codigo else None


@mcp.tool(annotations={"readOnlyHint": False, "openWorldHint": True})
def departamentos(grupo: str, anio: str, medida: str | None = None, guardar: bool = True) -> dict:
    """Valor de un indicador regional del BCRP en cada departamento del Perú, con su código de ubigeo, para un año.

    Se debe usar para comparar departamentos o para cruzar el BCRP con la ENAHO por código de departamento
    (ubigeo[:2]). grupo son palabras del grupo de series anuales, por ejemplo "gastos gobiernos regionales",
    "gastos gobiernos locales", "credito directo departamentos" o "depositos departamentos"; el recurso
    bcrp://grupos-departamentales los lista todos. medida elige la unidad cuando el grupo trae varias, por ejemplo
    "millones de soles" o "total". anio es el año, por ejemplo "2024".

    Cada territorio llega con codigo_territorio: "01" a "25" (el de FIRST_IDDP del mapa del curso) o, cuando el
    grupo distingue a la Municipalidad Metropolitana de Lima, "15LM" (Lima Metropolitana) y "15LP" (Gobierno
    Regional de Lima, es decir, Lima Provincias), que se mantienen separados. En el gasto de gobiernos regionales,
    15LM es solo el gasto que el BCRP registra para la Municipalidad Metropolitana de Lima dentro de ese grupo; la
    herramienta no informa qué otras entidades gastan en Lima Metropolitana, por lo que no debe suponerse. Con guardar=True escribe además
    salidas/bcrp_departamentos_<grupo>_<anio>.csv para que los scripts usen las mismas cifras. Si faltan
    departamentos, se informan en «faltan»; no se deben completar a mano.
    """
    r = _grupos_departamentales()
    palabras = _sin_tildes(grupo).split()
    texto_grupo = r.grupo.map(_sin_tildes)
    m = pd.Series(True, index=r.index)
    for palabra in palabras:
        m &= texto_grupo.str.contains(re.escape(palabra))
    candidatos = sorted(r[m].grupo.unique())
    if not candidatos:
        raise ToolError(f"No hay un grupo de series anuales por departamento que contenga {grupo!r}. "
                        "Se pueden consultar los grupos disponibles en el recurso bcrp://grupos-departamentales.")
    if len(candidatos) > 1:
        raise ToolError(f"{grupo!r} coincide con {len(candidatos)} grupos; se debe precisar cuál: {candidatos[:8]}")
    sel = r[r.grupo == candidatos[0]]
    medidas = sorted(set(sel.medida) - {""})
    if medida:
        sel = sel[sel.medida.map(_sin_tildes) == _sin_tildes(medida)]
        if sel.empty:
            raise ToolError(f"La medida {medida!r} no existe en este grupo; las disponibles son {medidas}.")
    elif len(medidas) > 1:
        raise ToolError(f"El grupo trae varias medidas {medidas}; se debe elegir una con el parámetro medida.")

    hay_lm = sel.lugar.map(_sin_tildes).isin(LIMA_METROPOLITANA).any()
    filas, excluidas = [], []
    for f in sel.itertuples():
        t = _territorio(f.lugar, hay_lm)
        if t is None:
            excluidas.append(f"{f.lugar} ({f.codigo})")
        else:
            filas.append({"codigo_territorio": t[0], "territorio": t[1], "codigo_serie": f.codigo})
    if not filas:
        raise ToolError(f"El grupo {candidatos[0]!r} no tiene series por departamento.")
    repetidos = pd.Series([f["codigo_territorio"] for f in filas]).duplicated()
    if repetidos.any():
        raise ToolError(f"El grupo {candidatos[0]!r} trae varias series para un mismo departamento; "
                        "se debe elegir la medida con el parámetro medida.")

    anio = str(anio).strip()[:4]
    codigos = [f["codigo_serie"] for f in filas]
    url = f"{API}/{'-'.join(codigos)}/json/{anio}/{anio}"
    periodos = [p for p in _pedir(url).get("periods", []) if p["name"] == anio]
    if not periodos:
        raise ToolError(f"El BCRP no tiene datos de {candidatos[0]!r} para {anio}.")
    valores = periodos[0]["values"]
    for fila, v in zip(filas, valores):
        fila["valor"] = None if v == "n.d." else round(float(v), 4)
    sin_dato = [f["territorio"] for f in filas if f["valor"] is None]
    esperados = set(_codigos_departamento().values())
    if hay_lm:
        esperados = (esperados - {"15"}) | {"15LM", "15LP"}
    faltan = sorted(esperados - {f["codigo_territorio"] for f in filas})
    filas.sort(key=lambda f: f["codigo_territorio"])

    total, url_total = None, None   # la serie «Total» del BCRP sirve para comprobar que no se perdió ningún dato
    fila_total = sel[sel.lugar.map(_sin_tildes) == "total"]
    if not fila_total.empty:
        url_total = f"{API}/{fila_total.codigo.iloc[0]}/json/{anio}/{anio}"
        p = _pedir(url_total).get("periods", [])
        if p and p[0]["values"][0] != "n.d.":
            total = round(float(p[0]["values"][0]), 4)
    suma = round(sum(f["valor"] for f in filas if f["valor"] is not None), 4)

    archivo = None
    if guardar:
        nombre = re.sub(r"[^a-z0-9]+", "_", _sin_tildes(candidatos[0]))[:50].strip("_")
        archivo = RAIZ / "salidas" / f"bcrp_departamentos_{nombre}_{anio}.csv"
        archivo.parent.mkdir(exist_ok=True)
        pd.DataFrame(filas).assign(grupo=candidatos[0], medida=medida or "".join(medidas), anio=anio,
                                   fuente=url).to_csv(archivo, index=False, encoding="utf-8")
        archivo = archivo.relative_to(RAIZ).as_posix()
    return {"grupo": candidatos[0], "medida": medida or "".join(medidas), "anio": anio, "n": len(filas),
            "territorios": filas, "suma": suma, "total_bcrp": total, "faltan": faltan, "sin_dato": sin_dato,
            "excluidas": excluidas, "archivo": archivo, "fuente": url, "fuente_total": url_total}


# TODO 4 · Recurso: al tratarse de una plantilla, se obtiene un recurso por cada una de las 17,167 series.
@mcp.resource("bcrp://serie/{codigo}")
def ficha(codigo: str) -> dict:
    """Ficha de una serie del BCRP: nombre, categoría, frecuencia, desde cuándo hay datos y última actualización."""
    return {**_ficha(codigo), "fuente": URL_CATALOGO}


@mcp.resource("bcrp://grupos-departamentales")
def grupos_departamentales() -> list[dict]:
    """Grupos de series anuales del BCRP con un dato por departamento, sus medidas y hasta qué año hay datos."""
    r = _grupos_departamentales()
    r = r.assign(fin=catalogo().loc[r.index, "Fecha de fin"])
    return [{"grupo": g, "series": len(s), "medidas": sorted(set(s.medida) - {""}), "hasta": s.fin.max()}
            for g, s in r.groupby("grupo")]


# TODO 5 · Prompt: una plantilla de instrucciones reutilizable, que se lanza con /mcp__bcrp__informe.
@mcp.prompt
def informe(tema: str) -> str:
    """Informe de cinco viñetas sobre un tema económico, con cifras verificables del BCRP."""
    return (f"Escribe 5 viñetas sobre «{tema}» con datos oficiales del BCRP. Busca las series con buscar_series "
            "y saca cada cifra con resumen o serie, sin hacer cuentas a mano. En cada viñeta cita el código de la "
            "serie, el periodo y la URL de la fuente.")


@mcp.prompt
def investigacion(pregunta: str) -> str:
    """Plan de investigación que combina las series del BCRP con la ENAHO 2024 y termina en un informe verificable."""
    return (f"Pregunta de investigación: «{pregunta}».\n"
            "1. Escribe primero un plan breve: qué series del BCRP y qué indicadores de la ENAHO se necesitan.\n"
            "2. Del BCRP: busca los códigos con buscar_series; usa resumen para la evolución nacional y "
            "departamentos para los datos por departamento. No calcules a mano.\n"
            "3. De la ENAHO: usa las skills limpiando-enaho, graficando-enaho y mapeando-enaho; el cruce de "
            "ambas fuentes se hace con la skill investigando-peru, por código de departamento.\n"
            "4. Cita en cada cifra la serie del BCRP (código y periodo) o el archivo de salidas/ del que sale. Si "
            "una herramienta falla o no hay datos, dilo; no inventes cifras ni afirmes causalidad.")


if __name__ == "__main__":
    mcp.run()
