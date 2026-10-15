---
description: Activa una habilidad (solo Martin). Uso /activar <nombre>
argument-hint: "<nombre>"
---
Habilidad a activar: $ARGUMENTS
1. Si `.claude/skills/$ARGUMENTS/SKILL.md` no existe, decirlo y listar las que hay.
2. Si su estado es "pendiente de conexión", no activarla: decir qué conexión falta.
3. Cambiar la línea "Estado:" del SKILL.md a "activa", subir la versión menor y anotar la fecha y "activada por Martin".
4. Actualizar la línea en `HABILIDADES.md` y anotar en "Mensajes entre asistentes" de `TABLERO.md`.
5. Avisar en una línea: "activé la habilidad X; se usa diciendo Z".
