---
name: instagram-lectura
description: (Pendiente de conexión) Leer reels para sacar ideas de contenido: los que Martin comparte o los públicos de cuentas de empresa. Usar cuando Martin dice "mirá este reel", "leé mis guardados" o "qué publica <cuenta>".
---

# instagram-lectura

**Estado:** pendiente de conexión · **Versión:** v0 · **Fecha:** 14-oct-2026

## Cuándo se dispara
- "mirá este reel", "leé mis guardados", "qué publica <cuenta>".

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
