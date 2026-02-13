-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me 

-- Lista de números
local lista = {1, 2, 3, 4, 5}
local indice = 1

-- Ejemplo de bucle 'while':
-- Itera sobre la lista mientras el índice sea menor o igual al tamaño de la lista
-- e imprime cada elemento de la lista
while indice <= #lista do
    print("Bucle 'while':", lista[indice])
    indice = indice + 1
end

-- Lista de números
lista = {1, 2, 3, 4, 5}

-- Ejemplo de bucle 'for':
-- Itera sobre la lista en incrementos de 2 y imprime cada elemento correspondiente
for indice = 1, #lista, 2 do
    print("Bucle 'for':", lista[indice])
end

-- Lista de números
lista = {10, 7, 4, 1}

-- Ejemplo de bucle 'for' con condición inversa:
-- Itera sobre la lista en decrementos de 3 y imprime cada tercer elemento en orden inverso
for indice = #lista, 1, -3 do
    print("Bucle 'for' con condición inversa:", lista[indice])
end

-- Lista de números
lista = {2, 4, 6, 8}

-- Ejemplo de bucle 'for' para modificar la lista:
-- Multiplica cada elemento de la lista por 5
for indice = 1, #lista do
    lista[indice] = lista[indice] * 5
end

-- Impresión de la lista modificada
for indice = 1, #lista do
    print("Lista modificada por el bucle 'for':", lista[indice])
end

-- Lista de números
lista = {3, 6, 9, 12}
indice = 1

-- Ejemplo de bucle 'repeat until':
-- Itera sobre la lista e imprime cada elemento
-- La condición se evalúa al final del bucle, por lo que se ejecuta al menos una vez
repeat
    print("Bucle 'repeat until':", lista[indice])
    indice = indice + 1
until not (indice <= #lista)  -- La negación de la condición asegura que el bucle se detenga cuando el índice sea mayor que el tamaño de la lista

-- Lista de números
local lista = {3, 6, 9, 12 ,15}
local indice = 1

-- Ejemplo de bucle 'while' con doble condición:
-- Itera sobre la lista mientras el índice sea menor o igual al tamaño de la lista
-- y el valor del elemento actual sea divisible entre 3
while indice <= #lista and lista[indice] % 3 == 0 do
    print("Bucle 'while' con doble condición:", lista[indice])
    indice = indice + 1
end
