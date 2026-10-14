---
name: explorador
description: Innovación continua de solo lectura. Cada semana (/explorar, domingos a la noche) busca novedades verificables en los campos de EXPLORADOR/campos.md, filtra con tres preguntas y propone máximo tres mejoras; cada mes (/expansion) actualiza el mapa de expansión. Usar cuando Martin dice "explorá", "qué hay de nuevo", "novedades" o "cómo seguimos creciendo".
---

# explorador

**Estado:** activa · **Versión:** v1 · **Fecha:** 14-oct-2026 · Solo lectura.

## Cuándo se dispara
- `/explorar` (programado domingos 20:50 hora de Miami) o "explorá", "qué hay de nuevo", "novedades de <campo>".
- `/expansion` (mensual) o "cómo seguimos creciendo", "mapa de expansión".

## Ciclo semanal (/explorar)
1. Leer qué existe (fuentes): `TABLERO.md`, `HABILIDADES.md`, `EXPLORADOR/campos.md`, `EXPLORADOR/en-espera.md`, README y dependencias de Mop-construccion, solana-signal-bot (bot Solana), tradingview-bot y fabrica-canales (los que estén accesibles en la sesión; si no, anotar "sin acceso"). No proponer lo ya instalado o descartado.
2. Buscar novedades de los últimos 30 días con el agente `explorador` (modelo barato): documentación oficial, repositorios activos, lanzamientos de proveedores.
3. Ficha por hallazgo en `EXPLORADOR/hallazgos/AAAA-MM-DD.md`: qué es, fuente con enlace y fecha, a qué proyecto sirve, mejora concreta con ejemplo, costo en plata y tiempo, riesgo, qué reemplazaría.
4. Filtro de tres preguntas, sin números inventados: ¿mejora un cuello de botella actual? ¿cuesta cero o lo paga un contrato? ¿se prueba en menos de una semana? Solo pasa lo que contesta sí a las tres.
5. Análisis final con el modelo principal. Presentar máximo tres propuestas, de la más fácil a la más completa, con recomendación y cierre: "Recomiendo esta por este motivo. Cambiaría si aparece este dato."
6. Lo no elegido va a `EXPLORADOR/en-espera.md` con fecha de revisión (+30 días).
7. Si nada pasa el filtro: "esta semana sin novedades que valgan".
8. Anotar en "Mensajes entre asistentes" de `TABLERO.md`.

## Visión mensual (/expansion)
- Actualizar `EXPLORADOR/mapa-expansion.md`: dónde está cada proyecto, qué tecnología lo lleva al siguiente escalón, qué hay que tener listo. Lo que haya que preparar pasa a "Anticipación" de `TABLERO.md`.

## Qué devuelve
Máximo tres propuestas en frases cortas, sin tablas, con la recomendación.

## Qué NO puede hacer
- Nunca instala, contrata, se registra ni modifica código.
- Con el bot Solana: solo lectura, auditoría y recomendaciones.
- Ningún gasto ni registro sin "aprobado" de Martin.
- Una idea nueva no cambia la prioridad de la semana: se registra.

## Cambios
- v1 (14-oct-2026): creada; primera corrida el 14-oct.
