/* Prueba de punta a punta en un navegador real (Chromium).
   Uso: node pruebas/prueba_navegador.js
   Necesita playwright-core (npm i playwright-core) y Chromium.
   Levanta el sitio con un servidor local, igual que GitHub Pages, y lo recorre
   como lo haría un cliente en celular y en computadora. */
const { chromium } = require("playwright-core");
const http = require("http");
const fs = require("fs");
const path = require("path");

const SITIO = path.join(__dirname, "..");
const CHROME = process.env.CHROME || "/opt/pw-browsers/chromium-1194/chrome-linux/chrome";
const CAPTURAS = process.env.CAPTURAS || "";
const TIPOS = { ".html": "text/html; charset=utf-8", ".css": "text/css", ".js": "text/javascript",
  ".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
  ".webp": "image/webp", ".txt": "text/plain", ".woff2": "font/woff2" };

let fallas = 0;
function chequear(cond, msg) {
  console.log((cond ? "  ok    " : "  FALLA ") + msg);
  if (!cond) fallas++;
}

function servidor() {
  return new Promise((resolve) => {
    const s = http.createServer((req, res) => {
      let ruta = decodeURIComponent(req.url.split("?")[0]);
      if (ruta.endsWith("/")) ruta += "index.html";
      const archivo = path.join(SITIO, ruta);
      if (!archivo.startsWith(SITIO) || !fs.existsSync(archivo)) { res.writeHead(404); return res.end("404"); }
      res.writeHead(200, { "Content-Type": TIPOS[path.extname(archivo)] || "application/octet-stream" });
      fs.createReadStream(archivo).pipe(res);
    });
    s.listen(0, "127.0.0.1", () => resolve(s));
  });
}

async function recorrer(browser, base, nombre, opciones) {
  console.log(`\n== ${nombre} ==`);
  const ctx = await browser.newContext(opciones);
  // Las fuentes de Google no siempre cargan en la prueba: no cuentan como error de la página.
  await ctx.route(/fonts\.(googleapis|gstatic)\.com/, (r) => r.fulfill({ status: 200, body: "" }));
  const page = await ctx.newPage();
  const errores = [];
  page.on("pageerror", (e) => errores.push(e.message));
  page.on("console", (m) => { if (m.type() === "error") errores.push(m.text()); });
  await page.addInitScript(() => { window.__abiertas = []; window.open = (u) => { window.__abiertas.push(u); return null; }; });
  await page.goto(base + "/index.html", { waitUntil: "load" });
  await page.waitForTimeout(300);

  const ancho = await page.evaluate(() => [document.documentElement.scrollWidth, window.innerWidth]);
  chequear(ancho[0] <= ancho[1], `sin desborde horizontal (${ancho[0]} <= ${ancho[1]})`);
  const rotas = await page.evaluate(async () => {
    const imgs = [...document.images].filter((i) => i.getAttribute("src"));
    imgs.forEach((i) => { i.loading = "eager"; });
    await Promise.all(imgs.map((i) => i.complete ? 0 : new Promise((r) => { i.onload = i.onerror = r; })));
    return imgs.filter((i) => !i.naturalWidth).map((i) => i.getAttribute("src"));
  });
  chequear(rotas.length === 0, "todas las imágenes cargan" + (rotas.length ? ` (rotas: ${rotas})` : ""));

  // menú
  const movil = opciones.viewport.width <= 1180;
  if (movil) {
    chequear(!(await page.isVisible(".menu a")), "en celular el menú arranca cerrado");
    await page.click("#menu-btn");
    chequear(await page.isVisible(".menu a[href='#constructoras']"), "el botón abre el menú");
    await page.click(".menu a[href='#obras']");
    chequear(!(await page.isVisible(".menu a")), "al tocar una opción el menú se cierra");
  } else {
    chequear(await page.isVisible(".menu a[href='#constructoras']"), "menú visible en computadora");
  }

  // idioma
  await page.click("#idioma");
  chequear((await page.textContent("h1")).includes("Tu visión"), "cambia a español");
  chequear(await page.evaluate(() => document.documentElement.lang) === "es", "lang=es");
  await page.reload({ waitUntil: "load" });
  chequear((await page.textContent("h1")).includes("Tu visión"), "recuerda el español al volver");
  await page.click("#idioma");
  chequear((await page.textContent("h1")).includes("Your Vision"), "vuelve a inglés");

  // filtros de la galería
  const total = await page.$$eval(".obra", (o) => o.length);
  await page.click(".chip[data-f='framing']");
  const vis = await page.$$eval(".obra", (o) => o.filter((x) => !x.hidden).map((x) => x.dataset.cat));
  chequear(vis.length > 0 && vis.every((c) => c === "framing"), `filtro Estructura muestra solo estructura (${vis.length})`);
  chequear((await page.textContent("#cuenta")).startsWith(String(vis.length)), "el contador coincide con el filtro");
  await page.click(".chip[data-f='all']");
  chequear(await page.$$eval(".obra", (o) => o.filter((x) => !x.hidden).length) === total, `Todo vuelve a mostrar las ${total} fotos`);

  // visor
  await page.click(".obra .abrir");
  chequear(await page.evaluate(() => document.getElementById("visor").open), "tocar una foto la abre grande");
  const src1 = await page.getAttribute("#visor-img", "src");
  await page.click("#v-sig");
  chequear((await page.getAttribute("#visor-img", "src")) !== src1, "la flecha pasa a la siguiente foto");
  await page.click("#v-cerrar");
  chequear(!(await page.evaluate(() => document.getElementById("visor").open)), "el visor se cierra");

  // formulario → WhatsApp
  await page.click("#form button[type=submit]");
  chequear(await page.isVisible("#aviso"), "formulario vacío: avisa");
  chequear((await page.evaluate(() => window.__abiertas.length)) === 0, "formulario vacío: no abre WhatsApp");
  await page.fill("#f-nombre", "Ana Pérez");
  await page.fill("#f-tel", "754 457");
  await page.click("#form button[type=submit]");
  chequear((await page.evaluate(() => window.__abiertas.length)) === 0, "teléfono corto: no abre WhatsApp");
  await page.fill("#f-tel", "(754) 457-3599");
  await page.selectOption("#f-tipo", { index: 1 });
  await page.fill("#f-msj", "Drywall en 2 cuartos");
  await page.click("#form button[type=submit]");
  const url = await page.evaluate(() => window.__abiertas[0] || "");
  chequear(url.startsWith("https://wa.me/17544573599?text="), "abre WhatsApp al 754-457-3599");
  const msj = decodeURIComponent(url.split("text=")[1] || "");
  chequear(msj.includes("Ana Pérez") && msj.includes("(754) 457-3599") && msj.includes("Drywall en 2 cuartos") && msj.includes("Drywall"),
    "el mensaje lleva nombre, teléfono, trabajo y detalle");
  chequear(msj.startsWith("Hi MOP"), "en inglés el mensaje sale en inglés");
  await page.click("#idioma");
  await page.click("#form button[type=submit]");
  const msjEs = decodeURIComponent((await page.evaluate(() => window.__abiertas[1] || "")).split("text=")[1] || "");
  chequear(msjEs.startsWith("Hola MOP"), "en español el mensaje sale en español");
  await page.click("#idioma");

  if (CAPTURAS) await page.screenshot({ path: path.join(CAPTURAS, `web-${opciones.viewport.width}.png`), fullPage: true });
  chequear(errores.length === 0, "sin errores en la consola" + (errores.length ? `: ${errores.join(" | ")}` : ""));
  await ctx.close();
}

(async () => {
  const s = await servidor();
  const base = `http://127.0.0.1:${s.address().port}`;
  const browser = await chromium.launch({ executablePath: CHROME });
  await recorrer(browser, base, "Celular 390 px", { viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  await recorrer(browser, base, "Celular chico 320 px", { viewport: { width: 320, height: 640 }, isMobile: true, hasTouch: true });
  await recorrer(browser, base, "Computadora 1366 px", { viewport: { width: 1366, height: 800 } });
  await browser.close();
  s.close();
  console.log(fallas ? `\n${fallas} falla(s).` : "\nTodo bien.");
  process.exit(fallas ? 1 : 0);
})();
