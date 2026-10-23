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
- 2026-10-22 11:05 · cliente-nuevo · Florida Palm Construction (S26-056) llega por Danny, que ahora escribe desde un dominio nuevo (Encore Construction) · Gmail + Drive → decidido: anotado en Obras de TABLERO.md; confirmar con Danny si Encore es su empresa nueva.
- 2026-10-22 11:20 · corrección · Encore Construction es la empresa nueva de Danny; los planos pueden venir de Encore o de Bello · chat → decidido: anotado en TABLERO.md y HISTORIA.md.
- 2026-10-22 11:40 · juntó-fuentes · presupuesto S26-056: Gmail + Drive + precios de la app + búsqueda web · Gmail, Drive, mop-estimador → decidido: ya lo cubre leer-planos; sin habilidad nueva.
- 2026-10-22 11:50 · camino-nuevo · Danny pasa a mandar planos a Martin para cotizar juntos (Encore o Bello) · chat → decidido: Anticipación ítem 11; bandeja ya lo cubre; cazador con Encore y Florida Palm como conocidas.
- 2026-10-22 11:30 · pedido-repetido · plano de más de 10 MB que el conector de Drive no baja (civil S26-056, 16,7 MB); Martin lo volvió a subir a Drive y sigue igual · Drive → decidido: camino = compartir por enlace un momento y bajarlo con curl; si se repite, sumarlo a la habilidad leer-planos.
- 2026-10-22 11:50 · corrección-formato · Martin: el grout no va en bolsas, va por yardas cúbicas con camión y bomba · chat → decidido: regla nueva en CLAUDE.md de mop-estimador (Reglas de oficio) y S26-056 corregida.
- 2026-10-22 12:15 · siempre · Martin: usar SIEMPRE nuestra base de precios aunque tenga días o semanas; no pedirle precios nuevos cada vez · chat → decidido: regla en CLAUDE.md de mop-estimador; S26-056 rehecho con la base.
- 2026-10-22 13:00 · cada-vez · Martin sube todos los días una foto de lo que se rindió, pero no quedaba guardada (0 partes en la base) · app + Supabase → decidido: parte del día con foto en la pantalla de la obra; si se repite que no carga partes, el vigilante lo avisa.
- 2026-10-23 00:20 · corrección-formato · Martin: el acero estaba bajo (muchas uniones soldadas), el civil bajo y al 3D le faltaba el acero · chat + planos S-3.x/S-4.x → decidido: en todo presupuesto con acero se cuentan las soldaduras una por una y los días salen de ahí; el 3D lleva cada columna, dintel y ménsula del juego.
- 2026-10-23 00:35 · no-me-hagas-repetir · Martin: "estos errores no podés tener más" (acero, civil y 3D de S26-056) · chat → decidido: control de cierre de cinco pasos en CLAUDE.md de mop-estimador; sin pasarlo, el número va como BORRADOR.
- 2026-10-23 01:15 · no-me-hagas-repetir · Martin: el maestro de obra, el superintendente y el manager que creamos tienen que usarse en CADA presupuesto; estaban en una rama sin unir y no se usaron · mop-estimador (rama sedano-solo-demo-estructura) → decidido: pasados a la rama principal; en cada estimado se corren los tres roles con su libro antes de darle un número a Martin.
