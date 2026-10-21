---
name: instagram-lectura
description: (Pendiente de conexión) Leer reels para sacar ideas de contenido: los que Martin comparte o los públicos de cuentas de empresa. Usar cuando Martin dice "mirá este reel", "leé mis guardados" o "qué publica <cuenta>".
---

# instagram-lectura

**Estado:** activa por enlace (camino 1) · **Versión:** v2 · **Fecha:** 21-oct-2026

## Cuándo se dispara
- "mirá este reel", "leé mis guardados", "qué publica <cuenta>".

## Cómo se lee un enlace (probado el 21-oct con un reel de onyaroof)
1. `yt-dlp --skip-download --write-info-json -o post <enlace>` en el scratchpad: autor, me gusta, comentarios, fecha.
2. `yt-dlp -o video.%(ext)s <enlace>` y hoja de cuadros con FFmpeg (`fps=1/3,tile=4x3`) para ver qué muestra.
3. Audio: `pip install faster-whisper`, pasar el audio como arreglo numpy (el archivo directo falla con la versión de av instalada), modelo `small`.
4. Decirle a Martin: quién es, qué vende, qué dice, si choca con las reglas de MOP y qué idea sirve para @mopconstruccion.inc.
5. REGLA (Martin, 21-oct): de cada reel buscar cómo aplicarlo en MOP (web, Instagram, mop-estimador) Y en sus bots:
   cazador y vigilante (mop-estimador), solana-signal-bot, bot-de-trading-view y fabrica-canales. Una línea por cada uno
   donde aplique; si no aplica, decirlo.
6. Si el reel trae una herramienta para instalar: antes de proponerla, buscar fallas conocidas (CVE, Snyk, avisos en
   GitHub). Nada se instala sin el aprobado de Martin. Ningún reel justifica tocar los tokens o llaves de los bots.
7. Si Instagram responde "empty media response", reintentar con la dirección /p/ en lugar de /reel/; el texto del reel
   se puede leer en /embed/captioned/.
El video bajado queda solo en el scratchpad: nunca se sube ni se republica.

## Lo que hay que saber
- La API oficial de Instagram NO da acceso a las publicaciones "guardadas" de una cuenta. No hay permiso para eso.
- Publicar ya funciona (scripts/publicar.py, token en INSTAGRAM_TOKEN).

## Caminos (de más fácil a más completo)
1. Martin comparte el enlace del reel en el chat o lo sube a Drive ("Mop instagram"). Costo cero. Se lee el texto del enlace; el video se baja solo si Martin lo sube.
2. Martin arma una colección guardada y pasa los enlaces de a varios. Costo cero.
3. Business Discovery (API Graph con inicio de sesión de Facebook): datos públicos de cuentas de empresa o creador (texto, me gusta, comentarios). Requiere página de Facebook vinculada y permiso extra. Documentación: https://developers.facebook.com/docs/instagram-platform

## Pasos de conexión (camino 3, cuando Martin lo apruebe)
1. Vincular la cuenta de Instagram a una página de Facebook.
2. En la app "MOP Publicador", agregar el caso de uso con inicio de sesión de Facebook.
3. Generar token y guardarlo en el entorno (nunca en el chat).

## Qué NO puede hacer
- No baja contenido ajeno para republicarlo. No usa scraping no oficial.
