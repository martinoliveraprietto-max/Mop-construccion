#!/usr/bin/env python3
"""Publica en Instagram (@mopconstruccion.inc) la siguiente publicación pendiente de
instagram/cola.json, con la API de Instagram con inicio de sesión de Instagram.

Uso:
  python3 scripts/publicar.py --verificar   # comprueba el token y la cuenta, no publica
  python3 scripts/publicar.py --simular     # muestra qué publicaría, no publica
  python3 scripts/publicar.py               # publica la siguiente pendiente

El token se lee SOLO de la variable de entorno INSTAGRAM_TOKEN y nunca se imprime.
Las imágenes se toman de la copia pública del repositorio en GitHub, así que tienen que
estar subidas (git push) ANTES de publicar.
"""
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://graph.instagram.com/v25.0"
BASE_IMG = "https://raw.githubusercontent.com/martinoliveraprietto-max/mop-construccion/main/"
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLA = os.path.join(RAIZ, "instagram", "cola.json")
TOKEN = os.environ.get("INSTAGRAM_TOKEN", "").strip()


def limpio(texto):
    """Saca el token de cualquier texto antes de mostrarlo."""
    return texto.replace(TOKEN, "***") if TOKEN else texto


def llamar(metodo, ruta, **params):
    params["access_token"] = TOKEN
    datos = urllib.parse.urlencode(params).encode()
    if metodo == "GET":
        req = urllib.request.Request(f"{API}/{ruta}?{datos.decode()}")
    else:
        req = urllib.request.Request(f"{API}/{ruta}", data=datos, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        cuerpo = limpio(e.read().decode(errors="replace"))
        sys.exit(f"ERROR {e.code} en {metodo} {ruta}: {cuerpo}")


def esperar(contenedor, tope_seg=180):
    t0 = time.time()
    while True:
        estado = llamar("GET", contenedor, fields="status_code").get("status_code")
        if estado == "FINISHED":
            return
        if estado in ("ERROR", "EXPIRED"):
            sys.exit(f"ERROR: el contenedor {contenedor} quedó en {estado}")
        if time.time() - t0 > tope_seg:
            sys.exit(f"ERROR: el contenedor {contenedor} sigue en {estado} después de {tope_seg} s")
        time.sleep(5)


def main():
    if not TOKEN:
        sys.exit("Falta INSTAGRAM_TOKEN en el entorno (Configuración del entorno > Variables de entorno).")
    yo = llamar("GET", "me", fields="user_id,username,account_type,media_count")
    ig_id = yo["user_id"]
    print(f"Cuenta: @{yo.get('username')} ({yo.get('account_type')}), {yo.get('media_count')} publicaciones")

    if "--verificar" in sys.argv:
        limite = llamar("GET", f"{ig_id}/content_publishing_limit", fields="quota_usage,config")
        print("Límite de publicación:", json.dumps(limite.get("data", limite)))
        return

    cola = json.load(open(COLA, encoding="utf-8"))
    pendiente = next((p for p in cola if p["estado"] == "pendiente"), None)
    if not pendiente:
        print("No queda nada pendiente en la cola.")
        return
    urls = [BASE_IMG + ruta for ruta in pendiente["imagenes"]]
    print(f"Siguiente: publicación {pendiente['id']} ({len(urls)} imagen/es)")
    if "--simular" in sys.argv:
        for u in urls:
            print("  ", u)
        print(pendiente["texto"])
        return

    if len(urls) == 1:
        contenedor = llamar("POST", f"{ig_id}/media", image_url=urls[0], caption=pendiente["texto"])["id"]
    else:
        hijos = []
        for u in urls:
            hijo = llamar("POST", f"{ig_id}/media", image_url=u, is_carousel_item="true")["id"]
            esperar(hijo)
            hijos.append(hijo)
        contenedor = llamar("POST", f"{ig_id}/media", media_type="CAROUSEL",
                            children=",".join(hijos), caption=pendiente["texto"])["id"]
    esperar(contenedor)
    media = llamar("POST", f"{ig_id}/media_publish", creation_id=contenedor)["id"]
    enlace = llamar("GET", media, fields="permalink").get("permalink")

    pendiente.update(estado="publicado", media_id=media,
                     publicado=time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()), enlace=enlace)
    with open(COLA, "w", encoding="utf-8") as f:
        json.dump(cola, f, ensure_ascii=False, indent=2)
    print(f"PUBLICADO: {enlace}")


if __name__ == "__main__":
    main()
