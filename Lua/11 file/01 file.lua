-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me

io.input("./salida.txt")
local file = io.read() -- puedes pasarle un numero como parametro para indicar cuantos caracteres quieres imprimir ejemplo: io.read(10) -> leer los 10 primeros caracteres de la primera linea
io.close()
print(file)

--[[
    Este código en Lua realiza las siguientes acciones:

    1. `io.input("./salida.txt")`: Establece el fichero de entrada actual como `salida.txt`. Esto significa que cualquier operación de lectura que siga utilizará este fichero como fuente de datos.

    2. `local file = io.read()`: Lee el contenido del fichero de entrada actual y lo almacena en la variable `file`. Al no especificar un parámetro numérico, `io.read()` leerá todo el contenido del fichero hasta el final.

    3. `io.close()`: Cierra el fichero de entrada actual, `salida.txt`. Es importante cerrar el fichero después de terminar de leerlo para liberar recursos.

    4. `print(file)`: Imprime el contenido del fichero, que se almacenó en la variable `file`, en la consola.

    En resumen, este código lee el contenido del fichero `salida.txt` y lo imprime en la consola.
]]