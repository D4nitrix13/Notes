-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me

io.input("./salida.txt")
local file = io.read("*all")
print(file)
io.close()

--[[
    Este código en Lua realiza lo siguiente:

    1. `io.input("./salida.txt")`: Establece el fichero de entrada actual como `salida.txt`. Esto significa que cualquier operación de lectura que siga utilizará este fichero como fuente de datos.

    2. `local file = io.read("*all")`: Lee todo el contenido del fichero de entrada actual y lo almacena en la variable `file`. El modificador `"*all"` indica que se debe leer todo el contenido del fichero.

    3. `print(file)`: Imprime el contenido del fichero en la consola.

    4. `io.close()`: Cierra el fichero de entrada actual, `salida.txt`. Es importante cerrar el fichero después de terminar de leerlo para liberar recursos.

    En resumen, este código lee todo el contenido del fichero `salida.txt` y lo imprime en la consola. Después de leer el fichero, se cierra para liberar los recursos del sistema.
]]