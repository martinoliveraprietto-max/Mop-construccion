---
name: publicar
description: Sube a la web pública de MOP (GitHub Pages) los cambios ya aprobados por Martin, con las pruebas en verde, y confirma que la página en internet quedó actualizada. Usar después de /fotos o de cualquier cambio en index.html, img/ o instagram/.
disable-model-invocation: true
argument-hint: "[mensaje del commit]"
---

# /publicar — subir cambios a la web

Mensaje del commit (puede venir vacío): $ARGUMENTS

Todo en español. Seguir los pasos EN ORDEN; si uno falla, frenar y decir cuál y por qué.

1. **Revisar el cambio.** `git status` y `git diff --stat`. Solo entran archivos de la tarea
   aprobada: nada de `__pycache__`, tokens, `.env`, ni la dirección de la casa de Martin.
2. **Pruebas.** `python3 pruebas/prueba_sitio.py` y `node pruebas/prueba_navegador.js`, las dos
   con código 0. Si alguna falla se arregla la causa; nunca se saltea una prueba.
3. **Commit y push a main.** `git add` de los archivos de la tarea (nunca `git add -A` a
   ciegas), commit con mensaje en español que diga qué cambia, y `git push origin main`.
   Antes, `git fetch origin main`; si main avanzó, `git pull --rebase origin main`. Si la red
   falla, reintentar hasta 4 veces esperando 2, 4, 8 y 16 s. (El gancho `guardia_git.py` vuelve
   a correr la prueba del sitio y frena el commit si falla.)
4. **Confirmar en internet.** GitHub Pages tarda 1 o 2 minutos. Revisar con
   `curl -s https://martinoliveraprietto-max.github.io/Mop-construccion/` que responda 200 y
   que aparezca el cambio (por ejemplo, el nombre de la foto nueva). Si a los 5 minutos no
   aparece, avisar a Martin.
5. **Responder a Martin** con el enlace, qué cambió (en una o dos líneas) y el hash
   (`git log --oneline -1`).
