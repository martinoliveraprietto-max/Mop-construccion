"""Pasa a texto un audio o video (llamadas de Martin, reels): python3 -m herramientas.transcribir ARCHIVO

Cerebro MOP (1-nov-2026). Gratis y local: FFmpeg (imageio-ffmpeg) saca el audio en mono 16 kHz
y faster-whisper lo pasa a texto en español. Al audio se le pasa como arreglo de numpy porque
con la ruta del archivo falla la versión de av que trae el entorno. El texto sale por pantalla:
no se guarda en este repositorio público; se resume en hechos con `herramientas.memoria anotar`.

Opciones: --modelo small (tiny, base, small, medium) · --idioma es
Necesita: python3 -m pip install -q faster-whisper imageio-ffmpeg numpy
"""
import argparse
import subprocess
import sys


def audio_16k(ruta):
    import imageio_ffmpeg
    import numpy as np
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    salida = subprocess.run([ff, "-loglevel", "error", "-i", ruta, "-ac", "1", "-ar", "16000",
                             "-f", "s16le", "-"], check=True, capture_output=True).stdout
    return np.frombuffer(salida, np.int16).astype(np.float32) / 32768


def transcribir(ruta, modelo="small", idioma="es"):
    from faster_whisper import WhisperModel
    m = WhisperModel(modelo, device="cpu", compute_type="int8")
    partes, _ = m.transcribe(audio_16k(ruta), language=idioma)
    return " ".join(p.text.strip() for p in partes)


def main(argv=None):
    p = argparse.ArgumentParser(prog="herramientas.transcribir", description=__doc__.split("\n")[0])
    p.add_argument("archivo")
    p.add_argument("--modelo", default="small")
    p.add_argument("--idioma", default="es")
    a = p.parse_args(argv)
    print(transcribir(a.archivo, a.modelo, a.idioma))
    return 0


if __name__ == "__main__":
    sys.exit(main())
