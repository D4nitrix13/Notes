-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me 

-- Calcula el tiempo UNIX (número de segundos desde la época) para la fecha proporcionada en la tabla
local pasado = os.time({
    year = 2005,
    month = 12,
    day = 13,
    hour = 23,
    min = 30,
    sec = 18
})

-- Imprime el tiempo UNIX actual
print("os.time() -> " .. os.time())

-- Calcula la diferencia de tiempo entre el tiempo actual y el tiempo 'pasado' en segundos
print("os.time() - pasado -> " .. os.time() - pasado)

-- Calcula la diferencia de tiempo entre el tiempo actual y el tiempo 'pasado' en segundos (otra forma de hacerlo)
print("os.difftime(os.time(), pasado) -> " .. os.difftime(os.time(), pasado))

-- Imprime la fecha y hora actual formateada según el formato predeterminado
print(os.date())

-- Obtiene el año de la fecha 'pasado' utilizando la función os.date
local ano_pasado = tonumber(os.date("%Y", pasado))
print(ano_pasado) -- Esto imprimirá el año (year) de la variable 'pasado'
