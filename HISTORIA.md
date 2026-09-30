# MOP Construction — historia y estado de todo (leer esto PRIMERO en cada chat nuevo)

Actualizado: 29-sep-2026. Si cambiás algo importante, actualizá este archivo en `main`.

## Cómo arrancar un chat nuevo (Martin copia y pega esto)
> Leé `HISTORIA.md` y `CLAUDE.md` del repositorio Mop-construccion (rama main) y la carpeta
> `mop-app/` de solana-signal-bot (rama `claude/mop-construction-website-djmiog`) antes de hacer nada.
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
| Emails a constructoras | solana-signal-bot, rama `claude/mop-construction-website-djmiog`, `mop-app/email/` |
| Planos en PDF (S-1 a S-5) | misma rama, `mop-app/planos/` (reglas en `planos/REGLAS.md`) |
| MOP Estimator (app de presupuestos) | repositorio privado `martinoliveraprietto-max/mop-estimador` (antes `mop-app/estimador-nuevo/`) |
| MOP Construction OS (gestión de obra) | dentro de `mop-estimador` (decisión 30-sep): documentos en `docs/os/`, rama `ccr-2a44a709-iekn7h` |
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
- Publicadas: 01, 02, Reel 01. El lunes 28 no salió nada: faltaba el token (Martin lo generó de nuevo
  el 28-sep por la noche y lo cargó en el entorno).
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
  inspecciones, historial), "Centro de mando" y "Parte del día" en la app. Todo en la rama `ccr-2a44a709-iekn7h`.
- PENDIENTE DE MARTIN: mandar las pantallas nuevas a su celular (eas update) y juntar la rama con main.

## Problemas conocidos entre chats
- Varios chats trabajan a la vez sobre lo mismo: antes de mandar o publicar algo, hacer `git pull`
  y mirar `envios.csv`, `cola.json` y el Gmail enviado para no repetir. El 28-sep dos chats
  arrancaron el mismo envío de emails; uno se apagó para no duplicar.
- Un chat que arrancó antes de cambiar una variable de entorno no la ve hasta reiniciarse.
- Archivos que Martin manda por el chat (fotos, PDF, diseños 3D) solo los ve el chat donde los
  mandó. Para pasarlos a otro chat: subirlos a Google Drive ("Mop instagram") o mandarlos por mail
  a mopconstruccion@gmail.com, y decirle al chat nuevo dónde están.
