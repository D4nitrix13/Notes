<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Accede como Root: Bypass de Login en Linux desde GRUB**

**Por Qué La Pantalla Está Negra Y No Ves Grub, Y Cómo Solucionarlo.**

---

## **Causa probable**

**Tienes esta línea en `/etc/default/grub`:**

```bash
GRUB_TIMEOUT_STYLE=hidden
```

*Esto **hace que GRUB no muestre el menú en pantalla**, y como estás usando además:*

```bash
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash noprompt noshell automatic-ubiquity ..."
```

*Ese conjunto de parámetros está diseñado para un **modo instalación automático (como netboot, preseed, etc.)**, **no para un sistema ya instalado**. Esto hace que **el sistema no arranque en modo interactivo** y por eso ves una pantalla negra.*

1. **Instalación desatendida activada**

    *Esto permite crear una VM de Ubuntu lista para usar automáticamente, aunque con configuración de idioma por defecto (en este caso no latinoamericano):*

    * *![Config 1](./Images/Config%201.png "./Images/Config%201.png")*
    * *![Config 2](./Images/Config%202.png "./Images/Config%202.png")*
    * *![Config 3](./Images/Config%203.png "./Images/Config%203.png")*
    * *![Config 4](./Images/Config%204.png "./Images/Config%204.png")*

2. **Corrección del archivo GRUB**

   * *Editado con `sudo nano /etc/default/grub`.*
   * *Modificación del comportamiento del arranque.*
   * *Uso correcto de `sudo update-grub` y `sudo reboot`.*

   * **Archivo original**
    *![Config Bak Grub](./Images/Config%20Bak%20Grub.png "./Images/Config%20Bak%20Grub.png")*

   ```bash
   GRUB_DEFAULT=0
   GRUB_TIMEOUT_STYLE=hidden
   GRUB_TIMEOUT=0
   GRUB_DISTRIBUTOR=`(. /etc/os-release; echo ${NAME:-Ubuntu} ) 2>/dev/null || echo Ubuntu`
   GRUB_CMDLINE_LINUX_DEFAULT="quiet splash noprompt noshell automatic-ubiquity debian-installer/locale=en_US keyboard-configuration/layoutcode=us languagechooser/language-name=English localechooser/supported-locales=en_US.UTF-8 countrychooser/shortlist=CT --"
   GRUB_CMDLINE_LINUX=""
   ```

   * **Archivo modificado**

    *![Config Good Grub](./Images/Config%20Good%20Grub.png "./Images/Config%20Good%20Grub.png")*

   ```bash
   GRUB_DEFAULT=0
   GRUB_TIMEOUT_STYLE=menu
   GRUB_TIMEOUT=5
   GRUB_DISTRIBUTOR=`(. /etc/os-release; echo ${NAME:-Ubuntu} ) 2>/dev/null || echo Ubuntu`
   GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
   GRUB_CMDLINE_LINUX=""
   ```

3. **Modificación del GRUB en arranque**

    *![View Grub](./Images/Grub%201.png "./Images/Grub%201.png")*

   * *En la entrada GRUB, presionas `e`.*

    *![Content Grub](./Images/Grub%202.png "./Images/Grub%202.png")*
    *![Content Grub](./Images/Grub%203.png "./Images/Grub%203.png")*

   * *Reemplazas `ro quiet splash` por `rw init=/bin/bash`.*
    *![Exit Grub](./Images/Grub%204.png "./Images/Grub%204.png")*

    **Presiona `Ctrl` + `x` para iniciar con los cambios.**

    *Con esto, logras que el sistema se inicie directamente en una **shell bash como root**, sin pasar por login.*

---

## **Comportamiento del sistema tras el arranque**

*![Vista Del Arranque Grub](./Images/Grub%205.png "./Images/Grub%205.png")*

*El sistema termina de montar los discos, muestra algunos mensajes como:*

```bash
bash: cannot set terminal process group (-1): Inappropriate ioctl for device
bash: no job control in this shell
```

**Y deja el prompt así:**

```bash
root@(none):/#
```

---

### **Verificación de privilegios**

*![Verificación Privilegios](./Images/Grub%206.png "./Images/Grub%206.png")*

```bash
whoami
# → root

id
# → uid=0(root) gid=0(root) groups=0(root)
```

*Confirmas que tienes acceso **total como root**.*

---

### **Ver usuarios con shell bash**

*![grep bash](./Images/Grub%207.png "./Images/Grub%207.png")*

```bash
grep bash /etc/passwd
```

**Salida:**

```bash
root:x:0:0:root:/root:/bin/bash
vboxuser:x:1000:1000:vboxuser:/home/vboxuser:/bin/bash
```

*Detectas que `vboxuser` es el primer usuario creado automáticamente.*

---

### **Copia de respaldo del archivo shadow**

*![cp shadow](./Images/Grub%208.png "./Images/Grub%208.png")*

```bash
cp /etc/shadow /home/vboxuser/shadow -v
```

*Esto guarda una copia del archivo de contraseñas para restaurar si fuera necesario.*

---

### **Cambio de contraseña**

*![Change Password](./Images/Grub%209.png "./Images/Grub%209.png")*

```bash
passwd vboxuser
```

*Ingresas una nueva contraseña dos veces.*
*Mensaje: `password updated successfully`.*

---

### **Reinicio forzado del sistema**

*![reboot](./Images/Grub%2010.png "./Images/Grub%2010.png")*

```bash
reboot -f
```

*Este comando reinicia sin pasar por el gestor de apagado habitual.*

---

### **Nota sobre el error**

**Si tras el `reboot -f` recibes el error:**

```bash
FATAL: Keyboard error: 955
```

*Solución: **reinicia la máquina desde VirtualBox (botón de reinicio de la ventana)**.*
*Referencia: [Foro VirtualBox - Error 955](https://kmgadvice.com/virtualbox-fatal-keyboard-error-995-solved/ "https://kmgadvice.com/virtualbox-fatal-keyboard-error-995-solved/")*

---

## **¿Qué es el GRUB?**

> ***GRUB (GRand Unified Bootloader)** es el **gestor de arranque** que usa la mayoría de sistemas Linux para cargar el sistema operativo.*
*Es lo primero que aparece al encender una máquina con Linux y te permite seleccionar cómo o qué sistema arrancar.*

*![GRUB Menu](./Images/Grub%201.png "./Images/Grub%201.png")*

---

## **¿Qué pasa cuando presionas la tecla `e`?**

*Cuando presionas `e`, entras en el **modo de edición temporal del GRUB**, donde puedes **modificar los parámetros de arranque del kernel**.*

*![Edición GRUB 1](./Images/Grub%202.png "./Images/Grub%202.png")*
*![Edición GRUB 2](./Images/Grub%203.png "./Images/Grub%203.png")*

## **¿Cómo se aplican los cambios en modo edición?**

*Una vez editado el comando de arranque:*

**Presiona `Ctrl` + `x` para iniciar con los cambios.**
    *Esto no guarda los cambios permanentemente, solo aplica para esa sesión. En el próximo reinicio se cargará la configuración original.*

---

## **¿Qué significa cada parte del comando `linux ...`?**

```bash
linux /boot/vmlinuz-6.14.0-23-generic root=UUID=... ro quiet splash crashkernel=... vt.handoff ...
```

* *`linux /boot/vmlinuz-...`: Indica la ruta del **kernel Linux** que se va a cargar.*
* *`root=UUID=...`: Le dice al kernel qué partición montar como sistema raíz (`/`).*
* *`ro`: Monta el sistema de archivos como **read-only (solo lectura)** al inicio.*
* *`quiet`: Oculta mensajes del sistema al arrancar (para un inicio limpio).*
* *`splash`: Muestra un gráfico o logo de carga en lugar de los logs.*
* *`crashkernel=...`: Reserva memoria para volcados de errores del kernel.*

---

## **¿Qué pasa si cambias `ro quiet splash` por `rw init=/bin/bash`?**

*![Edición final GRUB](./Images/Grub%204.png "./Images/Grub%204.png")*

* *`rw`: Monta el sistema **en modo lectura/escritura**, necesario para cambiar archivos o contraseñas.*
* *`init=/bin/bash`: Le dices al kernel que **en vez de cargar todo el sistema**, te arranque directamente una **shell Bash como root** (sin login, sin servicios, sin GUI).*

*Esto es lo que permite que accedas sin contraseña a una terminal root y puedas hacer tareas administrativas como cambiar claves.*

---

## **¿Qué es un bootloader y por qué GRUB lo es?**

*Un **bootloader** es un programa que **carga el sistema operativo** desde el disco al arrancar el equipo.*

* ***BIOS/UEFI** → Carga **GRUB***
* ***GRUB** → Carga el **kernel de Linux***
* ***Kernel** → Arranca el sistema operativo*

*Entonces, **GRUB es un bootloader** que actúa como intermediario entre el firmware y el sistema operativo.*

---

### **En resumen**

| **Comando o término** | **Significado**                                   |
| --------------------- | ------------------------------------------------- |
| *`GRUB`*              | *Gestor de arranque de Linux*                     |
| *Presionar `e`*       | *Editar temporalmente los parámetros de arranque* |
| *`ro`*                | *Montar raíz en modo solo lectura*                |
| *`rw`*                | *Montar raíz con permisos de escritura*           |
| *`quiet splash`*      | *Ocultar logs y mostrar logo*                     |
| *`init=/bin/bash`*    | *Arrancar directamente una shell bash como root*  |
| *Bootloader*          | *Cargador de arranque; GRUB es uno*               |

---

### **Caracters**

| *Símbolo Que Necesitas* | *Tecla Real A Presionar En Teclado* |
| ----------------------- | ----------------------------------- |
| *`/`*                   | *`-` (Guion)*                       |
| *`=`*                   | *`¿`*                               |
| *`'` (Comilla Simple)*  | *`{`*                               |
| *`-`*                   | *`'`*                               |
| *`&`*                   | *`Shift + 7`*                       |
