<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Configuración Recomendada de Fastfetch***

*Fastfetch es una herramienta de línea de comandos para mostrar información sobre tu sistema, como la distribución de Linux, el entorno de escritorio, el kernel y otros detalles relevantes, de una manera rápida y visualmente atractiva.*

1. **Fichero de Configuración Principal:**
   - *La configuración de Fastfetch se encuentra en el fichero `~/.config/fastfetch/config.jsonc`. Este fichero controla la apariencia y el contenido de la información que se muestra.*

```json
{
  "logo": {
    "source": "~/.config/fastfetch/pngs/Ubuntu.png",
    "height": 18
  },
  "display": {
    "separator": " : "
  },
  "modules": [
    {
      "type": "custom",
      "format": "\u001b[36m    I use Ubuntu"
    },
    {
      "type": "custom",
      "format": "\u001b[1;36m┌───────────────────────────────────────────────────────┐"
    },
    {
      "type": "os",
      "key": "   OS",
      "keyColor": "red"
    },
    {
      "type": "kernel",
      "key": "   Kernel",
      "keyColor": "red"
    },
    {
      "type": "packages",
      "key": "   Packages",
      "keyColor": "green"
    },
    {
      "type": "display",
      "key": "  󰦉 Display",
      "keyColor": "green"
    },
    {
      "type": "wm",
      "key": "   Window Manager",
      "keyColor": "yellow"
    },
    {
      "type": "terminal",
      "key": "   Terminal",
      "keyColor": "yellow"
    },
    {
      "type": "custom",
      "format": "\u001b[1;36m└───────────────────────────────────────────────────────┘"
    },
    "break",
    {
      "type": "title",
      "key": "  "
    },
    {
      "type": "custom",
      "format": "\u001b[1;36m┌───────────────────────────────────────────────────────┐"
    },
    {
      "type": "cpu",
      "format": "{1}",
      "key": "  󰻠 CPU",
      "keyColor": "blue"
    },
    {
      "type": "gpu",
      "key": "   GPU",
      "keyColor": "blue"
    },
    {
      "type": "gpu",
      "format": "{3}",
      "key": "   GPU Driver",
      "keyColor": "magenta"
    },
    {
      "type": "memory",
      "key": "  󰍛 Memory",
      "keyColor": "magenta"
    },
    {
      "type": "custom",
      "format": "\u001b[1;36m└───────────────────────────────────────────────────────┘"
    },
    "break",
    {
      "type": "colors",
      "paddingLeft": 2,
      "symbol": "circle"
    },
    "break"
  ]
}
```
