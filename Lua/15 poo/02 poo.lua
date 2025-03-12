-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me

-- Definición de la clase "Animal"
local Animal = {
    nombre = "",
    sonido = "",
}

-- Método para inicializar una nueva instancia de Animal
function Animal:nuevo(nombre, sonido)
    local obj = {}
    setmetatable(obj, self)
    self.__index = self
    obj.nombre = nombre
    obj.sonido = sonido
    return obj
end

-- Método para imprimir los datos de un animal
function Animal:mostrarDatos()
    print("Nombre:", self.nombre)
    print("Sonido:", self.sonido)
end

-- Definición de la clase "Perro" que hereda de "Animal" (herencia simple)
local Perro = Animal:nuevo()

-- Método específico para ladrar
function Perro:ladrar()
    print(self.nombre .. " dice: ¡Guau Guau!")
end

-- Definición de la clase "Gato" que hereda de "Animal" (herencia simple)
local Gato = Animal:nuevo()

-- Método específico para maullar
function Gato:maullar()
    print(self.nombre .. " dice: ¡Miau!")
end

-- Definición de la clase "Ave" que hereda de "Animal" (herencia simple)
local Ave = Animal:nuevo()

-- Método específico para volar
function Ave:volar()
    print(self.nombre .. " está volando.")
end

-- Definición de la clase "Perico" que hereda de "Ave" (herencia jerárquica)
local Perico = Ave:nuevo()

-- Método específico para hablar
function Perico:hablar()
    print(self.nombre .. " dice: ¡Hola!")
end

-- Definición de la clase "Pato" que hereda de "Ave" (herencia jerárquica)
local Pato = Ave:nuevo()

-- Método específico para nadar
function Pato:nadar()
    print(self.nombre .. " está nadando.")
end

-- Definición de la clase "SuperPerro" que hereda de "Perro" y "Ave" (herencia múltiple)
local SuperPerro = Perro:nuevo()

-- Método específico para volar
function SuperPerro:volar()
    print(self.nombre .. " está volando como un superperro.")
end

-- Crear instancias de las clases y llamar a sus métodos
local miPerro = Perro:nuevo("Rex", "Woof")
local miGato = Gato:nuevo("Whiskers", "Meow")
local miPerico = Perico:nuevo("Perry", "Tweet")
local miPato = Pato:nuevo("Donald", "Quack")
local miSuperPerro = SuperPerro:nuevo("SuperRex", "Woof")

-- Mostrar datos y acciones de los animales
miPerro:mostrarDatos()
miPerro:ladrar()

miGato:mostrarDatos()
miGato:maullar()

miPerico:mostrarDatos()
miPerico:volar()
miPerico:hablar()

miPato:mostrarDatos()
miPato:volar()
miPato:nadar()

miSuperPerro:mostrarDatos()
miSuperPerro:ladrar()
miSuperPerro:volar()

--[[
    Este código define varias clases que representan diferentes tipos de animales y sus características. Aquí tienes una explicación detallada:

    La clase base "Animal" tiene atributos para el nombre y el sonido del animal, así como un método para mostrar sus datos.
    Se definen clases derivadas como "Perro", "Gato" y "Ave", que heredan de "Animal" utilizando herencia simple. Cada una de estas clases define métodos específicos para las acciones típicas de esos animales.
    Se define la clase "Perico" que hereda de "Ave" y la clase "Pato" que también hereda de "Ave". Esto representa una herencia jerárquica donde ambas clases derivadas comparten la misma clase base.
    Se define la clase "SuperPerro" que hereda tanto de "Perro" como de "Ave", lo que representa herencia múltiple. Esta clase tiene acceso a métodos tanto de "Perro" como de "Ave".
    Se crean instancias de cada clase y se llaman a sus métodos para demostrar la herencia y el polimorfismo en acción.
]]