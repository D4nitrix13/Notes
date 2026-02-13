-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me

io.input("./int.txt")
local file = io.read("*number") -- "*number", "*line","*all"
io.close()
print(file + 1)

--[[
    Este código en Lua realiza las siguientes acciones:

    1. `io.input("./int.txt")`: Establece el fichero de entrada actual como `int.txt`. Esto significa que cualquier operación de lectura que siga utilizará este fichero como fuente de datos.

    2. `local file = io.read("*number")`: Lee el contenido del fichero de entrada actual y lo interpreta como un número. El modificador `"*number"` indica que se espera leer un número del fichero. Si el contenido no puede ser convertido a un número, la función `io.read()` devuelve `nil`. El número leído se almacena en la variable `file`.

    3. `io.close()`: Cierra el fichero de entrada actual, `int.txt`. Es importante cerrar el fichero después de terminar de leerlo para liberar recursos.

    4. `print(file + 1)`: Imprime en la consola el número leído del fichero más 1.

    En resumen, este código lee un número del fichero `int.txt`, lo interpreta como un número y luego imprime en la consola ese número más 1.
]]