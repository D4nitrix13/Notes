#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout
from typing import List

# Lista de precios que son considerados caros
expensive: List[int] = [32, 20]

# Suma de los elementos en la lista 'expensive' con un valor inicial de 0
totalSum: int = sum(expensive, start=0)

# Imprime la suma total de los elementos en la lista
print(totalSum, end="\n", file = stdout)  # Esto imprimirá: 52
