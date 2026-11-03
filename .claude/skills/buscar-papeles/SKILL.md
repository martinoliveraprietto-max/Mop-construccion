---
name: buscar-papeles
description: Usar antes de poner "sin dato" en TABLERO.md o de responderle a Martin "no sé", y cada vez que pregunte por un monto, una fecha, un pago, un seguro, una cotización o un contrato. Busca primero en Drive (la planilla "MOP Bandeja de obras (para Claude)" y las carpetas de adjuntos) y en Gmail, y recién después dice "sin dato".
---

# Buscar papeles antes de decir "sin dato"

**Versión:** v2 (1-nov-2026, Cerebro MOP: "la araña que aprende"). Paso 0 y paso 4 nuevos.

## Por qué existe
El 15-oct-2026 Martin tuvo que preguntar por los $308 del seguro. El acuerdo firmado ya estaba en Drive desde el 14-oct,
pero el tablero decía "renovación sin dato".

## Pasos
0. **Memoria primero:** `python3 -m herramientas.memoria buscar "<tema>"` por `execute_sql` (habilidad `memoria`). Si la ficha tiene el dato con fecha reciente, contestar con eso y no seguir.
1. **Drive:** leer la planilla "MOP Bandeja de obras (para Claude)". Ahí está cada correo con adjuntos y la carpeta de Drive donde se guardó.
   Después buscar en Drive por palabras clave del tema (nombre del cliente, de la aseguradora o de la obra).
2. **Gmail:** buscar por remitente y palabras clave de los últimos 60 días. Leer el hilo completo, no solo la vista previa.
2b. **Audios:** transcripciones de audios de Martin (habilidad `memoria`, sección Audios).
3. **Repositorio:** mirar `obras/` en las ramas del repositorio y `HISTORIA.md` de este repositorio.
4. Si aparece el dato: **anotarlo en la memoria** (`python3 -m herramientas.memoria anotar "<ficha>" "<dato>" --fuente "<Gmail o Drive, fecha>" --quien "<asistente>"`), así la próxima vez no se busca. Si es urgente, también en `TABLERO.md` con su fuente y fecha. Este repositorio es PÚBLICO: montos privados, correos y teléfonos no se copian acá; se nombra la fuente (Gmail o Drive).
5. Recién si no aparece en ninguno de los tres: "sin dato", diciendo dónde se buscó.

## Reglas
- No inventar: si el papel dice una cosa pero falta la prueba (por ejemplo, el débito en el banco), decir las dos cosas.
- Solo leer. Nada se manda ni se borra sin el "mandalo" de Martin.
