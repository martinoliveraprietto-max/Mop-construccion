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
- 2026-10-18 17:30 · camino-nuevo · Martin mandó un enlace de reel; se leyó con yt-dlp + faster-whisper (habla de un plugin oficial "Claude Code Setup") · Instagram + web oficial de Claude → decidido: habilidad instagram-lectura pasa a v1 con el método probado.
- 2026-10-18 18:00 · herramienta-nueva · corrí la revisión del plugin oficial Claude Code Setup (solo lectura, leída de su repositorio público) · repositorio + plugin → decidido: 2 propuestas a Martin (guardia también sobre lo preparado para commit; script de audio que no falle por el certificado del proxy); nada se cambia sin su aprobado.
- 2026-10-19 · pedido-repetido · segundo reel en el día para "mirar el video" (Automaton, agente que se paga sus servidores con cripto) · Instagram + GitHub de Conway Research → decidido: instagram-lectura ya lo cubre (2 usos); idea para MOP: palabra clave en comentarios ("comentá PRESUPUESTO"), pendiente de aprobado.
- 2026-10-19 00:10 · camino-nuevo · Martin preguntó si se puede ver y copiar el código de Automaton · GitHub Conway-Research/automaton (licencia MIT, ~67 mil líneas TypeScript) → decidido: se propone copiar solo las ideas (latido, tope de gasto, bitácora) dentro de lo que ya hay; nada de billetera ni código que se cambia solo.
- 2026-10-19 00:20 · corrección-de-formato · Martin: "olvidate de MOP, salí de la caja": no orientar todo a MOP cuando habla de ideas nuevas · chat → decidido: en ideas nuevas pensar fuera de MOP; las reglas de MOP siguen para lo de MOP.
- 2026-10-19 · camino-nuevo · primer video de Facebook (enlace share/r): yt-dlp lo baja igual que Instagram; se vio imagen (cuadros cada 4 s) y audio · Facebook → decidido: instagram-lectura sirve también para Facebook; agregar la línea a la habilidad.
- 2026-10-19 · herramienta-nueva · piloto de animación bíblica: imágenes con FLUX.1-schnell en el Space de Hugging Face (cuota gratis diaria, se agotó a las 7 imágenes) y pollinations.ai (de respaldo, mala calidad, con marca de agua); voces edge-tts es-US-AlonsoNeural y en-US-AndrewNeural; armado con FFmpeg · Hugging Face + edge-tts + FFmpeg → decidido: si el proyecto sigue, hacerle su propio repositorio y su habilidad.
- 2026-10-19 · corrección-de-formato · Martin: el video tiene que tener movimiento y los personajes tienen que hablar (no imágenes con subtítulos) · chat → decidido: rehacer como diálogo con voces por personaje; hace falta herramienta con GPU (Hugging Face PRO 9 USD/mes o una de video pago); Martin elige.
