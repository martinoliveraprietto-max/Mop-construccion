#!/bin/bash
# Gancho SessionStart de Claude Code: en la nube, deja listas las herramientas que usa este
# repositorio en cada sesión nueva (en la tableta las maneja Martin).
#   pillow + imageio-ffmpeg: fotos y reels (scripts/hacer_reel.py). Todo gratis.
#   yt-dlp: leer los subtítulos de los videos de YouTube que manda Martin.
#   playwright-core: pruebas/prueba_navegador.js (usa el Chromium que ya trae la nube).
set -uo pipefail
[ "${CLAUDE_CODE_REMOTE:-}" != "true" ] && exit 0

FALLARON=""
for p in pillow imageio-ffmpeg yt-dlp; do
  python3 -m pip show -q "$p" >/dev/null 2>&1 && continue
  python3 -m pip install -q --disable-pip-version-check --root-user-action=ignore "$p" \
    >>/tmp/instalar_mop.log 2>&1 || FALLARON="$FALLARON $p"
done
if ! node -e "require.resolve('playwright-core')" >/dev/null 2>&1; then
  (cd "${CLAUDE_PROJECT_DIR:-.}" && npm install --no-save --silent playwright-core \
    >>/tmp/instalar_mop.log 2>&1) || FALLARON="$FALLARON playwright-core"
fi

if [ -n "$FALLARON" ]; then
  echo "NO se pudo instalar:$FALLARON (detalle en /tmp/instalar_mop.log)."
  exit 1
fi
echo "Herramientas de MOP listas: pillow, imageio-ffmpeg, yt-dlp, playwright-core."
exit 0
