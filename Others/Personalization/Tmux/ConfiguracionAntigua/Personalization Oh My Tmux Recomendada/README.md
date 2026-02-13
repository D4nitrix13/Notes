# ***Configuración de tmux***

* *Este README explica cada línea de mi configuración personalizada de tmux. La configuración incluye ajustes básicos, uso del portapapeles del sistema, y personalización de la barra de estado con iconos y otros detalles.*

## ***Instalación de Oh-My-Tmux***

**Indices:**

* [***Configuración de tmux***](#configuración-de-tmux)
  * [***Instalación de Oh-My-Tmux***](#instalación-de-oh-my-tmux)
    * [***Prerrequisitos***](#prerrequisitos)
  * [***Paso 1: Clonar el repositorio***](#paso-1-clonar-el-repositorio)
    * [***Paso 2: Enlazar el fichero de configuración***](#paso-2-enlazar-el-fichero-de-configuración)
      * [***Paso 3: Copiar el fichero local de configuración***](#paso-3-copiar-el-fichero-local-de-configuración)
      * [***Uso***](#uso)
  * [***Configuración Básica***](#configuración-básica)
    * [***Personalización de la Barra de Estado***](#personalización-de-la-barra-de-estado)
      * [***Iconos Utilizados***](#iconos-utilizados)
      * [***Configuración de la Barra de Estado***](#configuración-de-la-barra-de-estado)
      * [***Intervalo de Actualización y Símbolos de Batería***](#intervalo-de-actualización-y-símbolos-de-batería)
    * [***Otras Configuraciones***](#otras-configuraciones)

> *Oh-My-Tmux es un marco de configuración para tmux que mejora su interfaz y usabilidad. Sigue estos pasos para instalarlo:*

---

### ***Prerrequisitos***

> *Antes de instalar Oh-My-Tmux, necesitas tener tmux instalado en tu sistema. Aquí te mostramos cómo hacerlo en Debian/Ubuntu y MacOS:*

```bash
# Debian/Ubuntu
sudo apt-get -y install tmux
```

```bash
# Arch Linux
sudo pacman -Syu --noconfirm tmux
```

```bash
# MacOS
brew install tmux
```

***Instalación***

---

## ***Paso 1: Clonar el repositorio***

**Clona el repositorio de Oh-My-Tmux en tu directorio de inicio con el siguiente comando:**

```bash
cd ~/
```

```bash
git clone https://github.com/gpakosz/.tmux.git --depth=1
```

### ***Paso 2: Enlazar el fichero de configuración***

> *Enlaza el fichero de configuración de tmux proporcionado por Oh-My-Tmux:*

```bash
ln -sf .tmux/.tmux.conf
```

```bash
ln -s -f .tmux/.tmux.conf
```

```bash
ln --symbolic --force .tmux/.tmux.conf
```

```bash
ln -s --force .tmux/.tmux.conf
```

```bash
ln --symbolic -f .tmux/.tmux.conf
```

* *El comando `ln -s -f` se utiliza para crear un enlace simbólico a un fichero o directorio. La opción `-s` significa "simbólico" y `-f` significa "forzar". En su forma no abreviada, el comando sería `ln --symbolic --force`.*

* *El comando `ln -s -f .tmux/.tmux.conf` crea un enlace simbólico en el directorio actual que apunta al fichero `.tmux.conf` en el directorio `.tmux`. Si ya existe un fichero llamado `.tmux.conf` en el directorio actual, la opción `--force` hace que `ln` lo sobrescriba.*

---

#### ***Paso 3: Copiar el fichero local de configuración***

> *Copia el fichero `.tmux.conf.local` en tu directorio de inicio o `/home`. Este fichero te permite personalizar tu configuración de tmux:*

```bash
cp .tmux/.tmux.conf.local .
```

```bash
cp ./.tmux/.tmux.conf.local ./
```

```bash
cp ~/.tmux/.tmux.conf.local ~/
```

---

#### ***Uso***

* *Inicia una nueva sesión de tmux y deberías ver la nueva configuración. Si ya tienes una sesión de tmux abierta, puedes recargar la configuración con el siguiente comando:*

```bash
tmux source-file ~/.tmux.conf
```

## ***Configuración Básica***

```bash
set -g base-index 1              # empezar a indexar ventanas desde 1 en lugar de 0
set -g detach-on-destroy off     # no salir de tmux al cerrar una sesión
set -g escape-time 0             # eliminar el retraso de tiempo de escape
set -g renumber-windows on       # renumerar todas las ventanas cuando se cierra una ventana
set -g set-clipboard on          # usar el portapapeles del sistema
set -g default-terminal "${TERM}"
```

* **`set -g base-index 1`:** *Comienza a indexar las ventanas desde 1 en lugar de 0.*
* **`set -g detach-on-destroy off`:** *No salir de tmux al cerrar una sesión, permite mantener tmux activo.*
* **`set -g escape-time 0`:** *Elimina el retraso de tiempo de escape, mejorando la respuesta de teclas.*
* **`set -g renumber-windows on`:** *Renumera todas las ventanas automáticamente cuando se cierra una ventana.*
* **`set -g set-clipboard on`:** *Usa el portapapeles del sistema para copiar y pegar entre tmux y el sistema operativo.*
* **`set -g default-terminal "${TERM}"`:** *Configura el terminal predeterminado en tmux para que coincida con el terminal actual.*

### ***Personalización de la Barra de Estado***

#### ***Iconos Utilizados***

**Página de iconos musicales: [emojiterra.com/guitar](https://emojiterra.com/guitar/ "https://emojiterra.com/guitar/")**

* **``** *-> nf-fa-guitar*
* **`󰭖`** *-> nf-md-account_clock*
* **``** *-> nf-fa-user*
* **``** *-> nf-weather-time_1*
* **``** *-> nf-cod-calendar*
* **``** *-> nf-pl-hostname*

#### ***Configuración de la Barra de Estado***

```bash
tmux_conf_theme_status_left="  #S | 󰭖#{?uptime_y, #{uptime_y}y,}#{?uptime_d, #{uptime_d}d,}#{?uptime_h, #{uptime_h}h,}#{?uptime_m, #{uptime_m}m,} "
tmux_conf_theme_status_right=" #{prefix}#{mouse}#{pairing}#{synchronized}#{?battery_status,#{battery_status},}#{?battery_bar, #{battery_bar},}#{?battery_percentage, #{battery_percentage},} |  %H:%M:%S |  %d %b %Y |  #{username}#{root} |  #{hostname} "
```

* **`tmux_conf_theme_status_left`:** *Define la parte izquierda de la barra de estado con iconos y el tiempo de actividad.*
  * **`#S`:** *Nombre de la sesión.*
  * `󰭖#{?uptime_y, #{uptime_y}y,}#{?uptime_d, #{uptime_d}d,}#{?uptime_h, #{uptime_h}h,}#{?uptime_m, #{uptime_m}m,}`:** *Tiempo de actividad del sistema en años, días, horas y minutos.*

* **`tmux_conf_theme_status_right`:** *Define la parte derecha de la barra de estado con varios indicadores.*
  * **`#{prefix}#{mouse}#{pairing}#{synchronized}`:** *Indicadores de estado de tmux (prefijo, mouse, emparejamiento y sincronización).*
  * **`#{?battery_status,#{battery_status},}#{?battery_bar, #{battery_bar},}#{?battery_percentage, #{battery_percentage},}`:** *Estado, barra y porcentaje de la batería.*
  * **`|  %H:%M:%S |  %d %b %Y |  #{username}#{root} |  #{hostname}`:** *Hora actual, fecha, nombre de usuario y nombre del host con iconos.*

#### ***Intervalo de Actualización y Símbolos de Batería***

```bash
set -g status-interval 1

tmux_conf_battery_status_charging="🔌"     # U+1F50C
tmux_conf_battery_status_discharging="🔋"  # U+1F50B
```

* **`set -g status-interval 1`:** *Configura el intervalo de actualización de la barra de estado a 1 segundo.*
* **`tmux_conf_battery_status_charging="🔌"`:** *Símbolo para la batería cargándose.*
* **`tmux_conf_battery_status_discharging="🔋"`:** *Símbolo para la batería descargándose.*

### ***Otras Configuraciones***

```bash
set -g history-limit 1000000
set -g mouse on
set -g status-position top
```

* **`set -g history-limit 1000000`:** *Aumenta el tamaño del historial de comandos a 1,000,000 líneas.*
* **`set -g mouse on`:** *Activa el modo mouse al iniciar tmux.*
* **`set -g status-position top`:** *Mueve la barra de estado a la parte superior de la ventana.*

**Esta configuración personalizada mejora la usabilidad y estética de tmux, facilitando su uso diario con características avanzadas y un estilo visual atractivo.**
