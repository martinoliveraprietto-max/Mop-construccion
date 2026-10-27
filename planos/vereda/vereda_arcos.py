"""Plano de vereda con dos arcos elípticos (escalera -> vereda existente).

Medidas en pulgadas. Cambiar los SUPUESTOS cuando Martin confirme y volver a correr:
    python3 planos/vereda/vereda_arcos.py
Genera vereda_arcos.svg (y la tabla de replanteo por pantalla).
"""
import math, pathlib

# --- Medidas dadas por Martin (27-oct) ---
ANCHO_ESCALON = 13 * 12 + 5      # 161" último escalón
LARGO = 8 * 12                   # 96" de la escalera a la vereda existente
ANCHO_VEREDA = 49.5              # vereda existente 4' 1 1/2" terminada (Martin, 27-oct)
# --- SUPUESTOS (confirmar en obra) ---
BORDE_IZQ_VEREDA = 0             # borde izquierdo de la vereda = centro de la escalera
                                 # (mirando desde la escalera hacia la vereda)

xs_izq, xs_der = -ANCHO_ESCALON / 2, ANCHO_ESCALON / 2
xe_izq, xe_der = BORDE_IZQ_VEREDA, BORDE_IZQ_VEREDA + ANCHO_VEREDA


UNION = LARGO / 2                # punto de unión de los dos arcos de cada lado


# Cada lado es una S de dos cuartos de elipse que se unen en (xm, UNION):
#  arco 1 (hacia afuera): centro (xm, 0), sale derecho de la punta del escalón;
#  arco 2 (hacia adentro): centro (xm, LARGO), llega derecho al borde de la vereda.
# En la unión los dos arcos tienen la misma tangente (paralela al escalón).
def xm(xs, xe):
    return (xs + xe) / 2


def punto(xs, xe, u):
    """u de 0 (escalón) a 1 (vereda)."""
    m = xm(xs, xe)
    if u <= 0.5:
        t = math.pi * u
        return m + (xs - m) * math.cos(t), UNION * math.sin(t)
    t = math.pi * (u - 0.5)
    return m + (xe - m) * math.sin(t), LARGO - (LARGO - UNION) * math.cos(t)


def x_en(xs, xe, y):
    m = xm(xs, xe)
    if y <= UNION:
        s_ = y / UNION
        return m + (xs - m) * math.sqrt(max(0.0, 1 - s_ * s_))
    c = (LARGO - y) / (LARGO - UNION)
    return m + (xe - m) * math.sqrt(max(0.0, 1 - c * c))


def pies(p):
    p = round(p * 4) / 4
    signo = "-" if p < 0 else ""
    p = abs(p)
    f, i = divmod(p, 12)
    entero = int(i)
    frac = {0: "", 0.25: " 1/4", 0.5: " 1/2", 0.75: " 3/4"}[i - entero]
    return f"{signo}{int(f)}' {entero}{frac}\""


def tabla():
    filas = []
    for k in range(0, 17):
        y = k * 6
        izq = -x_en(xs_izq, xe_izq, y)      # a la izquierda del centro
        der = x_en(xs_der, xe_der, y)       # a la derecha del centro
        filas.append((y, izq, der, izq + der))
    return filas


def svg():
    S = 4.2                      # px por pulgada
    mx, my = 130, 120            # márgenes
    xmin, xmax = -100, 100
    W = (xmax - xmin) * S + 2 * mx + 330
    H = (LARGO + 70 + 40) * S + 2 * my
    def X(x): return mx + (x - xmin) * S
    def Y(y): return my + (LARGO + 70 - y) * S   # y crece hacia la vereda (arriba)

    o = []
    a = o.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:.0f}" height="{H:.0f}" '
      f'viewBox="0 0 {W:.0f} {H:.0f}" font-family="Montserrat, Arial, sans-serif">')
    a(f'<rect width="100%" height="100%" fill="#ffffff"/>')
    a('<defs><pattern id="hor" width="10" height="10" patternUnits="userSpaceOnUse">'
      '<rect width="10" height="10" fill="#efe7d6"/><circle cx="3" cy="3" r="0.9" fill="#bfae8a"/>'
      '<circle cx="8" cy="7" r="0.7" fill="#bfae8a"/></pattern>'
      '<pattern id="lad" width="14" height="8" patternUnits="userSpaceOnUse">'
      '<rect width="14" height="8" fill="#d9b7a6"/><path d="M0 0H14M0 4H14M7 0V4M0 4V8M14 4V8" '
      'stroke="#a8796a" stroke-width="0.8"/></pattern>'
      '<marker id="fl" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
      '<path d="M0 0L10 5L0 10z" fill="#333"/></marker></defs>')

    # Escalera
    a(f'<rect x="{X(xs_izq)}" y="{Y(0)}" width="{ANCHO_ESCALON*S}" height="{30*S}" fill="#d6d6d6" stroke="#222" stroke-width="2"/>')
    for k in (1, 2):
        a(f'<line x1="{X(xs_izq)}" y1="{Y(-10*k)}" x2="{X(xs_der)}" y2="{Y(-10*k)}" stroke="#777" stroke-width="1"/>')
    a(f'<text x="{X(0)}" y="{Y(-20)}" text-anchor="middle" font-size="18" font-weight="700">ESCALERA</text>')

    # Vereda existente
    a(f'<rect x="{X(xe_izq)}" y="{Y(LARGO+60)}" width="{ANCHO_VEREDA*S}" height="{60*S}" fill="url(#lad)" stroke="#222" stroke-width="2"/>')
    a(f'<text x="{X((xe_izq+xe_der)/2)}" y="{Y(LARGO+30)}" text-anchor="middle" font-size="14" font-weight="700">VEREDA</text>')
    a(f'<text x="{X((xe_izq+xe_der)/2)}" y="{Y(LARGO+30)+17}" text-anchor="middle" font-size="14" font-weight="700">EXISTENTE</text>')

    # Vereda nueva (relleno)
    n = 60
    pts = [punto(xs_izq, xe_izq, i / n) for i in range(n + 1)]
    ptd = [punto(xs_der, xe_der, i / n) for i in range(n + 1)]
    contorno = pts + ptd[::-1]
    d = "M" + " L".join(f"{X(x):.1f},{Y(y):.1f}" for x, y in contorno) + "Z"
    a(f'<path d="{d}" fill="url(#hor)" stroke="none"/>')
    for p, col in ((pts, "#b8860b"), (ptd, "#b8860b")):
        d = "M" + " L".join(f"{X(x):.1f},{Y(y):.1f}" for x, y in p)
        a(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="4"/>')
    a(f'<text x="{X(26)}" y="{Y(42)}" text-anchor="middle" font-size="16" font-weight="700" fill="#5a4a20">VEREDA NUEVA</text>')

    # Centro de escalera
    a(f'<line x1="{X(0)}" y1="{Y(-30)}" x2="{X(0)}" y2="{Y(LARGO+66)}" stroke="#c0392b" stroke-width="1.5" stroke-dasharray="12 5 3 5"/>')
    a(f'<text x="{X(0)-6}" y="{Y(LARGO+64)}" text-anchor="end" font-size="12" fill="#c0392b">CENTRO ESCALERA</text>')

    # Centros de las elipses, unión y semiejes
    for xs, xe, lado in ((xs_izq, xe_izq, "A"), (xs_der, xe_der, "B")):
        m = xm(xs, xe)
        izq = xs < 0
        for yc, num in ((0, 1), (LARGO, 2)):
            a(f'<circle cx="{X(m)}" cy="{Y(yc)}" r="5" fill="#1f5fa8"/>')
            a(f'<line x1="{X(m)}" y1="{Y(yc)}" x2="{X(m)}" y2="{Y(UNION)}" stroke="#1f5fa8" stroke-width="1.2" stroke-dasharray="6 4"/>')
            a(f'<text x="{X(m)}" y="{Y(yc)+(22 if yc==0 else -12)}" text-anchor="middle" font-size="13" font-weight="700" fill="#1f5fa8">C{lado}{num}</text>')
        a(f'<line x1="{X(m)}" y1="{Y(LARGO)}" x2="{X(xe)}" y2="{Y(LARGO)}" stroke="#1f5fa8" stroke-width="1.2" stroke-dasharray="6 4"/>')
        a(f'<circle cx="{X(m)}" cy="{Y(UNION)}" r="6" fill="#c0392b"/>')
        a(f'<text x="{X(m)+(-10 if izq else 10)}" y="{Y(UNION)+5}" text-anchor="{"end" if izq else "start"}" font-size="13" font-weight="700" fill="#c0392b">Unión {lado}</text>')
        r = abs(xe - xs) / 2
        a(f'<text x="{X(xs)+(-8 if izq else 8)}" y="{Y(UNION*0.35)}" text-anchor="{"end" if izq else "start"}" font-size="14" font-weight="700" fill="#8a6400">{lado}1 hacia afuera</text>')
        a(f'<text x="{X(xs)+(-8 if izq else 8)}" y="{Y(UNION*0.35)+16}" text-anchor="{"end" if izq else "start"}" font-size="12" fill="#1f5fa8">{pies(r)} x {pies(UNION)}</text>')
        a(f'<text x="{X(m)+(-8 if izq else 8)}" y="{Y(UNION+(LARGO-UNION)*0.75)}" text-anchor="{"end" if izq else "start"}" font-size="14" font-weight="700" fill="#8a6400">{lado}2 hacia adentro</text>')
        a(f'<text x="{X(m)+(-8 if izq else 8)}" y="{Y(UNION+(LARGO-UNION)*0.75)+16}" text-anchor="{"end" if izq else "start"}" font-size="12" fill="#1f5fa8">{pies(r)} x {pies(LARGO-UNION)}</text>')

    # Cotas
    def cota_h(x1, x2, y, txt, dy=-14):
        a(f'<line x1="{X(x1)}" y1="{y}" x2="{X(x2)}" y2="{y}" stroke="#333" stroke-width="1.2" marker-start="url(#fl)" marker-end="url(#fl)"/>')
        a(f'<text x="{(X(x1)+X(x2))/2}" y="{y+dy}" text-anchor="middle" font-size="14" font-weight="700">{txt}</text>')
    cota_h(xs_izq, xs_der, Y(-30) + 30, f"ÚLTIMO ESCALÓN {pies(ANCHO_ESCALON)}", 22)
    cota_h(xs_izq, 0, Y(-30) + 70, pies(ANCHO_ESCALON / 2), 20)
    cota_h(0, xs_der, Y(-30) + 70, pies(ANCHO_ESCALON / 2), 20)
    cota_h(xe_izq, xe_der, Y(LARGO + 60) - 14, f"{pies(ANCHO_VEREDA)} terminada")
    xv = X(xs_der) + 60
    a(f'<line x1="{xv}" y1="{Y(0)}" x2="{xv}" y2="{Y(LARGO)}" stroke="#333" stroke-width="1.2" marker-start="url(#fl)" marker-end="url(#fl)"/>')
    a(f'<text x="{xv+8}" y="{Y(LARGO/2)}" font-size="14" font-weight="700">{pies(LARGO)}</text>')
    for yy in (0, LARGO):
        a(f'<line x1="{X(xs_der)+5}" y1="{Y(yy)}" x2="{xv+10}" y2="{Y(yy)}" stroke="#999" stroke-width="0.8"/>')

    # Tabla de replanteo
    tx, ty = X(xmax) + 90, my + 10
    a(f'<text x="{tx}" y="{ty}" font-size="17" font-weight="700">REPLANTEO (cada 6 pulgadas)</text>')
    a(f'<text x="{tx}" y="{ty+20}" font-size="12">Medir desde el escalón hacia la vereda,</text>')
    a(f'<text x="{tx}" y="{ty+36}" font-size="12">y de ahí al costado desde la línea de centro.</text>')
    cab = ("Desde escalón", "Izq. (A)", "Der. (B)", "Ancho")
    cols = (0, 105, 185, 265)
    yy = ty + 66
    for c, t in zip(cols, cab):
        a(f'<text x="{tx+c}" y="{yy}" font-size="12" font-weight="700">{t}</text>')
    for k, izq, der, an in tabla():
        yy += 21
        a(f'<line x1="{tx}" y1="{yy-17}" x2="{tx+320}" y2="{yy-17}" stroke="#ddd"/>')
        for c, t in zip(cols, (pies(k), pies(izq), pies(der), pies(an))):
            a(f'<text x="{tx+c}" y="{yy}" font-size="13">{t}</text>')
    yy += 40
    notas = [
        "SUPUESTOS (confirmar antes de armar):",
        f"- Vereda existente {pies(ANCHO_VEREDA)} (medida).",
        "- Su borde izquierdo cae en el centro",
        "  de la escalera (mirando desde la escalera).",
        "",
        "CÓMO ES CADA LADO (curva en S):",
        "- Arco 1 hacia afuera: sale derecho de la",
        "  punta del escalón. Centro en la línea del",
        "  escalón (CA1, CB1).",
        "- Arco 2 hacia adentro: llega derecho al",
        "  borde de la vereda. Centro en la línea de",
        "  la vereda vieja (CA2, CB2).",
        f"- Se unen a {pies(UNION)} del escalón, a mitad",
        "  de camino, sin quiebre.",
        "- Clavar estacas en los puntos de la tabla",
        "  y doblar la tabla/flex (masonite) por ellos.",
    ]
    for t in notas:
        a(f'<text x="{tx}" y="{yy}" font-size="12" font-weight="{"700" if t.endswith(":") else "400"}">{t}</text>')
        yy += 18

    a(f'<text x="{mx}" y="{40}" font-size="24" font-weight="700" font-family="Cinzel, serif">VEREDA CON ARCOS ELÍPTICOS EN S — PLANTA</text>')
    a(f'<text x="{mx}" y="{64}" font-size="13">MOP Construction · 27-oct-2026 · medidas en pies y pulgadas · sin escala para presupuesto</text>')
    a('</svg>')
    return "\n".join(o)


if __name__ == "__main__":
    aqui = pathlib.Path(__file__).parent
    (aqui / "vereda_arcos.svg").write_text(svg(), encoding="utf-8")
    for k, izq, der, an in tabla():
        print(f"{pies(k)} -> izq {pies(izq):>10}  der {pies(der):>10}  ancho {pies(an):>10}")
