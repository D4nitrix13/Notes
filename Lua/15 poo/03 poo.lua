-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me

--[[
    Abstracción:

    La abstracción implica ocultar los detalles internos y mostrar solo las operaciones relevantes. En este ejemplo, creamos una clase "Forma" que define un método abstracto "calcularArea". Las clases derivadas como "Rectangulo" y "Circulo" implementan este método de acuerdo con su propia lógica.
]]

-- Definición de la clase abstracta "Forma"
local Forma = {}

-- Método abstracto para calcular el área
function Forma:calcularArea()
    error("Método abstracto 'calcularArea' no implementado")
end

-- Definición de la clase "Rectangulo" que hereda de "Forma"
local Rectangulo = {}
Rectangulo.__index = Rectangulo
setmetatable(Rectangulo, Forma)

-- Método para calcular el área de un rectángulo
function Rectangulo:calcularArea()
    return self.ancho * self.altura
end

-- Crear instancia de Rectangulo
local miRectangulo = setmetatable({ ancho = 5, altura = 10 }, Rectangulo)

-- Mostrar el área del rectángulo
print("Área del rectángulo:", miRectangulo:calcularArea())

-- Definición de la clase "Circulo" que hereda de "Forma"
local Circulo = {}
Circulo.__index = Circulo
setmetatable(Circulo, Forma)

-- Método para calcular el área de un círculo
function Circulo:calcularArea()
    return math.pi * self.radio ^ 2
end

-- Crear instancia de Circulo
local miCirculo = setmetatable({ radio = 3 }, Circulo)

-- Mostrar el área del círculo
print("Área del círculo:", miCirculo:calcularArea())
print(3 ^ 2)
