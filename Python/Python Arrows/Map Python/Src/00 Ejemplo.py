#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout
from typing import Iterable, List

# Lista de precios en formato string con el símbolo '$'
dollars: List[str] = ['32$', '15$', '12$', '17$', '20$']

# Utilizando map con una función lambda para convertir los precios a enteros
# Esta línea devuelve un generador de tipo <map object at 0x...>
priceGenerator: Iterable[int] = map(lambda dollar: int(dollar[0:-1:1]), dollars)
print(priceGenerator, end="\n", file = stdout)  # Esto imprimirá: <map object at 0x...>

# Convertir el generador a una lista para obtener los precios como enteros
prices: List[int] = list(priceGenerator)
print(prices, end="\n", file = stdout)  # Esto imprimirá: [32, 15, 12, 17, 20]
