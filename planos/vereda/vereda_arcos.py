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
BORDE_IZQ_VEREDA = -ANCHO_VEREDA # borde DERECHO de la vereda = centro de la escalera:
                                 # el lado ancho queda a la derecha (foto de Martin, 27-oct)
ESPESOR = 4                      # losa de 4" (para el cálculo de hormigón)
                                 # (mirando desde la escalera hacia la vereda)

xs_izq, xs_der = -ANCHO_ESCALON / 2, ANCHO_ESCALON / 2
xe_izq, xe_der = BORDE_IZQ_VEREDA, BORDE_IZQ_VEREDA + ANCHO_VEREDA


UNION = LARGO / 2                # punto de unión de los dos arcos de cada lado


ANGULO = math.radians(60)        # cuánto de cada elipse se usa (60° = S suave)


# Cada lado es una S de dos arcos de elipse que se cruzan en diagonal en la unión
# (misma tangente, sin quiebre ni "escalón"):
#  arco 1 (hacia afuera): sale derecho (perpendicular) de la punta del escalón;
#  arco 2 (hacia adentro): llega derecho al borde de la vereda.
# Las dos elipses son proporcionales; si la unión está a mitad de camino son iguales.
def ejes(xs, xe):
    """Semiejes (horizontal con signo, vertical) del arco 1 y del arco 2."""
    r = (xe - xs) * math.sin(ANGULO) / (LARGO * (1 - math.cos(ANGULO)))
    b1, b2 = UNION / math.sin(ANGULO), (LARGO - UNION) / math.sin(ANGULO)
    return (r * b1, b1), (r * b2, b2)


def centros(xs, xe):
    (a1, _), (a2, _) = ejes(xs, xe)
    return (xs + a1, 0), (xe - a2, LARGO)


def union(xs, xe):
    (a1, b1), _ = ejes(xs, xe)
    return xs + a1 * (1 - math.cos(ANGULO)), UNION


FORMA = "s"                      # "s" = dos arcos elípticos por lado, "recta" = línea recta


def punto(xs, xe, u):
    """u de 0 (escalón) a 1 (vereda)."""
    if FORMA == "recta":
        return xs + (xe - xs) * u, LARGO * u
    (a1, b1), (a2, b2) = ejes(xs, xe)
    if u <= 0.5:
        t = 2 * u * ANGULO
        return xs + a1 * (1 - math.cos(t)), b1 * math.sin(t)
    t = 2 * (1 - u) * ANGULO
    return xe - a2 * (1 - math.cos(t)), LARGO - b2 * math.sin(t)


def x_en(xs, xe, y):
    if FORMA == "recta":
        return xs + (xe - xs) * y / LARGO
    (a1, b1), (a2, b2) = ejes(xs, xe)
    if y <= UNION:
        t = math.asin(min(1.0, y / b1))
        return xs + a1 * (1 - math.cos(t))
    t = math.asin(min(1.0, (LARGO - y) / b2))
    return xe - a2 * (1 - math.cos(t))


def area_pie2():
    n, total = 400, 0.0
    for i in range(n):
        y = (i + 0.5) * LARGO / n
        total += (x_en(xs_der, xe_der, y) - x_en(xs_izq, xe_izq, y)) * LARGO / n
    return total / 144


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
    # estacas cada 6"
    for k in range(1, 16):
        y = k * 6
        for xs, xe in ((xs_izq, xe_izq), (xs_der, xe_der)):
            a(f'<circle cx="{X(x_en(xs, xe, y)):.1f}" cy="{Y(y):.1f}" r="3.2" fill="#fff" stroke="#5a4a20" stroke-width="1.5"/>')
    for p, col in ((pts, "#b8860b"), (ptd, "#b8860b")):
        d = "M" + " L".join(f"{X(x):.1f},{Y(y):.1f}" for x, y in p)
        a(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="4"/>')
    a(f'<text x="{X(18)}" y="{Y(30)}" text-anchor="middle" font-size="16" font-weight="700" fill="#5a4a20">VEREDA NUEVA</text>')

    # Centro de escalera
    a(f'<line x1="{X(0)}" y1="{Y(-30)}" x2="{X(0)}" y2="{Y(LARGO+66)}" stroke="#c0392b" stroke-width="1.5" stroke-dasharray="12 5 3 5"/>')
    a(f'<text x="{X(0)+6}" y="{Y(LARGO+64)}" text-anchor="start" font-size="12" fill="#c0392b">CENTRO ESCALERA</text>')
    a(f'<text x="{X(0)}" y="{Y(-30)+110}" text-anchor="middle" font-size="12" fill="#555">Visto parado en la escalera, mirando hacia la vereda vieja</text>')
    for xx, txt in ((xs_izq, "LADO ANGOSTO"), (xs_der, "LADO ANCHO")):
        a(f'<text x="{X(xx)+(-10 if xx<0 else 10)}" y="{Y(-12)}" text-anchor="{"end" if xx<0 else "start"}" font-size="13" font-weight="700" fill="#555">{txt}</text>')

    if FORMA == "recta":
        for xs, xe, lado in ((xs_izq, xe_izq, "A"), (xs_der, xe_der, "B")):
            izq = xs < 0
            largo = math.hypot(xe - xs, LARGO)
            ang = math.degrees(math.atan2(abs(xe - xs), LARGO))
            xx, yy = (xs + xe) / 2, LARGO / 2
            anc, dx = ("end", -45) if izq else ("start", 45)
            a(f'<text x="{X(xx)+dx}" y="{Y(yy)}" text-anchor="{anc}" font-size="14" font-weight="700" fill="#8a6400">LADO {lado} RECTO</text>')
            a(f'<text x="{X(xx)+dx}" y="{Y(yy)+16}" text-anchor="{anc}" font-size="12" fill="#1f5fa8">largo {pies(largo)}</text>')
            a(f'<text x="{X(xx)+dx}" y="{Y(yy)+32}" text-anchor="{anc}" font-size="12" fill="#1f5fa8">corre {pies(abs(xe - xs))} en 8\' ({ang:.0f}°)</text>')
    else:
        for xs, xe, lado in ((xs_izq, xe_izq, "A"), (xs_der, xe_der, "B")):
            m, _ = union(xs, xe)
            izq = xs < 0
            (a1, b1), (a2, b2) = ejes(xs, xe)
            for (cx, cy), num, ext in zip(centros(xs, xe), (1, 2), (xs, xe)):
                nombre = f"C{lado}{num}"
                if not xmin <= cx <= xmax:   # centro fuera de la hoja: se marca en el borde
                    nombre += f" (a {pies(abs(cx))} del centro)"
                    cx = max(xmin, min(xmax, cx))
                a(f'<circle cx="{X(cx)}" cy="{Y(cy)}" r="5" fill="#1f5fa8"/>')
                a(f'<line x1="{X(cx)}" y1="{Y(cy)}" x2="{X(ext)}" y2="{Y(cy)}" stroke="#1f5fa8" stroke-width="1.2" stroke-dasharray="6 4"/>')
                anc = "middle" if abs(cx) < xmax else ("end" if cx > 0 else "start")
                a(f'<text x="{X(cx)}" y="{Y(cy)+(22 if cy==0 else -12)}" text-anchor="{anc}" font-size="13" font-weight="700" fill="#1f5fa8">{nombre}</text>')
            a(f'<circle cx="{X(m)}" cy="{Y(UNION)}" r="6" fill="#c0392b"/>')
            a(f'<text x="{X(m)+(-12 if izq else 12)}" y="{Y(UNION)+5}" text-anchor="{"end" if izq else "start"}" font-size="13" font-weight="700" fill="#c0392b">Unión {lado}</text>')
            for txt, yy, xx, med in ((f"{lado}1 hacia afuera", UNION * 0.3, xs, f"elipse {pies(abs(a1))} x {pies(b1)}"),
                                     (f"{lado}2 hacia adentro", UNION + (LARGO - UNION) * 0.75, xe, f"elipse {pies(abs(a2))} x {pies(b2)}")):
                anc = "end" if izq else "start"
                dx = (-10 if izq else 10) * (1 if xx == xs else 3)
                a(f'<text x="{X(xx)+dx}" y="{Y(yy)}" text-anchor="{anc}" font-size="14" font-weight="700" fill="#8a6400">{txt}</text>')
                a(f'<text x="{X(xx)+dx}" y="{Y(yy)+16}" text-anchor="{anc}" font-size="12" fill="#1f5fa8">{med}</text>')


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
        "- Su borde DERECHO cae en el centro de la",
        "  escalera: el lado ancho queda a la derecha.",
        "",
    ] + ([
        "CÓMO ES CADA LADO (línea recta):",
        "- Va derecho de la punta del escalón a la",
        "  esquina de la vereda vieja.",
        "- Hilo tirante entre las dos puntas y",
        "  tabla recta: no hace falta tabla flexible.",
        "- Las medidas de la tabla sirven para",
        "  controlar el hilo.",
    ] if FORMA == "recta" else [
        "CÓMO ES CADA LADO (curva en S):",
        "- Arco 1 hacia afuera: sale derecho de la",
        "  punta del escalón. Centro sobre la línea",
        "  del escalón (CA1, CB1).",
        "- Arco 2 hacia adentro: llega derecho al",
        "  borde de la vereda. Centro sobre la línea",
        "  de la vereda vieja (CA2, CB2).",
        f"- Se cruzan en diagonal a {pies(UNION)} del",
        "  escalón: la curva no se aplana ni quiebra.",
        "- Clavar estacas en los puntos (o) de la tabla",
        "  y doblar la tabla/flex (masonite) por ellos.",
    ]) + [
        "",
        "CANTIDADES:",
        f"- Superficie: {area_pie2():.0f} pies cuadrados.",
        f"- Hormigón a {ESPESOR}\": {area_pie2()*ESPESOR/12/27:.2f} yd³",
        f"  (con 10% de desperdicio: {area_pie2()*ESPESOR/12/27*1.1:.2f} yd³).",
    ]
    for t in notas:
        a(f'<text x="{tx}" y="{yy}" font-size="12" font-weight="{"700" if t.endswith(":") else "400"}">{t}</text>')
        yy += 18

    a(f'<text x="{mx}" y="{40}" font-size="24" font-weight="700" font-family="Cinzel, serif">VEREDA {'CON LADOS RECTOS' if FORMA == 'recta' else 'CON ARCOS ELÍPTICOS EN S'} — {TITULO}</text>')
    a(f'<text x="{mx}" y="{64}" font-size="13">MOP Construction · 27-oct-2026 · medidas en pies y pulgadas · sin escala para presupuesto</text>')
    a('</svg>')
    return "\n".join(o)


OPCIONES = [
    # archivo, título, unión desde el escalón, ángulo de los arcos
    ("vereda_arcos", "OPCIÓN 1 · PAREJA", LARGO / 2, 60, "s"),
    ("vereda_opcion2", "OPCIÓN 2 · CAMPANA LARGA", 60, 60, "s"),
    ("vereda_opcion3", "OPCIÓN 3 · ENTRADA LARGA Y SUAVE", 36, 50, "s"),
    ("vereda_recta", "OPCIÓN 4 · RECTA", LARGO / 2, 60, "recta"),
]

if __name__ == "__main__":
    aqui = pathlib.Path(__file__).parent
    for archivo, TITULO, UNION, grados, FORMA in OPCIONES:
        ANGULO = math.radians(grados)
        (aqui / f"{archivo}.svg").write_text(svg(), encoding="utf-8")
        print(f"{TITULO}: {area_pie2():.1f} pie2")
        for k, izq, der, an in tabla():
            print(f"  {pies(k)} -> izq {pies(izq):>10}  der {pies(der):>10}  ancho {pies(an):>10}")
