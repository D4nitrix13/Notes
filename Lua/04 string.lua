-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me 

-- Definición de una variable local que contiene un nombre
local name = "daniel perez"

-- Determina la longitud de la cadena de caracteres
local len = #name

-- Conversión de un número a una cadena de caracteres
local string_conversion = tostring(100)

-- Definición de una cadena de saludo
local saludo = "hola usuario"

-- Encuentra la posición de la palabra "perez" en la cadena
local inicio, fin = string.find(name, "perez")

-- Imprime la longitud de la cadena 'name'
print(#name)

-- Imprime la longitud almacenada en la variable 'len'
print(len)

-- Imprime el tipo de datos de 'string_conversion'
print(type(string_conversion))

-- Imprime una cadena de múltiples líneas
print([[
    Daniel Benjamin Perez Morales
    18 años
    Pentesting, Data Science, Web developer fullstack
]])

-- Imprime una cadena con caracteres de escape
print("Daniel Perez\ndev\t!pentester!\v\"18 años\"")

-- Convierte una cadena a mayúsculas
print(string.upper("mayusculas"))

-- Convierte una cadena a minúsculas
print(string.lower("MINUSCULA"))

-- Calcula la longitud de la cadena 'perez'
print(string.len("perez"))

-- Obtiene una subcadena de 'saludo'
print(string.sub(saludo, 0, 4))

-- Convierte un número ASCII en un carácter
print(string.char(97))

-- Convierte un carácter en su valor ASCII
print(string.byte("a"))

-- Obtiene los valores ASCII de los caracteres en 'saludo'
print(string.byte(saludo, 1, string.len(saludo)))

-- Repite la cadena 'daniel! ' diez veces
print(string.rep("daniel! ", 10))

-- Formatea una cadena con valores variables
--[[
%s: Este es un marcador de posición que indica que se debe insertar una cadena en esa posición en la cadena formateada. Cuando string.format() encuentra %s, espera un argumento que sea una cadena y lo inserta en ese lugar.

%.2f: Este es un marcador de posición para un número de punto flotante (flotante). El .2 después del % indica que se deben mostrar dos lugares decimales después del punto decimal. Por lo tanto, si el número es 80.6, se mostrará como 80.60.

%i: Este es un marcador de posición para un número entero. Cuando string.format() encuentra %i, espera un argumento que sea un número entero y lo inserta en ese lugar.
]]
print(string.format("name %s, nota %.2f, edad %i", name, 80.6, 18))

-- Encuentra la posición de la palabra "perez" en 'name'
print(string.find(name, "perez"))

-- Busca una coincidencia con la expresión regular "ez" en 'name'
print(string.match(name, "ez"))

-- Imprime el inicio y fin de la coincidencia de "perez" en 'name'
print("inicio -> " .. inicio .. "\nfin -> " .. fin)

-- Reemplaza todas las apariciones de "e" por "$" en 'name'
print(string.gsub(name, "e", "$"))
