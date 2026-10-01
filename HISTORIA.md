# MOP Construction — historia y estado de todo (leer esto PRIMERO en cada chat nuevo)

Actualizado: 1-oct-2026. Si cambiás algo importante, actualizá este archivo en `main`.

## Cómo arrancar un chat nuevo (Martin copia y pega esto)
> Leé `HISTORIA.md` y `CLAUDE.md` del repositorio Mop-construccion (rama main) y la carpeta
> `mop-app/` de solana-signal-bot (rama main; la de trabajo es `claude/mop-construction-website-djmiog`) antes de hacer nada.
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

## Dónde está cada cosa
| Qué | Dónde |
|---|---|
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
- Rojas: en el Drive solo está la Rev. aprobada del 23-jun-2026; el original ("Proyecto rojas.pdf", OneDrive personal)
  no se puede bajar desde la nube: Martin lo tiene que subir por la app.

## Lo que se resolvió en el chat principal "MOP Construction: logo profesional, web y email" (23 al 30-sep)
- Logo: el de la plomada que baja por la O (no hacer más propuestas). Archivos en `marca/` y `mop-app/logo/elegido/`.
- Web: se unificaron las dos webs, se sacaron fotos repetidas, se sumaron fotos de Instagram (galería
  luego reducida a 12 por seguridad), formulario que abre WhatsApp, sección "For builders".
- Instagram: publicación por la API (fotos, carruseles y Reels). Reels hechos con `scripts/hacer_reel.py`
  (1080x1920, sin música; Martin puede agregar música de tendencia desde la app): 01 "From dirt to roof",
  02 "Before the pour" (rehecho sin la acera que no le gustó), 03 "Empty shell to office", 04 "Going up: two stories".
  Recomendaciones de perfil dadas a Martin: nombre "MOP Construction | Framing", biografía de `perfil.txt`,
  enlace a la web, pasar a cuenta de empresa (categoría Construction Company, botones Llamar y WhatsApp,
  SIN dirección), historias destacadas (Framing, Concrete, Interiors, Before/After, Contact).
- Emails: lista de 562 constructoras sacada del registro del DBPR + webs (286 listas: 202 obra nueva,
  84 remodelación). Se descartaron oficios sueltos (plomeros, electricistas, jardinería). Texto v1 y v2
  (con logo) reemplazados por la v3 de texto simple (asunto con el nombre de la empresa, pedido de entrar
  a su lista de subcontratistas). Armador: `mop-app/email/armar_correo.py`; registro: `envio.py`.
- Dirección postal: se descartó PO Box y UPS Store; quedó la dirección comercial de Sunshine (suite propia).
  Pausado y no urgente: formulario 1583 del correo (USPS) para el reenvío de correspondencia; falta un
  comprobante de domicilio a nombre de Martin con la dirección actual (seguro de inquilino o licencia
  actualizada en MyDMV). Revisar en Sunbiz que "Principal Address" y "Mailing Address" ya no digan Hialeah.
- Planos (inglés, desde croquis): S-1 viga, columna y zapata; S-2/S-3 muro de entrada con celdas llenas
  #5 con epoxi (los muros NO se unen, el vano queda); S-4 columnas 8x12 y viga nueva 8x12; S-5 viga sobre
  puerta nueva. Scripts en `mop-app/planos/*.py` (base común `plano.py`).

## Problemas conocidos entre chats
- Varios chats trabajan a la vez sobre lo mismo: antes de mandar o publicar algo, hacer `git pull`
  y mirar `envios.csv`, `cola.json` y el Gmail enviado para no repetir. El 28-sep dos chats
  arrancaron el mismo envío de emails; uno se apagó para no duplicar.
- Un chat que arrancó antes de cambiar una variable de entorno no la ve hasta reiniciarse.
- Archivos que Martin manda por el chat (fotos, PDF, diseños 3D) solo los ve el chat donde los
  mandó. Para pasarlos a otro chat: subirlos a Google Drive ("Mop instagram") o mandarlos por mail
  a mopconstruccion@gmail.com, y decirle al chat nuevo dónde están.
