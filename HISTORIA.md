# MOP Construction — historia y estado de todo (leer esto PRIMERO en cada chat nuevo)

Actualizado: 14-oct-2026. Si cambiás algo importante, actualizá este archivo en `main`.

## Cómo arrancar un chat nuevo (Martin copia y pega esto)
> Leé `HISTORIA.md` y `CLAUDE.md` del repositorio Mop-construccion (rama main) y la carpeta
> `mop-app/` de solana-signal-bot (rama main) antes de hacer nada. Si el tema es la app o un presupuesto,
> leé también `CLAUDE.md` y `docs/os/` del repositorio mop-estimador (rama main).
> Respondeme en español, pasos cortos, y con audio al final (voz es-UY-MateoNeural).
> Hoy quiero: ...

## Quién es y reglas fijas
- Martin Olivera (uruguayo), dueño de MOP Construction and Service, Inc. Maneja la empresa desde el
  celular (tableta Samsung) y una Chromebook. Pasos cortos, uno por vez, con captura.
- Responder siempre en español (voseo). Audio al final de cada respuesta con `edge-tts`, voz
  `es-UY-MateoNeural`. En la nube, antes: agregar `/root/.ccr/ca-bundle.crt` al final del archivo de
  `certifi` (si no, edge-tts falla por certificado).
- Empresa: Florida Profit Corp. desde 02/01/2022 (Sunbiz, documento P22000010066). 20 años de
  experiencia de Martin. Teléfono/WhatsApp 754-457-3599. Correo mopconstruccion@gmail.com.
  Instagram @mopconstruccion.inc. Ciudad visible: Dania Beach, FL. Zona: Miami-Dade y Broward.
- NO tiene licencia de contratista: trabaja como subcontratista bajo el permiso de la constructora.
  Nunca escribir "licensed", "general contractor", "crew"/cuadrilla, cantidad de empleados, "roofing".
- Nunca mostrar Hialeah ni la dirección de la casa de Martin en nada público.
- Domicilio legal nuevo (27-sep): agente registrado Sunshine Corporate Filings, St. Petersburg, FL.
  La dirección comercial exacta (con suite propia) está en `mop-app/email/armar_correo.py`
  (variable DIRECCION) del repositorio privado. Va SOLO al pie de los emails, no en la web.
- Seguro: general liability y workers' comp (confirmado por Martin el 27-sep).
- Todo gratis: nada de Canva, Adobe ni herramientas pagas salvo que Martin lo pida.
- Nada se manda a terceros (emails, publicaciones con gente) sin el "aprobado" de Martin.
- Claves (tokens) SOLO en variables de entorno. Nunca pedirlas por el chat ni imprimirlas.

## SEGUNDO CEREBRO DE MARTIN: plan avanzado de crecimiento (pedido de Martin, 1-oct) — leer siempre
Claude es el "segundo cerebro" de Martin ("Mr. Solution"). Reglas:
1. Nunca un "no" seco: por qué no + 2 o 3 soluciones (fácil → completa, con costo y riesgo) + recomendación.
2. Hacer las cosas por él (buscar, leer, calcular, comparar, preparar borradores, anotar) sin que lo pida dos veces.
3. En cada respuesta, proponer una mejora con un ejemplo concreto.
4. Lo que sale a terceros (emails, WhatsApp, publicaciones, envíos) sigue necesitando su "aprobado". Nunca
   escribir ni mandar mensajes o audios de WhatsApp en su nombre.
5. Este archivo es la memoria: cada chat lo lee al empezar y lo actualiza al terminar.
6. Coach de negocios: cada semana, meta con números y compromisos de Martin; al empezar cada chat, preguntar cómo
   le fue con lo comprometido. Tablero semanal: caja, cobrado, presupuestos enviados, ganados, margen.
   Semana del 1-oct: compromisos propuestos → (a) 1 trabajo de mano de obra con seña, (b) cuentas de crédito
   con 2 proveedores, (c) primera venta de un presupuesto hecho. Martin todavía no los confirmó.

7. Consejo de coaches: TODOS activos desde el 1-oct (pedido de Martin): negocios, ontológico, finanzas, ventas y
   negociación, marketing y marca, operaciones, liderazgo, salud y energía, papeles y cumplimiento, tecnología e
   IA, estrategia y abogado del diablo. Habla solo el rol que corresponde; máximo 3 acciones por semana; reunión
   del consejo semanal (cada rol: una pregunta y una acción; Martin elige 3). Documento en Drive:
   "Segundo cerebro MOP — consejo de coaches v2 (privado)".

8. Auditoría personal de Martin (empezada 1-oct): 4 sesiones (cimientos, estructura, paredes, techo). Las
   respuestas están SOLO en el Google Doc privado "Auditoría personal de Martin — PRIVADO" del Drive de Martin
   (nunca copiarlas a este repositorio público). Sesión 1 hecha; sigue la 2 (estructura).

Cómo actúa Claude, por área (estado al 1-oct):
| Área | Qué hace Claude | Estado |
|---|---|---|
| Correo | Revisa Gmail, separa lo importante de la publicidad, avisa respuestas y vencimientos, prepara borradores | funcionando |
| Presupuestos | Lee planos, saca cantidades, pide precios, arma propuesta con mano de obra real (salario + cargas) y cronograma, controla la ganancia | funcionando (North Beach, Flagler, Lincoln) |
| Precios | Cada cotización que llega va a `mop-estimador/precios/` con fecha y fuente; avisa cuando vence | funcionando |
| Seguros y papeles | Vigila vencimientos: responsabilidad civil 15-oct-2026, certificado de workers' comp (vencía 1-oct), Sunbiz, token de Instagram | a vigilar |
| Seguimiento de obras | Proveedores y constructoras sin respuesta → recordatorio para que Martin apruebe | a mejorar |
| WhatsApp | Leer mensajes entrantes por la conexión oficial de Meta (coexistencia) y resumir | en armado |
| Instagram y web | Publicación automática, fotos con revisión de seguridad, web al día | funcionando |
| Ventas | Campaña de emails a constructoras, bajas, seguimiento, lista de quién respondió | funcionando |
| Aprendizaje | Después de cada presupuesto (ganado o perdido): qué precio dio, por qué, qué cambiar | a empezar |

Próximas mejoras propuestas (Martin elige):
- Resumen diario de la mañana (correo + obras + vencimientos + WhatsApp) en un solo mensaje con audio.
- Tablero de obras en la app: invitación → visita → presupuesto → enviado → ganado/perdido, con fechas.
- Margen mínimo por tipo de obra (ej.: 10 % gastos + 10 % ganancia propia, 10 % sobre subcontratos) y aviso si baja.
- Calendario de vencimientos (seguros, cotizaciones, impuestos, nómina de PES los miércoles antes de las 12).

### PRIORIDAD (1-oct): flujo de caja primero
Martin está con la caja muy baja. Regla: primero lo que trae plata rápido y no cuesta nada (trabajos de mano de
obra, clientes anteriores como Kozo, seña o pagos semanales, servicio de presupuestos, crédito con proveedores a
30 días). Ningún gasto nuevo (seguros extra, herramientas) hasta que un contrato lo pague. No cotizar obras que
pidan poner plata grande por adelantado sin seña. Meta: el primer millón, por etapas.

### Ideas grandes de crecimiento (1-oct, para que Martin elija; ninguna arrancada)
1. Licencia de contratista certificado de Florida (DBPR/CILB) con sus 20 años, o socio "qualifier": cobra directo al dueño.
2. Kit de precalificación (COI, W-9, referencias, capacidad, fotos) + alta en BuildingConnected, PlanHub y Procore.
3. Nicho de recertificación y reparación de hormigón en condominios (inspecciones obligatorias después de Surfside).
4. Certificación SBE de Miami-Dade + fianzas con garantía de la SBA: abre obra pública sin capital grande.
5. Vender el MOP Estimator / servicio de presupuestos en español a otros subcontratistas.
6. Marca personal en Instagram/YouTube en español ("Martin, el de la plomada") + perfil de Google.
7. Alianza con una constructora con licencia (MOP hace estructura, ellos el permiso).
8. Sistema propio de encofrado reutilizable para bajar costo en hormigón.

## Sistema de asistentes (prompt maestro del 13-oct-2026, hecho el 14-oct)
- `TABLERO.md`: canal entre Claude Code, Claude chat de texto y Claude voz (obras, mensajes, anticipación, decisiones).
- `OBSERVACIONES.md` + gancho Stop (`.claude/hooks/decidir_habilidades.py`): el agente crea habilidades solo.
- `HABILIDADES.md`: registro. Habilidades nuevas: estado-de-obra, anticipar, cuestionar, explorador (activas),
  instagram-lectura (pendiente de conexión). Comandos: /estado, /habilidades, /activar, /apagar, /explorar, /expansion.
- Explorador: `EXPLORADOR/` (campos, hallazgos, en-espera, mapa-expansion). Tarea programada "Explorador MOP:
  /explorar semanal" (trig_01WURKDzQ4TtQBpYgVd8qqDP), domingos 20:50 Miami, sesión nueva sin conectores.
- fabrica-canales: proyecto separado (3 canales con presentador virtual). Repositorio privado
  martinoliveraprietto-max/Fabrica-canales- (lo creó Martin el 14-oct; desde la nube no se puede crear). Código subido.
- Arreglos de la nube: edge-tts viejo da 403 → `pip install --upgrade edge-tts` (ya en el gancho de instalación);
  pyswisseph no compila → antes `pip install --upgrade setuptools`.
- Gmail 14-oct: Flagler ENVIADA el 9-oct (EST-2026-004); Sedano's #32 (Fortum) vence 21-oct; Galleria Mall (Fortum,
  5-oct) sin contestar; Blue Door (632 SW 8th St) planos del 18-sep.

## Dónde está cada cosa
| Qué | Dónde |
|---|---|
| Plan maestro de memoria (Cerebro MOP, aprobado y armado el 1-nov-2026) | `CEREBRO_MOP.md`; página en vivo para el celular: https://claude.ai/artifact/4jYsyGxKuV3K8VBcKzDyMU |
| Página web | este repo (`index.html`, `img/`), en línea: https://martinoliveraprietto-max.github.io/Mop-construccion/ |
| Instagram (cola, reels, textos, perfil) | este repo, `instagram/` y `scripts/publicar.py`, `scripts/hacer_reel.py` |
| Logo elegido (plomada que baja por la O) | este repo, `marca/` |
| Emails a constructoras | solana-signal-bot, `mop-app/email/` (en main desde el 1-oct; se trabaja en la rama `claude/mop-construction-website-djmiog`) |
| Planos en PDF (S-1 a S-5) | solana-signal-bot, `mop-app/planos/` (main y rama de trabajo; reglas en `planos/REGLAS.md`) |
| MOP Estimator (app de presupuestos) | repositorio privado `martinoliveraprietto-max/mop-estimador` (antes `mop-app/estimador-nuevo/`) |
| MOP Construction OS (gestión de obra) | dentro de `mop-estimador` (decisión 30-sep): documentos en `docs/os/` (en main) |
| Habilidad para leer planos y sacar cantidades | solana-signal-bot, `.claude/skills/leer-planos` |
| Fotos y videos nuevos de Martin | Google Drive, carpeta "Mop instagram" |

## Variables de entorno que tienen que estar (Editar entorno → variables, una por línea)
- `INSTAGRAM_TOKEN` (empieza con IGAA; se saca en developers.facebook.com → MOP Publicador →
  Casos de uso → lapicito → "2. Generar tokens de acceso" → Generar token). Dura 60 días.
- `EXPO_TOKEN` (lo usa el MOP Estimator). NO borrarlo al agregar otras.
- Si se borra una línea, se rompe lo que la usa: el 28-sep se borró la de Instagram por error.

## Estado por tema (29-sep)
### Web
- En línea, unificada. Galería de 12 fotos (pedido de Martin 27-sep): fuera todas las fotos con gente
  sin casco o en altura sin arnés; lista en `pruebas/fotos_fuera_de_la_web.txt`. Pruebas:
  `python3 pruebas/prueba_sitio.py` y `node pruebas/prueba_navegador.js`.

### Instagram
- Rutina "Instagram MOP: publicar" (trig_01VgsrELobr1sunwZtMWVMwr): lunes, miércoles, viernes y
  sábado 7:44 pm Miami, publica la siguiente de `instagram/cola.json` (fotos, carruseles y Reels).
- Publicadas: 01, 02, Reel 01 y Reel 03 (30-sep). Las 6 con gente quedaron con estado `revision_martin`
  en cola.json (la rutina las saltea); para liberarlas, volver a poner `pendiente`.
- El lunes 28 no salió nada: faltaba el token (Martin lo generó de nuevo el 28-sep por la noche y lo
  cargó en el entorno; funciona desde el 30-sep).
- PENDIENTE DE MARTIN: 6 publicaciones de la cola tienen gente sin casco o sin arnés: posts 03, 04,
  07, 08 y Reels 02 y 04. Decidir: publicar, recortar o sacar. Mientras tanto se publican solo las
  que no tienen gente (Reel 03, posts 05, 06, 09). El Reel 01 ya publicado también tiene gente en altura.
- Perfil: foto con el logo ya cambiada. Falta nombre, biografía y enlace (texto en
  `instagram/perfil/perfil.txt`) y archivar 6 posts viejos (lista en ese archivo).

### Emails a constructoras
- 28-sep: salieron 200 de 202 de obra nueva (texto v3, texto simple). 17 bajas (rebotes y "remove"),
  en `bajas.csv`: nunca volver a escribirles. Registro en `envios.csv`.
- Remodelación (84): texto propio aprobado por Martin; envío programado martes 29-sep desde 8:01.
- Correo de seguimiento (`seguimiento.txt`): escrito, NO aprobado todavía.
- Respuesta real: Daniel Burunat, gerente de proyecto de Vercetti Enterprises (Doral), invitó a
  cotizar "North Beach Entrance Signs" (fundaciones y estructura; Harding Ave & 87th St y Normandy
  Dr & Bay Dr), con 2 planos estructurales en el mail del 28-sep. Falta: leer planos, cantidades y
  propuesta; se manda solo con aprobado de Martin.
- Borradores en Gmail a proveedores de concreto y fundaciones (29-sep): no enviados.

### Planos
- S-1 a S-5 hechos desde croquis de Martin (inglés, marcan VERIFY lo que falta). S-5 (28-sep): viga
  de amarre nueva 8x12 sobre puerta nueva 39x81, pared de madera 2x6 y losa subida; faltan medidas.
- Regla (28-sep): cada plano con medidas confirmadas va con hoja aparte de materiales y precios, con
  la fuente de cada precio; si no hay precio, "PRECIO A CONFIRMAR".

### MOP Construction OS (30-sep)
- Martin aprobó hacerlo dentro del MOP Estimator (privado). Hecho: auditoría y plan (`docs/os/`), 3 errores de la base
  arreglados, núcleo de la obra en la base real (roles, tareas, materiales, RFI, órdenes de cambio, partes diarios,
  inspecciones, historial), "Centro de mando" y "Parte del día" en la app.
- 30-sep: Martin dijo que sí. Rama juntada con main del Estimator y pantallas publicadas en su celular (eas update,
  canal preview). Próximo: formularios de tareas, materiales, RFI y órdenes de cambio.

### Licitaciones de Fortum Construction (Nicole Swanton, 30-sep)
- Regla de Martin (30-sep): toda obra que se estima va COMPLETA a la app (plano, 3D, piezas, presupuesto con por qué).
- 1044 W Flagler: visita a obra lunes 5-oct 12:00 (Martin confirmó); precio vence viernes 9-oct. Cálculo en
  `mop-estimador/obras/1044-flagler/`. 1-oct: COMPLETA en la app ($85.754, 3D de 37 piezas).
- 298 Lincoln Rd, fase 2 (fachada y cascarón): presupuesto PRELIMINAR de la parte de MOP en
  `mop-estimador/obras/298-lincoln/` ($53.562 con precio; falta el hormigón 6000 psi y otros). La estructura del juego
  dice "not for construction": 12 preguntas a Nicole programadas para el 1-oct 8:01 (borrador en Gmail). COMPLETA en
  la app (3D, piezas, presupuesto con por qué). Acero pedido a Diana (Nu-Vue); soldadura: Dani Soldador (WhatsApp).
- Kilwins (1390 Ocean Dr #105): vence miércoles 14-oct; plano bajado (29 hojas), sin medir.
- Sedano's #32 Shell Space (Fortum, 14655 SW 56th St): vence miércoles 21-oct. 15-oct: 3D COMPLETO en la app (en main
  de mop-estimador, `obras/sedano-32/`): todas las etapas del plano (demolición, estructura con hierro, acero, framing,
  techo, plomería, electricidad, aire, cielorrasos, puertas, vidriera; rociadores y alarma no vienen en el juego).
  Versión para el cliente en inglés, video por etapas y fotos con render de Blender. Pedido de acero a Nu-Vue en
  Borradores, sale el 16-oct 7:30 (tarea programada), con el plano por enlace propio de la app (30 días).
  Llave permanente de la app creada (vence oct-2027): falta que Martin la guarde en el entorno como MOP_LLAVE.
- 1-oct, 8:02 Miami: ENVIADAS las 12 preguntas a Nicole (hilo "ITB: 298 Lincoln Rd - Phase 2"). Esperando respuesta.
- Falta: Lincoln en 3D "terminada" (como Flagler: baños con artefactos, ascensor, escalera, fachada) y
  respuesta de Diana (acero) y Dani Soldador (precio por trabajo).
- Rojas: en el Drive solo está la Rev. aprobada del 23-jun-2026; el original ("Proyecto rojas.pdf", OneDrive personal)
  no se puede bajar desde la nube: Martin lo tiene que subir por la app.

## Lo que se resolvió en el chat principal (23 al 30-sep)
Pasado a `archivo/HISTORIA-chat-septiembre-2026.md` el 1-nov-2026.

## Problemas conocidos entre chats
- Varios chats trabajan a la vez sobre lo mismo: antes de mandar o publicar algo, hacer `git pull`
  y mirar `envios.csv`, `cola.json` y el Gmail enviado para no repetir. El 28-sep dos chats
  arrancaron el mismo envío de emails; uno se apagó para no duplicar.
- Un chat que arrancó antes de cambiar una variable de entorno no la ve hasta reiniciarse.
- Archivos que Martin manda por el chat (fotos, PDF, diseños 3D) solo los ve el chat donde los
  mandó. Para pasarlos a otro chat: subirlos a Google Drive ("Mop instagram") o mandarlos por mail
  a mopconstruccion@gmail.com, y decirle al chat nuevo dónde están.

## Auditoría del seguro (oct-nov 2026)
Puntero y cómo seguir: `auditoria-seguro/ESTADO.md`. Papeles entregados el 2-nov; se espera respuesta de la
auditoría; cierre antes de fin de noviembre. El detalle es privado y está en el Drive de Martin (documento 28).
