# MOP Construction — sitio web e Instagram

Responder SIEMPRE en español. Martin (dueño) habla desde el celular: pasos cortos, uno por vez.
Martin es uruguayo. Al final de cada respuesta, mandarle también un audio con lo importante, con voz
uruguaya de hombre: `edge-tts --voice es-UY-MateoNeural --text "..." --write-media respuesta.mp3` en el
directorio temporal de la sesión, y enviarlo como archivo. Pedido por Martin el 27-sep.

## El negocio (datos reales, no inventar otros)
- MOP Construction and Service, Inc. — Dania Beach, FL — trabaja en Miami-Dade y Broward.
- Teléfono y WhatsApp: 754.457.3599 — correo: mopconstruccion@gmail.com
- Instagram: @mopconstruccion.inc — 20 años de experiencia — presupuesto gratis.
- Servicios: estructura (framing), drywall, pintura, pisos, carpintería de terminación, decks y exteriores.
- NO tiene licencia de contratista. No escribir "licensed", "general contractor", "crew"/cuadrilla,
  cantidad de empleados, "roofing" ni ofrecer "obra nueva" como obra propia: se ofrece como
  subcontratista bajo el permiso de la constructora a cargo ("Framing for new construction").
- Nunca mostrar Hialeah. Ciudad visible: Dania Beach, FL. Español de la web: neutro con "tú".
- Domicilio legal (Sunbiz, desde el 27-sep): agente registrado comercial en St. Petersburg, FL.
  NO se muestra en la web (ahí solo va la ciudad, Dania Beach, sin calle). Solo va en el pie de los
  emails a constructoras. Nunca escribir la dirección de la casa de Martin en este repositorio (es público).
- Lema: "Your Vision. Built Solid." — Logo elegido: el de la plomada que baja por la O
  (archivos en `marca/`). Colores: negro #0d0c0a, dorado #c9a55a / #e6c97e, crema #f3ead6.
  Letras: Cinzel (títulos), Montserrat (texto), Cormorant Garamond itálica (lema).

## Qué hay en el repositorio
- `index.html` + `img/`: la página web (inglés con botón ES). Versión UNIFICADA el 25-sep: esta web
  más la de la sesión "MOP Construction" (formulario que abre WhatsApp, datos para Google, ícono de
  la plomada, sección "For builders", menú en celular). Antes de subir cambios, correr
  `python3 pruebas/prueba_sitio.py` y `node pruebas/prueba_navegador.js` (necesita playwright-core). Para verla en internet gratis:
  GitHub → Settings → Pages → Deploy from branch → main → / (root). Falta que Martin lo active.
- `instagram/cola.json`: las 9 publicaciones en orden, con su texto y su estado.
- `instagram/publicaciones/`: las imágenes (1080x1350). `instagram/destacadas/`: portadas de
  historias destacadas (la API no maneja destacadas: las sube Martin).
- `instagram/textos.txt`: los textos y el plan, para Martin.
- `scripts/publicar.py`: publica la siguiente pendiente con la API de Instagram.

## Material nuevo (fotos y videos)
- Martin sube a Google Drive, carpeta "Mop instagram" (id 19ul5QKrqcSqsnZGLbO2OI8BrTeRzGIIO).
- Todo gratis: editar video con FFmpeg (`pip install imageio-ffmpeg`, se reinstala en cada sesión).
  Nada de Adobe, vidIQ ni herramientas pagas.
- Plan: lunes foto/carrusel, miércoles Reel antes/después, viernes Reel de proceso.

## Fotos: seguridad (lo primero que miran las constructoras)
- No se publica (web ni Instagram) una foto con gente en obra sin casco, ni trabajando en altura
  sin arnés. Se recorta a la persona o se descarta. Nunca se agregan cascos con IA ni se borronea.
- Tampoco carteles, logos o licencias de otras constructoras, patentes, caras de clientes ni
  números de casa. Detectado por Washington Nieves el 27-sep: varias fotos ya publicadas tienen
  gente sin casco. El 27-sep Martin pidió sacarlas y dejar la galería en 12 fotos: las demás siguen
  en `img/` (las usan los Reels) y están listadas en `pruebas/fotos_fuera_de_la_web.txt`; la prueba
  del sitio frena si alguna vuelve a la página o si la galería deja de tener 12.

## Herramientas de este repositorio (.claude/)
- `/fotos`: carga fotos nuevas de punta a punta (revisión de seguridad, GPS, galería, pruebas).
- `/publicar`: sube a GitHub Pages con las pruebas en verde y confirma que la web cambió.
- Guardias automáticas: `guardia_publica.py` frena al escribir palabras prohibidas, direcciones
  de calle o tokens; `guardia_git.py` corre `prueba_sitio.py` antes de cada commit o push y frena
  si falla. Al arrancar cada sesión en la nube se instalan pillow, imageio-ffmpeg, yt-dlp y
  playwright-core.
- Videos de YouTube que manda Martin: leer los subtítulos con
  `yt-dlp --skip-download --write-auto-subs --write-subs --sub-langs "es.*,en.*" --sub-format vtt`.
  Solo trae lo que se dice, no lo que se ve. Si YouTube responde 429, esperar unos minutos.

## Cómo se publica
- App de Meta "MOP Publicador" (API con inicio de sesión de Instagram), cuenta de empresa,
  permisos instagram_business_basic, _content_publish, _manage_comments, _manage_insights,
  _manage_messages. La cuenta mopconstruccion.inc es evaluadora de la app.
- El token vive SOLO en la variable de entorno `INSTAGRAM_TOKEN`. NUNCA imprimirlo, escribirlo en
  archivos, commits ni mensajes. `publicar.py` lo tapa en los errores.
- Primero: `python3 scripts/publicar.py --verificar`. Después `--simular`. Después sin opciones.
- Después de publicar, `cola.json` cambia (estado, media_id, enlace): hacer commit y push a main.
- Plan: lunes, miércoles y viernes 7:45 pm hora de Miami (America/New_York), una por vez.
- El token dura 60 días. Renovarlo antes con
  `GET https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token=...`
  y pedirle a Martin que guarde el nuevo en el entorno. Martin decidió NO cambiar el token aunque
  se vio en una foto del chat: no volver a pedírselo.
- Comentarios: se pueden contestar los simples (agradecer, "call us at 754.457.3599"). Pedidos de
  precio y mensajes privados, pasárselos a Martin.

## Pendiente
1. (Hecho 25-sep) Token verificado y 01 publicada. Se sacó #Contractor de los textos.
2. (Hecho 25-sep) Rutina "Instagram MOP: publicar la siguiente foto" (trig_01VgsrELobr1sunwZtMWVMwr): miércoles y
   sábados 7:44 pm Miami, publica la siguiente de cola.json. Reels (instagram/reels/, hechos con
   scripts/hacer_reel.py) los publica Martin lunes y viernes desde la app, con música de tendencia.
   Perfil nuevo (foto con la plomada, bio, enlace) en instagram/perfil/perfil.txt: lo cambia Martin.
3. Activar GitHub Pages y, si Martin compra dominio, conectarlo.
4. Conectar el formulario de la web a un correo (hoy solo avisa que llamen).
