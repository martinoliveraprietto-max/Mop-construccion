#!/bin/bash
# Gancho SessionStart de Claude Code: en la nube, deja listas las herramientas que usa este
# repositorio en cada sesión nueva (en la tableta las maneja Martin).
#   pillow + imageio-ffmpeg: fotos y reels (scripts/hacer_reel.py). Todo gratis.
#   edge-tts: los audios con voz uruguaya (Mateo) que Martin pidió al final de cada respuesta.
#   yt-dlp: leer los subtítulos de los videos de YouTube que manda Martin.
#   playwright-core: pruebas/prueba_navegador.js (usa el Chromium que ya trae la nube).
set -uo pipefail
[ "${CLAUDE_CODE_REMOTE:-}" != "true" ] && exit 0

FALLARON=""
for p in pillow imageio-ffmpeg yt-dlp edge-tts; do
  python3 -m pip show -q "$p" >/dev/null 2>&1 && continue
  python3 -m pip install -q --disable-pip-version-check --root-user-action=ignore "$p" \
    >>/tmp/instalar_mop.log 2>&1 || FALLARON="$FALLARON $p"
done
if ! node -e "require.resolve('playwright-core')" >/dev/null 2>&1; then
  (cd "${CLAUDE_PROJECT_DIR:-.}" && npm install --no-save --silent playwright-core \
    >>/tmp/instalar_mop.log 2>&1) || FALLARON="$FALLARON playwright-core"
fi

# edge-tts valida con certifi, que no trae el certificado del proxy de la nube: se lo sumamos una vez.
CA=/root/.ccr/ca-bundle.crt
CERTIFI=$(python3 -c "import certifi;print(certifi.where())" 2>/dev/null)
if [ -f "$CA" ] && [ -n "$CERTIFI" ] && ! grep -qF "$(sed -n 2p "$CA")" "$CERTIFI"; then
  cat "$CA" >> "$CERTIFI"
fi

if [ -n "$FALLARON" ]; then
  echo "NO se pudo instalar:$FALLARON (detalle en /tmp/instalar_mop.log)."
  exit 1
fi
echo "Herramientas de MOP listas: pillow, imageio-ffmpeg, yt-dlp, edge-tts, playwright-core."
exit 0
