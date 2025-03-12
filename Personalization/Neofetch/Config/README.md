<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***Descripción del Fichero de Configuración***

- *Ubicacion del fichero (`~/.config/neofetch/config.conf`) contiene la configuración personalizada para Neofetch. Neofetch es una herramienta que muestra información del sistema de manera visualmente atractiva en la terminal. En este fichero, puedes ajustar opciones como la información que se muestra, el estilo del texto, los colores, y otros parámetros de visualización según tus preferencias.*

- **Íconos Utilizados:**

*Los siguientes íconos se utilizan en la configuración. Para ver una hoja de trucos completa de los íconos de Nerd Fonts, visita [Nerd Fonts Cheat Sheet](https://www.nerdfonts.com/cheat-sheet "https://www.nerdfonts.com/cheat-sheet").*

- **Nombre del Ícono:** *`nf-dev-ubuntu`*  
  **Ícono:** **

- **Nombre del Ícono:** *`nf-fa-memory`*  
  **Ícono:** **

- **Nombre del Ícono:** *`nf-md-cpu_64_bit`*  
  **Ícono:** *󰻠*

- **Nombre del Ícono:** *`nf-oct-cpu`*  
  **Ícono:** **

- **Nombre del Ícono:** *`nf-seti-config`*  
  **Ícono:** **

- **Nombre del Ícono:** *`nf-md-monitor`*  
  **Ícono:** *󰍹*

- **Nombre del Ícono:** *`nf-dev-linux`*  
  **Ícono:** **

- **Nombre del Ícono:** *`nf-fa-desktop`*  
  **Ícono:** **

- **Nombre del Ícono:** *`nf-md-arch`*  
  **Ícono:** *󰣇*

## ***Información General***

```bash
# See this wiki page for more info:
# https://github.com/dylanaraps/neofetch/wiki/Customizing-Info

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me
```

**Estas líneas son comentarios que proporcionan información adicional sobre el script, incluyendo un enlace a la wiki para más detalles, así como información de contacto del autor.**

### ***Función `print_info()`***

```bash
print_info() {
```

**Esta línea define una función llamada `print_info` que se encarga de imprimir la información personalizada del sistema.**

#### ***Determinación del Símbolo del Sistema***

```bash
  # Leer la primera palabra del fichero /var/log/installer/media-info
  dist=$(awk '{print $1}' /var/log/installer/media-info | tr '[:upper:]' '[:lower:]')

  # Determinar el símbolo basado en el valor
  case "$dist" in
  ubuntu | xubuntu | lubuntu)
    symbol=""
    ;;
  arch)
    symbol="󰣇"
    ;;
  parrot)
    symbol=""
    ;;
  *)
    symbol=""
    ;;
  esac
```

- *`dist=$(awk '{print $1}' /var/log/installer/media-info | tr '[:upper:]' '[:lower:]')`: Lee la primera palabra del fichero `/var/log/installer/media-info`, la convierte a minúsculas y la asigna a la variable `dist`. Este fichero generalmente contiene información sobre la distribución del sistema.*
- *`case "$dist"`: Dependiendo del valor de `dist`, asigna un símbolo específico a la variable `symbol`. Esto permite personalizar los iconos según la distribución del sistema operativo:*
  - *`ubuntu`, `xubuntu`, `lubuntu` → símbolo para distribuciones basadas en Ubuntu.*
  - *`arch` → símbolo para Arch Linux.*
  - *`parrot` → símbolo para Parrot OS.*
  - *`*` → símbolo vacío para otras distribuciones.*

#### ***Impresión de Información***

```bash
  prin "​ ​​ $(color 6) Using $symbol for my OS ​​ ​"
  prin "$(color 8)┌────────────────────────────────────────────────────┐"

  info "​ ​ ​​$(color 1) $symbol OS          " distro
  #    info "​ ​​ ​$(color 1)  Host        " model
  info "​ ​​ ​$(color 1)  Kernel      " kernel
  #    info "​ ​​ ​$(color 1)  Uptime      " uptime
  info "​ ​​ ​$(color 2)  Packages    " packages
  #    info "​ ​​ ​$(color 2)  Shell       " shell
  info "​ ​​ ​$(color 2) 󰍹 Resolution  " resolution
  info "​ ​​ ​$(color 3)  de          " de
  #    info "​ ​​ ​$(color 3) 缾WM          " wm
  #    info "​ ​​ ​$(color 12)  WM Theme    " wm_theme
  #    info "$(color 13)  Theme       " theme
  #    info "$(color 14)  Icons       " icons
  info "​ ​​ ​$(color 3)  Terminal    " term
  #    info " Font        " font
  #    info " Terminal Font   " term_font

  prin "$(color 8)└────────────────────────────────────────────────────┘"
  prin " "
  info "​ ​​ ​​​ $(color 6) " title
  prin "$(color 8)┌────────────────────────────────────────────────────┐"

  info "​ ​​ ​$(color 12) 󰻠 CPU         " cpu
  info "​ ​​ ​$(color 12)  GPU         " gpu
  info "​ ​​ ​$(color 13)  GPU Driver  " gpu_driver # Linux/macOS only
  info "​ ​​ ​$(color 13)  Memory      " memory

  # info "CPU Usage" cpu_usage
  # info "Disk" disk
  # info "Battery" battery
  # info "Song" song
  # [[ "$player" ]] && prin "Music Player" "$player"
  # info "Local IP" local_ip
  # info "Public IP" public_ip
  # info "Users" users
  # info "Locale" locale  # This only works on glibc systems.

  prin "$(color 8)└────────────────────────────────────────────────────┘"
  prin " "
  prin "​ ​​ ​​ ​​$(color 1)​ ​​ ​​$(color 2)​ ​​ ​​$(color 3)​ ​​ ​​$(color 4)​ ​​ ​​$(color 5)​ ​​ ​​$(color 6)​ ​​ ​​$(color 7)​ ​​ ​​$(color 8)​ ​​ ​​$(color 16)"
```

- *`prin` y `info`: Estas funciones son responsables de imprimir información con formato y color. `prin` probablemente se usa para imprimir líneas y separadores, mientras que `info` muestra información específica del sistema.*
- *`$(color X)`: Cambia el color del texto usando códigos de color. Los colores se definen previamente en el script.*
- *Se imprimen varias secciones con información del sistema:*
  - ***Distribución** (`distro`), **Kernel** (`kernel`), **Paquetes** (`packages`), **Resolución** (`resolution`), **Entorno de escritorio** (`de`), **Terminal** (`term`), etc.*
- *Comentarios (`#`) indican líneas opcionales que están comentadas. Puedes descomentarlas para mostrar más información, como el modelo del host, el tiempo de actividad, el shell, el tema del gestor de ventanas, etc.*
- *La última parte de la función imprime una fila de íconos de color para agregar un toque visual.*

### ***Título***

```bash
# Title

# Hide/Show Fully qualified domain name.
#
# Default:  'off'
# Values:   'on', 'off'
# Flag:     --title_fqdn
title_fqdn="off"
```

- **`title_fqdn`:** *Controla si se muestra o no el nombre de dominio completo (FQDN) del sistema.*
  - **`on`:** *Muestra el FQDN.*
  - **`off`:** *Muestra solo el nombre del host.*
  - **Valor por defecto:** *`off`.*

### ***Kernel***

```bash
# Kernel

# Shorten the output of the kernel function.
#
# Default:  'on'
# Values:   'on', 'off'
# Flag:     --kernel_shorthand
# Supports: Everything except *BSDs (except PacBSD and PC-BSD)
#
# Example:
# on:  '4.8.9-1-ARCH'
# off: 'Linux 4.8.9-1-ARCH'
kernel_shorthand="on"
```

- **`kernel_shorthand`:** *Ajusta la forma en que se muestra la información del kernel.*
  - **`on`:** *Muestra solo la versión del kernel (p. ej., `4.8.9-1-ARCH`).*
  - **`off`:** *Muestra el prefijo "Linux" antes de la versión del kernel (p. ej., `Linux 4.8.9-1-ARCH`).*
  - **Valor por defecto:** *`on`.*

### ***Distribución***

```bash
# Distro

# Shorten the output of the distro function
#
# Default:  'off'
# Values:   'on', 'tiny', 'off'
# Flag:     --distro_shorthand
# Supports: Everything except Windows and Haiku
distro_shorthand="off"
```

- **`distro_shorthand`:** *Controla el formato de la salida para la información de la distribución.*
  - **`on`:** *Muestra la distribución en un formato más corto.*
  - **`tiny`:** *Muestra una versión aún más corta.*
  - **`off`:** *Muestra el nombre completo de la distribución.*
  - **Valor por defecto:** *`off`.*

### ***Arquitectura del Sistema Operativo***

```bash
# Show/Hide OS Architecture.
# Show 'x86_64', 'x86' and etc in 'Distro:' output.
#
# Default: 'on'
# Values:  'on', 'off'
# Flag:    --os_arch
#
# Example:
# on:  'Arch Linux x86_64'
# off: 'Arch Linux'
os_arch="on"
```

- **`os_arch`:** *Controla si se muestra la arquitectura del sistema operativo en la salida.*
  - **`on`:** *Muestra la arquitectura (p. ej., `x86_64`).*
  - **`off`:** *Solo muestra el nombre de la distribución sin la arquitectura (p. ej., `Arch Linux`).*
  - **Valor por defecto:** *`on`.*

### ***Tiempo de Actividad***

```bash
# Uptime

# Shorten the output of the uptime function
#
# Default: 'on'
# Values:  'on', 'tiny', 'off'
# Flag:    --uptime_shorthand
#
# Example:
# on:   '2 days, 10 hours, 3 mins'
# tiny: '2d 10h 3m'
# off:  '2 days, 10 hours, 3 minutes'
uptime_shorthand="off"
```

- **`uptime_shorthand`:** *Ajusta la forma en que se muestra la duración de actividad.*
  - **`on`:** *Muestra la duración en un formato más largo (p. ej., `2 days, 10 hours, 3 mins`).*
  - **`tiny`:** *Muestra una versión compacta (p. ej., `2d 10h 3m`).*
  - **`off`:** *Muestra la duración completa (p. ej., `2 days, 10 hours, 3 minutes`).*
  - **Valor por defecto:** *`on`.*

### ***Memoria***

```bash
# Memory

# Show memory pecentage in output.
#
# Default: 'off'
# Values:  'on', 'off'
# Flag:    --memory_percent
#
# Example:
# on:   '1801MiB / 7881MiB (22%)'
# off:  '1801MiB / 7881MiB'
memory_percent="on"
```

- **`memory_percent`:** *Controla si se muestra el porcentaje de uso de la memoria.*
  - **`on`:** *Muestra el uso de la memoria y el porcentaje (p. ej., `1801MiB / 7881MiB (22%)`).*
  - **`off`:** *Muestra solo el uso de la memoria sin el porcentaje (p. ej., `1801MiB / 7881MiB`).*
  - **Valor por defecto:** *`off`.*

### ***Unidad de Memoria***

```bash
# Change memory output unit.
#
# Default: 'mib'
# Values:  'kib', 'mib', 'gib'
# Flag:    --memory_unit
#
# Example:
# kib  '1020928KiB / 7117824KiB'
# mib  '1042MiB / 6951MiB'
# gib: ' 0.98GiB / 6.79GiB'
memory_unit="gib"
```

- **`memory_unit`:** *Ajusta la unidad en la que se muestra la memoria.*
  - **`kib`:** *Kilobytes (p. ej., `1020928KiB / 7117824KiB`).*
  - **`mib`:** *Mebibytes (p. ej., `1042MiB / 6951MiB`).*
  - **`gib`:** *Gibibytes (p. ej., `0.98GiB / 6.79GiB`).*
  - **Valor por defecto:** *`mib`.*

### ***Paquetes***

```bash
# Packages

# Show/Hide Package Manager names.
#
# Default: 'tiny'
# Values:  'on', 'tiny' 'off'
# Flag:    --package_managers
#
# Example:
# on:   '998 (pacman), 8 (flatpak), 4 (snap)'
# tiny: '908 (pacman, flatpak, snap)'
# off:  '908'
package_managers="on"
```

- **`package_managers`:** *Controla si se muestra el nombre de los gestores de paquetes.*
  - **`on`:** *Muestra el número de paquetes por gestor de paquetes (p. ej., `998 (pacman), 8 (flatpak), 4 (snap)`).*
  - **`tiny`:** *Muestra una versión abreviada (p. ej., `908 (pacman, flatpak, snap)`).*
  - **`off`:** *Solo muestra el número total de paquetes sin detalles de los gestores (p. ej., `908`).*
  - **Valor por defecto:** *`tiny`.*

### ***Shell***

```bash
# Shell

# Show the path to $SHELL
#
# Default: 'off'
# Values:  'on', 'off'
# Flag:    --shell_path
#
# Example:
# on:  '/bin/bash'
# off: 'bash'
shell_path="on"

# Show $SHELL version
#
# Default: 'on'
# Values:  'on', 'off'
# Flag:    --shell_version
#
# Example:
# on:  'bash 4.4.5'
# off: 'bash'
shell_version="on"
```

- **`shell_path`:** *Controla si se muestra la ruta completa del shell en uso.*
  - **`on`:** *Muestra la ruta completa (p. ej., `/bin/bash`).*
  - **`off`:** *Muestra solo el nombre del shell (p. ej., `bash`).*
  - **Valor por defecto:** *`off`.*

- **`shell_version`:** *Controla si se muestra la versión del shell en uso.*
  - **`on`:** *Muestra la versión del shell (p. ej., `bash 4.4.5`).*
  - **`off`:** *Muestra solo el nombre del shell (p. ej., `bash`).*
  - **Valor por defecto:** *`on`.*

### ***CPU***

```bash
# CPU

# CPU speed type
#
# Default: 'bios_limit'
# Values: 'scaling_cur_freq', 'scaling_min_freq', 'scaling_max_freq', 'bios_limit'.
# Flag:    --speed_type
# Supports: Linux with 'cpufreq'
# NOTE: Any file in '/sys/devices/system/cpu/cpu0/cpufreq' can be used as a value.
speed_type="bios_limit"
```

- **`speed_type`:** *Define el tipo de velocidad de CPU que se muestra.*
  - **`scaling_cur_freq`:** *Velocidad actual del CPU.*
  - **`scaling_min_freq`:** *Velocidad mínima del CPU.*

- **`scaling_max_freq`:** *Velocidad máxima del CPU.*
- **`bios_limit`:** *Velocidad limitada por la BIOS.*
- **Valor por defecto:** *`bios_limit`.*

### ***CPU Speed Shorthand***

```bash
# CPU speed shorthand
#
# Default: 'off'
# Values: 'on', 'off'.
# Flag:    --speed_shorthand
# NOTE: This flag is not supported in systems with CPU speed less than 1 GHz
#
# Example:
# on:    'i7-6500U (4) @ 3.1GHz'
# off:   'i7-6500U (4) @ 3.100GHz'
speed_shorthand="off"
```

- **`speed_shorthand`:** *Controla el formato de la velocidad del CPU.*
  - **`on`:** *Muestra la velocidad del CPU con una precisión reducida (p. ej., `3.1GHz`).*
  - **`off`:** *Muestra la velocidad del CPU con mayor precisión (p. ej., `3.100GHz`).*
  - **Valor por defecto:** *`off`.*
  - **Nota:** *No se soporta en sistemas con una velocidad de CPU menor a 1 GHz.*

### ***CPU Brand***

```bash
# Enable/Disable CPU brand in output.
#
# Default: 'on'
# Values:  'on', 'off'
# Flag:    --cpu_brand
#
# Example:
# on:   'Intel i7-6500U'
# off:  'i7-6500U (4)'
cpu_brand="on"
```

- **`cpu_brand`:** *Controla si se muestra el nombre de la marca del CPU.*
  - **`on`:** *Muestra el nombre completo de la marca del CPU (p. ej., `Intel i7-6500U`).*
  - **`off`:** *Muestra solo el modelo del CPU sin la marca (p. ej., `i7-6500U (4)`).*
  - **Valor por defecto:** *`on`.*

### ***CPU Speed***

```bash
# CPU Speed
# Hide/Show CPU speed.
#
# Default: 'on'
# Values:  'on', 'off'
# Flag:    --cpu_speed
#
# Example:
# on:  'Intel i7-6500U (4) @ 3.1GHz'
# off: 'Intel i7-6500U (4)'
cpu_speed="on"
```

- **`cpu_speed`:** *Controla si se muestra la velocidad del CPU.*
  - **`on`:** *Muestra la velocidad del CPU junto con el modelo y número de núcleos (p. ej., `Intel i7-6500U (4) @ 3.1GHz`).*
  - **`off`:** *Muestra solo el modelo y número de núcleos del CPU sin la velocidad (p. ej., `Intel i7-6500U (4)`).*
  - **Valor por defecto:** *`on`.*

### ***CPU Cores***

```bash
# CPU Cores
# Display CPU cores in output
#
# Default: 'logical'
# Values:  'logical', 'physical', 'off'
# Flag:    --cpu_cores
# Support: 'physical' doesn't work on BSD.
#
# Example:
# logical:  'Intel i7-6500U (4) @ 3.1GHz' (All virtual cores)
# physical: 'Intel i7-6500U (2) @ 3.1GHz' (All physical cores)
# off:      'Intel i7-6500U @ 3.1GHz'
cpu_cores="logical"
```

- **`cpu_cores`:** *Controla cómo se muestran los núcleos del CPU.*
  - **`logical`:** *Muestra todos los núcleos lógicos (virtuales) del CPU (p. ej., `Intel i7-6500U (4) @ 3.1GHz`).*
  - **`physical`:** *Muestra solo los núcleos físicos del CPU (p. ej., `Intel i7-6500U (2) @ 3.1GHz`).*
  - **`off`:** *Muestra solo el modelo del CPU sin detalles sobre los núcleos (p. ej., `Intel i7-6500U @ 3.1GHz`).*
  - **Valor por defecto:** *`logical`.*
  - **Nota:** *`physical` no funciona en sistemas BSD.*

### ***CPU Temperature***

```bash
# CPU Temperature
# Hide/Show CPU temperature.
# Note the temperature is added to the regular CPU function.
#
# Default: 'off'
# Values:  'C', 'F', 'off'
# Flag:    --cpu_temp
# Supports: Linux, BSD
# NOTE: For FreeBSD and NetBSD-based systems, you'll need to enable
#       coretemp kernel module. This only supports newer Intel processors.
#
# Example:
# C:   'Intel i7-6500U (4) @ 3.1GHz [27.2°C]'
# F:   'Intel i7-6500U (4) @ 3.1GHz [82.0°F]'
# off: 'Intel i7-6500U (4) @ 3.1GHz'
cpu_temp="C:"
```

- **`cpu_temp`:** *Controla si se muestra la temperatura del CPU.*
  - **`C`:** *Muestra la temperatura en grados Celsius (p. ej., `Intel i7-6500U (4) @ 3.1GHz [27.2°C]`).*
  - **`F`:** *Muestra la temperatura en grados Fahrenheit (p. ej., `Intel i7-6500U (4) @ 3.1GHz [82.0°F]`).*
  - **`off`:** *No muestra la temperatura del CPU (p. ej., `Intel i7-6500U (4) @ 3.1GHz`).*
  - **Valor por defecto:** *`off`.*
  - **Nota:** *En sistemas FreeBSD y NetBSD, se necesita habilitar el módulo del kernel `coretemp` para obtener la temperatura, y solo es compatible con procesadores Intel más recientes.*

### ***GPU Brand***

```bash
# GPU

# Enable/Disable GPU Brand
#
# Default: 'on'
# Values:  'on', 'off'
# Flag:    --gpu_brand
#
# Example:
# on:  'AMD HD 7950'
# off: 'HD 7950'
gpu_brand="on"
```

- **`gpu_brand`:** *Controla si se muestra la marca de la GPU.*
  - **`on`:** *Muestra el nombre completo de la marca de la GPU (p. ej., `AMD HD 7950`).*
  - **`off`:** *Muestra solo el modelo de la GPU sin la marca (p. ej., `HD 7950`).*
  - **Valor por defecto:** *`on`.*

### ***GPU Type***

```bash
# Which GPU to display
#
# Default: 'all'
# Values:  'all', 'dedicated', 'integrated'
# Flag:    --gpu_type
# Supports: Linux
#
# Example:
# all:
#   GPU1: AMD HD 7950
#   GPU2: Intel Integrated Graphics
#
# dedicated:
#   GPU1: AMD HD 7950
#
# integrated:
#   GPU1: Intel Integrated Graphics
gpu_type="all"
```

- **`gpu_type`:** *Controla qué tipo de GPU se muestra.*
  - **`all`:** *Muestra todas las GPU (dedicadas e integradas) (p. ej., `GPU1: AMD HD 7950`, `GPU2: Intel Integrated Graphics`).*
  - **`dedicated`:** *Muestra solo las GPU dedicadas (p. ej., `GPU1: AMD HD 7950`).*
  - **`integrated`:** *Muestra solo las GPU integradas (p. ej., `GPU1: Intel Integrated Graphics`).*
  - **Valor por defecto:** *`all`.*

### ***Resolution***

```bash
# Resolution

# Display refresh rate next to each monitor
# Default: 'off'
# Values:  'on', 'off'
# Flag:    --refresh_rate
# Supports: Doesn't work on Windows.
#
# Example:
# on:  '1920x1080 @ 60Hz'
# off: '1920x1080'
refresh_rate="on"
```

- **`refresh_rate`:** *Controla si se muestra la tasa de refresco junto con la resolución del monitor.*
  - **`on`:** *Muestra la tasa de refresco (p. ej., `1920x1080 @ 60Hz`).*
  - **`off`:** *Solo muestra la resolución sin la tasa de refresco (p. ej., `1920x1080`).*
  - **Valor por defecto:** *`off`.*
  - **Nota:** *No funciona en Windows.*

### ***GTK Theme / Icons / Font***

```bash
# Gtk Theme / Icons / Font

# Shorten output of GTK Theme / Icons / Font
#
# Default: 'off'
# Values:  'on', 'off'
# Flag:    --gtk_shorthand
#
# Example:
# on:  'Numix, Adwaita'
# off: 'Numix [GTK2], Adwaita [GTK3]'
gtk_shorthand="off"
```

- **`

gtk_shorthand`:** *Controla el formato abreviado para temas, iconos y fuentes GTK.*

- **`on`:** *Muestra la información en formato abreviado (p. ej., `Numix, Adwaita`).*
- **`off`:** *Muestra la información completa (p. ej., `Numix [GTK2], Adwaita [GTK3]`).*
- **Valor por defecto:** *`off`.*

### ***GTK2 / GTK3***

```bash
# Enable/Disable gtk2 Theme / Icons / Font
#
# Default: 'on'
# Values:  'on', 'off'
# Flag:    --gtk2
#
# Example:
# on:  'Numix [GTK2], Adwaita [GTK3]'
# off: 'Adwaita [GTK3]'
gtk2="on"

# Enable/Disable gtk3 Theme / Icons / Font
#
# Default: 'on'
# Values:  'on', 'off'
# Flag:    --gtk3
#
# Example:
# on:  'Numix [GTK2], Adwaita [GTK3]'
# off: 'Numix [GTK2]'
gtk3="on"
```

- **`gtk2`** *y* **`gtk3`:** *Controlan si se muestra la información de los temas, iconos y fuentes GTK2 y GTK3.*
  - **`gtk2`:**
    - **`on`:** *Muestra la información sobre el tema, iconos y fuentes GTK2 (p. ej., `Numix [GTK2], Adwaita [GTK3]`).*
    - **`off`:** *No muestra la información sobre GTK2 (p. ej., `Adwaita [GTK3]`).*
    - **Valor por defecto:** *`on`.*
  - **`gtk3`:**
    - **`on`:** *Muestra la información sobre el tema, iconos y fuentes GTK3 (p. ej., `Numix [GTK2], Adwaita [GTK3]`).*
    - **`off`:** *No muestra la información sobre GTK3 (p. ej., `Numix [GTK2]`).*
    - **Valor por defecto:** *`on`.*

### ***IP Address***

```bash
# IP Address

# Website to ping for the public IP
#
# Default: 'http://ident.me'
# Values:  'url'
# Flag:    --ip_host
public_ip_host="http://ident.me"

# Public IP timeout.
#
# Default: '2'
# Values:  'int'
# Flag:    --ip_timeout
public_ip_timeout=2
```

- **`public_ip_host`:** *Define el sitio web para consultar la IP pública.*
  - **Valor por defecto:** *`http://ident.me`.*
- **`public_ip_timeout`:** *Define el tiempo de espera para obtener la IP pública.*
  - **Valor por defecto:** *`2` (segundos).*

### ***Desktop Environment***

```bash
# Desktop Environment

# Show Desktop Environment version
#
# Default: 'on'
# Values:  'on', 'off'
# Flag:    --de_version
de_version="on"
```

- **`de_version`:** *Controla si se muestra la versión del entorno de escritorio.*
  - **`on`:** *Muestra la versión del entorno de escritorio (p. ej., `GNOME 3.38`).*
  - **`off`:** *No muestra la versión del entorno de escritorio.*
  - **Valor por defecto:** *`on`.*

### ***Disk***

```bash
# Disk

# Which disks to display.
# The values can be any /dev/sdXX, mount point or directory.
# NOTE: By default we only show the disk info for '/'.
#
# Default: '/'
# Values:  '/', '/dev/sdXX', '/path/to/drive'.
# Flag:    --disk_show
#
# Example:
# disk_show=('/' '/dev/sdb1'):
#      'Disk (/): 74G / 118G (66%)'
#      'Disk (/mnt/Videos): 823G / 893G (93%)'
#
# disk_show=('/'):
#      'Disk (/): 74G / 118G (66%)'
#
disk_show=('/')
```

- **`disk_show`:** *Controla qué discos se muestran en la salida.*
  - **`/`:** *Muestra información solo sobre el disco raíz.*
  - **`/dev/sdXX`:** *Muestra información sobre un disco específico.*
  - **`/path/to/drive`:** *Muestra información sobre un disco montado en una ruta específica.*
  - **Valor por defecto:** *`/`.*

### ***Disk Subtitle***

```bash
# Disk subtitle.
# What to append to the Disk subtitle.
#
# Default: 'mount'
# Values:  'mount', 'name', 'dir', 'none'
# Flag:    --disk_subtitle
#
# Example:
# name:   'Disk (/dev/sda1): 74G / 118G (66%)'
#         'Disk (/dev/sdb2): 74G / 118G (66%)'
#
# mount:  'Disk (/): 74G / 118G (66%)'
#         'Disk (/mnt/Local Disk): 74G / 118G (66%)'
#         'Disk (/mnt/Videos): 74G / 118G (66%)'
#
# dir:    'Disk (/): 74G / 118G (66%)'
#         'Disk (Local Disk): 74G / 118G (66%)'
#         'Disk (Videos): 74G / 118G (66%)'
#
# none:   'Disk: 74G / 118G (66%)'
#         'Disk: 74G / 118G (66%)'
#         'Disk: 74G / 118G (66%)'
disk_subtitle="mount"
```

- **`disk_subtitle`:** *Controla el subtítulo que se muestra junto a la información del disco.*
  - **`mount`:** *Usa el punto de montaje como subtítulo (p. ej., `Disk (/): 74G / 118G (66%)`).*
  - **`name`:** *Usa el nombre del disco como subtítulo (p. ej., `Disk (/dev/sda1): 74G / 118G (66%)`).*
  - **`dir`:** *Usa el nombre del directorio del disco como subtítulo (p. ej., `Disk (Local Disk): 74G / 118G (66%)`).*
  - **`none`:** *No usa ningún subtítulo (p. ej., `Disk: 74G / 118G (66%)`).*
  - **Valor por defecto:** *`mount`.*

**Aquí está la explicación de las opciones para `neofetch` relacionadas con el disco, la música y los colores:**

### ***Disk Percent***

```bash
# Disk percent.
# Show/Hide disk percent.
#
# Default: 'on'
# Values:  'on', 'off'
# Flag:    --disk_percent
#
# Example:
# on:  'Disk (/): 74G / 118G (66%)'
# off: 'Disk (/): 74G / 118G'
disk_percent="on"
```

- **`disk_percent`:** *Controla si se muestra el porcentaje de uso del disco.*
  - **`on`:** *Muestra el porcentaje de uso del disco (p. ej., `Disk (/): 74G / 118G (66%)`).*
  - **`off`:** *No muestra el porcentaje de uso del disco (p. ej., `Disk (/): 74G / 118G`).*
  - **Valor por defecto:** *`on`.*

### ***Song***

```bash
# Song

# Manually specify a music player.
#
# Default: 'auto'
# Values:  'auto', 'player-name'
# Flag:    --music_player
#
# Available values for 'player-name':
#
# amarok
# audacious
# banshee
# bluemindo
# clementine
# cmus
# deadbeef
# deepin-music
# dragon
# elisa
# exaile
# gnome-music
# gmusicbrowser
# gogglesmm
# guayadeque
# io.elementary.music
# iTunes
# juk
# lollypop
# mocp
# mopidy
# mpd
# muine
# netease-cloud-music
# olivia
# playerctl
# pogo
# pragha
# qmmp
# quodlibet
# rhythmbox
# sayonara
# smplayer
# spotify
# strawberry
# tauonmb
# tomahawk
# vlc
# xmms2d
# xnoise
# yarock
music_player="auto"

# Format to display song information.
#
# Default: '%artist% - %album% - %title%'
# Values:  '%artist%', '%album%', '%title%'
# Flag:    --song_format
#
# Example:
# default: 'Song: Jet - Get Born - Sgt Major'
song_format="%artist% - %album% - %title%"

# Print the Artist, Album and Title on separate lines
#
# Default: 'off'
# Values:  'on', 'off'
# Flag:    --song_shorthand
#
# Example:
# on:  'Artist: The Fratellis'
#      'Album: Costello Music'
#      'Song: Chelsea Dagger'
#
# off: 'Song: The Fratellis - Costello Music - Chelsea Dagger'
song_shorthand="off"

# 'mpc' arguments (specify a host, password etc).
#
# Default:  ''
# Example: mpc_args=(-h HOST -P PASSWORD)
mpc_args=()
```

- **`music_player`:** *Especifica manualmente el reproductor de música a utilizar.*
  - **`auto`:** *Detecta automáticamente el reproductor de música.*
  - **`player-name`:** *Puedes especificar un reproductor de música en particular de la lista (p. ej., `spotify`, `vlc`).*
  - **Valor por defecto:** *`auto`.*

- **`song_format`:** *Define el formato para mostrar la información de la canción.*
  - **`%artist% - %album% - %title%`:** *Muestra la canción en formato de artista, álbum y título (p. ej., `Jet - Get Born - Sgt Major`).*
  - **Valores disponibles:** *`%artist%`, `%album%`, `%title%`.*

- **`song_shorthand`:** *Controla si la información de la canción se muestra en líneas separadas.*
  - **`on`:** *Muestra el artista, álbum y título en líneas separadas.*
  - **`off`:** *Muestra la información de la canción en una sola línea.*
  - **Valor por defecto:** *`off`.*

- **`mpc_args`:** *Argumentos para `mpc`, como host y contraseña.*

### ***Text Colors***

```bash
# Text Colors

# Text Colors
#
# Default:  'distro'
# Values:   'distro', 'num' 'num' 'num' 'num' 'num' 'num'
# Flag:     --colors
#
# Each number represents a different part of the text in
# this order: 'title', '@', 'underline', 'subtitle', 'colon', 'info'
#
# Example:
# colors=(distro)      - Text is colored based on Distro colors.
# colors=(4 6 1 8 8 6) - Text is colored in the order above.
colors=(distro)
```

- **`colors`:** *Define los colores del texto en la salida de `neofetch`.*
  - **`distro`:** *Usa los colores basados en la distribución.*
  - **`num num num num num num`:** *Define colores específicos para partes del texto en el siguiente orden: título, `@`, subrayado, subtítulo, dos puntos e información.*
  - **Valor por defecto:** *`distro`.*

### ***Text Options***

```bash
# Text Options

# Toggle bold text
#
# Default:  'on'
# Values:   'on', 'off'
# Flag:     --bold
bold="on"

# Enable/Disable Underline
#
# Default:  'on'
# Values:   'on', 'off'
# Flag:     --underline
underline_enabled="on"

# Underline character
#
# Default:  '-'
# Values:   'string'
# Flag:     --underline_char
underline_char="-"

# Info Separator
# Replace the default separator with the specified string.
#
# Default:  ':'
# Flag:     --separator
#
# Example:
# separator="->":   'Shell-> bash'
# separator=" =":   'WM = dwm'
separator=":"
```

- **`bold`:** *Controla si el texto se muestra en negrita.*
  - **`on`:** *Activa el texto en negrita.*
  - **`off`:** *Desactiva el texto en negrita.*
  - **Valor por defecto:** *`on`.*

- **`underline_enabled`:** *Controla si el texto se subraya.*
  - **`on`:** *Activa el subrayado.*
  - **`off`:** *Desactiva el subrayado.*
  - **Valor por defecto:** *`on`.*

- **`underline_char`:** *Define el carácter para el subrayado.*
  - **Valor por defecto:** *`-`.*

- **`separator`:** *Reemplaza el separador predeterminado con el especificado.*
  - **Valor por defecto:** *`:`.*

### ***Color Blocks***

```bash
# Color Blocks

# Color block range
# The range of colors to print.
#
# Default:  '0', '15'
# Values:   'num'
# Flag:     --block_range
#
# Example:
#
# Display colors 0-7 in the blocks.  (8 colors)
# neofetch --block_range 0 7
#
# Display colors 0-15 in the blocks. (16 colors)
# neofetch --block_range 0 15
block_range=(0 15)

# Toggle color blocks
#
# Default:  'on'
# Values:   'on', 'off'
# Flag:     --color_blocks
color_blocks="on"

# Color block width in spaces
#
# Default:  '3'
# Values:   'num'
# Flag:     --block_width
block_width=3

# Color block height in lines
#
# Default:  '1'
# Values:   'num'
# Flag:     --block_height
block_height=1

# Color Alignment
#
# Default: 'auto'
# Values: 'auto', 'num'
# Flag: --col_offset
#
# Number specifies how far from the left side of the terminal (in spaces) to
# begin printing the columns, in case you want to e.g. center them under your
# text.
# Example:
# col_offset="auto" - Default behavior of neofetch
# col_offset=7      - Leave 7 spaces then print the colors
col_offset="auto"
```

- **`block_range`:** *Define el rango de colores que se imprimen en los bloques.*
  - **Valor por defecto:** *`0 15` (muestra colores del 0 al 15).*

- **`color_blocks`:** *Controla si se muestran los bloques de color.*
  - **`on`:** *Muestra los bloques de color.*
  - **`off`:** *No muestra los bloques de color.*
  - **Valor por defecto:** *`on`.*

- **`block_width`:** *Define el ancho de los bloques de color en espacios.*
  - **Valor por defecto:** *`3`.*

- **`block_height`:** *Define la altura de los bloques de color en líneas.*
  - **Valor por defecto:** *`1`.*

- **`col_offset`:** *Define la alineación de los bloques de color desde el lado izquierdo del terminal.*

  - **`auto`:** *Comportamiento predeterminado de `neofetch`.*
  - **`num`:** *Define un número específico de espacios desde el lado izquierdo para comenzar a imprimir los colores.*

**Esta configuración se refiere a la personalización de barras de progreso y opciones relacionadas con imágenes en la herramienta `neofetch`. Aquí está una explicación detallada de cada sección:**

### ***Barra de Progreso***

1. **Caracteres de la barra (`--bar_char`)**
   - **Descripción:** *Define los caracteres que se utilizan para representar las barras de progreso.*
   - **Valores:**
     - **`'-'` y `'='`:** *Carácter por defecto.*
     - **Ejemplo:** *`neofetch --bar_char '-' '='` usa `'-'` para el tiempo transcurrido y `'='` para el total.*

2. **Bordes de la Barra (`--bar_border`)**
   - **Descripción:** *Activa o desactiva el borde de las barras de progreso.*
   - **Valores:**
     - **`'on'`:** *Activa el borde.*
     - **`'off'`:** *Desactiva el borde.*

3. **Longitud de la Barra (`--bar_length`)**
   - **Descripción:** *Define la longitud de las barras de progreso en espacios.*
   - **Valor por defecto:** *`15`.*
   - **Ejemplo:** *`--bar_length 20` ajusta la longitud a 20 caracteres.*

4. **Colores de la Barra (`--bar_colors`)**
   - **Descripción:** *Establece los colores de las barras de progreso. Puede usar los colores del logo de tu distribución o definir números de colores.*
   - **Valores:**
     - **`'distro'`:** *Usa los colores del logo de la distribución.*
     - **`'num'`:** *Define números de colores específicos.*
     - **Ejemplo:** *`neofetch --bar_colors 3 4` usa el color 3 para el tiempo transcurrido y el color 4 para el total.*

5. **Mostrar Información con Barras (`--cpu_display`, `--memory_display`, `--battery_display`, `--disk_display`)**
   - **Descripción:** *Define cómo se muestra la información junto con las barras de progreso.*
   - **Valores:**
     - **`'bar'`:** *Solo la barra.*
     - **`'infobar'`:** *Información seguida de la barra.*
     - **`'barinfo'`:** *Barra seguida de la información.*
     - **`'off'`:** *Solo la información, sin barras.*
   - **Ejemplo:** *`--cpu_display 'barinfo'` muestra la barra de progreso seguida de la información de la CPU.*

### ***Opciones de Imágenes***

1. **Backend de Imagen (`--backend`)**
   - **Descripción:** *Define el backend para mostrar imágenes.*
   - **Valores:**
     - **`'ascii'`**, **`'caca'`**, **`'chafa'`***, etc.: Diferentes métodos para mostrar imágenes en la terminal.*
   - **Ejemplo:** *`image_backend='ascii'` usa el backend `ascii`.*

2. **Fuente de Imagen (`--source`)**
   - **Descripción:** *Especifica la fuente de la imagen o fichero ASCII a mostrar.*
   - **Valores:**
     - **`'auto'`:** *Selecciona automáticamente la mejor fuente según el backend.*
     - **`'/path/to/img'`:** *Ruta a una imagen específica.*
   - **Ejemplo:** *`image_source='/path/to/image.png'` usa una imagen específica en la ruta indicada.*

3. **Distribución ASCII (`--ascii_distro`)**
   - **Descripción:** *Define el arte ASCII para la distribución que se muestra.*
   - **Valores:**
     - **`'auto'`:** *Selecciona automáticamente el arte ASCII adecuado.*
     - **`'distro_name'`:** *Nombre específico de la distribución para el arte ASCII.*
   - **Ejemplo:** *`ascii_distro='Arch'` usa el arte ASCII para Arch Linux.*

4. **Colores ASCII (`--ascii_colors`)**
   - **Descripción:** *Configura los colores para el arte ASCII.*
   - **Valores:**
     - **`'distro'`:** *Usa los colores de la distribución.*
     - **`'num'`:** *Números de colores específicos.*
   - **Ejemplo:** *`ascii_colors=(4 6 1 8 8 6)` usa una paleta de colores específica para el arte ASCII.*

5. **Logo ASCII Negrita (`--ascii_bold`)**
   - **Descripción:** *Define si el logo ASCII debe estar en negrita.*
   - **Valores:**
     - **`'on'`:** *Activa la negrita.*
     - **`'off'`:** *Desactiva la negrita.*

### ***Opciones Adicionales***

1. **Bucle de Imagen (`--loop`)**
   - **Descripción:** *Si se activa, `neofetch` redibuja la imagen continuamente.*
   - **Valores:**
     - **`'on'`:** *Activa el bucle.*
     - **`'off'`:** *Desactiva el bucle.*

2. **Directorio de Miniaturas (`--thumbnail_dir`)**
   - **Descripción:** *Directorio donde se guardan las miniaturas de imágenes.*
   - **Valor por defecto:** *`'~/.cache/thumbnails/neofetch'`.*

3. **Modo de Recorte (`--crop_mode`)**
   - **Descripción:** *Define el modo de recorte para las imágenes.*
   - **Valores:**
     - **`'normal'`:** *Modo de recorte normal.*
     - **`'fit'`:** *Ajusta la imagen para que encaje en el espacio.*
     - **`'fill'`:** *Rellena el espacio con la imagen.*
   - **Ejemplo:** *`crop_mode='fit'`.*

4. **Desplazamiento del Recorte (`--crop_offset`)**
   - **Descripción:** *Define el desplazamiento para el modo de recorte normal.*
   - **Valores:**
     - **`'center'`:** *Centro de la imagen.*
     - **`'northwest'`**, **`'south'`**, etc.: Otros puntos de referencia para el desplazamiento.

5. **Tamaño de Imagen (`--image_size`)**
   - **Descripción:** *Configura el tamaño de la imagen.*
   - **Valores:**
     - **`'auto'`:** *Tamaño automático.*
     - **`'00px'`:** *Tamaño específico en píxeles.*
   - **Ejemplo:** *`image_size='50%'`.*

6. **Espacio entre Imagen y Texto (`--gap`)**
   - **Descripción:** *Define el espacio entre la imagen y el texto.*
   - **Valor por defecto:** *`8` espacios.*

7. **Desplazamientos de Imagen (`--xoffset`, `--yoffset`)**
   - **Descripción:** *Configura los desplazamientos horizontales y verticales para la imagen.*
   - **Valores:**
     - **`'px'`:** *Desplazamiento en píxeles.*
   - **Ejemplo:** *`xoffset=2`.*

8. **Color de Fondo de Imagen (`--bg_color`)**
   - **Descripción:** *Define el color de fondo para la imagen.*
   - **Valores:**
     - **`'color'`:** *Color de fondo.*
     - **`'blue'`:** *Ejemplo de color específico.*

9. **Modo Stdout (`--stdout`)**
   - **Descripción:** *Desactiva los colores y el backend de imágenes para usar `neofetch` en tuberías.*
   - **Valores:**
     - **`'on'`:** *Activa el modo stdout.*
     - **`'off'`:** *Desactiva el modo stdout.*

**Estas configuraciones te permiten personalizar la apariencia de `neofetch`, ajustar cómo se muestran las barras de progreso, manejar imágenes y arte ASCII, y definir opciones adicionales para una presentación más adaptada a tus preferencias.**

```conf
# See this wiki page for more info:
# https://github.com/dylanaraps/neofetch/wiki/Customizing-Info

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

print_info() {

  # Leer la primera palabra del fichero /var/log/installer/media-info
  dist=$(awk '{print $1}' /var/log/installer/media-info | tr '[:upper:]' '[:lower:]')

  # Determinar el símbolo basado en el valor
  case "$dist" in
  ubuntu | xubuntu | lubuntu)
    symbol=""
    ;;
  arch)
    symbol="󰣇"
    ;;
  parrot)
    symbol=""
    ;;
  *)
    symbol=""
    ;;
  esac

  prin "​ ​​ $(color 6) Using $symbol for my OS ​​ ​"
  prin "$(color 8)┌────────────────────────────────────────────────────┐"

  info "​ ​ ​​$(color 1) $symbol OS          " distro
  #    info "​ ​​ ​$(color 1)  Host        " model
  info "​ ​​ ​$(color 1)  Kernel      " kernel
  #    info "​ ​​ ​$(color 1)  Uptime      " uptime
  info "​ ​​ ​$(color 2)  Packages    " packages
  #    info "​ ​​ ​$(color 2)  Shell       " shell
  info "​ ​​ ​$(color 2) 󰍹 Resolution  " resolution
  info "​ ​​ ​$(color 3)  de          " de
  #    info "​ ​​ ​$(color 3) 缾WM          " wm
  #    info "​ ​​ ​$(color 12)  WM Theme    " wm_theme
  #    info "$(color 13)  Theme       " theme
  #    info "$(color 14)  Icons       " icons
  info "​ ​​ ​$(color 3)  Terminal    " term
  #    info " Font        " font
  #    info " Terminal Font   " term_font

  prin "$(color 8)└────────────────────────────────────────────────────┘"
  prin " "
  info "​ ​​ ​​​ $(color 6) " title
  prin "$(color 8)┌────────────────────────────────────────────────────┐"

  info "​ ​​ ​$(color 12) 󰻠 CPU         " cpu
  info "​ ​​ ​$(color 12)  GPU         " gpu
  info "​ ​​ ​$(color 13)  GPU Driver  " gpu_driver # Linux/macOS only
  info "​ ​​ ​$(color 13)  Memory      " memory

  # info "CPU Usage" cpu_usage
  # info "Disk" disk
  # info "Battery" battery
  # info "Song" song
  # [[ "$player" ]] && prin "Music Player" "$player"
  # info "Local IP" local_ip
  # info "Public IP" public_ip
  # info "Users" users
  # info "Locale" locale  # This only works on glibc systems.

  prin "$(color 8)└────────────────────────────────────────────────────┘"
  prin " "
  prin "​ ​​ ​​ ​​$(color 1)​ ​​ ​​$(color 2)​ ​​ ​​$(color 3)​ ​​ ​​$(color 4)​ ​​ ​​$(color 5)​ ​​ ​​$(color 6)​ ​​ ​​$(color 7)​ ​​ ​​$(color 8)​ ​​ ​​$(color 16)"

}

# Title

# Hide/Show Fully qualified domain name.
#
# Default:  'off'
# Values:   'on', 'off'
# Flag:     --title_fqdn
title_fqdn="off"

# Kernel

# Shorten the output of the kernel function.
#
# Default:  'on'
# Values:   'on', 'off'
# Flag:     --kernel_shorthand
# Supports: Everything except *BSDs (except PacBSD and PC-BSD)
#
# Example:
# on:  '4.8.9-1-ARCH'
# off: 'Linux 4.8.9-1-ARCH'
kernel_shorthand="on"

# Distro

# Shorten the output of the distro function
#
# Default:  'off'
# Values:   'on', 'tiny', 'off'
# Flag:     --distro_shorthand
# Supports: Everything except Windows and Haiku
distro_shorthand="off"

# Show/Hide OS Architecture.
# Show 'x86_64', 'x86' and etc in 'Distro:' output.
#
# Default: 'on'
# Values:  'on', 'off'
# Flag:    --os_arch
#
# Example:
# on:  'Arch Linux x86_64'
# off: 'Arch Linux'
os_arch="on"

# Uptime

# Shorten the output of the uptime function
#
# Default: 'on'
# Values:  'on', 'tiny', 'off'
# Flag:    --uptime_shorthand
#
# Example:
# on:   '2 days, 10 hours, 3 mins'
# tiny: '2d 10h 3m'
# off:  '2 days, 10 hours, 3 minutes'
uptime_shorthand="off"

# Memory

# Show memory pecentage in output.
#
# Default: 'off'
# Values:  'on', 'off'
# Flag:    --memory_percent
#
# Example:
# on:   '1801MiB / 7881MiB (22%)'
# off:  '1801MiB / 7881MiB'
memory_percent="on"

# Change memory output unit.
#
# Default: 'mib'
# Values:  'kib', 'mib', 'gib'
# Flag:    --memory_unit
#
# Example:
# kib  '1020928KiB / 7117824KiB'
# mib  '1042MiB / 6951MiB'
# gib: ' 0.98GiB / 6.79GiB'
memory_unit="gib"

# Packages

# Show/Hide Package Manager names.
#
# Default: 'tiny'
# Values:  'on', 'tiny' 'off'
# Flag:    --package_managers
#
# Example:
# on:   '998 (pacman), 8 (flatpak), 4 (snap)'
# tiny: '908 (pacman, flatpak, snap)'
# off:  '908'
package_managers="on"

# Shell

# Show the path to $SHELL
#
# Default: 'off'
# Values:  'on', 'off'
# Flag:    --shell_path
#
# Example:
# on:  '/bin/bash'
# off: 'bash'
shell_path="on"

# Show $SHELL version
#
# Default: 'on'
# Values:  'on', 'off'
# Flag:    --shell_version
#
# Example:
# on:  'bash 4.4.5'
# off: 'bash'
shell_version="on"

# CPU

# CPU speed type
#
# Default: 'bios_limit'
# Values: 'scaling_cur_freq', 'scaling_min_freq', 'scaling_max_freq', 'bios_limit'.
# Flag:    --speed_type
# Supports: Linux with 'cpufreq'
# NOTE: Any file in '/sys/devices/system/cpu/cpu0/cpufreq' can be used as a value.
speed_type="bios_limit"

# CPU speed shorthand
#
# Default: 'off'
# Values: 'on', 'off'.
# Flag:    --speed_shorthand
# NOTE: This flag is not supported in systems with CPU speed less than 1 GHz
#
# Example:
# on:    'i7-6500U (4) @ 3.1GHz'
# off:   'i7-6500U (4) @ 3.100GHz'
speed_shorthand="off"

# Enable/Disable CPU brand in output.
#
# Default: 'on'
# Values:  'on', 'off'
# Flag:    --cpu_brand
#
# Example:
# on:   'Intel i7-6500U'
# off:  'i7-6500U (4)'
cpu_brand="on"

# CPU Speed
# Hide/Show CPU speed.
#
# Default: 'on'
# Values:  'on', 'off'
# Flag:    --cpu_speed
#
# Example:
# on:  'Intel i7-6500U (4) @ 3.1GHz'
# off: 'Intel i7-6500U (4)'
cpu_speed="on"

# CPU Cores
# Display CPU cores in output
#
# Default: 'logical'
# Values:  'logical', 'physical', 'off'
# Flag:    --cpu_cores
# Support: 'physical' doesn't work on BSD.
#
# Example:
# logical:  'Intel i7-6500U (4) @ 3.1GHz' (All virtual cores)
# physical: 'Intel i7-6500U (2) @ 3.1GHz' (All physical cores)
# off:      'Intel i7-6500U @ 3.1GHz'
cpu_cores="logical"

# CPU Temperature
# Hide/Show CPU temperature.
# Note the temperature is added to the regular CPU function.
#
# Default: 'off'
# Values:  'C', 'F', 'off'
# Flag:    --cpu_temp
# Supports: Linux, BSD
# NOTE: For FreeBSD and NetBSD-based systems, you'll need to enable
#       coretemp kernel module. This only supports newer Intel processors.
#
# Example:
# C:   'Intel i7-6500U (4) @ 3.1GHz [27.2°C]'
# F:   'Intel i7-6500U (4) @ 3.1GHz [82.0°F]'
# off: 'Intel i7-6500U (4) @ 3.1GHz'
cpu_temp="C:"

# GPU

# Enable/Disable GPU Brand
#
# Default: 'on'
# Values:  'on', 'off'
# Flag:    --gpu_brand
#
# Example:
# on:  'AMD HD 7950'
# off: 'HD 7950'
gpu_brand="on"

# Which GPU to display
#
# Default: 'all'
# Values:  'all', 'dedicated', 'integrated'
# Flag:    --gpu_type
# Supports: Linux
#
# Example:
# all:
#   GPU1: AMD HD 7950
#   GPU2: Intel Integrated Graphics
#
# dedicated:
#   GPU1: AMD HD 7950
#
# integrated:
#   GPU1: Intel Integrated Graphics
gpu_type="all"

# Resolution

# Display refresh rate next to each monitor
# Default: 'off'
# Values:  'on', 'off'
# Flag:    --refresh_rate
# Supports: Doesn't work on Windows.
#
# Example:
# on:  '1920x1080 @ 60Hz'
# off: '1920x1080'
refresh_rate="on"

# Gtk Theme / Icons / Font

# Shorten output of GTK Theme / Icons / Font
#
# Default: 'off'
# Values:  'on', 'off'
# Flag:    --gtk_shorthand
#
# Example:
# on:  'Numix, Adwaita'
# off: 'Numix [GTK2], Adwaita [GTK3]'
gtk_shorthand="off"

# Enable/Disable gtk2 Theme / Icons / Font
#
# Default: 'on'
# Values:  'on', 'off'
# Flag:    --gtk2
#
# Example:
# on:  'Numix [GTK2], Adwaita [GTK3]'
# off: 'Adwaita [GTK3]'
gtk2="on"

# Enable/Disable gtk3 Theme / Icons / Font
#
# Default: 'on'
# Values:  'on', 'off'
# Flag:    --gtk3
#
# Example:
# on:  'Numix [GTK2], Adwaita [GTK3]'
# off: 'Numix [GTK2]'
gtk3="on"

# IP Address

# Website to ping for the public IP
#
# Default: 'http://ident.me'
# Values:  'url'
# Flag:    --ip_host
public_ip_host="http://ident.me"

# Public IP timeout.
#
# Default: '2'
# Values:  'int'
# Flag:    --ip_timeout
public_ip_timeout=2

# Desktop Environment

# Show Desktop Environment version
#
# Default: 'on'
# Values:  'on', 'off'
# Flag:    --de_version
de_version="on"

# Disk

# Which disks to display.
# The values can be any /dev/sdXX, mount point or directory.
# NOTE: By default we only show the disk info for '/'.
#
# Default: '/'
# Values:  '/', '/dev/sdXX', '/path/to/drive'.
# Flag:    --disk_show
#
# Example:
# disk_show=('/' '/dev/sdb1'):
#      'Disk (/): 74G / 118G (66%)'
#      'Disk (/mnt/Videos): 823G / 893G (93%)'
#
# disk_show=('/'):
#      'Disk (/): 74G / 118G (66%)'
#
disk_show=('/')

# Disk subtitle.
# What to append to the Disk subtitle.
#
# Default: 'mount'
# Values:  'mount', 'name', 'dir', 'none'
# Flag:    --disk_subtitle
#
# Example:
# name:   'Disk (/dev/sda1): 74G / 118G (66%)'
#         'Disk (/dev/sdb2): 74G / 118G (66%)'
#
# mount:  'Disk (/): 74G / 118G (66%)'
#         'Disk (/mnt/Local Disk): 74G / 118G (66%)'
#         'Disk (/mnt/Videos): 74G / 118G (66%)'
#
# dir:    'Disk (/): 74G / 118G (66%)'
#         'Disk (Local Disk): 74G / 118G (66%)'
#         'Disk (Videos): 74G / 118G (66%)'
#
# none:   'Disk: 74G / 118G (66%)'
#         'Disk: 74G / 118G (66%)'
#         'Disk: 74G / 118G (66%)'
disk_subtitle="mount"

# Disk percent.
# Show/Hide disk percent.
#
# Default: 'on'
# Values:  'on', 'off'
# Flag:    --disk_percent
#
# Example:
# on:  'Disk (/): 74G / 118G (66%)'
# off: 'Disk (/): 74G / 118G'
disk_percent="on"

# Song

# Manually specify a music player.
#
# Default: 'auto'
# Values:  'auto', 'player-name'
# Flag:    --music_player
#
# Available values for 'player-name':
#
# amarok
# audacious
# banshee
# bluemindo
# clementine
# cmus
# deadbeef
# deepin-music
# dragon
# elisa
# exaile
# gnome-music
# gmusicbrowser
# gogglesmm
# guayadeque
# io.elementary.music
# iTunes
# juk
# lollypop
# mocp
# mopidy
# mpd
# muine
# netease-cloud-music
# olivia
# playerctl
# pogo
# pragha
# qmmp
# quodlibet
# rhythmbox
# sayonara
# smplayer
# spotify
# strawberry
# tauonmb
# tomahawk
# vlc
# xmms2d
# xnoise
# yarock
music_player="auto"

# Format to display song information.
#
# Default: '%artist% - %album% - %title%'
# Values:  '%artist%', '%album%', '%title%'
# Flag:    --song_format
#
# Example:
# default: 'Song: Jet - Get Born - Sgt Major'
song_format="%artist% - %album% - %title%"

# Print the Artist, Album and Title on separate lines
#
# Default: 'off'
# Values:  'on', 'off'
# Flag:    --song_shorthand
#
# Example:
# on:  'Artist: The Fratellis'
#      'Album: Costello Music'
#      'Song: Chelsea Dagger'
#
# off: 'Song: The Fratellis - Costello Music - Chelsea Dagger'
song_shorthand="off"

# 'mpc' arguments (specify a host, password etc).
#
# Default:  ''
# Example: mpc_args=(-h HOST -P PASSWORD)
mpc_args=()

# Text Colors

# Text Colors
#
# Default:  'distro'
# Values:   'distro', 'num' 'num' 'num' 'num' 'num' 'num'
# Flag:     --colors
#
# Each number represents a different part of the text in
# this order: 'title', '@', 'underline', 'subtitle', 'colon', 'info'
#
# Example:
# colors=(distro)      - Text is colored based on Distro colors.
# colors=(4 6 1 8 8 6) - Text is colored in the order above.
colors=(distro)

# Text Options

# Toggle bold text
#
# Default:  'on'
# Values:   'on', 'off'
# Flag:     --bold
bold="on"

# Enable/Disable Underline
#
# Default:  'on'
# Values:   'on', 'off'
# Flag:     --underline
underline_enabled="on"

# Underline character
#
# Default:  '-'
# Values:   'string'
# Flag:     --underline_char
underline_char="-"

# Info Separator
# Replace the default separator with the specified string.
#
# Default:  ':'
# Flag:     --separator
#
# Example:
# separator="->":   'Shell-> bash'
# separator=" =":   'WM = dwm'
separator=":"

# Color Blocks

# Color block range
# The range of colors to print.
#
# Default:  '0', '15'
# Values:   'num'
# Flag:     --block_range
#
# Example:
#
# Display colors 0-7 in the blocks.  (8 colors)
# neofetch --block_range 0 7
#
# Display colors 0-15 in the blocks. (16 colors)
# neofetch --block_range 0 15
block_range=(0 15)

# Toggle color blocks
#
# Default:  'on'
# Values:   'on', 'off'
# Flag:     --color_blocks
color_blocks="on"

# Color block width in spaces
#
# Default:  '3'
# Values:   'num'
# Flag:     --block_width
block_width=3

# Color block height in lines
#
# Default:  '1'
# Values:   'num'
# Flag:     --block_height
block_height=1

# Color Alignment
#
# Default: 'auto'
# Values: 'auto', 'num'
# Flag: --col_offset
#
# Number specifies how far from the left side of the terminal (in spaces) to
# begin printing the columns, in case you want to e.g. center them under your
# text.
# Example:
# col_offset="auto" - Default behavior of neofetch
# col_offset=7      - Leave 7 spaces then print the colors
col_offset="auto"

# Progress Bars

# Bar characters
#
# Default:  '-', '='
# Values:   'string', 'string'
# Flag:     --bar_char
#
# Example:
# neofetch --bar_char 'elapsed' 'total'
# neofetch --bar_char '-' '='
bar_char_elapsed="-"
bar_char_total="="

# Toggle Bar border
#
# Default:  'on'
# Values:   'on', 'off'
# Flag:     --bar_border
bar_border="on"

# Progress bar length in spaces
# Number of chars long to make the progress bars.
#
# Default:  '15'
# Values:   'num'
# Flag:     --bar_length
bar_length=15

# Progress bar colors
# When set to distro, uses your distro's logo colors.
#
# Default:  'distro', 'distro'
# Values:   'distro', 'num'
# Flag:     --bar_colors
#
# Example:
# neofetch --bar_colors 3 4
# neofetch --bar_colors distro 5
bar_color_elapsed="distro"
bar_color_total="distro"

# Info display
# Display a bar with the info.
#
# Default: 'off'
# Values:  'bar', 'infobar', 'barinfo', 'off'
# Flags:   --cpu_display
#          --memory_display
#          --battery_display
#          --disk_display
#
# Example:
# bar:     '[---=======]'
# infobar: 'info [---=======]'
# barinfo: '[---=======] info'
# off:     'info'
cpu_display="off"
memory_display="off"
battery_display="off"
disk_display="off"

# Backend Settings

# Image backend.
#
# Default:  'ascii'
# Values:   'ascii', 'caca', 'chafa', 'jp2a', 'iterm2', 'off',
#           'pot', 'termpix', 'pixterm', 'tycat', 'w3m', 'kitty'
# Flag:     --backend
image_backend="ascii"

# Image Source
#
# Which image or ascii file to display.
#
# Default:  'auto'
# Values:   'auto', 'ascii', 'wallpaper', '/path/to/img', '/path/to/ascii', '/path/to/dir/'
#           'command output (neofetch --ascii "$(fortune | cowsay -W 30)")'
# Flag:     --source
#
# NOTE: 'auto' will pick the best image source for whatever image backend is used.
#       In ascii mode, distro ascii art will be used and in an image mode, your
#       wallpaper will be used.
# image_source=

# Ascii Options

# Ascii distro
# Which distro's ascii art to display.
#
# Default: 'auto'
# Values:  'auto', 'distro_name'
# Flag:    --ascii_distro
# NOTE: AIX, Alpine, Anarchy, Android, Antergos, antiX, "AOSC OS",
#       "AOSC OS/Retro", Apricity, ArcoLinux, ArchBox, ARCHlabs,
#       ArchStrike, XFerience, ArchMerge, Arch, Artix, Arya, Bedrock,
#       Bitrig, BlackArch, BLAG, BlankOn, BlueLight, bonsai, BSD,
#       BunsenLabs, Calculate, Carbs, CentOS, Chakra, ChaletOS,
#       Chapeau, Chrom*, Cleanjaro, ClearOS, Clear_Linux, Clover,
#       Condres, Container_Linux, CRUX, Cucumber, Debian, Deepin,
#       DesaOS, Devuan, DracOS, DarkOs, DragonFly, Drauger, Elementary,
#       EndeavourOS, Endless, EuroLinux, Exherbo, Fedora, Feren, FreeBSD,
#       FreeMiNT, Frugalware, Funtoo, GalliumOS, Garuda, Gentoo, Pentoo,
#       gNewSense, GNOME, GNU, GoboLinux, Grombyang, Guix, Haiku, Huayra,
#       Hyperbola, janus, Kali, KaOS, KDE_neon, Kibojoe, Kogaion,
#       Korora, KSLinux, Kubuntu, LEDE, LFS, Linux_Lite,
#       LMDE, Lubuntu, Lunar, macos, Mageia, MagpieOS, Mandriva,
#       Manjaro, Maui, Mer, Minix, LinuxMint, MX_Linux, Namib,
#       Neptune, NetBSD, Netrunner, Nitrux, NixOS, Nurunner,
#       NuTyX, OBRevenge, OpenBSD, openEuler, OpenIndiana, openmamba,
#       OpenMandriva, OpenStage, OpenWrt, osmc, Oracle, OS Elbrus, PacBSD,
#       Parabola, Pardus, Parrot, Parsix, TrueOS, PCLinuxOS, Peppermint,
#       popos, Porteus, PostMarketOS, Proxmox, Puppy, PureOS, Qubes, Radix,
#       Raspbian, Reborn_OS, Redstar, Redcore, Redhat, Refracted_Devuan,
#       Regata, Rosa, sabotage, Sabayon, Sailfish, SalentOS, Scientific,
#       Septor, SereneLinux, SharkLinux, Siduction, Slackware, SliTaz,
#       SmartOS, Solus, Source_Mage, Sparky, Star, SteamOS, SunOS,
#       openSUSE_Leap, openSUSE_Tumbleweed, openSUSE, SwagArch, Tails,
#       Trisquel, Ubuntu-Budgie, Ubuntu-GNOME, Ubuntu-MATE, Ubuntu-Studio,
#       Ubuntu, Venom, Void, Obarun, windows10, Windows7, Xubuntu, Zorin,
#       and IRIX have ascii logos
# NOTE: Arch, Ubuntu, Redhat, and Dragonfly have 'old' logo variants.
#       Use '{distro name}_old' to use the old logos.
# NOTE: Ubuntu has flavor variants.
#       Change this to Lubuntu, Kubuntu, Xubuntu, Ubuntu-GNOME,
#       Ubuntu-Studio, Ubuntu-Mate  or Ubuntu-Budgie to use the flavors.
# NOTE: Arcolinux, Dragonfly, Fedora, Alpine, Arch, Ubuntu,
#       CRUX, Debian, Gentoo, FreeBSD, Mac, NixOS, OpenBSD, android,
#       Antrix, CentOS, Cleanjaro, ElementaryOS, GUIX, Hyperbola,
#       Manjaro, MXLinux, NetBSD, Parabola, POP_OS, PureOS,
#       Slackware, SunOS, LinuxLite, OpenSUSE, Raspbian,
#       postmarketOS, and Void have a smaller logo variant.
#       Use '{distro name}_small' to use the small variants.
ascii_distro="auto"

# Ascii Colors
#
# Default:  'distro'
# Values:   'distro', 'num' 'num' 'num' 'num' 'num' 'num'
# Flag:     --ascii_colors
#
# Example:
# ascii_colors=(distro)      - Ascii is colored based on Distro colors.
# ascii_colors=(4 6 1 8 8 6) - Ascii is colored using these colors.
ascii_colors=(distro)

# Bold ascii logo
# Whether or not to bold the ascii logo.
#
# Default: 'on'
# Values:  'on', 'off'
# Flag:    --ascii_bold
ascii_bold="on"

# Image Options

# Image loop
# Setting this to on will make neofetch redraw the image constantly until
# Ctrl+C is pressed. This fixes display issues in some terminal emulators.
#
# Default:  'off'
# Values:   'on', 'off'
# Flag:     --loop
image_loop="off"

# Thumbnail directory
#
# Default: '~/.cache/thumbnails/neofetch'
# Values:  'dir'
thumbnail_dir="${XDG_CACHE_HOME:-${HOME}/.cache}/thumbnails/neofetch"

# Crop mode
#
# Default:  'normal'
# Values:   'normal', 'fit', 'fill'
# Flag:     --crop_mode
#
# See this wiki page to learn about the fit and fill options.
# https://github.com/dylanaraps/neofetch/wiki/What-is-Waifu-Crop%3F
crop_mode="normal"

# Crop offset
# Note: Only affects 'normal' crop mode.
#
# Default:  'center'
# Values:   'northwest', 'north', 'northeast', 'west', 'center'
#           'east', 'southwest', 'south', 'southeast'
# Flag:     --crop_offset
crop_offset="northwest"

# Image size
# The image is half the terminal width by default.
#
# Default: 'auto'
# Values:  'auto', '00px', '00%', 'none'
# Flags:   --image_size
#          --size
image_size='auto'

# Gap between image and text
#
# Default: '3'
# Values:  'num', '-num'
# Flag:    --gap
gap=8

# Image offsets
# Only works with the w3m backend.
#
# Default: '0'
# Values:  'px'
# Flags:   --xoffset
#          --yoffset
yoffset=0
xoffset=2

# Image background color
# Only works with the w3m backend.
#
# Default: ''
# Values:  'color', 'blue'
# Flag:    --bg_color
background_color='color'

# Misc Options

# Stdout mode
# Turn off all colors and disables image backend (ASCII/Image).
# Useful for piping into another command.
# Default: 'off'
# Values: 'on', 'off'
stdout="off"
```
