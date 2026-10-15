---
name: estado-de-obra
description: Dice el estado de una obra de MOP juntando su ficha de TABLERO.md, los últimos correos del contacto, el calendario de los próximos 7 días y la carpeta de Drive de la obra. Usar cuando Martin dice "estado de", "cómo va" o "qué pasa con" + nombre de obra (Rojas, Blue Door, Flagler, Lincoln, Kilwins, Galleria, Sedano's u otra).
---

# estado-de-obra

**Estado:** activa · **Versión:** v1 · **Fecha:** 14-oct-2026 · **Veces usada:** ver HABILIDADES.md

## Cuándo se dispara (frases exactas de Martin)
- "estado de <obra>"
- "cómo va <obra>"
- "qué pasa con <obra>"

## Pasos (con la fuente de cada dato)
1. Ficha: leer la obra en `TABLERO.md`, sección "Obras" (cliente y contacto, estado, monto, cobrado, por cobrar, próximo paso, riesgo).
2. Correos: Gmail (conector de claude.ai), `search_threads` con el nombre de la obra y/o la empresa del contacto, `newer_than:30d`. Leer con `get_thread` (formato PLAIN_TEXT) los 2 o 3 hilos más nuevos: las búsquedas solo muestran los mensajes más viejos de cada hilo.
3. Calendario: Google Calendar, `list_events` de hoy a 7 días; quedarse con lo que nombre la obra o el contacto.
4. Drive: Google Drive, `search_files` con `title contains '<obra>'`; listar carpeta y archivos más nuevos (cotizaciones, planos).
5. Comparar: si un correo cambia algo de la ficha (fecha, monto, estado), decirlo y actualizar la ficha en `TABLERO.md` con la fuente.
6. Sumar 1 a "veces usada" en `HABILIDADES.md`.

## Qué devuelve (frases cortas, sin tablas)
- Estado.
- Cobrado.
- Por cobrar con fecha.
- Próximo paso (con fecha).
- Riesgo.
- Una línea "Fuentes:" (tablero, correo con fecha, Drive, calendario).
Lo que no está en ninguna fuente: "sin dato".

## Qué NO puede hacer
- No manda correos ni mensajes: si hace falta escribir, prepara un borrador y espera el "aprobado" de Martin.
- No inventa montos ni fechas.
- No copia correos, teléfonos ni direcciones a TABLERO.md (repositorio público).

## Cambios
- v1 (14-oct-2026): creada. Probada con Kilwins el 14-oct (resultado en TABLERO.md, Mensajes entre asistentes).
