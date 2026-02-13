-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me 

-- Se define una variable local llamada 'string_numero' y se le asigna el valor "200"
local string_numero = "200"

-- Se convierte el string a un número y se le suma 1, luego se imprime el resultado
print("Conversión de un string a número y sumarle 1: " .. string_numero .. " -> type(string_numero) = " .. type(string_numero))
print(tonumber(string_numero) + 1)

-- Línea separadora para mejorar la legibilidad
print("\n---------------------------\n")

-- Se realizan algunas operaciones matemáticas básicas y se imprimen los resultados
print("Suma 5 + 3 -> " .. 5 + 3)
print("División 15 / 3 -> " .. 15 / 3)
print("Multiplicación 15 * 2 -> " .. 15 * 2)
print("Resta 5 - 3 -> " .. 5 - 3)
print("Exponenciación 3 ^ 2 -> " .. 3 ^ 2)
print("Módulo 15 % 3 -> " .. 15 % 3)
print("Valor de pi -> " .. math.pi)

-- Otra línea separadora
print("\n---------------------------\n")

-- Se genera un número aleatorio utilizando math.random() y se imprime
math.randomseed(os.time()) -- Se establece la semilla para obtener una aleatoriedad diferente cada vez
print("Número aleatorio utilizando math.random() -> " .. math.random()) -- Rango de aleatoriedad completa
print("Número aleatorio entre 0 y 10 utilizando math.random(10) -> " .. math.random(10))
print("Número aleatorio entre 0 y 10 utilizando math.random(0,10) -> " .. math.random(0,10))
print("Valor de os.time() -> " .. os.time())

-- Otra línea separadora
print("\n---------------------------\n")

-- Se utilizan algunas funciones matemáticas adicionales y se imprimen los resultados
print("Mínimo de los números 1,2,3,4,5,6,7,8,9,10 -> " .. math.min(1,2,3,4,5,6,7,8,9,10))
print("Máximo de los números 1,2,3,4,5,6,7,8,9,10 -> " .. math.max(1,2,3,4,5,6,7,8,9,10))
print("Redondeo hacia abajo de 18.56 -> " .. math.floor(18.56))
print("Redondeo hacia arriba de 18.56 -> " .. math.ceil(18.56))
print("Coseno de 18.56 -> " .. math.cos(18.56))
print("Seno de 18.56 -> " .. math.sin(18.56))
print("Tangente de 18.56 -> " .. math.tan(18.56))
