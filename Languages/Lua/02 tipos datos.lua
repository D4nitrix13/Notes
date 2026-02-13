-- Daniel Benjamin Perez Morales
-- Github: https://github.com/D4nitrix13
-- Email: danielperezdev@proton.me 

--[[
    Lua es un lenguaje de programación dinámico y débilmente tipado, lo que significa que las variables no están asociadas a tipos de datos específicos y pueden contener cualquier tipo de dato. Sin embargo, Lua es un lenguaje tipado y los valores tienen tipos definidos. A continuación, se presentan los tipos de datos básicos que se encuentran en Lua:
    
    1. Nil: El tipo `nil` representa la ausencia de un valor. Es similar a `null` en otros lenguajes de programación. Por defecto, las variables no inicializadas en Lua tienen el valor `nil`.
    
    2. Booleano: Lua tiene el tipo de datos booleano, que puede ser `true` (verdadero) o `false` (falso).
    
    3. Número: Lua tiene un solo tipo numérico, que puede ser entero o de punto flotante. No hay distinción entre enteros y números de punto flotante; todos los números se almacenan como números de punto flotante en Lua.
    
    4. Cadena de caracteres: Lua tiene soporte integrado para cadenas de caracteres. Pueden estar encerradas entre comillas simples `' '` o comillas dobles `" "`. Lua también permite el uso de delimitadores de cadena larga `[ -> [ ... ] <-]` para cadenas de varios líneas.
    
    5. Función: En Lua, las funciones son ciudadanos de primera clase. Esto significa que las funciones pueden ser asignadas a variables, pasadas como argumentos y devueltas como resultados de otras funciones.
    
    6. Tabla: Las tablas son la única estructura de datos compuesta en Lua y se utilizan para implementar arrays, diccionarios, sets, entre otras estructuras de datos. Las tablas en Lua son colecciones asociativas que pueden contener pares clave-valor.
    
    7. Hilos: Lua tiene soporte para programación concurrente mediante hilos. Los hilos en Lua se pueden crear, ejecutar y comunicar utilizando la biblioteca estándar `coroutine`.
    
    Estos son los tipos de datos básicos en Lua. La flexibilidad de Lua para manipular estos tipos de datos es una de sus características principales.
]]


--[[
    global = 100:
        Esta línea asigna el valor 100 a la variable global global. Esta es una asignación directa de un valor a una variable global. No se utiliza ninguna tabla especial.
    
    _G.GLOBAL = 10:
        _G es una tabla especial que contiene todas las variables globales y funciones definidas en el entorno actual.
        GLOBAL en _G es una variable global específica que se está definiendo o modificando dentro de la tabla _G. Se le está asignando el valor 10.
        Al utilizar _G.GLOBAL, se accede explícitamente a la tabla global _G y se define o modifica una variable llamada GLOBAL dentro de esta tabla. Esto es útil cuando se quiere tener un control más explícito sobre las variables globales y se desea evitar conflictos con otras variables del mismo nombre que puedan estar definidas en diferentes ámbitos.
]]
global = 100

_G.GLOBAL = 10

-- Definición de variables locales
local null = nil
local string = "daniel" -- Cadena de caracteres
local entero = 18 -- Número entero
local flotante = 1.21 -- Número de punto flotante
local booleano = true -- Valor booleano
local string_multilinea = [[
Daniel Perez Dev
Desarrolador Web
]] -- Cadena de caracteres multilínea

-- Imprime el valor de la variable global
print(global)

-- Imprime el tipo de datos de la variable null, string, entero, flotante y booleano
print(type(null))
print(type(string))
print(type(entero))
print(type(flotante))
print(type(booleano))

-- Imprime una concatenación de cadenas
print("Mi nombre es " .. string .. " tengo " .. entero .. " años")

-- Imprime una cadena de caracteres multilínea
print(string_multilinea)

-- Imprime los valores de las variables global y GLOBAL
print(global, GLOBAL)
