---
name: instagram-lectura
description: Leer reels para sacar ideas de contenido: los que Martin comparte o los públicos de cuentas de empresa. Usar cuando Martin dice "mirá este reel", "leé mis guardados" o "qué publica <cuenta>".
---

# instagram-lectura

**Estado:** activa (camino 1) · **Versión:** v1 · **Fecha:** 18-oct-2026

## Cuándo se dispara
- "mirá este reel", "leé mis guardados", "qué publica <cuenta>".

## Lo que hay que saber
- La API oficial de Instagram NO da acceso a las publicaciones "guardadas" de una cuenta. No hay permiso para eso.
- Publicar ya funciona (scripts/publicar.py, token en INSTAGRAM_TOKEN).

## Cómo se lee un reel (probado el 18-oct, gratis, solo para leerlo)
1. En el directorio temporal de la sesión: `yt-dlp --write-info-json -o "v.%(ext)s" <enlace>` (texto, cuenta, me gusta y el video).
2. Audio: FFmpeg de imageio-ffmpeg → `a.wav` 16 kHz mono.
3. Texto: `pip install faster-whisper`, modelo "small", idioma "es". Pasarle el audio ya leído con numpy
   (con un archivo directo falla por la versión de `av`).
4. Contarle a Martin: qué dice, si es verdad (verificar en la fuente oficial) y si sirve para MOP.
5. Para ver la imagen: FFmpeg con `-vf "fps=1/4,scale=240:-1,tile=4x4"` arma una hoja de cuadros y se mira.
   Funciona igual con enlaces de Facebook (share/r).
6. Borrar el video al terminar. Nunca se republica ni se sube al repositorio.

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
