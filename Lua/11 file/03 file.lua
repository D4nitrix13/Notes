-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me

io.input("./salida.txt")
print(io.read("*line"))
print(io.read("*line")) -- cuando el valor retornado se nill -> null es que ya no hay mas linea para leer
io.close()

--[[
    Este código en Lua realiza lo siguiente:

    1. `io.input("./salida.txt")`: Establece el fichero de entrada actual como `salida.txt`. Esto significa que cualquier operación de lectura que siga utilizará este fichero como fuente de datos.

    2. `print(io.read("*line"))`: Lee una línea del fichero de entrada actual y la imprime en la consola. El modificador `"*line"` indica que se debe leer una línea del fichero. Si no hay más líneas para leer, la función `io.read()` devuelve `nil`.

    3. `print(io.read("*line"))`: Intenta leer la siguiente línea del fichero de entrada actual y la imprime en la consola. Al igual que antes, si no hay más líneas para leer, la función `io.read()` devuelve `nil`.

    4. `io.close()`: Cierra el fichero de entrada actual, `salida.txt`. Es importante cerrar el fichero después de terminar de leerlo para liberar recursos.

    En resumen, este código lee dos líneas del fichero `salida.txt` y las imprime en la consola. Si hay más líneas en el fichero, las imprime; de lo contrario, imprime `nil` indicando que no hay más líneas para leer.
]]