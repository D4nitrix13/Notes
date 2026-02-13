-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me 

io.write("cuanto es 10 + 5: ")
local input = io.read()
print("Tu respusta ha sido -> " .. input)

-- Ejemplo de ingreso de una cadena
print("Ingrese una cadena:")
local str = io.read():match("^%s*(.-)%s*$")  -- Eliminar espacios en blanco al principio y al final
print("Ha ingresado la cadena:", str)

-- Ejemplo de ingreso de un número entero
print("Ingrese un número entero:")
local intStr = io.read():match("^%s*(%d+)%s*$")  -- Leer como cadena y extraer solo los dígitos
local int = tonumber(intStr)  -- Convertir la cadena a un número entero
if int then
    print("Ha ingresado el número entero:", int)
else
    print("Entrada inválida. Por favor, ingrese un número entero válido.")
end

-- Ejemplo de ingreso de un booleano
print("Ingrese 'true' o 'false' para un booleano:")
local boolStr = io.read():lower()  -- Leer como cadena y convertir a minúsculas
local bool
if boolStr == "true" then
    bool = true
elseif boolStr == "false" then
    bool = false
else
    print("Entrada inválida. Por favor, ingrese 'true' o 'false'.")
end
if bool ~= nil then
    print("Ha ingresado el booleano:", bool)
end

--[[
1. **Eliminar espacios en blanco al principio y al final:**
   ```lua
   "^%s*(.-)%s*$"
   ```
   - `^`: Coincide con el inicio de la cadena.
   - `%s*`: Coincide con cero o más espacios en blanco.
   - `(.-)`: Encierra el patrón `.-`, que coincide con cualquier carácter cero o más veces, de forma no codiciosa (para que no coincida con más espacios al final), y captura el resultado en un grupo de captura.
   - `%s*$`: Coincide con cero o más espacios en blanco seguidos del final de la cadena.
   
   Esta expresión regular se utiliza para eliminar los espacios en blanco al principio y al final de una cadena.

2. **Leer como cadena y extraer solo los dígitos:**
   ```lua
   "^%s*(%d+)%s*$"
   ```
   - `^`: Coincide con el inicio de la cadena.
   - `%s*`: Coincide con cero o más espacios en blanco.
   - `(%d+)`: Encierra el patrón `%d+`, que coincide con uno o más dígitos, y captura el resultado en un grupo de captura.
   - `%s*$`: Coincide con cero o más espacios en blanco seguidos del final de la cadena.

   Esta expresión regular se utiliza para leer la entrada del usuario como una cadena y extraer solo los dígitos. Esto se usa en el ejemplo de ingreso de un número entero.

3. **Explicación de los caracteres especiales:**
   - `^`: Coincide con el inicio de la cadena.
   - `%s`: Coincide con un espacio en blanco.
   - `*`: Coincide con cero o más repeticiones del elemento anterior.
   - `.`: Coincide con cualquier carácter.
   - `+`: Coincide con una o más repeticiones del elemento anterior.
   - `%d`: Coincide con un dígito.
   - `()`: Define un grupo de captura. Los patrones dentro de los paréntesis se capturan y pueden ser referenciados posteriormente.
   - `$`: Coincide con el final de la cadena.

Estas expresiones regulares se utilizan para validar y formatear la entrada del usuario en los ejemplos proporcionados.
]]