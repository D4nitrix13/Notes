-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me

-- Definición de una tabla "T" con datos de una persona -> Simulando una clase
local T = {
    name = "Daniel Benjamin Perez Morales",
    age = "18",
    lista = {"messi", "ronaldo"}
}

local clase_ejemplo = T
print(clase_ejemplo.name)
print(clase_ejemplo.age)
print(table.concat(clase_ejemplo.lista,", "))

-- Definición de una función "mascotaClase" que crea instancias de mascotas
local function mascotaClase(name)
    -- Si no se proporciona un nombre, se asigna "batman" por defecto
    name = name or "batman"
    return {
        name = name, -- Nombre de la mascota
        status = "hungry", -- Estado de alimentación inicial
        -- Método para alimentar a la mascota y cambiar su estado a "full"
        alimentar = function(self)
            self.status = "full"
        end
    }
end

-- Crear una instancia de mascota con el nombre "coby"
local dog = mascotaClase("coby")

-- Imprimir el estado inicial de la mascota
print(dog.status) -- Imprime "hungry"

-- Alimentar a la mascota
dog:alimentar()

-- Imprimir el estado de la mascota después de alimentarla
print(dog.status) -- Imprime "full"

--[[
    En Lua, los índices de las tablas comienzan en 1, no en 0 como en algunos otros lenguajes de programación. Por lo tanto, t.lista[0] intenta acceder al primer elemento de la tabla lista, pero como los índices comienzan en 1, esto devuelve nil, indicando que no hay ningún valor en la posición 0.

    Para acceder al primer elemento de la tabla lista, debes usar el índice 1:
]]