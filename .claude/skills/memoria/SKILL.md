---
name: memoria
description: Cerebro MOP. Usar SIEMPRE antes de leer TABLERO.md, HISTORIA.md o buscar en Drive o Gmail, cuando Martin nombra una obra, constructora, proveedor, bot, trámite o proyecto ("cómo va Kilwins", "qué pasó con Danny", "cómo están los bots"), y al terminar cualquier tarea que cambió algo. Busca la ficha en Supabase con una consulta y anota lo nuevo con fuente y fecha.
---

# memoria (Cerebro MOP)

**Estado:** activa · **Versión:** v1 · **Fecha:** 1-nov-2026 · Plan: `CEREBRO_MOP.md`.

## Los tres niveles
1. **Caliente:** `CALIENTE.md` (2 KB como máximo). Lo muestra el gancho de inicio entero. Ya está leído: no volver a abrirlo.
2. **Tibio:** fichas en Supabase (proyecto mop-estimador, `sfmhdtingccfkzkwbqgt`): `memoria_fichas` y `memoria_hechos`. Privadas.
3. **Frío:** Gmail, Drive, repositorios, informes de bots. Solo si la ficha no alcanza (ver "La araña" abajo).

## Buscar (antes de leer archivos grandes)
`python3 -m herramientas.memoria buscar "<nombre o tema>"` imprime la consulta; pasarla por la herramienta `execute_sql`.
Devuelve las fichas parecidas (aunque el nombre esté mal escrito) con sus 5 hechos más nuevos, fuente y fecha.
Contestar con eso. Decir la fecha del dato. Si tiene más de 30 días, decir "a confirmar".

## Anotar (al terminar algo que cambió un dato)
- Hecho nuevo: `python3 -m herramientas.memoria anotar "<ficha>" "<qué pasó>" --fuente "<de dónde>" --quien "<asistente>" [--tipo obra]`.
- Cambió el estado, el próximo paso o la fecha: `python3 -m herramientas.memoria ficha "<ficha>" --tipo <tipo> --estado ... --proximo ... --vence AAAA-MM-DD --fuente ...`.
- Pasar el SQL por `execute_sql`. Una línea por hecho, frases cortas. El resumen de la ficha, 600 caracteres como máximo.
- Si cambió algo de "Vence en 7 días" o "Esperando", rehacer el cartel (abajo).

## La araña que aprende
Si la ficha no tiene el dato: seguir `buscar-papeles` (Drive, Gmail, repositorios, audios transcriptos) y **anotar lo que se encontró en la ficha**, con fuente y fecha. La próxima vez no se busca.

## Audios de Martin
Audio o video de una llamada → `python3 -m herramientas.transcribir <archivo>` (faster-whisper, gratis) → resumir en 1 a 3 hechos → anotar en la ficha que corresponda. El texto completo no se guarda en el repositorio.

## Rehacer el cartel
`python3 -m herramientas.memoria caliente --sql` → `execute_sql` → guardar el resultado en un .json → `python3 -m herramientas.memoria caliente --filas <json> --escribir --decision "<d-m: decisión>"` (hasta 5) → commit de `CALIENTE.md`. Lo hace todos los días la tarea de las 6:27; un chat lo rehace si cambió algo urgente.

## Revisar (limpieza)
`python3 -m herramientas.memoria revisar` → `execute_sql`: fichas vencidas, sin fuente o con más de 30 días. Avisar en una línea.

## Qué NO hace
- Nunca copia montos, correos, teléfonos ni direcciones de casa a este repositorio público: eso vive solo en Supabase.
- No borra hechos: si uno está mal, se anota otro que lo corrige.
