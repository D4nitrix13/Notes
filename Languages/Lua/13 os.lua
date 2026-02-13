-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me

-- Imprime el directorio de trabajo actual -> os.getenv(variable de entorno)
print("os.getenv(\"PWD\") -> " .. os.getenv("PWD"))

-- Ejecuta un comando en el sistema operativo para crear un fichero de Python llamado 'fichero.py' con un simple comando de impresión
os.execute("echo 'print('Daniel Benjamin Perez Morales')' > fichero.py")

-- Renombra el fichero 'fichero.py' a 'name.py'
print("os.rename(\"./fichero.py\",name.py)")
os.rename("./fichero.py","./name.py")

-- Elimina el fichero 'name.py'
os.remove("./name.py")

-- Ejecuta un comando en el sistema operativo para listar los ficheros en el directorio actual, utilizando el comando 'lsd -la' si está disponible, de lo contrario, utiliza 'ls -la'
os.execute("lsd -la || ls -la")

-- Inicia un temporizador y realiza una suma iterativa en un bucle 'for' desde 1 hasta 10000, luego imprime el tiempo transcurrido
local start, x = os.clock(), 0
for i = 1, 10000, 1 do
    x = x + i
end
print("os.clock() - start -> " .. os.clock() - start)

-- Sal del programa con código de estado 0
print("os.exit(0)")
os.exit(0)
