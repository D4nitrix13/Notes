-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me

-- Verifica si se proporcionaron argumentos en la línea de comandos
if #arg > 0 then
    -- Imprime la cantidad de argumentos pasados
    print("Se proporcionaron " .. #arg .. " argumentos.")
    -- Itera sobre los argumentos e imprímelos uno por uno
    for i, v in ipairs(arg) do
        print("Argumento " .. i .. ": " .. v)
    end
else
    -- Imprime un mensaje si no se proporciona ningún argumento
    print("No se proporcionaron argumentos.")
end


--[[
    -- Verifica si se proporcionó un argumento en la línea de comandos
    if arg[1] ~= nil then
        -- Imprime un saludo con el argumento proporcionado
        print("Hola " .. arg[1])
    else
        -- Imprime un mensaje de error si no se proporciona ningún argumento
        print("Error: Debes proporcionar un nombre como argumento.")
    end

]]
