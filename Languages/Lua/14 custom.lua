-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me

-- Se importa el módulo local "module" desde el fichero "module.lua"
local modulo = require("./module")

-- Se llama a la función "sumar" del módulo importado y se pasan los números del 1 al 10 como argumentos
-- La función "sumar" está definida en el módulo "module.lua" y suma todos los argumentos que recibe
print(modulo.sumar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
