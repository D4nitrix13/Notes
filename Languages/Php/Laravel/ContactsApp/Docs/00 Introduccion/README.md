<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Apuntes sobre Instalación y Configuración de Laravel en Docker**

## **Recursos Recomendados**

- *[Instalar Composer en Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-composer-on-ubuntu-20-04-es "https://www.digitalocean.com/community/tutorials/how-to-install-and-use-composer-on-ubuntu-20-04-es")*
- *[Instalar Node.js en Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04 "https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04")*
- *[Versiones Anteriores de Node.js](https://nodejs.org/en/about/previous-releases "https://nodejs.org/en/about/previous-releases")*
- *[Migrating From Laravel Mix To Vite](https://github.com/laravel/vite-plugin/blob/main/UPGRADE.md "https://github.com/laravel/vite-plugin/blob/main/UPGRADE.md")*

---

## **Creación del Contenedor Docker**

```bash
docker container run \
  --attach STDOUT \
  --attach STDIN \
  --attach STDERR \
  --interactive \
  --publish 8000:8000 \
  --expose 8000 \
  --tty \
  --workdir /App \
  --label Framework=Laravel \
  --user root \
  --privileged \
  --network bridge \
  --dns 8.8.8.8 \
  --mount type=bind,source="$(pwd)",target=/App,readonly=false \
  --stop-timeout 10 \
  --stop-signal SIGTERM \
  --init \
  --restart unless-stopped \
  --name laravel-guide \
  php:8.3.0 /bin/bash -pli
```

- **Explicacion**
  - **`docker container run`:** *El Comando Docker Run Ejecuta Un Comando En Un Nuevo Contenedor, Extrayendo La Imagen Si Es Necesario E Iniciando El Contenedor.*
  - **`--attach STDOUT`:** *Conecta La Salida Estándar Del Contenedor Con La Terminal*
  - **`--attach STDIN`:** *Conecta La Entrada Estándar Del Contenedor Con La Terminal*
  - **`--attach STDERR`:** *Conecta La Salida De Errores Del Contenedor Con La Terminal*
    - **`--interactive`:** *Permite La Interacción Con El Contenedor*
    - **`--publish 8000:8000`:** *Mapea El Puerto 8000 Del Host Al Puerto 8000 Del Contenedor*
    - **`--expose 8000`:** *Expone El Puerto 8000 Dentro Del Contenedor*
    - **`--tty`:** *Asigna Una Terminal Pseudo-Tty*
    - **`--workdir /App`:** *Establece El Directorio De Trabajo En /App Dentro Del Contenedor*
    - **`--label Framework=Laravel`:** *Etiqueta El Contenedor Con "Framework=Laravel"*
    - **`--user root`:** *Ejecuta El Contenedor Como El Usuario Root*
    - **`--privileged`:** *Otorga Privilegios Extendidos Al Contenedor*
    - **`--network bridge`:** *Usa La Red Bridge De Docker*
    - **`--dns 8.8.8.8`:** *Usa El Servidor Dns De Google (8.8.8.8)*
    - **`--mount type=bind,source="$(pwd)",target=/App,readonly=false`:** *Monteo De Un Volumen*
    - **`--stop-timeout 10`:** *Define 10 Segundos De Espera Antes De Forzar La Detención Del Contenedor*
    - **`--stop-signal SIGTERM`:** *Define Sigterm Como La Señal Para Detener El Contenedor*
    - **`--init`:** *Usa Un Proceso Init Para Manejar Señales Y Procesos Huérfanos*
    - **`--restart unless-stopped`:** *Reinicia El Contenedor A Menos Que Se Haya Detenido Manualmente*
    - **`--name laravel-guide`:** *Asigna El Nombre "Laravel-Guide" Al Contenedor*
    - **`php:8.3.0 /bin/bash`:** *Usa La Imagen Php:8.3.0 E Inicia Un Shell Interactivo*

### **Forma Abreviada del Comando**

```bash
docker run -aSTDOUT -aSTDIN -aSTDERR -itp8000:8000 -w/App \
  -lFramework=Laravel --expose 8000 -u0 --privileged \
  --network bridge --dns 8.8.8.8 \
  --mount type=bind,source="$(pwd)",target=/App,readonly=false \
  --stop-timeout 10 --stop-signal SIGTERM --init --restart unless-stopped \
  --name laravel-guide php:8.3.0 /bin/bash -pli
```

---

## **Instalación de Dependencias**

### **Instalación de Herramientas de Desarrollo**

```bash
cd $(mktemp -d)
curl -sSLO https://github.com/sharkdp/bat/releases/latest/download/bat_0.25.0_amd64.deb
dpkg -i bat_0.25.0_amd64.deb
curl -sSLO https://github.com/lsd-rs/lsd/releases/download/v1.1.5/lsd_1.1.5_amd64_xz.deb
dpkg --install lsd_1.1.5_amd64_xz.deb
```

```bash
cd $(mktemp -d)
```

- **`mktemp -d`:** *El comando `mktemp` crea un directorio temporal. La opción `-d` indica que se debe crear un directorio y no un archivo. Este directorio tiene un nombre aleatorio único, generado por el sistema.*
- **`cd $(mktemp -d)`:** *Aquí, se usa `$(mktemp -d)` para obtener el nombre del directorio temporal recién creado, y luego `cd` cambia al directorio de trabajo actual a ese nuevo directorio.*

*El propósito de este comando es crear un entorno limpio y aislado donde se puedan descargar y manipular los archivos sin afectar el sistema de archivos global.*

```bash
curl -sSLO https://github.com/sharkdp/bat/releases/latest/download/bat_0.25.0_amd64.deb
```

- **`curl`:** *`curl` es una herramienta de línea de comandos para transferir datos desde o hacia un servidor utilizando distintos protocolos (en este caso, HTTP/HTTPS).*
- **`-sS`:** *La opción `-s` hace que `curl` opere en "modo silencioso", es decir, no mostrará ninguna información de progreso ni errores. La opción `-S` se usa para mostrar los errores si ocurren, incluso cuando el modo silencioso está habilitado. Es útil para asegurarse de que, si hay un error, se pueda detectar.*
- **`-L`:** *Esta opción le dice a `curl` que siga las redirecciones. Si la URL solicitada redirige a otra, `curl` continuará con la nueva URL automáticamente.*
- **`-O`:** *La opción `-O` le indica a `curl` que guarde el archivo con el nombre que tiene en la URL, es decir, `bat_0.25.0_amd64.deb`. Sin esta opción, `curl` guardaría el archivo con un nombre genérico (como `index.html`).*
- **`https://github.com/sharkdp/bat/releases/latest/download/bat_0.25.0_amd64.deb`:** *Esta es la URL de la última versión de la herramienta `bat` para sistemas basados en arquitectura `amd64`. El archivo descargado será un paquete de instalación `.deb` para sistemas basados en Debian.*

*Este comando descarga el archivo `.deb` para la instalación de `bat`.*

```bash
dpkg -i bat_0.25.0_amd64.deb
```

- **`dpkg`:** *`dpkg` es el sistema de gestión de paquetes de bajo nivel para distribuciones basadas en Debian (como Ubuntu). Es utilizado para instalar, eliminar o proporcionar información sobre paquetes `.deb`.*
- **`-i`:** *La opción `-i` le indica a `dpkg` que debe instalar el paquete especificado, que en este caso es `bat_0.25.0_amd64.deb`. Esta opción requiere que el archivo `.deb` ya esté presente en el sistema, y lo instala.*

*Este comando instala la herramienta `bat` (un reemplazo avanzado de `cat`) en el sistema.*

```bash
curl -sSLO https://github.com/lsd-rs/lsd/releases/download/v1.1.5/lsd_1.1.5_amd64_xz.deb
```

*Este comando sigue el mismo patrón que el anterior, pero ahora descarga el paquete `lsd`:*

- **`https://github.com/lsd-rs/lsd/releases/download/v1.1.5/lsd_1.1.5_amd64_xz.deb`:** *Esta URL apunta a la descarga de la versión `1.1.5` de `lsd` (un reemplazo avanzado para el comando `ls`) para sistemas de 64 bits (`amd64`). El archivo es un paquete `.deb` comprimido con `xz`.*

*Este comando descarga el archivo `.deb` para la instalación de `lsd`.*

```bash
dpkg --install lsd_1.1.5_amd64_xz.deb
```

- **`--install`:** *En lugar de la opción `-i`, aquí se utiliza `--install`, que es una forma más explícita de especificar que el paquete debe ser instalado. El resultado es el mismo que usar `-i`, pero es más legible.*

*Este comando instala la herramienta `lsd` en el sistema.*

---

### **Resumen**

**El script realiza las siguientes acciones:**

1. **Crea un directorio temporal** *donde se llevarán a cabo las descargas e instalaciones.*
2. **Descarga el paquete `.deb`** *de la herramienta `bat` desde GitHub y lo instala usando `dpkg`.*
3. **Descarga el paquete `.deb`** *de la herramienta `lsd` desde GitHub y lo instala también usando `dpkg`.*

*Este procedimiento es útil cuando se desea instalar software sin necesidad de usar un repositorio o sin afectar la configuración global del sistema. Todo se realiza en un directorio temporal, lo que mantiene el proceso aislado.*

### **Instalación de Dependencias Necesarias**

```bash
cd $(mktemp -d) && \
apt update && \
curl -sSLO https://github.com/git/git/archive/refs/tags/v2.49.0-rc0.tar.gz && \
tar -xvf v2.49.0-rc0.tar.gz && \
cd "$(pwd)/git-2.49.0-rc0" && \
apt install -y libcurl4-openssl-dev libssl-dev zlib1g-dev libexpat1-dev tcl8.6 tk8.6 gettext && \
make prefix=/usr/local all && \
mv git /usr/local/bin/
```

```bash
apt update && \
apt install -y git unzip && \
curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
curl -sL https://deb.nodesource.com/setup_22.x | bash && apt-get install -y nodejs
```

**Explicación de los Comandos:**

- **`apt update`:** *Actualiza la lista de paquetes disponibles.*
- **`apt install -y unzip`:** *Instala Unzip sin pedir confirmación.*
- **`curl -sS https://getcomposer.org/installer | php`:** *Descarga e instala Composer.*
- **`--install-dir=/usr/local/bin --filename=composer`:** *Instala Composer en `/usr/local/bin` con el nombre `composer`.*
- **`curl -sL https://deb.nodesource.com/setup_22.x | bash`:** *Configura el repositorio de Node.js v22.*
- **`apt-get install -y nodejs`:** *Instala Node.js.*

- **Salida Comando: `curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer`**

```bash
All settings correct for using Composer
Downloading...

Composer (version 2.8.6) successfully installed to: /usr/local/bin/composer
Use it: php /usr/local/bin/composer
```

- **Salida Comando: `curl -sL https://deb.nodesource.com/setup_22.x | bash`**

```bash
2025-02-27 00:51:30 - Installing pre-requisites
2025-02-27 00:51:45 - Repository configured successfully.
2025-02-27 00:51:45 - To install Node.js, run: apt-get install nodejs -y
2025-02-27 00:51:45 - You can use N|solid Runtime as a node.js alternative
2025-02-27 00:51:45 - To install N|solid Runtime, run: apt-get install nsolid -y
```

---

## **Configuración del Proyecto Laravel**

### **Inicializar un Repositorio Git**

```bash
git init "$(pwd)" --initial-branch=master
```

- **`git init`:** *Inicializa un nuevo repositorio Git en el directorio actual.*
- **`--initial-branch=master`:** *Especifica que el branch inicial sea `master`.*

### **Creación de un Usuario para Laravel**

```bash
useradd -ms /bin/bash d4nitrix13
chown -R d4nitrix13:d4nitrix13 .
```

- **`useradd -ms /bin/bash d4nitrix13`:** *Crea un usuario llamado `d4nitrix13` con un shell de bash.*
- **`chown -R d4nitrix13:d4nitrix13 .`:** *Cambia el propietario del directorio actual y su contenido a `d4nitrix13`.*

### **Crear un Proyecto Laravel**

```bash
composer create-project laravel/laravel=9.1.10 ApplicationLaravel
```

- **`composer create-project`:** *Crea un nuevo proyecto en base a un paquete de Composer.*
- **`laravel/laravel=9.1.10`:** *Especifica que se instale la versión `9.1.10` de Laravel.*
- **`Application`:** *Nombre del directorio donde se instalará Laravel.*

---

## **Uso de Artisan**

### **Ver Comandos Disponibles**

```bash
php artisan
```

*Muestra una lista de comandos de `artisan`, la interfaz de línea de comandos de Laravel.*

### **Levantar el Servidor de Desarrollo**

```bash
php artisan serve --host=0.0.0.0 --port 8000 --ansi -vvv --tries 10
```

- **`serve`:** *Inicia el servidor embebido de Laravel.*
- **`--host=0.0.0.0`:** *Permite que el servidor escuche en todas las interfaces de red.*
- **`--port 8000`:** *Define el puerto en el que el servidor se ejecuta (8000).*
- **`--ansi`:** *Forza la salida ANSI (colores en la terminal).*
- **`-vvv`:** *Modo de depuración muy detallado.*
- **`--tries 10`:** *Intenta levantar el servidor hasta 10 veces en caso de fallo.*

---

## **Notas Importantes sobre `Laravel 9.1.10 y Vite`**

*En versiones posteriores a Laravel `9.1.10`, Webpack dejó de ser el module bundler predeterminado, siendo reemplazado por **Vite**. Esta guía se basa en Laravel 9.1.10, que aún utilizaba Webpack. En futuras actualizaciones, se incluirá información sobre la configuración de Vite en Laravel.*

> [!NOTE]
> *Un **module bundler** (empaquetador de módulos) es una herramienta que toma múltiples archivos JavaScript, junto con sus dependencias, y los combina en uno o más archivos optimizados para su uso en un navegador o entorno de ejecución.*

### **¿Por qué se usa un module bundler?**

*Los proyectos modernos de JavaScript suelen dividir su código en múltiples archivos y módulos para mejorar la organización y reutilización del código. Sin embargo, los navegadores no siempre pueden gestionar bien este enfoque directamente. Un module bundler resuelve esto al:*

- **Combinar archivos** *en un único paquete para reducir las solicitudes HTTP.*
- **Optimizar el código** *eliminando partes innecesarias y aplicando minificación.*
- **Manejar dependencias** *automáticamente, asegurando que los módulos se carguen en el orden correcto.*
- **Permitir el uso de tecnologías modernas** *como ES6 Modules (`import/export`), TypeScript o preprocessors de CSS.*

### **Ejemplos de module bundlers:**

- **Webpack** *(usado en Laravel 9.1.10 y versiones anteriores)*
- **Vite** *(reemplazó Webpack en Laravel 9.2+)*

### **Diferencia entre Webpack y Vite**

- **Webpack** *usa un enfoque de **compilación previa** (pre-bundling), generando un paquete antes de la ejecución.*
- **Vite** *usa un servidor de desarrollo basado en **ES Modules**, lo que hace que la carga en desarrollo sea más rápida y eficiente.*

*Si estás trabajando con Laravel 9.1.10, usarás Webpack, pero en versiones más recientes, necesitarás aprender a configurar Vite.*
