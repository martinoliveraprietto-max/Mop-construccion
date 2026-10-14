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
- 2026-10-14 08:00 · corrección-de-formato · respuestas en español rioplatense, frases cortas, sin tablas, sin inglés salvo nombres propios · prompt del 13-oct → decidido: regla en CLAUDE.md.
