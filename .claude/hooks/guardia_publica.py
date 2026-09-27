#!/usr/bin/env python3
"""Gancho PreToolUse (Edit|Write) de Claude Code para el repositorio PÚBLICO de MOP.

Frena, antes de que Claude escriba un archivo, lo que no puede quedar a la vista de todos
(reglas de CLAUDE.md):
  1. Palabras que implican licencia o tamaño de empresa: "licensed", "general contractor",
     "crew", "cuadrilla", "employees", "empleados", "roofing", "techado".
  2. Cualquier dirección de calle en Dania Beach o la ciudad de Hialeah (la web muestra
     solo "Dania Beach, FL", sin calle). No se escribe acá ninguna dirección concreta: el
     patrón es genérico a propósito, porque este archivo también es público.
  3. El valor del token de Instagram (variable INSTAGRAM_TOKEN) o de cualquier variable de
     entorno terminada en _TOKEN, _KEY o _SECRET.
Quedan afuera CLAUDE.md, .claude/ y pruebas/: nombran esas palabras justamente para prohibirlas.

Formato (code.claude.com/docs/en/hooks): entra JSON por stdin con tool_name y tool_input;
salir con código 2 frena la herramienta y lo escrito en stderr le llega a Claude.
"""
import json
import os
import re
import sys

PROHIBIDAS = ["licensed", "general contractor", "crew", "cuadrilla", "employees",
              "empleados", "roofing", "techado", "hialeah"]
# Una calle en Dania Beach: número + nombre + tipo de calle, o el bulevar por nombre.
CALLE = re.compile(r"\b\d{2,6}\s+[NSEW]?\.?\s*[A-Za-z0-9 .]{2,30}\b(St|Street|Ave|Avenue|Blvd|"
                   r"Boulevard|Rd|Road|Dr|Drive|Ct|Court|Ter|Terrace|Way|Ln|Lane)\b[^\n]{0,40}"
                   r"Dania", re.I)
BULEVAR = re.compile(r"dania\s+beach\s+blvd", re.I)


def frenar(motivo):
    sys.stderr.write("GUARDIA (.claude/hooks/guardia_publica.py): " + motivo + "\n")
    sys.exit(2)


def main():
    try:
        datos = json.load(sys.stdin)
    except Exception:
        return
    ti = datos.get("tool_input") or {}
    ruta = (ti.get("file_path") or "").replace("\\", "/")
    raiz = (os.environ.get("CLAUDE_PROJECT_DIR") or datos.get("cwd") or "").replace("\\", "/")
    relativa = ruta[len(raiz):].lstrip("/") if raiz and ruta.startswith(raiz) else ruta
    if relativa == "CLAUDE.md" or relativa.startswith((".claude/", "pruebas/")):
        return
    nuevo = (ti.get("content") or "") + "\n" + (ti.get("new_string") or "")
    viejo = ti.get("old_string") or ""
    minus = nuevo.lower()

    for var, valor in os.environ.items():
        if re.search(r"(_TOKEN|_KEY|_SECRET)$", var) and valor and len(valor) >= 16 \
                and valor in nuevo:
            frenar("el texto contiene el valor de %s. Este repositorio es público: los "
                   "tokens viven solo en el entorno." % var)

    for palabra in PROHIBIDAS:
        # Solo frena si la palabra es NUEVA (no si ya estaba en el tramo que se reemplaza).
        if re.search(r"\b%s\b" % re.escape(palabra), minus) and \
                not re.search(r"\b%s\b" % re.escape(palabra), viejo.lower()):
            frenar("«%s» no puede aparecer en el sitio ni en Instagram (CLAUDE.md: MOP no "
                   "tiene licencia de contratista, no se habla de cuadrilla ni de empleados, "
                   "no se ofrece techado y nunca se muestra Hialeah)." % palabra)

    if (CALLE.search(nuevo) or BULEVAR.search(nuevo)) and not (
            CALLE.search(viejo) or BULEVAR.search(viejo)):
        frenar("parece una dirección de calle en Dania Beach. La web muestra solo la ciudad "
               "(«Dania Beach, FL»); la dirección de la casa de Martin nunca va en este "
               "repositorio público.")


if __name__ == "__main__":
    main()
