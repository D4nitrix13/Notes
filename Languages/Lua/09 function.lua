-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me 

-- Función sin parámetros y sin retorno
local function funcionSinParametros()
    print("Esta es una función sin parámetros y sin retorno")
end

-- Función con parámetros y con retorno
local function suma(a, b)
    return a + b
end

-- Función sin parámetros y con retorno
local function obtenerMensaje()
    return "Hola desde la función obtenerMensaje"
end

-- Función con parámetros y sin retorno
local function saludar(nombre)
    print("¡Hola, " .. nombre .. "!")
end

-- Función local
local function funcionLocal()
    print("Esta es una función local")
end

-- Función global (_G)
_G.funcionGlobal = function()
    print("Esta es una función global")
end

-- Función anónima
local funcionAnonima = function()
    print("Esta es una función anónima")
end


--[[
La expresión select("#", ...) se utiliza para obtener la cantidad de argumentos pasados a una función que acepta un número variable de argumentos.

    #: En Lua, el operador # se utiliza para obtener la longitud de una lista o la cantidad de elementos en una tabla.
    ...: Representa los argumentos pasados a la función que está siendo llamada.

La expresión sum = sum + select(i, ...) se utiliza para sumar los argumentos pasados a una función que tiene un número variable de parámetros.

select(i, ...) selecciona el i-ésimo argumento de la lista de argumentos ....
sum = sum + select(i, ...) suma el i-ésimo argumento al valor actual de sum.
]]

-- Función con parámetros variables
local function promedio(...)
    local sum = 0
    local contador = select("#", ...)
    print("local contador = select(\"#\", ...) -> " .. tostring(contador))
    for i = 1, contador, 1 do
        print("sum = sum + select(i, ...) -> " .. tostring(select(i, ...)))
        sum = sum + select(i, ...)
    end
    return sum / contador
end

local function sumarTodosElementos(...)
    local suma = 0
    for index, value in pairs({...}) do
        suma = suma + value
    end
    return suma
end

--[[
    La diferencia entre `select` y `{...}` radica en cómo se manejan los parámetros variables en Lua.

    - **`select`:** Es una función incorporada en Lua que permite acceder a los argumentos pasados a una función con un número variable de parámetros. Toma un índice y los argumentos pasados a la función, y devuelve el valor del argumento en esa posición. `select("#", ...)` se utiliza para obtener el número total de argumentos pasados a la función.

    - **`{...}`:** Esta sintaxis se utiliza para crear una tabla que contiene todos los argumentos pasados a la función. Cuando se utiliza `{...}`, se crea una tabla que contiene todos los parámetros pasados, y luego se puede iterar sobre esta tabla para realizar operaciones.

    Entonces, en el caso de la función `promedio`, se utiliza `select` porque se necesita acceder a los argumentos uno por uno para calcular el promedio. En cambio, en la función `sumarTodosElementos`, se utiliza `{...}` porque se quiere sumar todos los elementos sin necesidad de acceder a ellos de forma individual, sino tratándolos como una tabla.
]]

--[[
    En Lua, las funciones pueden capturar variables locales de los ámbitos circundantes en el que fueron definidas. En el caso de la función crearSumador, esta retorna una función anónima que toma un argumento b. Dentro de esta función anónima, la variable a se toma del ámbito en el que fue definida la función externa crearSumador. Aunque b no está definida dentro de crearSumador, la función interna anónima tiene acceso a a porque fue capturada como parte del cierre (closure) cuando se definió la función.

    Por lo tanto, cuando llamas a la función interna retornada por crearSumador, como en sumarDos = crearSumador(2), a es igual a 2 y la función interna solo necesita un argumento b para realizar la suma. Esto es una característica poderosa de las funciones en Lua que permite crear clausuras y mantener el estado entre llamadas a funciones.
]]

--[[
    Función que crea y devuelve una función para sumar un valor constante 'a' a otro valor 'b'.
    Esta función se utiliza para crear una función que suma 'a' a cualquier valor 'b' pasado como argumento.

    Parámetros:
    - a: Valor constante que se sumará al valor 'b'.
    
    Retorno:
    - Función anónima que toma un parámetro 'b' y devuelve la suma de 'a' y 'b'.
]]

-- Función que retorna otra función
local function crearSumador(a)
    return function(b)
        return a + b
    end
end


-- Función recursiva
local function factorial(n)
    if n == 0 then
        return 1
    else
        return n * factorial(n - 1)
    end
end

local function retornaFuncionaSinEjecutar()
    return obtenerMensaje
end

-- Llamadas a las funciones
local funcionSinEjecutar = retornaFuncionaSinEjecutar()
print("funcionSinEjecutar se ejecuta poniendo funcionSinEjecutar() -> " .. funcionSinEjecutar())


local sumar_x_cantidad = crearSumador(5)
print("local sumar_x_cantidad = crearSumador(5) -> " .. sumar_x_cantidad(15))

funcionSinParametros()
print("El resultado de la suma es:", suma(5, 3))
print(obtenerMensaje())
saludar("Daniel")
funcionLocal()
funcionGlobal()
funcionAnonima()
print("El promedio es:", promedio(5, 10, 15))

--[[
    Cuando ejecutas `print(crearSumador(5))`, estás imprimiendo el valor retornado por `crearSumador(5)`, que es una función anónima que toma un argumento `b` y devuelve la suma de `a` (en este caso, `5`) y `b`.

    La impresión que estás viendo, "dirección a memoria", es en realidad una representación de la función anónima en Lua, que no tiene una representación de cadena legible como lo haría una cadena de texto. Lo que estás viendo es la forma en que Lua muestra las funciones anónimas en la salida estándar.

    En Lua, las funciones son ciudadanos de primera clase, lo que significa que pueden ser pasadas como argumentos a otras funciones, retornadas por funciones y asignadas a variables. Cuando imprimes una función en Lua, estás viendo una representación interna de esa función, que puede no ser legible para los humanos en su forma bruta.
]]

local sumar5 = crearSumador(5)
print("El resultado de sumar 5 + 3 es:", sumar5(3))
print("El factorial de 5 es:", factorial(5))
print("sumar (1,2,3,4,5,6,7,8,9,10) -> " .. sumarTodosElementos(1,2,3,4,5,6,7,8,9,10))