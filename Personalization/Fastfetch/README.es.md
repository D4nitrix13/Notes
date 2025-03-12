<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***Configuración de Fastfetch para Terminal***

**Autor:** *Daniel Benjamin Pérez Morales*
**GitHub:** *[D4nitrix13](https://github.com/D4nitrix13 "https://github.com/D4nitrix13")*
**Correo:** *`danielperezdev@proton.me`*

*Este fichero de configuración está diseñado para personalizar la salida de Fastfetch, una herramienta que muestra información del sistema en la terminal. Esta configuración se adapta para ser utilizada con el terminal Kitty, debido a la falta de soporte para protocolos de imagen en Alacritty.*

## ***Contenido de la Configuración***

### ***Cargar Imágenes***

```json
"logo": {
  "source": "~/.config/fastfetch/pngs/Ubuntu.png",
  "width": 18
}
```

- **source:** *Ruta de la imagen a mostrar.*
- **width:** *Ancho de la imagen en píxeles.*

### ***Separadores***

```json
"display": {
  "separator": " 󰅂 "
}
```

- **separator:** *Símbolo separador usado entre claves.*

### ***Módulos***

**Cada módulo representa un tipo de información a mostrar en la terminal. Los módulos son configurables y pueden ser personalizados para mostrar diversos datos del sistema. Aquí hay una descripción de algunos de ellos:**

- **Módulo Custom**

  *La secuencia `\u001b[38;5;32m` es una secuencia de escape ANSI utilizada para cambiar el color del texto en la terminal. Esta secuencia específica se desglosa de la siguiente manera:*

  - *`\u001b` es el carácter de escape ANSI, a menudo representado como `ESC` o `\033`.*
  - *`[38;5;32m` es el código de color para establecer el color del texto.*

  *En esta secuencia:*

  - *`38` indica que se está utilizando el modo de color de 256 colores.*
  - *`5` especifica que se está utilizando la paleta de colores de 256 colores.*
  - *`32` es el índice de color en la paleta de 256 colores.*

  *El índice `32` en la paleta de 256 colores corresponde a un color verde en la mayoría de los terminales que soportan esta paleta de colores.*

  *La secuencia `\u001b[0m` se utiliza para restablecer los atributos de color y formato del texto al valor predeterminado. Básicamente, revierte cualquier formato o color aplicado previamente.*

  **En resumen:**

  - **`\u001b[38;5;32m`:** *Cambia el color del texto a verde.*
  - **`\u001b[0m`:** *Restablece el color del texto y otros atributos de formato al valor predeterminado.*

  ```json
  {
    "type": "custom",
    "format": "\u001b[38;5;32m   \u001b[0m 󰅂 \u001b[38;5;32m Tecnology      󰌛              "
  }
  ```

  ```text
  Javascript: nf-dev-javascript
  Python: nf-dev-python
  TypeScript: nf-seti-typescript
  Php: nf-seti-php
  C: nf-custom-c
  C#: nf-md-language_csharp
  Rust: nf-dev-rust
  Lua: nf-seti-lua
  Markdown: nf-fa-markdown
  Html: nf-fa-html5
  Css: nf-fa-css3
  MySQL: nf-fae-mysql
  Makefile: nf-seti-makefile
  MongoDB: nf-dev-mongodb
  Shell: nf-cod-terminal_bash
  npm: nf-dev-npm
  Docker: nf-dev-docker
  Git: nf-dev-git
  Github: nf-cod-github
  Neovim: nf-custom-neovim
  ```

- **Módulo OS (Sistema Operativo)**

  ```json
  {
    "type": "os",
    "key": "   OS",
    "keyColor": "green"
  }
  ```

- **Módulo Kernel**

  ```json
  {
    "type": "kernel",
    "key": "   Kernel",
    "keyColor": "green"
  }
  ```

- **Módulo CPU**

  ```json
  {
    "type": "cpu",
    "key": "  󰻠 CPU",
    "keyColor": "green",
    "showPeCoreCount": true,
    "temp": true
  }
  ```

- **Módulo GPU**

  ```json
  {
    "type": "gpu",
    "key": "   GPU {}",
    "keyColor": "green",
    "driverSpecific": true,
    "temp": true
  }
  ```

- **Módulo Memory (Memoria)**

  ```json
  {
    "type": "memory",
    "key": "  󰍛 Memory",
    "keyColor": "green"
  }
  ```

- **Módulo Font (Fuente)**

  ```json
  {
    "type": "font",
    "key": "   Font",
    "keyColor": "green"
  }
  ```

### ***Secciones Adicionales***

- **Separadores personalizados**

  ```json
  {
    "type": "custom",
    "format": "\u001b[1;36m┌────────────────────────────────────────────────────────────────────────────────────────┐"
  }
  ```

- **Título**

  ```json
  {
    "type": "title",
    "key": "  ",
    "keyColor": "green"
  }
  ```

> [!NOTE]
> *En el contexto de configuraciones de herramientas de línea de comandos como Fastfetch, el uso de `{}` en las claves de configuración se emplea para representar valores dinámicos o variables que se insertarán automáticamente en tiempo de ejecución. Aquí te explico su significado y uso:*

### ***Significado de `{}` en la Configuración***

1. **Marcador de Posición:**
   *`{}` actúa como un marcador de posición en el texto de formato. En lugar de mostrar un valor estático, `{}` indica que el contenido dentro de las llaves será reemplazado por un valor dinámico obtenido durante la ejecución.*

2. **Valores Dinámicos:**
   *Estos valores dinámicos se llenan con información que puede cambiar con el tiempo o variar según el entorno del sistema. Por ejemplo:*
   - *En la sección de `cpuusage`, `{}` se reemplazaría por el porcentaje de uso actual de la CPU.*
   - *En la sección de `monitor`, `{}` se reemplazaría por el número de monitores conectados.*

3. **Ejemplo de Uso:**

   ```json
   {
    "type": "monitor",
    "key": "  󰍺 Monitor {}"
   }
   ```

   *Aquí, el `{}` se reemplaza por el número real de monitores conectados en el sistema. Si el sistema detecta dos monitores, el texto final podría ser "Monitor 2".*

4. **Flexibilidad en la Configuración:**
   *El uso de `{}` permite que las herramientas de línea de comandos adapten su salida a la situación actual sin necesidad de editar el fichero de configuración manualmente. Esto facilita la personalización dinámica basada en el estado del sistema.*

### ***Ejemplo Práctico***

**Considera la siguiente configuración para mostrar el uso de la CPU:**

```json
{
  "type": "cpuusage",
  "key": "  󰻠 CPU Usage {}",
  "keyColor": "green",
  "showPeCoreCount": true
}
```

**En la ejecución, el `{}` en "CPU Usage {}" se reemplazaría por el porcentaje real de uso de la CPU, resultando en algo como "CPU Usage 45%" si el uso de la CPU es del 45%.**

| **Nombre del Icono** | **Visualización** | **Icono**                       |
| -------------------- | ----------------- | ------------------------------- |
| *OS*                 | *``*             | *nf-dev-ubuntu*                 |
| *Kernel*             | *``*             | *nf-dev-linux*                  |
| *Packages*           | *``*             | *nf-oct-package*                |
| *Display*            | *`󰦉`*             | *nf-md-monitor_cellphone*       |
| *Window Manager*     | *``*             | *nf-fa-window_maximize*         |
| *Terminal*           | *``*             | *nf-oct-terminal*               |
| *Host*               | *``*             | *nf-oct-fiscal_host*            |
| *BIOS*               | *``*             | *nf-fa-microchip*               |
| *Boot Manager*       | *``*             | *nf-fa-cogs*                    |
| *Board*              | *``*             | *nf-cod-circuit_board*          |
| *Chassis*            | *`󰪫`*             | *nf-md-desktop_tower_monitor*   |
| *Initsystem*         | *``*             | *nf-cod-server_process*         |
| *Uptime*             | *``*             | *nf-weather-time_4*             |
| *Loadavg*            | *`󰝲`*             | *nf-md-loading*                 |
| *Processes*          | *``*             | *nf-fa-list_check*              |
| *Editor*             | *``*             | *nf-cod-editor_layout*          |
| *Brightness*         | *`󰃝`*             | *nf-md-brightness_4*            |
| *Monitor*            | *`󰍺`*             | *nf-md-monitor_multiple*        |
| *LM*                 | *`󱄄`*             | *nf-md-monitor_shimmer*         |
| *DE*                 | *``*             | *nf-linux-lxqt*                 |
| *WM Theme*           | *`󰔎`*             | *nf-md-theme_light_dark*        |
| *Theme*              | *``*             | *nf-fae-palette_color*          |
| *Icons*              | *``*             | *nf-fa-icons*                   |
| *Font*               | *``*             | *nf-seti-font*                  |
| *Cursor*             | *`󰇀`*             | *nf-md-cursor_default*          |
| *Wallpaper*          | *`󰸉`*             | *nf-md-wallpaper*               |
| *Terminal Font*      | *`󰛖`*             | *nf-md-format_font*             |
| *Terminal Size*      | *``*             | *nf-cod-text_size*              |
| *Terminal Theme*     | *``*             | *nf-dev-terminal_badge*         |
| *User*               | *``*             | *nf-fa-circle_user*             |
| *CPU*                | *`󰻠`*             | *nf-md-cpu_64_bit*              |
| *CPU Cache*          | *``*             | *nf-oct-cache*                  |
| *CPU Usage*          | *`󰱷`*             | *nf-md-application_cog_outline* |
| *GPU*                | *``*             | *nf-oct-cpu*                    |
| *GPU Driver*         | *``*             | *nf-cod-settings_gear*          |
| *Memory*             | *`󰍛`*             | *nf-md-memory*                  |
| *Physical Memory*    | *``*             | *nf-fa-memory*                  |
| *Swap*               | *`󰯍`*             | *nf-md-swap_horizontal_bold*    |
| *Disk*               | *``*             | *nf-fa-floppy_disk*             |
| *Battery*            | *``*             | *nf-fa-battery_full*            |
| *Poweradapter*       | *``*             | *nf-fa-power_off*               |
| *Player*             | *``*             | *nf-oct-browser*                |
| *Media*              | *``*             | *nf-oct-video*                  |
| *Public IP*          | *``*             | *nf-oct-location*               |
| *IPv4*               | *`󰩠`*             | *nf-md-ip_network*              |
| *IPv6*               | *`󰲐`*             | *nf-md-ip_network_outline*      |
| *Mac*                | *`󰒍`*             | *nf-md-server_network*          |
| *Dns*                | *`󰮌`*             | *nf-md-dns_outline*             |
| *Wifi*               | *``*             | *nf-fa-wifi*                    |
| *Datetime*           | *`󰔠`*             | *nf-md-timetable*               |
| *Locale*             | *``*             | *nf-fa-font*                    |
| *Vulkan*             | *``*             | *nf-cod-graph_line*             |
| *OpenGL*             | *``*             | *nf-cod-graph_scatter*          |
| *OpenCL*             | *``*             | *nf-cod-graph*                  |
| *Users*              | *``*             | *nf-fa-user*                    |
| *Bluetooth*          | *``*             | *nf-fa-bluetooth*               |
| *Sound*              | *`󰗅`*             | *nf-md-surround_sound*          |
| *Camera*             | *``*             | *nf-fa-camera_retro*            |
| *Gamepad*            | *``*             | *nf-fa-gamepad*                 |
| *Weather*            | *`󰖐`*             | *nf-md-weather_cloudy*          |
| *Netio*              | *`󰣸`*             | *nf-md-network_strength_3*      |
| *Diskio*             | *`󰋊`*             | *nf-md-harddisk*                |
| *Physical Disk*      | *``*             | *nf-fa-temperature_empty*       |
| *Version*            | *``*             | *nf-oct-versions*               |
| *Colors*             | *`󰌁`*             | *nf-md-invert_colors*           |

### ***Notas Adicionales***

- *La configuración está diseñada para Kitty, ya que Alacritty no soporta protocolos de imagen [Issues](https://github.com/fastfetch-cli/fastfetch/issues/685 "https://github.com/fastfetch-cli/fastfetch/issues/685").*
- *Los íconos usados en la configuración provienen de Nerd Fonts y se pueden ajustar según preferencia.*
- *Se puede personalizar aún más agregando o quitando módulos y ajustando el formato de salida según las necesidades del usuario.*

> [!IMPORTANT]
> *Para más información y ajustes, puedes consultar la [documentación oficial de Fastfetch](https://github.com/fastfetch-cli/fastfetch/ "https://github.com/fastfetch-cli/fastfetch/") y adaptar la configuración a tus necesidades.*
