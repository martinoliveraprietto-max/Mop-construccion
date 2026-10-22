---
name: traspaso
description: Guarda todo y abre un chat nuevo que sigue donde quedó este. Usar con /traspaso o cuando Martin dice "guardá todo y abrí otro chat", "este chat está muy cargado", "pasalo a otra sesión", y proponerlo solo cuando el chat se pone largo (después de una compactación).
---

# traspaso

**Estado:** activa · **Versión:** v1 · **Fecha:** 22-oct-2026
Nació de /mejorar (22-oct): Martin lo pidió a mano 6 veces en 6 sesiones (17 al 22-oct).

## Cuándo se dispara
- `/traspaso`, "guardá todo y abrí otro chat", "este chat está muy cargado".
- Propuesta propia (una línea, sin hacerlo) cuando el chat ya se compactó una vez.

## Pasos
1. Escribir `TRASPASO.md` en la raíz del repositorio de la sesión (si ya existe, se reemplaza: es siempre el último):
   tema, qué se hizo, qué quedó a medias (con archivo y línea si es código), decisiones de Martin con fecha,
   próximos pasos en orden y qué espera de Martin. Sin llaves, correos, teléfonos ni direcciones si el
   repositorio es público (Mop-construccion lo es).
2. Una línea en "Mensajes entre asistentes" de `TABLERO.md` (si la sesión no está en Mop-construccion, se manda
   esa línea en el mensaje a la sesión nueva para que la anote).
3. Actualizar `HISTORIA.md` si cambió el estado de algún tema.
4. Commit y push a la rama de la sesión (sin push no hay traspaso: la sesión nueva no lo vería).
5. `create_session` (claude-code-remote) con el mismo repositorio y rama, título "<tema> — continuación (<fecha>)",
   y este mensaje inicial: "Seguís el trabajo de otra sesión. Leé CLAUDE.md, TRASPASO.md y TABLERO.md antes de
   hacer nada, y decile a Martin en tres líneas dónde quedamos y cuál es el próximo paso."
6. Avisarle a Martin con el nombre de la sesión nueva y mandarle el audio (`scripts/hablar.py`).

## Qué NO puede hacer
- No archiva ni borra la sesión vieja: eso lo decide Martin.
- No pasa a la sesión nueva tareas que esperan el "aprobado" de Martin como si estuvieran aprobadas.

## Cambios
- v1 (22-oct-2026): creada a partir de la primera corrida de /mejorar.
