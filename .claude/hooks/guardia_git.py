#!/usr/bin/env python3
"""Gancho PreToolUse (Bash) de Claude Code para el repositorio PÚBLICO de MOP.

Antes de `git commit` o `git push`:
  1. Corre `python3 pruebas/prueba_sitio.py` (sin dependencias, tarda segundos) y frena
     si falla: datos exactos, palabras prohibidas, fotos sin GPS, imágenes que existan.
     Lo que se sube a main queda publicado en GitHub Pages.
  2. Frena si lo preparado para el commit contiene el valor de INSTAGRAM_TOKEN o de otra
     variable de entorno terminada en _TOKEN, _KEY o _SECRET.
  3. Frena si se prepara basura de Python (__pycache__, .pyc).

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
        preparados = correr(["git", "diff", "--cached", "--name-only"], raiz).stdout.split()
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


if __name__ == "__main__":
    main()
