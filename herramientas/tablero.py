"""Tabla "tablero" de Supabase → sección "2. Sistema de asistentes" del TABLERO de Martin.

Pedido de Martin (19-oct-2026). Cada tarea programada (cazador, vigilante, bandeja,
guardián) deja al terminar una fila por número o estado en la tabla public.tablero del
proyecto mop-estimador; este comando las imprime en frases cortas, listas para pegar.

Uso:
  python3 -m herramientas.tablero                    imprime la sección
  python3 -m herramientas.tablero --filas f.json     igual, con las filas ya leídas
                                                     (salida de execute_sql guardada)
  python3 -m herramientas.tablero --sql              la consulta única para execute_sql
  python3 -m herramientas.tablero poner FRENTE CLAVE VALOR --fuente F --quien Q
                                                     escribe (o pisa) una fila

Sin --filas, lee por la API de Supabase si el entorno tiene SUPABASE_SERVICE_ROLE_KEY
(la tabla no tiene políticas: la clave publicable no alcanza). Sin esa clave, imprime la
consulta para correrla con la herramienta execute_sql de Supabase y sale con código 2.
Solo usa la biblioteca estándar.
"""
import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request
from zoneinfo import ZoneInfo

URL = os.environ.get("SUPABASE_URL") or "https://sfmhdtingccfkzkwbqgt.supabase.co"
MIAMI = ZoneInfo("America/New_York")
CONSULTA = ("select frente, clave, valor, fecha, fuente, quien_escribio "
            "from public.tablero order by frente, clave;")
# Primero los frentes que pidió Martin; los demás, en orden alfabético.
ORDEN = ["cazador", "vigilante", "bandeja", "guardián"]
ATRASO_HORAS = 36


def leer_fecha(texto):
    """Acepta la fecha como la da execute_sql ('2026-10-19 15:50:00.12+00') o la API."""
    t = str(texto).strip().replace(" ", "T", 1)
    if t.endswith("Z"):
        t = t[:-1] + "+00:00"
    elif len(t) >= 3 and t[-3] in "+-" and t[-2:].isdigit():
        t += ":00"
    if "." in t:
        cabeza, resto = t.split(".", 1)
        decimales = "".join(c for c in resto if c.isdigit())
        t = cabeza + "." + (decimales + "000000")[:6] + resto[len(decimales):]
    fecha = dt.datetime.fromisoformat(t)
    if fecha.tzinfo is None:
        fecha = fecha.replace(tzinfo=dt.timezone.utc)
    return fecha


def corta(fecha):
    f = fecha.astimezone(MIAMI)
    return "%d-%d %d:%02d" % (f.day, f.month, f.hour, f.minute)


def seccion(filas, ahora=None):
    ahora = ahora or dt.datetime.now(dt.timezone.utc)
    lineas = ["2. Sistema de asistentes (tabla tablero de Supabase, leída el %s de Miami)"
              % corta(ahora)]
    if not filas:
        lineas.append("- Sin datos: ninguna tarea escribió todavía en la tabla.")
        return "\n".join(lineas)
    frentes = {}
    for f in filas:
        frentes.setdefault(f["frente"], []).append(f)
    nombres = sorted(frentes, key=lambda n: (ORDEN.index(n) if n in ORDEN else len(ORDEN), n))
    for nombre in nombres:
        grupo = sorted(frentes[nombre], key=lambda f: f["clave"])
        fechas = [leer_fecha(f["fecha"]) for f in grupo]
        ultima = max(fechas)
        quienes = sorted({f["quien_escribio"] for f in grupo})
        datos = "; ".join("%s: %s" % (f["clave"], f["valor"]) for f in grupo)
        linea = "- %s (%s, %s): %s." % (nombre.capitalize(), corta(ultima),
                                        ", ".join(quienes), datos)
        horas = (ahora - ultima).total_seconds() / 3600
        if horas > ATRASO_HORAS:
            linea += " ATRASADO: %d horas sin escribir." % horas
        viejas = [f["clave"] for f, fe in zip(grupo, fechas)
                  if (ultima - fe).total_seconds() / 3600 > ATRASO_HORAS]
        if viejas:
            linea += " Sin actualizar: %s." % ", ".join(viejas)
        fuentes = sorted({f["fuente"] for f in grupo if f.get("fuente")})
        if fuentes:
            linea += " Fuente: %s." % ", ".join(fuentes)
        lineas.append(linea)
    return "\n".join(lineas)


def texto_sql(valor):
    return "'" + str(valor).replace("'", "''") + "'"


def sql_poner(frente, clave, valor, fuente, quien):
    return ("insert into public.tablero (frente, clave, valor, fuente, quien_escribio) "
            "values (%s, %s, %s, %s, %s) on conflict (frente, clave) do update set "
            "valor = excluded.valor, fuente = excluded.fuente, "
            "quien_escribio = excluded.quien_escribio;"
            % tuple(texto_sql(x) for x in (frente, clave, valor, fuente, quien)))


def api(metodo, ruta, llave, cuerpo=None, extra=None):
    cabeceras = {"apikey": llave, "Authorization": "Bearer " + llave,
                 "Content-Type": "application/json"}
    cabeceras.update(extra or {})
    datos = json.dumps(cuerpo).encode() if cuerpo is not None else None
    pedido = urllib.request.Request(URL + "/rest/v1/" + ruta, data=datos,
                                    headers=cabeceras, method=metodo)
    with urllib.request.urlopen(pedido, timeout=30) as r:
        texto = r.read().decode()
    return json.loads(texto) if texto else None


def cargar_filas(archivo):
    with open(archivo, encoding="utf-8") as a:
        datos = json.load(a)
    # execute_sql a veces devuelve {"result": [...]} o la lista suelta.
    if isinstance(datos, dict):
        datos = datos.get("result") or datos.get("filas") or []
    return datos


def main(argv=None):
    p = argparse.ArgumentParser(prog="python3 -m herramientas.tablero",
                                description="Tabla tablero de Supabase")
    p.add_argument("--filas", help="JSON con las filas ya leídas con execute_sql")
    p.add_argument("--sql", action="store_true", help="imprime la consulta y termina")
    sub = p.add_subparsers(dest="accion")
    q = sub.add_parser("poner", help="escribe o pisa una fila")
    q.add_argument("frente")
    q.add_argument("clave")
    q.add_argument("valor")
    q.add_argument("--fuente", default="")
    q.add_argument("--quien", required=True)
    q.add_argument("--sql", action="store_true", dest="solo_sql",
                   help="solo imprime el SQL para execute_sql")
    a = p.parse_args(argv)
    llave = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")

    if a.accion == "poner":
        sql = sql_poner(a.frente, a.clave, a.valor, a.fuente, a.quien)
        if a.solo_sql or not llave:
            if not a.solo_sql:
                print("Sin SUPABASE_SERVICE_ROLE_KEY: corré esto con execute_sql de Supabase "
                      "(proyecto sfmhdtingccfkzkwbqgt):", file=sys.stderr)
            print(sql)
            return 0 if a.solo_sql else 2
        api("POST", "tablero?on_conflict=frente,clave", llave,
            {"frente": a.frente, "clave": a.clave, "valor": a.valor, "fuente": a.fuente,
             "quien_escribio": a.quien},
            {"Prefer": "resolution=merge-duplicates,return=minimal"})
        print("tablero: %s · %s = %s" % (a.frente, a.clave, a.valor))
        return 0

    if a.sql:
        print(CONSULTA)
        return 0
    if a.filas:
        filas = cargar_filas(a.filas)
    elif llave:
        filas = api("GET", "tablero?select=*&order=frente,clave", llave)
    else:
        print("Sin SUPABASE_SERVICE_ROLE_KEY. Corré esta consulta con execute_sql de Supabase "
              "(proyecto sfmhdtingccfkzkwbqgt), guardá el resultado en un .json y pasalo con "
              "--filas:\n" + CONSULTA, file=sys.stderr)
        return 2
    print(seccion(filas))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except urllib.error.HTTPError as e:
        sys.exit("tablero: Supabase respondió %s %s" % (e.code, e.reason))
