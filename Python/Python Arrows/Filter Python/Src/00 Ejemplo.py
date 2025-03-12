#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout
from typing import List

# Lista de precios en formato entero
prices: List[int] = [32, 15, 12, 17, 20]

# Utilizando filter con una función lambda para seleccionar precios mayores o iguales a 20
# Esta línea devuelve un generador de tipo <filter object at 0x...>
priceFilter = filter(lambda price: price >= 20, prices)
print(priceFilter, end="\n", file = stdout)  # Esto imprimirá: <filter object at 0x...>

# Convertir el generador a una lista para obtener los precios filtrados
expensive: List[int] = list(priceFilter)
print(expensive, end="\n", file = stdout)  # Esto imprimirá: [32, 20]