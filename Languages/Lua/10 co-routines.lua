-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me 


--[[
Las co-rutinas en Lua son una característica poderosa que permite la ejecución concurrente de múltiples tareas dentro de un solo hilo de ejecución. Esto se logra mediante la pausa y la reanudación de la ejecución de una función en puntos específicos, permitiendo que otras tareas se ejecuten en el ínterin. 
]]

-- Crear una coroutine llamada "routine_1"
_G.routine_1 = coroutine.create(
    function ()
        -- Bucle para imprimir los números del 1 al 10
        for i = 1, 10, 1 do
            print("(routine 1): ".. i)
            -- Imprimir el estado actual de la coroutine "routine_1"
            print(coroutine.status(routine_1))
            -- Pausar la coroutine cuando i sea igual a 5
            if i == 5 then
                coroutine.yield()
            end
        end
    end
)

-- Definir una función que imprimirá números del 11 al 20
local routine_func = function ()
    for i = 20, 30, 1 do
        print("(routine 2): " .. i)
    end    
end

-- Crear una segunda coroutine llamada "routine_2" usando la función anterior
local routine_2 = coroutine.create(routine_func)

-- Resumir la ejecución de la coroutine "routine_1"
coroutine.resume(routine_1)
-- Imprimir el estado actual de la coroutine "routine_1" después de la primera ejecución
print(coroutine.status(routine_1))
-- Resumir la ejecución de la coroutine "routine_1" nuevamente
coroutine.resume(routine_1)
-- Imprimir el estado actual de la coroutine "routine_1" después de la segunda ejecución
print(coroutine.status(routine_1))

coroutine.resume(routine_2)


--[[
    Las coroutines en Lua pueden estar en varios estados, y la función `coroutine.status` se utiliza para verificar el estado actual de una coroutine. Los posibles estados de una coroutine son los siguientes:

    1. **Suspendida:** suspended -> La coroutine se ha pausado en algún punto usando `coroutine.yield()` o aún no se ha ejecutado.

    2. **Corriendo:** running -> La coroutine está actualmente en ejecución.

    3. **Muerta:** dead -> La coroutine ha terminado su ejecución.
]]