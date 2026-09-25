#!/usr/bin/env python3
"""Arma un Reel vertical (1080x1920, 30 fps, sin audio: la música de moda se agrega desde la app)
con fotos de obra: fondo desenfocado, foto entera al centro, zoom lento, texto arriba y placa final
con el logo. Uso: python3 scripts/hacer_reel.py  (arma los reels definidos en REELS)
Necesita: pip install imageio-ffmpeg pillow  y las fuentes en scripts/fuentes/."""
import os, subprocess, tempfile
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import imageio_ffmpeg

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FF = imageio_ffmpeg.get_ffmpeg_exe()
W, H, FPS = 1080, 1920, 30
ORO = (201, 165, 90); CREMA = (243, 234, 214); NEGRO = (13, 12, 10)
F = os.path.join(RAIZ, 'scripts', 'fuentes')
def texto_centrado(d, y, t, f, color, sombra=True):
    ancho = d.textlength(t, font=f)
    x = (W - ancho) / 2
    if sombra:
        for dx, dy in ((3, 3), (2, 2)):
            d.text((x + dx, y + dy), t, font=f, fill=(0, 0, 0))
    d.text((x, y), t, font=f, fill=color)

def cuadro(foto, arriba, abajo):
    im = Image.open(os.path.join(RAIZ, 'img', foto)).convert('RGB')
    fondo = im.copy(); r = max(W / fondo.width, H / fondo.height)
    fondo = fondo.resize((int(fondo.width * r) + 1, int(fondo.height * r) + 1)).crop((0, 0, W, H)).filter(ImageFilter.GaussianBlur(28))
    fondo = Image.eval(fondo, lambda v: int(v * .45))
    r = W / im.width; fr = im.resize((W, int(im.height * r)))
    if fr.height > 1180: fr = im.resize((int(im.width * 1180 / im.height), 1180))
    y0 = max(390, (H - fr.height) // 2)
    fondo.paste(fr, ((W - fr.width) // 2, y0))
    d = ImageDraw.Draw(fondo)
    fa = ImageFont.truetype(os.path.join(F, 'Montserrat.ttf'), 70); fa.set_variation_by_axes([800])
    fb = ImageFont.truetype(os.path.join(F, 'Montserrat.ttf'), 44); fb.set_variation_by_axes([600])
    y = 170
    for linea in arriba:
        texto_centrado(d, y, linea, fa, CREMA); y += 86
    if abajo:
        texto_centrado(d, H - 250, abajo, fb, ORO)
    return fondo

def placa_final():
    im = Image.new('RGB', (W, H), NEGRO)
    logo = Image.open(os.path.join(RAIZ, 'marca', 'mop-icono-negro-1080.png')).convert('RGB').resize((900, 900))
    im.paste(logo, (90, 360))
    d = ImageDraw.Draw(im)
    fa = ImageFont.truetype(os.path.join(F, 'Montserrat.ttf'), 46); fa.set_variation_by_axes([600])
    fb = ImageFont.truetype(os.path.join(F, 'Montserrat.ttf'), 64); fb.set_variation_by_axes([800])
    fc = ImageFont.truetype(os.path.join(F, 'Montserrat.ttf'), 38); fc.set_variation_by_axes([500])
    texto_centrado(d, 1300, 'CONSTRUCTION AND SERVICE, INC.', fa, CREMA, False)
    texto_centrado(d, 1420, '754-457-3599', fb, ORO, False)
    texto_centrado(d, 1520, 'Free estimates · Miami-Dade & Broward', fc, CREMA, False)
    return im

def reel(nombre, tomas, seg=1.5):
    tmp = tempfile.mkdtemp()
    partes = []
    for i, (foto, arriba, abajo) in enumerate(tomas + [(None, None, None)]):
        img = placa_final() if foto is None else cuadro(foto, arriba, abajo)
        p = os.path.join(tmp, f'{i:02d}.png'); img.save(p)
        dur = 2.2 if foto is None else seg
        n = int(dur * FPS)
        z = "1" if foto is None else f"1+0.0009*on"
        salida = os.path.join(tmp, f'{i:02d}.mp4')
        subprocess.run([FF, '-y', '-loglevel', 'error', '-loop', '1', '-i', p, '-vf',
                        f"scale={W*2}:{H*2},zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS},format=yuv420p",
                        '-t', str(dur), '-r', str(FPS), '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', salida], check=True)
        partes.append(salida)
    lista = os.path.join(tmp, 'lista.txt')
    open(lista, 'w').write(''.join(f"file '{p}'\n" for p in partes))
    destino = os.path.join(RAIZ, 'instagram', 'reels', nombre)
    subprocess.run([FF, '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lista, '-c', 'copy', '-movflags', '+faststart', destino], check=True)
    return destino

REELS = {
 'reel01-de-la-tierra-al-techo.mp4': [
   ('17.jpg', ['FROM DIRT', 'TO ROOF'], 'Layout & forms'),
   ('31.jpg', ['FROM DIRT', 'TO ROOF'], 'Foundation'),
   ('67.jpg', ['FROM DIRT', 'TO ROOF'], 'Block walls'),
   ('68.jpg', ['FROM DIRT', 'TO ROOF'], 'Trusses'),
   ('69.jpg', ['FROM DIRT', 'TO ROOF'], 'Sheathing'),
   ('84.jpg', ['FROM DIRT', 'TO ROOF'], 'Taking shape'),
   ('83.jpg', ['FROM DIRT', 'TO ROOF'], 'Built solid.')],
    # reel02 (concreto) sacado a pedido de Martin el 25-sep: esperar fotos mejores de concreto
 'reel03-local-vacio-a-oficina.mp4': [
   ('18.jpg', ['EMPTY SHELL', 'TO OFFICE'], 'Steel studs'),
   ('20.jpg', ['EMPTY SHELL', 'TO OFFICE'], 'Straight & plumb'),
   ('74.jpg', ['EMPTY SHELL', 'TO OFFICE'], 'Drywall & finish'),
   ('73.jpg', ['EMPTY SHELL', 'TO OFFICE'], 'Ready for business')],
}

if __name__ == '__main__':
    for nombre, tomas in REELS.items():
        print(reel(nombre, tomas))
