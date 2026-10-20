# Respaldo del Drive de MOP en OneDrive (20-oct-2026)

**Camino elegido primero: Google Takeout** (oficial y gratis, sin servidor): takeout.google.com con la cuenta de
MOP → solo "Drive" → entrega "Agregar a OneDrive" → "Exportar cada 2 meses durante 1 año". Hay que renovarlo
cada año.

**Camino de abajo (rclone, todas las noches): EN ESPERA.** Probado el 20-oct con rclone v1.75.2: avisa que la
autorización compartida de rclone para Google Drive "se retira y va a dejar de andar durante 2026". Para usarlo
hace falta crear una autorización propia en Google Cloud (rclone.org/drive/#making-your-own-client-id) y
agregarla en el paso 3 y 4. Solo si Martin quiere respaldo diario.

Por qué así: el conector "Microsoft 365" de Claude solo acepta cuentas de empresa o educativas
("No puede iniciar sesión con una cuenta personal", probado por Martin el 20-oct) y además solo lee.
rclone es gratis, acepta OneDrive personal y corre solo todas las noches en el servidor.

Programa: `herramientas/respaldo_onedrive.sh`. Lee el Drive con permiso de solo lectura y guarda en
OneDrive "Respaldo MOP Drive/actual"; lo borrado o cambiado queda en "Respaldo MOP Drive/borrados/<fecha>".

## Pasos (uno por vez; Martin los pega en Termux)

1. Instalar rclone en el celular (sirve para autorizar con el navegador del celular).
   → Termux
   ```
   pkg install -y rclone
   ```

2. Instalar rclone en el servidor.
   → Termux
   ```
   ssh bot "curl -s https://rclone.org/install.sh | sudo bash"
   ```

3. Autorizar Google Drive en SOLO LECTURA. En el celular:
   → Termux
   ```
   rclone authorize "drive" "eyJzY29wZSI6ImRyaXZlLnJlYWRvbmx5In0"
   ```
   Se abre el navegador: entrar con la cuenta de MOP y aceptar. Termux muestra un texto largo entre
   `--->` y `<---End paste`. Copiarlo entero.

4. Crear el remoto "mopdrive" en el servidor, pegando ese texto donde dice TEXTO (entre comillas simples).
   → Termux
   ```
   ssh bot "rclone config create mopdrive drive scope=drive.readonly token='TEXTO' --non-interactive"
   ```

5. Autorizar OneDrive. En el celular:
   → Termux
   ```
   rclone authorize "onedrive"
   ```
   Entrar con la cuenta de Microsoft de MOP y aceptar. Copiar el texto largo.

6. Crear el remoto "onedrive" en el servidor (rclone pregunta qué disco: elegir el OneDrive personal).
   → Termux
   ```
   ssh bot "rclone config create onedrive onedrive token='TEXTO' --non-interactive"
   ```
   Si pide `drive_id`, correr `ssh bot "rclone config reconnect onedrive:"` y aceptar las opciones.

7. Copiar el programa al servidor, probarlo una vez y dejarlo todas las noches a las 3:17.
   → Termux
   ```
   ssh bot "mkdir -p ~/respaldo_onedrive && curl -s https://raw.githubusercontent.com/martinoliveraprietto-max/Mop-construccion/main/herramientas/respaldo_onedrive.sh -o ~/respaldo_onedrive/respaldo.sh && chmod +x ~/respaldo_onedrive/respaldo.sh && ~/respaldo_onedrive/respaldo.sh; tail -3 ~/respaldo_onedrive/registro.txt"
   ssh bot "(crontab -l 2>/dev/null; echo '17 3 * * * ~/respaldo_onedrive/respaldo.sh') | crontab -"
   ```

8. Comprobar: en la app de OneDrive tiene que aparecer la carpeta "Respaldo MOP Drive".

## Cuidados
- Las autorizaciones quedan en el servidor (`~/.config/rclone/rclone.conf`), como las claves de los
  bots. Nunca se suben a GitHub ni se pegan en un chat.
- Espacio: el OneDrive de MOP tiene 150 GB, con 108,8 GB usados el 20-oct (mucho son fotos del celular).
- Para revisar cómo anduvo: `ssh bot "tail -5 ~/respaldo_onedrive/registro.txt"`.
