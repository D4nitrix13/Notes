<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***Instalación de XAMPP en Linux***

## **¿Qué es XAMPP y qué significa?**

- *XAMPP es un paquete de software libre que proporciona un entorno de desarrollo integrado. Su nombre es un acrónimo de los componentes principales que incluye:*

- **X:** *Multiplataforma (funciona en Windows, Linux y macOS).*
- **A:** *Apache, el servidor web más utilizado.*
- **M:** *MariaDB, un sistema de gestión de bases de datos.*
- **P:** *PHP, un lenguaje de programación enfocado en el desarrollo web.*
- **P:** *Perl, un lenguaje de programación muy utilizado en scripts y aplicaciones web.*

- *XAMPP es ampliamente utilizado por desarrolladores para probar y ejecutar aplicaciones web localmente antes de implementarlas en un servidor en producción.*

---

- ***Pasos para instalar XAMPP en Linux***

1. **Ir a la página oficial de XAMPP**  
   - **Abre tu navegador y visita la página oficial de descargas de Apache Friends:**
   - *[https://www.apachefriends.org/download.html](https://www.apachefriends.org/download.html "https://www.apachefriends.org/download.html")*

2. **Descargar el instalador de XAMPP usando `wget`**  
   - *Utiliza el siguiente comando en tu terminal para descargar el instalador más reciente de XAMPP desde SourceForge:*

   ```bash
   wget https://sourceforge.net/projects/xampp/files/XAMPP%20Linux/8.2.12/xampp-linux-x64-8.2.12-0-installer.run
   ```

    ```bash
    
    wget https://sourceforge.net/projects/xampp/files/XAMPP%20Linux/8.2.12/xampp-linux-x64-8.2.12-0-installer.run
    --2024-12-11 18:38:58--  https://sourceforge.net/projects/xampp/files/XAMPP%20Linux/8.2.12/xampp-linux-x64-8.2.12-0-installer.run
    Resolving sourceforge.net (sourceforge.net)... 104.18.12.149, 104.18.13.149, 2606:4700::6812:d95, ...
    Connecting to sourceforge.net (sourceforge.net)|104.18.12.149|:443... connected.
    HTTP request sent, awaiting response... 301 Moved Permanently
    Location: https://sourceforge.net/projects/xampp/files/XAMPP%20Linux/8.2.12/xampp-linux-x64-8.2.12-0-installer.run/ [following]
    --2024-12-11 18:38:59--  https://sourceforge.net/projects/xampp/files/XAMPP%20Linux/8.2.12/xampp-linux-x64-8.2.12-0-installer.run/
    Reusing existing connection to sourceforge.net:443.
    HTTP request sent, awaiting response... 301 Moved Permanently
    Location: https://sourceforge.net/projects/xampp/files/XAMPP%20Linux/8.2.12/xampp-linux-x64-8.2.12-0-installer.run/download [following]
    --2024-12-11 18:38:59--  https://sourceforge.net/projects/xampp/files/XAMPP%20Linux/8.2.12/xampp-linux-x64-8.2.12-0-installer.run/download
    Reusing existing connection to sourceforge.net:443.
    HTTP request sent, awaiting response... 302 Found
    Location: https://downloads.sourceforge.net/project/xampp/XAMPP%20Linux/8.2.12/xampp-linux-x64-8.2.12-0-installer.run?ts=gAAAAABnWdxDbAcnf8T7h9-8UY142US9eDtq-ACmO0dEOdIkXS0BTue9ehR-T1p6PAV6LkMYaM1MewcIwQqIEAJAP8v_UtqIPg%3D%3D&use_mirror=cytranet-dal&r= [following]
    --2024-12-11 18:38:59--  https://downloads.sourceforge.net/project/xampp/XAMPP%20Linux/8.2.12/xampp-linux-x64-8.2.12-0-installer.run?ts=gAAAAABnWdxDbAcnf8T7h9-8UY142US9eDtq-ACmO0dEOdIkXS0BTue9ehR-T1p6PAV6LkMYaM1MewcIwQqIEAJAP8v_UtqIPg%3D%3D&use_mirror=cytranet-dal&r=
    Resolving downloads.sourceforge.net (downloads.sourceforge.net)... 104.18.12.149, 104.18.13.149, 2606:4700::6812:c95, ...
    Connecting to downloads.sourceforge.net (downloads.sourceforge.net)|104.18.12.149|:443... connected.
    HTTP request sent, awaiting response... 302 Found
    Location: https://cytranet-dal.dl.sourceforge.net/project/xampp/XAMPP%20Linux/8.2.12/xampp-linux-x64-8.2.12-0-installer.run?viasf=1 [following]
    --2024-12-11 18:39:00--  https://cytranet-dal.dl.sourceforge.net/project/xampp/XAMPP%20Linux/8.2.12/xampp-linux-x64-8.2.12-0-installer.run?viasf=1
    Resolving cytranet-dal.dl.sourceforge.net (cytranet-dal.dl.sourceforge.net)... 162.226.127.129
    Connecting to cytranet-dal.dl.sourceforge.net (cytranet-dal.dl.sourceforge.net)|162.226.127.129|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 160483784 (153M) [application/x-makeself]
    Saving to: 'xampp-linux-x64-8.2.12-0-installer.run'

    xampp-linux-x64-8.2.12-0-installer.ru 100%[======================================================================>] 153.05M  18.5MB/s    in 8.8s

    2024-12-11 18:39:09 (17.4 MB/s) - 'xampp-linux-x64-8.2.12-0-installer.run' saved [160483784/160483784]
    ```

3. **Dar permisos de ejecución al fichero descargado**  
   - *Después de descargar el instalador, debes asegurarte de que tiene permisos de ejecución. Ejecuta el siguiente comando:*

    ```bash
    ls -l xampp-linux-x64-8.2.12-0-installer.run
    -rw-r--r-- 1 vscode vscode 160483784 Nov 25  2023 xampp-linux-x64-8.2.12-0-installer.run
    ```

    ```bash
    chmod +x xampp-linux-x64-8.2.12-0-installer.run
    ```

4. **Ejecutar el instalador**  
   - *Inicia el proceso de instalación ejecutando el fichero descargado:*

   ```bash
   yes | sudo ./xampp-linux-x64-8.2.12-0-installer.run
   ```

   ```bash
   
   yes | sudo ./xampp-linux-x64-8.2.12-0-installer.run
   ----------------------------------------------------------------------------
   Welcome to the XAMPP Setup Wizard.

   ----------------------------------------------------------------------------
   Select the components you want to install; clear the components you do not want
   to install. Click Next when you are ready to continue.

   XAMPP Core Files : Y (Cannot be edited)

   XAMPP Developer Files [Y/n] :
   Is the selection above correct? [Y/n]:
   ----------------------------------------------------------------------------
   Installation Directory

   XAMPP will be installed to /opt/lampp
   Press [Enter] to continue:
   ----------------------------------------------------------------------------
   Setup is now ready to begin installing XAMPP on your computer.

   Do you want to continue? [Y/n]:
   ----------------------------------------------------------------------------
   Please wait while Setup installs XAMPP on your computer.

   Installing
   0% ______________ 50% ______________ 100%
   #########################################

   ----------------------------------------------------------------------------
   Setup has finished installing XAMPP on your computer.
   ```

---

## **1. Comando: `xhost +local:docker`**

- **¿Qué hace?**

- *El comando `xhost` se utiliza para controlar el acceso a la pantalla de X (servidor X) en sistemas Linux. El servidor X es el componente que maneja las interfaces gráficas en sistemas Unix-like, y `xhost` se usa para configurar qué usuarios o clientes pueden conectarse a este servidor.*

- **`xhost +local:docker`:**
  - *Este comando le dice al servidor X que **permita las conexiones locales de Docker**. Esto es necesario cuando deseas ejecutar aplicaciones gráficas (como el gestor de XAMPP que intentas usar) desde un contenedor Docker y mostrar su salida gráfica en tu pantalla.*

- **Salida:**

```bash
non-network local connections being added to access control list
```

- **Explicación:** *Esta salida indica que el acceso para conexiones locales (que no son de red) ha sido **permitido** para los contenedores Docker. Esto es importante porque le da al contenedor permiso para acceder al servidor gráfico de tu sistema y mostrar la interfaz gráfica en tu pantalla.*

```bash
sudo ./manager-linux-x64.run
```

```bash
sudo ./manager-linux-x64.run
couldn't load file "/tmp/tclGkEbJI": libX11.so.6: cannot open shared object file: No such file or directory
```

- **Error: `couldn't load file "/tmp/tclGkEbJI": libX11.so.6: cannot open shared object file: No such file or directory`**

- **¿Qué significa?**
- *Este error indica que el programa que estás intentando ejecutar (en este caso, `manager-linux-x64.run` de XAMPP) no puede encontrar una de las bibliotecas necesarias para funcionar, en este caso **`libX11.so.6`**. Esta es una biblioteca esencial para interactuar con el servidor X (el sistema gráfico en Linux).*

- **`libX11.so.6`** *es parte de la biblioteca **X11**, que proporciona la funcionalidad gráfica básica en sistemas UNIX.*
  
- **Solución:**
- *El error se soluciona instalando **`libX11-6`**, que contiene la biblioteca `libX11.so.6`. El siguiente comando debería resolver el problema:*

  ```bash
  sudo apt-get install -y libx11-6
  ```

- **3. Comando: `sudo apt-get install -y libx11-6`**

- **¿Qué hace?**
- *Este comando instala el paquete **`libx11-6`**, que proporciona la biblioteca compartida **`libX11.so.6`** necesaria para que las aplicaciones gráficas basadas en X11 funcionen.*

- **¿Por qué es necesario?**
- *Como vimos en el error anterior, el contenedor no tiene esta biblioteca, lo que impide que el programa se ejecute correctamente. Al instalarla, proporcionas la biblioteca necesaria para la correcta ejecución del programa gráfico.*

```bash
sudo ./manager-linux-x64.run
```

```bash
sudo ./manager-linux-x64.run
couldn't load file "/tmp/tclQ7FSHd": libXext.so.6: cannot open shared object file: No such file or directory
```

- **Nuevo error: `couldn't load file "/tmp/tclQ7FSHd": libXext.so.6: cannot open shared object file: No such file or directory`**

- **¿Qué significa?**
- *Ahora el error ha cambiado. El programa aún no puede encontrar otra biblioteca importante: **`libXext.so.6`**. Esta biblioteca también pertenece a **X11** y es utilizada para funcionalidades adicionales, como la manipulación de ventanas y otras extensiones gráficas.*
- **Solución:**
- *Al igual que con el error anterior, la solución es instalar el paquete que contiene **`libXext.so.6`**. Para ello, necesitas instalar **`libxext6`:***

  ```bash
  sudo apt-get install libxext6 -y
  ```

- **5. Comando: `sudo apt-get install libxtst6 -y`**

- **¿Qué hace?**
- *Este comando instala el paquete **`libxtst6`**, que proporciona la biblioteca **`libXtst.so.6`**. Esta biblioteca es parte de la extensión **XTest**, que permite realizar pruebas de eventos de X (como el uso del mouse o teclado) y otras funciones similares.*

- **`libxtst6`** *puede ser necesaria si el programa que estás ejecutando depende de esas funciones.*

- ***Resumen de los errores y solución:***

1. **Error inicial (`libX11.so.6`):** *Necesitas instalar `libx11-6` para resolver este problema.*
2. **Error posterior (`libXext.so.6`):** *Debes instalar `libxext6` para solucionar este nuevo error relacionado con extensiones gráficas.*

```bash
sudo apt-get install libxext6 -y
sudo apt-get install -y libx11-6
```

- *Después de instalar las bibliotecas, vuelve a intentar ejecutar el fichero `manager-linux-x64.run`:*

   ```bash
   sudo ./manager-linux-x64.run
   ```

- **1. Comando con `docker container inspect`:**

```bash
curl http://"$(docker container inspect --format "{{.NetworkSettings.IPAddress}}" $(docker container list --all --filter status=running --filter network=bridge --filter publish=80 --filter expose=80 --quiet))"/dashboard/
```

- **Explicación:**

1. **`docker container inspect`:**
   - *Este comando se utiliza para obtener detalles de un contenedor Docker en particular.*
   - **`--format "{{.NetworkSettings.IPAddress}}"`:** *Aquí, le estás pidiendo al comando que te devuelva la dirección IP del contenedor en formato de texto. Esta es la IP interna que Docker asigna al contenedor dentro de su red `bridge`.*

2. **`docker container list --all --filter status=running --filter network=bridge --filter publish=80 --filter expose=80 --quiet`:**
   - **`docker container list`:** *Este comando lista los contenedores activos.*
   - **`--all`:** *Muestra todos los contenedores, incluso los detenidos.*
   - **`--filter status=running`:** *Filtra para mostrar solo los contenedores que están en ejecución.*
   - **`--filter network=bridge`:** *Filtra para mostrar contenedores conectados a la red `bridge`, que es la red predeterminada para contenedores Docker.*
   - **`--filter publish=80`:** *Filtra contenedores que tienen el puerto 80 expuesto al exterior.*
   - **`--filter expose=80`:** *Filtra contenedores que exponen el puerto 80 dentro del contenedor.*
   - **`--quiet`:** *Muestra solo los IDs de los contenedores sin detalles adicionales.*

3. **Resultado:**
   *Este comando construye dinámicamente la URL con la IP interna del contenedor que está ejecutando en la red `bridge` y accede al endpoint `/dashboard/`.*

4. **`curl`:**
   - *Finalmente, `curl` realiza una solicitud HTTP al endpoint `/dashboard/` del contenedor usando la IP interna que obtuvo previamente.*

- **Resumen de lo que hace:**
- *Este comando obtiene la IP de un contenedor que está en ejecución y que tiene el puerto 80 expuesto y accesible desde la red `bridge`. Luego, hace una solicitud `GET` al endpoint `/dashboard/` del contenedor, que podría ser la interfaz de administración o el dashboard de una aplicación web en ese contenedor.*

- **2. Comando con IP estática:**

```bash
curl http://172.17.0.2/dashboard/
```

- **Explicación:**
- **`curl`:** *Este comando simplemente realiza una solicitud HTTP a la URL `http://172.17.0.2/dashboard/`.*
- **`172.17.0.2`:** *Aquí estás usando una IP específica (`172.17.0.2`), que probablemente sea la IP interna de un contenedor Docker en la red `bridge` de tu máquina.*
  
- *Si la IP de tu contenedor es `172.17.0.2` y tienes un servicio web corriendo en el puerto 80 del contenedor, este comando debería devolver la respuesta de ese servicio, como el contenido del dashboard de la aplicación web.*

- **Resumen:**
*Este comando es más directo, ya que estás especificando la IP del contenedor de manera explícita, mientras que el primer comando lo hace dinámicamente usando `docker inspect`.*

- **Resumen general:**
- *El primer comando es útil si no sabes de antemano cuál es la IP del contenedor, ya que lo obtiene dinámicamente usando la inspección de Docker.*
- *El segundo comando asume que conoces la IP del contenedor (en este caso, `172.17.0.2`) y hace la solicitud directamente.*

- *Ambos comandos están tratando de acceder al mismo recurso (`/dashboard/`), pero el primero obtiene la IP automáticamente, lo que es más flexible y útil si no sabes la IP del contenedor.*

---

### ***Explicación del proceso***

> [!NOTE]
> *La instalación de XAMPP en Linux crea un directorio base en `/opt/lampp` que contiene todo lo necesario para ejecutar un servidor web, incluyendo Apache, MySQL, PHP y herramientas adicionales. Este directorio está estructurado de la siguiente manera:*

#### ***Estructura de `/opt/lampp`***

- **`apache2`:** *Ficheros de configuración y binarios del servidor Apache.*
- **`bin`:** *Binarios ejecutables necesarios para el funcionamiento del entorno LAMPP.*
- **`htdocs`:** *Directorio raíz donde se colocan los ficheros de los sitios web.*
- **`mysql`:** *Ficheros relacionados con la base de datos MySQL/MariaDB.*
- **`php`:** *Ficheros binarios y de configuración de PHP.*
- **`phpmyadmin`:** *Herramienta para administrar bases de datos MySQL/MariaDB desde la web.*
- **`logs`:** *Ficheros de registro de Apache y otros servicios.*
- **`ctlscript.sh`:** *Script para iniciar, detener y reiniciar los servicios de XAMPP.*

### ***Creación del directorio `contacts-app`***

1. **Directorio del proyecto:**
   - **Creamos un nuevo directorio llamado `contacts-app` dentro de `htdocs`, que será el directorio raíz del proyecto web.**

   ```bash
   sudo mkdir -p /opt/lampp/htdocs/contacts-app
   ```

2. **Permisos:**
   - **Cambiamos la propiedad del directorio al usuario actual para facilitar el trabajo con él sin permisos de root.**

   ```bash
   sudo chown -R $USER:$USER /opt/lampp/htdocs/contacts-app
   ```

3. **Enlace simbólico:**
   - **Creamos un enlace simbólico en `/App` que apunta al directorio del proyecto en `htdocs`.**

   ```bash
   ln -sf /opt/lampp/htdocs/contacts-app /App/contacts-app
   ```

- *Otra opción sería crear un directorio para la aplicación de contactos, utilizando el comando `mkdir -p /App/contacts-app`, el cual garantiza que la estructura de directorios necesaria se cree sin generar errores si el directorio ya existe. Luego, se crea un enlace simbólico con el comando `sudo ln -sf /App/contacts-app/ /opt/lampp/htdocs/contacts-app`. Esto hace que el directorio `/App/contacts-app/` se enlace simbólicamente a `/opt/lampp/htdocs/contacts-app`, lo que facilita el acceso y la ejecución de la aplicación en el entorno de servidor de XAMPP (que se encuentra en `/opt/lampp/htdocs`), sin necesidad de mover los ficheros de la aplicación.*

```bash
mkdir -p /App/contacts-app
sudo ln -sf /App/contacts-app/ /opt/lampp/htdocs/contacts-app
```

- **`mkdir -p`:** *Crea el directorio `/App/contacts-app` si no existe. La opción `-p` asegura que se creen los directorios intermedios necesarios.*
- **`sudo ln -sf`:** *Crea un enlace simbólico, donde `-s` indica un enlace simbólico y `-f` sobrescribe cualquier enlace existente.*

- *Este enfoque es útil cuando se desean mantener los ficheros de la aplicación en una ubicación separada, pero al mismo tiempo hacer que estén disponibles desde el directorio donde el servidor web espera encontrar los ficheros.*

1. **Fichero HTML básico:**
   - **Creamos un fichero `index.html` en el directorio del proyecto:**

   ```bash
   touch /App/contacts-app/index.html
   ```

   - **Luego, escribimos un HTML básico en este fichero:**

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Document</title>
   </head>
   <body>
       <h1>Title</h1>
   </body>
   </html>
   ```

### ***Prueba del servidor***

1. **Iniciar XAMPP:**
   - **Si XAMPP no está ejecutándose, puedes iniciarlo con:**

   ```bash
   sudo /opt/lampp/lampp start
   ```

   ```bash
   Starting XAMPP for Linux 8.2.12-0...
   XAMPP: Starting Apache...already running.
   XAMPP: Starting MySQL...ok.
   XAMPP: Starting ProFTPD...ok.
   ```

2. **Acceder al fichero desde el navegador:**
   - *La dirección para acceder sería algo como:*

   ```bash
   http://localhost/contacts-app/index.html
   ```

3. **Verificar con `curl`:**
   - *Para verificar el contenido del fichero desde la línea de comandos:*

   ```bash
   curl http://localhost/contacts-app/index.html
   ```

   - **La salida será el contenido del fichero HTML básico:**

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Document</title>
   </head>
   <body>
       <h1>Title</h1>
   </body>
   </html>
   ```

### ***Notas importantes***

- **Permisos de ficheros y directorios:** *Asegúrate de que los ficheros y directorios dentro de `htdocs` sean legibles por el servidor Apache.*
- **IP del servidor:** *Si accedes desde otra máquina en la red, usa la IP del servidor donde XAMPP está ejecutándose.*
- **Firewall:** *Asegúrate de que el puerto 80 (o 443 para HTTPS) esté abierto si accedes desde otra máquina.*

```bash
cd  /opt/
```

```bash
ls -l
```

- **Salida**

```bash
total 4
drwxr-xr-x 31 root root 4096 Dec 11 18:55 lampp
```

```bash
cd lampp/
```

```bash
ls -lA
```

- **Salida**

```bash
total 10788
-rw-r--r--  1 root   root     19518 Oct 30  2023 README-wsrep
-rw-r--r--  1 root   root      2874 Oct 30  2023 README.md
-rwxr-xr-x  1 root   root       957 Nov 25  2023 RELEASENOTES
-rw-r--r--  1 root   root     86263 Oct 30  2023 THIRDPARTY
drwxr-xr-x  5 root   root      4096 Dec 11 18:47 apache2
drwxrwxr-x  2 root   root     12288 Dec 11 18:48 bin
drwxr-xr-x  2 root   root      4096 Dec 11 18:51 build
drwxr-xr-x  2 root   root      4096 Dec 11 18:47 cgi-bin
-rwxr-xr-x  1 root   root     25750 Dec 11 18:47 ctlscript.sh
drwxr-xr-x  2 root   root      4096 Dec 11 18:51 docs
drwxrwxr-x  3 root   root      4096 Dec 11 18:48 error
drwxr-xr-x  8 root   root      4096 Dec 11 18:48 etc
drwxr-xr-x  5 root   root      4096 Dec 11 18:48 htdocs
drwxr-xr-x  3 root   root      4096 Dec 11 18:48 icons
drwxr-xr-x  2 root   root      4096 Dec 11 18:47 img
drwxr-xr-x 22 root   root     12288 Dec 11 18:51 include
drwxr-xr-x  2 root   root      4096 Dec 11 18:51 info
lrwxrwxrwx  1 root   root        16 Dec 11 18:51 lampp -> /opt/lampp/xampp
drwxr-xr-x 15 root   root     12288 Dec 11 18:55 lib
drwxr-xr-x  2 root   root      4096 Dec 11 18:47 lib64
drwxr-xr-x  2 root   root      4096 Dec 11 18:47 libexec
drwxr-xr-x  2 root   root      4096 Dec 11 18:48 licenses
drwxr-xr-x  2 daemon daemon    4096 Dec 11 18:55 logs
drwxr-xr-x  7 root   root      4096 Dec 11 18:51 man
-rwx------  1 root   root   3361003 Jun 15  2022 manager-linux-x64.run
drwxr-xr-x 14 root   root     12288 Dec 11 18:51 manual
drwxr-xr-x  2 root   root      4096 Dec 11 18:51 modules
drwxr-xr-x  3 root   root      4096 Dec 11 18:47 mysql
drwxr-xr-x  2 root   root      4096 Dec 11 18:47 pear
drwxr-xr-x  3 root   root      4096 Dec 11 18:47 php
drwxr-xr-x 13 root   root      4096 Dec 11 18:55 phpmyadmin
drwxr-xr-x  3 root   root      4096 Dec 11 18:47 proftpd
-rw-r--r--  1 root   root       905 Dec 11 18:55 properties.ini
drwxr-xr-x  2 root   root      4096 Dec 11 18:48 sbin
drwxr-xr-x 50 root   root      4096 Dec 11 18:51 share
drwxrwxrwx  2 daemon daemon    4096 Dec 11 18:47 temp
-rwx------  1 root   root   6893594 Dec 11 18:55 uninstall
-rw-------  1 root   root    466714 Dec 11 18:55 uninstall.dat
drwxr-xr-x  7 root   root      4096 Dec 11 18:47 var
-rwxr-xr-x  1 root   root     15201 Jul 22  2013 xampp
```

```bash
ls -ld htdocs/
```

- **Salida**

```bash
drwxr-xr-x 5 root root 4096 Dec 11 18:48 htdocs/
```

```bash
cd htdocs/
```

```bash
ls -lA
```

- **Salida**

```bash
total 56
-rw-r--r--  1 root   root    3607 Jun 15  2022 applications.html
-rw-r--r--  1 root   root     177 Jun 15  2022 bitnami.css
drwxr-xr-x 20 root   root    4096 Dec 11 18:48 dashboard
-rw-r--r--  1 root   root   30894 May 11  2007 favicon.ico
drwxr-xr-x  2 root   root    4096 Dec 11 18:48 img
-rw-r--r--  1 root   root     260 Jul  9  2015 home.php
drwxr-xr-x  2 daemon daemon  4096 Dec 11 18:47 webalizer
```

```bash
sudo mkdir -p contacts-app
```

```bash
cd ..
```

```bash
ls -ld .
```

- **Salida**

```bash
drwxr-xr-x 2 root root 4096 Dec 11 21:31 contacts-app/
```

```bash
sudo chown -R $USER:$USER contacts-app/
```

```bash
ln -sf /opt/lampp/htdocs/contacts-app /App/contacts-app
touch /App/contacts-app/index.html
```

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport"
        content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <h1>
        Title
    </h1>
</body>

</html>
```

```bash
curl http://172.17.0.2/contacts-app/index.html
```

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport"
        content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <h1>
        Title
    </h1>
</body>
```

para evitar hacer esto
vscode ➜ /opt/lampp/bin $ /opt/lampp/bin/php --version
PHP 8.2.12 (cli) (built: Nov 25 2023 08:09:53) (NTS)
Copyright (c) The PHP Group
Zend Engine v4.2.12, Copyright (c) Zend Technologies
vscode ➜ /opt/lampp/bin $ /opt/lampp/bin/mysql --version
/opt/lampp/bin/mysql  Ver 15.1 Distrib 10.4.32-MariaDB, for Linux (x86_64) using readline 5.1

Si estas en contenedor
echo 'export PATH="$PATH:/opt/lampp/bin"' >> ~/.bashrc
echo 'alias lampp="/opt/lampp/lampp"' >> ~/.bashrc

sudo su root

echo 'export PATH="$PATH:/opt/lampp/bin"' >> /root/.bashrc
echo 'alias lampp="/opt/lampp/lampp"' >> /root/.bashrc

si estas en el host
echo 'export PATH="$PATH:/opt/lampp/bin"' >> ~/.profile

docker container restart container-web
docker container exec --interactive --tty --user vscode --privileged container-web /bin/bash

```bash
/opt/lampp/lampp --help
Usage: lampp <action>

        start         Start XAMPP (Apache, MySQL and eventually others)
        startapache   Start only Apache
        startmysql    Start only MySQL
        startftp      Start only ProFTPD

        stop          Stop XAMPP (Apache, MySQL and eventually others)
        stopapache    Stop only Apache
        stopmysql     Stop only MySQL
        stopftp       Stop only ProFTPD

        reload        Reload XAMPP (Apache, MySQL and eventually others)
        reloadapache  Reload only Apache
        reloadmysql   Reload only MySQL
        reloadftp     Reload only ProFTPD

        restart       Stop and start XAMPP
        security      Check XAMPP's security

        enablessl     Enable SSL support for Apache
        disablessl    Disable SSL support for Apache

        backup        Make backup file of your XAMPP config, log and data files

        oci8          Enable the oci8 extenssion

        panel         Starts graphical XAMPP control panel
```
