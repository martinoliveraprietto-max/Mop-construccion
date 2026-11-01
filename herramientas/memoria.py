"""Cerebro MOP: fichas y hechos en Supabase, y el cartel CALIENTE.md (plan en CEREBRO_MOP.md).

Aprobado por Martin el 1-nov-2026 ("hacé todo hoy"). Las tablas viven en Supabase (proyecto
mop-estimador), privadas, sin políticas; las crea supabase/migrations/20261101190000_memoria.sql.

Uso (cada comando imprime el SQL para la herramienta execute_sql de Supabase):
  python3 -m herramientas.memoria buscar "kilwins"            busca fichas y sus 5 hechos
  python3 -m herramientas.memoria ficha NOMBRE --tipo obra [--resumen R] [--estado E]
          [--proximo P] [--vence AAAA-MM-DD] [--alias A ...] --fuente F
                                                              crea o pisa una ficha
  python3 -m herramientas.memoria anotar NOMBRE "texto" --fuente F --quien Q [--tipo obra]
                                                              agrega un hecho (y la ficha si falta)
  python3 -m herramientas.memoria revisar                     fichas vencidas, sin fuente o viejas
  python3 -m herramientas.memoria caliente --sql              consulta para armar el cartel
  python3 -m herramientas.memoria caliente --filas f.json [--escribir]
                                                              arma CALIENTE.md (2 KB como máximo)

Solo usa la biblioteca estándar. Nunca escribe datos de clientes en el repositorio: el cartel
lleva nombres, estados y fechas, como TABLERO.md, sin montos, correos ni teléfonos.
"""
import argparse
import datetime as dt
import json
import os
import sys
from zoneinfo import ZoneInfo

MIAMI = ZoneInfo("America/New_York")
TIPOS = ("obra", "constructora", "proveedor", "bot", "tramite", "persona", "proyecto", "sistema")
TOPE_BYTES = 1900  # el gancho de inicio solo deja ver 2 KB; el resto se corta
DIAS_VIEJA = 30
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def q(valor):
    if valor is None or valor == "":
        return "null"
    return "'" + str(valor).replace("'", "''") + "'"


def arreglo(valores):
    return "array[%s]::text[]" % ", ".join(q(v) for v in valores) if valores else "'{}'::text[]"


def sql_buscar(texto, cuantos=5):
    return "select * from public.memoria_buscar(%s, %d);" % (q(texto), cuantos)


def sql_ficha(nombre, tipo, fuente, resumen=None, estado=None, proximo=None, vence=None,
              alias=None):
    if tipo not in TIPOS:
        raise ValueError("tipo desconocido: %s (vale: %s)" % (tipo, ", ".join(TIPOS)))
    if resumen and len(resumen) > 600:
        raise ValueError("el resumen pasa los 600 caracteres: achicarlo")
    columnas = {"nombre": q(nombre), "tipo": q(tipo), "fuente": q(fuente)}
    for clave, valor in (("resumen", resumen), ("estado", estado), ("proximo", proximo),
                         ("vence", vence)):
        if valor is not None:
            columnas[clave] = q(valor)
    if alias:
        columnas["alias"] = arreglo(alias)
    nombres = ", ".join(columnas)
    valores = ", ".join(columnas.values())
    pisar = ", ".join("%s = excluded.%s" % (c, c) for c in columnas if c != "nombre")
    return ("insert into public.memoria_fichas (%s) values (%s) on conflict (nombre) do update "
            "set %s;" % (nombres, valores, pisar))


def sql_anotar(nombre, texto, fuente, quien, tipo="proyecto"):
    """Agrega un hecho. Si la ficha no existe la crea vacía (tipo dado); si existe, solo
    le marca la fecha de actualización."""
    return ("with f as (insert into public.memoria_fichas (nombre, tipo, fuente) values "
            "(%s, %s, %s) on conflict (nombre) do update set actualizado = now() "
            "returning id) insert into public.memoria_hechos (ficha_id, texto, fuente, quien) "
            "select id, %s, %s, %s from f;"
            % (q(nombre), q(tipo), q(fuente), q(texto), q(fuente), q(quien)))


SQL_REVISAR = (
    "select nombre, tipo, estado, vence, fuente, actualizado, "
    "case when vence is not null and vence < current_date then 'vencida' "
    "when fuente is null or fuente = '' then 'sin fuente' "
    "when actualizado < now() - interval '%d days' then 'vieja' end as problema "
    "from public.memoria_fichas where tipo <> 'sistema' and ("
    "(vence is not null and vence < current_date) or fuente is null or fuente = '' "
    "or actualizado < now() - interval '%d days') order by problema, vence nulls last;"
    % (DIAS_VIEJA, DIAS_VIEJA))

SQL_CALIENTE = (
    "select tipo, nombre, estado, proximo, vence from public.memoria_fichas "
    "where tipo <> 'sistema' and (vence <= current_date + 7 or estado ilike '%espera%' "
    "or estado ilike '%trabad%' or estado ilike '%decid%') order by vence nulls last, nombre;")


def cargar_filas(archivo):
    with open(archivo, encoding="utf-8") as a:
        datos = json.load(a)
    if isinstance(datos, dict):
        datos = datos.get("result") or datos.get("rows") or []
    return datos


def fecha_corta(valor):
    if not valor:
        return ""
    f = dt.date.fromisoformat(str(valor)[:10])
    return "%d-%d" % (f.day, f.month)


def recortar(texto, largo):
    texto = " ".join(str(texto or "").split())
    return texto if len(texto) <= largo else texto[:largo - 1].rstrip() + "…"


def armar_caliente(filas, ahora=None, decisiones=None):
    """Cartel de 2 KB como máximo: vence en 7 días, esperan a Martin, bots y decisiones."""
    ahora = ahora or dt.datetime.now(MIAMI)
    hoy = ahora.date()
    cabeza = ["# CALIENTE — lo urgente de hoy (Cerebro MOP)",
              "Armado el %s de Miami. Detalle: `python3 -m herramientas.memoria buscar <nombre>` "
              "(Supabase). Plan: CEREBRO_MOP.md." % ahora.strftime("%d-%m-%Y %H:%M"), ""]
    vence, espera, bots = [], [], []
    for f in filas:
        nombre = f.get("nombre", "")
        linea = "- %s: %s" % (nombre, recortar(f.get("proximo") or f.get("estado"), 90))
        v = f.get("vence")
        if f.get("tipo") == "bot":
            bots.append("- %s: %s" % (nombre, recortar(f.get("estado"), 90)))
        elif v and dt.date.fromisoformat(str(v)[:10]) <= hoy + dt.timedelta(days=7):
            atraso = " (VENCIDA)" if dt.date.fromisoformat(str(v)[:10]) < hoy else ""
            vence.append("- %s %s%s: %s" % (fecha_corta(v), nombre, atraso,
                                            recortar(f.get("proximo") or f.get("estado"), 80)))
        else:
            espera.append(linea)
    # Cada bloque tiene su cupo, para que lo que vence no tape a los bots ni a las decisiones.
    bloques = [("## Vence en 7 días", vence, 7), ("## Esperando (a Martin o al cliente)", espera, 5),
               ("## Bots", bots, 3), ("## Últimas decisiones", decisiones or [], 5)]
    mas = "- (hay más: buscar en la memoria)\n"
    texto = "\n".join(cabeza)
    for titulo, lineas, cupo in bloques:
        if not lineas:
            continue
        parte = "\n" + titulo + "\n"
        if len((texto + parte + mas).encode()) > TOPE_BYTES:
            break
        for i, l in enumerate(lineas):
            if i == cupo or len((texto + parte + l + "\n" + mas).encode()) > TOPE_BYTES:
                parte += mas
                break
            parte += l + "\n"
        texto += parte
    return texto.rstrip() + "\n"


def main(argv=None):
    p = argparse.ArgumentParser(prog="herramientas.memoria", description=__doc__.split("\n")[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("buscar")
    b.add_argument("texto")
    b.add_argument("--cuantos", type=int, default=5)
    f = sub.add_parser("ficha")
    f.add_argument("nombre")
    f.add_argument("--tipo", required=True, choices=TIPOS)
    f.add_argument("--fuente", required=True)
    for c in ("resumen", "estado", "proximo", "vence"):
        f.add_argument("--" + c)
    f.add_argument("--alias", nargs="*")
    a = sub.add_parser("anotar")
    a.add_argument("nombre")
    a.add_argument("texto")
    a.add_argument("--fuente", required=True)
    a.add_argument("--quien", required=True)
    a.add_argument("--tipo", default="proyecto", choices=TIPOS)
    sub.add_parser("revisar")
    c = sub.add_parser("caliente")
    c.add_argument("--sql", action="store_true")
    c.add_argument("--filas")
    c.add_argument("--decision", action="append", default=[],
                   help="línea de decisión reciente (repetible, máximo 5)")
    c.add_argument("--escribir", action="store_true", help="guarda CALIENTE.md en la raíz")
    args = p.parse_args(argv)

    if args.cmd == "buscar":
        print(sql_buscar(args.texto, args.cuantos))
    elif args.cmd == "ficha":
        print(sql_ficha(args.nombre, args.tipo, args.fuente, args.resumen, args.estado,
                        args.proximo, args.vence, args.alias))
    elif args.cmd == "anotar":
        print(sql_anotar(args.nombre, args.texto, args.fuente, args.quien, args.tipo))
    elif args.cmd == "revisar":
        print(SQL_REVISAR)
    elif args.cmd == "caliente":
        if args.sql or not args.filas:
            print(SQL_CALIENTE)
            return 0 if args.sql else 2
        texto = armar_caliente(cargar_filas(args.filas),
                               decisiones=["- " + d for d in args.decision[:5]])
        if args.escribir:
            with open(os.path.join(RAIZ, "CALIENTE.md"), "w", encoding="utf-8") as s:
                s.write(texto)
        print(texto, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
