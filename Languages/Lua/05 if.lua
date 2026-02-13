-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me 

-- Explicación de los valores de nil, false y 0 en Lua
-- nil -> falso, false -> falso, 0 -> falso
-- 'not' -> niega una condición
if true then
    print("if true") -- Se ejecutará siempre porque la condición es verdadera
end

-- Definición de variables 'a' y 'b'
local a = 5
local b = 10

-- Verificar si 'a' es igual a 5 y 'b' es igual a 10
if a == 5 and b == 10 then
    print("Valor de a -> 5\nValor de b -> 10")
end

-- Verificar si 'a' es igual a 15 o 'b' es igual a 10
if a == 15 or b == 10 then
    print("Ejemplo de operador 'or'")
end

-- Definición de una variable 'variable'
local variable = "Hola"

-- Verificar el tipo de la variable y actuar en consecuencia
if type(variable) == "string" then
    print("La variable es una cadena de caracteres.")
elseif type(variable) == "number" then
    print("La variable es un número.")
elseif type(variable) == "table" then
    print("La variable es una tabla.")
else
    print("La variable es de un tipo desconocido.")
end

-- Definición de la variable 'edad'
local edad = 20

-- Operador ternario simulado
local categoria = (edad >= 18) and "adulto" or "menor"

-- Impresión del resultado del operador ternario simulado
print("La categoría es: " .. categoria)

-- Impresión de resultados de operadores relacionales con conversión a cadena
-- Igual a
print("a == b -> " .. tostring(a == b))  -- Salida: false

-- No igual a
print("a ~= b -> " .. tostring(a ~= b))  -- Salida: true

-- Menor que
print("a < b -> " .. tostring(a < b))   -- Salida: true

-- Menor o igual que
print("a <= b -> " .. tostring(a <= b))  -- Salida: true

-- Mayor que
print("a > b -> " .. tostring(a > b))   -- Salida: false

-- Mayor o igual que
print("a >= b -> " .. tostring(a >= b))  -- Salida: false

-- Ejemplo del operador 'not'
local condicion = false
if not condicion then
    print("La condición es falsa.")  -- Se ejecutará porque la condición original es falsa y 'not' la niega
end
