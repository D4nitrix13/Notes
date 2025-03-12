<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***Descripción del Fichero de Configuración***

- *Ubicacion del fichero (`~/.config/lazygit/config.yml`) contiene la configuración personalizada para lazygit.*

## ***Documentación de Configuración de `lazygit`***

> [!NOTE]
> *`lazygit` es una herramienta de interfaz de usuario para Git que simplifica la gestión de repositorios desde la línea de comandos. La configuración de `lazygit` puede personalizarse extensamente a través de su fichero de configuración. A continuación se explica cada opción de configuración con detalle.*

### ***Configuración de la GUI***

```yaml
gui:
  authorColors: {}
  branchColors: {}
  scrollHeight: 2
  scrollPastBottom: true
  mouseEvents: true
  nerdFontsVersion: "3"
  skipDiscardChangeWarning: false
  skipStashWarning: false
  sidePanelWidth: 0.3333
  expandFocusedSidePanel: false
  mainPanelSplitMode: flexible
  language: auto
  timeFormat: 02 Jan 06 15:04:05 MST
  commitLength:
    show: true
  skipNoStagedFilesWarning: false
  showListFooter: true
  showFileTree: true
  showRandomTip: true
  showCommandLog: true
  showBottomLine: true
  commandLogSize: 8
  splitDiff: auto
```

### ***`authorColors`***

- **Descripción:** *Configuración para los colores asociados a los autores en las vistas de `lazygit`. Actualmente, está configurado como un diccionario vacío, lo que significa que no se aplican colores personalizados a los autores.*
- **Uso:** *Puedes definir colores específicos para los nombres de los autores si deseas una representación visual diferenciada.*

### ***`branchColors`***

- **Descripción:** *Configuración para los colores asociados a las ramas en las vistas de `lazygit`. Al igual que `authorColors`, está definido como un diccionario vacío, indicando que no hay colores personalizados aplicados a las ramas.*
- **Uso:** *Define colores específicos para las ramas para facilitar su identificación visual.*

### ***`scrollHeight`***

- **Descripción:** *Define la altura de la región de desplazamiento (scroll) en la interfaz de `lazygit`. Está configurada en `2`, lo que ajusta la altura de las barras de desplazamiento.*
- **Uso:** *Ajusta el valor para cambiar la altura de la barra de desplazamiento según tus preferencias visuales.*

### ***`scrollPastBottom`***

- **Descripción:** *Esta opción, cuando está habilitada (`true`), permite desplazarse más allá del final del contenido en la vista. Esto puede ser útil para obtener una vista más completa del historial o listas.*
- **Uso:** *Deja en `true` para permitir un desplazamiento adicional después del final del contenido.*

### ***`mouseEvents`***

- **Descripción:** *Activa o desactiva los eventos del ratón (`true` para activarlos). Cuando está habilitado, puedes interactuar con la interfaz de `lazygit` usando el ratón.*
- **Uso:** *Establece en `true` para habilitar la interacción con el ratón.*

### ***`nerdFontsVersion`***

- **Descripción:** *Define la versión de Nerd Fonts utilizada para los íconos en `lazygit`. En este caso, se está utilizando la versión `"3"`.*
- **Uso:** *Asegúrate de que la versión especificada coincida con la versión de los Nerd Fonts instalados en tu sistema.*

### ***`skipDiscardChangeWarning`***

- **Descripción:** *Controla si se omite la advertencia al descartar cambios. Cuando está en `false`, se mostrará una advertencia antes de descartar cambios.*
- **Uso:** *Configura en `true` para omitir la advertencia y realizar descartar cambios sin confirmación.*

### ***`skipStashWarning`***

- **Descripción:** *Controla si se omite la advertencia al hacer un stash (guardar cambios temporales). En `false`, se mostrará una advertencia antes de realizar el stash.*
- **Uso:** *Configura en `true` para evitar la advertencia al hacer un stash.*

### ***`sidePanelWidth`***

- **Descripción:** *Define el ancho del panel lateral en relación con el ancho total de la ventana. Configurado en `0.3333`, lo que significa que el panel lateral ocupará aproximadamente un tercio del ancho total.*
- **Uso:** *Ajusta el valor para cambiar el ancho del panel lateral según tus preferencias.*

### ***`expandFocusedSidePanel`***

- **Descripción:** *Controla si el panel lateral enfocado se expande automáticamente. Cuando está en `false`, el panel lateral no se expandirá automáticamente al ser enfocado.*
- **Uso:** *Configura en `true` si deseas que el panel lateral se expanda automáticamente cuando se enfoque.*

### ***`mainPanelSplitMode`***

- **Descripción:** *Define el modo de división del panel principal. En este caso, está configurado como `flexible`, permitiendo que el panel principal se ajuste dinámicamente en tamaño.*
- **Uso:** *Cambia a `fixed` si prefieres un tamaño de panel principal constante.*

### ***`language`***

- **Descripción:** *Establece el idioma de la interfaz. La opción `auto` permite que `lazygit` detecte automáticamente el idioma basado en la configuración del sistema.*
- **Uso:** *Deja en `auto` para el ajuste automático o especifica un idioma concreto si prefieres una configuración fija.*

### ***`timeFormat`***

- **Descripción:** *Define el formato de la hora en la interfaz de `lazygit`. En este caso, se usa el formato `02 Jan 06 15:04:05 MST` para mostrar las fechas y horas.*
- **Uso:** *Modifica el formato según tus preferencias de visualización de la hora.*

```yaml
timeFormat: 02 Jan 06 15:04:05 MST
```

### ***Explicación del Formato***

- `02` *- Día del mes (día numérico de 2 dígitos)*
- `Jan` *- Nombre del mes (abreviado a 3 letras)*
- `06` *- Año (últimos 2 dígitos del año)*
- `15` *- Hora (en formato de 24 horas, de 2 dígitos)*
- `04` *- Minutos (de 2 dígitos)*
- `05` *- Segundos (de 2 dígitos)*
- `MST` *- Zona horaria (abreviatura de la zona horaria)*

### ***`commitLength`***

- **Descripción:** *Controla la longitud de la visualización de los mensajes de commit. Cuando está configurado con `show: true`, se mostrarán mensajes de commit completos.*
- **Uso:** *Establece en `true` para mostrar los mensajes de commit en su longitud completa.*

### ***`skipNoStagedFilesWarning`***

- **Descripción:** *Configura si se omite la advertencia cuando no hay ficheros preparados para commit. En `false`, se mostrará una advertencia si no hay ficheros listos para commit.*
- **Uso:** *Cambia a `true` para evitar la advertencia en casos donde no hay ficheros preparados.*

### ***`showListFooter`***

- **Descripción:** *Indica si se debe mostrar el pie de página en las listas. Configurado en `true`, se mostrará un pie de página en las vistas de lista.*
- **Uso:** *Mantén en `true` para mostrar el pie de página.*

### ***`showFileTree`***

- **Descripción:** *Controla si se debe mostrar el árbol de ficheros en la interfaz. Cuando está en `true`, se mostrará el árbol de ficheros.*
- **Uso:** *Configura en `true` para habilitar la visualización del árbol de ficheros.*

### ***`showRandomTip`***

- **Descripción:** *Activa o desactiva la visualización de consejos aleatorios. Configurado en `true`, se mostrarán consejos aleatorios para mejorar la experiencia con `lazygit`.*
- **Uso:** *Mantén en `true` para recibir consejos útiles.*

### ***`showCommandLog`***

- **Descripción:** *Controla si se debe mostrar el registro de comandos ejecutados. En `true`, se mostrará un registro de los comandos que has ejecutado.*
- **Uso:** *Configura en `true` para tener un historial de comandos visible.*

### ***`showBottomLine`***

- **Descripción:** *Define si se debe mostrar una línea en la parte inferior de la interfaz. En `true`, se mostrará una línea en la parte inferior para mejorar la visualización.*
- **Uso:** *Establece en `true` para una línea de separación en la parte inferior.*

### ***`commandLogSize`***

- **Descripción:** *Define el tamaño del registro de comandos en número de entradas. Configurado en `8`, se mostrarán las últimas 8 entradas en el registro de comandos.*
- **Uso:** *Ajusta el valor para aumentar o disminuir el número de entradas visibles en el registro.*

### ***`splitDiff`***

- **Descripción:** *Controla el modo de división de las diferencias de ficheros. La opción `auto` ajustará automáticamente la visualización de las diferencias según el contenido.*
- **Uso:** *Establece en `manual` si prefieres controlar cómo se dividen las diferencias.*

### ***Configuración de Git en `lazygit`***

> [!NOTE]
> *La configuración de Git en `lazygit` permite personalizar cómo se manejan las operaciones de Git desde la interfaz de `lazygit`. A continuación se describen las opciones disponibles y cómo afectan el comportamiento de la herramienta.*

### ***Configuración de Git***

```yaml
git:
  paging:
    colorArg: always
    pager: delta --dark --paging=never
    useConfig: false
  commit:
    signOff: false
  merging:
    manualCommit: false
    args: ""
  skipHookPrefix: WIP
  autoFetch: true
  autoRefresh: true
  branchLogCmd: git log --graph --color=always --abbrev-commit --decorate --date=relative --pretty=medium {{branchName}} --
  allBranchesLogCmd: git log --graph --all --color=always --abbrev-commit --decorate --date=relative --pretty=medium
  overrideGpg: false
  disableForcePushing: false
  commitPrefixes: {}
  parseEmoji: false
```

### ***`paging`***

- **`colorArg:`** `always`
  - **Descripción:** *Define si los comandos de Git deben siempre aplicar colores en la salida. Configurado como `always`, todos los comandos aplicarán color a la salida para una mejor visualización.*
  - **Uso:** *Mantén en `always` para asegurar que la salida de Git siempre use colores.*

- **`pager:`** `delta --dark --paging=never`
  - **Descripción:** *Especifica el programa de paginación que se usará para mostrar la salida de los comandos de Git. En este caso, se usa `delta` con opciones para un tema oscuro y sin paginación.*
  - **Uso:** *Asegúrate de tener `delta` instalado y configurado para personalizar la visualización de las diferencias en Git.*
  - *[Guia Instalacion](https://dandavison.github.io/delta/installation.html "https://dandavison.github.io/delta/installation.html")*
  - **Instalacion Ubuntu:** *`sudo apt-get install -y git-delta`*
  - **Instalacion Arch Linux:** *`sudo pacman -Syu --no-confirm git-delta`*

- **`useConfig:`** `false`
  - **Descripción:** *Controla si se deben usar las configuraciones de paginación de Git. Cuando está en `false`, `lazygit` no usará la configuración de paginación definida en el fichero de configuración global de Git.*
  - **Uso:** *Mantén en `false` si prefieres la configuración de paginación definida en `lazygit`.*

### ***`commit`***

- **`signOff:`** `false`
  - **Descripción:** *Indica si se debe agregar una firma de confirmación al commit. Cuando está en `false`, no se añadirá automáticamente una firma (`Signed-off-by`) a los commits.*
  - **Uso:** *Establece en `true` si deseas agregar automáticamente una firma a cada commit.*

### ***`merging`***

- **`manualCommit:`** `false`
  - **Descripción:** *Determina si se requiere una confirmación manual para completar un merge. En `false`, los merges se completarán automáticamente sin necesidad de confirmación manual.*
  - **Uso:** *Cambia a `true` si prefieres revisar y confirmar manualmente los merges.*

- **`args:`** `""`
  - **Descripción:** *Especifica argumentos adicionales para los comandos de merge. Actualmente está vacío, indicando que no se pasarán argumentos adicionales.*
  - **Uso:** *Añade argumentos específicos si necesitas personalizar el comportamiento del merge.*

### ***`skipHookPrefix`***

- **Descripción:** *Define un prefijo para los commits que se deben omitir en los hooks de Git. En este caso, se omiten los commits que comienzan con el prefijo `WIP` (Work In Progress).*
- **Uso:** *Cambia el prefijo si necesitas omitir commits con otros prefijos en los hooks.*

### ***`autoFetch`***

- **Descripción:** *Controla si `lazygit` debe realizar automáticamente un fetch de los cambios. Configurado en `true`, se realizará un fetch automático para mantener los datos actualizados.*
- **Uso:** *Mantén en `true` para asegurar que tus datos estén siempre sincronizados con el repositorio remoto.*

### ***`autoRefresh`***

- **Descripción:** *Indica si `lazygit` debe actualizarse automáticamente cuando se detecten cambios. En `true`, la interfaz se actualizará automáticamente para reflejar los cambios recientes.*
- **Uso:** *Mantén en `true` para obtener una visualización actualizada sin tener que refrescar manualmente.*

### ***`branchLogCmd`***

- **Descripción:** *Define el comando para mostrar el historial de commits de una rama específica. Usa `git log` con opciones para un formato gráfico, colores, y fechas relativas.*
- **Uso:** *Modifica el comando si necesitas ajustar el formato o la información mostrada en el historial de una rama específica.*

### ***`allBranchesLogCmd`***

- **Descripción:** *Define el comando para mostrar el historial de commits en todas las ramas. Similar a `branchLogCmd`, pero incluye todos los commits de todas las ramas.*
- **Uso:** *Ajusta el comando según tus necesidades para ver el historial combinado de todas las ramas.*

### ***`overrideGpg`***

- **Descripción:** *Controla si `lazygit` debe anular la configuración de GPG para los commits. En `false`, se usará la configuración de GPG definida en Git.*
- **Uso:** *Establece en `true` si prefieres que `lazygit` ignore la configuración de GPG y use otra configuración.*

### ***`disableForcePushing`***

- **Descripción:** *Indica si se debe deshabilitar la opción de hacer push con `--force`. Configurado en `false`, permite hacer push con `--force`.*
- **Uso:** *Cambia a `true` para evitar accidentalmente forzar el push a los repositorios remotos.*

### ***`commitPrefixes`***

- **Descripción:** *Permite definir prefijos específicos para los mensajes de commit. Actualmente está vacío, indicando que no se aplican prefijos personalizados.*
- **Uso:** *Añade prefijos si deseas aplicar convenciones de mensajes de commit específicas.*

### ***`parseEmoji`***

- **Descripción:** *Controla si se deben analizar y mostrar emojis en los mensajes de commit. En `false`, los emojis no se analizarán ni se mostrarán.*
- **Uso:** *Establece en `true` si deseas que los emojis en los mensajes de commit se interpreten y muestren.*

### ***`log.order`***

- **Descripción:** *Define el orden en que se muestran los commits en el log. `topo-order` asegura que los commits se visualicen respetando la topología del gráfico de commits.*
- **Uso:** *Mantén en `topo-order` para preservar la estructura lógica de la historia del repositorio.*

### ***`log.showGraph`***

- **Descripción:** *Controla si se debe mostrar el gráfico de commits en el log. `always` indica que el gráfico se mostrará siempre.*
- **Uso:** *Deja en `always` si deseas ver el gráfico en todas las visualizaciones de logs.*

### ***`log.showWholeGraph`***

- **Descripción:** *Determina si se debe mostrar el gráfico completo de commits. En `false`, sólo se mostrará una parte relevante del gráfico.*
- **Uso:** *Mantén en `false` para evitar ver un gráfico excesivamente largo y enfocarte en la parte relevante.*

### ***`update.method`***

- **Descripción:** *Especifica el método para recibir actualizaciones de `lazygit`. `prompt` solicitará confirmación antes de actualizar.*
- **Uso:** *Mantén en `prompt` para recibir notificaciones antes de aplicar actualizaciones.*

### ***`update.days`***

- **Descripción:** *Define el intervalo de días para verificar actualizaciones. `14` días significa que `lazygit` verificará nuevas versiones cada dos semanas.*
- **Uso:** *Puedes ajustar este valor según la frecuencia con la que desees buscar actualizaciones.*

### ***`refresher.refreshInterval`***

- **Descripción:** *Establece el intervalo de tiempo (en segundos) para actualizar la interfaz de `lazygit`. `10` segundos asegura que los datos se actualicen regularmente.*
- **Uso:** *Ajusta el valor según la frecuencia con la que prefieras actualizar la interfaz.*

### ***`refresher.fetchInterval`***

- **Descripción:** *Determina el intervalo (en segundos) para realizar un fetch automático de los cambios en el repositorio remoto. `60` segundos asegura que los cambios se sincronicen de manera constante.*
- **Uso:** *Puedes incrementar este intervalo si deseas menos frecuencia en las actualizaciones automáticas.*

### ***`confirmOnQuit`***

- **Descripción:** *Controla si se debe pedir confirmación al salir de `lazygit`. En `false`, `lazygit` se cerrará inmediatamente sin solicitar confirmación.*
- **Uso:** *Deja en `false` si prefieres salir rápidamente sin confirmación.*

### ***`quitOnTopLevelReturn`***

- **Descripción:** *Indica si `lazygit` debe cerrarse automáticamente al retornar al nivel superior del repositorio. En `false`, no se cerrará automáticamente.*
- **Uso:** *Establece en `true` si deseas que `lazygit` se cierre automáticamente al salir del nivel superior.*

### ***`keybinding.universal.quit`***

- **Descripción:** *Define la tecla de atajo para salir de `lazygit`. `q` es la tecla predeterminada para esta acción.*
- **Uso:** *Usa `q` para cerrar `lazygit` rápidamente.*

### ***`keybinding.universal.quit-alt1`***

- **Descripción:** *Especifica una tecla alternativa para salir de `lazygit`. `<c-c>` permite salir utilizando Control + C.*
- **Uso:** *Utiliza `<c-c>` si prefieres este atajo de teclado para salir.*

### ***`keybinding.universal.return`***

- **Descripción:** *Establece la tecla para regresar al estado anterior en `lazygit`. `<esc>` es la tecla asignada para esta función.*
- **Uso:** *Presiona `<esc>` para volver al estado anterior en la interfaz.*

### ***`keybinding.universal.quitWithoutChangingDirectory`***

- **Descripción:** *Define la tecla de atajo para salir de `lazygit` sin cambiar el directorio actual. `Q` es la tecla asignada para esta función.*
- **Uso:** *Usa `Q` si deseas salir de `lazygit` y mantener el directorio actual en la terminal.*

### ***`keybinding.universal.togglePanel`***

- **Descripción:** *Permite alternar entre paneles en `lazygit`. `<tab>` es la tecla utilizada para esta acción.*
- **Uso:** *Presiona `<tab>` para cambiar rápidamente entre paneles.*

### ***`keybinding.universal.prevItem`***

- **Descripción:** *Establece la tecla para seleccionar el ítem anterior en la lista. `<up>` es la tecla predeterminada para esta acción.*
- **Uso:** *Utiliza `<up>` para moverte hacia el ítem anterior.*

### ***`keybinding.universal.nextItem`***

- **Descripción:** *Define la tecla para seleccionar el siguiente ítem en la lista. `<down>` es la tecla asignada para esta acción.*
- **Uso:** *Usa `<down>` para moverte hacia el siguiente ítem.*

### ***`keybinding.universal.prevItem-alt`***

- **Descripción:** *Especifica una tecla alternativa para seleccionar el ítem anterior en la lista. `k` es la tecla alternativa asignada.*
- **Uso:** *Utiliza `k` como alternativa para moverte hacia el ítem anterior.*

### ***`keybinding.universal.nextItem-alt`***

- **Descripción:** *Define una tecla alternativa para seleccionar el siguiente ítem en la lista. `j` es la tecla alternativa asignada.*
- **Uso:** *Usa `j` como alternativa para moverte hacia el siguiente ítem.*

### ***`keybinding.universal.prevPage`***

- **Descripción:** *Especifica la tecla para moverse a la página anterior en listas paginadas. `,` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `,` para ir a la página anterior en la lista.*

### ***`keybinding.universal.nextPage`***

- **Descripción:** *Define la tecla para moverse a la página siguiente en listas paginadas. `.` es la tecla asignada para esta acción.*
- **Uso:** *Usa `.` para avanzar a la siguiente página en la lista.*

### ***`keybinding.universal.scrollLeft`***

- **Descripción:** *Controla la tecla para desplazarse hacia la izquierda en un panel. `H` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `H` para desplazarte hacia la izquierda.*

### ***`keybinding.universal.scrollRight`***

- **Descripción:** *Define la tecla para desplazarse hacia la derecha en un panel. `L` es la tecla asignada para esta acción.*
- **Uso:** *Usa `L` para desplazarte hacia la derecha.*

### ***`keybinding.universal.gotoTop`***

- **Descripción:** *Especifica la tecla para ir al principio de la lista o panel. `<` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `<` para saltar al inicio de la lista.*

### ***`keybinding.universal.gotoBottom`***

- **Descripción:** *Controla la tecla para ir al final de la lista o panel. `>` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `>` para saltar al final de la lista.*

### ***`keybinding.universal.prevBlock`***

- **Descripción:** *Define la tecla para saltar al bloque anterior en la interfaz. `<left>` es la tecla asignada para esta acción.*
- **Uso:** *Usa `<left>` para moverte al bloque anterior.*

### ***`keybinding.universal.nextBlock`***

- **Descripción:** *Establece la tecla para saltar al siguiente bloque en la interfaz. `<right>` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `<right>` para moverte al siguiente bloque.*

### ***`keybinding.universal.prevBlock-alt`***

- **Descripción:** *Especifica una tecla alternativa para saltar al bloque anterior. `h` es la tecla alternativa asignada.*
- **Uso:** *Utiliza `h` como alternativa para moverte al bloque anterior.*

### ***`keybinding.universal.nextBlock-alt`***

- **Descripción:** *Define una tecla alternativa para saltar al siguiente bloque. `l` es la tecla alternativa asignada.*
- **Uso:** *Usa `l` como alternativa para moverte al siguiente bloque.*

### ***`keybinding.universal.nextBlock-alt2`***

- **Descripción:** *Establece otra tecla alternativa para saltar al siguiente bloque. `<tab>` es la tecla alternativa asignada.*
- **Uso:** *Presiona `<tab>` como alternativa para moverte al siguiente bloque.*

### ***`keybinding.universal.prevBlock-alt2`***

- **Descripción:** *Especifica otra tecla alternativa para saltar al bloque anterior. `<backtab>` es la tecla alternativa asignada.*
- **Uso:** *Utiliza `<backtab>` como alternativa para moverte al bloque anterior.*

### ***`keybinding.universal.jumpToBlock`***

- **Descripción:** *Define teclas específicas para saltar directamente a bloques numerados en la interfaz. Las teclas `1`, `2`, `3`, `4`, `5` permiten saltar a los bloques correspondientes.*
- **Uso:** *Usa estas teclas para moverte rápidamente entre bloques numerados.*

### ***`keybinding.universal.nextMatch`***

- **Descripción:** *Controla la tecla para saltar a la siguiente coincidencia en una búsqueda. `n` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `n` para avanzar a la siguiente coincidencia.*

### ***`keybinding.universal.prevMatch`***

- **Descripción:** *Establece la tecla para saltar a la coincidencia anterior en una búsqueda. `N` es la tecla asignada para esta acción.*
- **Uso:** *Usa `N` para retroceder a la coincidencia anterior.*

### ***`keybinding.universal.startSearch`***

- **Descripción:** *Define la tecla para iniciar una búsqueda en `lazygit`. `/` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `/` para comenzar una búsqueda.*

### ***`keybinding.universal.optionMenu`***

- **Descripción:** *Controla la tecla para abrir el menú de opciones en `lazygit`. `x` es la tecla asignada para esta acción.*
- **Uso:** *Usa `x` para acceder rápidamente al menú de opciones.*

### ***`keybinding.universal.optionMenu-alt1`***

- **Descripción:** *Especifica una tecla alternativa para abrir el menú de opciones. `?` es la tecla alternativa asignada.*
- **Uso:** *Utiliza `?` como alternativa para acceder al menú de opciones.*

### ***`keybinding.universal.select`***

- **Descripción:** *Define la tecla para seleccionar elementos en la interfaz de `lazygit`. `<space>` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `<space>` para seleccionar ítems en la lista.*

### ***`keybinding.universal.goInto`***

- **Descripción:** *Establece la tecla para entrar en un directorio o nivel inferior en la interfaz. `<enter>` es la tecla asignada para esta acción.*
- **Uso:** *Usa `<enter>` para navegar hacia niveles inferiores en la estructura.*

### ***`keybinding.universal.confirm`***

- **Descripción:** *Define la tecla para confirmar una acción o selección. `<enter>` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `<enter>` para confirmar selecciones o acciones en `lazygit`.*

### ***`keybinding.universal.remove`***

- **Descripción:** *Controla la tecla para eliminar elementos en la interfaz. `d` es la tecla asignada para esta acción.*
- **Uso:** *Usa `d` para eliminar elementos seleccionados.*

### ***`keybinding.universal.new`***

- **Descripción:** *Define la tecla para crear un nuevo elemento en la interfaz. `n` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `n` para añadir nuevos elementos.*

### ***`keybinding.universal.edit`***

- **Descripción:** *Establece la tecla para editar elementos en la interfaz. `e` es la tecla asignada para esta acción.*
- **Uso:** *Usa `e` para modificar elementos seleccionados.*

### ***`keybinding.universal.openFile`***

- **Descripción:** *Define la tecla para abrir ficheros en la interfaz de `lazygit`. `o` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `o` para abrir un fichero seleccionado.*

### ***`keybinding.universal.scrollUpMain`***

- **Descripción:** *Controla la tecla para desplazarse hacia arriba en el panel principal. `<pgup>` es la tecla asignada para esta acción.*
- **Uso:** *Usa `<pgup>` para subir en la visualización del panel principal.*

### ***`keybinding.universal.scrollDownMain`***

- **Descripción:** *Establece la tecla para desplazarse hacia abajo en el panel principal. `<pgdown>` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `<pgdown>` para bajar en la visualización del panel principal.*

### ***`keybinding.universal.scrollUpMain-alt1`***

- **Descripción:** *Especifica una tecla alternativa para desplazarse hacia arriba en el panel principal. `K` es la tecla alternativa asignada.*
- **Uso:** *Usa `K` como alternativa para subir en la visualización del panel principal.*

### ***`keybinding.universal.scrollDownMain-alt1`***

- **Descripción:** *Define una tecla alternativa para desplazarse hacia abajo en el panel principal. `J` es la tecla alternativa asignada.*
- **Uso:** *Presiona `J` como alternativa para bajar en la visualización del panel principal.*

### ***`keybinding.universal.scrollUpMain-alt2`***

- **Descripción:** *Establece otra tecla alternativa para desplazarse hacia arriba en el panel principal. `<c-u>` es la tecla alternativa asignada.*
- **Uso:** *Presiona `<c-u>` para subir en el panel principal utilizando Control + U.*

### ***`keybinding.universal.scrollDownMain-alt2`***

- **Descripción:** *Especifica otra tecla alternativa para desplazarse hacia abajo en el panel principal. `<c-d>` es la tecla alternativa asignada.*
- **Uso:** *Utiliza `<c-d>` para bajar en el panel principal utilizando Control + D.*

### ***`keybinding.universal.executeCustomCommand`***

- **Descripción:** *Controla la tecla para ejecutar un comando personalizado en la interfaz de `lazygit`. `:` es la tecla asignada para esta acción.*
- **Uso:** *Usa `:` para iniciar la ejecución de un comando personalizado.*

### ***`keybinding.universal.createRebaseOptionsMenu`***

- **Descripción:** *Define la tecla para crear un menú de opciones de rebase. `m` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `m` para acceder a las opciones de rebase.*

### ***`keybinding.universal.pushFiles`***

- **Descripción:** *Establece la tecla para enviar ficheros al repositorio remoto. `P` es la tecla asignada para esta acción.*
- **Uso:** *Usa `P` para hacer un push de los ficheros al remoto.*

### ***`keybinding.universal.pullFiles`***

- **Descripción:** *Define la tecla para obtener ficheros desde el repositorio remoto. `p` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `p` para hacer un pull de los ficheros desde el remoto.*

### ***`keybinding.universal.refresh`***

- **Descripción:** *Controla la tecla para actualizar la interfaz de `lazygit`. `R` es la tecla asignada para esta acción.*
- **Uso:** *Usa `R` para refrescar la interfaz y obtener datos actualizados.*

### ***`keybinding.universal.createPatchOptionsMenu`***

- **Descripción:** *Establece la tecla para crear un menú de opciones de patch. `<c-p>` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `<c-p>` para acceder a las opciones de creación de patches.*

### ***`keybinding.universal.nextTab`***

- **Descripción:** *Define la tecla para moverse a la siguiente pestaña en la interfaz de `lazygit`. `]` es la tecla asignada para esta acción.*
- **Uso:** *Usa `]` para avanzar a la siguiente pestaña.*

### ***`keybinding.universal.prevTab`***

- **Descripción:** *Establece la tecla para moverse a la pestaña anterior en la interfaz de `lazygit`. `[` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `[` para retroceder a la pestaña anterior.*

### ***`keybinding.universal.nextScreenMode`***

- **Descripción:** *Controla la tecla para cambiar al siguiente modo de pantalla en la interfaz de `lazygit`. `+` es la tecla asignada para esta acción.*
- **Uso:** *Usa `+` para alternar entre los modos de pantalla.*

### ***`keybinding.universal.prevScreenMode`***

- **Descripción:** *Establece la tecla para cambiar al modo de pantalla anterior en la interfaz de `lazygit`. `_` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `_` para retroceder al modo de pantalla anterior.*

### ***`keybinding.universal.undo`***

- **Descripción:** *Define la tecla para deshacer la última acción en `lazygit`. `z` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `z` para deshacer la acción más reciente.*

### ***`keybinding.universal.redo`***

- **Descripción:** *Establece la tecla para rehacer una acción previamente deshecha. `<c-z>` es la tecla asignada para esta acción.*
- **Uso:** *Usa `<c-z>` para rehacer la última acción deshecha.*

### ***`keybinding.universal.filteringMenu`***

- **Descripción:** *Controla la tecla para abrir el menú de filtrado en `lazygit`. `<c-s>` es la tecla asignada para esta acción.*
- **Uso:** *Usa `<c-s>` para acceder al menú de opciones de filtrado.*

### ***`keybinding.universal.diffingMenu`***

- **Descripción:** *Define la tecla para abrir el menú de diferencias en la interfaz de `lazygit`. `W` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `W` para comparar diferencias en el menú.*

### ***`keybinding.universal.diffingMenu-alt`***

- **Descripción:** *Especifica una tecla alternativa para abrir el menú de diferencias. `<c-e>` es la tecla alternativa asignada.*
- **Uso:** *Utiliza `<c-e>` para comparar diferencias como alternativa.*

### ***`keybinding.universal.copyToClipboard`***

- **Descripción:** *Controla la tecla para copiar contenido al portapapeles. `<c-o>` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `<c-o>` para copiar texto o contenido seleccionado al portapapeles.*

### ***`keybinding.universal.openRecentRepos`***

- **Descripción:** *Define la tecla para abrir repositorios recientes en `lazygit`. `<c-r>` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `<c-r>` para acceder rápidamente a repositorios utilizados recientemente.*

### ***`keybinding.universal.submitEditorText`***

- **Descripción:** *Establece la tecla para enviar el texto en el editor. `<enter>` es la tecla asignada para esta acción.*
- **Uso:** *Usa `<enter>` para confirmar y enviar texto desde el editor.*

### ***`keybinding.universal.extrasMenu`***

- **Descripción:** *Define la tecla para abrir el menú de extras en `lazygit`. `@` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `@` para acceder al menú de opciones adicionales.*

### ***`keybinding.universal.toggleWhitespaceInDiffView`***

- **Descripción:** *Establece la tecla para alternar la visualización de espacios en blanco en la vista de diferencias. `<c-w>` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `<c-w>` para mostrar u ocultar espacios en blanco en las comparaciones.*

### ***`keybinding.universal.increaseContextInDiffView`***

- **Descripción:** *Controla la tecla para aumentar el contexto en la vista de diferencias. `}` es la tecla asignada para esta acción.*
- **Uso:** *Usa `}` para ampliar el contexto visible en la comparación de diferencias.*

### ***`keybinding.universal.decreaseContextInDiffView`***

- **Descripción:** *Establece la tecla para reducir el contexto en la vista de diferencias. `{` es la tecla asignada para esta acción.*
- **Uso:** *Presiona `{` para reducir el contexto visible en la comparación de diferencias.*

### ***`status`***

**Define atajos de teclado para las acciones en la vista de estado:**

- **`checkForUpdate: u`:** *Presiona `u` para buscar actualizaciones.*
- **`recentRepos: <enter>`:** *Presiona `<enter>` para abrir repositorios recientes.*
- **`allBranchesLogGraph: a`:** *Presiona `a` para ver el gráfico del log de todas las ramas.*

### ***`files`***

**Define atajos para acciones relacionadas con ficheros:**

- **`commitChanges: c`:** *Presiona `c` para hacer un commit de los cambios.*
- **`commitChangesWithoutHook: w`:** *Presiona `w` para hacer un commit sin ejecutar hooks.*
- **`amendLastCommit: A`:** *Presiona `A` para modificar el último commit.*
- **`commitChangesWithEditor: C`:** *Presiona `C` para hacer un commit abriendo el editor.*
- **`refreshFiles: r`:** *Presiona `r` para actualizar la lista de ficheros.*
- **`stashAllChanges: s`:** *Presiona `s` para guardar todos los cambios en el stash.*
- **`viewStashOptions: S`:** *Presiona `S` para ver opciones del stash.*
- **`toggleStagedAll: a`:** *Presiona `a` para alternar el estado de "staged" para todos los ficheros.*
- **`viewResetOptions: D`:** *Presiona `D` para ver opciones de reset.*
- **`fetch: f`:** *Presiona `f` para hacer fetch de los cambios remotos.*
- **`toggleTreeView: "`":** *Presiona `\`` para alternar la vista de árbol.*
- **`openMergeTool: M`:** *Presiona `M` para abrir la herramienta de merge.*
- **`openStatusFilter: <c-b>`:** *Presiona `<c-b>` para abrir el filtro de estado.*

### ***`branches`***

**Define atajos para acciones en las ramas:**

- **`createPullRequest: o`:** *Presiona `o` para crear un pull request.*
- **`viewPullRequestOptions: O`:** *Presiona `O` para ver opciones del pull request.*
- **`copyPullRequestURL: <c-y>`:** *Presiona `<c-y>` para copiar la URL del pull request.*
- **`checkoutBranchByName: c`:** *Presiona `c` para cambiar a una rama por nombre.*
- **`forceCheckoutBranch: F`:** *Presiona `F` para forzar el cambio a una rama.*
- **`rebaseBranch: r`:** *Presiona `r` para hacer rebase de una rama.*
- **`renameBranch: R`:** *Presiona `R` para renombrar una rama.*
- **`mergeIntoCurrentBranch: M`:** *Presiona `M` para hacer merge en la rama actual.*
- **`viewGitFlowOptions: i`:** *Presiona `i` para ver opciones de Git Flow.*
- **`fastForward: f`:** *Presiona `f` para hacer fast-forward de la rama.*
- **`pushTag: P`:** *Presiona `P` para hacer push de una etiqueta.*
- **`setUpstream: u`:** *Presiona `u` para establecer un upstream para la rama.*
- **`fetchRemote: f`:** *Presiona `f` para hacer fetch del remoto.*

### ***`commits`***

**Define atajos para acciones relacionadas con los commits:**

- **`squashDown: s`:** *Presiona `s` para hacer squash del commit actual con el anterior.*
- **`renameCommit: r`:** *Presiona `r` para renombrar un commit.*
- **`renameCommitWithEditor: R`:** *Presiona `R` para renombrar un commit en el editor.*
- **`viewResetOptions: g`:** *Presiona `g` para ver opciones de reset para el commit.*
- **`markCommitAsFixup: f`:** *Presiona `f` para marcar un commit como fixup.*
- **`createFixupCommit: F`:** *Presiona `F` para crear un commit de fixup.*
- **`squashAboveCommits: S`:** *Presiona `S` para hacer squash de los commits anteriores.*
- **`moveDownCommit: <c-j>`:** *Presiona `<c-j>` para mover un commit hacia abajo.*
- **`moveUpCommit: <c-k>`:** *Presiona `<c-k>` para mover un commit hacia arriba.*
- **`amendToCommit: A`:** *Presiona `A` para modificar un commit.*
- **`resetCommitAuthor: a`:** *Presiona `a` para resetear el autor del commit.*
- **`pickCommit: p`:** *Presiona `p` para seleccionar un commit.*
- **`revertCommit: t`:** *Presiona `t` para revertir un commit.*
- **`cherryPickCopy: c`:** *Presiona `c` para copiar un commit para cherry-pick.*
- **`pasteCommits: v`:** *Presiona `v` para pegar commits.*
- **`tagCommit: T`:** *Presiona `T` para etiquetar un commit.*
- **`checkoutCommit: <space>`:** *Presiona `<space>` para hacer checkout de un commit.*
- **`resetCherryPick: <c-R>`:** *Presiona `<c-R>` para resetear un cherry-pick.*
- **`copyCommitAttributeToClipboard: "y"`:** *Presiona `y` para copiar un atributo del commit al portapapeles.*
- **`openLogMenu: <c-l>`:** *Presiona `<c-l>` para abrir el menú del log.*
- **`openInBrowser: o`:** *Presiona `o` para abrir un commit en el navegador.*
- **`viewBisectOptions: b`:** *Presiona `b` para ver opciones de bisect.*

### ***`stash`***

**Define atajos para la gestión del stash:**

- **`popStash: g`:** *Presiona `g` para aplicar (pop) el stash.*

### ***`commitFiles`***

**Define atajos para ficheros de commits:**

- **`checkoutCommitFile: c`:** *Presiona `c` para hacer checkout de un fichero en un commit.*

### ***`main`***

**Define atajos para la vista principal:**

- **`toggleSelectHunk: a`:** *Presiona `a` para alternar la selección de un fragmento (hunk).*
- **`pickBothHunks: b`:** *Presiona `b` para seleccionar ambos fragmentos en un conflicto.*
- **`editSelectHunk: E`:** *Presiona `E` para editar un fragmento seleccionado.*

### ***`submodules`***

**Define atajos para la gestión de submódulos:**

- **`init: i`:** *Presiona `i` para inicializar submódulos.*
- **`update: u`:** *Presiona `u` para actualizar submódulos.*
- **`bulkMenu: b`:** *Presiona `b` para abrir el menú de acciones masivas.*

### ***`os`***

**Define configuraciones relacionadas con el sistema operativo:**

- **`editPreset: "nvim-remote"`:** *Configura `nvim-remote` como editor predeterminado.*
- **`disableStartupPopups: false`:** *Indica si se deben desactivar los pop-ups al inicio (en este caso, no se desactivan).*

### ***`customCommands`***

**Define comandos personalizados que se ejecutan en diferentes contextos:**

- **`key: "b" command: "gh browse" context: "files"`:** *Presiona `b` en el contexto de ficheros para ejecutar `gh browse`.*
- **`key: "b" command: 'gh browse "{{.SelectedLocalCommit.Sha}}"' context: "commits"`:** *Presiona `b` en el contexto de commits para ejecutar `gh browse` con el SHA del commit seleccionado.*

### ***`services`***

**Define servicios personalizados o configuraciones adicionales, en este caso está vacío (`{}`).**

### ***`notARepository`***

**Define cómo `lazygit` debe comportarse si no se encuentra en un repositorio Git:**

- **`skip`:** *Indica que debe saltar ciertas acciones si no está en un repositorio Git.*

### ***`promptToReturnFromSubprocess`***

**Define si se debe preguntar al usuario si desea regresar desde un subproceso:**

- **`true`:** *Se muestra un mensaje para confirmar si se debe regresar desde un subproceso.*

> [!NOTE]
> *Esta configuración permite personalizar el comportamiento y los atajos de `lazygit` para adaptarse a las preferencias del usuario, optimizando su flujo de trabajo con Git.*
