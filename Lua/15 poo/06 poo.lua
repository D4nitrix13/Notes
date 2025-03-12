-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me

-- Definición de un decorador que imprime un mensaje antes y después de llamar a una función
local function decorador(funcion)
    print("return function(...)")
    return function(...)
        print("Antes de llamar a la función")
        local resultado = funcion(...) -- Llama a la función original con los argumentos dados
        print("Después de llamar a la función")
        return resultado
    end
end

-- Función original
local function miFuncion(x, y)
    return x + y
end

-- Decoramos la función original
miFuncion = decorador(miFuncion)

-- Llamamos a la función decorada
print(miFuncion(3, 5)) -- Esto imprimirá el mensaje antes y después de llamar a la función, y luego imprimirá el resultado (8)
