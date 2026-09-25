#!/usr/bin/env python3
"""Prueba del sitio de MOP (raíz del repositorio) sin dependencias raras: corre en Termux.

Controla datos exactos, palabras prohibidas, datos para Google, traducciones,
que existan todas las imágenes que usa la página y que ninguna foto lleve datos
internos (ubicación GPS, modelo del teléfono).
Uso: python3 pruebas/prueba_sitio.py
"""
import json
import os
import re
import sys

SITIO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
fallas = []


def chequear(condicion, mensaje):
    print(("  ok    " if condicion else "  FALLA ") + mensaje)
    if not condicion:
        fallas.append(mensaje)


html = open(os.path.join(SITIO, "index.html"), encoding="utf-8").read()
texto = re.sub(r"<[^>]+>", " ", html)

print("== Datos exactos ==")
for dato in ["MOP Construction and Service, Inc.", "Your Vision.", "Built Solid.", "754.457.3599",
             "+17544573599", "mopconstruccion@gmail.com", "Dania Beach, FL", "Miami-Dade", "Broward",
             "instagram.com/mopconstruccion.inc", "wa.me/17544573599"]:
    chequear(dato.lower() in html.lower(), f"aparece «{dato}»")

print("== Palabras que no pueden aparecer ==")
for prohibida in ["general contractor", "licensed", "license", "licencia", "hialeah", "crew",
                  "cuadrilla", "empleados", "employees", "roofing", "techado"]:
    chequear(prohibida not in html.lower(), f"no aparece «{prohibida}»")

print("== Datos para Google ==")
m = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
chequear(m is not None, "hay datos estructurados")
if m:
    try:
        d = json.loads(m.group(1))
        chequear(d.get("telephone") == "+1-754-457-3599", "teléfono en los datos estructurados")
        chequear(d.get("address", {}).get("addressLocality") == "Dania Beach", "ciudad Dania Beach")
        chequear("streetAddress" not in d.get("address", {}), "sin dirección de calle")
    except ValueError as e:
        chequear(False, f"los datos estructurados son JSON válido ({e})")

print("== Traducciones ==")
vacias = re.findall(r'data-es=""', html)
chequear(not vacias, "ninguna traducción vacía")
chequear(html.count("data-es=") > 100, f"textos traducidos: {html.count('data-es=')}")
voseo = [v for v in ["Tocá", "Contanos", "querés", "Empezá", "escribinos", "llamanos"] if v in html]
chequear(not voseo, "español neutro con «tú» (sin voseo)")

print("== Imágenes ==")
rutas = sorted(set(re.findall(r'(?:src|data-src|href)="((?:img/)[^"]+)"', html)))
faltan = [r for r in rutas if not os.path.exists(os.path.join(SITIO, r))]
chequear(not faltan, f"existen las {len(rutas)} imágenes que usa la página" + (f" (faltan: {faltan})" if faltan else ""))
chequear(os.path.exists(os.path.join(SITIO, "favicon.png")), "existe favicon.png")
fotos = [f for f in os.listdir(os.path.join(SITIO, "img")) if f.lower().endswith((".jpg", ".jpeg"))]
usadas = {os.path.basename(r) for r in rutas}
sobran = [f for f in fotos if f not in usadas and f != "04.jpg"]
chequear(not sobran, "todas las fotos de img/ se usan" + (f" (sin usar: {sobran})" if sobran else ""))


def exif_con_datos(ruta):
    """Busca en el JPEG un bloque EXIF con GPS (0x8825) o modelo (0x0110), sin librerías."""
    b = open(ruta, "rb").read()
    i = b.find(b"Exif\x00\x00")
    if i < 0:
        return False
    tiff = b[i + 6:]
    le = tiff[:2] == b"II"
    num = lambda x: int.from_bytes(x, "little" if le else "big")
    ifd = num(tiff[4:8])
    n = num(tiff[ifd:ifd + 2])
    etiquetas = {num(tiff[ifd + 2 + k * 12: ifd + 4 + k * 12]) for k in range(n)}
    return bool(etiquetas & {0x8825, 0x0110, 0x010F})


for f in sorted(fotos):
    ruta = os.path.join(SITIO, "img", f)
    kb = os.path.getsize(ruta) // 1024
    if exif_con_datos(ruta) or kb > 600:
        chequear(False, f"img/{f}: sin datos internos y liviana ({kb} KB)")
chequear(True, f"{len(fotos)} fotos revisadas (datos internos y peso)")

print()
if fallas:
    print(f"{len(fallas)} falla(s).")
    sys.exit(1)
print("Todo bien.")
