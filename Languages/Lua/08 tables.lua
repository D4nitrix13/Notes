-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me 

--[[
En Lua, los índices de las tablas comienzan en 1, no en 0 como en algunos otros lenguajes de programación. Por lo tanto, t.lista[0] intenta acceder al primer elemento de la tabla lista, pero como los índices comienzan en 1, esto devuelve nil, indicando que no hay ningún valor en la posición 0.

Para acceder al primer elemento de la tabla lista, debes usar el índice 1:
]]
-- Creación de una tabla vacía
local lista = {} 
print("Tabla creada:", lista) -- Muestra la tabla creada

-- Añadir datos a una lista
local valor = "Daniel"
table.insert(lista, valor) 
print("Elemento añadido:", valor) -- Muestra el elemento añadido a la lista

-- Ejemplo práctico: Guardar nombres de usuarios
table.insert(lista, "Carol")
print("Elemento añadido:", "Laura")
table.insert(lista, "Sixdally")
print("Elemento añadido:", "Sixdally")

-- Eliminar elementos de la lista
local indice = 1
local eliminado = table.remove(lista, indice) 
print("Elemento eliminado:", eliminado) -- Muestra el elemento eliminado de la lista

-- Ejemplo práctico: Eliminar el primer usuario registrado
eliminado = table.remove(lista, 1)
print("Elemento eliminado:", eliminado)

-- Definición de una lista
local lista = {10, 20, 30, 40, 50}
print("acceder al primer elemento de la lista\nlista[1] = " .. lista[1])
-- Eliminar el último elemento de la lista
local indice = #lista
local eliminado = table.remove(lista, indice)

-- Imprimir el elemento eliminado y la lista actualizada
print("Elemento eliminado:", eliminado)
print("Lista actualizada:")
for indice, valor in ipairs(lista) do
    print(indice, valor)
end

-- Insertar elementos en la lista
indice = 2
valor = "Ruby"
table.insert(lista, indice, valor) 
print("Elemento insertado en la posición", indice, ":", valor)

-- Borrar todos los elementos de la lista
lista = {}
print("Todos los elementos han sido borrados") 

-- Lista bidimensional
local matriz = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
} 
print("Matriz bidimensional creada\nImprimr matriz bidimensional") 
for index, value in ipairs(matriz) do
    print(table.concat(value,","))
end

-- Concatenar tablas
local lista1 = {1, 2, 3}
local lista2 = {4, 5, 6}
local lista_concatenada = {} 
for _, v in ipairs(lista1) do
    table.insert(lista_concatenada, v)
end

for _, v in ipairs(lista2) do
    table.insert(lista_concatenada, v)
end
print("Listas concatenadas") 

-- Ordenar elementos de la lista
table.sort(lista) 
print("Elementos de la lista ordenados") 

-- Iterar sobre una lista e imprimir los elementos
for indice, valor in ipairs(lista) do
    print("Índice:", indice, "Valor:", valor)
end

-- Definición de una lista
local lista = {"Manzana", "Mango", "Cereza", "Uva"}

-- Concatenar los elementos de la lista en una cadena separada por comas
local lista_concatenada = table.concat(lista, ", ")

-- Imprimir la lista concatenada
print("Elementos de la lista:", lista_concatenada)

-- Definición de una tabla diccionarios
local t = {nombre = "Daniel", edad = 18, ciudad = "Madrid"}

-- Iterar sobre la tabla e imprimir las claves y valores
print("Iteración sobre la tabla:")
for key, value in pairs(t) do
    print("Clave:", key, "Valor:", value)
end

-- Añadir un nuevo elemento a la tabla
print("\nAñadir un nuevo elemento a la tabla:")
t.telefono = "123456789"
for key, value in pairs(t) do
    print("Clave:", key, "Valor:", value)
end

-- Eliminar un elemento de la tabla
print("\nEliminar un elemento de la tabla:")
t.edad = nil
for key, value in pairs(t) do
    print("Clave:", key, "Valor:", value)
end

-- Insertar un elemento en una clave específica
print("\nInsertar un elemento en una clave específica:")
t.edad = 25
for key, value in pairs(t) do
    print("Clave:", key, "Valor:", value)
end

-- Borrar todos los elementos de la tabla
print("\nBorrar todos los elementos de la tabla:")
for key, _ in pairs(t) do
    t[key] = nil
end

for key, value in pairs(t) do
    print("Clave:", key, "Valor:", value)
end


local t = {10, 20, 30, [5] = 50, ["key"] = "value"}

-- ipairs solo itera sobre claves numéricas
print("ipairs(t)")
for index, value in ipairs(t) do
    print(index, value)
end

-- pairs itera sobre todas las claves y valores de una tabla
print("pairs(t)")
for key, value in pairs(t) do
    print(key, value)
end

--[[
La diferencia principal entre pairs e ipairs en Lua radica en cómo iteran sobre una tabla y qué tipos de claves consideran.

    pairs: Esta función itera sobre todas las claves y valores de una tabla, sin importar si las claves son índices numéricos o no. Itera sobre todas las claves y valores de una tabla en un orden arbitrario.

    ipairs: Esta función está diseñada específicamente para iterar sobre las claves numéricas de una tabla que se comporta como un array. Solo itera sobre las claves numéricas y sus valores asociados en orden secuencial, comenzando desde 1 y avanzando hasta el final del array. Cuando encuentra una clave no numérica, como una clave de cadena o cualquier otro tipo, detiene la iteración.

En resumen:

    pairs itera sobre todas las claves y valores de una tabla, independientemente de su tipo y orden.
    ipairs itera solo sobre las claves numéricas y valores asociados en un array, en orden secuencial.
]]
-- pairs itera sobre todas las claves


-- En Lua, no hay una distinción clara entre diccionarios y listas; las tablas pueden ser utilizadas para ambos propósitos. Dependiendo de cómo se utilice, una tabla puede comportarse como un array (lista) o un diccionario. En este caso, t actúa como un diccionario debido a la naturaleza de las claves y los valores.

-- Explicaciones de las funciones utilizadas:

--[[
    table.insert:
    La función table.insert(lista, valor) agrega el valor proporcionado al final de la lista.

    table.insert:
    La función table.insert(lista, indice, valor) inserta el valor proporcionado en la posición especificada en la lista.

    table.remove:
    La función table.remove(lista, indice) elimina el elemento en la posición indicada de la lista y devuelve dicho elemento.

    ipairs:
    La función ipairs(lista) itera sobre los pares (índice, valor) en la lista proporcionada.

    table.sort:
    La función table.sort(lista) ordena los elementos de la lista en orden ascendente.

    table.concat:
    La función table.concat(lista, sep) concatena todos los elementos de la lista en una cadena, utilizando el separador proporcionado.
]]--
