#!/usr/bin/env python3
"""Gancho Stop: antes de cerrar, obliga a decidir las observaciones pendientes.

Lee OBSERVACIONES.md. Toda línea del registro ("- AAAA-MM-DD ...") que no tenga "→ decidido"
está pendiente. Si hay pendientes, frena el cierre (decision: block) y le dice a Claude qué
reglas aplicar. Si no hay, deja cerrar. Para no entrar en un círculo, si el gancho ya frenó
una vez en este cierre (stop_hook_active), deja cerrar.
"""
import json
import os
import re
import sys

REGLAS = (
    "Aplicá las reglas: 2 veces o más → habilidad; 1 vez con 'siempre'/'cada vez'/'de ahora en más'/"
    "'no me hagas repetir' → habilidad; corrección de formato → regla en CLAUDE.md; herramienta nueva → "
    "'Anticipación' de TABLERO.md + esqueleto con estado 'pendiente de conexión'; si nada cumple → "
    "'sin habilidades nuevas'. Después agregá '→ decidido: ...' al final de cada línea, avisale a Martin "
    "en una línea cada habilidad creada o cambiada, y escribí en 'Mensajes entre asistentes' de TABLERO.md "
    "qué hiciste y qué queda."
)


def main():
    try:
        datos = json.load(sys.stdin)
    except Exception:
        datos = {}
    if datos.get("stop_hook_active"):
        return
    raiz = os.environ.get("CLAUDE_PROJECT_DIR") or datos.get("cwd") or "."
    ruta = os.path.join(raiz, "OBSERVACIONES.md")
    if not os.path.exists(ruta):
        return
    pendientes = [l.strip() for l in open(ruta, encoding="utf-8")
                  if re.match(r"-\s*\d{4}-\d{2}-\d{2}", l.strip()) and "→ decidido" not in l]
    if not pendientes:
        return
    motivo = ("Antes de cerrar: hay %d observaciones sin decidir en OBSERVACIONES.md:\n%s\n%s"
              % (len(pendientes), "\n".join(pendientes[:10]), REGLAS))
    print(json.dumps({"decision": "block", "reason": motivo}, ensure_ascii=False))


if __name__ == "__main__":
    main()
