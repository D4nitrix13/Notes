#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout
from typing import List, Callable

# Lista de precios en formato de cadena con el símbolo de dólar
dollars: List[str] = ['32$', '15$', '12$', '17$', '20$']

def map(iterable: List[str], func: Callable[[str], int]) -> List[int]:
    """
    Aplica una función a cada elemento de un iterable y devuelve una lista de resultados.

    :param iterable: Lista de cadenas a transformar.
    :param func: Función que transforma una cadena en un entero.
    :return: Lista de enteros transformados.
    """
    mapped: List[int] = list()
    for e in iterable:
        mapped.append(func(e))
    return mapped
    # * forma simplificada con list comprehension
    # return [func(e) for e in iterable]

def filter(iterable: List[int], func: Callable[[int], bool]) -> List[int]:
    """
    Filtra los elementos de un iterable aplicando una función de criterio.

    :param iterable: Lista de enteros a filtrar.
    :param func: Función que determina si un entero debe ser incluido.
    :return: Lista de enteros que cumplen con el criterio de la función.
    """
    filtered: List[int] = list()
    for e in iterable:
        # La misma lógica se puede expresar como:
        # if (func(e) == True): filtered.append(e)
        if func(e):
            filtered.append(e)
    return filtered
    # con list comprehension
    # return [int(e) for e in iterable if func(e)]

def reduce(iterable: List[int], func: Callable[[int, int], int], acum: int = 0) -> int:
    """
    Aplica una función de acumulación a los elementos de un iterable, reduciéndolos a un solo valor.

    :param iterable: Lista de enteros a reducir.
    :param func: Función de acumulación que combina dos enteros en uno.
    :param acum: Valor inicial de acumulación.
    :return: Entero resultante de la reducción.
    """
    for e in iterable:
        acum = func(acum, e)
    return acum

# Aplicar map para convertir los precios de cadena a enteros eliminando el símbolo de dólar
prices: List[int] = map(iterable=dollars, func=lambda dollar: int(dollar[0:-1:1]))

# Filtrar los precios que son mayores o iguales a 20
expensive: List[int] = filter(iterable=prices, func=lambda price: price >= 20)

# Reducir la lista de precios filtrados sumándolos
total: int = reduce(iterable=expensive, func=lambda acum, price: acum + price, acum=0)

# Imprimir el resultado final
print(total, end="\n", file = stdout)  # Esto imprimirá: 52
