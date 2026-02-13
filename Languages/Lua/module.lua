-- Solo se puede tener una tabla
_G.matematicas = {}

--[[
# ***Esta funcion suma todos los elementos enteros dados***

- **Ejemplo de uso:**

```lua
local modulo = require("./module")
print(modulo.sumar(1,2,3,4,5,6,7,8,9,10))
```
]]
function matematicas.sumar(...)
    local s = 0
    local n = select("#", ...) -- Obtiene el número de argumentos pasados a la función
    for i = 1, n do
        s = s + select(i, ...) -- Suma el i-ésimo argumento
    end
    return s
end

return matematicas

--[[
    Cuando estás creando un módulo propio en Lua, es una práctica común encapsular todo el código relacionado con el módulo dentro de una tabla. Esto ayuda a organizar y estructurar el código de manera más clara y permite evitar colisiones de nombres con otros módulos o variables globales.

    Al comienzo del módulo, `_G.matematicas = {}` crea una nueva tabla llamada `matematicas` en el espacio global. Esto establece un espacio de nombres para todas las funciones y variables relacionadas con el módulo `matematicas`.

    Al final del módulo, `return matematicas` devuelve la tabla `matematicas` que contiene todas las funciones y variables definidas en el módulo. Esto permite que otros scripts o módulos importen el módulo `matematicas` y accedan a sus funciones y variables.

    Por lo tanto, este patrón de diseño proporciona un encapsulamiento claro del código del módulo, evita contaminar el espacio global con nombres de funciones y variables, y facilita la reutilización y la modularidad del código en Lua.
]]
