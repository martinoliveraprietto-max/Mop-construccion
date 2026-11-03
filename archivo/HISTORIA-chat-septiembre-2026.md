# HISTORIA — lo resuelto en el chat principal del 23 al 30-sep-2026 (archivo)

Pasado acá el 1-nov-2026 (Cerebro MOP) para que HISTORIA.md quede liviano. No se borró nada.

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

### Decisiones de Martin (1-oct, chat de la tarde)
- North Beach (Vercetti, obra pública de Miami Beach): NO se cotiza. Se le escribe a Daniel Burunat con
  elegancia (borrador en el chat, espera "aprobado") y se avisa a los proveedores que estaban cotizando
  (Florida Foundation, GSI, Expert Dewatering, Deco Truss, Valmont, Manley deBoer). Sirvió para aprender y contactos.
- Cuenta de Oracle Cloud "mopconstruccion" (región São Paulo): la abrió Martin, no es sospechosa.
- Shell Lumber mandó precios por pieza (PDF): van como respaldo de precios de la app.
- North Beach SÍ se cotiza (Martin cambió de idea): presupuesto real en mop-estimador, rama
  claude/north-beach-propuesta-real (obras/north-beach/propuesta-v2-*). Total $1.168.470 (unos $682.000 son
  asignaciones; micropilotes ~$453.000). Mano de obra con salario de obra pública (tabla Miami-Dade 2026, Miami Beach
  ord. 2021-4405) + 28,3 % de cargas = $50,25/h; cuadrilla de 10; herramientas $2.004/semana. Martin pidió NO mandar
  ni programar nada el 2-oct: revisarlo primero.
- Seguros (verificado 1-oct con el certificado): responsabilidad civil Burlington Ins Co por Pandora Insurance,
  1M por hecho / 2M total, vigente 15-oct-2025 a 15-oct-2026 (RENOVAR; el certificado todavía muestra el domicilio
  viejo de Hialeah: pedir a Pandora que lo cambie). Sin seguro de autos ni umbrella. Workers' comp por PES /
  Liberty Employee Leasing (PEO): el certificado vencía 1-oct-2026, pedir el nuevo. Martin tiene exención de
  dueño (oct-2025): confirmar con PES si él figura cubierto. Sin fianza.

### Memoria para el Claude de voz (1-oct)
- Google Doc privado "Segundo cerebro MOP — memoria para Claude (privado)" en el Drive de Martin
  (id 1iTdNSYY2e5tbFdMwU_WrMqycdeA5a_Sm_XcSQtt_hcY): resumen de esta historia sin datos técnicos. Mantenerlo al día
  cuando cambie algo importante. Paso 2 pendiente: Martin crea el proyecto "Segundo cerebro MOP" en la app de Claude
  y le agrega ese documento.

### Obra en curso y clientes fuertes (1-oct)
- Kozo Construction (Felipe), obra Rojas: los ~$30.000 que faltan (2 losas de hormigón y una escalera) son
  el saldo del contrato Rojas. Ojo: contrato $135.000 y cobrado ~$120.734 (si los $20.250 del 7-nov son la seña
  de Rojas) → por contrato quedarían ~$14.266; confirmar con Kozo el saldo (¿adicionales?) antes de facturar. Es la plata más cercana: armar cronograma, certificados de avance semanales y pedir adelanto para
  materiales. Antes de hormigonar: confirmar con Pandora que el seguro cubra hormigón.
- Danny Ruiz (Bello Construction, obra Vázquez): Martin habla por WhatsApp; Danny está renovando su web para
  conseguir más obra. Idea: ofrecerle fotos de Vázquez y un testimonio para su web (relación y próximas obras).
- Kozo y Danny Ruiz fueron ~74 % del ingreso de los últimos 12 meses (detalle privado en el Drive de Martin).

### Orden de la plata (desde el 1-oct, decisión de Martin)
- Martin avisa en el chat cada compra y cada factura que manda. Claude la anota en la planilla privada
  "Libro de caja MOP (desde 1-oct-2026)" dentro de la carpeta de Drive "MOP Comprobantes (facturas y compras)"
  (id 1YgsP8sQs7YsCdO34MWII598B_E3QX_jh) y guarda ahí la foto o el PDF. Como el conector de Drive no edita
  planillas, se recrea con las filas nuevas y la vieja va a la papelera. Resumen semanal para el coach.

### Base de contactos (desde el 1-oct, pedido de Martin)
- Planilla privada en el Drive de Martin: "Contactos MOP - base de trabajo (PRIVADO)"
  (id 1cGzqsmyyf23cA2QjQvVJA87kQkkZ8bXaaTCiswB1jWk). ~50 contactos sacados de Gmail: clientes/constructoras,
  proveedores, subcontratistas, servicios y arquitectos, con qué hacen, última charla y obras.
- Cuando Martin pida algo ("¿a quién le pido acero?"), mirar primero esa planilla. Los datos de contacto
  NO se copian a este repositorio (es público). Faltan los contactos del celular (exportar .vcf a Drive).

### WhatsApp Business (1-oct, decisión de Martin)
- Cuenta creada en el 754-457-3599. Nombre "Mop Construction..." (Meta avisa por MOP en mayúsculas; se puede
  pedir después). Horario L-V 7-18, sáb 8-13. Sin dirección. Catálogo: más adelante.
- Decisión de Martin: hasta arreglar el seguro (hoy clasificado framing interior), el perfil dice SOLO framing,
  sin enlace a la web ni a Instagram. Pendiente: pedir a Pandora agregar concreto/drywall antes del 15-oct, y
  decidir si la web e Instagram también se muestran solo con framing mientras tanto.

### Plan 2-oct (pedido de Martin)
- Viernes 2-oct: correo a Daniel Burunat (Vercetti) con el número de North Beach: gracias, aceptamos el desafío,
  este es el precio con todo, y con transparencia lo que hoy falta (fianza, umbrella). Borrador en el chat; sale
  SOLO con el aprobado de Martin. Martin tiene que decidir antes: ganancia 9 % ($1.168.470) o 13,4 % ($1.226.891).
- Flagler se entrega el viernes 9-oct (NO el 2): visita lunes 5-oct 12:00.

### Proyecto "Segundo Cerebro MOP" en claude.ai (creado 1-oct)
- Instrucciones cargadas. Conocimiento: 3 archivos .txt en el Drive de Martin (la app del celular no acepta Google
  Docs): "Segundo cerebro MOP - para el proyecto de Claude.txt" (memoria + 12 coaches), "... - 2 Obras clientes y
  presupuestos.txt" y "... - 3 Finanzas papeles y vida (PRIVADO).txt". Son fotos del 1-oct: cuando cambie algo
  grande, generar versiones nuevas y avisarle a Martin que las reemplace en el proyecto.

### Coach astrológico (13.º, 1-oct)
- Carta natal calculada con pyswisseph (script en el scratchpad de la sesión; se rehace con los datos del archivo
  privado). Los datos de nacimiento y la lectura están SOLO en el Drive de Martin:
  "Segundo cerebro MOP - 4 Carta natal de Martin (PRIVADO).txt". No copiarlos a este repositorio público.
- Fechas útiles: Mercurio retrógrado 24-oct al 14-nov-2026 y 10-feb al 4-mar-2027 (revisar todo dos veces).

### WhatsApp conectado para leer mensajes (opción 3, Martin dijo SÍ el 1-oct)
- Camino: "coexistencia" de Meta (WhatsApp Business app + Cloud API en el mismo número; la app sigue igual).
  Requisitos: app Business 2.24.17 o más nueva, número usado en la app 7+ días, portafolio de Meta Business, y
  alta por un socio de Meta (Tech Provider / BSP): no se puede hacer solo. Los mensajes entrantes van a Supabase
  (función) y Claude los lee; NUNCA manda mensajes por Martin.
- Paso 1 (pendiente de Martin): confirmar versión de la app y que el 754-457-3599 está en WhatsApp Business.
- Después: elegir socio (el más barato con coexistencia y webhook) o hacer de MOP Publicador su propio Tech Provider.

### Otros pendientes (1-oct)
- Adventure Ave (esperando desde 28-sep); Vázquez (Danny Ruiz): comparar el juego de PA Architect con el de la
  diseñadora cuando Martin lo vuelva a subir; North Beach y A100 no tienen el "¿por qué?" en sus líneas.
- Esperan el OK de Martin: cambio de roles y permisos en la app; volver a publicar presupuestos viejos.
- 1-oct: se le pasó a Martin un prompt para que un amigo arme una app parecida desde cero (sin datos de MOP);
  guardado en `mop-estimador/docs/prompt-app-desde-cero.md`.
- Los PDF de los planos (Lincoln, Flagler, Kilwins, Rojas) NO están en ningún repositorio (regla): el chat nuevo los
  vuelve a bajar del correo de Nicole (enlaces de SharePoint, truco de la cookie en el CLAUDE.md del estimador) o del
  Drive. Lincoln y Flagler ya están subidos a la app (Storage `planos`).
- 2-oct: chat "MOP Construction OS platform" archivado a pedido de Martin; se archivaron también 15 chats viejos
  ya terminados. Uno ("Hugging Face (2)") esperaba una foto JPG en el Drive para hacer un video.

