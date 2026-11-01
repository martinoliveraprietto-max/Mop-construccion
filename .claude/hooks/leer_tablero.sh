#!/bin/bash
# Gancho SessionStart (Cerebro MOP, 1-nov-2026): muestra el cartel CALIENTE.md entero.
# Claude Code solo deja ver los primeros 2 KB de lo que imprime un gancho; antes se mostraban
# HABILIDADES.md y TABLERO.md (16 KB) y el tablero no llegaba. Ahora va solo lo caliente y
# el resto se busca en la memoria (python3 -m herramientas.memoria buscar <nombre>).
cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
echo "=== Hoy: $(TZ=America/New_York date '+%A %d-%m-%Y %H:%M') (Miami) ==="
echo "Regla: decir en tres líneas qué vence hoy, qué está trabado y qué habilidades hay activas."
[ -f CALIENTE.md ] && cat CALIENTE.md
if [ -f HABILIDADES.md ]; then
  activas=$(grep -c '^- .* · activa' HABILIDADES.md)
  echo "Habilidades activas: $activas (lista en HABILIDADES.md). Tablero completo: TABLERO.md, solo si hace falta."
fi
exit 0
