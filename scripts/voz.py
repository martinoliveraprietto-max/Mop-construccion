# Voz uruguaya (es-UY-MateoNeural) por un Space de Hugging Face que corre edge-tts (la nube no deja WebSocket).
import json, sys, urllib.request
B = "https://innoai-edge-tts-text-to-speech.hf.space/gradio_api"
texto, salida = sys.argv[1], sys.argv[2]
req = urllib.request.Request(B + "/call/tts_interface", json.dumps(
    {"data": [texto, "es-UY-MateoNeural - es-UY (Male)", 0, 0]}).encode(), {"Content-Type": "application/json"})
ev = json.load(urllib.request.urlopen(req, timeout=60))["event_id"]
datos = None
for linea in urllib.request.urlopen(B + "/call/tts_interface/" + ev, timeout=180).read().decode().splitlines():
    if linea.startswith("data:") and linea[5:].strip().startswith("["):
        datos = json.loads(linea[5:])
url = datos[0]["url"]
open(salida, "wb").write(urllib.request.urlopen(url, timeout=120).read())
print("ok", salida)
