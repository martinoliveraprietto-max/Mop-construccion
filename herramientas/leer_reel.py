"""Lee un reel ajeno desde una grabación de pantalla: python3 -m herramientas.leer_reel VIDEO [--salida DIR]

Por qué existe (3-nov-2026): desde el 1-nov Instagram pide iniciar sesión para ver reels; yt-dlp y la
página embed vuelven vacías, y el permiso de MOP Publicador (inicio de sesión de Instagram) no trae
business_discovery ni oEmbed (probado 3-nov). Camino que sí funciona: Martin graba la pantalla del celular
con sonido mientras pasa el reel y lo manda al chat o a Drive ("Mop instagram"). Esta herramienta saca:
  1. lo que se dice (faster-whisper, idioma automático), y
  2. una grilla con un cuadro cada N segundos (lo que se ve: textos en pantalla, tomas).
Solo para leer y sacar ideas: nunca se republica contenido ajeno. Nada se guarda en el repositorio.

Opciones: --cada 3 (segundos entre cuadros) · --modelo small · --idioma (vacío = automático)
Necesita: python3 -m pip install -q faster-whisper imageio-ffmpeg numpy pillow
"""
import argparse
import glob
import os
import subprocess
import sys
import tempfile


def cuadros(video, carpeta, cada=3):
    import imageio_ffmpeg
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run([ff, "-loglevel", "error", "-i", video, "-vf", f"fps=1/{cada},scale=360:-2",
                    os.path.join(carpeta, "c%03d.jpg")], check=True)
    return sorted(glob.glob(os.path.join(carpeta, "c*.jpg")))


def grilla(imagenes, salida, columnas=4):
    from PIL import Image, ImageDraw
    if not imagenes:
        return None
    ims = [Image.open(p).convert("RGB") for p in imagenes]
    w, h = ims[0].size
    filas = (len(ims) + columnas - 1) // columnas
    hoja = Image.new("RGB", (columnas * w, filas * h), (13, 12, 10))
    for i, im in enumerate(ims):
        x, y = (i % columnas) * w, (i // columnas) * h
        hoja.paste(im.resize((w, h)), (x, y))
        ImageDraw.Draw(hoja).text((x + 6, y + 6), str(i + 1), fill=(230, 201, 126))
    hoja.save(salida, quality=85)
    return salida


def hablado(video, modelo="small", idioma=None):
    from faster_whisper import WhisperModel
    from herramientas.transcribir import audio_16k
    m = WhisperModel(modelo, device="cpu", compute_type="int8")
    partes, info = m.transcribe(audio_16k(video), language=idioma or None)
    texto = " ".join(p.text.strip() for p in partes)
    return texto, info.language


def main(argv=None):
    p = argparse.ArgumentParser(prog="herramientas.leer_reel", description=__doc__.split("\n")[0])
    p.add_argument("video")
    p.add_argument("--salida", default=None, help="carpeta para la grilla (por defecto, una temporal)")
    p.add_argument("--cada", type=float, default=3)
    p.add_argument("--modelo", default="small")
    p.add_argument("--idioma", default="")
    p.add_argument("--sin-audio", action="store_true")
    a = p.parse_args(argv)
    carpeta = a.salida or tempfile.mkdtemp(prefix="reel_")
    os.makedirs(carpeta, exist_ok=True)
    hoja = grilla(cuadros(a.video, carpeta, a.cada), os.path.join(carpeta, "grilla.jpg"))
    print(f"GRILLA: {hoja} (un cuadro cada {a.cada:g} s, numerados)")
    if not a.sin_audio:
        try:
            texto, lengua = hablado(a.video, a.modelo, a.idioma)
            print(f"IDIOMA: {lengua}")
            print("DICE: " + (texto or "(sin voz)"))
        except subprocess.CalledProcessError:
            print("DICE: (el video no tiene sonido: pedirle a Martin que grabe con sonido)")
        except Exception as e:  # sin faster-whisper u otro error: la grilla igual sirve
            print(f"DICE: no se pudo pasar a texto ({e.__class__.__name__}: {e})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
