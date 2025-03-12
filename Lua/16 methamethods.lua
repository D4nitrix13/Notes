-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me

local vector1 = {x = 5, y = 10}
local vector2 = {x = 3, y = 7}

setmetatable(vector1, {
    __add = function(v1, v2)
        return {x = v1.x + v2.x, y = v1.y + v2.y}
    end
})

print("\n1. Metamétodo __add (suma)")
local suma = vector1 + vector2
print("Suma:", suma.x, suma.y) -- Imprime: Suma: 8 17

print("\n2. Metamétodo __sub (resta)")
local vector1 = {x = 5, y = 10}
local vector2 = {x = 3, y = 7}

setmetatable(vector1, {
    __sub = function(v1, v2)
        return {x = v1.x - v2.x, y = v1.y - v2.y}
    end
})

local resta = vector1 - vector2
print("Resta:", resta.x, resta.y) -- Imprime: Resta: 2 3

print("\n3. Metamétodo __mul (multiplicación)")
local vector1 = {x = 5, y = 10}
local escalar = 3

setmetatable(vector1, {
    __mul = function(v1, escalar)
        return {x = v1.x * escalar, y = v1.y * escalar}
    end
})

local multiplicacion = vector1 * escalar
print("Multiplicación:", multiplicacion.x, multiplicacion.y) -- Imprime: Multiplicación: 15 30

print("\n4. Metamétodo __div (división)")
local vector1 = {x = 10, y = 20}
local escalar = 2

setmetatable(vector1, {
    __div = function(v1, escalar)
        return {x = v1.x / escalar, y = v1.y / escalar}
    end
})

local division = vector1 / escalar
print("División:", division.x, division.y) -- Imprime: División: 5 10

print("\n5. Metamétodo __mod (módulo)")
local numero = { valor = 10 } -- Convertir el número en una tabla
local divisor = 3

setmetatable(numero, {
    __mod = function(n, divisor)
        return n.valor % divisor
    end
})

local modulo = numero % divisor
print("Módulo:", modulo) -- Imprime: Módulo: 1

print("\n6. Metamétodo __concat (concatenación)")
local cadena1 = {valor = "Hola "}
local cadena2 = "Mundo!"

setmetatable(cadena1, {
    __concat = function(str1, str2)
        return str1.valor .. str2
    end
})

local concatenacion = cadena1 .. cadena2
print("Concatenación:", concatenacion) -- Imprime: Concatenación: Hola Mundo!

print("\n7. Metamétodo __len (longitud)")
local lista = {1, 2, 3, 4, 5}

setmetatable(lista, {
    __len = function(tbl)
        local count = 0
        for _ in pairs(tbl) do
            count = count + 1
        end
        return count
    end
})

print("Longitud de la lista:", #lista) -- Imprime: Longitud de la lista: 5

print("\n8. Metamétodo __eq (igualdad)")
local vector1 = {x = 5, y = 10}
local vector2 = {x = 5, y = 10}
local vector3 = {x = 3, y = 7}

setmetatable(vector1, {
    __eq = function(v1, v2)
        return v1.x == v2.x and v1.y == v2.y
    end
})

print("Vector1 es igual a Vector2:", vector1.x == vector2.x and vector1.y == vector2.y) -- Imprime: Vector1 es igual a Vector2: true
print("Vector1 es igual a Vector3:", vector1.x == vector3.x and vector1.y == vector3.y) -- Imprime: Vector1 es igual a Vector3: false

print("\n9. Metamétodo __le (menor o igual)")
local numero1 = { valor = 10 } -- Convertir el número en una tabla
local numero2 = { valor = 5 }
local numero3 = { valor = 15 }

setmetatable(numero1, {
    __le = function(n1, n2)
        return n1.valor <= n2.valor
    end
})

-- Ahora se compara el valor dentro de las tablas
print("Número1 es menor o igual a Número2:", numero1.valor <= numero2.valor) -- Imprime: Número1 es menor o igual a Número2: false
print("Número1 es menor o igual a Número3:", numero1.valor <= numero3.valor) -- Imprime: Número1 es menor o igual a Número3: true

print("\n10. Metamétodo __lt (menor que)")
local numero1 = { valor = 10}
local numero2 = { valor = 5 }
local numero3 = { valor = 15 }

setmetatable(numero1, {
    __lt = function(n1, n2)
        return n1 < n2
    end
})

print("Número1 es menor que Número2:", numero1.valor < numero2.valor) -- Imprime: Número1 es menor que Número2: false
print("Número1 es menor que Número3:", numero1.valor < numero3.valor) -- Imprime: Número1 es menor que Número3: true

print("\n11. Metamétodo __gt (mayor que)")
local numero1 = { valor = 10}
local numero2 = { valor = 5 }
local numero3 = { valor = 15 }

setmetatable(numero1, {
    __gt = function(n1, n2)
        return n1 > n2
    end
})

print("Número1 es mayor que Número2:", numero1.valor > numero2.valor) -- Imprime: Número1 es mayor que Número2: true
print("Número1 es mayor que Número3:", numero1.valor > numero3.valor) -- Imprime: Número1 es mayor que Número3: false

print("\n12. Metamétodo __ge (mayor o igual)")
local numero1 = { valor = 10}
local numero2 = { valor = 5 }
local numero3 = { valor = 15 }

setmetatable(numero1, {
    __ge = function(n1, n2)
        return n1 >= n2
    end
})

print("Número1 es mayor o igual a Número2:", numero1.valor >= numero2.valor) -- Imprime: Número1 es mayor o igual a Número2: true
print("Número1 es mayor o igual a Número3:", numero1.valor >= numero3.valor) -- Imprime: Número1 es mayor o igual a Número3: false
