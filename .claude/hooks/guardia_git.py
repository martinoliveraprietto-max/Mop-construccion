#!/usr/bin/env python3
"""Gancho PreToolUse (Bash) de Claude Code para el repositorio PÚBLICO de MOP.

Antes de `git commit` o `git push`:
  1. Corre `python3 pruebas/prueba_sitio.py` (sin dependencias, tarda segundos) y frena
     si falla: datos exactos, palabras prohibidas, fotos sin GPS, imágenes que existan.
     Lo que se sube a main queda publicado en GitHub Pages.
  2. Frena si lo preparado para el commit contiene el valor de INSTAGRAM_TOKEN o de otra
     variable de entorno terminada en _TOKEN, _KEY o _SECRET.
  3. Frena si se prepara basura de Python (__pycache__, .pyc).
  4. Frena si las líneas agregadas traen palabras prohibidas o una dirección de calle
     (mismas reglas que guardia_publica.py, que no ve lo escrito desde Bash).

Formato (code.claude.com/docs/en/hooks): entra JSON por stdin; código 2 frena y lo escrito
en stderr le llega a Claude.
"""
import json
import os
import re
import subprocess
import sys


def frenar(motivo):
    sys.stderr.write("GUARDIA (.claude/hooks/guardia_git.py): " + motivo + "\n")
    sys.exit(2)


def correr(args, raiz, tiempo=120):
    return subprocess.run(args, cwd=raiz, capture_output=True, text=True, timeout=tiempo)


def main():
    try:
        datos = json.load(sys.stdin)
    except Exception:
        return
    cmd = (datos.get("tool_input") or {}).get("command") or ""
    raiz = os.environ.get("CLAUDE_PROJECT_DIR") or datos.get("cwd") or os.getcwd()

    # Cada tramo del comando cuenta solo si EMPIEZA con git: un `echo "git commit"` no dispara.
    es_commit = es_push = False
    for tramo in re.split(r"\|\||&&|[;|\n]", cmd):
        palabras = tramo.strip().lstrip("({").split()
        while palabras and re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", palabras[0]):
            palabras.pop(0)
        if len(palabras) >= 2 and palabras[0] == "git":
            resto = [p for p in palabras[1:] if not p.startswith("-")]
            # git -C <dir> commit: saltear la ruta que sigue a -C
            if "-C" in palabras[1:3] and len(palabras) > 3:
                resto = [p for p in palabras[3:] if not p.startswith("-")]
            if resto and resto[0] == "commit":
                es_commit = True
            if resto and resto[0] == "push":
                es_push = True
    if not (es_commit or es_push):
        return

    prueba = os.path.join(raiz, "pruebas", "prueba_sitio.py")
    if os.path.exists(prueba):
        try:
            r = correr([sys.executable, prueba], raiz)
        except subprocess.TimeoutExpired:
            frenar("pruebas/prueba_sitio.py tardó más de 2 minutos; revisarla antes de subir.")
        if r.returncode != 0:
            fallas = [l for l in r.stdout.splitlines() if "FALLA" in l][:8]
            frenar("pruebas/prueba_sitio.py falló; no se sube a la web pública:\n  "
                   + "\n  ".join(fallas or [r.stdout[-600:] or r.stderr[-600:]]))

    if es_commit:
        preparados = correr(["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"], raiz).stdout.split()
        basura = [p for p in preparados if "__pycache__" in p or p.endswith(".pyc")]
        if basura:
            frenar("hay basura de Python preparada para el commit (%s). Sacarla con "
                   "git rm --cached." % ", ".join(basura[:5]))
        diff = correr(["git", "diff", "--cached"], raiz).stdout
        for var, valor in os.environ.items():
            if re.search(r"(_TOKEN|_KEY|_SECRET)$", var) and valor and len(valor) >= 16 \
                    and valor in diff:
                frenar("lo preparado para el commit contiene el valor de %s. El repositorio "
                       "es público: sacarlo antes de seguir." % var)
        revisar_textos(correr(["git", "diff", "--cached", "-U0"], raiz).stdout)


def revisar_textos(diff):
    """Las mismas reglas de guardia_publica.py, ahora sobre lo que se sube.

    guardia_publica.py solo mira Edit y Write; lo escrito desde Bash (echo, sed, scripts)
    se le escapa. Acá se revisan las líneas agregadas de cada archivo preparado, con las
    mismas excepciones (CLAUDE.md, .claude/, pruebas/). Encontrado por Claude Setup el 19-oct.
    """
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from guardia_publica import PROHIBIDAS, CALLE, BULEVAR

    archivos = {}
    actual = None
    for linea in diff.splitlines():
        if linea.startswith("+++ "):
            ruta = linea[4:]
            actual = ruta[2:] if ruta.startswith("b/") else None
            if actual and (actual == "CLAUDE.md" or actual.startswith((".claude/", "pruebas/"))):
                actual = None
            if actual:
                archivos.setdefault(actual, ([""], [""]))
        elif linea.startswith("--- ") or not actual:
            continue
        elif linea.startswith("+"):
            archivos[actual][0].append(linea[1:])
        elif linea.startswith("-"):
            archivos[actual][1].append(linea[1:])

    for ruta, (agregadas, sacadas) in archivos.items():
        nuevo, viejo = "\n".join(agregadas), "\n".join(sacadas)
        for palabra in PROHIBIDAS:
            patron = r"\b%s\b" % re.escape(palabra)
            # Solo frena si la palabra es NUEVA en ese archivo (no si se movió de lugar).
            if re.search(patron, nuevo.lower()) and not re.search(patron, viejo.lower()):
                frenar("«%s» aparece en %s. El repositorio es público y CLAUDE.md lo prohíbe "
                       "(sin licencia de contratista, sin cuadrilla ni empleados, sin techado, "
                       "nunca Hialeah). Sacarlo antes del commit." % (palabra, ruta))
        if (CALLE.search(nuevo) or BULEVAR.search(nuevo)) and not (
                CALLE.search(viejo) or BULEVAR.search(viejo)):
            frenar("%s tiene algo que parece una dirección de calle en Dania Beach. En este "
                   "repositorio público va solo la ciudad. Sacarla antes del commit." % ruta)


if __name__ == "__main__":
    main()
