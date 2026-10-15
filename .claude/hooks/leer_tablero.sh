#!/bin/bash
# Gancho SessionStart: muestra HABILIDADES.md y TABLERO.md para que Claude arranque sabiendo qué vence,
# qué está trabado y qué habilidades hay activas (regla de CLAUDE.md).
cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
echo "=== Hoy: $(TZ=America/New_York date '+%A %d-%m-%Y %H:%M') (Miami) ==="
echo "Regla: decir en tres líneas qué vence hoy, qué está trabado y qué habilidades hay activas."
for f in HABILIDADES.md TABLERO.md; do
  [ -f "$f" ] && { echo; echo "=== $f ==="; head -c 12000 "$f"; }
done
exit 0
