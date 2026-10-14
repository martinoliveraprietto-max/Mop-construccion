---
name: anticipar
description: Cuando Martin nombra una herramienta, aplicación, cliente, API o camino nuevo, anota en "Anticipación" de TABLERO.md qué conector, habilidad, dato o permiso va a hacer falta, lo deja preparado antes de que lo pida (esqueleto, enlaces oficiales, pasos de conexión) y le avisa en una línea.
---

# anticipar

**Estado:** activa · **Versión:** v1 · **Fecha:** 14-oct-2026

## Cuándo se dispara
- Martin nombra algo nuevo: una herramienta o aplicación ("TikTok", "QuickBooks"), un cliente o constructora nueva, una API, un camino nuevo ("quiero vender por...").
- Frases típicas: "quiero usar", "conectá", "probemos con", "me llamó <empresa nueva>".

## Pasos (con fuente)
1. Revisar si ya está: `TABLERO.md` (Anticipación), `HABILIDADES.md`, `.claude/skills/`, conectores disponibles (en Claude Code: `/mcp`; en la sesión: lista de herramientas).
2. Anotar en OBSERVACIONES.md: `fecha hora · herramienta-nueva · qué · fuente`.
3. Buscar la documentación OFICIAL (sitio del proveedor) y anotar: qué conector, permiso, clave o dato hace falta, y costo (si no está publicado: "sin dato").
4. Preparar: si es una conexión, crear `.claude/skills/<nombre>/SKILL.md` con estado "pendiente de conexión" y los pasos de conexión numerados (cortos, para el celular). Si es un cliente, abrir su ficha en "Obras".
5. Escribir el ítem en "Anticipación" de `TABLERO.md`: qué hace falta, estado (listo / pendiente de conexión / pendiente de Martin), enlace oficial.
6. Avisar a Martin en una línea: "Dejé preparado X para Y; falta Z de tu parte."

## Qué devuelve
Una línea de aviso y, si Martin pregunta, los pasos de conexión.

## Qué NO puede hacer
- No se registra en servicios, no paga, no pide claves por el chat (las claves van solo al entorno).
- No instala nada pago sin "aprobado".

## Cambios
- v1 (14-oct-2026): creada. Primeros ítems: Instagram (API oficial de Meta) y conectores de Gmail, Calendar y Drive.
