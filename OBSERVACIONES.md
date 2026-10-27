# OBSERVACIONES — lo que el agente nota para crear habilidades

Formato de cada línea: `- AAAA-MM-DD HH:MM · tipo · qué pasó · fuentes`
Tipos: pedido-repetido / datos-de-varias-fuentes / "siempre" / herramienta-nueva / corrección-de-formato.
Cuando se decide qué hacer con una línea, se le agrega al final `→ decidido: ...` (así el gancho de cierre sabe que ya se revisó).

Reglas de decisión (las aplica el gancho Stop antes de cerrar):
- Aparece 2 veces o más → habilidad.
- 1 vez con "siempre", "cada vez", "de ahora en más" o "no me hagas repetir" → habilidad.
- Corrección de formato → regla en CLAUDE.md.
- Herramienta nueva → "Anticipación" de TABLERO.md + esqueleto con estado "pendiente de conexión".
- Si nada cumple → escribir "sin habilidades nuevas".

## Registro
- 2026-10-14 08:00 · "siempre" · Martin pidió en el prompt maestro que al arrancar y al terminar cada sesión se lea y escriba el tablero · prompt del 13-oct → decidido: regla en CLAUDE.md y ganchos SessionStart/Stop.
- 2026-10-14 08:00 · datos-de-varias-fuentes · para cargar las obras se juntaron HISTORIA.md + Gmail + Drive + Calendar a mano · TABLERO.md → decidido: habilidad estado-de-obra (v1).
- 2026-10-14 08:00 · herramienta-nueva · Instagram API para leer reels guardados · prompt del 13-oct → decidido: Anticipación ítem 1 + esqueleto instagram-lectura (pendiente de conexión).
- 2026-10-14 08:00 · herramienta-nueva · YouTube Data API y TikTok Content Posting API (fabrica-canales) · prompt del 13-oct → decidido: Anticipación ítem 3 + CONEXIONES.md en fabrica-canales.
- 2026-10-14 03:40 · herramienta-nueva · crear repositorios de GitHub desde la nube da 403 · mcp github create_repository → decidido: Anticipación ítem 3 (Martin crea el repositorio vacío).
- 2026-10-14 04:45 · herramienta-nueva · Apps Script en la cuenta de Google como agente Gmail → Drive (Martin pidió el agente) · mop-estimador herramientas/bandeja_gmail.gs → decidido: Anticipación ítem 6; instalado.
- 2026-10-14 08:00 · corrección-de-formato · respuestas en español rioplatense, frases cortas, sin tablas, sin inglés salvo nombres propios · prompt del 13-oct → decidido: regla en CLAUDE.md.
- 2026-10-15 02:20 · "siempre" · Martin: todo plano en 3D muestra cada etapa que marca el plano, la haga o no MOP, y la obra terminada para el cliente · chat 15-oct → decidido: regla en CLAUDE.md de mop-estimador (main).
- 2026-10-15 02:20 · herramienta-nueva · adjuntos de correo grandes: la herramienta de Gmail no los lleva; se suben a la app y va un enlace propio de 30 días · mop-estimador subir_obra compartir → decidido: regla en CLAUDE.md de mop-estimador.
- 2026-10-15 02:40 · herramienta-nueva · Blender 4.2 LTS para render profesional (no viene instalado en la nube) · download.blender.org → decidido: anotado en la regla del 3D (se baja a /opt/blender).
- 2026-10-15 03:10 · "siempre" · Martin: los videos y el 3D para el cliente siempre con render profesional · chat 15-oct → decidido: Decisiones de TABLERO.md, tabla decisiones de la app y regla en CLAUDE.md de mop-estimador.
- 2026-10-15 22:00 · buscó-a-mano · Martin tuvo que preguntar por la entrada del seguro: el acuerdo firmado ya estaba en Drive desde el 14-oct y el tablero decía "sin dato" · Drive (bandeja de obras) → decidido: habilidad buscar-papeles (v1).
- 2026-10-15 23:30 · corrección-de-formato · Martin: "escribí y hablá en español" (respuestas salieron en inglés) · chat 15-oct → decidido: ya está en CLAUDE.md (responder siempre en español); se cumple, sin regla nueva.
- 2026-10-15 23:30 · juntó-fuentes · presupuesto de Sedano's: tabla de precios de la app, materiales.csv, presupuesto de Kilwins en la base y búsquedas en internet · Supabase + repositorio + web → decidido: ya lo cubre la regla de precios de mop-estimador (13-oct); sin habilidad nueva.
- 2026-10-16 10:00 · herramienta-nueva · Martin pidió instalar 10 skills de skills.sh (claude-office-skills y coreyhaines31/marketingskills) en alcance de proyecto · npx skills add → decidido: instaladas y registradas en HABILIDADES.md como v0; mejoras contra los 5 agentes propuestas a Martin, nada se implementa hasta su aprobado.
- 2026-10-15 23:40 · herramienta-nueva · datos abiertos de permisos del condado de Miami-Dade (ArcGIS) y lista de licitaciones de construcción del condado (SPD) para el cazador · Martin: "desarrollame un excelente cazador de obras" → decidido: habilidad cazador v1 en mop-estimador, ítem 7 de Anticipación actualizado.
- 2026-10-15 23:55 · camino-nuevo · licencia de contratista general (CGC) para MOP por un calificador (Danny Ruiz o el amigo de Washington) · chat 15-oct → decidido: Anticipación ítem 10 con la ley leída; la decisión pasa por cuestionar.
- 2026-10-19 16:05 · herramienta-nueva · tabla tablero en Supabase para que las tareas programadas dejen sus números y la tarea de las 6:27 los lea de una vez · pedido de Martin vía Claude chat → decidido: migración + herramientas/tablero.py + paso nuevo en vigilante y cazador; anotado en Mensajes entre asistentes de TABLERO.md.
- 2026-10-27 15:40 · datos-de-2-fuentes · resumen diario del cazador (informe del cazador + bandeja del vigilante en mop-estimador) · Martin: "¿qué hizo hoy el cazador y qué me resta?" → decidido: sin habilidades nuevas (primera vez, sin "siempre"); si se repite, crear /cazador-hoy.
