<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Instalacion de Ubuntu***

- [***Instalacion de Ubuntu***](#instalacion-de-ubuntu)
  - [***VirtualBox***](#virtualbox)
  - [***Instalar Ubuntu***](#instalar-ubuntu)
  - [***Instalacion en Maquina Virtual***](#instalacion-en-maquina-virtual)
  - [***Designaciones de Disco en Linux***](#designaciones-de-disco-en-linux)
  - [***Instalacion del sistema operativo en Hardware***](#instalacion-del-sistema-operativo-en-hardware)
  - [***Si tenemos problema al particionar el disco se puede deber a muchas razones***](#si-tenemos-problema-al-particionar-el-disco-se-puede-deber-a-muchas-razones)
    - [**¿En máquina virtual es UEFI o Legacy?**](#en-máquina-virtual-es-uefi-o-legacy)
    - [*En **VirtualBox***](#en-virtualbox)
    - [*En **VMware***](#en-vmware)
    - [*En **QEMU/KVM***](#en-qemukvm)
    - [**¿Es necesaria la partición EFI en una máquina virtual?**](#es-necesaria-la-partición-efi-en-una-máquina-virtual)
    - [**Depende del modo en que está arrancando la VM**](#depende-del-modo-en-que-está-arrancando-la-vm)
    - [**Cómo verificar si estás en UEFI o Legacy (Desde El Instalador)**](#cómo-verificar-si-estás-en-uefi-o-legacy-desde-el-instalador)
    - [**Método 1: Desde la terminal del instalador**](#método-1-desde-la-terminal-del-instalador)
    - [**Método 2: Revisar ficheros existentes**](#método-2-revisar-ficheros-existentes)
    - [**Método 3: Revisar el particionado automático**](#método-3-revisar-el-particionado-automático)
    - [**¿Cuándo Se Puede Instalar Ubuntu Sin Crear /boot/efi?**](#cuándo-se-puede-instalar-ubuntu-sin-crear-bootefi)
    - [**1. Cuando YA existe una partición EFI en el disco**](#1-cuando-ya-existe-una-partición-efi-en-el-disco)
    - [**2. Cuando instalas en modo BIOS/Legacy**](#2-cuando-instalas-en-modo-bioslegacy)
    - [**Cuándo Es Obligatorio Crear /Boot/Efi (Vfat)**](#cuándo-es-obligatorio-crear-bootefi-vfat)
    - [**Resumen General (Tabla Definitiva)**](#resumen-general-tabla-definitiva)

---

## ***VirtualBox***

> *Una máquina virtual (VM, por sus siglas en inglés) es un entorno virtualizado que emula un sistema informático físico y permite ejecutar sistemas operativos y aplicaciones como si estuvieran instalados en hardware físico. Esto es útil para probar software, realizar pruebas de seguridad, ejecutar sistemas operativos múltiples en un mismo hardware, entre otros usos.*

- **Para instalar VirtualBox**

  - *Instalar desde su pagina oficial*

    - [***VirtualBox***](https://www.virtualbox.org/ "https://www.virtualbox.org/")

  - *Actualizar el sistema*

      ```bash
      sudo apt-get update
      ```

     ```bash
      sudo apt-get upgrade -y
     ```

  - *Instalar VirtualBox*

     ```bash
      sudo apt-get install -y virtualbox
      ```

     ```bash
      vboxmanage --version
      ```

## ***Instalar Ubuntu***

> *Ubuntu es un sistema operativo de código abierto basado en el kernel de Linux. Es conocido por su enfoque en la facilidad de uso, la estabilidad y la seguridad. Ubuntu se distribuye gratuitamente y está respaldado por una comunidad activa de desarrolladores y usuarios.*

1. **Versiones principales**

   1. **Ubuntu Desktop:**

      1. > *La versión de escritorio estándar, diseñada para usuarios de computadoras personales.*

   2. **Xubuntu:**

      1. *Utiliza el entorno de escritorio Xfce, siendo una opción más ligera y eficiente para sistemas con recursos limitados.*

   3. **Lubuntu:**

      1. > *Ofrece un entorno de escritorio LXQt, diseñado para ser liviano y adecuado para hardware más antiguo o menos potente.*

   4. **Ubuntu Cloud:**

      1. > *Orientado a la implementación y gestión de servicios en la nube, utiliza herramientas como OpenStack.*

   5. **Ubuntu IoT:**
      1. > *Diseñado para dispositivos de Internet de las cosas (IoT), proporciona un entorno de desarrollo para aplicaciones IoT.*

2. **Empresa detrás**

   1. > *Canonical Ltd. es la empresa que respalda y desarrolla Ubuntu. Fue fundada por Mark Shuttleworth y tiene como objetivo promover el uso de software de código abierto.*

3. **Características principales**

   1. **Entorno de escritorio:**

      - *Utiliza el entorno de escritorio GNOME por defecto en la versión estándar, pero ofrece variantes con otros entornos más ligeros.*

   2. **Ciclo de lanzamiento:**

      1. *Ubuntu sigue un ciclo de lanzamiento regular con versiones de soporte a largo plazo (LTS-Long Term Support) y versiones regulares.*

   3. **Centro de Software:**

      1. *Proporciona un fácil acceso a la instalación y gestión de aplicaciones.*

   4. **Seguridad:**
      1. *Ubuntu se enorgullece de su seguridad y ofrece actualizaciones regulares para mantener el sistema protegido.*

---

## ***Instalacion en Maquina Virtual***

1. *Ejecutamos el siguiente comando para abrir virtualbox*

     ```bash
     virtualbox
     ```

      1. *![Image Virtualbox Number #1](../Images/Img%20Virtualbox/00%20Virtualbox.png "../Images/Img Virtualbox/00 Virtualbox.png")*

      2. *![Image Virtualbox Number #2](../Images/Img%20Virtualbox/01%20Virtualbox.png "../Images/Img Virtualbox/01 Virtualbox.png")*

      3. *![Image Virtualbox Number #3](../Images/Img%20Virtualbox/02%20Virtualbox.png "../Images/Img Virtualbox/02 Virtualbox.png")*

      4. *![Image Virtualbox Number #4](../Images/Img%20Virtualbox/03%20Virtualbox.png "../Images/Img Virtualbox/03 Virtualbox.png")*

      5. *![Image Virtualbox Number #5](../Images/Img%20Virtualbox/04%20Virtualbox.png "../Images/Img Virtualbox/04 Virtualbox.png")*

      6. *![Image Virtualbox Number #6](../Images/Img%20Virtualbox/05%20Virtualbox.png "../Images/Img Virtualbox/05 Virtualbox.png")*

      7. *![Image Virtualbox Number #7](../Images/Img%20Virtualbox/06%20Virtualbox.png "../Images/Img Virtualbox/06 Virtualbox.png")*

      8. *![Image Virtualbox Number #8](../Images/Img%20Virtualbox/07%20Virtualbox.png "../Images/Img Virtualbox/07 Virtualbox.png")*

      9. *![Image Virtualbox Number #9](../Images/Img%20Virtualbox/08%20Virtualbox.png "../Images/Img Virtualbox/08 Virtualbox.png")*

      10. *![Image Virtualbox Number #10](../Images/Img%20Virtualbox/09%20Virtualbox.png "../Images/Img Virtualbox/09 Virtualbox.png")*

      11. *![Image Virtualbox Number #11](../Images/Img%20Virtualbox/10%20Virtualbox.png "../Images/Img Virtualbox/10 Virtualbox.png")*

      12. *![Image Virtualbox Number #12](../Images/Img%20Virtualbox/11%20Virtualbox.png "../Images/Img Virtualbox/11 Virtualbox.png")*

      13. *![Image Virtualbox Number #13](../Images/Img%20Virtualbox/12%20Virtualbox.png "../Images/Img Virtualbox/12 Virtualbox.png")*

      14. *![Image Virtualbox Number #14](../Images/Img%20Virtualbox/13%20Virtualbox.png "../Images/Img Virtualbox/13 Virtualbox.png")*

      15. *![Image Virtualbox Number #15](../Images/Img%20Virtualbox/14%20Virtualbox.png "../Images/Img Virtualbox/14 Virtualbox.png")*

      16. *![Image Virtualbox Number #16](../Images/Img%20Virtualbox/15%20Virtualbox.png "../Images/Img Virtualbox/15 Virtualbox.png")*

      17. *![Image Virtualbox Number #17](../Images/Img%20Virtualbox/16%20Virtualbox.png "../Images/Img Virtualbox/16 Virtualbox.png")*

      18. *![Image Virtualbox Number #18](../Images/Img%20Virtualbox/17%20Virtualbox.png "../Images/Img Virtualbox/17 Virtualbox.png")*

      19. *![Image Virtualbox Number #19](../Images/Img%20Virtualbox/18%20Virtualbox.png "../Images/Img Virtualbox/18 Virtualbox.png")*

      20. *![Image Virtualbox Number #20](../Images/Img%20Virtualbox/19%20Virtualbox.png "../Images/Img Virtualbox/19 Virtualbox.png")*

      21. *![Image Virtualbox Number #21](../Images/Img%20Virtualbox/20%20Virtualbox.png "../Images/Img Virtualbox/20 Virtualbox.png")*

      22. *![Image Virtualbox Number #22](../Images/Img%20Virtualbox/21%20Virtualbox.png "../Images/Img Virtualbox/21 Virtualbox.png")*

      23. *![Image Virtualbox Number #23](../Images/Img%20Virtualbox/22%20Virtualbox.png "../Images/Img Virtualbox/22 Virtualbox.png")*

      24. *![Image Virtualbox Number #24](../Images/Img%20Virtualbox/23%20Virtualbox.png "../Images/Img Virtualbox/23 Virtualbox.png")*

      25. *![Image Virtualbox Number #25](../Images/Img%20Virtualbox/24%20Virtualbox.png "../Images/Img Virtualbox/24 Virtualbox.png")*

      26. *![Image Virtualbox Number #26](../Images/Img%20Virtualbox/25%20Virtualbox.png "../Images/Img Virtualbox/25 Virtualbox.png")*

      27. *![Image Virtualbox Number #27](../Images/Img%20Virtualbox/26%20Virtualbox.png "../Images/Img Virtualbox/26 Virtualbox.png")*

      28. *![Image Virtualbox Number #28](../Images/Img%20Virtualbox/27%20Virtualbox.png "../Images/Img Virtualbox/27 Virtualbox.png")*

      29. *![Image Virtualbox Number #29](../Images/Img%20Virtualbox/28%20Virtualbox.png "../Images/Img Virtualbox/28 Virtualbox.png")*

      30. *![Image Virtualbox Number #30](../Images/Img%20Virtualbox/29%20Virtualbox.png "../Images/Img Virtualbox/29 Virtualbox.png")*

      31. *![Image Virtualbox Number #31](../Images/Img%20Virtualbox/30%20Virtualbox.png "../Images/Img Virtualbox/30 Virtualbox.png")*

      32. *![Image Virtualbox Number #32](../Images/Img%20Virtualbox/31%20Virtualbox.png "../Images/Img Virtualbox/31 Virtualbox.png")*

      33. *![Image Virtualbox Number #33](../Images/Img%20Virtualbox/32%20Virtualbox.png "../Images/Img Virtualbox/32 Virtualbox.png")*

      34. *![Image Virtualbox Number #34](../Images/Img%20Virtualbox/33%20Virtualbox.png "../Images/Img Virtualbox/33 Virtualbox.png")*

      35. *![Image Virtualbox Number #35](../Images/Img%20Virtualbox/34%20Virtualbox.png "../Images/Img Virtualbox/34 Virtualbox.png")*

      36. *![Image Virtualbox Number #36](../Images/Img%20Virtualbox/35%20Virtualbox.png "../Images/Img Virtualbox/35 Virtualbox.png")*

      37. *![Image Virtualbox Number #37](../Images/Img%20Virtualbox/36%20Virtualbox.png "../Images/Img Virtualbox/36 Virtualbox.png")*

      38. *![Image Virtualbox Number #38](../Images/Img%20Virtualbox/37%20Virtualbox.png "../Images/Img Virtualbox/37 Virtualbox.png")*

      39. *![Image Virtualbox Number #39](../Images/Img%20Virtualbox/38%20Virtualbox.png "../Images/Img Virtualbox/38 Virtualbox.png")*

      40. *![Image Virtualbox Number #40](../Images/Img%20Virtualbox/39%20Virtualbox.png "../Images/Img Virtualbox/39 Virtualbox.png")*

      41. *![Image Virtualbox Number #41](../Images/Img%20Virtualbox/40%20Virtualbox.png "../Images/Img Virtualbox/40 Virtualbox.png")*

      42. *![Image Virtualbox Number #42](../Images/Img%20Virtualbox/41%20Virtualbox.png "../Images/Img Virtualbox/41 Virtualbox.png")*

      43. *![Image Virtualbox Number #43](../Images/Img%20Virtualbox/42%20Virtualbox.png "../Images/Img Virtualbox/42 Virtualbox.png")*

      44. *![Image Virtualbox Number #44](../Images/Img%20Virtualbox/43%20Virtualbox.png "../Images/Img Virtualbox/43 Virtualbox.png")*

      45. *![Image Virtualbox Number #45](../Images/Img%20Virtualbox/44%20Virtualbox.png "../Images/Img Virtualbox/44 Virtualbox.png")*

      46. *![Image Virtualbox Number #46](../Images/Img%20Virtualbox/45%20Virtualbox.png "../Images/Img Virtualbox/45 Virtualbox.png")*

      47. *![Image Virtualbox Number #47](../Images/Img%20Virtualbox/46%20Virtualbox.png "../Images/Img Virtualbox/46 Virtualbox.png")*

      48. *![Image Virtualbox Number #48](../Images/Img%20Virtualbox/47%20Virtualbox.png "../Images/Img Virtualbox/47 Virtualbox.png")*

      49. *![Image Virtualbox Number #49](../Images/Img%20Virtualbox/48%20Virtualbox.png "../Images/Img Virtualbox/48 Virtualbox.png")*

      50. *![Image Virtualbox Number #50](../Images/Img%20Virtualbox/49%20Virtualbox.png "../Images/Img Virtualbox/49 Virtualbox.png")*

      51. *![Image Virtualbox Number #51](../Images/Img%20Virtualbox/50%20Virtualbox.png "../Images/Img Virtualbox/50 Virtualbox.png")*

      52. *![Image Virtualbox Number #52](../Images/Img%20Virtualbox/51%20Virtualbox.png "../Images/Img Virtualbox/51 Virtualbox.png")*

> *Las particiones son divisiones lógicas en el disco duro de tu computadora que permiten organizar y gestionar el espacio de almacenamiento. Estas divisiones son esenciales por varias razones:*

1. **Gestión del sistema de ficheros:**

   1. > *Las particiones ayudan a organizar y gestionar el sistema de ficheros del sistema operativo. Cada partición puede tener su propio sistema de ficheros y configuración.*

2. **Aislamiento de datos:**

   1. > *Si una partición falla, las demás pueden seguir funcionando. Esto significa que, por ejemplo, si tienes tus ficheros personales en una partición separada, es menos probable que se vean afectados en caso de problemas en otras áreas del sistema.*

3. **Múltiples sistemas operativos:**

   1. > *Si deseas tener varios sistemas operativos en una misma máquina, necesitarás particiones separadas para cada uno.*

4. **Mejora del rendimiento:**

   1. > *Al separar áreas del disco, es posible mejorar el rendimiento de ciertos aspectos del sistema, como la velocidad de acceso a datos.*

> **Un disco puede tener 4 Particiones Primarias es decir un disco puede almacenar 5 sistemas operativos y los discos puede tener varias particiones logicas**

1. **(raíz):**

   1. > *Contiene los ficheros del sistema y directorios principales. Es la partición principal.*

2. **boot:**

   1. > *Almacena los ficheros del kernel y otros ficheros de inicio del sistema.*

3. **home:**

   1. > *Contiene los directorios personales de los usuarios, incluyendo documentos, música, imágenes, etc.*

4. **swap:**

   1. > *Esta es la partición de intercambio y se utiliza como espacio adicional cuando la memoria RAM está llena. Puede mejorar el rendimiento del sistema en situaciones de baja memoria.*

5. **tmp:**

   1. > *Almacena ficheros temporales.*

6. **var:**

   1. > *Contiene datos variables, como registros del sistema y ficheros de spool.*

7. **usr:**

   1. > *Almacena programas y ficheros de sistema que no cambian con frecuencia.*

8. **opt:**
   1. > *Utilizado para instalar software adicional de terceros.*

> *En general, se recomienda crear tres particiones al instalar un sistema operativo, siguiendo una estructura que incluya una partición primaria para el sistema operativo y dos particiones lógicas. Estas dos particiones lógicas suelen ser /Swap y /Home. Veamos el propósito de cada una:*

**Partición primaria para el sistema operativo (/):**

1. *Esta partición es donde se instala el sistema operativo. Contiene los ficheros del sistema, el kernel y otros componentes esenciales para el funcionamiento del sistema.*

2. *Mantener el sistema operativo en una partición separada facilita la gestión y las actualizaciones sin afectar los datos personales.*

**Partición lógica de intercambio (/Swap):**

1. *La partición de intercambio (Swap) actúa como un espacio adicional cuando la memoria RAM está llena. Permite que el sistema operativo transfiera datos temporales al disco duro para evitar problemas de falta de memoria.*

2. *Mejora el rendimiento del sistema en situaciones de uso intensivo de memoria.*

**Partición lógica para ficheros personales (/Home):**

1. *La partición /Home almacena los directorios personales de los usuarios, que incluyen documentos, música, imágenes y configuraciones personales.*

2. *Al tener /Home en una partición separada, los ficheros personales están aislados del sistema operativo. Esto significa que si decides reinstalar o actualizar el sistema operativo, los ficheros personales permanecerán intactos, facilitando la migración y la protección de tus datos.*

---

## ***Designaciones de Disco en Linux***

> *En sistemas operativos basados en Linux, los discos duros y otros dispositivos de almacenamiento son representados en el sistema de ficheros como ficheros en el directorio `/dev`. La designación de disco base suele seguir el patrón `/dev/sda`, donde "sda" podría ser reemplazado por otras letras según la cantidad de discos presentes en el sistema (por ejemplo, `/dev/sdb`, `/dev/sdc`, etc.).*

1. **Particiones Primarias y Lógicas**

   *Cuando se crean particiones en un disco, las designaciones de disco cambian para reflejar estas divisiones. A continuación, se describen las convenciones comunes:*

   - **Disco Completo:** *`/dev/sda` representa todo el disco.*

   - **Particiones Primarias:** *Las particiones primarias se numeran secuencialmente, por ejemplo, `/dev/sda1`, `/dev/sda2`, `/dev/sda3`, etc. Cada número indica una partición primaria diferente en el mismo disco.*

   - **Particiones Lógicas:** *Cuando se utilizan particiones lógicas (generalmente dentro de una partición extendida), las designaciones cambian a `/dev/sda5`, `/dev/sda6`, `/dev/sda7`, etc. La numeración comienza desde 5 para indicar particiones lógicas.*

2. **Diferencia entre Particiones Primarias y Lógicas**

   *La principal diferencia entre particiones primarias y lógicas radica en cómo se utilizan y cómo interactúan con la tabla de particiones:*

   - **Particiones Primarias:** *Están limitadas a un máximo de cuatro por disco. Son independientes y pueden contener sistemas de ficheros o actuar como contenedores para sistemas de ficheros adicionales (por ejemplo, contenedor de una partición extendida).*

   - **Particiones Lógicas:** *Se utilizan cuando se necesitan más de cuatro particiones en un disco. Se crean dentro de una partición extendida, que es una partición primaria especial. La partición extendida actúa como un contenedor para varias particiones lógicas. Esto permite superar la limitación de cuatro particiones primarias.*

3. **Ejemplo Práctico**

   *Supongamos que tenemos un disco `/dev/sda` con tres particiones primarias y una partición extendida con dos particiones lógicas:*

   `/dev/sda1` - *Partición Primaria*
   `/ev/sda2`  - *Partición Primaria*
   `/dev/sda3` - *Partición Primaria*
   `/dev/sda4` - *Partición Extendida*
   `/dev/sda5` - *Partición Lógica*
   `/dev/sda6` - *Partición Lógica*

   *n este ejemplo, `/dev/sda1`, `/dev/sda2`, y `/dev/sda3` son particiones primarias, mientras que `/dev/sda5` y `/dev/sda6` son particiones lógicas dentro de la partición extendida `/dev/sda4`.*

4. **Guest Additions en VirtualBox**

**¿Qué son las Guest Additions?**

> *Las Guest Additions son controladores y utilidades que mejoran la integración y el rendimiento de una máquina virtual en VirtualBox.*

**Funcionalidades Comunes de Guest Additions:**

- **Mejora de Resolución de Pantalla:** *Ajusta automáticamente la resolución de pantalla de la máquina virtual.*
- **Integración del Ratón:** *Permite una transición más fluida entre el sistema anfitrión y el sistema invitado.*
- **Compartición de Directorios:** *Facilita la transferencia de ficheros entre ambos sistemas.*

**Instalación de Guest Additions:**

1. **Iniciar la Máquina Virtual:** *Asegúrate de que tu máquina virtual esté en ejecución.*

2. **Insertar el CD de Guest Additions:**

   - *Desde el menú de VirtualBox, selecciona "Dispositivos" -> "Insertar imagen de CD de Guest Additions..."*
   - *![Image Virtualbox Number #53](../Images/Img%20Virtualbox/52%20Virtualbox.png "../Images/Img Virtualbox/52 Virtualbox.png")*

3. **Acceder al Terminal en el Sistema Invitado:**

   - *En la máquina virtual, abre la terminal.*

   - *Es posible que necesites tener instalados los "build-essential" y los "linux-headers" antes de ejecutar el script de instalación.*

      ```bash
      sudo apt-get install -y build-essential linux-headers-$(uname -r)
      ```

   - *![Image Virtualbox Number #58](../Images/Img%20Virtualbox/57%20Virtualbox.png "../Images/Img Virtualbox/57 Virtualbox.png")*

4. **Ejecutar el script de instalacion:**

   1. *Ir al directorio y ejecutarlo*

      1. *![Image Virtualbox Number #54](../Images/Img%20Virtualbox/53%20Virtualbox.png "../Images/Img Virtualbox/53 Virtualbox.png")*

         ```bash
         cd /media/daniel/VBox_Gas_6.1.38
         ```

      2. *Remplazar daniel por tu usuario y VBox_Gas_6.1.38 con el directorio que te aparece*

         ```bash
         ls
         ```

         1. *![Image Virtualbox Number #55](../Images/Img%20Virtualbox/54%20Virtualbox.png "../Images/Img Virtualbox/54 Virtualbox.png")*

         2. *Actualizamos el sistema*

              ```bash
              sudo apt-get update
              ```

         3. *Terminamos de actualizar el sistema*

              ```bash
               sudo apt-get upgrade -y
               ```

         4. **Ejecutamos el instalador de las Guest Additions**
             - *Utilizamos el siguiente comando para iniciar la instalación de las VirtualBox Guest Additions, que permiten habilitar funciones como el redimensionamiento automático de pantalla, portapapeles compartido y carpetas compartidas:*

             ```bash
             sudo ./VBoxLinuxAdditions.run
             ```

              - *Es importante ejecutarlo con permisos de superusuario (sudo) para que pueda compilar e instalar correctamente los módulos del kernel necesarios.*

      3. *![Image Virtualbox Number #56](../Images/Img%20Virtualbox/55%20Virtualbox.png "../Images/Img Virtualbox/55 Virtualbox.png")*

      4. *![Image Virtualbox Number #57](../Images/Img%20Virtualbox/56%20Virtualbox.png "../Images/Img Virtualbox/56 Virtualbox.png")*

5. **Reiniciar la Máquina Virtual:**

      ```bash
      sudo reboot
      ```

6. *Desde el menú de VirtualBox, selecciona "Dispositivos" -> "Papeles compartidos...", Seleccionar Bidireccional*

7. *Desde el menú de VirtualBox, selecciona "Dispositivos" -> "Arrastrar y soltar...", Seleccionar Bidireccional*

8. **Estos comandos y pasos son específicos para sistemas basados en Debian o Ubuntu. Si estás utilizando una distribución diferente, es posible que necesites adaptar los comandos según los requisitos del sistema operativo invitado.**

---

## ***Instalacion del sistema operativo en Hardware***

***Recomendacion al hacer las particiones para intalar el sistema operativo en hardware***

**Un solo SSD o HDD:**

> *Solo hay que particionar el disco dejando el espacio que puedas, mi recomendación es mitad para Windows mitad para Linux, aunque si tienes un HDD con mucho espacio puedes dejar 200-300 GB para Linux y el resto para Windows si lo usas para juegos o similar.*

**SSD + HDD:**

> *Tienes que particionar el SSD para instalar ahí el sistema operativo, y tienes que particionar el HDD para montar ahí el /home y almacenar tus ficheros. En cuando al SSD recomiendo si es posible mitad para Windows mitad para Linux. El HDD va a tu criterio, deja el espacio que consideres necesario.*

**Un solo disco en el PC (SSD o HDD) pero con disco externo para ficheros:**

> *Se tiene que particionar el disco que tienes en el PC, ya sea SSD o HDD, debes hacer espacio para instalar el Sistema, tus ficheros los almacenas en el disco externo.*

- *[Etcher](https://etcher.balena.io/ "https://etcher.balena.io/")*

> *Balena Etcher es una herramienta de código abierto que se utiliza para escribir imágenes de sistemas operativos en tarjetas SD, unidades flash USB u otros dispositivos de almacenamiento masivo. Su principal función es facilitar la creación de medios de arranque para sistemas operativos, especialmente en el contexto de sistemas basados en Linux y otras plataformas embebidas.*

**Algunas características clave de Balena Etcher incluyen:**

1. **Interfaz Gráfica de Usuario (GUI):** *Balena Etcher ofrece una interfaz gráfica intuitiva y fácil de usar que simplifica el proceso de escritura de imágenes en dispositivos de almacenamiento.*

2. **Multiplataforma:** *Está disponible para sistemas operativos Windows, macOS y Linux, lo que permite a los usuarios de diferentes plataformas utilizar la herramienta de manera consistente.*

3. **Soporte para Formatos** *de Imagen Comunes: Puede escribir imágenes en varios formatos comunes, como ISO, IMG y ZIP, lo que facilita la creación de medios de instalación para sistemas operativos.*

> **Modo de uso**

1. *Necesitaremos una **USB** de almenos 8 GB para arrancar el ordenador desde la **USB***

   1. *Se recomienda que la **USB** este vacia*

2. *Ejecutar el programa*
   1. *Te pedira que seleccione la iso del sistema operativo*
   2. *Segunda cosa que te pedira es la unidad extraible osea el USB*
   3. *De ultimo simplemente lo finalizaremos*
   4. *Y ya con esa **USB** podremos instalar Linux en cualquier ordenador*

> **Primeramente hay que crear las particiones desde windows por que en la maquina virtual no habia ningun sistema operativo instalado**

**Buscar en la barra de busqueda en windows** *Crear y formatear particiones del disco o administracion de discos*

1. *Seleccionar el disco que queremos particionar y luego darle reducir volumen*

2. *Tendremos un limite de espacio para particionar el disco windows no los dira*

3. *Poner la cantidad de espacio que queremos particionar siempre y cuando no sobre pase el limite establecido por windows y listo*

4. *Luego tenemos que configurar la BIOS para arrancar el ordenador desde la USB*

> *La BIOS, que significa "Basic Input/Output System" (Sistema Básico de Entrada/Salida), es un software esencial almacenado en un chip de memoria flash en la placa base de una computadora. La BIOS es fundamental para el inicio y la operación básica del sistema antes de que el sistema operativo se cargue desde el disco duro o cualquier otro dispositivo de almacenamiento.*

1. *Para entrar ala bios hay muchas formas. Mantener presionada la tecla **Shift** y reiniciar el sistema operativo en windows. O apagar el ordenador y presionar las teclas especiales como **f11**,**f12** para abrir la bios*

2. *Cuando entremos ala Bios ir ala opcion modo avanzado y luego ir a **BOOT** y luego colocar la USB de primero para que arranque el sistema operativo desde el usb de primero*

---

## ***Si tenemos problema al particionar el disco se puede deber a muchas razones***

1. *[Guía partition wizard](https://www.partitionwizard.com/partitionmanager/cannot-shrink-volume-win10.html "https://www.partitionwizard.com/partitionmanager/cannot-shrink-volume-win10.html")*

### **¿En máquina virtual es UEFI o Legacy?**

*Depende de la configuración del software de virtualización.*

### *En **VirtualBox***

- *Por defecto: **Legacy / BIOS (CSM)***
- *Si activas: **System → Enable EFI (special OSes)***
  *→ entonces usas **UEFI***

### *En **VMware***

- *La mayoría de versiones modernas usan **UEFI** por defecto en sistemas Linux nuevos.*

### *En **QEMU/KVM***

- *Si usas `OVMF` → **UEFI***
- *Si usas BIOS por defecto → **Legacy***

---

### **¿Es necesaria la partición EFI en una máquina virtual?**

### **Depende del modo en que está arrancando la VM**

| **Modo de arranque** | **¿Necesita partición EFI VFAT?** | **Explicación**                                     |
| -------------------- | --------------------------------- | --------------------------------------------------- |
| **UEFI**             | **Sí**                            | *GRUB se instala en una partición EFI obligatoria.* |
| **Legacy / BIOS**    | **No**                            | *GRUB se instala en el MBR del disco.*              |

- **Conclusión:**

- *Si tu máquina virtual está en **UEFI**, debes crear **/boot/efi***
- *Si está en **Legacy**, NO necesitas partición EFI*

---

### **Cómo verificar si estás en UEFI o Legacy (Desde El Instalador)**

### **Método 1: Desde la terminal del instalador**

*En el menú del USB o en “Try Ubuntu”, abre una terminal:*

```bash
[ -d /sys/firmware/efi ] && echo "UEFI" || echo "Legacy"
```

- *Si devuelve **UEFI** → Estás arrancando en UEFI*
- *Si devuelve **Legacy** → Estás arrancando en BIOS*

---

### **Método 2: Revisar ficheros existentes**

**En UEFI:**

```bash
ls /sys/firmware/efi
```

- *Si devuelve contenido → UEFI*

- **Output**

    ```bash
    config_table  efivars  esrt  fw_platform_size  fw_vendor  runtime  runtime-map  systab
    ```

- *Si da error → Legacy*

---

### **Método 3: Revisar el particionado automático**

- *Si el instalador crea o pide una partición **FAT32 /boot/efi** → Estás en **UEFI***
- *Si solo crea `/` y `swap` → Estás en **Legacy***

---

### **¿Cuándo Se Puede Instalar Ubuntu Sin Crear /boot/efi?**

*Sí, se puede instalar Ubuntu sin crear manualmente la partición VFAT `/boot/efi`, pero **solo en situaciones específicas**. Aquí está explicado claramente:*

---

### **1. Cuando YA existe una partición EFI en el disco**

*Situaciones:*

- *Ya había Windows instalado antes (modo UEFI).*
- *Habías tenido otra distro Linux.*
- *El fabricante dejó creada la partición EFI.*

*En estos casos el instalador detecta automáticamente:*

```bash
/dev/sda1  100–512 MB  FAT32  EFI System Partition
```

*Entonces Ubuntu usa esa partición para:*

- *Instalar GRUB*
- *Montar `/boot/efi`*

- **No necesitas crearla de nuevo.**

---

### **2. Cuando instalas en modo BIOS/Legacy**

**Esto sucede cuando:**

- *El firmware está en **Legacy Mode / CSM***
- *El disco usa **MBR***
- *Secure Boot está **deshabilitado***

*Entonces Ubuntu NO usa particiones EFI.*
*En este caso:*

- *GRUB se instala en el **MBR del disco***
- *No se requiere VFAT ni `/boot/efi`*

---

### **Cuándo Es Obligatorio Crear /Boot/Efi (Vfat)**

*Debes crearla manualmente si:*

- *Estás en modo **UEFI***
- *El disco está en **GPT***
- ***No existe** una partición EFI previa*

*Si no la creas, el instalador fallará con errores como:*

> *“Failed to install grub-efi-amd64”* **o** *“No EFI system partition was found”*

---

### **Resumen General (Tabla Definitiva)**

| **Situación**                        | **¿Requiere /boot/efi (VFAT)?** | **Motivo**                     |
| ------------------------------------ | ------------------------------- | ------------------------------ |
| *Ya existe partición EFI*            | *No*                            | *El instalador la reutiliza.*  |
| *BIOS/Legacy Mode*                   | *No*                            | *GRUB va al MBR.*              |
| *Disco MBR*                          | *No*                            | *MBR no usa EFI.*              |
| *UEFI + disco GPT sin partición EFI* | *Sí*                            | *GRUB necesita partición EFI.* |
| *UEFI con partición EFI borrada*     | *Sí*                            | *Tienes que crearla.*          |
