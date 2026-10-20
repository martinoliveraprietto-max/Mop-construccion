#!/bin/bash
# Respaldo nocturno del Google Drive de MOP al OneDrive de MOP (pedido de Martin, 20-oct-2026).
# Corre en el servidor con rclone. Pasos de instalación: herramientas/respaldo_onedrive.md.
#
# - El Drive se lee con permiso de SOLO LECTURA (remoto "mopdrive"): este programa no puede borrar
#   ni cambiar nada en Google.
# - En OneDrive (remoto "onedrive") la copia queda en "Respaldo MOP Drive/actual". Lo que se borra o
#   se cambia en Drive no se pierde: la versión vieja pasa a "Respaldo MOP Drive/borrados/<fecha>".
# - Los documentos de Google se guardan como Word, Excel y PowerPoint.
# - Pocas transferencias a la vez y prioridad baja: el servidor es compartido con los bots.
set -uo pipefail

DESTINO="onedrive:Respaldo MOP Drive"
FECHA="$(date +%Y-%m-%d)"
REGISTRO="$HOME/respaldo_onedrive/registro.txt"
mkdir -p "$(dirname "$REGISTRO")"

{
  echo "=== $(date '+%Y-%m-%d %H:%M') comienza ==="
  nice -n 19 rclone sync "mopdrive:" "$DESTINO/actual" \
    --backup-dir "$DESTINO/borrados/$FECHA" \
    --drive-export-formats docx,xlsx,pptx,pdf \
    --transfers 2 --checkers 4 \
    --stats-one-line --stats 0 --log-level NOTICE
  echo "=== $(date '+%Y-%m-%d %H:%M') termina con código $? ==="
} >> "$REGISTRO" 2>&1

# El registro guarda solo las últimas 2000 líneas.
tail -n 2000 "$REGISTRO" > "$REGISTRO.tmp" && mv "$REGISTRO.tmp" "$REGISTRO"
