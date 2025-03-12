-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me

-- Definición de una clase "Persona"
local Persona = {
    nombre = "", -- Atributo para almacenar el nombre de la persona
    edad = 0,    -- Atributo para almacenar la edad de la persona
}

-- Método para inicializar una nueva instancia de Persona
function Persona:nuevo(nombre, edad)
    local obj = {}          -- Crea un nuevo objeto vacío
    setmetatable(obj, self) -- Establece la metatabla del objeto como la clase Persona
    self.__index = self     -- Establece el índice de la clase Persona a sí misma para la herencia
    obj.nombre = nombre     -- Asigna el nombre pasado como argumento al atributo nombre del objeto
    obj.edad = edad         -- Asigna la edad pasada como argumento al atributo edad del objeto
    return obj              -- Devuelve el objeto creado
end

-- Método para imprimir los datos de una persona
function Persona:mostrarDatos()
    print("Nombre:", self.nombre) -- Imprime el nombre del objeto actual
    print("Edad:", self.edad)     -- Imprime la edad del objeto actual
end

-- Crear una nueva instancia de Persona
local persona1 = Persona:nuevo("Daniel", 18)

-- Llamar al método para mostrar los datos de la persona
persona1:mostrarDatos() -- Imprime los datos de la persona1
