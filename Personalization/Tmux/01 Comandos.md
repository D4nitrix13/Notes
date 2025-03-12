<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **_Ver la versión de Tmux_**

**Indices:**

- [**_Ver la versión de Tmux_**](#ver-la-versión-de-tmux)
- [**_Iniciar Tmux_**](#iniciar-tmux)
  - [**_Indicar comando por texto_**](#indicar-comando-por-texto)
  - [**_Navegación entre paneles_**](#navegación-entre-paneles)
    - [**_Otros comandos_**](#otros-comandos)
    - [**_Sesiones_**](#sesiones)
    - [**_Listar todas las sesiones_**](#listar-todas-las-sesiones)
    - [**_Adjuntar a la última sesión_**](#adjuntar-a-la-última-sesión)
    - [**_Ventanas_**](#ventanas)
    - [**_Otros comandos:_**](#otros-comandos-1)
    - [**_Activar el modo de ratón_**](#activar-el-modo-de-ratón)
    - [_**Prefijos**_](#prefijos)
    - [_**Funciones de Vinculación**_](#funciones-de-vinculación)
    - [_**Modo de Copia Vi**_](#modo-de-copia-vi)
    - [**_Establecer una opción para todas las sesiones_**](#establecer-una-opción-para-todas-las-sesiones)
    - [**_Obtener una lista completa de comandos_**](#obtener-una-lista-completa-de-comandos)
    - [**_Comandos Especiales_**](#comandos-especiales)
    - [_**Barra de estado**_](#barra-de-estado)
    - [_**Primera forma: Usando el modo de comando de tmux**_](#primera-forma-usando-el-modo-de-comando-de-tmux)
    - [_**Segunda forma: Usando la línea de comandos del sistema**_](#segunda-forma-usando-la-línea-de-comandos-del-sistema)
    - [_**Explicación Adicional: Autocompletado en el Modo de Comando de tmux**_](#explicación-adicional-autocompletado-en-el-modo-de-comando-de-tmux)
    - [_**Ejemplo Práctico**_](#ejemplo-práctico)
    - [**_Recursos adicionales_**](#recursos-adicionales)

> _Para ver la versión de Tmux, ejecuta el siguiente comando:_

```bash
tmux -V
```

# **_Iniciar Tmux_**

> **Para iniciar una nueva sesión de Tmux, simplemente ejecuta `tmux` en tu terminal:**

```bash
tmux
```

```bash
tmux new
```

## **_Indicar comando por texto_**

- _En tmux, el comando `Ctrl-b :` se utiliza para abrir el indicador de comando. Esto te permite introducir comandos de tmux directamente._

- _Por ejemplo, después de presionar `Ctrl-b :`, podrías escribir `split-window` para dividir la ventana actual en dos paneles. O podrías escribir `new-session -s mysession` para crear una nueva sesión llamada "mysession" o usar cualquier otro nombre._

```bash
Ctrl-b :
```

```bash
Ctrl-b new-session -s mysession
```

- _En resumen, `Ctrl-b :` te proporciona una forma de acceder a todas las funcionalidades de tmux directamente desde el teclado, sin tener que usar atajos de teclado específicos para cada comando._

## **_Navegación entre paneles_**

> _*Para moverse entre paneles en Tmux, puedes usar las teclas de dirección o los comandos `{` y `}`._*

```bash
# Moverse al panel de la izquierda
Ctrl-b Left
```

```bash
# Moverse al panel de la izquierda configuracion personal
Ctrl-b h
```

```bash
# Moverse al panel de la derecha
Ctrl-b Right
```

```bash
# Moverse al panel de la derecha configuracion personal
Ctrl-b l
```

```bash
# Moverse al panel de arriba configuracion personal
Ctrl-b Up
```

```bash
# Moverse al panel de arriba configuracion personal
Ctrl-b k
```

```bash
# Moverse al panel de abajo
Ctrl-b Down
```

```bash
# Moverse al panel de abajo configuracion personal
Ctrl-b j
```

```bash
# Moverse al panel anterior
Ctrl-b {
```

```bash
# Moverse al panel siguiente
Ctrl-b }
```

### **_Otros comandos_**

> **Lista de otros comandos útiles en Tmux:**

```bash
# Listar todas las sesiones
Ctrl-b s
```

```bash
# Listar todas las ventanas
Ctrl-b w
```

```bash
# Renombrar la sesión actual
Ctrl-b $
```

```bash
# Cambiar al último panel activo
Ctrl-b ;
```

```bash
# Cambiar al último panel activo configuracion personal
Ctrl-b Tab
```

```bash
# Dividir la ventana verticalmente
Ctrl-b %
```

```bash
# Dividir la ventana horizontalmente
Ctrl-b ""
```

```bash
# Maximizar o restaurar el panel actual
Ctrl-b z
```

```bash
# Rotar los paneles
Ctrl-b Space
```

```bash
# Matar el panel actual
Ctrl-b x
```

```bash
# Entrar en el modo de copia
Ctrl-b [
```

```bash
# Iniciar el modo de copia y mover el cursor para seleccionar el texto a copiar
# Usar Las Teclas Direccionales Para Seleccionar Texto
Space

# Tambien Se Puede Si Tienes Oh-My-Tmux
Ctrl-b Space
```

```bash
# Copiar el texto seleccionado
Enter

# Tambien Se Puede Si Tienes Oh-My-Tmux
Alt-w
```

```bash
# Pegar el texto copiado
Ctrl-b ]
```

```bash
# Mostrar la hora en el panel actual
Ctrl-b t
```

### **_Sesiones_**

- **Crear una nueva sesión**

```bash
tmux new
```

```bash
tmux new-session
```

- **Crear una nueva sesión con un nombre específico**

```bash
tmux new -s mysession
```

```bash
tmux new-session -s mysession
```

- **Adjuntar a una sesión existente o crear una nueva con un nombre específico**

```bash
tmux new-session -A -s mysession
```

- **Matar una sesión específica**

```bash
tmux kill-session -t mysession
```

- **Matar todas las sesiones excepto la actual**

```bash
tmux kill-session -a
```

- **Para eliminar todas las sesiones, ventanas y paneles en tmux, incluyendo la sesión actual**

```bash
tmux kill-server
```

- **Matar todas las sesiones excepto una específica**

```bash
tmux kill-session -a -t mysession
```

- **Desconectar de la sesión actual**

```bash
Ctrl-b d
```

- **Desconectar a otros de la sesión (Maximizar ventana desconectando a otros clientes)**

```bash
tmux attach -d
```

### **_Listar todas las sesiones_**

```bash
tmux ls
```

```bash
tmux list-sessions
```

### **_Adjuntar a la última sesión_**

```bash
tmux a
```

```bash
tmux at
```

```bash
tmux attach
```

```bash
tmux attach-session
```

- _Moverse entre las sesiones de tmux._

- **Te lleva a la sesión anterior.**

```bash
Ctrl-b (
```

- **Te lleva a la siguiente sesión.**

```bash
Ctrl-b )
```

- _Adjuntar a una sesión con un nombre específico_

```bash
tmux attach -t mysession
```

```bash
tmux attach-session -t mysession
```

### **_Ventanas_**

- _Crear una nueva ventana_

```bash
Ctrl-b c
```

- _Renombrar la ventana actual_

```bash
Ctrl-b ,
```

- _Cerrar la ventana actual_

```bash
Ctrl-b &
```

- _Moverse a la ventana anterior_

```bash
Ctrl-b p
```

```bash
# configuracion personal
Ctrl-b Ctrl-h
```

- _Moverse a la siguiente ventana_

```bash
Ctrl-b n
```

```bash
# configuracion personal
Ctrl-b Ctrl-l
```

- _Seleccionar una ventana por su número_

```bash
Ctrl-b 0-9
```

### **_Otros comandos:_**

- _Mostrar todos los atajos de teclado_

```bash
tmux list-keys
```

- _Mostrar información sobre todas las sesiones, ventanas, paneles, etc_

```bash
tmux info
```

### **_Activar el modo de ratón_**

```bash
tmux set -g mouse on
```

```bash
Ctrl-b m
```

- _El comando `Ctrl-b m` en mi configuración de tmux está vinculado a un script que alterna el soporte del ratón en tmux. Cuando el soporte del ratón está activado, puedes usar el ratón para cambiar entre paneles, desplazarte por el historial del panel, cambiar el tamaño de los paneles, etc._

```bash
bind m run "cut -c3- '#{TMUX_CONF}' | sh -s _toggle_mouse"
```

> _Este comando ejecuta un script `_toggle_mouse` que alterna el soporte del ratón. Si el soporte del ratón está desactivado, este comando lo activará, y viceversa._

### _**Prefijos**_

> [!NOTE]
> _Tmux puede ser controlado desde un cliente adjunto utilizando una combinación de teclas, compuesta por una tecla de prefijo seguida de una tecla de comando. Esta configuración utiliza `C-a` como prefijo secundario, mientras que mantiene `C-b` como el prefijo predeterminado. En la siguiente lista de vinculaciones de teclas:_

- **Tmux se controla mediante combinaciones de teclas que consisten en un prefijo seguido de una tecla de comando. Esta configuración usa `C-a` como un prefijo secundario, manteniendo `C-b` como el predeterminado.**

- **`<prefix>`:** _Presiona `Ctrl + a` o `Ctrl + b`_
- **`<prefix> c`:** _Presiona `Ctrl + a` o `Ctrl + b` seguido de `c`_
- **`<prefix> C-c`:** _Presiona `Ctrl + a` o `Ctrl + b` seguido de `Ctrl + c`_

### _**Funciones de Vinculación**_

- **`<prefix> e`:** _Abre el fichero de personalización `.local` con el editor definido por `$EDITOR` (por defecto `vim` cuando está vacío)._
- **`<prefix> r`:** _Recarga la configuración._
- **`C-l`:** _Limpia la pantalla y el historial de tmux._
- **`<prefix> C-c`:** _Crea una nueva sesión._
- **`<prefix> C-f`:** _Cambia a otra sesión por nombre._
- **`<prefix> C-h` y `<prefix> C-l`:** _Navega por las ventanas (las vinculaciones predeterminadas `<prefix> n` y `<prefix> p` están desactivadas)._
- **`<prefix> Tab`:** _Lleva a la última ventana activa._
- **`<prefix> -`:** _Divide el panel actual verticalmente._
- **`<prefix> _`:** _Divide el panel actual horizontalmente._
- **`<prefix> h`, `<prefix> j`, `<prefix> k`, `<prefix> l`:** _Navega por los paneles al estilo Vim._
- **`<prefix> H`, `<prefix> J`, `<prefix> K`, `<prefix> L`:** _Redimensiona los paneles._
- **`<prefix> <` y `<prefix> >`:** _Intercambia paneles._
- **`<prefix> +`:** _Maximiza el panel actual a una nueva ventana._
- **`<prefix> m`:** _Alterna el modo ratón encendido o apagado._
- **`<prefix> U`:** _Lanza Urlscan (preferido) o Urlview, si está disponible._
- **`<prefix> F`:** _Lanza Facebook PathPicker, si está disponible._
- **`<prefix> Enter`:** _Entra en el modo de copia._
- **`<prefix> b`:** _Lista los buffers de pegado._
- **`<prefix> p`:** _Pega desde el buffer de pegado superior._
- **`<prefix> P`:** _Elige el buffer de pegado del cual pegar._

### _**Modo de Copia Vi**_

> [!NOTE]
> **El modo de copia vi está configurado para coincidir con mi propia configuración de Vim. Las vinculaciones son las siguientes:**

- **`v`:** _Comienza la selección / modo visual._
- **`C-v`:** _Alterna entre el modo visual de bloque y el modo visual._
- **`H`:** _Salta al inicio de la línea._
- **`L`:** _Salta al final de la línea._
- **`y`:** _Copia la selección al buffer de pegado superior._
- **`Escape`:** _Cancela la operación actual._

### **_Establecer una opción para todas las sesiones_**

```bash
tmux set -g OPTION
```

- _Establecer una opción para todas las ventanas_

```bash
tmux setw -g OPTION
```

### **_Obtener una lista completa de comandos_**

```bash
man tmux
```

### **_Comandos Especiales_**

> _El comando `join-pane` en Tmux se utiliza para mover un panel de una ventana a otra, esencialmente fusionando las ventanas en una sola con múltiples paneles._

- **La opción `-s` (source) se utiliza para especificar el panel que deseas mover, y la opción `-t` (target) se utiliza para especificar a qué ventana deseas mover el panel.**

```bash
# Mover el panel 1 de la ventana 2 a la ventana 1
tmux join-pane -s 2.1 -t 1
```

1. _En este ejemplo, `2.1` se refiere al panel 1 de la ventana 2, y `1` se refiere a la ventana 1. Después de ejecutar este comando, el panel 1 de la ventana 2 se moverá a la ventana 1._

2. _Si no especificas un número de panel después del punto, Tmux asumirá que quieres mover el panel activo actualmente. Del mismo modo, si no especificas un número de panel para la opción `-t`, Tmux asumirá que quieres mover el panel a la ventana activa actualmente._

```bash
# Mover el panel activo de la ventana 1 a la ventana 2
tmux join-pane -s 1 -t 2
```

### _**Barra de estado**_

- **En tmux, los comandos `set status on` y `set status off` se utilizan para mostrar u ocultar la barra de estado. Aquí están las dos formas de hacerlo:**

### _**Primera forma: Usando el modo de comando de tmux**_

1. **Inicia el modo de comando:**
   - _Presiona `Ctrl + b` para activar el prefijo predeterminado._
   - _Luego presiona `:` para abrir la línea de comandos de tmux._

2. **Ejecuta los comandos:**
   - _Para mostrar la barra de estado, escribe `set status on` y presiona `Enter`._
   - _Para ocultar la barra de estado, escribe `set status off` y presiona `Enter`._

### _**Segunda forma: Usando la línea de comandos del sistema**_

1. **Ejecuta los comandos directamente desde la terminal:**
   - _Para mostrar la barra de estado, escribe `tmux set status on` y presiona `Enter`._
   - _Para ocultar la barra de estado, escribe `tmux set status off` y presiona `Enter`._

- _Ambas formas logran el mismo objetivo, pero la primera se realiza dentro de una sesión activa de tmux, mientras que la segunda se puede hacer desde fuera de la sesión tmux, siempre y cuando tmux esté corriendo y se esté apuntando a la sesión correcta._

### _**Explicación Adicional: Autocompletado en el Modo de Comando de tmux**_

> [!TIP]
> **Cuando utilizas el modo de comando de tmux, también puedes beneficiarte del autocompletado. Aquí te explico cómo funciona:**

1. **Inicia el modo de comando:**
   - _Presiona `Ctrl + b` para activar el prefijo predeterminado._
   - _Luego presiona `:` para abrir la línea de comandos de tmux._

2. **Escribe el comando y usa el autocompletado:**
   - _Comienza a escribir un comando, por ejemplo, `set status`._
   - _Presiona `Tab`. Tmux mostrará una lista de comandos relacionados que comienzan con lo que has escrito. Esto te permite ver todas las opciones disponibles y seleccionar la correcta sin necesidad de recordar el nombre exacto del comando._

### _**Ejemplo Práctico**_

1. **Mostrar la barra de estado:**
   - _Presiona `Ctrl + b` + `:` para abrir la línea de comandos._
   - _Escribe `set stat` y presiona `Tab`. Verás una lista de comandos que comienzan con `set stat`, incluyendo `set status`._
   - _Selecciona `set status on` y presiona `Enter`._

2. **Ocultar la barra de estado:**
   - _Presiona `Ctrl + b` + `:` para abrir la línea de comandos._
   - _Escribe `set stat` y presiona `Tab`. Selecciona `set status off` y presiona `Enter`._

_Con esta función de autocompletado, trabajar con tmux se vuelve más fácil y eficiente, ya que puedes explorar y seleccionar comandos rápidamente sin necesidad de escribirlos por completo._

### **_Recursos adicionales_**

- **[Tmux Cheat Sheet](https://tmuxcheatsheet.com/ "https://tmuxcheatsheet.com/")**
- **[Tmux GitHub](https://github.com/tmux/tmux "https://github.com/tmux/tmux")**
