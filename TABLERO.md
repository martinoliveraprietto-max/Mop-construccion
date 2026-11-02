# TABLERO — canal entre asistentes de MOP

Creado: 13-oct-2026 (cargado el 14-oct). Lo leen y escriben tres asistentes:
- **Claude Code**: programa y ejecuta.
- **Claude chat de texto**: organiza el día, lee correo, calendario y Drive, arma fichas.
- **Claude voz**: decide con Martin y manda órdenes.

Reglas: nunca dos asistentes en la misma tarea. Lo que no está en una fuente va como "sin dato".
Este repositorio es PÚBLICO: acá van nombres de empresa y montos que ya están en HISTORIA.md,
nunca correos, teléfonos, direcciones de casa ni datos privados (esos van al Drive privado).

---

## Obras

Fuentes de esta carga: HISTORIA.md (1-oct) y Gmail (búsqueda del 14-oct).
Estados posibles: cotizando / propuesta enviada / ganada / en ejecución / cobrando / cerrada / perdida (con motivo).

### Rojas (Kozo Construction)
- Cliente y contacto: Kozo Construction, Felipe.
- Estado: en ejecución / cobrando (faltan 2 losas de hormigón y una escalera).
- Monto: contrato $135.000.
- Cobrado: ~$120.734 (si los $20.250 del 7-nov fueron la seña de Rojas; a confirmar).
- Por cobrar con fecha: ~$14.266 por contrato, o ~$30.000 si hay adicionales. Fecha: sin dato.
- Próximo paso con fecha: confirmar con Kozo el saldo real antes de facturar; armar cronograma y certificados de avance semanales. Fecha: sin dato.
- Riesgo: diferencia entre $14.266 y $30.000 sin aclarar. Seguro de responsabilidad civil RENOVADO (firmado el 12-oct, vigente desde el 15-oct, entrada ya pagada según Martin el 15-oct); falta pedirle a Pandora el certificado nuevo (Kozo lo pide para pagar) y confirmar si cubre hormigón antes de hormigonar. Plano original "Proyecto rojas.pdf" solo en OneDrive personal de Martin.

### Blue Door (632 SW 8th St)
- Cliente y contacto: Blue Door Contractors, Rodrigo (planos reenviados por Redline Consulting el 18-sep).
- Estado: cotizando (sin dato de avance después del 19-sep).
- Monto: sin dato.
- Cobrado: hubo un pago de Blue Door el 24-sep (referencia "632 Strux"), registrado en las finanzas privadas de Drive; a confirmar con Martin a qué trabajo corresponde.
- Por cobrar con fecha: sin dato.
- Próximo paso con fecha: Martin confirma si se cotiza y para cuándo. Sin dato de vencimiento.
- Riesgo: no figura en HISTORIA.md; el 19-sep Martin reenvió los planos a un tercero y no hay respuesta registrada.

### 1044 W Flagler (Fortum Construction)
- Cliente y contacto: Fortum Construction, Nicole Swanton.
- Estado: propuesta enviada (EST-2026-004, 9-oct).
- Monto: $85.754 según HISTORIA (1-oct). La versión final de la propuesta (v3 del 6-oct) es mayor: el número está en el Drive privado (Segundo cerebro 7) y en el PDF EST-2026-004.
- Cobrado: $0.
- Por cobrar con fecha: sin dato (no ganada).
- Próximo paso con fecha: Nicole dijo el 9-oct "follow up shortly". Seguimiento sugerido: jueves 16-oct si no responde.
- Riesgo: sin respuesta a 5 días; plomería se pidió a Redline el 8-oct (sin dato de respuesta).

### 298 Lincoln Rd, fase 2 (Fortum Construction)
- Cliente y contacto: Fortum Construction, Nicole Swanton.
- Estado: cotizando (presupuesto PRELIMINAR).
- Monto: $53.562 preliminar (falta hormigón 6000 psi y otros).
- Cobrado: $0.
- Por cobrar con fecha: sin dato.
- Próximo paso con fecha: respuestas de Nicole a las 12 preguntas (enviadas 1-oct), precio de acero (Diana, Nu-Vue), soldadura (Dani Soldador) y hormigón (pedidos el 5-oct a 8 proveedores). Fecha de entrega: sin dato.
- Riesgo: la estructura dice "not for construction"; National Shell no cotiza (obra chica para ellos).

### Kilwins (1390 Ocean Dr #105, Fortum Construction)
- Cliente y contacto: Fortum Construction, Nicole Swanton.
- Estado: propuesta enviada el miércoles 14-oct a Nicole (precio base, alternativa A de losa para plomería en dos variantes y alternativa 1 de muros perimetrales; válida 30 días). Montos en el correo enviado (Gmail, 14-oct). Nicole respondió el jueves 15-oct 11:49, pasó la propuesta a David y pregunta si MOP cotiza también las puertas.
- Monto: en el correo enviado el 14-oct (Gmail), no se copia a este repositorio público.
- Cobrado: $0.
- Por cobrar con fecha: sin dato (no ganada).
- Próximo paso con fecha: contar las puertas en Kilwins Combine CDs.pdf (cuadro de puertas y planta) desde la tablet, armar el adicional "puertas, marcos y herrajes" con marca estándar que cumpla el plano, materiales y mano de obra por separado, y contestarle a Nicole. Conectores Dayton D250XL: Nicole confirmó presupuestar cada 16" a cada lado de la zanja.
- Riesgo: falta saber si el flete está incluido en la cotización de techos de ACP Ideas (QUO-11567); sin recorrido de obra (local ocupado).

### Galleria Mall Renovation (Fortum Construction)
- Cliente y contacto: Fortum Construction, Nicole Swanton (invitación del 5-oct, después de conocerse en persona).
- Estado: cotizando (sin respuesta registrada de MOP).
- Monto: sin dato.
- Cobrado: $0.
- Por cobrar con fecha: sin dato.
- Próximo paso con fecha: contestarle a Nicole qué partidas se cotizan (ella pidió incluir puertas). Vencimiento: sin dato.
- Riesgo: invitación sin contestar desde hace 9 días.

### Otras que aparecieron en Gmail (no pedidas en la carga, se anotan para no perderlas)
- Sedano's #32 Shell Space (Fortum): MOP confirmó propuesta para el miércoles 21-oct. Nicole preguntó el 13-oct si MOP y su socio mandan una propuesta juntos o separadas: la respuesta la manda Martin con Dani; ningún asistente la redacta.

---

## Mensajes entre asistentes
Formato: fecha · quién escribe · qué hizo · qué detectó · qué le toca al siguiente.
Los mensajes hasta el 24-oct están en `archivo/TABLERO-mensajes-hasta-24-oct-2026.md`.

- 29-oct-2026 · Claude Code · Web EN PAUSA hasta después de la auditoría (pedido de Martin): una sola página con una foto de carpintería y los datos de contacto; la web completa está en el commit 855698a (para volver: restaurar index.html de ese commit). Las pruebas aceptan el modo pausa. La publicación automática de Instagram ya estaba apagada desde el 17-oct · Instagram todavía tiene publicaciones con techos (una dice "From dirt to roof"); los correos del cazador llevan el enlace a la web en pausa · Martin: archivar desde la app las publicaciones con techos; después del 3-nov decidir si se vuelve a la web completa.
- 28-oct-2026 · Claude Code · Auditoría del seguro: póliza leída entera (resumen textual en archivos privados de la sesión, no en el repo); 12 meses de banco listos y verificados; borradores de cuestionario y ventas por mes · La póliza está clasificada como remodelación residencial con ventas estimadas muy por debajo de lo real: va a haber prima adicional; exige certificado de seguro de cada subcontratista; la clase puede no calzar con estructura para obra nueva · Martin: hablar con Pandora antes de la llamada de NEIS del 3-nov; decidir dudosos; pedir reporte bruto a Liberty y certificados de los dos subcontratistas grandes; subir todo el 2-nov.
- 29-oct-2026 · Claude Code · Leí el reel que mandó Martin (cuenta de IA, "11 skills de Claude para operar en bolsa") con yt-dlp; anoté el camino en instagram-lectura · no es para MOP tal cual; la idea útil es simular el presupuesto muchas veces antes de mandarlo · Martin: decir si quiere el simulador de margen en mop-estimador.
- 1-nov-2026 · Claude Code · Con el "aprobado" de Martin instalé humanizer y 4 de social-media-skills (hook-generator, post-formatter, content-matrix, post-writer), leídas antes (solo texto, sin programas), adaptadas a MOP y registradas en HABILIDADES.md. Dejé afuera las que piden Gemini o Apify pagos y las de LinkedIn · nada · Martin: decir si el texto nuevo del Reel 02 reemplaza al de cola.json.
- 1-nov-2026 · Claude Code · Leí 3 reels de memoria (claude-obsidian, segundo cerebro, araña) y armé el plan maestro `CEREBRO_MOP.md` (3 niveles, fichas en Supabase, araña que aprende, bots incluidos, fases del 1 al 16-nov) · el gancho de inicio se corta a 2 KB: los chats nuevos no ven el TABLERO · Martin: aprobar la fase 0 (CALIENTE.md) y la fase 1.
- 1-nov-2026 · Claude Code · Cerebro MOP armado (Martin: "hacé todo hoy"): CALIENTE.md y gancho de inicio de 1,6 KB (antes 16 KB cortados), habilidad memoria, buscar-papeles v2, herramientas/memoria.py y transcribir.py, TABLERO e HISTORIA adelgazados (lo viejo en archivo/), tarea de las 6:27 con el paso 7 (memoria y cartel; ahora puede subir solo CALIENTE.md) · Martin corrió la migración desde el editor de Supabase (el aviso no aparece en el celular); 30 fichas y 30 hechos cargados y búsqueda probada · mañana 6:27 primera corrida con el paso 7: revisar que suba CALIENTE.md.
- 1-nov-2026 · Claude Code · Portero (Martin: "aprobado, hacé todo"): astrólogo pasa a Haiku; tablero 6:27, explorador y anticipador a Sonnet (antes Fable o el modelo por defecto); el vigilante sigue con el principal (lee planos y estima). Mod "cerebro-mop": panel con CALIENTE.md y comando /cerebro; copia en `mods/cerebro-mop/` · las tareas de sesión fija (aviso de fallas, /mejorar, informes del multiactivo) no cambian de modelo desde acá · mañana 7:15 revisar la primera corrida del tablero con Sonnet.
- 1-nov-2026 · Claude Code · Página "Cerebro MOP" en claude.ai para el celular (el panel del mod no se ve en el teléfono): lee en vivo las fichas y la tabla tablero de Supabase con la conexión de Martin; enlace en HISTORIA.md y CEREBRO_MOP.md · Martin: abrirla y decir si se ve bien.
- 1-nov-2026 · Claude Code · Memoria para todo Claude (Martin: "dale"): mop-estimador muestra CALIENTE.md al arrancar y tiene la habilidad memoria (main 835bc59); la tarea de las 6:27 pone arriba del TABLERO de Martin el bloque CEREBRO MOP (enlace y 5 urgencias); a Martin se le pasó la frase para sus preferencias de claude.ai · ojo: el CLAUDE.md de mop-estimador pesa 75 KB, conviene adelgazarlo · Martin: pegar la frase en Ajustes.
- 1-nov-2026 · Claude Code · Creé la habilidad mesa (Martin: "dale, armá la habilidad mesa"): 3 coaches con métodos probados sobre los datos de la memoria, abogado del diablo y recomendación; primera prueba con Call Your Mother Deli · Martin: decidir CYM antes del jueves 5-nov.
- 1-nov-2026 · Claude Code · Martin pidió cerrar este chat y abrir otro: traspaso en `archivo/TRASPASO-2026-11-01.md` (qué se hizo y qué queda) · el chat nuevo arranca leyendo ese archivo · chat nuevo: revisar la corrida de las 6:27 del lunes a las 7:15 y preguntar por Call Your Mother Deli.
- 1-nov-2026 · Claude Code (chat nuevo) · Martin aprobó la recomendación de la mesa para Call Your Mother Deli: anotada en Decisiones y en la memoria; revisión de la tarea 6:27 programada para el lunes 7:15 de Miami · Martin: plano a la bandeja el lunes a la noche.
- 2-nov-2026 · Claude Code · Revisé la primera corrida de la tarea 6:27 con Sonnet: escribió 2 hechos en la memoria y el bloque CEREBRO MOP en el TABLERO de Martin; NO pudo subir CALIENTE.md (no le apareció add_repo y el clon público dio 403 al subir). Lo rehice y subí desde este chat · Martin: agregar el repositorio Mop-construccion a la tarea 6:27 para que suba sola.
---

## Anticipación
Conectores, habilidades, datos o permisos que van a hacer falta. Estado: listo / pendiente de conexión / pendiente de Martin.

1. **Instagram por la API oficial de Meta (leer reels guardados y publicar)** — 14-oct.
   - Publicar: listo (app "MOP Publicador", token en `INSTAGRAM_TOKEN`).
   - Leer "guardados": la API de Instagram NO da acceso a las publicaciones guardadas de la cuenta (no existe ese permiso). Caminos: (a) Martin comparte cada reel al chat o a la carpeta de Drive "Mop instagram"; (b) colección guardada → copiar el enlace y pasarlo; (c) leer reels públicos de otras cuentas con Business Discovery (solo cuentas de empresa o creador; necesita la variante de la API con inicio de sesión de Facebook).
   - Esqueleto: `.claude/skills/instagram-lectura/SKILL.md` (pendiente de conexión).
   - Documentación oficial: https://developers.facebook.com/docs/instagram-platform
2. **Gmail, Google Calendar y Google Drive en Claude Code** — 14-oct.
   - Verificado en esta sesión: los tres conectores de la cuenta de claude.ai están disponibles (se leyeron Gmail, Calendar y Drive). Estado: listo.
   - Si una sesión nueva no los ve: escribir `/mcp` en Claude Code y revisar en claude.ai → Configuración → Conectores.
   - Límite: el conector de Drive no edita planillas (se recrean).
3. **fabrica-canales** — 14-oct. Repositorio creado por Martin el 14-oct: martinoliveraprietto-max/Fabrica-canales- (privado), código subido. Faltan: ANTHROPIC_API_KEY (pago, espera aprobado), YOUTUBE_API_KEY (gratis), OAuth de YouTube por canal, 3 canales de YouTube y 3 cuentas de TikTok, app de TikTok con Content Posting API. Detalle en `CONEXIONES.md` de ese repositorio.
4. **Medición de planos con IA (explorador, 14-oct)** — prueba gratis de Kreo o BuildVision. Antes: permiso de Fortum para subir el plano. Pendiente de Martin.
6. **Bandeja de obras (Gmail → Drive → Claude Code)** — HECHO 14-oct. Apps Script en la cuenta mopconstruccion (código en mop-estimador `herramientas/bandeja_gmail.gs`), revisa Gmail cada 15 minutos, instalado el 14-oct 0:43 (hay otro proyecto vacío en la cuenta personal, borrable). El vigilante trig_01JZwaH6KFa8wqJuh9cEPhk6 ya tiene el repositorio mop-estimador y Gmail, Google Drive y Supabase conectados (Martin, 14-oct 0:53). Ronda manual de las 0:55: terminó bien; procesó 6 mensajes (cotización ACP de Kilwins cargada en precios; Whitecap pide conectores Dayton; Sedano's: bajar el plano a mano; Pandora y PES no son de obra) y lo anotó en `avisos/bandeja.md` (commit 00eb89c). Los enlaces de SharePoint no se bajan solos: se avisa "bajar a mano". Ojo: el Drive de mopconstruccion está casi lleno.
7. **Cazador de obras** — CONSTRUIDO v1 el 15-oct (antes: pendiente de construir, diseñado por Martin con Claude voz el 14-oct). Vive en mop-estimador: código `cazador/`, habilidad `/cazador`, entregas en `avisos/cazador/`. Tarea programada "Cazador de obras MOP" (trig_01DVi8HeUEPH8vKFzYb5annP), lunes a viernes 7:55 de Miami. Faltan: (a) Martin agrega Gmail y Google Drive a esa tarea en claude.ai (sin eso no lee correo ni deja borradores); (b) la dirección postal de MOP para el pie de los correos (ley CAN-SPAM); (c) fuente fresca de Broward (Fort Lauderdale dejó de actualizar en marzo) y de la ciudad de Miami con constructora.
   - Cuatro fuentes: permisos aprobados de Miami-Dade y Broward; licitaciones chicas de ciudad, condado y escuelas sin fianza; correo de constructoras que ya invitaron o respondieron (Fortum, A-Line, White Hawk, Cetoute) con seguimiento a los dos días; fotos de camionetas y carteles de la calle.
   - Filtro de cuatro reglas: (1) zona Miami-Dade y Broward; (2) rubros de MOP: framing de madera y metal, hormigón estructural, drywall, pintura, pisos, carpintería, decks; remodelación completa pasa; solo eléctrico, plomería o techo se descarta; (3) tamaño entre 10.000 y 150.000 dólares para la parte de MOP; sin cifra pasa marcado "tamaño sin dato"; (4) si es hormigón o exterior y el seguro no lo cubre, pasa con aviso en rojo.
   - Entrega: cada mañana máximo cinco oportunidades con constructora, contacto, trabajo y correo borrador. Nada se manda sin "aprobado".
   - Cada semana anota a quién se escribió, quién contestó y quién dio obra, para aprender qué constructoras responden.
8. **Máquina de cotizar en 24 horas** — pendiente de construir (diseñada por Martin con Claude voz, 14-oct). Cinco pasos:
   1. Recibir: la bandeja de obras ya lo cubre. Al llegar una invitación: carpeta de la obra en Drive, bajar planos, ficha con los renglones fijos del tablero, estado "cotizando", aviso en una línea.
   2. Leer planos con MOP Estimator: medidas, cantidades, rubros. Lo dudoso va "sin dato" y se convierte en la lista de preguntas a la constructora, en borrador para el "aprobado" ese mismo día.
   3. Precios: materiales con el catálogo de Home Depot cargado y la lista de Nu-Vue para acero; mano de obra con las horas por rubro del equipo y el precio por hora de Martin. Si falta un precio: pedido de cotización al proveedor en borrador y renglón marcado "estimado" hasta que llegue.
   4. Armar la propuesta en el formato que ya usa MOP: alcance, inclusiones, exclusiones, precio por rubro, seña del 30 % y cobro por avance, más una hoja aparte para Martin con el "por qué" de cada precio. Revisa el seguro y marca en rojo hormigón o exterior.
   5. Cerrar el ciclo: Martin revisa medidas y aprueba; correo de envío en borrador; seguimiento listo a los dos días; cuando se gana o se pierde, anota el motivo y compara el precio contra lo que pasó.
   - Prueba más chica: Kilwins. Si en un día saca ficha, preguntas y borrador de propuesta, funciona.
9. **Agente de caja** — solo idea registrada, diseño pendiente (14-oct; Martin lo está diseñando con Claude voz). Leer movimientos del banco y el Libro de caja, separar personal de empresa, aplicar los porcentajes de cada cobro, y cada viernes tres números: cobrado, por cobrar con fecha, sueldo disponible. Avisar cuándo facturar el avance de cada obra.
10. **Agente de licencia** — solo idea registrada, diseño pendiente (14-oct). Diez preguntas por día del examen CILB con puntaje, y armado del kit de precalificación en paralelo.
   - 15-oct (Martin): hay oportunidad de licencia de contratista general (CGC) por un calificador (qualifier), con dos candidatos: Danny Ruiz (Bello Construction; en los permisos del condado figura "BELLO CONSTRUCTION LLC" con dos licencias, CBC1261211 y CGC1526216, a confirmar cuál es la suya) o el amigo de Washington Nieves del proyecto del puente (nombre y licencia: sin dato). Estado: pendiente de Martin.
   - Lo que dice la ley (F.S. 489.119 y 489.1195, leídas el 15-oct): el calificador firma que tiene la aprobación final de toda la obra Y de todo lo financiero de MOP (contratos, cheques, pagos), salvo que la junta apruebe a Martin como "financially responsible officer"; responde por la supervisión de todas las obras; si ya califica otra empresa, la junta decide si lo deja calificar una segunda (tiene que mostrar que puede supervisar las dos); si se va, MOP tiene 60 días para reemplazarlo y no puede contratar mientras tanto; el número de licencia va en cada propuesta, publicidad y camioneta. Prestar la licencia sin supervisar de verdad es infracción.
   - Para decidir (habilidad cuestionar): quién firma los cheques, cuánto cobra el calificador, qué pasa si se pelean, y si conviene más rendir el examen CILB con los 20 años de oficio (camino propio, sin depender de nadie).
   - Orden de construcción decidido por Martin (14-oct): primero la máquina de cotizar (hay invitaciones de Fortum esperando), después el cazador, después caja, después licencia.
   - Todos encadenados: el cazador alimenta la máquina de cotizar, la máquina alimenta caja, y el tablero muestra el embudo con números cada viernes: invitaciones, cotizadas, ganadas, cobrado.
5. **edge-tts** — 14-oct: dio error 403 con la versión vieja; se arregla con `pip install --upgrade edge-tts`. Listo.

---

## Decisiones
Formato: fecha · decisión · qué se esperaba · qué pasó (se completa a los 30 días).

- 1-nov-2026 · Call Your Mother Deli (Fortum): se cotiza, con condición (recomendación de la mesa, aprobada por Martin). RememBR va primero; lunes 2-nov a la noche plano a la bandeja; martes llamar a Fortum por CYM y las 3 propuestas que esperan; miércoles propuesta solo con lo de MOP · Esperado: propuesta entregada antes del jueves 5-nov sin atrasar RememBR · Qué pasó: revisar el 1-dic-2026.
- 13-oct-2026 · Arranca el proyecto fabrica-canales (prueba de 60 días, meta: un canal con 1.000 suscriptores; si a los 30 días ningún canal crece, se para) · Esperado: canal que crezca sin trabajo de Martin · Qué pasó: revisar el 12-nov-2026.
- 13-oct-2026 · Sistema de asistentes con tablero y habilidades que se crean solas · Esperado: menos pedidos repetidos y nada vencido sin aviso · Qué pasó: revisar el 12-nov-2026.
- 15-oct-2026 · Los videos y el 3D para el cliente llevan SIEMPRE render profesional (Blender, materiales y luces reales), en todas las obras · Esperado: que el cliente vea la obra terminada como una foto real y eso ayude a ganar trabajos · Qué pasó: revisar el 14-nov-2026.
- 16-oct-2026 · Claude Code · Ciclo cerrado del cazador (pedido de Martin: "que el cazador también mande los emails… y cierra el ciclo"): la corrida de la mañana deja en una cola el primer correo a cada constructora con correo comprobado; el vigilante (9:43 y 13:43, tiene Gmail) lo manda, mira las respuestas y las anota (pidió no escribir, contestó, invitó a cotizar); si mandan planos, la bandeja los lleva a Drive y el vigilante arma la obra en la aplicación con presupuesto, 3D y piezas. Frenos: solo correos de la página de la empresa, máximo 5 por día, días hábiles de 9 a 17, nunca a las constructoras conocidas, uno cada 30 días, interruptor para frenar todo. Decisión de Martin anotada: es la única excepción al "mandalo"; precios y propuestas siguen con su aprobación. 5 pruebas nuevas, 147 en verde, en main de mop-estimador · sin la dirección postal de MOP no sale ningún correo (la ley la exige) · Martin: pasar la dirección postal comercial (no la de la casa); Claude voz: avisar a Martin cuando un constructor invite a cotizar.
