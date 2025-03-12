-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me

-- Intenta abrir el fichero "myfile.txt" para añadir contenido
local fichero = io.open("myfile.txt", "a")

-- Verifica si el identificador de fichero no es nil (es decir, si el fichero se abrió correctamente)
if fichero then
    -- Escribe datos adicionales en el fichero
    fichero:write("\nsoy desarrollador web, pentester y data science\ntengo 18 años")
    -- Cierra el identificador de fichero
    fichero:close()
else
    -- Maneja el caso en el que el fichero no se pudo abrir
    print("Error: No se pudo abrir el fichero para escribir.")
end
