#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout
from typing import List, Callable, TypeVar, Union, Any, Iterator

# Datos de ejemplo
dollars: List[str] = ['32$', '15$', '12$', '17$', '20$']

# Tipos genéricos
E = TypeVar("E")  # Tipo de elemento en la lista
R = TypeVar("R")  # Tipo de retorno de la función
A = TypeVar("A")  # Tipo acumulado para reduce

# Función map genérica
def map(iterable: List[E], func: Callable[[E], R]) -> Iterator[R]:
    mapped: List[R] = []
    for e in iterable:
        mapped.append(func(e))
    return iter(mapped)
    # * Implementación utilizando comprensión de listas
    # return (func(e) for e in iterable)


# Función filter genérica
def filter(iterable: Iterator[E], func: Callable[[E], bool]) -> Iterator[E]:
    filtered: List[E] = list()
    for e in iterable:
        if func(e):
            filtered.append(e)
    return iter(filtered)
    # * Implementación utilizando comprensión de listas
    # return (e for e in iterable if func(e))


# Función reduce genérica
def reduce(iterable: List[E], func: Callable[[A, E], A], acum: Union[A, Any] = 0) -> A:
    for e in iterable:
        acum = func(acum, e)
    return acum

# Aplicar map para convertir los precios de cadena a enteros eliminando el símbolo de dólar
prices: Iterator[int] = map(iterable=dollars, func=lambda dollar: int(dollar[0:-1:1]))

# Filtrar los precios que son mayores o iguales a 20
expensive: Iterator[int] = filter(iterable=prices, func=lambda price: price >= 20)

# Convertir expensive a una lista antes de imprimir
expensive_list: List[int] = list(expensive)
print(f"Precios caros: {expensive_list}", end="\n", file = stdout)  # Esto imprimirá: Precios caros: [32, 20]

# Reducir la lista de precios filtrados sumándolos
total: int = reduce(iterable=expensive_list, func=lambda acum, price: acum + price, acum=0)

# Imprimir el resultado final
print(f"Total: {total}", end="\n", file = stdout)  # Esto imprimirá: Total: 52
