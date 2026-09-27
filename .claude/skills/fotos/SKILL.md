---
name: fotos
description: Carga fotos de obra nuevas a la web de MOP de punta a punta. Revisa cada foto (casco y arnés, carteles de otras empresas, patentes, caras, direcciones), la achica, le borra el GPS, la numera, la agrega a la galería con su categoría y sus textos en inglés y español, y corre las pruebas. Usar cuando Martin manda fotos por el chat o avisa que subió fotos a la carpeta de Drive.
argument-hint: "[de dónde vienen: chat | drive]"
---

# /fotos — cargar fotos de obra a la web

Origen de las fotos: $ARGUMENTS (si viene vacío: las que Martin adjuntó en el chat; si no hay,
la carpeta de Drive "Mop instagram", id 19ul5QKrqcSqsnZGLbO2OI8BrTeRzGIIO).

Todo en español con Martin. Seguir los pasos EN ORDEN. Este repositorio es PÚBLICO: nada se
sube sin que Martin vea antes la lista de fotos aceptadas y rechazadas.

## 1. Mirar cada foto (con la herramienta de leer imágenes, una por una)
Clasificar cada una en ACEPTADA, RECORTAR o RECHAZADA, con el motivo en una línea:

- **Seguridad (lo que más miran las constructoras):** persona en obra SIN CASCO, o trabajando
  en altura (techo, andamio, escalera alta, cerchas) SIN ARNÉS → RECHAZADA, salvo que la persona
  se pueda recortar y lo que queda siga mostrando el trabajo (→ RECORTAR). Nunca agregar cascos
  con inteligencia artificial ni retocar a la persona; tampoco borronearla (se sigue viendo).
- **Otras empresas:** cartel, logo, camioneta rotulada o número de licencia de otra constructora
  → RECORTAR (si el cartel queda en un borde) o RECHAZADA. En la web nada puede sugerir que la
  obra o la licencia son de MOP si no lo son.
- **Datos privados:** patentes de autos, caras de clientes, números de casa o de calle,
  papeles con nombres → RECORTAR o RECHAZADA.
- **Nada de Hialeah** a la vista (carteles de la ciudad, direcciones).
- **Repetidas:** comparar con las que ya hay en `img/` (misma obra, mismo ángulo) → RECHAZADA.
- **Calidad:** movida, oscura o sin trabajo visible → RECHAZADA.
- Elegir la **categoría** de la galería: `new` (casas nuevas), `framing` (estructura),
  `outdoor` (exteriores), `decks` (decks y muelles), `interior` (interiores y comercial),
  `concrete` (estructuras de concreto: pozo, cabilla, encofrado, colado), `foundations`
  (fundaciones).

Mostrarle a Martin la tabla (foto, veredicto, motivo, categoría) y ESPERAR su aprobación.

## 2. Preparar las aprobadas (Python con Pillow)
- `ImageOps.exif_transpose`, recortar si corresponde, convertir a RGB.
- Achicar a 1100 px del lado más largo (el tamaño de las que ya están), JPEG calidad 80,
  progresivo, **sin EXIF** (sin GPS ni modelo de teléfono). Menos de 600 KB.
- Nombre: el número siguiente al más alto de `img/` (`ls img | sort -n | tail -1`), dos cifras
  o más: `96.jpg`, `97.jpg`…

## 3. Agregarlas a la galería de `index.html`
Dentro de `<div class="galeria" id="galeria">`, una línea por foto con el MISMO formato que las
existentes (copiar una y cambiar):
`<figure class="obra" data-cat="CATEGORIA"><button type="button" class="abrir" data-src="img/N.jpg" aria-label="Open photo"><img src="img/N.jpg" width="ANCHO" height="ALTO" loading="lazy" alt="TEXTO EN INGLÉS"></button><figcaption data-es="TEXTO EN ESPAÑOL">TEXTO EN INGLÉS</figcaption></figure>`
- `width`/`height`: los reales de la foto ya achicada.
- Textos cortos y verdaderos, de lo que se ve ("Tie beam formwork and rebar"). Español neutro
  con "tú" si hace falta. Sin "licensed", "general contractor", "crew", empleados ni techado
  (la guardia `guardia_publica.py` lo frena igual).
- Las fotos más fuertes van primero en su categoría.

## 4. Probar
- `python3 pruebas/prueba_sitio.py` y `node pruebas/prueba_navegador.js`: las dos en verde.
- Captura de la galería en celular (390 px) con Playwright y mandársela a Martin.

## 5. Publicar
Solo con el visto bueno de Martin: seguir la habilidad `/publicar`.
