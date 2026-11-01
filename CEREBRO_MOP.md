# CEREBRO MOP — plan maestro de memoria

Pedido de Martin, 1-nov-2026: "memoria excelente, súper rápida, todo ordenado y súper económica, para MOP, los bots y el trabajo futuro".
Estado: **aprobado por Martin el 1-nov ("hacé todo hoy") y armado el mismo día** (ver "Hecho el 1-nov" al final). Este archivo es público: acá van solo reglas y diseño, nunca datos de clientes, plata ni datos personales.

## El problema medido (1-nov)
- El gancho de inicio muestra unos 16 KB y Claude Code solo deja ver los primeros 2 KB: los chats nuevos no ven el TABLERO.
- La memoria está repartida en 5 lugares (este repositorio, mop-estimador, Supabase, Drive y el documento del proyecto de claude.ai) y TABLERO.md e HISTORIA.md pesan unos 26 KB cada uno.
- Cada chat vuelve a leer y a buscar lo mismo: tarda y gasta.
- Lo que se habla por teléfono y por WhatsApp no entra.

## Cinco reglas
1. **Un solo lugar por dato.** Cada dato vive en un lugar; los demás lo citan.
2. **Tres niveles.** Caliente (siempre cargado, 2 KB como máximo), tibio (fichas, una consulta) y frío (correos, PDF, informes, audios: solo se busca si hace falta).
3. **Escribir al momento.** Quien hace algo deja una línea en la ficha cuando termina: el chat, el cazador, el vigilante, los informes de los bots.
4. **Privado en Supabase, reglas en el repositorio.** Clientes, montos, seguros, bots y lo personal van en la base privada. En este repositorio público, solo reglas y código.
5. **Cada dato con fuente y fecha.** Lo que tiene más de 30 días sin confirmar se marca "a revisar".

## Los tres niveles
- **Caliente — `CALIENTE.md`** (2 KB como máximo). Lo único que el gancho de inicio muestra entero: qué vence hoy y mañana, qué está trabado, decisiones que esperan a Martin, una línea por bot y las 5 últimas decisiones. Lo rehace la tarea de las 6:27; si algo cambia en el día, lo actualiza el chat que lo cambió. Como el repositorio es público, la versión del repositorio dice solo títulos ("Kilwins: vence el viernes") y la completa vive en Supabase.
- **Tibio — fichas en Supabase** (proyecto de mop-estimador):
  - `memoria_fichas`: tipo (obra, constructora, proveedor, bot, trámite, persona, proyecto), nombre, alias, resumen corto (600 caracteres como máximo), estado, próximo paso, vence, actualizado, fuente.
  - `memoria_hechos`: una línea por hecho, con ficha, fecha, texto, fuente y quién lo escribió. Solo se agrega, nunca se borra.
  - Búsqueda en una sola consulta: texto completo en español más nombres parecidos ("kilwin" encuentra "Kilwins"). Sin servicios pagos.
  - Se conecta con lo que ya existe: `oportunidades` (fichas del cazador) y `tablero` (números de las tareas).
- **Frío — donde ya está:** Gmail, Drive (bandeja de obras, carpetas de obra, informes de los bots), los repositorios. No se copia: la ficha guarda el enlace.

## La araña que aprende (mejor que las de los reels)
Cuando la ficha no alcanza: busca en Supabase, Drive, Gmail, los repositorios y las transcripciones de audios; contesta, y **guarda lo que encontró como hecho en la ficha, con fuente y fecha**. La próxima vez no busca. Es la versión 2 de `buscar-papeles`.

## Lo que entra
- Audios de Martin después de una llamada: se pasan a texto (faster-whisper, gratis, probado el 1-nov) y van como hechos a la ficha.
- Chats de WhatsApp exportados por Martin a la carpeta de la obra en Drive.
- Correos: los trae la bandeja (ya funciona).
- Bots: el informe diario de cada bot deja su línea en la ficha del bot (estado, ganancia o pérdida en simulación, qué espera decisión). Así los bots entran al cartel sin abrir sus informes.

## Mantenimiento automático (tarea de las 6:27)
- Rehace `CALIENTE.md`.
- Revisa las fichas: vencidas, sin fuente, con más de 30 días, o que se contradicen. Avisa en una línea.
- Una vez por mes pasa a archivo lo viejo de TABLERO.md e HISTORIA.md, para que no vuelvan a crecer.

## Lo económico
- Cero dólares nuevos: Supabase, Drive, faster-whisper y las tareas ya existen.
- Menos lectura por chat: 2 KB al arrancar en vez de leer archivos de 26 KB.
- Tareas chicas (resumir, pasar a texto, cargar fichas) con el modelo más barato; programar y revisar con el principal.
- Se mide antes y después (ver abajo), sin números inventados.

## Cómo sabremos que anda
- Chat nuevo, pregunta "¿qué vence hoy?": contesta bien sin leer ningún archivo.
- "¿Cómo va Kilwins?": una consulta, respuesta con fuente y fecha.
- "¿Cómo están los bots?": una línea por bot, con la fecha del dato.
- Se toma el tiempo y lo que gasta cada prueba hoy (antes) y al terminar cada fase.

## Fases (máximo 3 acciones por semana)
- **Fase 0 — hoy, media hora:** `CALIENTE.md`, el gancho lo muestra primero y entero, y la medición de antes.
- **Fase 1 — semana del 2-nov:** tablas y búsqueda en Supabase, herramienta `memoria` (buscar, anotar, caliente) en mop-estimador, y carga inicial de fichas desde TABLERO, HISTORIA y las tareas.
- **Fase 2 — semana del 9-nov:** araña que aprende (`buscar-papeles` v2), audios de Martin a fichas, y que el cazador, el vigilante y los informes de los bots escriban su línea al terminar.
- **Fase 3 — semana del 16-nov:** mantenimiento en la tarea de las 6:27, TABLERO e HISTORIA adelgazados, medición de después.
- **Fase 4 — desde diciembre (trabajo futuro):** pestaña "Memoria" en la app del estimador; memoria por obra que alimenta los presupuestos (precios reales, horas reales, lo que salió mal); resumen semanal para la reunión del consejo; memoria de decisiones de los bots (por qué se aprobó o se frenó cada estrategia).

## Riesgos (abogado del diablo)
- **Un sistema más para mantener.** Solución: reemplaza, no suma. El volcado de inicio se cambia por el cartel, y TABLERO e HISTORIA se achican.
- **Datos viejos o equivocados.** Solución: fuente y fecha en cada dato, más la revisión diaria.
- **Datos privados en el repositorio público.** Solución: lo privado solo en Supabase; las guardias ya frenan direcciones y palabras prohibidas.
- **Vuelta atrás:** si no sirve, se apaga el gancho nuevo y todo sigue como hoy. No se borra nada.

## Hecho el 1-nov-2026
- Fase 0: `CALIENTE.md` y el gancho de inicio nuevo (`.claude/hooks/leer_tablero.sh`): pasó de unos 16 KB (cortado a 2 KB) a unos 1,6 KB que se ven enteros.
- Fase 1: tablas `memoria_fichas` y `memoria_hechos` y la función `memoria_buscar` (migración `supabase/migrations/20261101190000_memoria.sql`), herramienta `herramientas/memoria.py` con 7 pruebas (`pruebas/prueba_memoria.py`), habilidad `memoria`. Carga inicial de 30 fichas lista; la migración en Supabase espera la confirmación de Martin (Supabase pidió confirmar y nadie contestó a tiempo).
- Fase 2: `buscar-papeles` v2 (la araña que aprende), `herramientas/transcribir.py` para audios.
- Fase 3: la tarea de las 6:27 rehace el cartel y revisa la memoria; TABLERO.md (27 a 18 KB) e HISTORIA.md (26 a 16 KB) adelgazados, lo viejo en `archivo/`.
- Fase 4 (pestaña "Memoria" en la app del estimador): queda para diciembre, como dice el plan.
