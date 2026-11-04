---
name: instagram-lectura
description: Leer reels para sacar ideas de contenido: los que Martin comparte (enlace o grabación de pantalla) o los públicos de cuentas de empresa. Usar cuando Martin dice "mirá este reel", manda un enlace de instagram.com/reel, una grabación de pantalla, "leé mis guardados" o "qué publica <cuenta>".
---

# instagram-lectura

**Estado:** activa · **Versión:** v1 · **Fecha:** 3-nov-2026 (v0: 14-oct)

## Cuándo se dispara
- Martin manda un enlace de instagram.com/reel o /p/, o una grabación de pantalla de un reel.
- "mirá este reel", "leé mis guardados", "qué publica <cuenta>".

## Lo que hay que saber (probado 3-nov-2026)
- Desde el 1-nov Instagram pide iniciar sesión: yt-dlp da "empty media response", la página embed viene sin video ni texto, Firecrawl no soporta Instagram.
- El permiso de "MOP Publicador" (inicio de sesión de Instagram) NO trae business_discovery ni instagram_oembed.
- No se saltea el inicio de sesión ni se disfraza el pedido (ni cookies de la cuenta de MOP: arriesga la cuenta).
- La API oficial no da acceso a las "guardadas".

## Pasos
1. Con el enlace: probar una vez `yt-dlp --skip-download --dump-json <enlace>`. A veces anda (4-nov sí, 3-nov no). Si anda, bajar el video con `yt-dlp -f "b[ext=mp4]/b" -o reel.mp4 <enlace>` a una carpeta nueva del scratchpad y seguir en el paso 3.
2. Si falla (lo normal desde el 1-nov): pedirle a Martin, en una línea, que grabe la pantalla del celular CON SONIDO mientras pasa el reel y lo mande al chat o a la carpeta "Mop instagram" de Drive (id 19ul5QKrqcSqsnZGLbO2OI8BrTeRzGIIO). Si quiere, que copie también el texto de la publicación.
3. Con el video: `python3 -m herramientas.leer_reel <video> --salida <carpeta del scratchpad>`. Da lo que se dice (faster-whisper, idioma automático) y una grilla con un cuadro cada 3 segundos. Mirar la grilla con Read.
4. Responder: qué dice, qué muestra, y 2 o 3 ideas concretas para MOP (formato, gancho, texto), sin copiar.
5. Nada se republica ni se guarda en el repositorio. La idea útil va a la memoria si Martin la aprueba.

## Camino oficial (más completo, cuando Martin lo apruebe)
Business Discovery (API Graph con inicio de sesión de Facebook): texto, me gusta, comentarios y enlace del video de cuentas de empresa o creador.
1. Crear una página de Facebook de MOP y vincularle la cuenta de Instagram (desde la app de Instagram: Editar perfil → Página).
2. En la app "MOP Publicador": agregar el caso de uso con inicio de sesión de Facebook y el permiso instagram_basic + pages_show_list.
3. Generar el token y guardarlo en el entorno como INSTAGRAM_FB_TOKEN (nunca en el chat).
Documentación: https://developers.facebook.com/docs/instagram-platform/instagram-api-with-facebook-login/business-discovery

## Qué NO hace
- No baja contenido ajeno para republicarlo. No usa scraping no oficial ni saltea bloqueos.
