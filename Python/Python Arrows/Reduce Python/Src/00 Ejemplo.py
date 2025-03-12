#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout
from typing import List
from functools import reduce

# Lista de precios que son considerados caros
expensive: List[int] = [32, 20]

# Calcula la suma total de los elementos en la lista 'expensive' usando 'reduce'
# La función 'reduce' toma una función lambda y aplica acumulativamente la operación a los elementos de la lista
# La función lambda toma dos argumentos: 'acum' y 'price', y devuelve la suma de ambos
totalSum: int = reduce(lambda acum, price: acum + price, expensive)

# Imprime la suma total de los elementos en la lista
print(totalSum, end="\n", file = stdout)  # Esto imprimirá: 52
