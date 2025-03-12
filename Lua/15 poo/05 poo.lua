-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me

--[[
Polimorfismo:

El polimorfismo permite que objetos de diferentes clases sean tratados de manera uniforme. En este ejemplo, tenemos una clase "Animal" con un método "hacerSonido", y las clases derivadas "Perro" y "Gato" implementan este método de manera diferente.
]]

-- Definición de la clase "Animal"
local Animal = {}

-- Método para hacer sonido (método polimórfico)
function Animal:hacerSonido()
    error("Método 'hacerSonido' no implementado")
end

-- Definición de la clase "Perro" que hereda de "Animal"
local Perro = {}
Perro.__index = Perro
setmetatable(Perro, Animal)

-- Método para hacer ladrido
function Perro:hacerSonido()
    print("¡Guau Guau!")
end

-- Definición de la clase "Gato" que hereda de "Animal"
local Gato = {}
Gato.__index = Gato
setmetatable(Gato, Animal)

-- Método para hacer maullido
function Gato:hacerSonido()
    print("¡Miau!")
end

-- Crear instancia de Perro y Gato
local miPerro = Perro
local miGato = Gato

-- Hacer que los animales hagan sonidos
miPerro:hacerSonido()
miGato:hacerSonido()
