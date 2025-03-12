-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me

-- Intenta abrir el fichero para escribir
local fichero = io.open("myfile.txt", "w")

-- Verifica si el identificador de fichero no es nil (es decir, si el fichero se abrió correctamente)
if fichero then
    -- Escribe datos en el fichero
    fichero:write("mi nombre es daniel perez")
    -- Cierra el identificador de fichero
    fichero:close()
else
    -- Maneja el caso en el que el fichero no se pudo abrir
    print("Error: No se pudo abrir el fichero para escribir.")
end
