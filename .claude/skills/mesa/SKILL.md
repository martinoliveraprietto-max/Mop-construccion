---
name: mesa
description: Mesa de directorio de MOP. Usar cuando Martin escribe "/mesa <pregunta>", "qué dice la mesa", "consultá al consejo" o tiene que decidir algo de negocio (cotizar o no una obra, precio, oferta, seguimiento, contenido, contratar, gastar). Convoca a los 3 coaches del consejo que más saben del tema, cada uno con un método probado y con nombre, sobre los números reales de la memoria, más el abogado del diablo, y cierra con una recomendación. Martin decide.
---

# mesa (mesa de directorio de MOP)

**Estado:** activa · **Versión:** v1 · **Fecha:** 1-nov-2026 · Aprobada por Martin ("dale, armá la habilidad mesa").
Idea tomada de un carrusel de @marcosrazzetti (1-nov), adaptada al consejo de coaches de `CLAUDE.md`: se usan los
MÉTODOS de cada referente, nunca se habla haciéndose pasar por ellos.

## Paso 1: los datos primero (nunca opinar en el aire)
Buscar en la memoria lo que nombra la pregunta (habilidad `memoria`: `select * from public.memoria_buscar('<tema>', 5);`)
y, si hace falta, la caja, lo cobrado en la semana, las propuestas enviadas y ganadas (ficha de la constructora, tablero).
Cada número con su fecha. Lo que no se sabe: "sin dato" (y se dice qué dato cambiaría la recomendación).

## Paso 2: elegir 3 sillas (las que más saben del tema; nunca más de 3)
Cada silla es un coach del consejo de `CLAUDE.md` con su método:
- **Negocios y ofertas** (método Hormozi): ecuación de valor = resultado × probabilidad de lograrlo ÷ (tiempo × esfuerzo
  del cliente). ¿Cómo hacemos la oferta tan clara que sea tonto decir que no? Para MOP: el paquete estructura + framing +
  placa, plazos firmes, una sola llamada para todo.
- **Embudo** (método Brunson): escalera de valor y dónde se pierde la gente. Para MOP: cazador → correo → visita →
  propuesta → ganada; medir cada paso.
- **Respuesta directa** (método Kennedy): un mensaje, un mercado, un medio y un solo pedido por mensaje, con fecha.
- **Ventas y seguimiento** (método Cardone): el que sigue gana; seguimiento con fecha hasta un sí o un no. Para MOP:
  propuestas enviadas que esperan (Kilwins, Sedano's, Flagler).
- **Contenido** (método Gary Vee): documentar, no inventar; obra real todas las semanas en Instagram.
- **Finanzas** (método "Profit First"): caja primero; ninguna decisión que deje la caja sin colchón.
- **Operaciones** (Last Planner / plan de 3 semanas): ¿tenemos gente, días y plano para cumplir? ¿Qué se traba?
- **Ontológico** (juicios y hechos): separar lo que es un hecho de lo que es una opinión; pedidos y promesas claros.
- **Estrategia** (visión del primer millón): ¿esto acerca o aleja de la meta? ¿Diversifica clientes?
- **Astrológico**: solo si Martin lo pide; reflexión, nunca dato para decidir.
Fuera de la mesa: Jordan Belfort (condenado por fraude) y cualquier táctica de presión, engaño o mentira. Persuasión con
la verdad, siempre.

## Paso 3: cada silla habla (2 o 3 frases)
Nombre de la silla y su método · lo que ve en los números · qué recomienda, concreto y con fecha.

## Paso 4: el abogado del diablo (siempre)
Una sola objeción, la más peligrosa (pre-mortem: "pasaron 3 meses y salió mal: ¿por qué?"), con su solución.

## Paso 5: cierre
Una recomendación (sí / no / sí con condición), su costo en plata y tiempo, el riesgo, y el primer paso de hoy.
Si la decisión es grande (precio, contrato, gasto, obra nueva), anotarla en "Decisiones" de `TABLERO.md` con fecha de
revisión a 30 días (como la habilidad `cuestionar`). Lo que se decida se anota en la memoria (ficha de la obra o la
constructora). Martin decide: la mesa aconseja.

## Formato
Respuesta corta para el celular, sin tablas, español rioplatense, con el audio como siempre. Máximo 3 acciones por
semana: si la mesa propone más, elegir las 3 que más acercan a la meta.
