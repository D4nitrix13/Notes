-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me 

package.path = package.path .. ";../lib/?.lua"
package.path = package.path .. ";../Modules/?.lua"
local moduleValidation = require("moduleValidation")
local moduleColor = require("moduleColor")

--[[
Este código Lua tiene como objetivo configurar las rutas de búsqueda de módulos (`package.path`) para incluir directorios específicos donde Lua buscará ficheros `.lua` cuando se requieran módulos mediante `require`.

Vamos a desglosarlo:

1. **Configuración de `package.path`:**
   ```lua
   package.path = package.path .. ";../lib/?.lua"
   package.path = package.path .. ";../Modules/?.lua"
   ```
   - `package.path` es una variable predefinida en Lua que indica las rutas de búsqueda para los módulos.
   - `..` se utiliza para concatenar cadenas en Lua.
   - `";../lib/?.lua"` y `";../Modules/?.lua"` son las rutas especificadas. Estas líneas añaden dos rutas adicionales donde Lua buscará ficheros `.lua` cuando se requieran módulos.

2. **Requerir módulos:**
   ```lua
   local moduleValidation = require("moduleValidation")
   local moduleColor = require("moduleColor")
   ```
   - `require("moduleValidation")` y `require("moduleColor")` son llamadas para cargar los módulos llamados `moduleValidation.lua` y `moduleColor.lua` desde las rutas especificadas en `package.path`.
   - El resultado de `require` asigna el contenido exportado del módulo (como funciones o variables) a las variables locales `moduleValidation` y `moduleColor`.

### Ejemplo:

Supongamos que tienes la siguiente estructura de directorios y ficheros:

```
/Proyecto
  /lib
    moduleValidation.lua
  /Modules
    moduleColor.lua
  main.lua
```

En `main.lua`, podrías tener el código que mencionaste:

```lua
package.path = package.path .. ";../lib/?.lua"
package.path = package.path .. ";../Modules/?.lua"

local moduleValidation = require("moduleValidation")
local moduleColor = require("moduleColor")

-- Ahora puedes usar las funciones y variables definidas en moduleValidation y moduleColor
```

Esto permite que Lua encuentre y cargue los módulos `moduleValidation.lua` desde `/lib` y `moduleColor.lua` desde `/Modules` cuando se necesiten en `main.lua`.
]]

--[[
En Lua, el símbolo `;` se utiliza como separador dentro de la cadena de `package.path` para indicar múltiples rutas de búsqueda. Mientras que el símbolo `?` se utiliza como un comodín en las rutas de búsqueda para representar el nombre del módulo que se está requiriendo.

Vamos a detallarlo:

1. **`;` en `package.path`:**
   - En Lua, `package.path` es una cadena que define las rutas de búsqueda para los módulos. Al concatenar `";"` seguido de una nueva ruta, se añade esa ruta a las rutas existentes en `package.path`.
   - Por ejemplo:
     ```lua
     package.path = package.path .. ";../lib/?.lua"
     ```
     Aquí, `";../lib/?.lua"` se agrega al final de las rutas existentes en `package.path`. Esto significa que Lua buscará módulos en el directorio `lib` (relativo al directorio actual) utilizando el comodín `?` para reemplazar el nombre del módulo.

2. **`?` en las rutas de búsqueda (`package.path`):**
   - El símbolo `?` dentro de una ruta de búsqueda indica un comodín que Lua reemplazará con el nombre real del módulo que se está requiriendo.
   - Por ejemplo:
     ```lua
     package.path = package.path .. ";../Modules/?.lua"
     ```
     Aquí, `";../Modules/?.lua"` significa que Lua buscará ficheros `.lua` dentro del directorio `Modules` (relativo al directorio actual). Cuando se requiera un módulo específico, como `moduleValidation`, Lua buscará un fichero llamado `moduleValidation.lua` dentro de ese directorio.

### Ejemplo:

Supongamos que tienes la siguiente estructura de directorios y ficheros:

```
/Proyecto
  /lib
    moduleValidation.lua
  /Modules
    moduleColor.lua
  main.lua
```

Entonces, el contenido de `main.lua` con las rutas de búsqueda configuradas sería:

```lua
package.path = package.path .. ";../lib/?.lua"
package.path = package.path .. ";../Modules/?.lua"

local moduleValidation = require("moduleValidation")
local moduleColor = require("moduleColor")

-- Ahora puedes usar las funciones y variables definidas en moduleValidation y moduleColor
```

En este caso:

- `package.path` ahora incluye `";../lib/?.lua"` y `";../Modules/?.lua"`.
- Cuando se requiere `moduleValidation`, Lua buscará `moduleValidation.lua` dentro de `/lib`.
- Cuando se requiere `moduleColor`, Lua buscará `moduleColor.lua` dentro de `/Modules`.

Esto permite una organización modular y flexible de código en Lua, utilizando rutas de búsqueda configurables para encontrar y cargar módulos según sea necesario.
]]