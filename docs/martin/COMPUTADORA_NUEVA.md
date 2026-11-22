# Computadora nueva: dejarla lista el día que llega

Armado el 21-nov-2026 (decisión de Martin en el chat). **Nada de esto se ejecutó todavía.** La computadora NO está comprada.
Sin claves en este documento: las claves y tokens se cargan a mano en la computadora, nunca acá (repositorio público).

## Qué se compra (decisión de Martin)
- Tope total: $1.500 con el extensor de pantallas incluido. Para la computadora quedan unos $1.140 con impuestos.
- Windows, 16 pulgadas, pantalla táctil, 32 GB de memoria, 1 TB de disco (ideal).
- Candidatas:
  - HP OmniBook X Flip 2 en 1 16" (Ryzen AI 9 465, 32 GB, 512 GB). $999,99 en Best Buy el 13-nov. Precio de hoy: sin dato. Ojo: 512 GB, menos que el ideal.
  - Lenovo Yoga 7a 2 en 1 16" (Ryzen AI 9 465, 32 GB, 1 TB). Precio: sin dato.
- Límite de las dos: sin placa de video dedicada. Blender (render profesional de los 3D para clientes) y video pesado van a andar lentos. Para eso sigue la nube.
- Antes de pagar: que el puerto USB-C de la computadora sirva para el extensor (ver paso 9).

## El día que llega (en orden, uno por vez)

### 1. Primer arranque de Windows
- Cuenta de Microsoft: la de MOP (no la personal, si se puede).
- Correr Windows Update hasta que no pida más reinicios.
- Mirar el disco libre y anotarlo.
- Activar BitLocker (cifrado del disco): si se pierde la computadora, los planos de los constructores no quedan a la vista.

### 2. WSL (Linux adentro de Windows)
Abrir PowerShell como administrador → Claude Code:
```
wsl --install -d Ubuntu-24.04
```
Reiniciar. Al abrir Ubuntu, elegir usuario y contraseña (se anota en papel, no en el chat).
Después, en Ubuntu:
```
sudo apt update && sudo apt upgrade -y
sudo apt install -y git python3 python3-pip python3-venv ffmpeg poppler-utils build-essential curl unzip
```

### 3. Node (para la app, playwright y hyperframes)
En Ubuntu:
```
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs
node --version
```

### 4. Git y GitHub
```
git config --global user.name "Martin Olivera"
git config --global user.email "<el correo de MOP>"
```
Conectar GitHub con la herramienta oficial `gh` (`sudo apt install -y gh` y `gh auth login`, entrar por el navegador). El token queda guardado por `gh`, no en un archivo nuestro.

### 5. Claude Code
Seguir la instalación oficial de https://code.claude.com (en Ubuntu, dentro de WSL). Entrar con la cuenta de claude.ai de MOP. Probar con `claude` y escribir "hola".

### 6. Clonar los dos repositorios
```
mkdir -p ~/mop && cd ~/mop
gh repo clone martinoliveraprietto-max/Mop-construccion
gh repo clone martinoliveraprietto-max/mop-estimador
```
Trabajar siempre dentro de `~/mop` (el disco de Linux), no en `/mnt/c/...`: es mucho más rápido.

### 7. Python y pruebas en verde
mop-estimador:
```
cd ~/mop/mop-estimador
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt edge-tts pyswisseph faster-whisper
python3 -m pytest -q pruebas
```
Mop-construccion:
```
cd ~/mop/Mop-construccion
pip install pillow imageio-ffmpeg yt-dlp
npm install --no-save playwright-core
python3 pruebas/prueba_sitio.py
node pruebas/prueba_navegador.js
```
La app (Expo) de mop-estimador:
```
cd ~/mop/mop-estimador/app && npm install && npm run prueba
```
Si algo falla: copiar el error a Claude Code, no tocar nada a mano.

### 8. Chrome y FFmpeg (videos, hyperframes, Reels)
- Chrome para Windows: de google.com/chrome. Entrar con la cuenta de Google de MOP.
- Dentro de WSL, el navegador para las pruebas: `npx playwright install --with-deps chromium`.
- FFmpeg ya quedó en el paso 2 (`ffmpeg -version` para comprobar).
- hyperframes (videos armados con páginas web): necesita Node 22, Chrome y FFmpeg, los tres de arriba. Cómo se instala exactamente: sin dato en los repositorios; seguir su guía oficial el día que se use y anotar acá los pasos.
- Blender 4.2 LTS (render de los 3D): de blender.org, versión Windows. Va a andar, pero lento (sin placa de video).

### 9. Extensor de tres pantallas (Amazon, llega el domingo 22-nov)
- Leer la caja: casi todos estos extensores necesitan un controlador de "DisplayLink" o del fabricante. Bajarlo SOLO de la página del fabricante que diga la caja (o de synaptics.com si dice DisplayLink).
- Conectarlo al puerto USB-C que tenga el dibujo de pantalla o rayo. Si la computadora no tiene ese puerto, el extensor no anda: revisarlo ANTES de comprar.
- Probarlo los primeros días: si falla, devolverlo dentro del plazo de Amazon (fecha límite: sin dato; mirarla en el pedido).
- Hasta que llegue la computadora, el extensor queda en la caja (no abrir lo que quizá haya que devolver).

### 10. Lo de todos los días
- Google Drive para escritorio (carpetas de obra y "Mop instagram").
- WhatsApp de escritorio (si Martin quiere).
- Acceso directo a la app MOP y a la página Cerebro MOP en Chrome.
- Copia de seguridad: Historial de archivos de Windows a un disco externo, o Drive.

## Sacarle el máximo rendimiento (HP OmniBook X Flip 16, comprada el 21-nov)
Datos de la caja: Ryzen AI 9 465, 32 GB soldados (no se amplía la memoria), 512 GB, pantalla OLED táctil,
gráficos integrados Radeon 880M, 2 puertos Thunderbolt 4. Nada de esto está hecho todavía.

1. **Actualizar todo antes de usarla:** Windows Update hasta el final; después la app "HP Support Assistant"
   (o "myHP") → actualizar BIOS y controladores; después el controlador de gráficos de AMD (amd.com, "AMD Software").
2. **Modo de energía:** enchufada, Configuración → Sistema → Energía → "Máximo rendimiento". En "myHP", el modo
   "Rendimiento" (se calienta más y el ventilador suena más: es normal).
3. **Sacar lo que sobra:** desinstalar la prueba de McAfee (Windows ya trae su antivirus, Defender) y los
   programas de prueba. Configuración → Aplicaciones → Inicio: apagar lo que arranca solo y no hace falta.
4. **Cuidar el disco (512 GB se llenan rápido):** planos y videos en Google Drive "a pedido" (no todo en el
   disco); dejar siempre más de 100 GB libres. Si se llena: disco externo USB-C, o cambiar el disco interno por
   uno de 1-2 TB (un comprador de Best Buy dice que se cambia; confirmarlo con el manual de HP antes de abrir).
5. **WSL con más memoria:** archivo `C:\Users\<usuario>\.wslconfig` con `memory=16GB` y `processors=8`, así Linux
   (Claude Code, pruebas) usa la mitad y Windows sigue fluido.
6. **El extensor KYY:** al puerto Thunderbolt 4 (el del rayo), con su controlador de kyymonitor.com, y la
   computadora enchufada a su cargador. Cuatro pantallas gastan memoria de video: si va lento, bajar el brillo
   o usar 3 pantallas.
7. **Pantalla OLED:** modo oscuro y barra de tareas que se oculta sola (evita marcas de imágenes fijas).
8. **Batería:** en "myHP", carga inteligente (no queda siempre al 100 % si vive enchufada).
9. **3D y video:** Blender corre, pero sin placa de video dedicada es lento. Los renders para clientes siguen en
   la nube. Probar Blender con "Cycles" usando la placa AMD (Preferencias → Sistema → HIP) y, si no la toma, CPU.

## Qué pasa de Termux (celular) y de la Chromebook
- **Termux:** hoy corre el estimador local (`instalar-celular.sh`, puerto 8010) y los bots. Con la computadora:
  - el estimador y las pruebas pasan a la computadora (WSL);
  - los bots: ver cuáles corren de verdad en Termux y decidir uno por uno si pasan a la computadora (tiene que quedar prendida) o siguen en el celular. Sin dato de cuáles están activos hoy: revisarlo ese día.
  - Termux queda como respaldo en la obra (dictar, mirar), no como herramienta principal.
- **Chromebook:** queda como segunda pantalla o para la oficina; nada nuevo se instala ahí. Antes de dejarla: ver si tiene archivos que no estén en Drive y subirlos.
- Las claves que hoy viven en el celular o en la Chromebook: pasarlas a mano a la computadora, una por una, sin escribirlas en ningún chat ni archivo del repositorio.

## Al terminar
- Pruebas en verde de los dos repositorios.
- Anotar en TABLERO.md: qué computadora se compró, precio final, de qué cuenta se pagó, fecha límite de devolución.
