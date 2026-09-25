# MOP Construction — sitio web e Instagram

Responder SIEMPRE en español. Martin (dueño) habla desde el celular: pasos cortos, uno por vez.

## El negocio (datos reales, no inventar otros)
- MOP Construction and Service, Inc. — Dania Beach, FL — trabaja en Miami-Dade y Broward.
- Teléfono y WhatsApp: 754.457.3599 — correo: mopconstruccion@gmail.com
- Instagram: @mopconstruccion.inc — 20 años de experiencia — presupuesto gratis.
- Servicios: estructura (framing), drywall, pintura, pisos, carpintería de terminación, decks y exteriores.
- NO tiene licencia de contratista. No escribir "licensed", "general contractor" ni ofrecer "obra
  nueva" en textos nuevos. (La página todavía muestra "New construction & framing": se le avisó a
  Martin del riesgo legal en Florida; la decisión es suya.)
- Lema: "Your Vision. Built Solid." — Logo elegido: el de la plomada que baja por la O
  (archivos en `marca/`). Colores: negro #0d0c0a, dorado #c9a55a / #e6c97e, crema #f3ead6.
  Letras: Cinzel (títulos), Montserrat (texto), Cormorant Garamond itálica (lema).

## Qué hay en el repositorio
- `index.html` + `img/`: la página web (inglés con botón ES). Para verla en internet gratis:
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
2. Programar las siguientes (Routine lunes/miércoles/viernes).
3. Activar GitHub Pages y, si Martin compra dominio, conectarlo.
4. Conectar el formulario de la web a un correo (hoy solo avisa que llamen).
