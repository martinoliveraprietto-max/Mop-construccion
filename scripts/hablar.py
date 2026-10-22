#!/usr/bin/env python3
"""Arma el audio para Martin con voz uruguaya de hombre (edge-tts, es-UY-MateoNeural).

Uso:
  python3 scripts/hablar.py "texto" ruta/respuesta.mp3

En la nube, edge-tts falla con "certificate verify failed" porque no conoce el certificado
del proxy (pasó el 16, el 20 y el 21-oct): acá se le pasa ese certificado directamente.
Si edge-tts igual falla (por ejemplo, 403 cuando Microsoft cambia la firma), se usa la voz
de Google (gTTS, acento de Argentina) para que Martin nunca se quede sin audio.
"""
import asyncio
import os
import ssl
import subprocess
import sys

VOZ = "es-UY-MateoNeural"
CA_NUBE = "/root/.ccr/ca-bundle.crt"


def con_edge(texto, salida):
    import edge_tts
    import edge_tts.communicate as comunicacion
    if os.path.exists(CA_NUBE):
        comunicacion._SSL_CTX = ssl.create_default_context(cafile=CA_NUBE)
    asyncio.run(edge_tts.Communicate(texto, VOZ).save(salida))


def con_google(texto, salida):
    try:
        from gtts import gTTS
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", "--disable-pip-version-check",
                        "--root-user-action=ignore", "gTTS"], check=True)
        from gtts import gTTS
    if os.path.exists(CA_NUBE):
        os.environ.setdefault("REQUESTS_CA_BUNDLE", CA_NUBE)
    gTTS(texto, lang="es", tld="com.ar").save(salida)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    texto, salida = sys.argv[1], sys.argv[2]
    for nombre, hacer in (("edge-tts", con_edge), ("Google", con_google)):
        try:
            hacer(texto, salida)
            if os.path.getsize(salida) > 1000:
                print(f"Audio listo ({nombre}): {salida}")
                return
            print(f"{nombre} dejó el audio vacío.", file=sys.stderr)
        except Exception as error:
            print(f"{nombre} falló: {error}", file=sys.stderr)
    sys.exit("No se pudo armar el audio.")


if __name__ == "__main__":
    main()
