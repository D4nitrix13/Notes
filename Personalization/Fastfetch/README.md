<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***Fastfetch Configuration for Terminal***

**Author:** *Daniel Benjamin Pérez Morales*  
**GitHub:** *[D4nitrix13](https://github.com/D4nitrix13 "https://github.com/D4nitrix13")*  
**Email:** *`danielperezdev@proton.me`*

*This configuration file is designed to customize the output of Fastfetch, a tool that displays system information in the terminal. This configuration is adapted for use with the Kitty terminal due to the lack of image protocol support in Alacritty.*

## ***Configuration Contents***

### ***Loading Images***

```json
"logo": {
  "source": "~/.config/fastfetch/pngs/Ubuntu.png",
  "width": 18
}
```

- **source:** *Path to the image to display.*
- **width:** *Width of the image in pixels.*

### ***Separators***

```json
"display": {
  "separator": " 󰅂 "
}
```

- **separator:** *Separator symbol used between keys.*

### ***Modules***

**Each module represents a type of information to display in the terminal. Modules are configurable and can be customized to show various system data. Here is a description of some of them:**

- **Custom Module**

  *The sequence `\u001b[38;5;32m` is an ANSI escape sequence used to change the text color in the terminal. This specific sequence is broken down as follows:*

  - *`\u001b` is the ANSI escape character, often represented as `ESC` or `\033`.*
  - *`[38;5;32m` is the color code for setting the text color.*

  *In this sequence:*

  - *`38` indicates that the 256-color mode is being used.*
  - *`5` specifies that the 256-color palette is used.*
  - *`32` is the color index in the 256-color palette.*

  *Index `32` in the 256-color palette corresponds to a green color in most terminals that support this color palette.*

  *The sequence `\u001b[0m` is used to reset the text color and formatting attributes to the default. Essentially, it reverts any previously applied formatting or color.*

  **In summary:**

  - **`\u001b[38;5;32m`:** *Changes the text color to green.*
  - **`\u001b[0m`:** *Resets the text color and other formatting attributes to the default.*

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

- **OS (Operating System) Module**

  ```json
  {
    "type": "os",
    "key": "   OS",
    "keyColor": "green"
  }
  ```

- **Kernel Module**

  ```json
  {
    "type": "kernel",
    "key": "   Kernel",
    "keyColor": "green"
  }
  ```

- **CPU Module**

  ```json
  {
    "type": "cpu",
    "key": "  󰻠 CPU",
    "keyColor": "green",
    "showPeCoreCount": true,
    "temp": true
  }
  ```

- **GPU Module**

  ```json
  {
    "type": "gpu",
    "key": "   GPU {}",
    "keyColor": "green",
    "driverSpecific": true,
    "temp": true
  }
  ```

- **Memory Module**

  ```json
  {
    "type": "memory",
    "key": "  󰍛 Memory",
    "keyColor": "green"
  }
  ```

- **Font Module**

  ```json
  {
    "type": "font",
    "key": "   Font",
    "keyColor": "green"
  }
  ```

### ***Additional Sections***

- **Custom Separators**

  ```json
  {
    "type": "custom",
    "format": "\u001b[1;36m┌────────────────────────────────────────────────────────────────────────────────────────┐"
  }
  ```

- **Title**

  ```json
  {
    "type": "title",
    "key": "  ",
    "keyColor": "green"
  }
  ```

> [!NOTE]
> *In the context of command-line tool configurations like Fastfetch, the use of `{}` in configuration keys is employed to represent dynamic values or variables that will be automatically inserted at runtime. Here’s an explanation of its meaning and use:*

### ***Meaning of `{}` in Configuration***

1. **Placeholder:**
   *`{}` acts as a placeholder in the format text. Instead of displaying a static value, `{}` indicates that the content within the braces will be replaced by a dynamic value obtained during execution.*

2. **Dynamic Values:**
   *These dynamic values are filled with information that can change over time or vary depending on the system environment. For example:*
   - *In the `cpuusage` section, `{}` would be replaced by the current CPU usage percentage.*
   - *In the `monitor` section, `{}` would be replaced by the number of connected monitors.*

3. **Usage Example:**

   ```json
   {
    "type": "monitor",
    "key": "  󰍺 Monitor {}"
   }
   ```

   *Here, `{}` is replaced with the actual number of monitors connected to the system. If the system detects two monitors, the final text might be "Monitor 2".*

4. **Flexibility in Configuration:**
   *The use of `{}` allows command-line tools to adapt their output to the current situation without needing to manually edit the configuration file. This facilitates dynamic customization based on the system's state.*

### ***Practical Example***

**Consider the following configuration to display CPU usage:**

```json
{
  "type": "cpuusage",
  "key": "  󰻠 CPU Usage {}",
  "keyColor": "green",
  "showPeCoreCount": true
}
```

**In execution, the `{}` in "CPU Usage {}" would be replaced by the actual CPU usage percentage, resulting in something like "CPU Usage 45%" if the CPU usage is 45%.**

| **Icon Name**     | **Display** | **Icon**                        |
| ----------------- | ----------- | ------------------------------- |
| *OS*              | *``*       | *nf-dev-ubuntu*                 |
| *Kernel*          | *``*       | *nf-dev-linux*                  |
| *Packages*        | *``*       | *nf-oct-package*                |
| *Display*         | *`󰦉`*       | *nf-md-monitor_cellphone*       |
| *Window Manager*  | *``*       | *nf-fa-window_maximize*         |
| *Terminal*        | *``*       | *nf-oct-terminal*               |
| *Host*            | *``*       | *nf-oct-fiscal_host*            |
| *BIOS*            | *``*       | *nf-fa-microchip*               |
| *Boot Manager*    | *``*       | *nf-fa-cogs*                    |
| *Board*           | *``*       | *nf-cod-circuit_board*          |
| *Chassis*         | *`󰪫`*       | *nf-md-desktop_tower_monitor*   |
| *Initsystem*      | *``*       | *nf-cod-server_process*         |
| *Uptime*          | *``*       | *nf-weather-time_4*             |
| *Loadavg*         | *`󰝲`*       | *nf-md-loading*                 |
| *Processes*       | *``*       | *nf-fa-list_check*              |
| *Editor*          | *``*       | *nf-cod-editor_layout*          |
| *Brightness*      | *`󰃝`*       | *nf-md-brightness_4*            |
| *Monitor*         | *`󰍺`*       | *nf-md-monitor_multiple*        |
| *LM*              | *`󱄄`*       | *nf-md-monitor_shimmer*         |
| *DE*              | *``*       | *nf-linux-lxqt*                 |
| *WM Theme*        | *`󰔎`*       | *nf-md-theme_light_dark*        |
| *Theme*           | *``*       | *nf-fae-palette_color*          |
| *Icons*           | *``*       | *nf-fa-icons*                   |
| *Font*            | *``*       | *nf-seti-font*                  |
| *Cursor*          | *`󰇀`*       | *nf-md-cursor_default*          |
| *Wallpaper*       | *`󰸉`*       | *nf-md-wallpaper*               |
| *Terminal Font*   | *`󰛖`*       | *nf-md-format_font*             |
| *Terminal Size*   | *``*       | *nf-cod-text_size*              |
| *Terminal Theme*  | *``*       | *nf-dev-terminal_badge*         |
| *User*            | *``*       | *nf-fa-circle_user*             |
| *CPU*             | *`󰻠`*       | *nf-md-cpu_64_bit*              |
| *CPU Cache*       | *``*       | *nf-oct-cache*                  |
| *CPU Usage*       | *`󰱷`*       | *nf-md-application_cog_outline* |
| *GPU*             | *``*       | *nf-oct-cpu*                    |
| *GPU Driver*      | *``*       | *nf-cod-settings_gear*          |
| *Memory*          | *`󰍛`*       | *nf-md-memory*                  |
| *Physical Memory* | *``*       | *nf-fa-memory*                  |
| *Swap*            | *`󰯍`*       | *nf-md-swap_horizontal_bold*    |
| *Disk*            | *``*       | *nf-fa-floppy_disk*             |
| *Battery*         | *``*       | *nf-fa-battery_full*            |
| *Poweradapter*    | *``*       | *nf-fa-power_off*               |
| *Player*          | *``*       | *nf-oct-browser*                |
| *Media*           | *``*       | *nf-oct-video*                  |
| *Public IP*       | *``*       | *nf-oct-location*               |
| *IPv4*            | *`󰩠`*       | *nf-md-ip_network*              |
| *IPv6*            | *`󰲐`*       | *nf-md-ip_network_outline*      |
| *Mac*             | *`󰒍`*       | *nf-md-server_network*          |
| *Dns*             | *`󰮌`*       | *nf-md-dns_outline*             |
| *Wifi*            | *``*       | *nf-fa-wifi*                    |
| *Datetime*        | *`󰔠`*       | *nf-md-timetable*               |
| *Locale*          | *``*       | *nf-fa-font*                    |
| *Vulkan*          | *``*       | *nf-cod-graph_line*             |
| *OpenGL*          | *``*       | *nf-cod-graph_scatter*          |
| *OpenCL*          | *``*       | *nf-cod-graph*                  |
| *Users*           | *``*       | *nf-fa-user*                    |
| *Bluetooth*       | *``*       | *nf-fa-bluetooth*               |
| *Sound*           | *`󰗅`*       | *nf-md-surround_sound*          |
| *Camera*          | *``*       | *nf-fa-camera_retro*            |
| *Gamepad*         | *``*       | *nf-fa-gamepad*                 |
| *Weather*         | *`󰖐`*       | *nf-md-weather_cloudy*          |
| *Netio*           | *`󰣸`*       | *nf-md-network_strength_3*      |
| *Diskio*          | *`󰋊`*       | *nf-md-harddisk*                |
| *Physical Disk*   | *``*       | *nf-fa-temperature_empty*       |
| *Version*         | *``*       | *nf-oct-versions*               |
| *Colors*          | *`󰌁`*       | *nf-md-invert_colors*           |

### ***Additional Notes***

- *The configuration is designed for Kitty, as Alacritty does not support image protocols [Issues](https://github.com/fastfetch-cli/fastfetch/issues/685 "https://github.com/fastfetch-cli/fastfetch/issues/685").*
- *The icons used in the configuration come from Nerd Fonts and can be adjusted according to preference.*
- *Further customization can be done by adding or removing modules and adjusting the output format according to user needs.*

> [!IMPORTANT]
> *For more information and adjustments, you can consult the [official Fastfetch documentation](https://github.com/fastfetch-cli/fastfetch/ "https://github.com/fastfetch-cli/fastfetch/") and adapt the configuration to your needs.*
